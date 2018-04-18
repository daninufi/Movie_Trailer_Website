import media
import fresh_tomatoes

# contains the function that takes the movie list and
# generates HTML file including movie content.

# Create movie objects
the_godfather = media.Movie("The God Father",
                            "The aging patriarch of an organized"
                            " crime dynasty"
                            " transfers control of his clandestine"
                            " empire to his reluctant son.",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=sY1S34973zA")

up = media.Movie("Up",
                 "Carl sets out to fulfill his dream"
                 " to see the wilds of South America",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

an_american_tale = media.Movie("An American Tale",
                               "Fievel Mousekewitz gets lost and must"
                               " find a way to reunite with his family",
                               "https://upload.wikimedia.org/wikipedia/en/d/d2/AnAmericanTailPoster.jpg",
                               "https://www.youtube.com/watch?v=kvZfEQ_pMdg")

the_revenant = media.Movie("The Revenant",
                           "A frontiersman on a fur trading expedition"
                           " in the 1820s fights for survival.",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                           "https://www.youtube.com/watch?v=QRfj1VCg16Y")

everest = media.Movie("Everest",
                      "The story of New Zealand's Robert Rob Edwin Hall",
                      "https://upload.wikimedia.org/wikipedia/en/2/28/Everest_poster.jpg",
                      "https://www.youtube.com/watch?v=5ZQVpPiOji0")

manhattan = media.Movie("Manhattan",
                        "The life of a divorced television"
                        " writer dating a teenage girl",
                        "https://upload.wikimedia.org/wikipedia/en/f/f3/Manhattan-poster01.jpg",
                        "https://www.youtube.com/watch?v=Ck0ENY4eawQ")

# stores movie list
movies = [the_godfather, up, an_american_tale,
          the_revenant, everest, manhattan]

# opens function with movie list to generate HTML
fresh_tomatoes.open_movies_page(movies)
