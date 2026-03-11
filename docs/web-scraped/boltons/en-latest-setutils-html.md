# Source: https://boltons.readthedocs.io/en/latest/setutils.html

Title: IndexedSet type — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/setutils.html

Published Time: Wed, 28 Jan 2026 06:30:29 GMT

Markdown Content:
`setutils` - `IndexedSet` type[](https://boltons.readthedocs.io/en/latest/setutils.html#module-boltons.setutils "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)") type brings the practical expressiveness of set theory to Python. It has a very rich API overall, but lacks a couple of fundamental features. For one, sets are not ordered. On top of this, sets are not indexable, i.e, `my_set[8]` will raise an [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)"). The [`IndexedSet`](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet "boltons.setutils.IndexedSet") type remedies both of these issues without compromising on the excellent complexity characteristics of Python’s built-in set implementation.

_class_ boltons.setutils.IndexedSet(_other=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet "Link to this definition")
`IndexedSet` is a `collections.MutableSet` that maintains insertion order and uniqueness of inserted elements. It’s a hybrid type, mostly like an OrderedSet, but also [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")-like, in that it supports indexing and slicing.

Parameters:
**other** (_iterable_) – An optional iterable used to initialize the set.

>>> x = IndexedSet(list(range(4)) + list(range(8)))
>>> x
IndexedSet([0, 1, 2, 3, 4, 5, 6, 7])
>>> x - set(range(2))
IndexedSet([2, 3, 4, 5, 6, 7])
>>> x[-1]
7
>>> fcr = IndexedSet('freecreditreport.com')
>>> ''.join(fcr[:fcr.index('.')])
'frecditpo'

Standard set operators and interoperation with [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)") are all supported:

>>> fcr & set('cash4gold.com')
IndexedSet(['c', 'd', 'o', '.', 'm'])

As you can see, the `IndexedSet` is almost like a `UniqueList`, retaining only one copy of a given value, in the order it was first added. For the curious, the reason why IndexedSet does not support setting items based on index (i.e, `__setitem__()`), consider the following dilemma:

my_indexed_set = [A, B, C, D]
my_indexed_set[2] = A

At this point, a set requires only one _A_, but a [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") would overwrite _C_. Overwriting _C_ would change the length of the list, meaning that `my_indexed_set[2]` would not be _A_, as expected with a list, but rather _D_. So, no `__setitem__()`.

Otherwise, the API strives to be as complete a union of the [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") and [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)") APIs as possible.

add(_item_)→add item to the set[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.add)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.add "Link to this definition")clear()→empty the set[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.clear)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.clear "Link to this definition")count(_val)->count number of instances of value(0 or 1_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.count)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.count "Link to this definition")difference(_*others_)→get a new set with elements not in others[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.difference)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.difference "Link to this definition")difference_update(_*others)->discard self.intersection(*others_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.difference_update)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.difference_update "Link to this definition")discard(_item)->discard item from the set(does not raise_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.discard)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.discard "Link to this definition")_classmethod_ from_iterable(_it_)→create a set from an iterable[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.from_iterable)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.from_iterable "Link to this definition")index(_val_)→get the index of a value,raises if not present[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.index)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.index "Link to this definition")intersection(_*others_)→get a set with overlap of this and others[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.intersection)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.intersection "Link to this definition")intersection_update(_*others)->discard self.difference(*others_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.intersection_update)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.intersection_update "Link to this definition")isdisjoint(_other_)→return True if no overlap with other[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.isdisjoint)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.isdisjoint "Link to this definition")issubset(_other_)→return True if other contains this set[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.issubset)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.issubset "Link to this definition")issuperset(_other_)→return True if set contains other[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.issuperset)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.issuperset "Link to this definition")iter_difference(_*others_)→iterate over elements not in others[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.iter_difference)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.iter_difference "Link to this definition")iter_intersection(_*others_)→iterate over elements also in others[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.iter_intersection)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.iter_intersection "Link to this definition")iter_slice(_start_, _stop_, _step=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.iter_slice)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.iter_slice "Link to this definition")
iterate over a slice of the set

pop(_index)->remove the item at a given index(-1 by default_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.pop)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.pop "Link to this definition")remove(_item_)→remove item from the set,raises if not present[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.remove)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.remove "Link to this definition")reverse()→reverse the contents of the set in-place[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.reverse)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.reverse "Link to this definition")sort()→sort the contents of the set in-place[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.sort)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.sort "Link to this definition")symmetric_difference(_*others_)→XOR set of this and others[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.symmetric_difference)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.symmetric_difference "Link to this definition")symmetric_difference_update(_other_)→in-place XOR with other[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.symmetric_difference_update)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.symmetric_difference_update "Link to this definition")union(_*others_)→return a new set containing this set and others[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.union)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.union "Link to this definition")update(_*others_)→add values from one or more iterables[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#IndexedSet.update)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet.update "Link to this definition")boltons.setutils.complement(_wrapped_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/setutils.html#complement)[](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.complement "Link to this definition")
Given a [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)"), convert it to a **complement set**.

Whereas a [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)") keeps track of what it contains, a [complement set](https://en.wikipedia.org/wiki/Complement_(set_theory)) keeps track of what it does _not_ contain. For example, look what happens when we intersect a normal set with a complement set:

>>> list(set(range(5)) & complement(set([2, 3])))

[0, 1, 4]

We get the everything in the left that wasn’t in the right, because intersecting with a complement is the same as subtracting a normal set.

Parameters:
**wrapped** ([_set_](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")) – A set or any other iterable which should be turned into a complement set.

All set methods and operators are supported by complement sets, between other [`complement()`](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.complement "boltons.setutils.complement")-wrapped sets and/or regular [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)") objects.

Because a complement set only tracks what elements are _not_ in the set, functionality based on set contents is unavailable: [`len()`](https://docs.python.org/3/library/functions.html#len "(in Python v3.14)"), [`iter()`](https://docs.python.org/3/library/functions.html#iter "(in Python v3.14)") (and for loops), and `.pop()`. But a complement set can always be turned back into a regular set by complementing it again:

>>> s = set(range(5))
>>> complement(complement(s)) == s
True

Note

An empty complement set corresponds to the concept of a [universal set](https://en.wikipedia.org/wiki/Universal_set) from mathematics.

Complement sets by example[](https://boltons.readthedocs.io/en/latest/setutils.html#complement-sets-by-example "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

Many uses of sets can be expressed more simply by using a complement. Rather than trying to work out in your head the proper way to invert an expression, you can just throw a complement on the set. Consider this example of a name filter:

>>> class NamesFilter(object):
...    def  __init__ (self, allowed):
...        self._allowed = allowed
...
...    def filter(self, names):
...        return [name for name in names if name in self._allowed]
>>> NamesFilter(set(['alice', 'bob'])).filter(['alice', 'bob', 'carol'])
['alice', 'bob']

What if we want to just express “let all the names through”?

We could try to enumerate all of the expected names:

``NamesFilter({'alice', 'bob', 'carol'})``

But this is very brittle – what if at some point over this object is changed to filter `['alice', 'bob', 'carol', 'dan']`?

Even worse, what about the poor programmer who next works on this piece of code? They cannot tell whether the purpose of the large allowed set was “allow everything”, or if ‘dan’ was excluded for some subtle reason.

A complement set lets the programmer intention be expressed succinctly and directly:

NamesFilter(complement(set()))

Not only is this code short and robust, it is easy to understand the intention.
