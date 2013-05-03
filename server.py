#!/usr/bin/python
import webbrowser

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

new = 2

if sys.argv[1:]:
      port = int(sys.argv[1])
else:
      port = 9000
      server_address = ('127.0.0.1', port)

      HandlerClass.protocol_version = Protocol
      httpd = ServerClass(server_address, HandlerClass)

      sa = httpd.socket.getsockname()
      print "Serving HTTP on", sa[0], "port", sa[1], "..."
     #httpd.serve_forever()

# open a public URL, in this case, the webbrowser docs
url = 'http://localhost:' + sa[1]
webbrowser.open(url, new=new)
httpd.serve_forever()

