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

	interfaces = parse.find_objects(r"^interface ")

	for interface in interfaces:
		intf_list.append(interface.text)
		if interface in parse.find_objects_w_child('^interface', '^\s+no ip address'):
			intf_list.remove(interface.text)


	return(intf_list)

def parseConf(conf):

	f = open(conf,'r')
	for line in f:
		if "Last configuration" in line:
			last_change = line
        
	conf_change = last_change[31:58]


	return(conf_change)



def parseHost(conf):

	host = []

	parse = CiscoConfParse(conf)
	
	hostnames = parse.find_objects(r"^hostname")
	
	for hostname in hostnames:
		hostname = hostname.replace(r'hostname\s', r'')
		host.append(hostname)

	return(host)

def parseVersion(version):

	f = open(version,'r')
	for line in f:
		if "uptime" in line:
			uptime = line
		if "ROM:" in line:
			rom = line

	rom_ver = rom[23:]
	uptime = uptime[15:]
	return rom_ver,uptime

def generateHtml(conf, ver):
	
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
  	<td>Namn & Last Change</td><td id="namn">xxx</td><td>LastChange</td>
 	</tr>
 	<tr>
  	<td>Interface & IP-nummer</td><td id="interface">interface</td> <td id ="ip">allaipnummer</td>
 	</tr>
	</table>
	<table>
	<tr>
	<td>Rom version:</td><td id="ROM">ROM_VER</td></tr>
	<br>
	<tr>
	<td>Uptime:</td><td id="Uptime">UPTIME</td>
	</tr>
	</body>
	</html>
	'''

	soup = BeautifulSoup(html_template, 'html.parser')
	
	#soup.find(id='namn').string = parseHost(conf)

	FILNAMN = 'Lab_3_Infotabell.html'

	out =  open(FILNAMN,'w')
	out.write(soup.prettify())
	out.close()

	host = parseHost(conf)[0]
	ips = '<br>'.join(parseIP(conf))
	intf = '<br>'.join(parseIntf(conf))
	lastChange = parseConf(conf)
	rom_ver, uptime = parseVersion(ver)

	with open(FILNAMN, 'r') as file :
		filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('allaipnummer',ips)
	filedata = filedata.replace('interface', intf)
	filedata = filedata.replace('LastChange',lastChange)
	filedata = filedata.replace('ROM_VER',rom_ver)
	filedata = filedata.replace('UPTIME',uptime)
	filedata = filedata.replace('xxx', host)

	# Write the file out again
	with open(FILNAMN, 'w') as file:
		file.write(filedata)



	webbrowser.open('file:Users/yaggen/Desktop/python/hv-pyscheme/Lab/'+FILNAMN)
    

conf = "router_configuration.txt"
version = "router_show_version.txt"
generateHtml(conf,version)
