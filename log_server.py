#!/usr/bin/env python3
"""
Simple HTTP log server for PS4 logs
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "ps4_logs.txt")

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/log' or self.path == '/_log':
            # Get content length
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8', errors='ignore')

            # Print with timestamp
            timestamp = datetime.now().strftime('%H:%M:%S')
            line = f"[{timestamp}] {body}"
            print(line)

            # Save to file
            with open(LOG_FILE, 'a') as f:
                f.write(line + '\n')

            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'ok')
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        # Suppress default HTTP logs
        pass

def main():
    server = HTTPServer(('0.0.0.0', 8082), LogHandler)
    print("[*] Log server listening on http://0.0.0.0:8082")
    print("[*] Waiting for logs from PS4...\n")
    server.serve_forever()

if __name__ == '__main__':
    main()
