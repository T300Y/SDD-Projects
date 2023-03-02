#web server developed using Agile with more functionality at each live release

#set your local hosting parameters
hostName = "localhost"
serverPort = 8000

#import some standard libraries that handle HTTP requests
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        sendHTTPheaders(self)
        self.wfile.write(bytes("<h1>AgileWebServer2000</h1>","utf-8"))

def sendHTTPheaders(self):
    #send HTTP headers to the web browser
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

webServer = HTTPServer((hostName, serverPort), MyServer)
print("Serving from http://%s:%s" % (hostName, serverPort))
webServer.serve_forever()
