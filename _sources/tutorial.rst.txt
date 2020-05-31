Getting started with mixins
**********************************

Install
=======

Install via::

    pip install mixins

Usage
=========

Subclass a Mixin class to gain its functionality:

This is a simple example of :py:class:`.ReprMixin`::

    from mixins.repr import ReprMixin

    class MyClass(ReprMixin):
        repr_cols = ['b']

        def __init__(self, a, b):
            self.a = a
            self.b = b

    >>> obj = MyClass(1, 2)
    >>> print(obj)
    <MyClass(b=2)>

