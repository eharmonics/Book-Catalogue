import requests     # import requests module to the program


def data_fetch(isbn_num):
    '''
    This function searches the given ISBN number in Google Book API and get data from the endpoint.
    Then from this JSON data, filter out the required inforation about the book and return them as a tuple
    Parameters:
        isbn_number - the ISBN number of the book
    '''
    try:
        # this try except block is used to catch all the errors that can be occurred while connecting to the API
        # endpoint, and data retrieving.

        # url of the end point
        url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn_num}'
        response = requests.get(url).json()  # retrieve data in the JSON format
        # if there are multiple responses, we filter out the first response from it
        if type(response) == list:
            response = response[0]
        # extract required data from the JSON response
        title = response['items'][0]['volumeInfo']['title']
        authors = response['items'][0]['volumeInfo']['authors']
        page_count = response['items'][0]['volumeInfo']['pageCount']
        image_links = response['items'][0]['volumeInfo']['imageLinks']
        # in some responses, the 'averageRating' can't be found
        # if it can't find, the program return 'Not Found' string
        # check whether 'averageRating' is in the JSON response
        if 'averageRating' in response['items'][0]['volumeInfo']:
            avg_rating = response['items'][0]['volumeInfo']['averageRating']
        else:
            avg_rating = 'Not Found'
        # return data as a tuple
        return isbn_num, title, ','.join(authors), page_count, avg_rating, image_links['thumbnail']
    except:
        return 'error'

# we can call this function like below to print out the data
# print(data_fetch(1408810549))
