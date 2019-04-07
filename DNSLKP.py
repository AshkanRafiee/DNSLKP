import socket
import sys
 
try:
  host = sys.argv[1]
  print "Domain",host
  print "IP",socket.gethostbyname(host)
  dns = socket.gethostbyaddr(host)
  for c in dns:
     print "DNS Server = ",c
except:
  print "Error! Check Internet Connection or Syntax! Or Maybe Site Is SuperSecure @!"
  print "Syntax : DNSLKP.py example.com"