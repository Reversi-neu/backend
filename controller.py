import sys
from server import Server

# -- This is the 'controller' file of the server. It creates a server object and runs it. --
if __name__ == '__main__':
    # port is in cmd line args
    port = int(sys.argv[1])
    server = Server(port)
    server.run()