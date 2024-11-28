from lcl import twic

def test_twic_file():
    highest = 1560
    base_url = "https://theweekinchess.com/zips/"
    twic_pattern = "twic<<number>>g.zip"

    high = twic.get_highest_twic_issue(highest, base_url, twic_pattern)
    assert high > highest
