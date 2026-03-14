# Source: https://docs.pyinvoke.org/en/stable/api/exceptions.html

Title: exceptions — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/exceptions.html

Markdown Content:
Custom exception classes.

These vary in use case from “we needed a specific data structure layout in exceptions used for message-passing” to simply “we needed to express an error condition in a way easily told apart from other, truly unexpected errors”.

_exception_ invoke.exceptions.AmbiguousEnvVar[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AmbiguousEnvVar "Permalink to this definition")
Raised when loading env var config keys has an ambiguous target.

New in version 1.0.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AmbiguousEnvVar.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.AuthFailure(_result:Result_, _prompt:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AuthFailure "Permalink to this definition")
An authentication failure, e.g. due to an incorrect `sudo` password.

Note

[`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") objects attached to these exceptions typically lack exit code information, since the command was never fully executed - the exception was raised instead.

New in version 1.0.

 __init__ (_result:Result_, _prompt:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AuthFailure.__init__ "Permalink to this definition") __str__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AuthFailure.__str__ "Permalink to this definition")
Return str(self).

_exception_ invoke.exceptions.CollectionNotFound(_name:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _start:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CollectionNotFound "Permalink to this definition") __init__ (_name:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _start:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CollectionNotFound.__init__ "Permalink to this definition") __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CollectionNotFound.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.CommandTimedOut(_result:Result_, _timeout:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CommandTimedOut "Permalink to this definition")
Raised when a subprocess did not exit within a desired timeframe.

 __init__ (_result:Result_, _timeout:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CommandTimedOut.__init__ "Permalink to this definition") __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CommandTimedOut.__repr__ "Permalink to this definition")
Return repr(self).

 __str__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CommandTimedOut.__str__ "Permalink to this definition")
Return str(self).

_exception_ invoke.exceptions.Exit(_message:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _code:Optional[[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Exit "Permalink to this definition")
Simple custom stand-in for SystemExit.

Replaces scattered sys.exit calls, improves testability, allows one to catch an exit request without intercepting real SystemExits (typically an unfriendly thing to do, as most users calling [`sys.exit`](https://docs.python.org/2.7/library/sys.html#sys.exit "(in Python v2.7)") rather expect it to truly exit.)

Defaults to a non-printing, exit-0 friendly termination behavior if the exception is uncaught.

If `code` (an int) given, that code is used to exit.

If `message` (a string) given, it is printed to standard error, and the program exits with code `1` by default (unless overridden by also giving `code` explicitly.)

New in version 1.0.

 __init__ (_message:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _code:Optional[[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Exit.__init__ "Permalink to this definition") __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Exit.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.Failure(_result:Result_, _reason:Optional[[WatcherError](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError")]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure "Permalink to this definition")
Exception subclass representing failure of a command execution.

“Failure” may mean the command executed and the shell indicated an unusual result (usually, a non-zero exit code), or it may mean something else, like a `sudo` command which was aborted when the supplied password failed authentication.

Two attributes allow introspection to determine the nature of the problem:

*   `result`: a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") instance with info about the command being executed and, if it ran to completion, how it exited.

*   `reason`: a wrapped exception instance if applicable (e.g. a [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") raised [`WatcherError`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError")) or `None` otherwise, in which case, it’s probably a [`Failure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure "invoke.exceptions.Failure") subclass indicating its own specific nature, such as [`UnexpectedExit`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnexpectedExit "invoke.exceptions.UnexpectedExit") or [`CommandTimedOut`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CommandTimedOut "invoke.exceptions.CommandTimedOut").

This class is only rarely raised by itself; most of the time [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") (or a wrapper of same, such as [`Context.sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo")) will raise a specific subclass like [`UnexpectedExit`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnexpectedExit "invoke.exceptions.UnexpectedExit") or [`AuthFailure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AuthFailure "invoke.exceptions.AuthFailure").

New in version 1.0.

 __init__ (_result:Result_, _reason:Optional[[WatcherError](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError")]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure.__init__ "Permalink to this definition") __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure.__repr__ "Permalink to this definition")
Return repr(self).

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

streams_for_display()→Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure.streams_for_display "Permalink to this definition")
Return stdout/err streams as necessary for error display.

Subject to the following rules:

*   If a given stream was _not_ hidden during execution, a placeholder is used instead, to avoid printing it twice.

*   Only the last 10 lines of stream text is included.

*   PTY-driven execution will lack stderr, and a specific message to this effect is returned instead of a stderr dump.

Returns
Two-tuple of stdout, stderr strings.

New in version 1.3.

_exception_ invoke.exceptions.ParseError(_msg:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _context:Optional[ParserContext]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ParseError "Permalink to this definition")
An error arising from the parsing of command-line flags/arguments.

Ambiguous input, invalid task names, invalid flags, etc.

New in version 1.0.

 __init__ (_msg:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _context:Optional[ParserContext]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ParseError.__init__ "Permalink to this definition") __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ParseError.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.PlatformError[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.PlatformError "Permalink to this definition")
Raised when an illegal operation occurs for the current platform.

E.g. Windows users trying to use functionality requiring the `pty` module.

Typically used to present a clearer error message to the user.

New in version 1.0.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.PlatformError.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.ResponseNotAccepted[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ResponseNotAccepted "Permalink to this definition")
A responder/watcher class noticed a ‘bad’ response to its submission.

Mostly used by [`FailingResponder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.FailingResponder "invoke.watchers.FailingResponder") and subclasses, e.g. “oh dear I autosubmitted a sudo password and it was incorrect.”

New in version 1.0.

_exception_ invoke.exceptions.SubprocessPipeError[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.SubprocessPipeError "Permalink to this definition")
Some problem was encountered handling subprocess pipes (stdout/err/in).

Typically only for corner cases; most of the time, errors in this area are raised by the interpreter or the operating system, and end up wrapped in a [`ThreadException`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException "invoke.exceptions.ThreadException").

New in version 1.3.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.SubprocessPipeError.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.ThreadException(_exceptions:List[ExceptionWrapper]_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException "Permalink to this definition")
One or more exceptions were raised within background threads.

The real underlying exceptions are stored in the [`exceptions`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException.exceptions "invoke.exceptions.ThreadException.exceptions") attribute; see its documentation for data structure details.

Note

Threads which did not encounter an exception, do not contribute to this exception object and thus are not present inside [`exceptions`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException.exceptions "invoke.exceptions.ThreadException.exceptions").

New in version 1.0.

 __init__ (_exceptions:List[ExceptionWrapper]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException.__init__ "Permalink to this definition") __str__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException.__str__ "Permalink to this definition")
Return str(self).

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

exceptions _:Tuple[ExceptionWrapper,...]_ _=()_[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException.exceptions "Permalink to this definition")
A tuple of [`ExceptionWrappers`](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionWrapper "invoke.util.ExceptionWrapper") containing the initial thread constructor kwargs (because [`threading.Thread`](https://docs.python.org/2.7/library/threading.html#threading.Thread "(in Python v2.7)") subclasses should always be called with kwargs) and the caught exception for that thread as seen by [`sys.exc_info`](https://docs.python.org/2.7/library/sys.html#sys.exc_info "(in Python v2.7)") (so: type, value, traceback).

Note

The ordering of this attribute is not well-defined.

Note

Thread kwargs which appear to be very long (e.g. IO buffers) will be truncated when printed, to avoid huge unreadable error display.

_exception_ invoke.exceptions.UncastableEnvVar[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UncastableEnvVar "Permalink to this definition")
Raised on attempted env var loads whose default values are too rich.

E.g. trying to stuff `MY_VAR="foo"` into `{'my_var': ['uh', 'oh']}` doesn’t make any sense until/if we implement some sort of transform option.

New in version 1.0.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UncastableEnvVar.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.UnexpectedExit(_result:Result_, _reason:Optional[[WatcherError](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError")]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnexpectedExit "Permalink to this definition")
A shell command ran to completion but exited with an unexpected exit code.

Its string representation displays the following:

*   Command executed;

*   Exit code;

*   The last 10 lines of stdout, if it was hidden;

*   The last 10 lines of stderr, if it was hidden and non-empty (e.g. pty=False; when pty=True, stderr never happens.)

New in version 1.0.

 __str__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnexpectedExit.__str__ "Permalink to this definition")
Return str(self).

_exception_ invoke.exceptions.UnknownFileType[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnknownFileType "Permalink to this definition")
A config file of an unknown type was specified and cannot be loaded.

New in version 1.0.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnknownFileType.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.UnpicklableConfigMember[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnpicklableConfigMember "Permalink to this definition")
A config file contained module objects, which can’t be pickled/copied.

We raise this more easily catchable exception instead of letting the (unclearly phrased) TypeError bubble out of the pickle module. (However, to avoid our own fragile catching of that error, we head it off by explicitly testing for module members.)

New in version 1.0.2.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnpicklableConfigMember.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_exception_ invoke.exceptions.WatcherError[¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "Permalink to this definition")
Generic parent exception class for [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher")-related errors.

Typically, one of these exceptions indicates a [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") noticed something anomalous in an output stream, such as an authentication response failure.

[`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") catches these and attaches them to [`Failure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure "invoke.exceptions.Failure") exceptions so they can be referenced by intermediate code and/or act as extra info for end users.

New in version 1.0.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)
