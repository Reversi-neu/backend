from db import DB
from flask import jsonify
import datetime

# AccountManager class - manages all account related actions
class AccountManager:

    def __init__(self):
        self.db = DB()
        self.default_elo = 1000
    
    # Gets a user by ID, returns a user object
    def getUserByID(self, userID):
        userID = int(userID)
        if (userID == 0): # AI
            return jsonify({
                'userID': 0,
                'username': None,
                'password': None,
            })

        statement = 'SELECT * FROM users WHERE userID = %s'
        rv = self.db.callDB(statement, (userID))

        if (len(rv) == 0):
            return None

        return jsonify({
            'userID': rv[0][0],
            'username': rv[0][1],
            'password': rv[0][2],
        })

    # Gets user by username and password, returns a user object
    def login(self, username, password):
        rv = self.db.callDB('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))

        if (len(rv) == 0):
            return jsonify({
                'userID': None,
                'username': None,
                'password': None,
            })

        return jsonify({
            'userID': rv[0][0],
            'username': rv[0][1],
            'password': rv[0][2],
        })

    # Creates a new user, returns a user object
    def signup(self, username, password):
        newId = self.getNextUserID()
        date = datetime.datetime.now()

        self.db.callDB('INSERT INTO users VALUES (%s, %s, %s, %s)', (newId, username, password, date))
        self.db.callDB('INSERT INTO elo VALUES (%s, %s, %s)', (newId, self.default_elo, date))
        rv = self.db.callDB('SELECT * FROM users WHERE userID = %s', (newId))

        if (len(rv) == 0):
            return jsonify({
                'userID': None,
                'username': None,
                'password': None,
            })

        return jsonify({
            'userID': rv[0][0],
            'username': rv[0][1],
            'password': rv[0][2],
        })

    # Creates a guest user, returns a user object
    def guest(self):
        newId = self.getNextUserID()
        date = datetime.datetime.now()

        self.db.callDB('INSERT INTO users VALUES (%s, %s, %s, %s)', (newId, None, None, date))
        self.db.callDB('INSERT INTO elo VALUES (%s, %s, %s)', (newId, self.default_elo, date))
        rv = self.db.callDB('SELECT * FROM users WHERE userID = %s', (newId))

        if (len(rv) == 0):
            return jsonify({
                'userID': None,
                'username': None,
                'password': None,
            })

        return jsonify({
            'userID': rv[0][0],
            'username': rv[0][1],
            'password': rv[0][2],
        })
    
    # Gets the next user ID from the DB
    def getNextUserID(self):
        rv = self.db.callDB('SELECT MAX(userID) FROM users', ())

        if (len(rv) == 0):
            return 1

        return rv[0][0] + 1
    
    # Gets the elo leaderboard for users
    def getLeaderboard(self):
        rv = self.db.callDB('SELECT * FROM elo WHERE userID > 0 ORDER BY elo DESC', ())
        res = []
        for i in range(len(rv)):
            res.append({
                'username': self.getUserByID(rv[i][0]).get_json()['username'],
                'userID': rv[i][0],
                'elo': rv[i][1],
                'date': rv[i][2],
            })
        
        return jsonify(res)