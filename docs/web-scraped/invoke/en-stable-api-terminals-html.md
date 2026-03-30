# Source: https://docs.pyinvoke.org/en/stable/api/terminals.html

Title: terminals — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/terminals.html

Markdown Content:
Utility functions surrounding terminal devices & I/O.

Much of this code performs platform-sensitive branching, e.g. Windows support.

This is its own module to abstract away what would otherwise be distracting logic-flow interruptions.

invoke.terminals.WINDOWS _=False_[¶](https://docs.pyinvoke.org/en/stable/api/terminals.html#invoke.terminals.WINDOWS "Permalink to this definition")
Whether or not the current platform appears to be Windows in nature.

Note that Cygwin’s Python is actually close enough to “real” UNIXes that it doesn’t need (or want!) to use PyWin32 – so we only test for literal Win32 setups (vanilla Python, ActiveState etc) here.

New in version 1.0.

invoke.terminals.bytes_to_read(_input\_:IO_)→[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/terminals.html#invoke.terminals.bytes_to_read "Permalink to this definition")
Query stream `input_` to see how many bytes may be readable.

Note

If we are unable to tell (e.g. if `input_` isn’t a true file descriptor or isn’t a valid TTY) we fall back to suggesting reading 1 byte only.

Parameters
**input** – Input stream object (file-like).

Returns
[`int`](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)") number of bytes to read.

New in version 1.0.

invoke.terminals.character_buffered(_stream:IO_)→Generator[[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/terminals.html#invoke.terminals.character_buffered "Permalink to this definition")
Force local terminal `stream` be character, not line, buffered.

Only applies to Unix-based systems; on Windows this is a no-op.

New in version 1.0.

invoke.terminals.pty_size()→Tuple[[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)"),[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/terminals.html#invoke.terminals.pty_size "Permalink to this definition")
Determine current local pseudoterminal dimensions.

Returns
A `(num_cols, num_rows)` two-tuple describing PTY size. Defaults to `(80, 24)` if unable to get a sensible result dynamically.

New in version 1.0.

invoke.terminals.ready_for_reading(_input\_:IO_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/terminals.html#invoke.terminals.ready_for_reading "Permalink to this definition")
Test `input_` to determine whether a read action will succeed.

Parameters
**input** – Input stream object (file-like).

Returns
`True` if a read should succeed, `False` otherwise.

New in version 1.0.

invoke.terminals.stdin_is_foregrounded_tty(_stream:IO_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/terminals.html#invoke.terminals.stdin_is_foregrounded_tty "Permalink to this definition")
Detect if given stdin `stream` seems to be in the foreground of a TTY.

Specifically, compares the current Python process group ID to that of the stream’s file descriptor to see if they match; if they do not match, it is likely that the process has been placed in the background.

This is used as a test to determine whether we should manipulate an active stdin so it runs in a character-buffered mode; touching the terminal in this way when the process is backgrounded, causes most shells to pause execution.

Note

Processes that aren’t attached to a terminal to begin with, will always fail this test, as it starts with “do you have a real `fileno`?”.

New in version 1.0.
