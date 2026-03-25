# Source: https://boltons.readthedocs.io/en/latest/tableutils.html

Title: 2D data structure — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/tableutils.html

Markdown Content:
tableutils - 2D data structure — boltons 25.0.0 documentation

[boltons](https://boltons.readthedocs.io/en/latest/index.html)

latest
stable

*   [Architecture](https://boltons.readthedocs.io/en/latest/architecture.html)
*   [`cacheutils` - Caches and caching](https://boltons.readthedocs.io/en/latest/cacheutils.html)
*   [`debugutils` - Debugging utilities](https://boltons.readthedocs.io/en/latest/debugutils.html)
*   [`dictutils` - Mapping types (OMD)](https://boltons.readthedocs.io/en/latest/dictutils.html)
*   [`ecoutils` - Ecosystem analytics](https://boltons.readthedocs.io/en/latest/ecoutils.html)
*   [`fileutils` - Filesystem helpers](https://boltons.readthedocs.io/en/latest/fileutils.html)
*   [`formatutils` - `str.format()` toolbox](https://boltons.readthedocs.io/en/latest/formatutils.html)
*   [`funcutils` - `functools` fixes](https://boltons.readthedocs.io/en/latest/funcutils.html)
*   [`gcutils` - Garbage collecting tools](https://boltons.readthedocs.io/en/latest/gcutils.html)
*   [`ioutils` - Input/output enhancements](https://boltons.readthedocs.io/en/latest/ioutils.html)
*   [`iterutils` - `itertools` improvements](https://boltons.readthedocs.io/en/latest/iterutils.html)
*   [`jsonutils` - JSON interactions](https://boltons.readthedocs.io/en/latest/jsonutils.html)
*   [`listutils` - `list` derivatives](https://boltons.readthedocs.io/en/latest/listutils.html)
*   [`mathutils` - Mathematical functions](https://boltons.readthedocs.io/en/latest/mathutils.html)
*   [`mboxutils` - Unix mailbox utilities](https://boltons.readthedocs.io/en/latest/mboxutils.html)
*   [`namedutils` - Lightweight containers](https://boltons.readthedocs.io/en/latest/namedutils.html)
*   [`pathutils` - Filesystem fun](https://boltons.readthedocs.io/en/latest/pathutils.html)
*   [`queueutils` - Priority queues](https://boltons.readthedocs.io/en/latest/queueutils.html)
*   [`setutils` - `IndexedSet` type](https://boltons.readthedocs.io/en/latest/setutils.html)
*   [`socketutils` - `socket` wrappers](https://boltons.readthedocs.io/en/latest/socketutils.html)
*   [`statsutils` - Statistics fundamentals](https://boltons.readthedocs.io/en/latest/statsutils.html)
*   [`strutils` - Text manipulation](https://boltons.readthedocs.io/en/latest/strutils.html)
*   [`tableutils` - 2D data structure](https://boltons.readthedocs.io/en/latest/tableutils.html#)
    *   [`Table`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table)
        *   [`Table.extend()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.extend)
        *   [`Table.from_data()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_data)
        *   [`Table.from_dict()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_dict)
        *   [`Table.from_list()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_list)
        *   [`Table.from_object()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_object)
        *   [`Table.get_cell_html()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.get_cell_html)
        *   [`Table.to_html()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.to_html)
        *   [`Table.to_text()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.to_text)

*   [`tbutils` - Tracebacks and call stacks](https://boltons.readthedocs.io/en/latest/tbutils.html)
*   [`timeutils` - `datetime` additions](https://boltons.readthedocs.io/en/latest/timeutils.html)
*   [`typeutils` - Type handling](https://boltons.readthedocs.io/en/latest/typeutils.html)
*   [`urlutils` - Structured URL](https://boltons.readthedocs.io/en/latest/urlutils.html)

[boltons](https://boltons.readthedocs.io/en/latest/index.html)

*   [](https://boltons.readthedocs.io/en/latest/index.html)
*   `tableutils` - 2D data structure
*   [View page source](https://boltons.readthedocs.io/en/latest/_sources/tableutils.rst.txt)

* * *

`tableutils` - 2D data structure[](https://boltons.readthedocs.io/en/latest/tableutils.html#module-boltons.tableutils "Link to this heading")
==============================================================================================================================================

If there is one recurring theme in `boltons`, it is that Python has excellent datastructures that constitute a good foundation for most quick manipulations, as well as building applications. However, Python usage has grown much faster than builtin data structure power. Python has a growing need for more advanced general-purpose data structures which behave intuitively.

The [`Table`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table "boltons.tableutils.Table") class is one example. When handed one- or two-dimensional data, it can provide useful, if basic, text and HTML renditions of small to medium sized data. It also heuristically handles recursive data of various formats (lists, dicts, namedtuples, objects).

For more advanced [`Table`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table "boltons.tableutils.Table")-style manipulation check out the [pandas](http://pandas.pydata.org/) DataFrame.

_class_ boltons.tableutils.Table(_data=None_, _headers=\_MISSING_, _metadata=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table "Link to this definition")
This Table class is meant to be simple, low-overhead, and extensible. Its most common use would be for translation between in-memory data structures and serialization formats, such as HTML and console-ready text.

As such, it stores data in list-of-lists format, and _does not_ copy lists passed in. It also reserves the right to modify those lists in a “filling” process, whereby short lists are extended to the width of the table (usually determined by number of headers). This greatly reduces overhead and processing/validation that would have to occur otherwise.

General description of headers behavior:

Headers describe the columns, but are not part of the data, however, if the _headers_ argument is omitted, Table tries to infer header names from the data. It is possible to have a table with no headers, just pass in `headers=None`.

Supported inputs:

*   [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") of [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") objects

*   [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") (list/single)

*   [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)") (list/single)

*   `collections.namedtuple` (list/single)

*   TODO: DB API cursor?

*   TODO: json

Supported outputs:

*   HTML

*   Pretty text (also usable as GF Markdown)

*   TODO: CSV

*   TODO: json

*   TODO: json lines

To minimize resident size, the Table data is stored as a list of lists.

extend(_data_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.extend)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.extend "Link to this definition")
Append the given data to the end of the Table.

_classmethod_ from_data(_data_, _headers=\_MISSING_, _max\_depth=1_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.from_data)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_data "Link to this definition")
Create a Table from any supported data, heuristically selecting how to represent the data in Table format.

Parameters:
*   **data** ([_object_](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) – Any object or iterable with data to be imported to the Table.

*   **headers** (_iterable_) – An iterable of headers to be matched to the data. If not explicitly passed, headers will be guessed for certain datatypes.

*   **max_depth** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The level to which nested Tables should be created (default: 1).

*   **_data_type** (_InputType subclass_) – For advanced use cases, do not guess the type of the input data, use this data type instead.

_classmethod_ from_dict(_data_, _headers=\_MISSING_, _max\_depth=1_, _metadata=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.from_dict)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_dict "Link to this definition")
Create a Table from a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"). Operates the same as [`from_data()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_data "boltons.tableutils.Table.from_data"), but forces interpretation of the data as a Mapping.

_classmethod_ from_list(_data_, _headers=\_MISSING_, _max\_depth=1_, _metadata=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.from_list)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_list "Link to this definition")
Create a Table from a [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"). Operates the same as [`from_data()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_data "boltons.tableutils.Table.from_data"), but forces the interpretation of the data as a Sequence.

_classmethod_ from_object(_data_, _headers=\_MISSING_, _max\_depth=1_, _metadata=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.from_object)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_object "Link to this definition")
Create a Table from an [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)"). Operates the same as [`from_data()`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.from_data "boltons.tableutils.Table.from_data"), but forces the interpretation of the data as an object. May be useful for some [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") and [`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") subtypes.

get_cell_html(_value_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.get_cell_html)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.get_cell_html "Link to this definition")
Called on each value in an HTML table. By default it simply escapes the HTML. Override this method to add additional conditions and behaviors, but take care to ensure the final output is HTML escaped.

to_html(_orientation=None_, _wrapped=True_, _with\_headers=True_, _with\_newlines=True_, _with\_metadata=False_, _max\_depth=1_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.to_html)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.to_html "Link to this definition")
Render this Table to HTML. Configure the structure of Table HTML by subclassing and overriding `_html_*` class attributes.

Parameters:
*   **orientation** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – one of ‘auto’, ‘horizontal’, or ‘vertical’ (or the first letter of any of those). Default ‘auto’.

*   **wrapped** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – whether or not to include the wrapping ‘<table></table>’ tags. Default `True`, set to `False` if appending multiple Table outputs or an otherwise customized HTML wrapping tag is needed.

*   **with_newlines** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Set to `True` if output should include added newlines to make the HTML more readable. Default `False`.

*   **with_metadata** (_bool/str_) – Set to `True` if output should be preceded with a Table of preset metadata, if it exists. Set to special value `'bottom'` if the metadata Table HTML should come _after_ the main HTML output.

*   **max_depth** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Indicate how deeply to nest HTML tables before simply reverting to [`repr()`](https://docs.python.org/3/library/functions.html#repr "(in Python v3.14)")-ing the nested data.

Returns:
A text string of the HTML of the rendered table.

to_text(_with\_headers=True_, _maxlen=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tableutils.html#Table.to_text)[](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table.to_text "Link to this definition")
Get the Table’s textual representation. Only works well for Tables with non-recursive data.

Parameters:
*   **with_headers** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to include a header row at the top.

*   **maxlen** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Max length of data in each cell.

[Previous](https://boltons.readthedocs.io/en/latest/strutils.html "strutils - Text manipulation")[Next](https://boltons.readthedocs.io/en/latest/tbutils.html "tbutils - Tracebacks and call stacks")

* * *

© Copyright 2025, Mahmoud Hashemi.

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/). 

[**Still Using Cursor?**Ask AI to Build a Feature. Augment creates a working PR.**Install Now**](https://server.ethicalads.io/proxy/click/10132/019cdf43-4c8d-7583-9fe4-fc89b21840e0/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

Close Ad

![Image 1](https://server.ethicalads.io/proxy/view/10132/019cdf43-4c8d-7583-9fe4-fc89b21840e0/)
