from lcl import twic, download
import tempfile

def test_twic_file():
    highest = 1560
    base_url = "https://theweekinchess.com/zips/"
    twic_pattern = "twic<<number>>g.zip"

    high = twic.get_highest_twic_issue(highest, base_url, twic_pattern)
    assert high > highest


def test_download():
    with tempfile.TemporaryDirectory() as tmp_dir:
        issue_number = 1561
        base_url = "https://theweekinchess.com/zips/"
        twic_pattern = "twic<<number>>g.zip"
        twic.download_twic_file(base_url, issue_number, tmp_dir, tmp_dir, twic_pattern)
    assert 1 == 1
   