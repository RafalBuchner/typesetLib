import unittest
import os
import pprint
import sys

article = open("article.txt", "r").read()


class AbstractObjectsTest(unittest.TestCase):
    def test_text(self):
        from typesetLib.abstract.text import TextObj
        from typesetLib.abstract.styles import CharacterStyle
        txt = TextObj()
        self.assertIsNone(txt.getText())
        self.assertIsNone(txt.paragraphs)

        txt.setText(article)
        self.assertListEqual(txt.textSegments, [])
        segment_0 = txt.setCharacterStyle(0, 3, 5, characterStyle=CharacterStyle())

        self.assertEqual(len(txt.textSegments), 1)
        self.assertEqual(txt.textSegments[0].txtStr, "2017,")

        segment_1 = txt.setCharacterStyle(0, segment_0.endIndex, 8, characterStyle=CharacterStyle())
        self.assertEqual(len(txt.textSegments), 2)

        textMap, styleMap = txt.paragraphs[0].getTextAndStyleMaps()
        self.assertEqual(len(textMap), len(styleMap))

        textMap, styleMap = txt.getTextAndStyleMaps()
        self.assertEqual(len(textMap), len(styleMap))


if __name__ == "__main__":
    unittest.main()
