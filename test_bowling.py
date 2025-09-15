from bowling_game import example_game

def test_example_game_score():
    game = example_game()
    assert game.score() == 190

def test_dummy_math():
    # simple test to confirm pytest runs
    assert 1 + 1 == 2
