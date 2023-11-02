from movies import Movies

movies = Movies()  # Instantiate the Movies class with your data

while True:
    print("Menu:")
    print("1. List all movie names")
    print("2. Search movies by name")
    print("3. Search movies by cast")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        movie_names = movies.list_all_movie_names()
        for name in movie_names:
            print(name)
    elif choice == '2':
        keyword = input("Enter a keyword to search for movies by name: ")
        matching_movies = movies.search_movies_by_name(keyword)
        for name in matching_movies:
            print(name)
    elif choice == '3':
        keyword = input("Enter a keyword to search for movies by cast: ")
        matching_movies = movies.search_movies_by_cast(keyword)
        for movie, actors in matching_movies:
            print(movie)
            print(actors)
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
