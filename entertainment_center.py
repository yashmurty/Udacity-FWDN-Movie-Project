import media
import fresh_tomatoes

fight_club = media.Movie(
        "Fight Club",
        "An insomniac office worker, looking for a way to " +
        "change his life, crosses paths with a devil-may-care " +
        "soap maker, forming an underground fight club that " +
        "evolves into something much, much more.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzc1YmU2ZjEtYWIwMC00ZjM3LWI0NTctMDVlNGQ3YmYwMzE5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL50_SY999_CR0,0,704,999_AL_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_godfather = media.Movie(
        "The Godfather",
        "The aging patriarch of an organized crime dynasty " +
        "transfers control of his clandestine empire to his reluctant son.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTc0ZDk1YWItZDZiNi00NTdmLWE0MDctNTVhYTRhMDBmZjNjXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_QL50_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=sY1S34973zA")

the_dark_knight = media.Movie(
        "The Dark Knight",
        "When the menace known as the Joker wreaks havoc and " +
        "chaos on the people of Gotham, the caped crusader " +
        "must come to terms with one of the greatest " +
        "psychological tests of his ability to fight unjust",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

angry_men = media.Movie(
        "12 Angry Men",
        "A jury holdout attempts to prevent a miscarriage of " +
        "justice by forcing his colleagues to reconsider the evidence.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BODQwOTc5MDM2N15BMl5BanBnXkFtZTcwODQxNTEzNA@@._V1_QL50_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=fSG38tk6TpI")


schindlers_list = media.Movie(
        "Schindler's List",
        "In German-occupied Poland during World War II, Oskar " +
        "Schindler gradually becomes concerned for his Jewish workforce " +
        "after witnessing their persecution by the Nazi Germans.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzMwMTM4MDU2N15BMl5BanBnXkFtZTgwMzQ0MjMxMDE@._V1_QL50_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=gG22XNhtnoY")

pulp_fiction = media.Movie(
        "Pulp Fiction",
        "The lives of two mob hit men, a boxer, a " +
        "gangster's wife, and a pair of diner bandits " +
        "intertwine in four tales of violence and redemption.",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_QL50_SY1000_CR0,0,673,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

movies = [fight_club, the_godfather, the_dark_knight, angry_men,
          schindlers_list, pulp_fiction]
# Generate a website that displays these movies using fresh_tomatoes Mobule
fresh_tomatoes.open_movies_page(movies)
