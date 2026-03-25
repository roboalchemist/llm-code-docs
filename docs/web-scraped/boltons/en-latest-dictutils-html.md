# Source: https://boltons.readthedocs.io/en/latest/dictutils.html

Title: Mapping types (OMD) — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/dictutils.html

Markdown Content:
`dictutils` - Mapping types (OMD)[](https://boltons.readthedocs.io/en/latest/dictutils.html#module-boltons.dictutils "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

Python has a very powerful mapping type at its core: the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") type. While versatile and featureful, the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") prioritizes simplicity and performance. As a result, it does not retain the order of item insertion [[1]](https://boltons.readthedocs.io/en/latest/dictutils.html#id2), nor does it store multiple values per key. It is a fast, unordered 1:1 mapping.

The [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict") contrasts to the built-in [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), as a relatively maximalist, ordered 1:n subtype of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"). Virtually every feature of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") has been retooled to be intuitive in the face of this added complexity. Additional methods have been added, such as [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "(in Python v3.14)")-like functionality.

A prime advantage of the [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict") (OMD) is its non-destructive nature. Data can be added to an [`OMD`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OMD "boltons.dictutils.OMD") without being rearranged or overwritten. The property can allow the developer to work more freely with the data, as well as make more assumptions about where input data will end up in the output, all without any extra work.

One great example of this is the `OMD.inverted()` method, which returns a new OMD with the values as keys and the keys as values. All the data and the respective order is still represented in the inverted form, all from an operation which would be outright wrong and reckless with a built-in [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") or [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "(in Python v3.14)").

The OMD has been performance tuned to be suitable for a wide range of usages, including as a basic unordered MultiDict. Special thanks to [Mark Williams](https://github.com/markrwilliams) for all his help.

_class_ boltons.dictutils.FrozenDict[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#FrozenDict)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict "Link to this definition")
An immutable dict subtype that is hashable and can itself be used as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") key or [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)") entry. What [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "(in Python v3.14)") is to [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)"), FrozenDict is to [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)").

There was once an attempt to introduce such a type to the standard library, but it was rejected: [PEP 416](https://www.python.org/dev/peps/pep-0416/).

Because FrozenDict is a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") subtype, it automatically works everywhere a dict would, including JSON serialization.

clear(_*a_, _**kw_)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict.clear "Link to this definition")
raises a TypeError, because FrozenDicts are immutable

_classmethod_ fromkeys(_keys_, _value=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#FrozenDict.fromkeys)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict.fromkeys "Link to this definition")
Create a new dictionary with keys from iterable and values set to value.

pop(_*a_, _**kw_)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict.pop "Link to this definition")
raises a TypeError, because FrozenDicts are immutable

popitem(_*a_, _**kw_)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict.popitem "Link to this definition")
raises a TypeError, because FrozenDicts are immutable

setdefault(_*a_, _**kw_)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict.setdefault "Link to this definition")
raises a TypeError, because FrozenDicts are immutable

update(_*a_, _**kw_)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict.update "Link to this definition")
raises a TypeError, because FrozenDicts are immutable

updated(_*a_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#FrozenDict.updated)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict.updated "Link to this definition")
Make a copy and add items from a dictionary or iterable (and/or keyword arguments), overwriting values under an existing key. See [`dict.update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "(in Python v3.14)") for more details.

_class_ boltons.dictutils.ManyToMany(_items=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany "Link to this definition")
a dict-like entity that represents a many-to-many relationship between two groups of objects

behaves like a dict-of-tuples; also has .inv which is kept up to date which is a dict-of-tuples in the other direction

also, can be used as a directed graph among hashable python objects

add(_key_, _val_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany.add)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany.add "Link to this definition")get(_key_, _default=frozenset({})_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany.get)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany.get "Link to this definition")iteritems()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany.iteritems)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany.iteritems "Link to this definition")keys()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany.keys)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany.keys "Link to this definition")remove(_key_, _val_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany.remove)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany.remove "Link to this definition")replace(_key_, _newkey_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany.replace)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany.replace "Link to this definition")
replace instances of key by newkey

update(_iterable_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#ManyToMany.update)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany.update "Link to this definition")
given an iterable of (key, val), add them all

boltons.dictutils.MultiDict[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.MultiDict "Link to this definition")
alias of [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict")

boltons.dictutils.OMD[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OMD "Link to this definition")
alias of [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict")

_class_ boltons.dictutils.OneToOne(_*a_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne "Link to this definition")
Implements a one-to-one mapping dictionary. In addition to inheriting from and behaving exactly like the builtin [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), all values are automatically added as keys on a reverse mapping, available as the inv attribute. This arrangement keeps key and value namespaces distinct.

Basic operations are intuitive:

>>> oto = OneToOne({'a': 1, 'b': 2})
>>> print(oto['a'])
1
>>> print(oto.inv[1])
a
>>> len(oto)
2

Overwrites happens in both directions:

>>> oto.inv[1] = 'c'
>>> print(oto.get('a'))
None
>>> len(oto)
2

For a very similar project, with even more one-to-one functionality, check out [bidict](https://github.com/jab/bidict).

clear()→None.Remove all items from D.[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne.clear)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.clear "Link to this definition")copy()→a shallow copy of D[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne.copy)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.copy "Link to this definition")inv[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.inv "Link to this definition")pop(_k_[, _d_])→v,remove specified key and return the corresponding value.[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne.pop)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.pop "Link to this definition")
If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne.popitem)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.popitem "Link to this definition")
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault(_key_, _default=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne.setdefault)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.setdefault "Link to this definition")
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

_classmethod_ unique(_*a_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne.unique)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.unique "Link to this definition")
This alternate constructor for OneToOne will raise an exception when input values overlap. For instance:

>>> OneToOne.unique({'a': 1, 'b': 1})
Traceback (most recent call last):
...
ValueError: expected unique values, got multiple keys for the following values: ...

This even works across inputs:

>>> a_dict = {'a': 2}
>>> OneToOne.unique(a_dict, b=2)
Traceback (most recent call last):
...
ValueError: expected unique values, got multiple keys for the following values: ...

update([_E_, ]_**F_)→None.Update D from dict/iterable E and F.[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OneToOne.update)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne.update "Link to this definition")
If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

_class_ boltons.dictutils.OrderedMultiDict(_*a_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "Link to this definition")
A MultiDict is a dictionary that can have multiple values per key and the OrderedMultiDict (OMD) is a MultiDict that retains original insertion order. Common use cases include:

> *   handling query strings parsed from URLs
> 
> *   inverting a dictionary to create a reverse index (values to keys)
> 
> *   stacking data from multiple dictionaries in a non-destructive way

The OrderedMultiDict constructor is identical to the built-in [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), and overall the API constitutes an intuitive superset of the built-in type:

>>> omd = OrderedMultiDict()
>>> omd['a'] = 1
>>> omd['b'] = 2
>>> omd.add('a', 3)
>>> omd.get('a')
3
>>> omd.getlist('a')
[1, 3]

Some non-[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")-like behaviors also make an appearance, such as support for [`reversed()`](https://docs.python.org/3/library/functions.html#reversed "(in Python v3.14)"):

>>> list(reversed(omd))
['b', 'a']

Note that unlike some other MultiDicts, this OMD gives precedence to the most recent value added. `omd['a']` refers to `3`, not `1`.

>>> omd
OrderedMultiDict([('a', 1), ('b', 2), ('a', 3)])
>>> omd.poplast('a')
3
>>> omd
OrderedMultiDict([('a', 1), ('b', 2)])
>>> omd.pop('a')
1
>>> omd
OrderedMultiDict([('b', 2)])

If you want a safe-to-modify or flat dictionary, use [`OrderedMultiDict.todict()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.todict "boltons.dictutils.OrderedMultiDict.todict").

>>> from pprint import pprint as pp  # preserve printed ordering
>>> omd = OrderedMultiDict([('a', 1), ('b', 2), ('a', 3)])
>>> pp(omd.todict())
{'a': 3, 'b': 2}
>>> pp(omd.todict(multi=True))
{'a': [1, 3], 'b': [2]}

With `multi=False`, items appear with the keys in to original insertion order, alongside the most-recently inserted value for that key.

>>> OrderedMultiDict([('a', 1), ('b', 2), ('a', 3)]).items(multi=False)
[('a', 3), ('b', 2)]

Warning

`dict(omd)` changed behavior [in Python 3.7](https://bugs.python.org/issue34320) due to changes made to support the transition from [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "(in Python v3.14)") to the built-in dictionary being ordered. Before 3.7, the result would be a new dictionary, with values that were lists, similar to `omd.todict(multi=True)` (but only shallow-copy; the lists were direct references to OMD internal structures). From 3.7 onward, the values became singular, like `omd.todict(multi=False)`. For reliable cross-version behavior, just use [`todict()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.todict "boltons.dictutils.OrderedMultiDict.todict").

add(_k_, _v_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.add)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.add "Link to this definition")
Add a single value _v_ under a key _k_. Existing values under _k_ are preserved.

addlist(_k_, _v_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.addlist)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.addlist "Link to this definition")
Add an iterable of values underneath a specific key, preserving any values already under that key.

>>> omd = OrderedMultiDict([('a', -1)])
>>> omd.addlist('a', range(3))
>>> omd
OrderedMultiDict([('a', -1), ('a', 0), ('a', 1), ('a', 2)])

Called `addlist` for consistency with [`getlist()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.getlist "boltons.dictutils.OrderedMultiDict.getlist"), but tuples and other sequences and iterables work.

clear()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.clear)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.clear "Link to this definition")
Empty the dictionary.

copy()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.copy)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.copy "Link to this definition")
Return a shallow copy of the dictionary.

counts()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.counts)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.counts "Link to this definition")
Returns a mapping from key to number of values inserted under that key. Like [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "(in Python v3.14)"), but returns a new [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict").

_classmethod_ fromkeys(_keys_, _default=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.fromkeys)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.fromkeys "Link to this definition")
Create a dictionary from a list of keys, with all the values set to _default_, or `None` if _default_ is not set.

get(_k_, _default=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.get)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.get "Link to this definition")
Return the value for key _k_ if present in the dictionary, else _default_. If _default_ is not given, `None` is returned. This method never raises a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)").

To get all values under a key, use [`OrderedMultiDict.getlist()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.getlist "boltons.dictutils.OrderedMultiDict.getlist").

getlist(_k_, _default=\_MISSING_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.getlist)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.getlist "Link to this definition")
Get all values for key _k_ as a list, if _k_ is in the dictionary, else _default_. The list returned is a copy and can be safely mutated. If _default_ is not given, an empty [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") is returned.

inverted()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.inverted)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.inverted "Link to this definition")
Returns a new [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict") with values and keys swapped, like creating dictionary transposition or reverse index. Insertion order is retained and all keys and values are represented in the output.

>>> omd = OMD([(0, 2), (1, 2)])
>>> omd.inverted().getlist(2)
[0, 1]

Inverting twice yields a copy of the original:

>>> omd.inverted().inverted()
OrderedMultiDict([(0, 2), (1, 2)])

items(_multi=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.items)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.items "Link to this definition")
Returns a list containing the output of [`iteritems()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.iteritems "boltons.dictutils.OrderedMultiDict.iteritems"). See that method’s docs for more details.

iteritems(_multi=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.iteritems)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.iteritems "Link to this definition")
Iterate over the OMD’s items in insertion order. By default, yields only the most-recently inserted value for each key. Set _multi_ to `True` to get all inserted items.

iterkeys(_multi=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.iterkeys)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.iterkeys "Link to this definition")
Iterate over the OMD’s keys in insertion order. By default, yields each key once, according to the most recent insertion. Set _multi_ to `True` to get all keys, including duplicates, in insertion order.

itervalues(_multi=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.itervalues)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.itervalues "Link to this definition")
Iterate over the OMD’s values in insertion order. By default, yields the most-recently inserted value per unique key. Set _multi_ to `True` to get all values according to insertion order.

keys(_multi=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.keys)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.keys "Link to this definition")
Returns a list containing the output of [`iterkeys()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.iterkeys "boltons.dictutils.OrderedMultiDict.iterkeys"). See that method’s docs for more details.

pop(_k_, _default=\_MISSING_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.pop)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.pop "Link to this definition")
Remove all values under key _k_, returning the most-recently inserted value. Raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") if the key is not present and no _default_ is provided.

popall(_k_, _default=\_MISSING_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.popall)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.popall "Link to this definition")
Remove all values under key _k_, returning them in the form of a list. Raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") if the key is not present and no _default_ is provided.

poplast(_k=\_MISSING_, _default=\_MISSING_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.poplast)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.poplast "Link to this definition")
Remove and return the most-recently inserted value under the key _k_, or the most-recently inserted key if _k_ is not provided. If no values remain under _k_, it will be removed from the OMD. Raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") if _k_ is not present in the dictionary, or the dictionary is empty.

setdefault(_k_, _default=\_MISSING_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.setdefault)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.setdefault "Link to this definition")
If key _k_ is in the dictionary, return its value. If not, insert _k_ with a value of _default_ and return _default_. _default_ defaults to `None`. See [`dict.setdefault()`](https://docs.python.org/3/library/stdtypes.html#dict.setdefault "(in Python v3.14)") for more information.

sorted(_key=None_, _reverse=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.sorted)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.sorted "Link to this definition")
Similar to the built-in [`sorted()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.sorted "boltons.dictutils.OrderedMultiDict.sorted"), except this method returns a new [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict") sorted by the provided key function, optionally reversed.

Parameters:
*   **key** (_callable_) – A callable to determine the sort key of each element. The callable should expect an **item** (key-value pair tuple).

*   **reverse** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Set to `True` to reverse the ordering.

>>> omd = OrderedMultiDict(zip(range(3), range(3)))
>>> omd.sorted(reverse=True)
OrderedMultiDict([(2, 2), (1, 1), (0, 0)])

Note that the key function receives an **item** (key-value tuple), so the recommended signature looks like:

>>> omd = OrderedMultiDict(zip('hello', 'world'))
>>> omd.sorted(key=lambda i: i[1])  # i[0] is the key, i[1] is the val
OrderedMultiDict([('o', 'd'), ('l', 'l'), ('e', 'o'), ('l', 'r'), ('h', 'w')])

sortedvalues(_key=None_, _reverse=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.sortedvalues)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.sortedvalues "Link to this definition")
Returns a copy of the [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict") with the same keys in the same order as the original OMD, but the values within each keyspace have been sorted according to _key_ and _reverse_.

Parameters:
*   **key** (_callable_) – A single-argument callable to determine the sort key of each element. The callable should expect an **item** (key-value pair tuple).

*   **reverse** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Set to `True` to reverse the ordering.

>>> omd = OrderedMultiDict()
>>> omd.addlist('even', [6, 2])
>>> omd.addlist('odd', [1, 5])
>>> omd.add('even', 4)
>>> omd.add('odd', 3)
>>> somd = omd.sortedvalues()
>>> somd.getlist('even')
[2, 4, 6]
>>> somd.keys(multi=True) == omd.keys(multi=True)
True
>>> omd == somd
False
>>> somd
OrderedMultiDict([('even', 2), ('even', 4), ('odd', 1), ('odd', 3), ('even', 6), ('odd', 5)])

As demonstrated above, contents and key order are retained. Only value order changes.

todict(_multi=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.todict)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.todict "Link to this definition")
Gets a basic [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") of the items in this dictionary. Keys are the same as the OMD, values are the most recently inserted values for each key.

Setting the _multi_ arg to `True` is yields the same result as calling [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") on the OMD, except that all the value lists are copies that can be safely mutated.

update(_E_, _**F_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.update)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.update "Link to this definition")
Add items from a dictionary or iterable (and/or keyword arguments), overwriting values under an existing key. See [`dict.update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "(in Python v3.14)") for more details.

update_extend(_E_, _**F_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.update_extend)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.update_extend "Link to this definition")
Add items from a dictionary, iterable, and/or keyword arguments without overwriting existing items present in the dictionary. Like [`update()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.update "boltons.dictutils.OrderedMultiDict.update"), but adds to existing keys instead of overwriting them.

values(_multi=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.values)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.values "Link to this definition")
Returns a list containing the output of [`itervalues()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.itervalues "boltons.dictutils.OrderedMultiDict.itervalues"). See that method’s docs for more details.

viewitems()→a set-like object providing a view on OMD's items[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.viewitems)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.viewitems "Link to this definition")viewkeys()→a set-like object providing a view on OMD's keys[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.viewkeys)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.viewkeys "Link to this definition")viewvalues()→an object providing a view on OMD's values[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#OrderedMultiDict.viewvalues)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict.viewvalues "Link to this definition")boltons.dictutils.subdict(_d_, _keep=None_, _drop=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/dictutils.html#subdict)[](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.subdict "Link to this definition")
Compute the “subdictionary” of a dict, _d_.

A subdict is to a dict what a subset is a to set. If _A_ is a subdict of _B_, that means that all keys of _A_ are present in _B_.

Returns a new dict with any keys in _drop_ removed, and any keys in _keep_ still present, provided they were in the original dict. _keep_ defaults to all keys, _drop_ defaults to empty, so without one of these arguments, calling this function is equivalent to calling `dict()`.

>>> from pprint import pprint as pp
>>> pp(subdict({'a': 1, 'b': 2}))
{'a': 1, 'b': 2}
>>> subdict({'a': 1, 'b': 2, 'c': 3}, drop=['b', 'c'])
{'a': 1}
>>> pp(subdict({'a': 1, 'b': 2, 'c': 3}, keep=['a', 'c']))
{'a': 1, 'c': 3}
