from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typesetLib.text import TextObj
    from typesetLib.textFrame import TextFrame

from typesetLib.basic import BasicProofObject, BasicDrawbotObject


class Story(BasicProofObject):
    def __init__(self, textObj: TextObj):
        self.textObj = textObj
        self.textBoxes = []

        self.textLeft: TextObj

    def addTextBox(self, layoutTextBox: TextFrame):
        self.textBoxes.append(layoutTextBox)


class DBStory(Story):
    def draw(self):
        NotImplemented
