from flask import Flask
from flask import Flask
from flask_cors import CORS
from api_manager import APIManager
from db import DB
from model.games_manager import GamesManager
from account_manager import AccountManager
from socket_manager import SocketManager

# Server class - the main class of the server
class Server:

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)

        self.db = DB()
        self.gamesManager = GamesManager(self.getNextGameID())
        self.accountManager = AccountManager()
        self.apiManager = APIManager(self.app, self.gamesManager, self.accountManager)
        self.socketManager = SocketManager(self.app, self.gamesManager, self.accountManager)

    # running the server
    def run(self):
        self.socketManager.run()

    # helper function to get the next game ID from the DB
    def getNextGameID(self):
        rv = self.db.callDB('SELECT MAX(gameID) FROM games', ())

        if (len(rv) == 0):
            return 1

        return rv[0][0] + 1