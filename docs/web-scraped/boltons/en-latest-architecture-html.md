# Source: https://boltons.readthedocs.io/en/latest/architecture.html

Title: Architecture — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/architecture.html

Markdown Content:
`boltons` has a minimalist architecture: remain as consistent, and self-contained as possible, with an eye toward maintaining its range of use cases and usage patterns as wide as possible.

Integration[](https://boltons.readthedocs.io/en/latest/architecture.html#integration "Link to this heading")
-------------------------------------------------------------------------------------------------------------

Utility libraries are often used extensively within a project, and because they are not often fundamental to the architecture of the application, simplicity and stability may take precedence over version recency. In these cases, developers can:

> 1.   Copy the whole `boltons` package into a project.
> 
> 2.   Copy just the `utils.py` file that a project requires.

Boltons take this into account by design. The `boltons` package depends on no packages, making it easy for inclusion into a project. Furthermore, virtually all individual modules have been written to be as self-contained as possible, allowing cherrypicking of functionality into projects.

Design of a `bolton`[](https://boltons.readthedocs.io/en/latest/architecture.html#design-of-a-bolton "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

`boltons` aims to be a living library, an ever-expanding collection of tested and true utilities. For a bolton to be a bolton, it should:

> 1.   Be pure-Python and as self-contained as possible.
> 
> 2.   Perform a common task or fulfill a common role.
> 
> 3.   Demonstrate and mitigate some insufficiency in the standard library.
> 
> 4.   Strive for the standard set forth by the standard library by striking a balance between best practice and “good enough”, correctness and common sense. When in doubt, ask, “what would the standard library do?”
> 
> 5.   Have approachable documentation with at least one helpful [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "(in Python v3.14)"), links to relevant standard library functionality, as well as any 3rd-party packages that provide further capabilities.

Finally, boltons should be substantial implementations of commonly trivialized stumbling blocks and not the other way around. The larger the problem solved, the less likely the functionality is suitable for inclusion in boltons; boltons are fundamental and self-contained, not sweeping and architecture-defining.

Themes of `boltons`[](https://boltons.readthedocs.io/en/latest/architecture.html#themes-of-boltons "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

`boltons` has had a wide variety of inspirations over the years, but a definite set of themes have emerged:

1.   From the Python docs:

    1.   [`queueutils`](https://boltons.readthedocs.io/en/latest/queueutils.html#module-boltons.queueutils "boltons.queueutils") - [heapq docs](https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes)

    2.   [`iterutils`](https://boltons.readthedocs.io/en/latest/iterutils.html#module-boltons.iterutils "boltons.iterutils") - [itertools docs](https://docs.python.org/2/library/itertools.html#recipes)

    3.   [`timeutils`](https://boltons.readthedocs.io/en/latest/timeutils.html#module-boltons.timeutils "boltons.timeutils") - [datetime docs](https://docs.python.org/2/library/datetime.html#tzinfo-objects)

2.   Reimplementations and tweaks of the standard library:

    1.   [`boltons.fileutils.copytree()`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.copytree "boltons.fileutils.copytree") - [`shutil.copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "(in Python v3.14)")

    2.   [`boltons.namedutils.namedtuple`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedtuple "boltons.namedutils.namedtuple") - [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.14)")

3.   One-off implementations discovered in multiple other libraries’ `utils.py` or equivalent

    1.   [`boltons.strutils.slugify()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.slugify "boltons.strutils.slugify")

    2.   [`boltons.strutils.bytes2human()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.bytes2human "boltons.strutils.bytes2human")

    3.   [`boltons.timeutils.relative_time()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.relative_time "boltons.timeutils.relative_time")

4.   More powerful multi-purpose data structures

    1.   [`boltons.dictutils.OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict")

    2.   [`boltons.setutils.IndexedSet`](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet "boltons.setutils.IndexedSet")

    3.   [`boltons.listutils.BList`](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BList "boltons.listutils.BList")

    4.   [`boltons.namedutils.namedlist`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedlist "boltons.namedutils.namedlist")

    5.   [`boltons.tableutils.Table`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table "boltons.tableutils.Table")

5.   Personal practice and experience

    1.   [`boltons.debugutils`](https://boltons.readthedocs.io/en/latest/debugutils.html#module-boltons.debugutils "boltons.debugutils")

    2.   [`boltons.gcutils`](https://boltons.readthedocs.io/en/latest/gcutils.html#module-boltons.gcutils "boltons.gcutils")

    3.   [`boltons.tbutils`](https://boltons.readthedocs.io/en/latest/tbutils.html#module-boltons.tbutils "boltons.tbutils")
