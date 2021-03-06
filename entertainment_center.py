import fresh_tomatoes
import media

# Sets up six specific instances of the class movie
annie_hall = media.Movie("Annie Hall",
                         "A relationship between a man and a woman " +
                         "begins and ends.",
                         "https://upload.wikimedia.org/wikipedia/en/e/" +
                         "e6/Anniehallposter.jpg",
                         "1977",
                         "Woody Allen, Diane Keaton",
                         "https://www.youtube.com/watch?v=OqVgCfZX-yE")

clue = media.Movie("Clue",
                   "A movie based on the classic board game",
                   "https://upload.wikimedia.org/wikipedia/" +
                   "en/1/18/Clue_Poster.jpg",
                   "1985",
                   "Tim Curry, Madeline Kahn, " +
                   "Eileen Brennan, Christopher Lloyd",
                   "https://www.youtube.com/watch?v=cDDdeHtrxfA")

paris_texas = media.Movie("Paris, Texas",
                          "After wandering in the desert, " +
                          "a man reunites with his son and wife.",
                          "https://upload.wikimedia.org/wikipedia/en/" +
                          "7/76/Paris_texas_moviep.jpg",
                          "1984",
                          "Henry Dean Stanton, Nastassja Kinski, " +
                          "Dean Stockwell",
                          "https://www.youtube.com/watch?v=9e590FeeGCM")


phila_story = media.Movie("The Philadelphia Story",
                          "The night before her wedding, a society heiress " +
                          "reconsiders her upcoming nuptials.",
                          "https://upload.wikimedia.org/wikipedia/en/" +
                          "5/54/The-Philadelphia-Story-%281940%29.jpg",
                          "1940",
                          "Cary Grant, Katharine Hepburn, James Stewart",
                          "https://www.youtube.com/watch?v=6CtquHsxoZo")

hot_fuzz = media.Movie("Hot Fuzz",
                       "An exiled London cop finds trouble in a quaint " +
                       "British town in the countryside.",
                       "http://www.gstatic.com/tv/thumb/movieposters/" +
                       "163411/p163411_p_v7_aa.jpg",
                       "2007",
                       "Edgar Wright, Simon Pegg",
                       "https://www.youtube.com/watch?v=L6PKkxn7pq0")

bridesmaids = media.Movie("Bridesmaids",
                          "A woman grapples with her best friend's " +
                          "upcoming wedding. Hilarity ensues.",
                          "https://upload.wikimedia.org/wikipedia/en/" +
                          "d/df/BridesmaidsPoster.jpg",
                          "2011",
                          "Kristen Wiig, Maya Rudolph, Rose Byrne",
                          "https://www.youtube.com/watch?v=FNppLrmdyug")

# Creates an array the stores all instances of the Movie object
movies = [annie_hall, clue, paris_texas, phila_story, hot_fuzz, bridesmaids]

# Passes the "movies" array to the open movies function
# within the fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)
