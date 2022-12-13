import unittest
import src.movies as movies
import json

class TestSDK(unittest.TestCase):
    def test_get_all_movies(self):
        test = movies.Movie.get_all_movies()
        self.assertEqual(len(test), 8)


    def test_get_movie_by_id(self):
        result = movies.Movie.get_movie_by_id("5cd95395de30eff6ebccde59")
        json_object = json.loads(result)
        self.assertEqual(json_object['docs'][0]['name'], 
            "The Desolation of Smaug")


    def test_get_movie_quote_by_id(self):
        result = movies.Movie.get_movie_quote_by_id("5cd95395de30eff6ebccde59")
        json_object = json.loads(result)
        assert json_object['docs'] == []


    def test_create_movie_empty(self):
        test = movies.Movie()
        self.assertEqual(test.id,"")
        self.assertEqual(test.name,"")
        self.assertEqual(test.run_time_minutes,0)
        self.assertEqual(test.budget_millions,0)
        self.assertEqual(test.box_office_revenue_millions,0)
        self.assertEqual(test.academy_award_nominations,0)
        self.assertEqual(test.academy_award_wins,0)
        self.assertEqual(test.rotten_tomatoes_score,0)

if __name__ == "__main__":
    unittest.main()