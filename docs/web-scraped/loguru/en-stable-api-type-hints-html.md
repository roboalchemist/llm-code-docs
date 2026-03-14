# Source: https://loguru.readthedocs.io/en/stable/api/type_hints.html

Title: Type Hints — loguru documentation

URL Source: https://loguru.readthedocs.io/en/stable/api/type_hints.html

Markdown Content:
[loguru](https://loguru.readthedocs.io/en/stable/index.html)

Loguru relies on a [stub file](https://www.python.org/dev/peps/pep-0484/#stub-files) to document its types. This implies that these types are not accessible during execution of your program, however they can be used by type checkers and IDE. Also, this means that your Python interpreter has to support [postponed evaluation of annotations](https://www.python.org/dev/peps/pep-0563/) to prevent error at runtime. This is achieved with a [`__future__`](https://www.python.org/dev/peps/pep-0563/#enabling-the-future-behavior-in-python-3-7) import in Python 3.7+ or by using [string literals](https://www.python.org/dev/peps/pep-0484/#forward-references) for earlier versions.

A basic usage example could look like this:

from  __future__  import annotations

import loguru
from loguru import logger

def good_sink(message: loguru.Message):
    print("My name is", message.record["name"])

def bad_filter(record: loguru.Record):
    return record["invalid"]

logger.add(good_sink, filter=bad_filter)

$ mypy test.py
test.py:8: error: TypedDict "Record" has no key 'invalid'
Found 1 error in 1 file (checked 1 source file)

There are several internal types to which you can be exposed using Loguru’s public API, they are listed here and might be useful to type hint your code:

*   `Logger`: the usual [`Logger`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger "loguru._logger.Logger") object (also returned by [`opt()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.opt "loguru._logger.Logger.opt"), [`bind()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.bind "loguru._logger.Logger.bind") and [`patch()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.patch "loguru._logger.Logger.patch")).

*   `Message`: the formatted logging message sent to the sinks (a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") with `record` attribute).

*   `Record`: the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)") containing all contextual information of the logged message.

*   `Level`: the [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "(in Python v3.13)") returned by [`level()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.level "loguru._logger.Logger.level") (with `name`, `no`, `color` and `icon` attributes).

*   `Catcher`: the context decorator returned by [`catch()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.catch "loguru._logger.Logger.catch").

*   `Contextualizer`: the context decorator returned by [`contextualize()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.contextualize "loguru._logger.Logger.contextualize").

*   `AwaitableCompleter`: the awaitable object returned by [`complete()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.complete "loguru._logger.Logger.complete").

*   `RecordFile`: the `record["file"]` with `name` and `path` attributes.

*   `RecordLevel`: the `record["level"]` with `name`, `no` and `icon` attributes.

*   `RecordThread`: the `record["thread"]` with `id` and `name` attributes.

*   `RecordProcess`: the `record["process"]` with `id` and `name` attributes.

*   `RecordException`: the `record["exception"]` with `type`, `value` and `traceback` attributes.

If that is not enough, one can also use the [`loguru-mypy`](https://github.com/kornicameister/loguru-mypy) library developed by [@kornicameister](https://github.com/kornicameister). Plugin can be installed separately using:

pip install loguru-mypy

It helps to catch several possible runtime errors by performing additional checks like:

*   `opt(lazy=True)` loggers accepting only `typing.Callable[[], typing.Any]` arguments

*   `opt(record=True)` loggers wrongly calling log handler like so `logger.info(..., record={})`

*   and even more…

For more details, go to official [documentation of `loguru-mypy`](https://github.com/kornicameister/loguru-mypy/blob/master/README.md).

See also: [Source Code of Type Hints](https://loguru.readthedocs.io/en/stable/api/type_hints_source.html#type-hints-source).
