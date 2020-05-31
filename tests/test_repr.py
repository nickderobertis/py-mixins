from mixins import ReprMixin

# TODO [$5ed3cc897e9fd40007ee1e3c]: more comprehensive tests for ReprMixin


def test_repr():
    class ExampleClass(ReprMixin):
        repr_cols = ['a']

        def __init__(self, a: int, b: str):
            self.a = a
            self.b = b

    obj = ExampleClass(1, 'hello')
    assert repr(obj) == '<ExampleClass(a=1)>'

