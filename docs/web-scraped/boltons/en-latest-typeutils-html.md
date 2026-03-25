# Source: https://boltons.readthedocs.io/en/latest/typeutils.html

Title: Type handling — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/typeutils.html

Markdown Content:
[boltons](https://boltons.readthedocs.io/en/latest/index.html)
`typeutils` - Type handling[](https://boltons.readthedocs.io/en/latest/typeutils.html#module-boltons.typeutils "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

Python’s built-in [`functools`](https://docs.python.org/3/library/functools.html#module-functools "(in Python v3.14)") module builds several useful utilities on top of Python’s first-class function support. `typeutils` attempts to do the same for metaprogramming with types and instances.

_class_ boltons.typeutils.classproperty(_fn_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/typeutils.html#classproperty)[](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.classproperty "Link to this definition")
Much like a [`property`](https://docs.python.org/3/library/functions.html#property "(in Python v3.14)"), but the wrapped get function is a class method. For simplicity, only read-only properties are implemented.

boltons.typeutils.get_all_subclasses(_cls_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/typeutils.html#get_all_subclasses)[](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.get_all_subclasses "Link to this definition")
Recursively finds and returns a [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") of all types inherited from _cls_.

>>> class A(object):
...     pass
...
>>> class B(A):
...     pass
...
>>> class C(B):
...     pass
...
>>> class D(A):
...     pass
...
>>> [t. __name__  for t in get_all_subclasses(A)]
['B', 'D', 'C']
>>> [t. __name__  for t in get_all_subclasses(B)]
['C']

boltons.typeutils.issubclass(_subclass_, _baseclass_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/typeutils.html#issubclass)[](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.issubclass "Link to this definition")
Just like the built-in [`issubclass()`](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.issubclass "boltons.typeutils.issubclass"), this function checks whether _subclass_ is inherited from _baseclass_. Unlike the built-in function, this `issubclass` will simply return `False` if either argument is not suitable (e.g., if _subclass_ is not an instance of [`type`](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")), instead of raising [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)").

Parameters:
*   **subclass** ([_type_](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")) – The target class to check.

*   **baseclass** ([_type_](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")) – The base class _subclass_ will be checked against.

>>> class MyObject(object): pass
...
>>> issubclass(MyObject, object)  # always a fun fact
True
>>> issubclass('hi', 'friend')
False

boltons.typeutils.make_sentinel(_name='\_MISSING'_, _var\_name=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/typeutils.html#make_sentinel)[](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.make_sentinel "Link to this definition")
Creates and returns a new **instance** of a new class, suitable for usage as a “sentinel”, a kind of singleton often used to indicate a value is missing when `None` is a valid input.

Parameters:
*   **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Name of the Sentinel

*   **var_name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Set this name to the name of the variable in its respective module enable pickleability. Note: pickleable sentinels should be global constants at the top level of their module.

>>> make_sentinel(var_name='_MISSING')
_MISSING

The most common use cases here in boltons are as default values for optional function arguments, partly because of its less-confusing appearance in automatically generated documentation. Sentinels also function well as placeholders in queues and linked lists.

Note

By design, additional calls to `make_sentinel` with the same values will not produce equivalent objects.

>>> make_sentinel('TEST') == make_sentinel('TEST')
False
>>> type(make_sentinel('TEST')) == type(make_sentinel('TEST'))
False
