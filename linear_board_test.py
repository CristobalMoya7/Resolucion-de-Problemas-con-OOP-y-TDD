import pytest
from linear_board import *
from settings import BOARD_LENGTH, VICTORY_STRICKE

def test_empty_board():
    empty _ LinearBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory("x") == False

def test_add():
    b = LinearBoard()
    for i in range(BOARD_LENGTH):
        b.add("x")
    assert b.is_full() == True

def test_victory():
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add("x")

    assert b.is_victory("o") == False
    assert b.is_victory("x") == True

def test_tie():
    b = LinearBoard()
    
    b.add("o")
    b.add("o")
    b.add("x")
    b.add("o")
    
    assert b.is_tie("x", "o")