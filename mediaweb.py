# This will import the web browser to allow trailers to play
import webbrowser

# Creates an class to allow Movie to be a structure for data
class Movie:
    # __init__ allow a default structure to be loaded
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # self.____ allows actions to be tied to functions
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    ''' 
    As an example here show_trailer is a function that will open
    the web browser to open a youtube trailer. It is
    called as self.trailer_youtube_url in practice.
    '''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
