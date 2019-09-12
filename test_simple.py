"""simple tests"""


def test_string_concatenation(session_timer):
    """Assert string concatenation"""
    assert '5' + '5' == '55'


def test_int_addition(session_timer):
    """Assert integer addition"""
    assert 5 + 5 == 10


def test_random_int_interval(session_timer, return_random_int_char_function):
    """Assert random.randint return int that >= 0 and <= 9"""
    assert return_random_int_char_function <= 9 and return_random_int_char_function >= 0


def test_random_randint_return_int(session_timer, return_random_int_char_function):
    """Assert random.randint return int"""
    assert isinstance(return_random_int_char_function, int)


def test_add_key_to_dict(session_timer):
    mydict = {'name': 'Pupa', 'age': 32}
    mydict['weight'] = 72
    assert mydict['weight'] == 72


def test_list_to_set(session_timer):
    mylist = ['spam', 'eggs', 1, 0.88, 'spam']
    myset = set(mylist)
    assert myset == {'spam', 'eggs', 1, 0.88}


def test_string_to_list(session_timer):
    mystring = 'spam'
    mylist = list(mystring)
    assert mylist == ['s', 'p', 'a', 'm']
