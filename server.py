#!/usr/bin/python
import webbrowser

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import time


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
      port = int(sys.argv[1])
else:
      port = 9000

server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()

print "Serving HTTP on", sa[0], "port", sa[1], "..."

url = 'http://localhost:' + str(sa[1])

webbrowser.open(url, new=1, autoraise=True)

httpd.serve_forever()