from typesetLib.abstract.basic import BasicProofObject


class Style(BasicProofObject):
    def __init__(
        self,
        font=None,
        fontSize=10,
        fallbackFont=None,
        fill=(0, 0, 0),
        cmykFill=None,
        stroke=None,
        cmykStroke=None,
        strokeWidth=1,
        align=None,
        lineHeight=None,
        tracking=None,
        baselineShift=None,
        openTypeFeatures=None,
        tabs=None,
        language=None,
        indent=None,
        tailIndent=None,
        firstLineIndent=None,
        paragraphTopSpacing=None,
        paragraphBottomSpacing=None,
    ):
        super().__init__()
        self.font = font
        self.fontSize = fontSize
        self.fallbackFont = fallbackFont
        self.fill = fill
        self.cmykFill = cmykFill
        self.stroke = stroke
        self.cmykStroke = cmykStroke
        self.strokeWidth = strokeWidth
        self.align = align
        self.lineHeight = lineHeight
        self.tracking = tracking
        self.baselineShift = baselineShift
        self.openTypeFeatures = openTypeFeatures
        self.tabs = tabs
        self.language = language
        self.indent = indent
        self.tailIndent = tailIndent
        self.firstLineIndent = firstLineIndent
        self.paragraphTopSpacing = paragraphTopSpacing
        self.paragraphBottomSpacing = paragraphBottomSpacing

    def asDict(self):
        return {
                "font": self.font,
                "fontSize": self.fontSize,
                "fallbackFont": self.fallbackFont,
                "fill": self.fill,
                "cmykFill": self.cmykFill,
                "stroke": self.stroke,
                "cmykStroke": self.cmykStroke,
                "strokeWidth": self.strokeWidth,
                "align": self.align,
                "lineHeight": self.lineHeight,
                "tracking": self.tracking,
                "baselineShift": self.baselineShift,
                "openTypeFeatures": self.openTypeFeatures,
                "tabs": self.tabs,
                "language": self.language,
                "indent": self.indent,
                "tailIndent": self.tailIndent,
                "firstLineIndent": self.firstLineIndent,
                "paragraphTopSpacing": self.paragraphTopSpacing,
                "paragraphBottomSpacing": self.paragraphBottomSpacing
            }



class ParagraphStyle(Style):
    def __init__(self, **kwargs):
        super(ParagraphStyle, self).__init__(**kwargs)
        # print(self.font)


class CharacterStyle(Style):
    def __init__(self, **kwargs):
        super(CharacterStyle, self).__init__(**kwargs)


if __name__ == "__main__":
    style = ParagraphStyle(font="mój foncik")
