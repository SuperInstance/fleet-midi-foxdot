"""FoxDot bridge — live coding patterns for fleet agents."""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class FoxDotHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        code = body.get('code', 'Clock.clear()')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({"status":"ok","foxdot_code":code}).encode())

if __name__ == '__main__':
    HTTPServer(('', 3007), FoxDotHandler).serve_forever()
