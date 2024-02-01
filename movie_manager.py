import requests as r
import json

file_path = r"C:\Users\ViliM\OneDrive - Högskolan Dalarna\[4] GMI35S Scriptprogrammering\Laboration 3\Labb_3_Grupp_23\OMDB-key.txt"
try:
    with open(file_path, "r") as file:
        # Öppnar dokument för API-nyckel.
        api = file.read()
        # Gjort API-nyckeln "osynlig".
except FileNotFoundError as ferr:
    # Felsökning ifall filen inte existerar.
    print(ferr)

search_history = []     # Lista för sökhistorik.


def movie_search_title():   # Define av filmsökning med hjälp av exakt titelsökning.

    print('\nWrite the title for the movie you want to search for. ')
    title = input()
    response = r.get('https://www.omdbapi.com/?apikey='+api+'&t='+title).json()
    # Response.get (döpt response till "r") där vi hämtar information
    # Från OMDB, med hjälp av exakt titelsökning. (&t=). Gör sedan om till json fil.

    if 'Error' in response:     # Felhantering
        print(f"Error: {response['Error']}")
    else:
        search_result = {   # Search_result där vi letar efter title, år, och imdbID. OM det inte blir error.
            'Title': response.get('Title', 'N/A'),
            'Year': response.get('Year', 'N/A'),
            'imdbID': response.get('imdbID', 'N/A')
        }
        # IF-sats där om vi får resultat, skriver ut detta om filmen existerar.
        # Kolla else-satsen.
        if search_result['Title'] != 'N/A':
            print('The search gave this result:\n')
            print('Title:', search_result['Title'])
            print('Year:', search_result['Year'])
            print('imdbID:', search_result['imdbID'])
            search_history.append(response)
        else:
            print(f"No movies were found with the title '{title}'.")

        with open('movie_search.json', 'w') as json_file: 
            # Öppnar JSON fil där vi dumpar search_history.
            json.dump(search_history, json_file, indent=4)


def movie_search_word(): 
    # Define där vi söker filmer efter att ett ord stämmer överens med filmen användaren sökt efter.

    print('\nWrite a word in the title of the movie you want to search for.')
    w_title = input()
    w_response = r.get('https://www.omdbapi.com/?apikey='+api+'&s='+w_title).json()  # Hämtar info från OMDB
    # Med hjälp av (&s=) så är det ORD i titel och inte exakta titeln. Måste vara ett komplett ord och ej halvt ord.

    try: # uppdaterar och lägger till data i lista med hjälp av .append.
        search_history.append(w_response['Search'][0])

    except KeyError: # Felhantering ifall sökningen inte gick igenom med det ordet användaren använde.
        print('No movie was found with that title.')

    print('The search gave these results:\n')
    for w_value in w_response['Search']:    # For-loop som printar värden och öppnar movie_search.json för att dumpa-
                                            # - all data som finns om filmen.
        print('Title:', w_value["Title"], 'Year:', w_value["Year"], 'imdbID:', w_value["imdbID"])

        with open('movie_search.json', 'w') as json_file:
            json.dump(search_history, json_file, indent=4)
            
            
def search_hist():
    # Sökhistorik där vi kan se alla filmer som användaren har sökt när programmet har varit igång.
    
    print("Latest searches.\n")
    for response in search_history:
        if 'Search' in response:
            for row in response['Search']:
                print('Title:', row.get("Title", "N/A"))
        else:
            print('Title', response.get("Title", "N/A"))
