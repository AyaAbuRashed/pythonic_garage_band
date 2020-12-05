
from pythonic_garage_band.pythonic_garage_band import *


def test_guitarist_str():

    guitarist = Guitarist("shown madness")
    actual = str(guitarist)
    expected = "My name is shown madness and I play guitar"
    assert actual == expected


def test_guitarist_repr():
    
    guitarist = Guitarist("shown madness")
    actual = repr(guitarist)
    expected = "Guitarist instance. Name = shown madness"
    assert actual == expected


def test_guitarist():
    guitarist = Guitarist("shown madness")
    assert guitarist.name == "shown madness"
    assert guitarist.get_instrument() == "guitar"

def test_drummer_str():
    drummer = Drummer("william")
    actual = str(drummer)
    expected = "My name is william and I play drums"
    assert actual == expected


def test_drummer_repr():
    drummer = Drummer("william")
    actual = repr(drummer)
    expected = "Drummer instance. Name = william"
    assert actual == expected


def test_bassist_str():
    bassist = Bassist("Mark")
    actual = str(bassist)
    expected = "My name is Mark and I play bass"
    assert actual == expected


def test_bassist_repr():
    bassist = Bassist("Mark")
    actual = repr(bassist)
    expected = "Bassist instance. Name = Mark"
    assert actual == expected

def test_bassist():
    flea = Bassist("jenny")
    assert flea.name == "jenny"
    assert flea.get_instrument() == "bass"


def test_band_name():
    nirvana = Band("BLACKPINK")
    assert nirvana.name == "BLACKPINK"




