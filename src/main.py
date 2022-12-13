import sys
import books as books
import chapters as chapters
import characters as characters
import movies as movies
import quotes as quotes

if __name__ == "__main__":
    print("App Started:")
    print(books.Book.get_all_books())
    print(chapters.Chapter.get_all_chapters())
    print(characters.Character.get_all_characters())
    print(movies.Movie.get_all_movies())
    print(quotes.Quote.get_all_quotes())

