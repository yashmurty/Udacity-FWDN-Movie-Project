import webbrowser


class Movie():
    """Movie Class definition :

    Attributes:
        movie_title (str): The title of the movie.
        movie_storyline (str): The storyline of the movie.
        poster_image (str): The Web URL of the movie image.
        trailer_youtube (str): The YouTube URL of the movie trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """__init__ method definition :
        Same attribute definition as of Movie class level.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
