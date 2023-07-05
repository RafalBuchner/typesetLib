import drawBot as db
import os
import traceback
import subprocess
import shlex
import typesetLib.helpers as hlp
###
    # PREPARE TO TESTS
###
_outputFolder_ = "__drawbot_output__"
if not os.path.exists(_outputFolder_):
    os.mkdir(_outputFolder_)


def exec_cmd(command, silent=False):
    try:
        if silent:
            subprocess.check_call(shlex.split(command), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        else:
            subprocess.check_call(shlex.split(command))
    except:
        print(f"issue with cmd\n\t${cmd}")
        print(traceback.format_exc())
###
    # TESTS START
###

# Grid basic tests
from typesetLib.abstract.grid import Grid
db.size("A4Landscape")

grid = Grid(
    originPos=(10,10),
    columnRowNum=(6, 8),
    gridSize=(db.width()-20, db.height()-20),
    cellSize=None,
    colGutter=10,
    rowGutter=10
)

db.fill(None)
db.stroke(1,0,0)

colNum, rowNum = grid.columnRowNum
for x_idx in range(colNum):
    for y_idx in range(rowNum):
        db.rect(*grid.getAreaPosSize(x_idx,y_idx,1,1))
db.fill(1,0,0,0.2)
db.stroke(None)
db.rect(*grid.getAreaPosSize(0,0,1,5))
db.rect(*grid.getAreaPosSize(2,3,1,5))
db.rect(*grid.getAreaPosSize(2,0,4,2))
db.saveImage(os.path.join(_outputFolder_, "grid_based_on_gridSize.pdf"))

db.newDrawing()

from typesetLib.abstract.grid import Grid
db.size("A4Landscape")

grid = Grid(
    originPos=(10,10),
    columnRowNum=(6, 8),
    gridSize=(db.width()-20, db.height()-20),
    cellSize=None,
    colGutter=10,
    rowGutter=10
)

db.fill(None)
db.stroke(1,0,0)

colNum, rowNum = grid.columnRowNum
for x_idx in range(colNum):
    for y_idx in range(rowNum):
        db.rect(*grid.getAreaPosSize(x_idx,y_idx,1,1))
db.fill(1,0,0,0.2)
db.stroke(None)
db.rect(*grid[0,0], *grid*(1,5))
db.rect(*grid[2,3], *grid*(1,5))
db.rect(*grid[2,0], *grid*(4,2))
db.saveImage(os.path.join(_outputFolder_, "grid_mul_and_getitem_tests.pdf"))

db.newDrawing()
db.size("A4Landscape")
grid = Grid(
    originPos=(10,10),
    columnRowNum=(6, 8),
    gridSize=None,
    cellSize=(20, 50),
    colGutter=10,
    rowGutter=10
)

db.fill(None)
db.stroke(1,0,0)

colNum, rowNum = grid.columnRowNum
for x_idx in range(colNum):
    for y_idx in range(rowNum):
        db.rect(*grid.getAreaPosSize(x_idx,y_idx,1,1))
db.fill(1,0,0,0.2)
db.stroke(None)
db.rect(*grid.getAreaPosSize(0,0,1,5))
db.rect(*grid.getAreaPosSize(2,3,1,5))
db.rect(*grid.getAreaPosSize(2,0,4,2))

db.saveImage(os.path.join(_outputFolder_, "grid_based_on_cellSize.pdf"))

from typesetLib.abstract.grid import makeNestedGrid

db.newDrawing()
db.size("A4Landscape")
grid = Grid(
    originPos=(10, 10),
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
db.fill(1,0,0,0.2)
colNum, rowNum = grid.columnRowNum
for x_idx in range(colNum):
    for y_idx in range(rowNum):
        db.rect(*grid.getAreaPosSize(x_idx,y_idx,1,1))

db.fill(0,0,1,0.5)
colNum, rowNum = nested_grid.columnRowNum
for x_idx in range(colNum):
    for y_idx in range(rowNum):
        db.rect(*nested_grid.getAreaPosSize(x_idx,y_idx,1,1))
db.saveImage(os.path.join(_outputFolder_, "nested_grid.pdf"))
###
    # TESTS END
###
###
    # FINISH THE TESTS
###
exec_cmd(f"open {os.path.abspath(_outputFolder_) }")