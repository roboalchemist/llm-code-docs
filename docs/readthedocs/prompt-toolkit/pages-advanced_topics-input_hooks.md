# Input hooks

Input hooks are a tool for inserting an external event loop into the
prompt_toolkit event loop, so that the other loop can run as long as
prompt_toolkit (actually asyncio) is idle. This is used in applications like
IPython [https://ipython.org/], so that GUI toolkits can display their
windows while we wait at the prompt for user input.

As a consequence, we will “trampoline” back and forth between two event loops.

Note

This will use a `SelectorEventLoop`, not the :class:
`ProactorEventLoop` (on Windows) due to the way the
implementation works (contributions are welcome to make that work).
