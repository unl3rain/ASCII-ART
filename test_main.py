import pytest
from main import loadFont, printArt, loadFontOriginal, printArtOriginal

@pytest.fixture(scope="module")
def standard():
    font = "standard.txt"
    return loadFont(font)

@pytest.fixture(scope="module")
def shadow():
    font = "shadow.txt"
    return loadFont(font)

@pytest.fixture(scope="module")
def thinkertoy():
    font = "thinkertoy.txt"
    return loadFont(font)

@pytest.fixture(scope="module")
def standardOriginal():
    font = "standard.txt"
    return loadFontOriginal(font)

@pytest.fixture(scope="module")
def shadowOriginal():
    font = "shadow.txt"
    return loadFontOriginal(font)

@pytest.fixture(scope="module")
def thinkertoyOriginal():
    font = "thinkertoy.txt"
    return loadFontOriginal(font)

def test1(standard, standardOriginal):
    input = "Hello"
    output1 = printArt(input, standard)
    output2 = printArtOriginal(input, standardOriginal)
    assert output1.splitlines() == output2.splitlines()

def test2(standard, standardOriginal):
    input = "Hello\\nWorld"
    output1 = printArt(input, standard)
    output2 = printArtOriginal(input, standardOriginal)
    assert output1.splitlines() == output2.splitlines()