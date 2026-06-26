from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# NEW TEST: a wrong guess should ALWAYS cost the same points, no matter which
# attempt number it is. This catches the old bug where the score jumped around.
def test_wrong_guess_is_consistent():
    # Too High on an even attempt and an odd attempt should give the same result
    assert update_score(50, "Too High", 2) == 45
    assert update_score(50, "Too High", 3) == 45
    # Too Low should also cost 5 points
    assert update_score(50, "Too Low", 4) == 45


# NEW TEST: the input parser should accept good numbers and reject junk.
def test_parse_guess_handles_input():
    assert parse_guess("42") == (True, 42, None)
    ok, value, error = parse_guess("hello")
    assert ok is False
    ok, value, error = parse_guess("")
    assert ok is False


# NEW TEST: each difficulty should report the correct range.
def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
