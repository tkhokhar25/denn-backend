import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def get_database_connection():
    connection = psycopg2.connect(dbname='denn', user='postgres', password='tusharsucks', host='localhost')
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    
    return connection, cursor