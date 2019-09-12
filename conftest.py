import pytest
import datetime
import random
import string

@pytest.fixture(scope='session')
def session_timer(request):
    start_time = datetime.datetime.now()
    print('SESSION SCOPE FIXTURE: Test started')
    yield

    def fin():
        end_time = datetime.datetime.now()
        print('SESSION SCOPE FIXTURE: Test run time : %s' % (end_time - start_time))

    request.addfinalizer(fin)


@pytest.fixture(scope='function')
def return_random_int_char_function():
    random_int = random.randint(0, 9)
    print('FUNCTION SCOPE FIXTURE: Generated random int: %s' % random_int)
    return random_int


@pytest.fixture(scope='module')
def return_string_module():
    letters = string.ascii_lowercase
    mystring = ''.join(random.choice(letters) for i in range(10))
    print('MODULE SCOPE FIXTURE: Generated random string: %s' % mystring)
    return mystring
