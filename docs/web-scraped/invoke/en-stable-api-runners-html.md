# Source: https://docs.pyinvoke.org/en/stable/api/runners.html

Title: runners — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/runners.html

Markdown Content:
_class_ invoke.runners.Runner(_context:Context_)[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "Permalink to this definition")
Partially-abstract core command-running API.

This class is not usable by itself and must be subclassed, implementing a number of methods such as [`start`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.start "invoke.runners.Runner.start"), [`wait`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.wait "invoke.runners.Runner.wait") and [`returncode`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.returncode "invoke.runners.Runner.returncode"). For a subclass implementation example, see the source code for [`Local`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local "invoke.runners.Local").

New in version 1.0.

 __init__ (_context:Context_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.__init__ "Permalink to this definition")
Create a new runner with a handle on some [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context").

Parameters
**context** –

a [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") instance, used to transmit default options and provide access to other contextualized information (e.g. a remote-oriented [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") might want a [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") subclass holding info about hostnames and ports.)

Note

The [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") given to [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") instances **must** contain default config values for the [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") class in question. At a minimum, this means values for each of the default [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") keyword arguments such as `echo` and `warn`.

Raises
[**exceptions.ValueError**](https://docs.python.org/2.7/library/exceptions.html#exceptions.ValueError "(in Python v2.7)") – if not all expected default values are found in `context`.

context[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.context "Permalink to this definition")
The [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") given to the same-named argument of [`__init__`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.__init__ "invoke.runners.Runner.__init__").

program_finished[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.program_finished "Permalink to this definition")
A [`threading.Event`](https://docs.python.org/2.7/library/threading.html#threading.Event "(in Python v2.7)") signaling program completion.

Typically set after [`wait`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.wait "invoke.runners.Runner.wait") returns. Some IO mechanisms rely on this to know when to exit an infinite read loop.

read_chunk_size _=1000_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_chunk_size "Permalink to this definition")
How many bytes (at maximum) to read per iteration of stream reads.

input_sleep _=0.01_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.input_sleep "Permalink to this definition")
How many seconds to sleep on each iteration of the stdin read loop and other otherwise-fast loops.

warned_about_pty_fallback[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.warned_about_pty_fallback "Permalink to this definition")
Whether pty fallback warning has been emitted.

watchers _:List[StreamWatcher]_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.watchers "Permalink to this definition")
A list of [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") instances for use by [`respond`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.respond "invoke.runners.Runner.respond"). Is filled in at runtime by [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run").

run(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _**kwargs:Any_)→Optional[[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "Permalink to this definition")
Execute `command`, returning an instance of [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") once complete.

By default, this method is synchronous (it only returns once the subprocess has completed), and allows interactive keyboard communication with the subprocess.

It can instead behave asynchronously (returning early & requiring interaction with the resulting object to manage subprocess lifecycle) if you specify `asynchronous=True`. Furthermore, you can completely disassociate the subprocess from Invoke’s control (allowing it to persist on its own after Python exits) by saying `disown=True`. See the per-kwarg docs below for details on both of these.

Note

All kwargs will default to the values found in this instance’s [`context`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.context "invoke.runners.Runner.context") attribute, specifically in its configuration’s `run` subtree (e.g. `run.echo` provides the default value for the `echo` keyword, etc). The base default values are described in the parameter list below.

Parameters
*   **command** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The shell command to execute.

*   **asynchronous** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

When set to `True` (default `False`), enables asynchronous behavior, as follows:

    *   Connections to the controlling terminal are disabled, meaning you will not see the subprocess output and it will not respond to your keyboard input - similar to `hide=True` and `in_stream=False` (though explicitly given `(out|err|in)_stream` file-like objects will still be honored as normal).

    *   [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") returns immediately after starting the subprocess, and its return value becomes an instance of [`Promise`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "invoke.runners.Promise") instead of [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result").

    *   [`Promise`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "invoke.runners.Promise") objects are primarily useful for their [`join`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise.join "invoke.runners.Promise.join") method, which blocks until the subprocess exits (similar to threading APIs) and either returns a final [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") or raises an exception, just as a synchronous `run` would.

> *   As with threading and similar APIs, users of `asynchronous=True` should make sure to `join` their [`Promise`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "invoke.runners.Promise") objects to prevent issues with interpreter shutdown.
> 
>         *   One easy way to handle such cleanup is to use the [`Promise`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "invoke.runners.Promise") as a context manager - it will automatically `join` at the exit of the context block.

New in version 1.4.

*   **disown** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

When set to `True` (default `False`), returns immediately like `asynchronous=True`, but does not perform any background work related to that subprocess (it is completely ignored). This allows subprocesses using shell backgrounding or similar techniques (e.g. trailing `&`, `nohup`) to persist beyond the lifetime of the Python process running Invoke.

Note

If you’re unsure whether you want this or `asynchronous`, you probably want `asynchronous`! 
Specifically, `disown=True` has the following behaviors:

    *   The return value is `None` instead of a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") or subclass.

    *   No I/O worker threads are spun up, so you will have no access to the subprocess’ stdout/stderr, your stdin will not be forwarded, `(out|err|in)_stream` will be ignored, and features like `watchers` will not function.

    *   No exit code is checked for, so you will not receive any errors if the subprocess fails to exit cleanly.

    *   `pty=True` may not function correctly (subprocesses may not run at all; this seems to be a potential bug in Python’s `pty.fork`) unless your command line includes tools such as `nohup` or (the shell builtin) `disown`.

New in version 1.4.

*   **dry** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

Whether to dry-run instead of truly invoking the given command. See [`--dry`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-dry) (which flips this on globally) for details on this behavior.

New in version 1.3.

*   **echo** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

Controls whether [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") prints the command string to local stdout prior to executing it. Default: `False`.

Note

`hide=True` will override `echo=True` if both are given. 
*   **echo_format** –

A string, which when passed to Python’s inbuilt `.format` method, will change the format of the output when `run.echo` is set to true.

Currently, only `{command}` is supported as a parameter.

Defaults to printing the full command string in ANSI-escaped bold.

*   **echo_stdin** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

Whether to write data from `in_stream` back to `out_stream`.

In other words, in normal interactive usage, this parameter controls whether Invoke mirrors what you type back to your terminal.

By default (when `None`), this behavior is triggered by the following:

> *   Not using a pty to run the subcommand (i.e. `pty=False`), as ptys natively echo stdin to stdout on their own;
> 
>     *   And when the controlling terminal of Invoke itself (as per `in_stream`) appears to be a valid terminal device or TTY. (Specifically, when [`isatty`](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.isatty "invoke.util.isatty") yields a `True` result when given `in_stream`.)
> 
> Note
> 
> 
> This property tends to be `False` when piping another program’s output into an Invoke session, or when running Invoke within another program (e.g. running Invoke from itself).

If both of those properties are true, echoing will occur; if either is false, no echoing will be performed.

When not `None`, this parameter will override that auto-detection and force, or disable, echoing.

*   **encoding** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Override auto-detection of which encoding the subprocess is using for its stdout/stderr streams (which defaults to the return value of [`default_encoding`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.default_encoding "invoke.runners.default_encoding")).

*   **err_stream** – Same as `out_stream`, except for standard error, and defaulting to `sys.stderr`.

*   **env** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) –

By default, subprocesses receive a copy of Invoke’s own environment (i.e. `os.environ`). Supply a dict here to update that child environment.

For example, 
```
run('command', env={'PYTHONPATH':
'/some/virtual/env/maybe'})
```
 would modify the `PYTHONPATH` env var, with the rest of the child’s env looking identical to the parent.

See also

`replace_env` for changing ‘update’ to ‘replace’. 
*   **fallback** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Controls auto-fallback behavior re: problems offering a pty when `pty=True`. Whether this has any effect depends on the specific [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") subclass being invoked. Default: `True`.

*   **hide** –

Allows the caller to disable `run`’s default behavior of copying the subprocess’ stdout and stderr to the controlling terminal. Specify `hide='out'` (or `'stdout'`) to hide only the stdout stream, `hide='err'` (or `'stderr'`) to hide only stderr, or `hide='both'` (or `True`) to hide both streams.

The default value is `None`, meaning to print everything; `False` will also disable hiding.

Note

Stdout and stderr are always captured and stored in the `Result` object, regardless of `hide`’s value. Note

`hide=True` will also override `echo=True` if both are given (either as kwargs or via config/CLI). 
*   **in_stream** –

A file-like stream object to used as the subprocess’ standard input. If `None` (the default), `sys.stdin` will be used.

If `False`, will disable stdin mirroring entirely (though other functionality which writes to the subprocess’ stdin, such as autoresponding, will still function.) Disabling stdin mirroring can help when `sys.stdin` is a misbehaving non-stream object, such as under test harnesses or headless command runners.

*   **out_stream** – A file-like stream object to which the subprocess’ standard output should be written. If `None` (the default), `sys.stdout` will be used.

*   **pty** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

By default, `run` connects directly to the invoked process and reads its stdout/stderr streams. Some programs will buffer (or even behave) differently in this situation compared to using an actual terminal or pseudoterminal (pty). To use a pty instead of the default behavior, specify `pty=True`.

Warning

Due to their nature, ptys have a single output stream, so the ability to tell stdout apart from stderr is **not possible** when `pty=True`. As such, all output will appear on `out_stream` (see below) and be captured into the `stdout` result attribute. `err_stream` and `stderr` will always be empty when `pty=True`. 
*   **replace_env** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – When `True`, causes the subprocess to receive the dictionary given to `env` as its entire shell environment, instead of updating a copy of `os.environ` (which is the default behavior). Default: `False`.

*   **shell** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Which shell binary to use. Default: `/bin/bash` (on Unix; `COMSPEC` or `cmd.exe` on Windows.)

*   **timeout** –

Cause the runner to submit an interrupt to the subprocess and raise [`CommandTimedOut`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CommandTimedOut "invoke.exceptions.CommandTimedOut"), if the command takes longer than `timeout` seconds to execute. Defaults to `None`, meaning no timeout.

New in version 1.3.

*   **warn** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

Whether to warn and continue, instead of raising [`UnexpectedExit`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnexpectedExit "invoke.exceptions.UnexpectedExit"), when the executed command exits with a nonzero status. Default: `False`.

Note

This setting has no effect on exceptions, which will still be raised, typically bundled in [`ThreadException`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException "invoke.exceptions.ThreadException") objects if they were raised by the IO worker threads.

Similarly, [`WatcherError`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError") exceptions raised by [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") instances will also ignore this setting, and will usually be bundled inside [`Failure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure "invoke.exceptions.Failure") objects (in order to preserve the execution context).

Ditto [`CommandTimedOut`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.CommandTimedOut "invoke.exceptions.CommandTimedOut") - basically, anything that prevents a command from actually getting to “exited with an exit code” ignores this flag. 
*   **watchers** –

A list of [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") instances which will be used to scan the program’s `stdout` or `stderr` and may write into its `stdin` (typically `bytes` objects) in response to patterns or other heuristics.

See [Automatically responding to program output](https://docs.pyinvoke.org/en/stable/concepts/watchers.html) for details on this functionality.

Default: `[]`.

Returns
[`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result"), or a subclass thereof.

Raises
[`UnexpectedExit`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.UnexpectedExit "invoke.exceptions.UnexpectedExit"), if the command exited nonzero and `warn` was `False`.

Raises
[`Failure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure "invoke.exceptions.Failure"), if the command didn’t even exit cleanly, e.g. if a [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") raised [`WatcherError`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError").

Raises
[`ThreadException`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException "invoke.exceptions.ThreadException") (if the background I/O threads encountered exceptions other than [`WatcherError`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError")).

New in version 1.0.

make_promise()→[invoke.runners.Promise](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "invoke.runners.Promise")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.make_promise "Permalink to this definition")
Return a [`Promise`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "invoke.runners.Promise") allowing async control of the rest of lifecycle.

New in version 1.4.

create_io_threads()→Tuple[Dict[Callable,[invoke.util.ExceptionHandlingThread](https://docs.pyinvoke.org/en/stable/api/util.html#invoke.util.ExceptionHandlingThread "invoke.util.ExceptionHandlingThread")],List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")],List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.create_io_threads "Permalink to this definition")
Create and return a dictionary of IO thread worker objects.

Caller is expected to handle persisting and/or starting the wrapped threads.

generate_result(_**kwargs:Any_)→[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.generate_result "Permalink to this definition")
Create & return a suitable [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") instance from the given `kwargs`.

Subclasses may wish to override this in order to manipulate things or generate a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") subclass (e.g. ones containing additional metadata besides the default).

New in version 1.0.

read_proc_output(_reader:Callable_)→Generator[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_proc_output "Permalink to this definition")
Iteratively read & decode bytes from a subprocess’ out/err stream.

Parameters
**reader** –

A literal reader function/partial, wrapping the actual stream object in question, which takes a number of bytes to read, and returns that many bytes (or `None`).

`reader` should be a reference to either [`read_proc_stdout`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_proc_stdout "invoke.runners.Runner.read_proc_stdout") or [`read_proc_stderr`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_proc_stderr "invoke.runners.Runner.read_proc_stderr"), which perform the actual, platform/library specific read calls.

Returns
A generator yielding strings.

Specifically, each resulting string is the result of decoding [`read_chunk_size`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_chunk_size "invoke.runners.Runner.read_chunk_size") bytes read from the subprocess’ out/err stream.

New in version 1.0.

write_our_output(_stream:IO_, _string:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.write_our_output "Permalink to this definition")
Write `string` to `stream`.

Also calls `.flush()` on `stream` to ensure that real terminal streams don’t buffer.

Parameters
*   **stream** – A file-like stream object, mapping to the `out_stream` or `err_stream` parameters of [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run").

*   **string** – A Unicode string object.

Returns
`None`.

New in version 1.0.

handle_stdout(_buffer\_:List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]_, _hide:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_, _output:IO_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.handle_stdout "Permalink to this definition")
Read process’ stdout, storing into a buffer & printing/parsing.

Intended for use as a thread target. Only terminates when all stdout from the subprocess has been read.

Parameters
*   **buffer** – The capture buffer shared with the main thread.

*   **hide** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether or not to replay data into `output`.

*   **output** – Output stream (file-like object) to write data into when not hiding.

Returns
`None`.

New in version 1.0.

handle_stderr(_buffer\_:List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]_, _hide:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_, _output:IO_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.handle_stderr "Permalink to this definition")
Read process’ stderr, storing into a buffer & printing/parsing.

Identical to [`handle_stdout`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.handle_stdout "invoke.runners.Runner.handle_stdout") except for the stream read from; see its docstring for API details.

New in version 1.0.

read_our_stdin(_input\_:IO_)→Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_our_stdin "Permalink to this definition")
Read & decode bytes from a local stdin stream.

Parameters
**input** – Actual stream object to read from. Maps to `in_stream` in [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run"), so will often be `sys.stdin`, but might be any stream-like object.

Returns
A Unicode string, the result of decoding the read bytes (this might be the empty string if the pipe has closed/reached EOF); or `None` if stdin wasn’t ready for reading yet.

New in version 1.0.

handle_stdin(_input\_:IO_, _output:IO_, _echo:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.handle_stdin "Permalink to this definition")
Read local stdin, copying into process’ stdin as necessary.

Intended for use as a thread target.

Note

Because real terminal stdin streams have no well-defined “end”, if such a stream is detected (based on existence of a callable `.fileno()`) this method will wait until [`program_finished`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.program_finished "invoke.runners.Runner.program_finished") is set, before terminating.

When the stream doesn’t appear to be from a terminal, the same semantics as [`handle_stdout`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.handle_stdout "invoke.runners.Runner.handle_stdout") are used - the stream is simply `read()` from until it returns an empty value.

Parameters
*   **input** – Stream (file-like object) from which to read.

*   **output** – Stream (file-like object) to which echoing may occur.

*   **echo** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – User override option for stdin-stdout echoing.

Returns
`None`.

New in version 1.0.

should_echo_stdin(_input\_:IO_, _output:IO_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.should_echo_stdin "Permalink to this definition")
Determine whether data read from `input_` should echo to `output`.

Used by [`handle_stdin`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.handle_stdin "invoke.runners.Runner.handle_stdin"); tests attributes of `input_` and `output`.

Parameters
*   **input** – Input stream (file-like object).

*   **output** – Output stream (file-like object).

Returns
A `bool`.

New in version 1.0.

respond(_buffer\_:List[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.respond "Permalink to this definition")
Write to the program’s stdin in response to patterns in `buffer_`.

The patterns and responses are driven by the [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") instances from the `watchers` kwarg of [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") - see [Automatically responding to program output](https://docs.pyinvoke.org/en/stable/concepts/watchers.html) for a conceptual overview.

Parameters
**buffer** – The capture buffer for this thread’s particular IO stream.

Returns
`None`.

New in version 1.0.

generate_env(_env:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_, _replace\_env:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_)→Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.generate_env "Permalink to this definition")
Return a suitable environment dict based on user input & behavior.

Parameters
*   **env** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – Dict supplying overrides or full env, depending.

*   **replace_env** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether `env` updates, or is used in place of, the value of [`os.environ`](https://docs.python.org/2.7/library/os.html#os.environ "(in Python v2.7)").

Returns
A dictionary of shell environment vars.

New in version 1.0.

should_use_pty(_pty:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_, _fallback:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.should_use_pty "Permalink to this definition")
Should execution attempt to use a pseudo-terminal?

Parameters
*   **pty** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether the user explicitly asked for a pty.

*   **fallback** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether falling back to non-pty execution should be allowed, in situations where `pty=True` but a pty could not be allocated.

New in version 1.0.

_property_ has_dead_threads _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.has_dead_threads "Permalink to this definition")
Detect whether any IO threads appear to have terminated unexpectedly.

Used during process-completion waiting (in [`wait`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.wait "invoke.runners.Runner.wait")) to ensure we don’t deadlock our child process if our IO processing threads have errored/died.

Returns
`True` if any threads appear to have terminated with an exception, `False` otherwise.

New in version 1.0.

wait()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.wait "Permalink to this definition")
Block until the running command appears to have exited.

Returns
`None`.

New in version 1.0.

write_proc_stdin(_data:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.write_proc_stdin "Permalink to this definition")
Write encoded `data` to the running process’ stdin.

Parameters
**data** – A Unicode string.

Returns
`None`.

New in version 1.0.

decode(_data:bytes_)→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.decode "Permalink to this definition")
Decode some `data` bytes, returning Unicode.

New in version 1.0.

_property_ process_is_finished _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.process_is_finished "Permalink to this definition")
Determine whether our subprocess has terminated.

Note

The implementation of this method should be nonblocking, as it is used within a query/poll loop.

Returns
`True` if the subprocess has finished running, `False` otherwise.

New in version 1.0.

start(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _shell:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _env:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.start "Permalink to this definition")
Initiate execution of `command` (via `shell`, with `env`).

Typically this means use of a forked subprocess or requesting start of execution on a remote system.

In most cases, this method will also set subclass-specific member variables used in other methods such as [`wait`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.wait "invoke.runners.Runner.wait") and/or [`returncode`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.returncode "invoke.runners.Runner.returncode").

Parameters
*   **command** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Command string to execute.

*   **shell** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Shell to use when executing `command`.

*   **env** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – Environment dict used to prep shell environment.

New in version 1.0.

start_timer(_timeout:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.start_timer "Permalink to this definition")
Start a timer to [`kill`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.kill "invoke.runners.Runner.kill") our subprocess after `timeout` seconds.

read_proc_stdout(_num\_bytes:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_)→Optional[bytes][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_proc_stdout "Permalink to this definition")
Read `num_bytes` from the running process’ stdout stream.

Parameters
**num_bytes** ([_int_](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) – Number of bytes to read at maximum.

Returns
A string/bytes object.

New in version 1.0.

read_proc_stderr(_num\_bytes:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_)→Optional[bytes][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.read_proc_stderr "Permalink to this definition")
Read `num_bytes` from the running process’ stderr stream.

Parameters
**num_bytes** ([_int_](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) – Number of bytes to read at maximum.

Returns
A string/bytes object.

New in version 1.0.

close_proc_stdin()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.close_proc_stdin "Permalink to this definition")
Close running process’ stdin.

Returns
`None`.

New in version 1.3.

default_encoding()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.default_encoding "Permalink to this definition")
Return a string naming the expected encoding of subprocess streams.

This return value should be suitable for use by encode/decode methods.

New in version 1.0.

send_interrupt(_interrupt:KeyboardInterrupt_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.send_interrupt "Permalink to this definition")
Submit an interrupt signal to the running subprocess.

In almost all implementations, the default behavior is what will be desired: submit `` to the subprocess’ stdin pipe. However, we leave this as a public method in case this default needs to be augmented or replaced.

Parameters
**interrupt** – The locally-sourced `KeyboardInterrupt` causing the method call.

Returns
`None`.

New in version 1.0.

returncode()→Optional[[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.returncode "Permalink to this definition")
Return the numeric return/exit code resulting from command execution.

Returns
[`int`](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)"), if any reasonable return code could be determined, or `None` in corner cases where that was not possible.

New in version 1.0.

stop()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.stop "Permalink to this definition")
Perform final cleanup, if necessary.

This method is called within a `finally` clause inside the main [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") method. Depending on the subclass, it may be a no-op, or it may do things such as close network connections or open files.

Returns
`None`

New in version 1.0.

kill()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.kill "Permalink to this definition")
Forcibly terminate the subprocess.

Typically only used by the timeout functionality.

This is often a “best-effort” attempt, e.g. remote subprocesses often must settle for simply shutting down the local side of the network connection and hoping the remote end eventually gets the message.

_property_ timed_out _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.timed_out "Permalink to this definition")
Returns `True` if the subprocess stopped because it timed out.

New in version 1.3.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_class_ invoke.runners.Local(_context:Context_)[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local "Permalink to this definition")
Execute a command on the local system in a subprocess.

Note

When Invoke itself is executed without a controlling terminal (e.g. when `sys.stdin` lacks a useful `fileno`), it’s not possible to present a handle on our PTY to local subprocesses. In such situations, [`Local`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local "invoke.runners.Local") will fallback to behaving as if `pty=False` (on the theory that degraded execution is better than none at all) as well as printing a warning to stderr.

To disable this behavior, say `fallback=False`.

New in version 1.0.

 __init__ (_context:Context_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.__init__ "Permalink to this definition")
Create a new runner with a handle on some [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context").

Parameters
**context** –

a [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") instance, used to transmit default options and provide access to other contextualized information (e.g. a remote-oriented [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") might want a [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") subclass holding info about hostnames and ports.)

Note

The [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") given to [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") instances **must** contain default config values for the [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") class in question. At a minimum, this means values for each of the default [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") keyword arguments such as `echo` and `warn`.

Raises
[**exceptions.ValueError**](https://docs.python.org/2.7/library/exceptions.html#exceptions.ValueError "(in Python v2.7)") – if not all expected default values are found in `context`.

should_use_pty(_pty:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_, _fallback:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=True_)→[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.should_use_pty "Permalink to this definition")
Should execution attempt to use a pseudo-terminal?

Parameters
*   **pty** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether the user explicitly asked for a pty.

*   **fallback** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – Whether falling back to non-pty execution should be allowed, in situations where `pty=True` but a pty could not be allocated.

New in version 1.0.

read_proc_stdout(_num\_bytes:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_)→Optional[bytes][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.read_proc_stdout "Permalink to this definition")
Read `num_bytes` from the running process’ stdout stream.

Parameters
**num_bytes** ([_int_](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) – Number of bytes to read at maximum.

Returns
A string/bytes object.

New in version 1.0.

read_proc_stderr(_num\_bytes:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_)→Optional[bytes][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.read_proc_stderr "Permalink to this definition")
Read `num_bytes` from the running process’ stderr stream.

Parameters
**num_bytes** ([_int_](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) – Number of bytes to read at maximum.

Returns
A string/bytes object.

New in version 1.0.

close_proc_stdin()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.close_proc_stdin "Permalink to this definition")
Close running process’ stdin.

Returns
`None`.

New in version 1.3.

start(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _shell:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _env:Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.start "Permalink to this definition")
Initiate execution of `command` (via `shell`, with `env`).

Typically this means use of a forked subprocess or requesting start of execution on a remote system.

In most cases, this method will also set subclass-specific member variables used in other methods such as `wait` and/or [`returncode`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.returncode "invoke.runners.Local.returncode").

Parameters
*   **command** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Command string to execute.

*   **shell** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Shell to use when executing `command`.

*   **env** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – Environment dict used to prep shell environment.

New in version 1.0.

kill()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.kill "Permalink to this definition")
Forcibly terminate the subprocess.

Typically only used by the timeout functionality.

This is often a “best-effort” attempt, e.g. remote subprocesses often must settle for simply shutting down the local side of the network connection and hoping the remote end eventually gets the message.

_property_ process_is_finished _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.process_is_finished "Permalink to this definition")
Determine whether our subprocess has terminated.

Note

The implementation of this method should be nonblocking, as it is used within a query/poll loop.

Returns
`True` if the subprocess has finished running, `False` otherwise.

New in version 1.0.

returncode()→Optional[[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.returncode "Permalink to this definition")
Return the numeric return/exit code resulting from command execution.

Returns
[`int`](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)"), if any reasonable return code could be determined, or `None` in corner cases where that was not possible.

New in version 1.0.

stop()→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local.stop "Permalink to this definition")
Perform final cleanup, if necessary.

This method is called within a `finally` clause inside the main `run` method. Depending on the subclass, it may be a no-op, or it may do things such as close network connections or open files.

Returns
`None`

New in version 1.0.

_class_ invoke.runners.Result(_stdout:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _stderr:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _encoding:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _shell:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _env:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _exited:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")=0_, _pty:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_, _hide:Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...]=()_)[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "Permalink to this definition")
A container for information about the result of a command execution.

All params are exposed as attributes of the same name and type.

Parameters
*   **stdout** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The subprocess’ standard output.

*   **stderr** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Same as `stdout` but containing standard error (unless the process was invoked via a pty, in which case it will be empty; see [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run").)

*   **encoding** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The string encoding used by the local shell environment.

*   **command** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The command which was executed.

*   **shell** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The shell binary used for execution.

*   **env** ([_dict_](https://docs.python.org/2.7/library/stdtypes.html#dict "(in Python v2.7)")) – The shell environment used for execution. (Default is the empty dict, `{}`, not `None` as displayed in the signature.)

*   **exited** ([_int_](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) –

An integer representing the subprocess’ exit/return code.

Note

This may be `None` in situations where the subprocess did not run to completion, such as when auto-responding failed or a timeout was reached. 
*   **pty** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) – A boolean describing whether the subprocess was invoked with a pty or not; see [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run").

*   **hide** (_tuple_) –

A tuple of stream names (none, one or both of `('stdout', 'stderr')`) which were hidden from the user when the generating command executed; this is a normalized value derived from the `hide` parameter of [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run").

For example, `run('command', hide='stdout')` will yield a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") where `result.hide == ('stdout',)`; `hide=True` or `hide='both'` results in `result.hide == ('stdout', 'stderr')`; and `hide=False` (the default) generates `result.hide == ()` (the empty tuple.)

Note

[`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") objects’ truth evaluation is equivalent to their [`ok`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.ok "invoke.runners.Result.ok") attribute’s value. Therefore, quick-and-dirty expressions like the following are possible:

if run("some shell command"):
    do_something()
else:
    handle_problem()

However, remember [Zen of Python #2](http://zen-of-python.info/explicit-is-better-than-implicit.html#2).

New in version 1.0.

 __init__ (_stdout:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _stderr:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _encoding:Optional[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]=None_, _command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _shell:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")=''_, _env:Optional[Dict[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),Any]]=None_, _exited:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")=0_, _pty:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")=False_, _hide:Tuple[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),...]=()_)[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.__init__ "Permalink to this definition")_property_ return_code _:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.return_code "Permalink to this definition")
An alias for `.exited`.

New in version 1.0.

 __str__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.__str__ "Permalink to this definition")
Return str(self).

 __repr__ ()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.__repr__ "Permalink to this definition")
Return repr(self).

_property_ ok _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.ok "Permalink to this definition")
A boolean equivalent to `exited == 0`.

New in version 1.0.

_property_ failed _:[bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.failed "Permalink to this definition")
The inverse of `ok`.

I.e., `True` if the program exited with a nonzero return code, and `False` otherwise.

New in version 1.0.

tail(_stream:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _count:[int](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")=10_)→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.tail "Permalink to this definition")
Return the last `count` lines of `stream`, plus leading whitespace.

Parameters
*   **stream** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Name of some captured stream attribute, eg `"stdout"`.

*   **count** ([_int_](https://docs.python.org/2.7/library/functions.html#int "(in Python v2.7)")) – Number of lines to preserve.

New in version 1.3.

 __weakref__ [¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result.__weakref__ "Permalink to this definition")
list of weak references to the object (if defined)

_class_ invoke.runners.Promise(_runner:[invoke.runners.Runner](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner")_)[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "Permalink to this definition")
A promise of some future [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result"), yielded from asynchronous execution.

This class’ primary API member is [`join`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise.join "invoke.runners.Promise.join"); instances may also be used as context managers, which will automatically call [`join`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise.join "invoke.runners.Promise.join") when the block exits. In such cases, the context manager yields `self`.

[`Promise`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise "invoke.runners.Promise") also exposes copies of many [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") attributes, specifically those that derive from [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") kwargs and not the result of command execution. For example, `command` is replicated here, but `stdout` is not.

New in version 1.4.

 __init__ (_runner:[invoke.runners.Runner](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise.__init__ "Permalink to this definition")
Create a new promise.

Parameters
**runner** –

An in-flight [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") instance making this promise.

Must already have started the subprocess and spun up IO threads.

join()→[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Promise.join "Permalink to this definition")
Block until associated subprocess exits, returning/raising the result.

This acts identically to the end of a synchronously executed `run`, namely that:

*   various background threads (such as IO workers) are themselves joined;

*   if the subprocess exited normally, a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") is returned;

*   in any other case (unforeseen exceptions, IO sub-thread [`ThreadException`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ThreadException "invoke.exceptions.ThreadException"), [`Failure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.Failure "invoke.exceptions.Failure"), [`WatcherError`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.WatcherError "invoke.exceptions.WatcherError")) the relevant exception is raised here.

See [`run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") docs, or those of the relevant classes, for further details.

invoke.runners.default_encoding()→[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.default_encoding "Permalink to this definition")
Obtain apparent interpreter-local default text encoding.

Often used as a baseline in situations where we must use SOME encoding for unknown-but-presumably-text bytes, and the user has not specified an override.
