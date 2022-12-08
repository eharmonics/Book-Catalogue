# import sqlite3 library to the program
import sqlite3
from sqlite3 import Error
from fetch_data import data_fetch   # import data_fetch function to the program

'''
Connecting to the database, executing queries and commiting changes are common steps to all the functions definied below.
I have defined these steps inside each function, because I wanted to make each action as a seperate block of code

In comments, common steps are decribed in the first function. In other functions, only the uncommon steps are described
'''


def create_credentialTable():
    '''
    This function creates a table named 'userdata' in the database to store user login credentials.
    '''
    # try-except block is used to handle the errors that can be occurred while database handling
    try:
        # make connection to the database file
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()   # creat a cursor object to access the database
        # define the query to creat the table with column names and data types
        query = '''CREATE TABLE IF NOT EXISTS userdata(
            username text NOT NULL,
            password text NOT NULL
        );'''
        c.execute(query)    # excute the query
        conn.commit()   # commit the transaction
    except Error as e:
        print(e)


def create_currentUserTable():
    '''
    This function creates a table named 'currentuser' in the database to store the username of the most recently loged user.
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = '''CREATE TABLE IF NOT EXISTS currentuser(
            username text NOT NULL
        );'''
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)


def create_userTable(username):
    '''
    This function creates a table named by the given username in the database to store user's books data'.
    Parameters:
        username - the name of the user that needs to creat a table for
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        # to create the query, a 'f' string is used, since the table name needs to be included according to the function argument
        query = f'''CREATE TABLE IF NOT EXISTS {username}(
            isbn_number integer NOT NULL,
            title text,
            authors text,
            page_count integer,
            avg_rating text,
            link text
        );'''
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)


def insert_credentials(username, password):
    '''
    This function creates to add user login credentials to the userdata table.
    Parameters:
        username - the name of the user that needs to add to the table
        password - the password of the user that needs to add to the table
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = f'''INSERT INTO userdata VALUES(?,?)'''
        c.execute(query, (username, password))
        conn.commit()
    except Error as e:
        print(e)


def insert_currentUser(username):
    '''
    This function creates to add current user's name to the curentuser table.
    Parameters:
        username - the name of the user that needs to add to the table
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = '''INSERT INTO currentuser VALUES(?)'''
        c.execute(query, (username,))
        conn.commit()
    except Error as e:
        print(e)


def insert_bookdata(username, data):
    '''
    This function creates to add book data to the given user's table.
    Parameters:
        username - the name of the table that needs to add book data
        data - the book data as a tuple
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = f'''INSERT INTO {username} VALUES(?,?,?,?,?,?)'''
        c.execute(query, data)
        conn.commit()
    except Error as e:
        print(e)


def read_credentials():
    '''
    This function creates to read user login credentials from the userdata table. It returns data as a list of tuples.
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = '''SELECT * from userdata'''
        c.execute(query)
        records = c.fetchall()  # take all the data records to a single list
        conn.commit()
        return records
    except Error as e:
        print(e)


def read_bookData(username):
    '''
    This function creates to read book date from the user's table. It returns data as a list of tuples.
    Parameters: 
        username - the name of the table that needs to read data
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = f'''SELECT * from {username}'''
        c.execute(query)
        records = c.fetchall()
        conn.commit()
        return records
    except Error as e:
        print(e)


def read_currentUser():
    '''
    This function creates to read the current user from the currentuser table. 
    It returns the first element of the last tuple in the list of tuples.
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = '''SELECT * from currentuser'''
        c.execute(query)
        records = c.fetchall()
        conn.commit()
        return records[-1][0]
    except Error as e:
        print(e)


def delete_allRows(table_name):
    '''
    This function creates to delete all the rows from the given table.
    Parameters:
        table_name -  the name of the table
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = f'''DELETE FROM {table_name};'''
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)


def delete_singleRows(table_name, row_id):
    '''
    This function creates to delete a single row from the specified table using given row_id.
    Parameters:
        table_name -  the name of the table
        row_id - isbn_number of the row, that needs to be deleted
    '''
    try:
        conn = sqlite3.connect('data/database.db')
        c = conn.cursor()
        query = f'''DELETE FROM {table_name} where isbn_number = {row_id}'''
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)


''' To creat a table in the database manually use following format (after uncommenting)'''
# create_credentialTable()
# create_currentUserTable()
# create_userTable(username)

''' To insert data to a table in the database manually use following format (after uncommenting)'''
# insert_currentUser(username)
# insert_credentials(username, password)
# insert_bookdata(username, data)

''' To read data from a table in the database manually use following format (after uncommenting)'''
# read_bookData(username)
# read_credentials()
# read_currentUser()

''' To delete a data from a table in the database manually use following format (after uncommenting)'''
# delete_singleRows(table_name, row_id)

''' To delete all data rows from a table in the database manually use following format (after uncommenting)'''
# delete_allRows(table_name)
