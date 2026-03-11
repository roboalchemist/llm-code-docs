# Source: https://boltons.readthedocs.io/en/latest/jsonutils.html

Title: JSON interactions — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/jsonutils.html

Markdown Content:
[boltons](https://boltons.readthedocs.io/en/latest/index.html)
`jsonutils` - JSON interactions[](https://boltons.readthedocs.io/en/latest/jsonutils.html#module-boltons.jsonutils "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

`jsonutils` aims to provide various helpers for working with JSON. Currently it focuses on providing a reliable and intuitive means of working with [JSON Lines](http://jsonlines.org/)-formatted files.

_class_ boltons.jsonutils.JSONLIterator(_file\_obj_, _ignore\_errors=False_, _reverse=False_, _rel\_seek=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/jsonutils.html#JSONLIterator)[](https://boltons.readthedocs.io/en/latest/jsonutils.html#boltons.jsonutils.JSONLIterator "Link to this definition")
The `JSONLIterator` is used to iterate over JSON-encoded objects stored in the [JSON Lines format](http://jsonlines.org/) (one object per line).

Most notably it has the ability to efficiently read from the bottom of files, making it very effective for reading in simple append-only JSONL use cases. It also has the ability to start from anywhere in the file and ignore corrupted lines.

Parameters:
*   **file_obj** (_file_) – An open file object.

*   **ignore_errors** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to skip over lines that raise an error on deserialization ([`json.loads()`](https://docs.python.org/3/library/json.html#json.loads "(in Python v3.14)")).

*   **reverse** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Controls the direction of the iteration. Defaults to `False`. If set to `True` and _rel\_seek_ is unset, seeks to the end of the file before iteration begins.

*   **rel_seek** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Used to preseek the start position of iteration. Set to 0.0 for the start of the file, 1.0 for the end, and anything in between.

_property_ cur_byte_pos[](https://boltons.readthedocs.io/en/latest/jsonutils.html#boltons.jsonutils.JSONLIterator.cur_byte_pos "Link to this definition")
A property representing where in the file the iterator is reading.

next()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/jsonutils.html#JSONLIterator.next)[](https://boltons.readthedocs.io/en/latest/jsonutils.html#boltons.jsonutils.JSONLIterator.next "Link to this definition")
Yields one [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") loaded with [`json.loads()`](https://docs.python.org/3/library/json.html#json.loads "(in Python v3.14)"), advancing the file object by one line. Raises [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "(in Python v3.14)") upon reaching the end of the file (or beginning, if `reverse` was set to `True`.

boltons.jsonutils.reverse_iter_lines(_file\_obj_, _blocksize=4096_, _preseek=True_, _encoding=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/jsonutils.html#reverse_iter_lines)[](https://boltons.readthedocs.io/en/latest/jsonutils.html#boltons.jsonutils.reverse_iter_lines "Link to this definition")
Returns an iterator over the lines from a file object, in reverse order, i.e., last line first, first line last. Uses the `file.seek()` method of file objects, and is tested compatible with `file` objects, as well as `StringIO.StringIO`.

Parameters:
*   **file_obj** (_file_) – An open file object. Note that `reverse_iter_lines` mutably reads from the file and other functions should not mutably interact with the file object after being passed. Files can be opened in bytes or text mode.

*   **blocksize** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The block size to pass to `file.read()`. Warning: keep this a fairly large multiple of 2, defaults to 4096.

*   **preseek** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Tells the function whether or not to automatically seek to the end of the file. Defaults to `True`. `preseek=False` is useful in cases when the file cursor is already in position, either at the end of the file or in the middle for relative reverse line generation.
