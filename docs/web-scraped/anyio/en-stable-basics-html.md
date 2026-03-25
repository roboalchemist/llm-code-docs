# Source: https://anyio.readthedocs.io/en/stable/basics.html

Title: The basics — AnyIO 0.0.post50 documentation

URL Source: https://anyio.readthedocs.io/en/stable/basics.html

Markdown Content:
AnyIO requires Python 3.8 or later to run. It is recommended that you set up a [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) when developing or playing around with AnyIO.

Installation[](https://anyio.readthedocs.io/en/stable/basics.html#installation "Link to this heading")
-------------------------------------------------------------------------------------------------------

To install AnyIO, run:

pip install anyio

To install a supported version of [Trio](https://github.com/python-trio/trio), you can install it as an extra like this:

pip install anyio[trio]

Running async programs[](https://anyio.readthedocs.io/en/stable/basics.html#running-async-programs "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

The simplest possible AnyIO program looks like this:

from anyio import run

async def main():
    print('Hello, world!')

run(main)

This will run the program above on the default backend (asyncio). To explicitly specify which backend to run on, you can use the `backend` argument, like so:

run(main, backend='trio')
run(main, backend='asyncio')

But AnyIO code is not required to be run via [`run()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.run "anyio.run"). You can just as well use the native `run()` function of the backend library:

import sniffio
import trio
from anyio import sleep

async def main():
    print('Hello')
    await sleep(1)
    print("I'm running on", sniffio.current_async_library())

trio.run(main)

Changed in version 4.0.0: On the `asyncio` backend, `anyio.run()` now uses a back-ported version of [`asyncio.Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "(in Python v3.14)") on Pythons older than 3.11.

Backend specific options[](https://anyio.readthedocs.io/en/stable/basics.html#backend-specific-options "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

Any options exclusive to a specific backend can be passed with the `backend_options` argument to [`run()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.run "anyio.run"):

run(main, backend="asyncio", backend_options={"debug": True})
run(
    main,
    backend="trio",
    backend_options={"restrict_keyboard_interrupt_to_checkpoints": True}
)

Here is the list of supported options for each backend:

**Asyncio**:

*   options covered in the documentation of [`asyncio.Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "(in Python v3.14)")

*   `use_uvloop` (`bool`, default=False): Use the faster [uvloop](https://pypi.org/project/uvloop/) event loop implementation, if available (this is a shorthand for passing `loop_factory=uvloop.new_event_loop`, or `loop_factory=winloop.new_event_loop` if using Windows, and is ignored if `loop_factory` is passed a value other than `None`)

**Trio**: options covered in the [official documentation](https://trio.readthedocs.io/en/stable/reference-core.html#trio.run)

Changed in version 3.2.0: The default value of `use_uvloop` was changed to `False`.

Changed in version 4.0.0: The `policy` option was replaced with `loop_factory`.

Using native async libraries[](https://anyio.readthedocs.io/en/stable/basics.html#using-native-async-libraries "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

AnyIO lets you mix and match code written for AnyIO and code written for the asynchronous framework of your choice. There are a few rules to keep in mind however:

*   You can only use “native” libraries for the backend you’re running, so you cannot, for example, use a library written for [Trio](https://github.com/python-trio/trio) together with a library written for asyncio.

*   Tasks spawned by these “native” libraries on backends other than [Trio](https://github.com/python-trio/trio) are not subject to the cancellation rules enforced by AnyIO

*   Threads spawned outside of AnyIO cannot use [`from_thread.run()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.run "anyio.from_thread.run") to call asynchronous code
