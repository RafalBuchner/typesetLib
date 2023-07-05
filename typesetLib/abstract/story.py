from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typesetLib.abstract.text import TextObj
    from typesetLib.abstract.textFrame import TextFrame

from typesetLib.abstract.basic import BasicProofObject


class Story(BasicProofObject):
    def __init__(self, textObj: TextObj):
        self.textObj = textObj
        self.textBoxes = []

        self.textReminds: TextObj

    def addTextBox(self, layoutTextBox: TextFrame):
        self.textBoxes.append(layoutTextBox)
