"""another tests"""
import pytest

def test_string_add_int_raise_exc(session_timer, return_string_module):
    """Assert string and int not added"""
    with pytest.raises(Exception) as e:
        assert return_string_module + 5
    assert str(e.value) == 'can only concatenate str (not "int") to str'
