from lcl import gps

def test_haversine():
    assert gps.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 946.3876221719836

