from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, unquote
import PortalConnection  # Assuming you have a database connection module for water fountains

hostName = "localhost"
serverPort = 1024

conn = PortalConnection.PortalConnection()  # Assuming you have a database connection object

class PortalServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        pth = self.path
        if pth == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(
             """
                <!doctype html>
                <html lang=\"en\">
                <head>
                  Water Fountains
                </head>
                </html>      
                 """, 
                 "utf-8"))
        
        else:
          self.send_response(404, message='Not Found')
          self.end_headers()
          

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), PortalServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
