# Source: https://boltons.readthedocs.io/en/latest/iterutils.html

Title: itertools improvements — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/iterutils.html

Markdown Content:
`iterutils` - `itertools` improvements[](https://boltons.readthedocs.io/en/latest/iterutils.html#module-boltons.iterutils "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

[`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "(in Python v3.14)") is full of great examples of Python generator usage. However, there are still some critical gaps. `iterutils` fills many of those gaps with featureful, tested, and Pythonic solutions.

Many of the functions below have two versions, one which returns an iterator (denoted by the `*_iter` naming pattern), and a shorter-named convenience form that returns a list. Some of the following are based on examples in itertools docs.

Sections

*   [Iteration](https://boltons.readthedocs.io/en/latest/iterutils.html#iteration)

*   [Stripping and splitting](https://boltons.readthedocs.io/en/latest/iterutils.html#stripping-and-splitting)

*   [Nested](https://boltons.readthedocs.io/en/latest/iterutils.html#nested)

*   [Numeric](https://boltons.readthedocs.io/en/latest/iterutils.html#numeric)

*   [Categorization](https://boltons.readthedocs.io/en/latest/iterutils.html#categorization)

*   [Sorting](https://boltons.readthedocs.io/en/latest/iterutils.html#sorting)

*   [Reduction](https://boltons.readthedocs.io/en/latest/iterutils.html#reduction)

*   [Type Checks](https://boltons.readthedocs.io/en/latest/iterutils.html#type-checks)

[Iteration](https://boltons.readthedocs.io/en/latest/iterutils.html#id3)[](https://boltons.readthedocs.io/en/latest/iterutils.html#iteration "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

These are generators and convenient [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")-producing counterparts comprising several common patterns of iteration not present in the standard library.

boltons.iterutils.chunked(_src_, _size_, _count=None_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#chunked)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.chunked "Link to this definition")
Returns a list of _count_ chunks, each with _size_ elements, generated from iterable _src_. If _src_ is not evenly divisible by _size_, the final chunk will have fewer than _size_ elements. Provide the _fill_ keyword argument to provide a pad value and enable padding, otherwise no padding will take place.

>>> chunked(range(10), 3)
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
>>> chunked(range(10), 3, fill=None)
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, None, None]]
>>> chunked(range(10), 3, count=2)
[[0, 1, 2], [3, 4, 5]]

See [`chunked_iter()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.chunked_iter "boltons.iterutils.chunked_iter") for more info.

boltons.iterutils.chunked_iter(_src_, _size_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#chunked_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.chunked_iter "Link to this definition")
Generates _size_-sized chunks from _src_ iterable. Unless the optional _fill_ keyword argument is provided, iterables not evenly divisible by _size_ will have a final chunk that is smaller than _size_.

>>> list(chunked_iter(range(10), 3))
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
>>> list(chunked_iter(range(10), 3, fill=None))
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, None, None]]

Note that `fill=None` in fact uses `None` as the fill value.

boltons.iterutils.chunk_ranges(_input\_size_, _chunk\_size_, _input\_offset=0_, _overlap\_size=0_, _align=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#chunk_ranges)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.chunk_ranges "Link to this definition")
Generates _chunk\_size_-sized chunk ranges for an input with length _input\_size_. Optionally, a start of the input can be set via _input\_offset_, and and overlap between the chunks may be specified via _overlap\_size_. Also, if _align_ is set to _True_, any items with _i % (chunk\_size-overlap\_size) == 0_ are always at the beginning of the chunk.

Returns an iterator of (start, end) tuples, one tuple per chunk.

>>> list(chunk_ranges(input_offset=10, input_size=10, chunk_size=5))
[(10, 15), (15, 20)]
>>> list(chunk_ranges(input_offset=10, input_size=10, chunk_size=5, overlap_size=1))
[(10, 15), (14, 19), (18, 20)]
>>> list(chunk_ranges(input_offset=10, input_size=10, chunk_size=5, overlap_size=2))
[(10, 15), (13, 18), (16, 20)]

>>> list(chunk_ranges(input_offset=4, input_size=15, chunk_size=5, align=False))
[(4, 9), (9, 14), (14, 19)]
>>> list(chunk_ranges(input_offset=4, input_size=15, chunk_size=5, align=True))
[(4, 5), (5, 10), (10, 15), (15, 19)]

>>> list(chunk_ranges(input_offset=2, input_size=15, chunk_size=5, overlap_size=1, align=False))
[(2, 7), (6, 11), (10, 15), (14, 17)]
>>> list(chunk_ranges(input_offset=2, input_size=15, chunk_size=5, overlap_size=1, align=True))
[(2, 5), (4, 9), (8, 13), (12, 17)]
>>> list(chunk_ranges(input_offset=3, input_size=15, chunk_size=5, overlap_size=1, align=True))
[(3, 5), (4, 9), (8, 13), (12, 17), (16, 18)]

boltons.iterutils.pairwise(_src_, _end=Sentinel('\_UNSET')_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#pairwise)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.pairwise "Link to this definition")
Convenience function for calling [`windowed()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.windowed "boltons.iterutils.windowed") on _src_, with _size_ set to 2.

>>> pairwise(range(5))
[(0, 1), (1, 2), (2, 3), (3, 4)]
>>> pairwise([])
[]

Unless _end_ is set, the number of pairs is always one less than the number of elements in the iterable passed in, except on an empty input, which will return an empty list.

With _end_ set, a number of pairs equal to the length of _src_ is returned, with the last item of the last pair being equal to _end_.

>>> list(pairwise(range(3), end=None))
[(0, 1), (1, 2), (2, None)]

This way, _end_ values can be useful as sentinels to signal the end of the iterable.

boltons.iterutils.pairwise_iter(_src_, _end=Sentinel('\_UNSET')_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#pairwise_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.pairwise_iter "Link to this definition")
Convenience function for calling [`windowed_iter()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.windowed_iter "boltons.iterutils.windowed_iter") on _src_, with _size_ set to 2.

>>> list(pairwise_iter(range(5)))
[(0, 1), (1, 2), (2, 3), (3, 4)]
>>> list(pairwise_iter([]))
[]

Unless _end_ is set, the number of pairs is always one less than the number of elements in the iterable passed in, or zero, when _src_ is empty.

With _end_ set, a number of pairs equal to the length of _src_ is returned, with the last item of the last pair being equal to _end_.

>>> list(pairwise_iter(range(3), end=None))
[(0, 1), (1, 2), (2, None)]

This way, _end_ values can be useful as sentinels to signal the end of the iterable. For infinite iterators, setting _end_ has no effect.

boltons.iterutils.windowed(_src_, _size_, _fill=Sentinel('\_UNSET')_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#windowed)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.windowed "Link to this definition")
Returns tuples with exactly length _size_. If _fill_ is unset and the iterable is too short to make a window of length _size_, no tuples are returned. See [`windowed_iter()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.windowed_iter "boltons.iterutils.windowed_iter") for more.

boltons.iterutils.windowed_iter(_src_, _size_, _fill=Sentinel('\_UNSET')_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#windowed_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.windowed_iter "Link to this definition")
Returns tuples with length _size_ which represent a sliding window over iterable _src_.

>>> list(windowed_iter(range(7), 3))
[(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

If _fill_ is unset, and the iterable is too short to make a window of length _size_, then no window tuples are returned.

>>> list(windowed_iter(range(3), 5))
[]

With _fill_ set, the iterator always yields a number of windows equal to the length of the _src_ iterable.

>>> windowed(range(4), 3, fill=None)
[(0, 1, 2), (1, 2, 3), (2, 3, None), (3, None, None)]

This way, _fill_ values can be useful to signal the end of the iterable. For infinite iterators, setting _fill_ has no effect.

boltons.iterutils.unique(_src_, _key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#unique)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.unique "Link to this definition")
`unique()` returns a list of unique values, as determined by _key_, in the order they first appeared in the input iterable, _src_.

>>> ones_n_zeros = '11010110001010010101010'
>>> ''.join(unique(ones_n_zeros))
'10'

See [`unique_iter()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.unique_iter "boltons.iterutils.unique_iter") docs for more details.

boltons.iterutils.unique_iter(_src_, _key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#unique_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.unique_iter "Link to this definition")
Yield unique elements from the iterable, _src_, based on _key_, in the order in which they first appeared in _src_.

>>> repetitious = [1, 2, 3] * 10
>>> list(unique_iter(repetitious))
[1, 2, 3]

By default, _key_ is the object itself, but _key_ can either be a callable or, for convenience, a string name of the attribute on which to uniqueify objects, falling back on identity when the attribute is not present.

>>> pleasantries = ['hi', 'hello', 'ok', 'bye', 'yes']
>>> list(unique_iter(pleasantries, key=lambda x: len(x)))
['hi', 'hello', 'bye']

boltons.iterutils.redundant(_src_, _key=None_, _groups=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#redundant)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.redundant "Link to this definition")
The complement of [`unique()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.unique "boltons.iterutils.unique").

By default returns non-unique/duplicate values as a list of the _first_ redundant value in _src_. Pass `groups=True` to get groups of all values with redundancies, ordered by position of the first redundant value. This is useful in conjunction with some normalizing _key_ function.

>>> redundant([1, 2, 3, 4])
[]
>>> redundant([1, 2, 3, 2, 3, 3, 4])
[2, 3]
>>> redundant([1, 2, 3, 2, 3, 3, 4], groups=True)
[[2, 2], [3, 3, 3]]

An example using a _key_ function to do case-insensitive redundancy detection.

>>> redundant(['hi', 'Hi', 'HI', 'hello'], key=str.lower)
['Hi']
>>> redundant(['hi', 'Hi', 'HI', 'hello'], groups=True, key=str.lower)
[['hi', 'Hi', 'HI']]

_key_ should also be used when the values in _src_ are not hashable.

Note

This output of this function is designed for reporting duplicates in contexts when a unique input is desired. Due to the grouped return type, there is no streaming equivalent of this function for the time being.

[Stripping and splitting](https://boltons.readthedocs.io/en/latest/iterutils.html#id4)[](https://boltons.readthedocs.io/en/latest/iterutils.html#stripping-and-splitting "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A couple of [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")-inspired mechanics that have come in handy on iterables, too:

boltons.iterutils.split(_src_, _sep=None_, _maxsplit=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#split)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.split "Link to this definition")
Splits an iterable based on a separator. Like [`str.split()`](https://docs.python.org/3/library/stdtypes.html#str.split "(in Python v3.14)"), but for all iterables. Returns a list of lists.

>>> split(['hi', 'hello', None, None, 'sup', None, 'soap', None])
[['hi', 'hello'], ['sup'], ['soap']]

See [`split_iter()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.split_iter "boltons.iterutils.split_iter") docs for more info.

boltons.iterutils.split_iter(_src_, _sep=None_, _maxsplit=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#split_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.split_iter "Link to this definition")
Splits an iterable based on a separator, _sep_, a max of _maxsplit_ times (no max by default). _sep_ can be:

> *   a single value
> 
> *   an iterable of separators
> 
> *   a single-argument callable that returns True when a separator is encountered

`split_iter()` yields lists of non-separator values. A separator will never appear in the output.

>>> list(split_iter(['hi', 'hello', None, None, 'sup', None, 'soap', None]))
[['hi', 'hello'], ['sup'], ['soap']]

Note that `split_iter` is based on `str.split()`, so if _sep_ is `None`, `split()`**groups** separators. If empty lists are desired between two contiguous `None` values, simply use `sep=[None]`:

>>> list(split_iter(['hi', 'hello', None, None, 'sup', None]))
[['hi', 'hello'], ['sup']]
>>> list(split_iter(['hi', 'hello', None, None, 'sup', None], sep=[None]))
[['hi', 'hello'], [], ['sup'], []]

Using a callable separator:

>>> falsy_sep = lambda x: not x
>>> list(split_iter(['hi', 'hello', None, '', 'sup', False], falsy_sep))
[['hi', 'hello'], [], ['sup'], []]

See [`split()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.split "boltons.iterutils.split") for a list-returning version.

boltons.iterutils.strip(_iterable_, _strip\_value=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#strip)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.strip "Link to this definition")
Strips values from the beginning and end of an iterable. Stripped items will match the value of the argument strip_value. Functionality is analogous to that of the method str.strip. Returns a list.

>>> strip(['Fu', 'Foo', 'Bar', 'Bam', 'Fu'], 'Fu')
['Foo', 'Bar', 'Bam']

boltons.iterutils.strip_iter(_iterable_, _strip\_value=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#strip_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.strip_iter "Link to this definition")
Strips values from the beginning and end of an iterable. Stripped items will match the value of the argument strip_value. Functionality is analogous to that of the method str.strip. Returns a generator.

>>> list(strip_iter(['Fu', 'Foo', 'Bar', 'Bam', 'Fu'], 'Fu'))
['Foo', 'Bar', 'Bam']

boltons.iterutils.lstrip(_iterable_, _strip\_value=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#lstrip)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.lstrip "Link to this definition")
Strips values from the beginning of an iterable. Stripped items will match the value of the argument strip_value. Functionality is analogous to that of the method str.lstrip. Returns a list.

>>> lstrip(['Foo', 'Bar', 'Bam'], 'Foo')
['Bar', 'Bam']

boltons.iterutils.lstrip_iter(_iterable_, _strip\_value=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#lstrip_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.lstrip_iter "Link to this definition")
Strips values from the beginning of an iterable. Stripped items will match the value of the argument strip_value. Functionality is analogous to that of the method str.lstrip. Returns a generator.

>>> list(lstrip_iter(['Foo', 'Bar', 'Bam'], 'Foo'))
['Bar', 'Bam']

boltons.iterutils.rstrip(_iterable_, _strip\_value=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#rstrip)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.rstrip "Link to this definition")
Strips values from the end of an iterable. Stripped items will match the value of the argument strip_value. Functionality is analogous to that of the method str.rstrip. Returns a list.

>>> rstrip(['Foo', 'Bar', 'Bam'], 'Bam')
['Foo', 'Bar']

boltons.iterutils.rstrip_iter(_iterable_, _strip\_value=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#rstrip_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.rstrip_iter "Link to this definition")
Strips values from the end of an iterable. Stripped items will match the value of the argument strip_value. Functionality is analogous to that of the method str.rstrip. Returns a generator.

>>> list(rstrip_iter(['Foo', 'Bar', 'Bam'], 'Bam'))
['Foo', 'Bar']

[Nested](https://boltons.readthedocs.io/en/latest/iterutils.html#id5)[](https://boltons.readthedocs.io/en/latest/iterutils.html#nested "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Nested data structures are common. Yet virtually all of Python’s compact iteration tools work with flat data: list comprehensions, map/filter, generator expressions, itertools, even other iterutils.

The functions below make working with nested iterables and other containers as succinct and powerful as Python itself.

boltons.iterutils.remap(_root_, _visit=<function default\_visit>_, _enter=<function default\_enter>_, _exit=<function default\_exit>_, _cache:bool=True_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#remap)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "Link to this definition")
The remap (“recursive map”) function is used to traverse and transform nested structures. Lists, tuples, sets, and dictionaries are just a few of the data structures nested into heterogeneous tree-like structures that are so common in programming. Unfortunately, Python’s built-in ways to manipulate collections are almost all flat. List comprehensions may be fast and succinct, but they do not recurse, making it tedious to apply quick changes or complex transforms to real-world data.

remap goes where list comprehensions cannot.

Here’s an example of removing all Nones from some data:

>>> from pprint import pprint
>>> reviews = {'Star Trek': {'TNG': 10, 'DS9': 8.5, 'ENT': None},
...            'Babylon 5': 6, 'Dr. Who': None}
>>> pprint(remap(reviews, lambda p, k, v: v is not None))
{'Babylon 5': 6, 'Star Trek': {'DS9': 8.5, 'TNG': 10}}

Notice how both Nones have been removed despite the nesting in the dictionary. Not bad for a one-liner, and that’s just the beginning. See [this remap cookbook](http://sedimental.org/remap.html) for more delicious recipes.

remap takes four main arguments: the object to traverse and three optional callables which determine how the remapped object will be created.

Parameters:
*   **root** – The target object to traverse. By default, remap supports iterables like [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"), [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), and [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)"), but any object traversable by _enter_ will work.

*   **visit** (_callable_) –

This function is called on every item in _root_. It must accept three positional arguments, _path_, _key_, and _value_. _path_ is simply a tuple of parents’ keys. _visit_ should return the new key-value pair. It may also return `True` as shorthand to keep the old item unmodified, or `False` to drop the item from the new structure. _visit_ is called after _enter_, on the new parent.

The _visit_ function is called for every item in root, including duplicate items. For traversable values, it is called on the new parent object, after all its children have been visited. The default visit behavior simply returns the key-value pair unmodified.

*   **enter** (_callable_) –

This function controls which items in _root_ are traversed. It accepts the same arguments as _visit_: the path, the key, and the value of the current item. It returns a pair of the blank new parent, and an iterator over the items which should be visited. If `False` is returned instead of an iterator, the value will not be traversed.

The _enter_ function is only called once per unique value. The default enter behavior support mappings, sequences, and sets. Strings and all other iterables will not be traversed.

*   **exit** (_callable_) –

This function determines how to handle items once they have been visited. It gets the same three arguments as the other functions – _path_, _key_, _value_ – plus two more: the blank new parent object returned from _enter_, and a list of the new items, as remapped by _visit_.

Like _enter_, the _exit_ function is only called once per unique value. The default exit behavior is to simply add all new items to the new parent, e.g., using [`list.extend()`](https://docs.python.org/3/library/stdtypes.html#list.extend "(in Python v3.14)") and [`dict.update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "(in Python v3.14)") to add to the new parent. Immutable objects, such as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") or `namedtuple`, must be recreated from scratch, but use the same type as the new parent passed back from the _enter_ function.

*   **cache** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Controls whether to cache transformed objects. Uses object identity for the cache. For example this is turned off for applications like research which need to traverse all trees.

*   **reraise_visit** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – A pragmatic convenience for the _visit_ callable. When set to `False`, remap ignores any errors raised by the _visit_ callback. Items causing exceptions are kept. See examples for more details.

*   **trace** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Pass `trace=True` to print out the entire traversal. Or pass a tuple of `'visit'`, `'enter'`, or `'exit'` to print only the selected events.

remap is designed to cover the majority of cases with just the _visit_ callable. While passing in multiple callables is very empowering, remap is designed so very few cases should require passing more than one function.

When passing _enter_ and _exit_, it’s common and easiest to build on the default behavior. Simply add 
```
from boltons.iterutils import
default_enter
```
 (or `default_exit`), and have your enter/exit function call the default behavior before or after your custom logic. See [this example](http://sedimental.org/remap.html#sort_all_lists).

Duplicate and self-referential objects (aka reference loops) are automatically handled internally, [as shown here](http://sedimental.org/remap.html#corner_cases).

boltons.iterutils.get_path(_root_, _path_, _default=Sentinel('\_UNSET')_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#get_path)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.get_path "Link to this definition")
Retrieve a value from a nested object via a tuple representing the lookup path.

>>> root = {'a': {'b': {'c': [[1], [2], [3]]}}}
>>> get_path(root, ('a', 'b', 'c', 2, 0))
3

The path tuple format is intentionally consistent with that of [`remap()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "boltons.iterutils.remap"), but a single dotted string can also be passed.

One of get_path’s chief aims is improved error messaging. EAFP is great, but the error messages are not.

For instance, `root['a']['b']['c'][2][1]` gives back `IndexError: list index out of range`

What went out of range where? get_path currently raises 
```
PathAccessError: could not access 2 from path ('a', 'b', 'c', 2,
1), got error: IndexError('list index out of range',)
```
, a subclass of IndexError and KeyError.

You can also pass a default that covers the entire operation, should the lookup fail at any level.

Parameters:
*   **root** – The target nesting of dictionaries, lists, or other objects supporting `__getitem__`.

*   **path** ([_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")) – A sequence of strings and integers to be successively looked up within _root_. A dot-separated (`a.b`) string may also be passed.

*   **default** – The value to be returned should any `PathAccessError` exceptions be raised.

boltons.iterutils.research(_root_, _query=<function<lambda>>_, _reraise=False_, _enter=<function default\_enter>_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#research)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.research "Link to this definition")
The [`research()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.research "boltons.iterutils.research") function uses [`remap()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "boltons.iterutils.remap") to recurse over any data nested in _root_, and find values which match a given criterion, specified by the _query_ callable.

Results are returned as a list of `(path, value)` pairs. The paths are tuples in the same format accepted by [`get_path()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.get_path "boltons.iterutils.get_path"). This can be useful for comparing values nested in two or more different structures.

Here’s a simple example that finds all integers:

>>> root = {'a': {'b': 1, 'c': (2, 'd', 3)}, 'e': None}
>>> res = research(root, query=lambda p, k, v: isinstance(v, int))
>>> print(sorted(res))
[(('a', 'b'), 1), (('a', 'c', 0), 2), (('a', 'c', 2), 3)]

Note how _query_ follows the same, familiar `path, key, value` signature as the `visit` and `enter` functions on [`remap()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "boltons.iterutils.remap"), and returns a [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)").

Parameters:
*   **root** – The target object to search. Supports the same types of objects as [`remap()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "boltons.iterutils.remap"), including [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)"), [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), and [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)").

*   **query** (_callable_) – The function called on every object to determine whether to include it in the search results. The callable must accept three arguments, _path_, _key_, and _value_, commonly abbreviated _p_, _k_, and _v_, same as _enter_ and _visit_ from [`remap()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "boltons.iterutils.remap").

*   **reraise** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to reraise exceptions raised by _query_ or to simply drop the result that caused the error.

With [`research()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.research "boltons.iterutils.research") it’s easy to inspect the details of a data structure, like finding values that are at a certain depth (using `len(p)`) and much more. If more advanced functionality is needed, check out the code and make your own [`remap()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "boltons.iterutils.remap") wrapper, and consider [submitting a patch](https://github.com/mahmoud/boltons/pulls)!

boltons.iterutils.flatten(_iterable_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#flatten)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.flatten "Link to this definition")
`flatten()` returns a collapsed list of all the elements from _iterable_ while collapsing any nested iterables.

>>> nested = [[1, 2], [[3], [4, 5]]]
>>> flatten(nested)
[1, 2, 3, 4, 5]

boltons.iterutils.flatten_iter(_iterable_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#flatten_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.flatten_iter "Link to this definition")
`flatten_iter()` yields all the elements from _iterable_ while collapsing any nested iterables.

>>> nested = [[1, 2], [[3], [4, 5]]]
>>> list(flatten_iter(nested))
[1, 2, 3, 4, 5]

[Numeric](https://boltons.readthedocs.io/en/latest/iterutils.html#id6)[](https://boltons.readthedocs.io/en/latest/iterutils.html#numeric "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Number sequences are an obvious target of Python iteration, such as the built-in `range()`, and [`itertools.count()`](https://docs.python.org/3/library/itertools.html#itertools.count "(in Python v3.14)"). Like the [Iteration](https://boltons.readthedocs.io/en/latest/iterutils.html#iteration) members above, these return iterators and lists, but take numeric inputs instead of iterables.

boltons.iterutils.backoff(_start_, _stop_, _count=None_, _factor=2.0_, _jitter=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#backoff)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.backoff "Link to this definition")
Returns a list of geometrically-increasing floating-point numbers, suitable for usage with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). Exactly like [`backoff_iter()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.backoff_iter "boltons.iterutils.backoff_iter"), but without the `'repeat'` option for _count_. See [`backoff_iter()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.backoff_iter "boltons.iterutils.backoff_iter") for more details.

>>> backoff(1, 10)
[1.0, 2.0, 4.0, 8.0, 10.0]

boltons.iterutils.backoff_iter(_start_, _stop_, _count=None_, _factor=2.0_, _jitter=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#backoff_iter)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.backoff_iter "Link to this definition")
Generates a sequence of geometrically-increasing floats, suitable for usage with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). Starts with _start_, increasing by _factor_ until _stop_ is reached, optionally stopping iteration once _count_ numbers are yielded. _factor_ defaults to 2. In general retrying with properly-configured backoff creates a better-behaved component for a larger service ecosystem.

>>> list(backoff_iter(1.0, 10.0, count=5))
[1.0, 2.0, 4.0, 8.0, 10.0]
>>> list(backoff_iter(1.0, 10.0, count=8))
[1.0, 2.0, 4.0, 8.0, 10.0, 10.0, 10.0, 10.0]
>>> list(backoff_iter(0.25, 100.0, factor=10))
[0.25, 2.5, 25.0, 100.0]

A simplified usage example:

for timeout in backoff_iter(0.25, 5.0):
    try:
        res = network_call()
        break
    except Exception as e:
        log(e)
        time.sleep(timeout)

An enhancement for large-scale systems would be to add variation, or _jitter_, to timeout values. This is done to avoid a thundering herd on the receiving end of the network call.

Finally, for _count_, the special value `'repeat'` can be passed to continue yielding indefinitely.

Parameters:
*   **start** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Positive number for baseline.

*   **stop** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Positive number for maximum.

*   **count** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Number of steps before stopping iteration. Defaults to the number of steps between _start_ and _stop_. Pass the string, ‘repeat’, to continue iteration indefinitely.

*   **factor** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Rate of exponential increase. Defaults to 2.0, e.g., [1, 2, 4, 8, 16].

*   **jitter** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – A factor between -1.0 and 1.0, used to uniformly randomize and thus spread out timeouts in a distributed system, avoiding rhythm effects. Positive values use the base backoff curve as a maximum, negative values use the curve as a minimum. Set to 1.0 or True for a jitter approximating Ethernet’s time-tested backoff solution. Defaults to False.

boltons.iterutils.frange(_stop_, _start=None_, _step=1.0_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#frange)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.frange "Link to this definition")
A `range()` clone for float-based ranges.

>>> frange(5)
[0.0, 1.0, 2.0, 3.0, 4.0]
>>> frange(6, step=1.25)
[0.0, 1.25, 2.5, 3.75, 5.0]
>>> frange(100.5, 101.5, 0.25)
[100.5, 100.75, 101.0, 101.25]
>>> frange(5, 0)
[]
>>> frange(5, 0, step=-1.25)
[5.0, 3.75, 2.5, 1.25]

boltons.iterutils.xfrange(_stop_, _start=None_, _step=1.0_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#xfrange)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.xfrange "Link to this definition")
Same as [`frange()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.frange "boltons.iterutils.frange"), but generator-based instead of returning a list.

>>> tuple(xfrange(1, 3, step=0.75))
(1.0, 1.75, 2.5)

See [`frange()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.frange "boltons.iterutils.frange") for more details.

[Categorization](https://boltons.readthedocs.io/en/latest/iterutils.html#id7)[](https://boltons.readthedocs.io/en/latest/iterutils.html#categorization "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These functions operate on iterables, dividing into groups based on a given condition.

boltons.iterutils.bucketize(_src_, _key=<class'bool'>_, _value\_transform=None_, _key\_filter=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#bucketize)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.bucketize "Link to this definition")
Group values in the _src_ iterable by the value returned by _key_.

>>> bucketize(range(5))
{False: [0], True: [1, 2, 3, 4]}
>>> is_odd = lambda x: x % 2 == 1
>>> bucketize(range(5), is_odd)
{False: [0, 2, 4], True: [1, 3]}

_key_ is [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") by default, but can either be a callable or a string or a list if it is a string, it is the name of the attribute on which to bucketize objects.

>>> bucketize([1+1j, 2+2j, 1, 2], key='real')
{1.0: [(1+1j), 1], 2.0: [(2+2j), 2]}

if _key_ is a list, it contains the buckets where to put each object

>>> bucketize([1,2,365,4,98],key=[0,1,2,0,2])
{0: [1, 4], 1: [2], 2: [365, 98]}

Value lists are not deduplicated:

>>> bucketize([None, None, None, 'hello'])
{False: [None, None, None], True: ['hello']}

Bucketize into more than 3 groups

>>> bucketize(range(10), lambda x: x % 3)
{0: [0, 3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]}

`bucketize` has a couple of advanced options useful in certain cases. _value\_transform_ can be used to modify values as they are added to buckets, and _key\_filter_ will allow excluding certain buckets from being collected.

>>> bucketize(range(5), value_transform=lambda x: x*x)
{False: [0], True: [1, 4, 9, 16]}

>>> bucketize(range(10), key=lambda x: x % 3, key_filter=lambda k: k % 3 != 1)
{0: [0, 3, 6, 9], 2: [2, 5, 8]}

Note in some of these examples there were at most two keys, `True` and `False`, and each key present has a list with at least one item. See [`partition()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.partition "boltons.iterutils.partition") for a version specialized for binary use cases.

boltons.iterutils.partition(_src_, _key=<class'bool'>_, _*keys_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#partition)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.partition "Link to this definition")
No relation to [`str.partition()`](https://docs.python.org/3/library/stdtypes.html#str.partition "(in Python v3.14)"), `partition` is like [`bucketize()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.bucketize "boltons.iterutils.bucketize"), but for added convenience returns a collection for each predicate passed.

`partition` now accepts multiple _key_ functions and will return `N + 1` lists for `N` predicates. Each value from _src_ is placed into the first list whose predicate evaluates to `True` with values that match none of the predicates placed in the last list.

>>> nonempty, empty = partition(['', '', 'hi', '', 'bye'])
>>> nonempty
['hi', 'bye']

_key_ defaults to [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"), but can be carefully overridden to use either a function that returns either `True` or `False` or a string name of the attribute on which to partition objects.

>>> import string
>>> is_digit = lambda x: x in string.digits
>>> decimal_digits, hexletters = partition(string.hexdigits, is_digit)
>>> ''.join(decimal_digits), ''.join(hexletters)
('0123456789', 'abcdefABCDEF')

Multiple predicates may be supplied to divide into more buckets:

>>> positive, negative, zero = partition(range(-1, 2),
...                                     lambda i: i > 0,
...                                     lambda i: i < 0)
>>> positive, negative, zero
([1], [-1], [0])

[Sorting](https://boltons.readthedocs.io/en/latest/iterutils.html#id8)[](https://boltons.readthedocs.io/en/latest/iterutils.html#sorting "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The built-in [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "(in Python v3.14)") is great, but what do you do when you want to partially override the sort order?

boltons.iterutils.soft_sorted(_iterable_, _first=None_, _last=None_, _key=None_, _reverse=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#soft_sorted)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.soft_sorted "Link to this definition")
For when you care about the order of some elements, but not about others.

Use this to float to the top and/or sink to the bottom a specific ordering, while sorting the rest of the elements according to normal [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "(in Python v3.14)") rules.

>>> soft_sorted(['two', 'b', 'one', 'a'], first=['one', 'two'])
['one', 'two', 'a', 'b']
>>> soft_sorted(range(7), first=[6, 15], last=[2, 4], reverse=True)
[6, 5, 3, 1, 0, 2, 4]
>>> import string
>>> ''.join(soft_sorted(string.hexdigits, first='za1', last='b', key=str.lower))
'aA1023456789cCdDeEfFbB'

Parameters:
*   **iterable** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list or other iterable to sort.

*   **first** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A sequence to enforce for elements which should appear at the beginning of the returned list.

*   **last** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A sequence to enforce for elements which should appear at the end of the returned list.

*   **key** (_callable_) – Callable used to generate a comparable key for each item to be sorted, same as the key in [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "(in Python v3.14)"). Note that entries in _first_ and _last_ should be the keys for the items. Defaults to passthrough/the identity function.

*   **reverse** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether or not elements not explicitly ordered by _first_ and _last_ should be in reverse order or not.

Returns a new list in sorted order.

boltons.iterutils.untyped_sorted(_iterable_, _key=None_, _reverse=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#untyped_sorted)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.untyped_sorted "Link to this definition")
A version of [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "(in Python v3.14)") which will happily sort an iterable of heterogeneous types and return a new list, similar to legacy Python’s behavior.

>>> untyped_sorted(['abc', 2.0, 1, 2, 'def'])
[1, 2.0, 2, 'abc', 'def']

Note how mutually orderable types are sorted as expected, as in the case of the integers and floats above.

Note

Results may vary across Python versions and builds, but the function will produce a sorted list, except in the case of explicitly unorderable objects.

[Reduction](https://boltons.readthedocs.io/en/latest/iterutils.html#id9)[](https://boltons.readthedocs.io/en/latest/iterutils.html#reduction "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

`reduce()` is a powerful function, but it is also very open-ended and not always the most readable. The standard library recognized this with the addition of [`sum()`](https://docs.python.org/3/library/functions.html#sum "(in Python v3.14)"), [`all()`](https://docs.python.org/3/library/functions.html#all "(in Python v3.14)"), and [`any()`](https://docs.python.org/3/library/functions.html#any "(in Python v3.14)"). All these functions take a basic operator (`+`, `and`, and `or`) and use the operator to turn an iterable into a single value.

Functions in this category follow that same spirit, turning iterables like lists into single values:

boltons.iterutils.one(_src_, _default=None_, _key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#one)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.one "Link to this definition")
Along the same lines as builtins, [`all()`](https://docs.python.org/3/library/functions.html#all "(in Python v3.14)") and [`any()`](https://docs.python.org/3/library/functions.html#any "(in Python v3.14)"), and similar to [`first()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.first "boltons.iterutils.first"), `one()` returns the single object in the given iterable _src_ that evaluates to `True`, as determined by callable _key_. If unset, _key_ defaults to [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"). If no such objects are found, _default_ is returned. If _default_ is not passed, `None` is returned.

If _src_ has more than one object that evaluates to `True`, or if there is no object that fulfills such condition, return _default_. It’s like an [XOR](https://en.wikipedia.org/wiki/Exclusive_or) over an iterable.

>>> one((True, False, False))
True
>>> one((True, False, True))
>>> one((0, 0, 'a'))
'a'
>>> one((0, False, None))
>>> one((True, True), default=False)
False
>>> bool(one(('', 1)))
True
>>> one((10, 20, 30, 42), key=lambda i: i > 40)
42

See [Martín Gaitán’s original repo](https://github.com/mgaitan/one) for further use cases.

boltons.iterutils.first(_iterable_, _default=None_, _key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#first)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.first "Link to this definition")
Return first element of _iterable_ that evaluates to `True`, else return `None` or optional _default_. Similar to [`one()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.one "boltons.iterutils.one").

>>> first([0, False, None, [], (), 42])
42
>>> first([0, False, None, [], ()]) is None
True
>>> first([0, False, None, [], ()], default='ohai')
'ohai'
>>> import re
>>> m = first(re.match(regex, 'abc') for regex in ['b.*', 'a(.*)'])
>>> m.group(1)
'bc'

The optional _key_ argument specifies a one-argument predicate function like that used for _filter()_. The _key_ argument, if supplied, should be in keyword form. For example, finding the first even number in an iterable:

>>> first([1, 1, 3, 4, 5], key=lambda x: x % 2 == 0)
4

Contributed by Hynek Schlawack, author of [the original standalone module](https://github.com/hynek/first).

boltons.iterutils.same(_iterable_, _ref=Sentinel('\_UNSET')_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#same)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.same "Link to this definition")
`same()` returns `True` when all values in _iterable_ are equal to one another, or optionally a reference value, _ref_. Similar to [`all()`](https://docs.python.org/3/library/functions.html#all "(in Python v3.14)") and [`any()`](https://docs.python.org/3/library/functions.html#any "(in Python v3.14)") in that it evaluates an iterable and returns a [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"). `same()` returns `True` for empty iterables.

>>> same([])
True
>>> same([1])
True
>>> same(['a', 'a', 'a'])
True
>>> same(range(20))
False
>>> same([[], []])
True
>>> same([[], []], ref='test')
False

[Type Checks](https://boltons.readthedocs.io/en/latest/iterutils.html#id10)[](https://boltons.readthedocs.io/en/latest/iterutils.html#type-checks "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the same vein as the feature-checking builtin, [`callable()`](https://docs.python.org/3/library/functions.html#callable "(in Python v3.14)").

boltons.iterutils.is_iterable(_obj_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#is_iterable)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.is_iterable "Link to this definition")
Similar in nature to [`callable()`](https://docs.python.org/3/library/functions.html#callable "(in Python v3.14)"), `is_iterable` returns `True` if an object is [iterable](https://docs.python.org/2/glossary.html#term-iterable), `False` if not.

>>> is_iterable([])
True
>>> is_iterable(object())
False

boltons.iterutils.is_scalar(_obj_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#is_scalar)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.is_scalar "Link to this definition")
A near-mirror of [`is_iterable()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.is_iterable "boltons.iterutils.is_iterable"). Returns `False` if an object is an iterable container type. Strings are considered scalar as well, because strings are more often treated as whole values as opposed to iterables of 1-character substrings.

>>> is_scalar(object())
True
>>> is_scalar(range(10))
False
>>> is_scalar('hello')
True

boltons.iterutils.is_collection(_obj_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/iterutils.html#is_collection)[](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.is_collection "Link to this definition")
The opposite of [`is_scalar()`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.is_scalar "boltons.iterutils.is_scalar"). Returns `True` if an object is an iterable other than a string.

>>> is_collection(object())
False
>>> is_collection(range(10))
True
>>> is_collection('hello')
False
