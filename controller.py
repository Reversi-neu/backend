from server import Server

# -- This is the 'controller' file of the server. It creates a server object and runs it. --
if __name__ == '__main__':
    server = Server()
    server.run()