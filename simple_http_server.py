import socketserver  
import http.server  
        
        
class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):  
    def do_GET(self):  
        if self.path == '/':  
            self.send_response(200)  
            self.send_header('Content-type', 'text/plain; charset=utf-8')  
            self.end_headers()  
            self.wfile.write(b'Hello World')  
        else:  
            self.send_error(404)  
        
        
if __name__ == '__main__':  
    PORT = 8000  
    handler = MyHttpRequestHandler  
    httpd = socketserver.TCPServer(("", PORT), handler)  
    print("Serving at port", PORT)  
    httpd.serve_forever() 
