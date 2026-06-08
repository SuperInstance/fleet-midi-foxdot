"""FoxDot bridge — real-time Python live coding from fleet agent states.

FoxDot sends OSC to SuperCollider for immediate audio. This server
takes agent state data and generates FoxDot patterns in real time.
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

SCALES = {
    'major': [0,2,4,5,7,9,11], 'minor': [0,2,3,5,7,8,10],
    'pentatonic': [0,2,4,7,9], 'blues': [0,3,4,5,7,10],
}

def ternary_to_foxdot(ternary_vector, scale='major', root=0):
    """Convert ternary vector to FoxDot player code.
    
    +1 → high note (3rd of scale)
    0  → mid note (root of scale)
    -1 → low note (5th below)
    """
    s = SCALES.get(scale, SCALES['major'])
    lines = []
    base = root
    for v in ternary_vector:
        if v == 1:
            lines.append(f'p1 >> pluck({s[2] + base}, dur=1)')
            base += 1
        elif v == -1:
            lines.append(f'p2 >> bass({s[5] + base - 12}, dur=2)')
            base -= 1
        else:
            lines.append(f'p3 >> pads({s[0] + base}, dur=1)')
    return '\n'.join(lines)

class FoxDotHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        code = body.get('code', 'Clock.clear()')
        vector = body.get('ternary_vector', None)
        if vector:
            scale = body.get('scale', 'major')
            code = ternary_to_foxdot(vector, scale)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok", "foxdot_code": code}).encode())

if __name__ == '__main__':
    HTTPServer(('', 3007), FoxDotHandler).serve_forever()
