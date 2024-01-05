import time
from DB_Connect import insertData


while True:
    insertData()
    
    # Sleep for 10 mins (600 seconds)
    time.sleep(600)
