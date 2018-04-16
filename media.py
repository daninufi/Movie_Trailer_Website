import webbrowser #imports web browser controller

#creates movie class
class Movie ():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url= poster_image
        self.trailer_youtube_url = trailer_youtube

#opens youtube trailer in browser
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
