from bowling_game import BowlingGame, example_game

# Test 1: Example Game from your code
def test_example_game_score():
    game = example_game()
    assert game.score() == 190

# Test 2: Perfect Game - all strikes
def test_perfect_game():
    game = BowlingGame()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300

# Test 3: All Spares - 21 rolls of 5
def test_all_spares():
    game = BowlingGame()
    for _ in range(21):
        game.roll(5)
    assert game.score() == 150

# Test 4: Gutter Game - all 0s
def test_gutter_game():
    game = BowlingGame()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0

# Test 5: Regular Game - mixed random rolls
def test_regular_game():
    game = BowlingGame()
    rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1,
             7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
    for pins in rolls:
        game.roll(pins)
    assert game.score() == 72
