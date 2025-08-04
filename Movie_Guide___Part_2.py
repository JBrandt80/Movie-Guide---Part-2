# Jeffrey
# CIS261
# Movie Guide - Part 2

MOVIE_FILE = "movies.txt"

def display_menu():
    print("Movie Guide")
    print() # Adds a blank line
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print() # Adds a blank line

def read_movies():
    try:
        with open(MOVIE_FILE, "r") as file:\
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return[]

def write_movies(movies):
    with open(MOVIE_FILE, "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def list_movies(movies):
    if not movies:
        print("There are no movies in the list. \n")
    else:
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie}")
        print() # Adds a blank line

def add_movie(movies):
    title = input("Enter movie: ")
    movies.append(title)
    write_movies(movies)
    print(f"{title} was added. \n")

def delete_movie(movies):
    try:
        number = int(input("Enter movie number to delete: "))
        if 1 <= number <= len(movies):
            removed = movies.pop(number - 1)
            write_movies(movies)
            print(f"{removed} was deleted. \n")
        else:
            print("Invalid movie number. \n")
    except ValueError:
        print("Invalid input. Please enter a number. \n")

def main():
    movies = read_movies()
    display_menu()

    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again. \n")

if __name__ == "__main__":
    if not read_movies():
        initial_movies = [
            "Cat on a Hot Tin Roof",
            "On the Waterfront",
            "Monty Python and the Holy Grail"
        ]
        write_movies(initial_movies)
    main()