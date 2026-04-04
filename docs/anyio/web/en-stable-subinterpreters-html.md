# Source: https://anyio.readthedocs.io/en/stable/subinterpreters.html

Title: Working with subinterpreters — AnyIO 0.0.post50 documentation

URL Source: https://anyio.readthedocs.io/en/stable/subinterpreters.html

Markdown Content:
[AnyIO](https://anyio.readthedocs.io/en/stable/index.html)
Subinterpreters offer a middle ground between worker threads and worker processes. They allow you to utilize multiple CPU cores to run Python code while avoiding the overhead and complexities of spawning subprocesses.

Warning

Subinterpreter support is considered **experimental**. The underlying Python API for managing subinterpreters has not been finalized yet, and has had little real-world testing. As such, it is not recommended to use this feature for anything important yet.

Running a function in a worker interpreter[](https://anyio.readthedocs.io/en/stable/subinterpreters.html#running-a-function-in-a-worker-interpreter "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Running functions in a worker interpreter makes sense when:

*   The code you want to run in parallel is CPU intensive

*   The code is either pure Python code, or extension code that does not release the Global Interpreter Lock (GIL)

If the code you’re trying to run only does blocking network I/O, or file I/O, then you’re better off using [worker thread](https://anyio.readthedocs.io/en/stable/threads.html) instead.

This is done by using [`to_interpreter.run_sync()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_interpreter.run_sync "anyio.to_interpreter.run_sync"):

import time

from anyio import run, to_interpreter

from yourothermodule import cpu_intensive_function

async def main():
    result = await to_interpreter.run_sync(
        cpu_intensive_function, 'Hello, ', 'world!'
    )
    print(result)

run(main)

Limitations[](https://anyio.readthedocs.io/en/stable/subinterpreters.html#limitations "Link to this heading")
--------------------------------------------------------------------------------------------------------------

*   Subinterpreters are only supported on Python 3.13 or later

*   Code in the `__main__` module cannot be run with this (as a consequence, this applies to any functions defined in the REPL)

*   The target functions cannot react to cancellation

*   Unlike with threads, the code running in the subinterpreter cannot share mutable data with other interpreters/threads (however, sharing _immutable_ data is fine)
