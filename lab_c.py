from bs4 import BeautifulSoup
import webbrowser
from ciscoconfparse import CiscoConfParse
from ciscoconfparse.ccp_util import IPv4Obj

def parseIP(conf):

	parse = CiscoConfParse(conf, factory=True)

	ip_add = []

	interfaces = parse.find_objects(r"^interf")

	for e in interfaces:
		IPv4_REGEX = r"ip\saddress\s(\S+\s+\S+)"
		for cmd in e.re_search_children(IPv4_REGEX):
			ipv4_addr = e.re_match_iter_typed(IPv4_REGEX, result_type=IPv4Obj)
			ip_add.append(ipv4_addr.ip.exploded)

	return(ip_add)


def parseHost(conf):

	host = []

	parse = CiscoConfParse(conf)
	
	hostnames = parse.find_objects(r"^hostname")
	
	for hostname in hostnames:
		hostname = hostname.replace(r'hostname\s', r'')
		host.append(hostname)

	return(hostname)


def generateHtml(conf):
	
	html_template = '''
	<html>
	<head>
 	<title>Infotabell</title>
 	<style>
   	table, th, td {border: solid 1px black;}
   	th, td {padding: 5px;}
   	table {border-collapse: collapse;}
 	</style>
	</head>
	<body>
	<h1>Routerinformation</h1>
	<table>
 	<tr>
  	<td>Namn</td><td id="namn">xxx</td>
 	</tr>
 	<tr>
  	<td>IP-nummer</td><td id="ip">allaipnummer</td>
 	</tr>
	</table>
	</body>
	</html>
	'''

	soup = BeautifulSoup(html_template, 'html.parser')
	soup.find(id='namn').string = parseHost(conf)
	soup.find(id='ip').string = parseIP(conf)

	FILE = 'Lab_3_Infotabell.html'

	FILNAMN = 'infotabell.html'

	out =  open(FILNAMN,'w')
	out.write(soup.prettify())
	out.close()

	# Säg till systemets webbläsare att öppna filen
	# Man måste ha en absolut sökväg till html-filen här

	webbrowser.open('file:Users/yaggen/Desktop/python/hv-pyscheme/Lab/'+FILNAMN)

conf = "router_configuration.txt"
generateHtml(conf)


