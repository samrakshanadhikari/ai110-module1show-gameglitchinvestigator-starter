from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

def test_guess_too_high():
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")

def test_range_for_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_scales_with_difficulty():
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_parse_guess_rejects_decimal_input():
    assert parse_guess("4.2") == (False, None, "That is not a whole number.")

def test_update_score_never_goes_below_zero():
    assert update_score(0, "Too Low", 3) == 0
