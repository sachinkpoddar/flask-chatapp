# Script to make a new chatroom

from flask import Flask
app = Flask(__name__)
app.debug = True
app.secret_key = b'JPtUKpetQiyfzGpBS5SM' 

from database import Connection
db = Connection(app, 'localhost', 27017)

db.create_room("room1") # Make new room