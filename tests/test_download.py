from lcl import download

def test_twic_file():
    assert download.existFile("https://theweekinchess.com/zips/twic1568g.zip") == True