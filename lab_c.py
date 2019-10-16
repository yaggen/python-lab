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


def parseIntf(conf):
	parse = CiscoConfParse(conf)

	intf_list = []

	interfaces = parse.find_objects(r"^interf ")

	for interface in interfaces:
		intf_list.append(interface)

	return(intf_list)

def parseHost(conf):

	host = []

	parse = CiscoConfParse(conf)
	
	hostnames = parse.find_objects(r"^hostname")
	
	for hostname in hostnames:
		hostname = hostname.replace(r'hostname\s', r'')
		host.append(hostname)

	return(host)


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
	
	#soup.find(id='namn').string = parseHost(conf)

	FILNAMN = 'Lab_3_Infotabell.html'

	out =  open(FILNAMN,'w')
	out.write(soup.prettify())
	out.close()

	with open(FILNAMN, 'r') as file :
		filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('allaipnummer', str(parseIP(conf)[0:3]))

	# Write the file out again
	with open(FILNAMN, 'w') as file:
		file.write(filedata)



	webbrowser.open('file:Users/yaggen/Desktop/python/hv-pyscheme/Lab/'+FILNAMN)
    

conf = "router_configuration.txt"
myIps = parseIP(conf)
host = parseHost(conf)

generateHtml(conf)

