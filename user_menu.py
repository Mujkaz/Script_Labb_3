import requests as r , json , movie_manager
 # https://www.omdbapi.com/?apikey=5d7a7e3e&s=searched_movie

def menu_options():
    menu = """
[1] Search movies based on it's exact title.
[2] Search movies based on a word in the title.
[3] Show history of previously searched movies.
[4] Exit program.
"""
    print(menu)
def menu_selection(select):
    if select == 1:
        print("You have selected 1")
    elif select == 2:
        print("You have selected 2")
    elif select == 3:
        print("You have selected 3")
    elif select == 4:
        print("Exiting...")
        exit()
    else:
        print("Invalid selection. Please try again.")
def menu_choice():
    while True:
        menu_options()
        try:
            select = int(input("Please select an option"))
            menu_selection(select)
        except ValueError:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    menu_choice()