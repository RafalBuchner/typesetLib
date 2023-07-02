from typesetLib.abstract.basic import ProofBasicObject


class AbstractText(ProofBasicObject):
    def __init__(self, txt=None):
        super().__init__()
        self.paragraphs = None
        self._text = txt

        # needed for character styling
        self.textSegments = []
        self.setText(txt)

    @property
    def paragraphs(self):
        if self.getText is None:
            return None

    def setText(self, txt):
        self.paragraphs = None
        self._text = txt

        # needed for character styling
        self.textSegments = []

        if txt is None:
            return

        self.paragraphs = []
        for idx, parTxt in enumerate(self._text.split("\n")):
            par = AbstractParagraph(parTxt, idx)
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

    def setCharacterStyle(paragraphIndex, startIdx, charRange, characterStyle):
        seg = AbstractTextSegment(paragraphIndex, startIndex,
                          charRange, characterStyle)
        self.textSegments.append(seg)

    def getTextSegmentStr(self, textSegment):
        par = self.getParagraphByIndex[textSegment.paragraphIndex]

        txt = par.txt[textSegment.index,
                      textSegment.index + textSegment.charRange]
        return txt

    def getSegmentsPerParagraphDict(self):
        segmentsPerParagraph = {}
        for par in self.paragraphs:
            segmentsPerParagraph[par] = []
            for textSegment in self.textSegments:
                if textSegment.paragraphIndex == par.index:
                    segmentsPerParagraph[par].append(textSegment)
        return segmentsPerParagraph

    def getStyleMap(self):
        segmentsPerParagraph = self.getSegmentsPerParagraphDict()
        # styleMap = []
        # textMap = []
        for par, segments in self.getSegmentsPerParagraphDict().items():
            pass


        # TODO:
        # this will be the method that returns two lists,
        # (not dicts, because they can exclude txt segments as keys)
        # which will contain:
        # styleMap - character and paragraph styles in the same order as:
        # textMap – chunks of text strings, that are divided based on style map

class AbstractParagraph(ProofBasicObject):
    def __init__(self, txt, index, paragraphStyle=None):
        self.txt = txt
        self.index = index
        self.paragraphStyle = paragraphStyle

    def setParagraphStyle(self, paragraphStyle):
        self.paragraphStyle = paragraphStyle


class AbstractTextSegment(ProofBasicObject):
    """
    TextSegment
    represents chunk of text. You can think of it as of a selection of text.
    It is needed to make Character Styling happen

    parameters
    paragraphIndex – int - self explanatory.
    startIndex – int - index of a character in parent-paragraph's text that starts the segment
    charRange - int - count of letters, that are included in the text segment

    """

    def __init__(self, paragraphIndex, startIndex,
                 charRange, characterStyle=None):
        self.paragraphIndex = paragraphIndex
        self.startIndex = startIndex
        self.charRange = charRange
        self.characterStyle = characterStyle

    @property
    def endIndex(self):
        return self.charRange-self.startIndex
    
