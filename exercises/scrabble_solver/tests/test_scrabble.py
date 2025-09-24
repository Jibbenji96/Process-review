from lib.scrabble import Scrabble

def test_scrabble_inits():
    scrabble = Scrabble()
    assert scrabble.scores == {'A': 1,
                                'E': 1,
                                'I': 1, 
                                'O': 1, 
                                'U': 1, 
                                'L': 1, 
                                'N': 1, 
                                'R': 1, 
                                'S': 1, 
                                'T': 1, 
                                'D': 2, 
                                'G': 2, 
                                'B': 3, 
                                'C': 3, 
                                'M': 3, 
                                'P': 3, 
                                'F': 4, 
                                'H': 4, 
                                'V': 4, 
                                'W': 4, 
                                'Y': 4, 
                                'K': 5, 
                                'J': 8, 
                                'X': 8, 
                                'Q': 10, 
                                'Z': 10
                            }
    

def test_scrabble_new():
    scrabble = Scrabble()
    scrabble.new('cabbage')

    assert scrabble.word == 'cabbage'


def test_scrabble_score_cabbage():
    scrabble = Scrabble()
    scrabble.new('cabbage')

    assert scrabble.points() == 14


def test_scrabble_score_numeric():
    scrabble = Scrabble()
    scrabble.new('cabbage!')

    assert scrabble.points() == 0


def test_scrabble_score_cheese():
    scrabble = Scrabble()
    scrabble.new('cheese')
    
    assert scrabble.points() == 11