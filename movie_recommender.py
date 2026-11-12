def recommend_movie(genre):
    genre = genre.lower()

    if genre == "action":
        return "Recommended movie: Mission Impossible"
    elif genre == "comedy":
        return "Recommended movie: The Mask"
    elif genre == "science fiction":
        return "Recommended movie: Interstellar"
    elif genre == "animation":
        return "Recommended movie: Toy Story"
    elif genre == "drama":
        return "Recommended movie: The Pursuit of Happyness"
    else:
        return "Sorry, I don't have a recommendation for that genre."


print("Welcome to the Movie Recommendation System")

name = input("Enter your name: ")
genre = input(
    "Enter your preferred genre "
    "(action/comedy/science fiction/animation/drama): "
)

recommendation = recommend_movie(genre)

print()
print("Hello", name)
print(recommendation)
