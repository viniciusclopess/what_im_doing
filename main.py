import db
import functions

def inicialize():
    response = functions.go()
    db.insert(response[0], response[1], response[2])
inicialize()
