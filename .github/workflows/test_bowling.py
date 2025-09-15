from bowling_game import example_game

def test_example_game_score():
    game = example_game()
    assert game.score() == 190
