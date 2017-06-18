# -*- coding: utf-8 -*-
from apispec import utils


def test_load_yaml_from_docstring():
    def f():
        """
        Foo
            bar
            baz quux

        ---
        herp: 1
        derp: 2
        """
    result = utils.load_yaml_from_docstring(f.__doc__)
    assert result == {'herp': 1, 'derp': 2}


# from marshmallow.utils
def test_is_collection():
    assert utils.is_collection([1, 'foo', {}]) is True
    assert utils.is_collection(('foo', 2.3)) is True
    assert utils.is_collection({'foo': 'bar'}) is False
