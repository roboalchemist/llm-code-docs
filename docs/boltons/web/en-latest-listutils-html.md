# Source: https://boltons.readthedocs.io/en/latest/listutils.html

Title: list derivatives — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/listutils.html

Markdown Content:
`listutils` - `list` derivatives[](https://boltons.readthedocs.io/en/latest/listutils.html#module-boltons.listutils "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Python’s builtin [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") is a very fast and efficient sequence type, but it could be better for certain access patterns, such as non-sequential insertion into a large lists. `listutils` provides a pure-Python solution to this problem.

For utilities for working with iterables and lists, check out `iterutils`. For the a [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")-based version of `collections.namedtuple`, check out `namedutils`.

boltons.listutils.BList[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BList "Link to this definition")
alias of [`BarrelList`](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList "boltons.listutils.BarrelList")

_class_ boltons.listutils.BarrelList(_iterable=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList "Link to this definition")
The `BarrelList` is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") subtype backed by many dynamically-scaled sublists, to provide better scaling and random insertion/deletion characteristics. It is a subtype of the builtin [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") and has an identical API, supporting indexing, slicing, sorting, etc. If application requirements call for something more performant, consider the [blist module available on PyPI](https://pypi.python.org/pypi/blist).

The name comes by way of Kurt Rose, who said it reminded him of barrel shifters. Not sure how, but it’s BList-like, so the name stuck. BList is of course a reference to [B-trees](https://en.wikipedia.org/wiki/B-tree).

Parameters:
**iterable** – An optional iterable of initial values for the list.

>>> blist = BList(range(100000))
>>> blist.pop(50000)
50000
>>> len(blist)
99999
>>> len(blist.lists)  # how many underlying lists
8
>>> slice_idx = blist.lists[0][-1]
>>> blist[slice_idx:slice_idx + 2]
BarrelList([11637, 11638])

Slicing is supported and works just fine across list borders, returning another instance of the BarrelList.

append(_item_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.append)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.append "Link to this definition")
Append object to the end of the list.

count(_item_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.count)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.count "Link to this definition")
Return number of occurrences of value.

del_slice(_start_, _stop_, _step=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.del_slice)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.del_slice "Link to this definition")extend(_iterable_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.extend)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.extend "Link to this definition")
Extend list by appending elements from the iterable.

_classmethod_ from_iterable(_it_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.from_iterable)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.from_iterable "Link to this definition")index(_item_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.index)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.index "Link to this definition")
Return first index of value.

Raises ValueError if the value is not present.

insert(_index_, _item_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.insert)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.insert "Link to this definition")
Insert object before index.

iter_slice(_start_, _stop_, _step=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.iter_slice)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.iter_slice "Link to this definition")pop(_*a_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.pop)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.pop "Link to this definition")
Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.

reverse()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.reverse)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.reverse "Link to this definition")
Reverse _IN PLACE_.

sort()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/listutils.html#BarrelList.sort)[](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList.sort "Link to this definition")
Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.
