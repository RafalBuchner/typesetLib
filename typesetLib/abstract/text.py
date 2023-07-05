from typesetLib.abstract.basic import BasicProofObject


class TextObj(BasicProofObject):
    """
    Represents text that runs in the Story object.

    Parameters:
    - txt (str): Text of the TextObj.
    """
    def __init__(self, txt:str=None):
        super().__init__()
        self.paragraphs = None
        self._text = txt

        # needed for character styling
        self.setText(txt)

    @property
    def textSegments(self):
        if self.paragraphs is None:
            return []
        return [seg for par in self.paragraphs for seg in par.getTextSegments()]

    @property
    def paragraphs(self):
        if self.getText is None:
            return None
        return self.__paragraphs

    @paragraphs.setter
    def paragraphs(self, value):
        self.__paragraphs = value

    def setText(self, txt):
        self.paragraphs = None
        self._text = txt

        if txt is None:
            return

        self.paragraphs = []

        for idx, parTxt in enumerate(self._text.split("\n")):
            par = Paragraph(self, parTxt, idx)
            self.paragraphs.append(par)

    def getText(self):
        return self._text

    def getParagraphByIndex(self, paragraphIndex):
        if paragraphIndex >= len(self.paragraphs):
            return None
        return self.paragraphs[paragraphIndex]

    def setTextStyle(self, paragraphStyle):
        # setting style for whole text
        for par in self.paragraphs:
            par.setParagraphStyle(paragraphStyle)

    def setParagraphStyleByIndex(self, paragraphStyle, paragraphIndex):
        par = self.getParagraphByIndex[paragraphIndex]
        par.setParagraphStyle(paragraphStyle)

    def setCharacterStyle(self, paragraphIndex, startIndex, charRange, characterStyle):
        segment = self.paragraphs[paragraphIndex].addTextSegment(startIndex, charRange, characterStyle)
        return segment

    def getTextAndStyleMaps(self):

        textMap = []
        styleMap = []
        for par in self.paragraphs:
            parTextMap, parStyleMap = par.getTextAndStyleMaps()
            textMap += parTextMap
            styleMap += parStyleMap

        return textMap, styleMap


class Paragraph(BasicProofObject):
    """
    Represents paragraph, as a part of TextObj.

    Parameters:
    - textObj (Paragraph): The parent TextObj object.
    - txtStr (str): String that belongs to the paragraph. Slice of text defined by TextObj (TextObj.getText())
    - index (int): The order number of Paragraph. Determined by TextObj.
    - paragraphStyle (ParagraphStyle): The style applied to the paragraph.
    """
    def __init__(self, textObj, txtStr, index, paragraphStyle=None):
        self._textSegments = []
        self.parent = textObj
        self.txtStr = txtStr
        self.index = index
        self.paragraphStyle = paragraphStyle

    def setParagraphStyle(self, paragraphStyle):
        self.paragraphStyle = paragraphStyle

    def addTextSegment(self, startIndex,
                       charRange, characterStyle=None):
        # TODO:
        #  check if new text segment is not overlapping with some
        #  other segment. If it does, then override overlapped chunk.
        #  It can be hard to implement, but possible.

        segment = TextSegment(self, startIndex,
                                      charRange, characterStyle)

        self._textSegments.append(segment)
        return segment

    def getTextSegments(self):
        self._textSegments.sort(key=lambda x: x.startIndex)
        return self._textSegments

    def getTextAndStyleMaps(self):
        # TODO:
        #  for now this method will assume, that the text segments are not
        #  overlapping!!! otherwise it will create a mess.
        segs = self.getTextSegments()
        styleMap = []
        indices = []
        for idx, seg in enumerate(segs):
            # indices for creating textmap
            indices.append(seg.startIndex)
            indices.append(seg.endIndex)

            # creating stylemap

            # if characterStyle starts with the beggining paragraph,
            # don't add default style on the beggining,
            # otherwise:
            if idx == 0 and seg.startIndex != 0:
                styleMap = [self.paragraphStyle]

            characterStyle = self.paragraphStyle
            if seg.characterStyle is not None:
                characterStyle = seg.characterStyle
            styleMap.append(characterStyle)

            # if next segment starts right after current one,
            # continue and don't add paragraph style to stylemap
            if idx + 1 < len(segs):
                nextSeg = segs[idx + 1]
                if seg.endIndex == nextSeg.startIndex:
                    continue
            styleMap.append(self.paragraphStyle)

        if len(segs) > 0:

            textMap = [self.txtStr[:segs[0].startIndex]]
            for i, j in zip(indices, indices[1:] + [None]):

                # take care of empty strings, that
                # appear between neighbouring
                # text segments:
                if self.txtStr[i:j] != "":
                    textMap.append(self.txtStr[i:j])
        else:
            styleMap = [self.paragraphStyle]
            textMap = [self.txtStr]

        return textMap, styleMap


class TextSegment(BasicProofObject):
    """
    Represents the smallest chunk of text, which can be thought of as a selection of text.
    It is needed to enable character styling.

    Parameters:
    - paragraphObj (Paragraph): The parent paragraph object.
    - startIndex (int): The index of the character in the parent paragraph's text that starts the segment.
    - charRange (int): The number of letters included in the text segment.
    - characterStyle (CharacterStyle): The style applied to the text segment.
    """

    def __init__(self, paragraphObj, startIndex,
                 charRange, characterStyle=None):
        self.parent = paragraphObj
        self.paragraphIndex = self.parent.index
        self.startIndex = startIndex
        self.charRange = charRange
        self.characterStyle = characterStyle

    @property
    def endIndex(self):
        return self.startIndex + self.charRange

    @property
    def txtStr(self):
        txt = self.parent.txtStr[self.startIndex:
                                 self.endIndex]
        return txt
