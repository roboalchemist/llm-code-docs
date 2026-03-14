# Type Hints

Loguru relies on a stub file [https://www.python.org/dev/peps/pep-0484/#stub-files] to document its types. This implies that these types are not
accessible during execution of your program, however they can be used by type checkers and IDE.
Also, this means that your Python interpreter has to support postponed evaluation of annotations [https://www.python.org/dev/peps/pep-0563/]
to prevent error at runtime. This is achieved with a `__future__` [https://www.python.org/dev/peps/pep-0563/#enabling-the-future-behavior-in-python-3-7] import in Python 3.7+ or by using
string literals [https://www.python.org/dev/peps/pep-0484/#forward-references] for earlier versions.

A basic usage example could look like this:

```
from __future__ import annotations

import loguru
from loguru import logger

def good_sink(message: loguru.Message):
    print("My name is", message.record["name"])

def bad_filter(record: loguru.Record):
    return record["invalid"]

logger.add(good_sink, filter=bad_filter)

```