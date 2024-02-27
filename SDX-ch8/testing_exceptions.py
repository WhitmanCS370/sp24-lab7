from mock_context import ContextFake

def subber(a, b):
    return a - b

def test_exceptions():
    with ContextFake("subber", value=1234) as fake:
        assert not(subber(2,3)== 1234)
        assert not(subber(2,3)== -1)

test_exceptions()