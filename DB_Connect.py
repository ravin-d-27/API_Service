import psycopg2
from json import dumps
from decouple import config
import requests

def insertData():

    # Your PostgreSQL connection details
    db_params = {
        "host": config("HOST"),
        "database": config("DATABASE"),
        "user": "eznolnll",
        "password": config("PASSWORD"),
        "port": config("PORT"),
    }

    request_str = "http://api.airpollutionapi.com/1.0/aqi?lat=28.7040590&lon=77.10249&APPID={}".format(config('API_KEY'))
    response = requests.get(request_str)



    # Data to be inserted
    data_to_insert = response.json()["data"]

    # Convert data to JSON string
    json_data = dumps({"data": data_to_insert})

    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Insert data into the database
    try:
        insert_query = """
        INSERT INTO air_quality_data (status, msg, text, alert, color, value, index, updated, temp, content, country, clouds, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """

        # Assuming 'status' and 'msg' are NULL for now, adjust accordingly
        cursor.execute(insert_query, (
            "success",
            None,
            data_to_insert["text"],
            data_to_insert["alert"],
            data_to_insert["color"],
            data_to_insert["value"],
            data_to_insert["index"],
            data_to_insert["updated"],
            data_to_insert["temp"],
            data_to_insert["content"],
            data_to_insert["country"],
            data_to_insert["clouds"],
            data_to_insert["coordinates"]["latitude"],
            data_to_insert["coordinates"]["longitude"]
        ))

        # Fetch the ID of the inserted record
        inserted_id = cursor.fetchone()[0]

        # Commit the changes to the database
        connection.commit()

        print(f"Data inserted with ID: {inserted_id}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and the connection
        cursor.close()
        connection.close()
