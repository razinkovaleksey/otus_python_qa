"""another string tests"""

def test_string_fixture_length(session_timer, return_string_module):
    """assert string length"""
    assert len(return_string_module) == 10


def test_string_fixture_is_string(session_timer, return_string_module):
    """assert string type"""
    assert isinstance(return_string_module, str)
