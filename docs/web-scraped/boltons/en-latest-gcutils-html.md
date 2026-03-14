# Source: https://boltons.readthedocs.io/en/latest/gcutils.html

Title: Garbage collecting tools — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/gcutils.html

Markdown Content:
The Python Garbage Collector ([GC](https://docs.python.org/2/glossary.html#term-garbage-collection)) doesn’t usually get too much attention, probably because:

> *   Python’s [reference counting](https://docs.python.org/2/glossary.html#term-reference-count) effectively handles the vast majority of unused objects
> 
> *   People are slowly learning to avoid implementing [object.__del__()](https://docs.python.org/2/glossary.html#term-reference-count)
> 
> *   The collection itself strikes a good balance between simplicity and power ([tunable generation sizes](https://docs.python.org/2/library/gc.html#gc.set_threshold))
> 
> *   The collector itself is fast and rarely the cause of long pauses associated with GC in other runtimes

Even so, for many applications, the time will come when the developer will need to track down:

> *   Circular references
> 
> *   Misbehaving objects (locks, `__del__()`)
> 
> *   Memory leaks
> 
> *   Or just ways to shave off a couple percent of execution time

Thanks to the [`gc`](https://docs.python.org/3/library/gc.html#module-gc "(in Python v3.14)") module, the GC is a well-instrumented entry point for exactly these tasks, and `gcutils` aims to facilitate it further.

_class_ boltons.gcutils.GCToggler(_postcollect=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/gcutils.html#GCToggler)[](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.GCToggler "Link to this definition")
The `GCToggler` is a context-manager that allows one to safely take more control of your garbage collection schedule. Anecdotal experience says certain object-creation-heavy tasks see speedups of around 10% by simply doing one explicit collection at the very end, especially if most of the objects will stay resident.

Two GCTogglers are already present in the `gcutils` module:

*   [`toggle_gc`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.toggle_gc "boltons.gcutils.toggle_gc") simply turns off GC at context entrance, and re-enables at exit

*   [`toggle_gc_postcollect`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.toggle_gc_postcollect "boltons.gcutils.toggle_gc_postcollect") does the same, but triggers an explicit collection after re-enabling.

>>> with toggle_gc:
...     x = [object() for i in range(1000)]

Between those two instances, the `GCToggler` type probably won’t be used much directly, but is documented for inheritance purposes.

boltons.gcutils.get_all(_type\_obj_, _include\_subtypes=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/gcutils.html#get_all)[](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.get_all "Link to this definition")
Get a list containing all instances of a given type. This will work for the vast majority of types out there.

>>> class Ratking(object): pass
>>> wiki, hak, sport = Ratking(), Ratking(), Ratking()
>>> len(get_all(Ratking))
3

However, there are some exceptions. For example, `get_all(bool)` returns an empty list because `True` and `False` are themselves built-in and not tracked.

>>> get_all(bool)
[]

Still, it’s not hard to see how this functionality can be used to find all instances of a leaking type and track them down further using [`gc.get_referrers()`](https://docs.python.org/3/library/gc.html#gc.get_referrers "(in Python v3.14)") and [`gc.get_referents()`](https://docs.python.org/3/library/gc.html#gc.get_referents "(in Python v3.14)").

`get_all()` is optimized such that getting instances of user-created types is quite fast. Setting _include\_subtypes_ to `False` will further increase performance in cases where instances of subtypes aren’t required.

Note

There are no guarantees about the state of objects returned by `get_all()`, especially in concurrent environments. For instance, it is possible for an object to be in the middle of executing its `__init__()` and be only partially constructed.

boltons.gcutils.toggle_gc _=<boltons.gcutils.GCToggler object>_[](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.toggle_gc "Link to this definition")
A context manager for disabling GC for a code block. See [`GCToggler`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.GCToggler "boltons.gcutils.GCToggler") for more details.

boltons.gcutils.toggle_gc_postcollect _=<boltons.gcutils.GCToggler object>_[](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.toggle_gc_postcollect "Link to this definition")
A context manager for disabling GC for a code block, and collecting before re-enabling. See [`GCToggler`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.GCToggler "boltons.gcutils.GCToggler") for more details.
