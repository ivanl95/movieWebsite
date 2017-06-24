import mediaweb
import fresh_tomatoes

toy_story = mediaweb.Movie("Toy Story","A story of a boy with toys",
                           "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                           "https://www.youtube.com/watch?v=KYz2wyBy3kc")
                           
avatar = mediaweb.Movie("Avatar","Movie about a marine on an alien planet",
                        "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
            
bvs = mediaweb.Movie("Batman v Superman: Dawn of Justice","A movie about two superheroes fighting",
                        "https://i2.wp.com/cdn.batman-news.com/wp-content/uploads/2016/02/635907799835969617-BVS-DOJ-IMAX-ExclusiveArt-DOM-Lg-2.jpg?quality=85&strip=info&ssl=1&w=800",
                        "https://www.youtube.com/watch?v=0WWzgGyAH6Y")
#print(avatar.storyline)
# avatar.show_trailer()
#bvs.show_trailer()

movies = [toy_story, avatar, bvs]
fresh_tomatoes.open_movies_page(movies)
