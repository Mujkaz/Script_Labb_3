import requests as r, json, user_menu


#https://www.omdbapi.com/?apikey=5d7a7e3e&s=searched_movie

#https://www.omdbapi.com/?i=tt3896198&apikey=5d7a7e3e #Länken med all data
file_path = r"C:\Users\ViliM\OneDrive - Högskolan Dalarna\[4] GMI35S Scriptprogrammering\Laboration 3\Labb_3_Grupp_23\OMDB-key.txt"
try:
    with open(file_path, "r") as file:
        api = file.read()
except FileNotFoundError as ferr:
    print(ferr)

search_history = []     # Tom lista för att se de senaste sökningarna.
w_search_history = []

def movie_search_title():

    print('\nWrite the title for the movie you want to search for. ')
    title = input()
    response = r.get('https://www.omdbapi.com/?apikey='+api+'&t='+title).json()


    if 'Error' in response:
        print(f"Error: {response['Error']}")
    else:
        search_result = {
            'Title': response.get('Title', 'N/A'),
            'Year': response.get('Year', 'N/A'),
            'imdbID': response.get('imdbID', 'N/A')
        }

        if search_result['Title'] != 'N/A':
            print('The search gave this result:\n')
            print('Title:', search_result['Title'])
            print('Year:', search_result['Year'])
            print('imdbID:', search_result['imdbID'])
            search_history.append(response)
        else:
            print(f"No movies were found with the title '{title}'.")




def movie_search_word():

    print('\nWrite a word in the title of the movie you want to search for.')
    w_title = input()
    w_response = r.get('https://www.omdbapi.com/?apikey='+api+'&s='+w_title).json()

    try:
        search_history.append(w_response['Search'][0])
    except KeyError:
        print('No movie was found with that title.')

    print('The search gave these results:\n')
    for w_value in w_response['Search']:
        print('Title:', w_value["Title"], 'Year:', w_value["Year"], 'imdbID:', w_value["imdbID"])


def search_hist():
    print("Latest searches.\n")
    for response in search_history:
        if 'Search' in response:
            for row in response['Search']:
                print('Title:', row.get("Title", "N/A"), 'Year:', row.get("Year:", "N/A"), 'imdbID:', row.get("imdbID:", "NA/"))
        else:
            print('Title', response.get("Title", "N/A"), 'Year:', response.get("Year:", "N/A"), 'imdbID', response.get("imdbID:", "NA/"))


