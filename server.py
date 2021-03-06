import os
from flask import Flask
from flask import request

try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
#os.chdir('static')

# server http port 8000
#httpd = Server(("", PORT), Handler)
#try:
#  print("Start pythonserving at port %i" % PORT)
  
#  httpd.serve_forever()
#except KeyboardInterrupt:
#  pass
#httpd.server_close()

# flask http port 
app = Flask(__name__)
print ("port num", PORT)

@app.route("/flask")
def hello():
    return "Hello World! ftom flask \n"

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
    
    #app.run(host="", debug=True)