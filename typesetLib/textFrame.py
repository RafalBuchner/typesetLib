from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typesetLib.abstract.story import Story

from typesetLib.abstract.basic import BasicLayoutGraphicObject
from typesetLib.abstract.page import Page


class TextFrame(BasicLayoutGraphicObject):
    """
    - story (Story)
    """

    def __init__(self, position: tuple[float], size: tuple[float], story: Story = None, verticalAlignment: str = "top"):
        super().__init__(size, index=None, position=position, verticalAlignment=verticalAlignment)
        if story != None:
            self.assignToStory(story)

    def assignToStory(self, story: Story):
        self.story = story
        idx = len(self.story.textBoxes) - 1
        self.setIndex(idx)

        self.story.addTextBox(self)

    @property
    def nextTextBox(self):
        if self.story is None:
            return None

        nextIndex = self.index + 1
        if nextIndex >= len(self.story.textBoxes):
            return None

        return self.story.textBoxes[nextIndex]

    @property
    def prevTextBox(self):
        if self.story is None:
            return None

        prevIndex = self.index - 1
        if prevIndex < 0:
            return None

        return self.story.textBoxes[prevIndex]

    def getParentPage(self):
        iterationLimit = 50
        parentPage = None
        currentObj = self
        for i in range(iterationLimit):
            currentObj = currentObj.parent
            if isinstance(currentObj, Page):
                parentPage = currentObj
                break
        return parentPage
