import webbrowser  # imports web browser controller


class Movie ():
    """Class containing the attributes common to all movie objects.

Args:
    movie_title (str): movie title.
    movie_storyline (str): storyline summary.
    poster_image (str): url to the movie's poster image.
    trailer_youtube (str): url to the movie trailer on YouTube.

Attributes:
    movie_title (str): movie title.
    movie_storyline (str): storyline summary.
    poster_image (str): url to the movie's poster image.
    trailer_youtube (str): url to the movie trailer on YouTube.

Methods:
    play_trailer (str): opens a window on page playing the youtube video.
"""
    def __init__(self, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def play_trailer(self):
        """Print a message from the current person

    Args:
        something (str): The message to print.

    Returns:
    None.
    """
        webbrowser.open(self.trailer_youtube_url)
