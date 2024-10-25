import json

# Function to load movies from a JSON file
def load_movies(file_name="movies.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save movies to a JSON file
def save_movies(movies, file_name="movies.json"):
    with open(file_name, "w") as file:
        json.dump(movies, file, indent=4)

# Function to generate a new unique ID
def generate_movie_id(movies):
    if movies:
        return max(movie["id"] for movie in movies) + 1
    else:
        return 1

# Function to add a movie to the list
def add_movie():
    movies = load_movies()
    movie_id = generate_movie_id(movies)
    name = input("Enter movie name: ")
    genre = input("Enter movie genre: ")
    year = int(input("Enter movie release year: "))
    age_rating = input("Enter age rating (e.g., 14 years and below): ")
    movie_hours = input("Enter movie duration (e.g., 2 hours 30 minutes): ")
    watched = input("Have you watched it? (yes/no): ").lower() == 'yes'
    rating = float(input("Enter movie rating (0-10): "))
    movie_type = input("Enter movie type (Movie/Short/Season): ")
    available_at = input("Where is it available (e.g., Netflix, Hulu): ")

    movies.append({
        "id": movie_id,
        "name": name,
        "genre": genre,
        "year": year,
        "age_rating": age_rating,
        "movie_hours": movie_hours,
        "watched": watched,
        "rating": rating,
        "type": movie_type,
        "available_at": available_at
    })
    save_movies(movies)
    print(f"Movie '{name}' added successfully with ID: {movie_id}.")

# Function to remove a movie by ID
def remove_movie():
    movie_id = int(input("Enter the ID of the movie to remove: "))
    movies = load_movies()
    updated_movies = [movie for movie in movies if movie["id"] != movie_id]
    
    if len(movies) == len(updated_movies):
        print(f"No movie found with ID '{movie_id}'.")
    else:
        save_movies(updated_movies)
        print(f"Movie with ID '{movie_id}' removed successfully.")

# Function to update a movie by ID
def update_movie():
    movie_id = int(input("Enter the ID of the movie to update: "))
    movies = load_movies()
    movie = next((m for m in movies if m["id"] == movie_id), None)
    
    if movie:
        print(f"Updating movie: {movie['name']}")
        movie['name'] = input(f"Enter new name (current: {movie['name']}): ") or movie['name']
        movie['genre'] = input(f"Enter new genre (current: {movie['genre']}): ") or movie['genre']
        movie['year'] = int(input(f"Enter new year (current: {movie['year']}): ") or movie['year'])
        movie['age_rating'] = input(f"Enter new age rating (current: {movie['age_rating']}): ") or movie['age_rating']
        movie['movie_hours'] = input(f"Enter new duration (current: {movie['movie_hours']}): ") or movie['movie_hours']
        movie['watched'] = input(f"Watched? (current: {movie['watched']}) (yes/no): ").lower() == 'yes'
        movie['rating'] = float(input(f"Enter new rating (current: {movie['rating']}): ") or movie['rating'])
        movie['type'] = input(f"Enter new type (current: {movie['type']}): ") or movie['type']
        movie['available_at'] = input(f"Enter new availability (current: {movie['available_at']}): ") or movie['available_at']
        
        save_movies(movies)
        print(f"Movie with ID {movie_id} updated successfully.")
    else:
        print(f"No movie found with ID '{movie_id}'.")

# Function to format and display movies
def format_movie(movie):
    return (f"ID: {movie['id']} / Name: {movie['name']} / Genre: {movie['genre']} / Year: {movie['year']} / "
            f"Age Rating: {movie['age_rating']} / Duration: {movie['movie_hours']} / Rating: {movie['rating']} / "
            f"Watched: {movie['watched']} / Available at: {movie['available_at']}")

# Function to display all movies
def display_all_movies():
    movies = load_movies()
    if movies:
        print("\nAll Movies:")
        for movie in movies:
            print(format_movie(movie))
            print("-" * 50)
    else:
        print("\nNo movies found.")
    input("\nPress Enter to return to the menu...")

# Function to display movies by watched status
def display_watched_movies(watched_status):
    movies = load_movies()
    filtered_movies = [movie for movie in movies if movie["watched"] == watched_status]
    
    if filtered_movies:
        status = "Watched" if watched_status else "Unwatched"
        print(f"\n{status} Movies:")
        for movie in filtered_movies:
            print(format_movie(movie))
            print("-" * 50)
    else:
        print(f"\nNo {status.lower()} movies found.")
    input("\nPress Enter to return to the menu...")

# Function to display movies alphabetically
def display_movies_alphabetically():
    movies = load_movies()
    sorted_movies = sorted(movies, key=lambda movie: movie["name"].lower())
    
    if sorted_movies:
        print("\nMovies Sorted Alphabetically:")
        for movie in sorted_movies:
            print(format_movie(movie))
            print("-" * 50)
    else:
        print("\nNo movies found.")
    input("\nPress Enter to return to the menu...")

# Function to display movies sorted by year
def display_movies_by_year():
    movies = load_movies()
    sorted_movies = sorted(movies, key=lambda movie: movie["year"])
    
    if sorted_movies:
        print("\nMovies Sorted by Year:")
        for movie in sorted_movies:
            print(format_movie(movie))
            print("-" * 50)
    else:
        print("\nNo movies found.")
    input("\nPress Enter to return to the menu...")

# Function to display movies by rating threshold
def display_by_rating(min_rating):
    movies = load_movies()
    rated_movies = [movie for movie in movies if movie["rating"] >= min_rating]
    if rated_movies:
        print(f"\nMovies with rating >= {min_rating}:")
        for movie in rated_movies:
            print(format_movie(movie))
            print("-" * 50)
    else:
        print(f"\nNo movies found with a rating >= {min_rating}.")
    input("\nPress Enter to return to the menu...")

# Function to search for a movie by name
def search_movie():
    search_name = input("Enter the movie name to search: ").strip().lower()
    movies = load_movies()
    found_movies = [movie for movie in movies if search_name in movie["name"].lower()]

    if found_movies:
        print("\nSearch Results:")
        for movie in found_movies:
            print(format_movie(movie))
            print("-" * 50)
    else:
        print(f"\nNo movies found with the name containing '{search_name}'.")
    input("\nPress Enter to return to the menu...")

# Function to show the menu and get user choice
def show_menu():
    print("\nMovie Manager")
    print("1. Add a new movie")
    print("2. Remove a movie")
    print("3. Update a movie")
    print("4. Display all movies")
    print("5. Display unwatched movies")
    print("6. Display watched movies")
    print("7. Display movies alphabetically")
    print("8. Display movies by year")
    print("9. Display movies by rating")
    print("10. Search movie by name")
    print("11. Exit")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-11): ")
        
        if choice == '1':
            add_movie()
        elif choice == '2':
            remove_movie()
        elif choice == '3':
            update_movie()
        elif choice == '4':
            display_all_movies()
        elif choice == '5':
            display_watched_movies(watched_status=False)
        elif choice == '6':
            display_watched_movies(watched_status=True)
        elif choice == '7':
            display_movies_alphabetically()
        elif choice == '8':
            display_movies_by_year()
        elif choice == '9':
            min_rating = float(input("Enter the minimum rating (0-10): "))
            display_by_rating(min_rating)
        elif choice == '10':
            search_movie()
        elif choice == '11':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()