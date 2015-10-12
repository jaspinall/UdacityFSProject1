import webbrowser

#Defines a class Movie
class Movie():
    """Create a class Movie with title, storyline, image, release date,
       cast, and youtube trailer attributes"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 release_date, starring, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.release_date = release_date
        self.starring = starring
        self.trailer_youtube_url = trailer_youtube

#Method that opens the movie trailer for each instance of Movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
