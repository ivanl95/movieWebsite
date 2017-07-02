import mediaweb
import fresh_tomatoes

toy_story = mediaweb.Movie("Toy Story", "A story of a boy with toys",
                           # Code utilizes Google's URL Shortener
                           "https://goo.gl/5Q8xYU",
                           "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = mediaweb.Movie("Avatar", "Movie about a marine on an alien planet",
                        "https://goo.gl/mkjJAk",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

bvs = mediaweb.Movie("Batman v Superman: Dawn of Justice", "A movie about two superheroes fighting",
                     "https://goo.gl/mhtwzg0",
                     "https://www.youtube.com/watch?v=0WWzgGyAH6Y")

'''
This initiates an instance to utilize 
our classes in the function fresh_tomatoes
'''
movies = [toy_story, avatar, bvs]

'''
This command will open our website
'''
fresh_tomatoes.open_movies_page(movies)
