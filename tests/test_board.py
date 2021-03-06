from src.board import Board
from src.board import get_higher_value
import pytest

def test_change_tile():
	A=Board(4,4)
	A.change_tile(1,1,"Salut")
	assert A.get_grid()==[[None,None,None,None],[None,'Salut',None,None],[None,None,None,None],[None,None,None,None]]


def test_read_tile():
	A=Board(4,4)
	A.change_tile(1,1,"Salut")
	assert A.read_tile(1,1)=="Salut"

def test_transpose_grid_clockwise():
	A=Board(2,2)
	A.change_tile(1,1,"Bonjour")
	B=A.transpose_grid_clockwise()
	C=[[None,None],["Bonjour",None]]
	assert B==C

def test_transpose_grid_anticlockwise():
	A=Board(2,2)
	A.change_tile(1,1,"Bonjour")
	B=A.transpose_grid_anticlockwise()
	C=[[None,"Bonjour"],[None,None]]
	assert B==C
def test_get_all_tiles():
	A=Board(2,2)
	A.change_tile(1,1,"Salut")
	A.change_tile(0,0,"Bonjour")
	A.change_tile(1,0,"Hi")
	A.change_tile(0,1,"Guten Tag")
	L=['Bonjour','Guten Tag','Hi','Salut']
	assert A.get_all_tiles()==L

def test_get_higher_value():
	assert get_higher_value([[None,None,None,1],[2,3,4,5],[6,7,8,6],[1550,8,4,2]]) == 1550

def test_grid_to_string_with_size():
	A=Board(2,2)
	A.change_tile(1,1,"Salut")
	A.change_tile(0,0,"Bonjour")
	A.change_tile(1,0,"Hi")
	A.change_tile(0,1,"Guten")

	txt=" ======== ========\n|Bonjour |Guten   |\n ======== ========\n|Hi      |Salut   |\n ======== ======== "
	txt2=A.grid_to_string_with_size()
	assert txt2==txt
