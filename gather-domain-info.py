#!/usr/bin/python3

import sys,whois,socket,dns.resolver
from termcolor import colored

if len(sys.argv) != 2:
	exit('Usage: gather-domain-info.py domain.ext\n')

w = whois.whois(sys.argv[1])
ip = socket.gethostbyname((sys.argv[1]))

print('Domain: ' + colored(str(sys.argv[1]), 'green') + '\n')
print('Registrar: ' + colored(str(w.registrar) + ' - ' +str(w.registrar_name), 'green') + '\n') 
print('Expiration date: ' + colored(str(w.expiration_date), 'green') + '\n')
print('Authoritative name server:\n' + colored(str(w.name_servers), 'green') + '\n')
print('DNS Lookup: www.' + str(sys.argv[1]) + ' points to: ' + colored(socket.gethostbyname('www.' +str(sys.argv[1])), 'green'))
print('DNS Lookup: ' + str(sys.argv[1]) + ' points to: ' + colored(socket.gethostbyname(str(sys.argv[1])), 'green') + '\n')
print('Mail Routing:\n')
mx = dns.resolver.query(sys.argv[1], 'MX')
for rdata in mx:
    print('MX:', colored(rdata.exchange, 'green'), 'priority:', colored(rdata.preference, 'green'))
# Common third domain level for mail services
mailservices = [ 'mail.' ]
mailservicesip = []

for item in mailservices:
        if socket.gethostbyname(str(item) + str(sys.argv[1])):
                mailservicesip.append(socket.gethostbyname(str(item) + str(sys.argv[1])))

for x in mailservicesip:
	if str(ip) != str(x):
		print(colored('NOTICE: mail services seem hosted on: ' + str(x), 'red'))
		exit('\nFinished.\n')
	else:
		print('\nThis domain seems hosted on server: ' + colored(str(socket.gethostbyaddr(ip)[0]), 'green'))
print('\nFinished.\n')
