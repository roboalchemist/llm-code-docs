# Source: https://boltons.readthedocs.io/en/latest/namedutils.html

Title: Lightweight containers — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/namedutils.html

Markdown Content:
`namedutils` - Lightweight containers[](https://boltons.readthedocs.io/en/latest/namedutils.html#module-boltons.namedutils "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

The `namedutils` module defines two lightweight container types: [`namedtuple`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedtuple "boltons.namedutils.namedtuple") and [`namedlist`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedlist "boltons.namedutils.namedlist"). Both are subtypes of built-in sequence types, which are very fast and efficient. They simply add named attribute accessors for specific indexes within themselves.

The [`namedtuple`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedtuple "boltons.namedutils.namedtuple") is identical to the built-in `collections.namedtuple`, with a couple of enhancements, including a `__repr__` more suitable to inheritance.

The [`namedlist`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedlist "boltons.namedutils.namedlist") is the mutable counterpart to the [`namedtuple`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedtuple "boltons.namedutils.namedtuple"), and is much faster and lighter-weight than full-blown [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)"). Consider this if you’re implementing nodes in a tree, graph, or other mutable data structure. If you want an even skinnier approach, you’ll probably have to look to C.

boltons.namedutils.namedlist(_typename_, _field\_names_, _verbose=False_, _rename=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/namedutils.html#namedlist)[](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedlist "Link to this definition")
Returns a new subclass of list with named fields.

>>> Point = namedlist('Point', ['x', 'y'])
>>> Point. __doc__                    # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with pos args or keywords
>>> p[0] + p[1]                     # indexable like a plain list
33
>>> x, y = p                        # unpack like a regular list
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessible by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)

boltons.namedutils.namedtuple(_typename_, _field\_names_, _verbose=False_, _rename=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/namedutils.html#namedtuple)[](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedtuple "Link to this definition")
Returns a new subclass of tuple with named fields.

>>> Point = namedtuple('Point', ['x', 'y'])
>>> Point. __doc__                    # docstring for the new class
'Point(x, y)'
>>> p = Point(11, y=22)             # instantiate with pos args or keywords
>>> p[0] + p[1]                     # indexable like a plain tuple
33
>>> x, y = p                        # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y                       # fields also accessible by name
33
>>> d = p._asdict()                 # convert to a dictionary
>>> d['x']
11
>>> Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
>>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)
