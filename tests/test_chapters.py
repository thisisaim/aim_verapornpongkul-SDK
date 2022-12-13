import unittest
import src.chapters as chapters

import json

class TestSDK(unittest.TestCase):

    def test_get_all_chapters(self):
        test = chapters.Chapter.get_all_chapters()
        self.assertEqual(len(test), 62)


    def test_get_chapter_by_id(self):
        result = chapters.Chapter.get_chapter_by_id("6091b6d6d58360f988133b8c")
        json_object = json.loads(result)
        self.assertEqual(json_object['docs'][0]['chapterName'], 
            "The Shadow of the Past")


    def test_create_chapter_empty(self):
        test = chapters.Chapter()
        self.assertEqual(test.id, "")
        self.assertEqual(test.book, "")
        self.assertEqual(test.chapterName, "")

if __name__ == "__main__":
    unittest.main()