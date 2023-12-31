import time
from DB_Connect import insertData


while True:
    insertData()
    
    # Sleep for one hour (3600 seconds)
    time.sleep(3600)
