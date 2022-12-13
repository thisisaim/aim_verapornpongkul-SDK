import unittest
import src.quotes as quotes
import json

class TestSDK(unittest.TestCase):

    def test_get_all_quotes(self):
        test = quotes.Quote.get_all_quotes()
        self.assertEqual(len(test), 2384)


    def test_get_movie_quote_by_id(self):
        result = quotes.Quote.get_movie_quote_by_id("5cd96e05de30eff6ebcce7e9")
        json_object = json.loads(result)
        self.assertEqual(json_object['docs'][0]['movie'],      
            "5cd95395de30eff6ebccde5d")


    def test_create_quote_empty(self):
        test = quotes.Quote()
        self.assertEqual(test.dialog, "")
        self.assertEqual(test.movie, "")
        self.assertEqual(test.character, "")

if __name__ == "__main__":
    unittest.main()