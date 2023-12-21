from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8000


class Handler(SimpleHTTPRequestHandler):
    def send_error(self, code, message=None):
        if code == 404:
            with open("404.html", "rb") as err_msg:
                page404 = err_msg.read()

            self.send_response(code)
            self.send_header("Connection", "close")
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(page404)))
            self.end_headers()
            self.wfile.write(page404)
        else:
            SimpleHTTPRequestHandler.send_error(self, code, message)


Handler.extensions_map={
    '.manifest': 'text/cache-manifest',
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.svg':	'image/svg+xml',
    '.css':	'text/css',
    '.js':	'application/x-javascript',
    '': 'application/octet-stream', # Default
    }

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("", PORT), Handler)

httpd.serve_forever()
