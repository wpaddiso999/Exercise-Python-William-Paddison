class Movies:
    def __init__(self):
        self._movies = []  # Initialize the _movies list

        # Load movie data from a text file and populate the _movies list
        with open('movies.txt', 'r') as file:
            for line in file:
                movie_data = line.strip().split(',')
                if len(movie_data) == 2:
                    movie_name, cast = movie_data
                    cast_list = cast.split('|')
                    movie = {'name': movie_name, 'cast': cast_list}
                    self._movies.append(movie)

    def list_all_movie_names(self):
        return [movie['name'] for movie in self._movies]

    def search_movies_by_name(self, keyword):
        keyword = keyword.lower()
        matching_movies = [movie for movie in self._movies if keyword in movie['name'].lower()]
        return [movie['name'] for movie in matching_movies]

    def search_movies_by_cast(self, keyword):
        keyword = keyword.lower()
        matching_movies = []
        for movie in self._movies:
            matching_actors = [actor for actor in movie['cast'] if keyword in actor.lower()]
            if matching_actors:
                matching_movies.append((movie['name'], matching_actors))
        return matching_movies
