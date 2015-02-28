import movie
import cisko

# The purpose  of this code is to create six instances of the Movie class, and show them in the website

#creation of the ray movie
ray = movie.Movie("Ray",
                  "https://www.youtube.com/watch?v=jVHCQfcugdw",
                  "The life story of Ray Charles...",
                  "http://upload.wikimedia.org/wikipedia/en/2/2b/Ray_poster.jpg"
)

#creation of the Perfect Game movie instance
the_prefect_game = movie.Movie("The Perfect Game",
                               "https://www.youtube.com/watch?v=SPmnXrvwEq8",
                               "a group of boys from Monterrey, Mexico who become the first non-U.S. team to win the Little League World Series",
                               "http://upload.wikimedia.org/wikipedia/en/0/04/Perfect_game.jpg"
)

# Creation of the U turn movie instance
U_turn = movie.Movie("U Turn",
                     "https://www.youtube.com/watch?v=SgSZsxNtt8w",
                     "When Bobby Cooper's (Sean Penn) car breaks down in the two-horse town of Superior, Arizona, he becomes entangled in a web of murder, sex and deceit",
                     "http://upload.wikimedia.org/wikipedia/en/0/03/U-Turnposter.jpg"
)

# creation of Americathon movie instance
Amricathon = movie.Movie("Americathon",
                         "https://www.youtube.com/watch?v=BqYoB6BLOMw",
                         "a young TV consultant is hired by the President of a bankrupt USA to organize a telethon in order to prevent the country from being repossessed by wealthy Native Americans",
                         "http://upload.wikimedia.org/wikipedia/en/f/fc/Americathon.jpg"

)


#creation of K 9 movie instance
k_9 = movie.Movie("K9",
                  "https://www.youtube.com/watch?v=hCRZBon82Qw",
                  "To stop an elusive criminal, a maverick detective enlists the aid of a police dog who's an unusually intelligent smart alec",
                  "http://upload.wikimedia.org/wikipedia/en/d/d9/K_nine.jpg"
)


#creation of the Ugly truth Movie instance
the_ugly_truth = movie.Movie("The Ugly Truth",
                             "https://www.youtube.com/watch?v=DvsZtGxsvV0",
                             "A romantically challenged morning show producer is reluctantly embroiled in a series of outrageous tests by her chauvinistic correspondent to prove his theories on relationships and help",
                             "http://upload.wikimedia.org/wikipedia/en/a/ad/Ugly_truth.jpg"
)


# cration of a list of movie to feed the Open_Moviepage in the cisko Module
movies = [ray, the_prefect_game, U_turn, Amricathon, k_9, the_ugly_truth]

# call of the Open_movie_page
cisko.open_movies_page(movies)


