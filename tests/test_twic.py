from lcl import twic, download

def test_twic_file():
    highest = 1560
    base_url = "https://theweekinchess.com/zips/"
    twic_pattern = "twic<<number>>g.zip"

    high = twic.get_highest_twic_issue(highest, base_url, twic_pattern)
    assert high > highest


def test_download():
    download_dir = "/Users/littlecapa/Downloads/tmp"
    unzip_dir = "/Users/littlecapa/Downloads/tmp"
    issue_number = 1561
    base_url = "https://theweekinchess.com/zips/"
    twic_pattern = "twic<<number>>g.zip"
    twic.download_twic_file(base_url, issue_number, download_dir, unzip_dir, twic_pattern)
    assert 1 == 1
    download.delete_all_files_in_directory(download_dir)