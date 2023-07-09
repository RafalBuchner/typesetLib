import unittest
import os
import pprint
import sys

article = open("article.txt", "r").read()


class AbstractObjectsTest(unittest.TestCase):
    def test_textObj(self):
        from typesetLib.text import TextObj
        from typesetLib.styles import CharacterStyle
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
        from typesetLib.page import Page
        page = Page((100, 200))
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
        from typesetLib.text import TextObj
        from typesetLib.story import Story
        from typesetLib.page import Page
        from typesetLib.textFrame import TextFrame

        txt = TextObj()
        txt.setText(article)
        story = Story(txt)

        page = Page((500, 1000))

        textBoxObj1 = TextFrame((0, 10), (10, 20), story)
        textBoxObj2 = TextFrame((49, 23), (40, 50), story)
        textBoxObj3 = TextFrame((3, 11), (80, 70), story)
        self.assertEqual(len(story.textBoxes), 3)

        for textBoxObj in story.textBoxes:
            page.addChild(textBoxObj)

        self.assertEqual(len(page.children[TextFrame.__name__]), 3)

    def test_basicDrawbot(self):
        from typesetLib.basic import BasicDrawbotObject

        db_obj = BasicDrawbotObject()
        db_obj.setCanvasSize((1000, 1000))

        # position only
        db_x, db_y = db_obj.translateOriginOfPosition((0, 50))
        self.assertEqual(db_y, 950)
        # position + size
        db_x, db_y, db_w, db_h = db_obj.translateOriginOfPosition((0, 50, 0, 70))
        self.assertEqual(db_y, 880)

    def test_GridObjects(self):
        from typesetLib.grid import Grid, DBGrid

        grid = Grid(
            originPos=(10, 10),
            columnRowNum=(6, 8),
            gridSize=None,
            cellSize=(20, 50),
            colGutter=10,
            rowGutter=10
        )
        x1, y1 = grid.getCellPosition(2, 2)
        x2, y2, w2, h2 = grid.getAreaPosSize(2, 2, 5, 6)

        db_grid = DBGrid(
            originPos=(10, 10),
            columnRowNum=(6, 8),
            gridSize=None,
            cellSize=(20, 50),
            colGutter=10,
            rowGutter=10
        )
        x3, y3 = db_grid.getCellPosition(2, 2)
        x4, y4, w4, h4 = db_grid.getAreaPosSize(2, 2, 5, 6)
        self.assertEqual(y1, y2)


if __name__ == "__main__":
    unittest.main()
