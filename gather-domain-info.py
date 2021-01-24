#!/usr/bin/python3

import sys,whois,socket,dns.resolver
from termcolor import colored

if len(sys.argv) != 2:
	exit('Usage: gather-domain-info.py domain.ext\n')

w = whois.whois(sys.argv[1])
ip = socket.gethostbyname((sys.argv[1]))

print('Domain: ' + colored(str(w.domain_name), 'green') + '\n')
print('Expiration date: ' + colored(str(w.expiration_date), 'green') + '\n')
print('Authoritative name server:\n' + colored(str(w.name_servers), 'green') + '\n')
print('DNS Lookup: www.' + str(w.domain_name) + ' points to: ' + colored(socket.gethostbyname('www.' +str(w.domain_name)), 'green'))
print('DNS Lookup: ' + str(w.domain_name) + ' points to: ' + colored(socket.gethostbyname(str(w.domain_name)), 'green') + '\n')
print('Mail Routing:\n')
mx = dns.resolver.query(w.domain_name, 'MX')
for rdata in mx:
    print('MX:', colored(rdata.exchange, 'green'), 'priority:', colored(rdata.preference, 'green'))
print('\nThis domain seems hosted on server: ' + colored(str(socket.gethostbyaddr(ip)[0]), 'green'))
