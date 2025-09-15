from bowling_game import example_game

def test_example_game_score():
    game = example_game()
    assert game.score() == 190

def test_dummy_math():
    # This is a backup test to prove pytest runs
    assert 2 + 2 == 4
