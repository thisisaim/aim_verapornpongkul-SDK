import unittest
import src.characters as characters
import json

class TestSDK(unittest.TestCase):

    def test_get_all_characters(self):
        test = characters.Character.get_all_characters()
        self.assertEqual(len(test), 933)


    def test_get_character_by_id(self):
        result = characters.Character.get_character_by_id("5cd99d4bde30eff6ebccfbbf")
        json_object = json.loads(result)
        self.assertTrue(json_object['docs'][0]['name'], "Adrahil I")


    def test_get_character_quote_by_id(self):
        result = characters.Character.get_character_quote_by_id(
            "5cd99d4bde30eff6ebccfbbf")
        json_object = json.loads(result)
        assert json_object['docs'] == []


    def test_create_characters_empty(self):
        test = characters.Character()
        self.assertEqual(test.id,"")
        self.assertEqual(test.height,"")
        self.assertEqual(test.race,"")
        self.assertEqual(test.gender,"")
        self.assertEqual(test.birth,"")
        self.assertEqual(test.spouse,"")
        self.assertEqual(test.death,"")
        self.assertEqual(test.realm,"")
        self.assertEqual(test.hair,"")
        self.assertEqual(test.name,"")
        self.assertEqual(test.wikiUrl,"")

if __name__ == "__main__":
    unittest.main()