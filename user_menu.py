import movie_manager


def menu_options():     # Menyval som användaren ser när den startar programmet.
    menu = """
        [1] Search movies based on it's exact title.
        [2] Search movies based on a word in the title.
        [3] Show history of previously searched movies.
        [4] Exit program.
        """
    print(menu)


def menu_selection(select):     # Menyhanterare som hanterar vart användaren skickas beroende på vilket val den gjorde.
    if select == 1:
        print("You have selected 1")
        movie_manager.movie_search_title()      # Titelsökning
    elif select == 2:
        print("You have selected 2")
        movie_manager.movie_search_word()   # Ord-i-titel-sökning.
    elif select == 3:
        print("You have selected 3")
        movie_manager.search_hist()     # Historik av filmer som användaren har sökt efter.
    elif select == 4:
        print("Exiting...")
        exit() # Avslutar program.
    else:   # Ifall användaren skriver fel för att navigera i menyn.
        print("Invalid selection. Please try again.")


def menu_choice():  # Felhantering i menyn, så att det blir en siffra och inte en bokstav.
    while True:
        menu_options()
        try:
            select = int(input("Please select an option"))
            menu_selection(select)
        except ValueError:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    menu_choice()
