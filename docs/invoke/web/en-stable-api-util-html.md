# Source: https://docs.pyinvoke.org/en/stable/api/util.html

Title: util — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/util.html

Markdown Content:
_class_ invoke.util.ExceptionHandlingThread(_**kwargs:Any_)[¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread "Permalink to this definition")
Thread handler making it easier for parent to handle thread exceptions.

Based in part on Fabric 1’s ThreadHandler. See also Fabric GH issue #204.

When used directly, can be used in place of a regular `threading.Thread`. If subclassed, the subclass must do one of:

*   supply `target` to `__init__`

*   define `_run()` instead of `run()`

This is because this thread’s entire point is to wrap behavior around the thread’s execution; subclasses could not redefine `run()` without breaking that functionality.

New in version 1.0.

 __init__ (_**kwargs:Any_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread.__init__ "Permalink to this definition")
Create a new exception-handling thread instance.

Takes all regular [`threading.Thread`](https://docs.python.org/2.7/library/threading.html#threading.Thread "(in Python v2.7)") keyword arguments, via `**kwargs` for easier display of thread identity when raising captured exceptions.

 __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread.__repr__ "Permalink to this definition")
Return repr(self).

exception()→Optional[[invoke.util.ExceptionWrapper](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionWrapper "invoke.util.ExceptionWrapper")][¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread.exception "Permalink to this definition")
If an exception occurred, return an [`ExceptionWrapper`](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionWrapper "invoke.util.ExceptionWrapper") around it.

Returns
An [`ExceptionWrapper`](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionWrapper "invoke.util.ExceptionWrapper") managing the result of [`sys.exc_info`](https://docs.python.org/2.7/library/sys.html#sys.exc_info "(in Python v2.7)"), if an exception was raised during thread execution. If no exception occurred, returns `None` instead.

New in version 1.0.

_property_ is_dead _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread.is_dead "Permalink to this definition")
Returns `True` if not alive and has a stored exception.

Used to detect threads that have excepted & shut down.

New in version 1.0.

run()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread.run "Permalink to this definition")
Method representing the thread’s activity.

You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

invoke.util.has_fileno(_stream:IO_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.has_fileno "Permalink to this definition")
Cleanly determine whether `stream` has a useful `.fileno()`.

Note

This function helps determine if a given file-like object can be used with various terminal-oriented modules and functions such as [`select`](https://docs.python.org/2.7/library/select.html#module-select "(in Python v2.7)"), [`termios`](https://docs.python.org/2.7/library/termios.html#module-termios "(in Python v2.7)"), and [`tty`](https://docs.python.org/2.7/library/tty.html#module-tty "(in Python v2.7)"). For most of those, a fileno is all that is required; they’ll function even if `stream.isatty()` is `False`.

Parameters
**stream** – A file-like object.

Returns
`True` if `stream.fileno()` returns an integer, `False` otherwise (this includes when `stream` lacks a `fileno` method).

New in version 1.0.

invoke.util.helpline(_obj:[object](https://docs.python.org/2.7/library/functions.html#object "(in Python v2.7)")_)→Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.helpline "Permalink to this definition")
Yield an object’s first docstring line, or None if there was no docstring.

New in version 1.0.

invoke.util.isatty(_stream:IO_)→Union[[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.isatty "Permalink to this definition")
Cleanly determine whether `stream` is a TTY.

Specifically, first try calling `stream.isatty()`, and if that fails (e.g. due to lacking the method entirely) fallback to [`os.isatty`](https://docs.python.org/2.7/library/os.html#os.isatty "(in Python v2.7)").

Note

Most of the time, we don’t actually care about true TTY-ness, but merely whether the stream seems to have a fileno (per [`has_fileno`](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.has_fileno "invoke.util.has_fileno")). However, in some cases (notably the use of [`pty.fork`](https://docs.python.org/2.7/library/pty.html#pty.fork "(in Python v2.7)") to present a local pseudoterminal) we need to tell if a given stream has a valid fileno but _isn’t_ tied to an actual terminal. Thus, this function.

Parameters
**stream** – A file-like object.

Returns
A boolean depending on the result of calling `.isatty()` and/or [`os.isatty`](https://docs.python.org/2.7/library/os.html#os.isatty "(in Python v2.7)").

New in version 1.0.

invoke.util.task_name_sort_key(_name:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Tuple[List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")],[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.task_name_sort_key "Permalink to this definition")
Return key tuple for use sorting dotted task names, via e.g. [`sorted`](https://docs.python.org/2.7/library/functions.html#sorted "(in Python v2.7)").

New in version 1.0.

_class_ invoke.util.ExceptionWrapper(_kwargs_, _type_, _value_, _traceback_)[¶](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionWrapper "Permalink to this definition")
A namedtuple wrapping a thread-borne exception & that thread’s arguments. Mostly used as an intermediate between [`ExceptionHandlingThread`](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread "invoke.util.ExceptionHandlingThread") (which preserves initial exceptions) and [`ThreadException`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException "invoke.exceptions.ThreadException") (which holds 1..N such exceptions, as typically multiple threads are involved.)
