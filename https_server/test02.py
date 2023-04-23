#
# https://www.lifewithpython.com/2021/03/python-https-server.html
#
# line:10 ssl.SSLError: [SSL] PEM lib (_ssl.c:3895)
#

import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
CERTFILE = "./dist/localhost.pem"

Handler = SimpleHTTPRequestHandler

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERTFILE)

with HTTPServer(("", PORT), Handler) as httpd:
	print("serving at address", httpd.server_address, "using cert file", CERTFILE)
	httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
	httpd.serve_forever()

