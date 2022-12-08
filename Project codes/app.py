# import flask functions to the program
from flask import Flask, render_template, redirect, url_for, request
from fetch_data import data_fetch   # import data_fetch function
# import database management functions to the program
from database_management import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    '''
    Login page
    '''
    error = None
    if request.method == 'POST':
        # read username and the password entered by the user
        if (request.form['username'], request.form['password']) not in read_credentials():
            # when username and password are not matching to existing credential
            error = 'Invalid Credentials. Please try again.'
        else:
            # when credentials are matching
            # make the logged user to current user
            insert_currentUser(request.form['username'])
            # create a table to the current user if the person is a new user
            create_userTable(request.form['username'])
            return redirect(url_for('home'))    # redirect to the home page
    return render_template('login.html', error=error)


@app.route('/home', methods=['GET', 'POST'])
def home():
    '''
    Home page
    '''
    error = None
    if request.method == 'POST':
        if data_fetch(request.form['isbn_number']) != 'error':
            # get the isbn number from the web page and retrieve the data from the API
            # if the data is successfully loaded, insert them to the corresponding table in database
            insert_bookdata(read_currentUser(), data_fetch(
                request.form['isbn_number']))
            return redirect(url_for('home'))    # redirect to home page
        else:
            error = 'Error: There is an error in data loading.'
    return render_template('home.html', data=read_bookData(read_currentUser()), error=error)


@app.route('/delete', methods=['POST'])
def delete_book():
    '''
    This is to identify the delete button pressing and remove the datarow from the database
    '''
    delete_singleRows(read_currentUser(), request.form['book_to_delete'])
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
