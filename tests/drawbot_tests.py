import unittest
import drawBot as db
import os
import typesetLib.helpers as hlp

_outputFolder_ = "__drawbot_output__"
_outputFolder_ = os.path.abspath(_outputFolder_)
if not os.path.exists(_outputFolder_):
    os.mkdir(_outputFolder_)


class DrawbotObjectTest(unittest.TestCase):
    def test_gridBasedOnGridSize(self):
        from typesetLib.grid import Grid

        db.size("A4Landscape")

        grid = Grid(
            originPos=(10, 10),
            columnRowNum=(6, 8),
            gridSize=(db.width() - 20, db.height() - 20),
            cellSize=None,
            colGutter=10,
            rowGutter=10
        )

        db.fill(None)
        db.stroke(1, 0, 0)

        colNum, rowNum = grid.columnRowNum
        for x_idx in range(colNum):
            for y_idx in range(rowNum):
                db.rect(*grid.getAreaPosSize(x_idx, y_idx, 1, 1))
        db.fill(1, 0, 0, 0.2)
        db.stroke(None)
        db.rect(*grid.getAreaPosSize(0, 0, 1, 5))
        db.rect(*grid.getAreaPosSize(2, 3, 1, 5))
        db.rect(*grid.getAreaPosSize(2, 0, 4, 2))
        db.saveImage(os.path.join(_outputFolder_, "grid_based_on_gridSize.pdf"))
        hlp.exec_cmd(f"open {_outputFolder_}")

    def test_grid_mul_and_getitem_tests(self):
        from typesetLib.grid import Grid

        db.newDrawing()
        db.size("A4Landscape")

        grid = Grid(
            position=(10, 10),
            columnRowNum=(6, 8),
            gridSize=(db.width() - 20, db.height() - 20),
            cellSize=None,
            colGutter=10,
            rowGutter=10
        )

        db.fill(None)
        db.stroke(1, 0, 0)

        colNum, rowNum = grid.columnRowNum
        for x_idx in range(colNum):
            for y_idx in range(rowNum):
                db.rect(*grid.getAreaPosSize(x_idx, y_idx, 1, 1))
        db.fill(1, 0, 0, 0.2)
        db.stroke(None)
        db.rect(*grid[0, 0], *grid * (1, 5))
        db.rect(*grid[2, 3], *grid * (1, 5))
        db.rect(*grid[2, 0], *grid * (4, 2))
        db.saveImage(os.path.join(_outputFolder_, "grid_mul_and_getitem_tests.pdf"))
        hlp.exec_cmd(f"open {_outputFolder_}")

    def grid_basedOnCellSize(self):
        db.newDrawing()
        db.size("A4Landscape")
        grid = Grid(
            position=(10, 10),
            columnRowNum=(6, 8),
            gridSize=None,
            cellSize=(20, 50),
            colGutter=10,
            rowGutter=10
        )

        db.fill(None)
        db.stroke(1, 0, 0)

        colNum, rowNum = grid.columnRowNum
        for x_idx in range(colNum):
            for y_idx in range(rowNum):
                db.rect(*grid.getAreaPosSize(x_idx, y_idx, 1, 1))
        db.fill(1, 0, 0, 0.2)
        db.stroke(None)
        db.rect(*grid.getAreaPosSize(0, 0, 1, 5))
        db.rect(*grid.getAreaPosSize(2, 3, 1, 5))
        db.rect(*grid.getAreaPosSize(2, 0, 4, 2))

        db.saveImage(os.path.join(_outputFolder_, "grid_based_on_cellSize.pdf"))
        hlp.exec_cmd(f"open {_outputFolder_}")

    def test_nestingGrids(self):
        from typesetLib.grid import Grid
        from typesetLib.grid import makeNestedGrid

        db.newDrawing()
        db.size("A4Landscape")
        grid = Grid(
            position=(10, 10),
            columnRowNum=(6, 8),
            gridSize=(db.width() - 20, db.height() - 20),
            cellSize=None,
            colGutter=10,
            rowGutter=10
        )

        nested_grid = makeNestedGrid(
            parentGrid=grid,
            colCellIndex=2,
            rowCellIndex=2,
            horCellNum=3,
            verCellNum=4,
            colGutter=10,
            rowGutter=10
        )
        db.stroke(None)
        db.fill(1, 0, 0, 0.2)
        colNum, rowNum = grid.columnRowNum
        for x_idx in range(colNum):
            for y_idx in range(rowNum):
                db.rect(*grid.getAreaPosSize(x_idx, y_idx, 1, 1))

        db.fill(0, 0, 1, 0.5)
        colNum, rowNum = nested_grid.columnRowNum
        for x_idx in range(colNum):
            for y_idx in range(rowNum):
                db.rect(*nested_grid.getAreaPosSize(x_idx, y_idx, 1, 1))
        db.saveImage(os.path.join(_outputFolder_, "nested_grid.pdf"))
        hlp.exec_cmd(f"open {_outputFolder_}")


if __name__ == "__main__":
    unittest.main()
