from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typesetLib.abstract.text import TextObj
    from typesetLib.abstract.layoutTextBox import LayoutTextBox

from typesetLib.abstract.basic import ProofBasicObject




class Story(ProofBasicObject):
	def __init__(self, textObj: TextObj):
		self.textObj = textObj
		self.textBoxes = []

		self.textReminds: TextObj


	def addTextBox(self, layoutTextBox: LayoutTextBox):
		self.textBoxes.append(layoutTextBox)





