import psycopg2
from decouple import config
conn = psycopg2.connect(database=config("DATABASE"), user="eznolnll", password=config("PASSWORD"), host=config("HOST"), port=config("PORT"))


print("Opened database successfully")