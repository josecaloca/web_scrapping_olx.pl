import sqlite3
import pandas as pd

def collect_data(conn_string = 'database/database_olx.db'):
    # establish conection to the sqlite database
    sqliteConnection = sqlite3.connect(conn_string)
    #define the cursor
    cursor = sqliteConnection.cursor()
    # extract all the data from the SQL database and create a dataframe
    df = pd.DataFrame(cursor.execute('SELECT * FROM offers'),
                    columns=['title', 'price', 'location','link'])
    sqliteConnection.close()
    
    return df