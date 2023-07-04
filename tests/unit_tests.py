import unittest
import os
import pprint
import sys

article = open("article.txt", "r").read()


class AbstractObjectsTest(unittest.TestCase):
    def test_textObj(self):
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

    def test_Page(self):
        from typesetLib.abstract.page import Page
        page = Page((100,200))
        self.assertEqual(page.currentPgNumber, 1)
        self.assertEqual(page.index, 0)

        page.pageFlip()
        self.assertEqual(page.currentPgNumber, 2)
        self.assertEqual(page.index, 1)
        page.pageFlip()
        self.assertEqual(page.currentPgNumber, 3)
        self.assertEqual(page.index, 2)
        page.resetPgNumberToStart()
        self.assertEqual(page.currentPgNumber, 1)
        self.assertEqual(page.index, 0)
        page.setStartingPgNumber(4)
        self.assertEqual(page.currentPgNumber, 4)
        self.assertEqual(page.index, 0)
        page.setCurrentPgNumber(10)
        self.assertEqual(page.currentPgNumber, 10)
        self.assertEqual(page.index, 6)
        page.setIndex(11)
        self.assertEqual(page.currentPgNumber, 15)
        self.assertEqual(page.index, 11)


    def test_basicLayouting(self):
        from typesetLib.abstract.text import TextObj
        from typesetLib.abstract.story import Story
        from typesetLib.abstract.page import Page
        from typesetLib.abstract.layoutTextBox import LayoutTextBox

        txt = TextObj()
        txt.setText(article)
        story = Story(txt)

        page = Page((500, 1000))

        textBoxObj1 = LayoutTextBox((0,10), (10,20), story)
        textBoxObj2 = LayoutTextBox((49,23), (40,50), story)
        textBoxObj3 = LayoutTextBox((3,11), (80,70), story)
        self.assertEqual(len(story.textBoxes), 3)

        for textBoxObj in story.textBoxes:
            page.addChild(textBoxObj)

        self.assertEqual(len(page.children[LayoutTextBox.__name__]), 3)


if __name__ == "__main__":
    unittest.main()
