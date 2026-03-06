from app import check_guess

def test_guess_less():
    assert check_guess(500, 700) == "less"

def test_guess_more():
    assert check_guess(500, 200) == "more"

def test_guess_correct():
    assert check_guess(500, 500) == "correct"

def test_zero_case():
    assert check_guess(0, 0) == "correct"

def test_negative_case():
    assert check_guess(-10, -20) == "more"
