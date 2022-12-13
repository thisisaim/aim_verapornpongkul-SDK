import unittest
import src.books as books
import src.chapters as chapters
import src.characters as characters
import src.movies as movies
import src.quotes as quotes
import json

class TestSDK(unittest.TestCase):

    def test_get_all_books(self):
        result = books.Book.get_all_books()
        self.assertEqual(len(result), 3)


    def test_get_book_by_id(self):
        result = books.Book.get_book_by_id("5cf5805fb53e011a64671582")
        json_object = json.loads(result)
        self.assertEqual(json_object['docs'][0]['name'],
            "The Fellowship Of The Ring")


    def test_get_book_chapter_by_id(self):
        result = books.Book.get_book_chapter_by_id("5cf5805fb53e011a64671582")
        json_object = json.loads(result)
        self.assertEqual(json_object['docs'][0]['chapterName'],
            "A Long-expected Party")

if __name__ == "__main__":
    unittest.main()

