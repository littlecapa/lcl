import re
from lcl.net_lib import get_local_ip

def is_valid_ip(ip: str) -> bool:
    """
    Check if the given string is a valid IPv4 address.
    """
    # Regular expression for IPv4 address
    ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

    # Check if it matches the pattern
    if not re.match(ip_pattern, ip):
        return False

    # Validate each octet is between 0 and 255
    octets = ip.split('.')
    return all(0 <= int(octet) <= 255 for octet in octets)


def test_is_valid_ip():
    """
    Test the is_valid_ip function with various input cases.
    """
    assert is_valid_ip(get_local_ip()) == True
