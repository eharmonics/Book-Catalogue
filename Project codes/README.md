# Book Catalogue

## Used Python version

Python 3.9.10

## Used Python packages

- sqlite3
- flask
- requests

## About the program

This program is a simple book catalogue management web application. It allows logging in for multiple users and managing book data for each user separately. Users can add books to the list by entering the ISBN number of the book. An added book can be removed from the catalog using the 'Delete' button near the book. The program stores all the data in a database file using multiple tables. There are tables to store,

- User credentials
- Book data for each user
- Current logged-in username

Book data is taken from the Google Book API using the ISBN number of the book. There is a separate program called _fetch_data.py_ to retrieve data from the API and filter.

All the functionality related to the database is handled by the _database_management.py_ file.

The main program is handled by the _app.py_ file and it uses the _login.html_ and _home.html_ template files for rendering web pages.

In HTML template files, _Bootstrap functions_ for JavaScript are used to modify the web page interface.
