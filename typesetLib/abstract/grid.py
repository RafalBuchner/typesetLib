from typesetLib.abstract.basic import BasicLayoutGraphicObject


class Grid(BasicLayoutGraphicObject):
    def __init__(self, originPos: tuple[float], gridSize: tuple[float], cellSize: tuple[float],
				 columnRowNum: int, colGutter: float, rowGutter: float):
        self._originPos = originPos
		self.columnRowNum = columnRowNum
		self.colGutter = colGutter
		self.rowGutter = rowGutter
		self.cellSize = None
		self.gridSize = None

		if (gridSize is not None or len(gridSize) == 2) and (cellSize is None or len(cellSize) != 2):
			# gridSize determined cellSize
			self.gridSize = gridSize
			gridWidth, gridHeight = self.gridSize
			colNum, rowNum = self.columnRowNum
			cellWidth = (gridWidth - self.colGutter * self.colGutterNum) / colNum
			cellHeight = (gridHeight - self.rowGutter * self.rowGutterNum) / rowNum
			self.cellSize = (cellWidth, cellHeight)



		if (cellSize is not None or len(cellSize) == 2) and (gridSize is None or len(gridSize) != 2):
			# cellSize determined gridSize
			self.cellSize = cellSize
			cellWidth, cellHeight = self.cellSize
			colNum, rowNum = self.columnRowNum
			gridWidth = colNum * cellWidth + self.colGutter *  self.colGutterNum
			gridHeight = rowNum * cellHeight + self.rowGutter * self.rowGutterNum
			self.gridSize = (gridWidth, gridHeight)
	@property
	def colGutterNum(self):
		"""
		number of gutters between the columns
		"""
		return self.columnRowNum[0] - 1

	@property
	def rowGutterNum(self):
		"""
        number of gutters between the rows
        """
		return self.columnRowNum[1] - 1

    def setPosition(self, position):
        self._position = position

    def getPosition(self):
        return self._position

	def getAreaPosSize(self, colCellIndex, rowCellIndex, horCellNum, verCellNum):
		cellWidth, cellHeight = self.cellSize
		x, y = self._originPos
		x += colCellIndex * cellWidth + colCellIndex * self.colGutter
		y += rowCellIndex * cellHeight + rowCellIndex * self.rowGutter

		width = horCellNum * cellWidth + self.colGutter * (horCellNum-1)
		height = verCellNum * cellHeight + self.rowGutter * (verCellNum-1)

		return x, y, width, height
