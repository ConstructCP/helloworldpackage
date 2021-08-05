import helloworld


def fail_test():
    raise Exception('Test failed')


def test_hello_world():
    assert helloworld.hello_world() == 'Hello world!'


def test_hello_world_with_arg():
    try:
        helloworld.hello_world(42)
    except TypeError:
        pass
    except:
        fail_test()
    else:
        fail_test()


def test_hello_by_name():
    assert helloworld.hello_by_name('Bill') == 'Hello, Bill!'
    assert helloworld.hello_by_name('Night City') == 'Hello, Night City!'
    assert helloworld.hello_by_name(42) == 'Hello, 42!'


def test_hello_by_name_without_arg():
    try:
        helloworld.hello_by_name()
    except TypeError:
        pass
    except:
        fail_test()
    else:
        fail_test()


if __name__ == '__main__':
    test_hello_world()
    test_hello_world_with_arg()
    test_hello_by_name()
    test_hello_by_name_without_arg()
