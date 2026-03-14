# Source: https://anyio.readthedocs.io/en/stable/api.html

Title: API reference — AnyIO 0.0.post50 documentation

URL Source: https://anyio.readthedocs.io/en/stable/api.html

Markdown Content:
 AnyIO
latest
stable
3.x
2.x
1.4.0
 
The basics
Creating and managing tasks
Cancellation and timeouts
Using synchronization primitives
Streams
Using typed attributes
Using sockets and streams
Working with threads
Using subprocesses
Working with subinterpreters
Asynchronous file I/O support
Asynchronous Temporary File and Directory
Receiving operating system signals
Context manager mix-in classes
Testing with AnyIO
API reference
Event loop
Asynchronous resources
Typed attributes
Timeouts and cancellation
Task groups
Running code in worker threads
Running code in subinterpreters
Running code in worker processes
Running asynchronous code from other threads
Async file I/O
Temporary files and directories
Context manager mix-in classes
Streams and stream wrappers
Sockets and networking
Subprocesses
Synchronization
Operating system signals
Asynchronous functools
Low level operations
Testing and debugging
Exceptions
Migrating from AnyIO 3 to AnyIO 4
Migrating from AnyIO 2 to AnyIO 3
Why you should be using AnyIO APIs instead of asyncio APIs
Frequently Asked Questions
Getting help
Reporting bugs
Contributing to AnyIO
Version history
 API reference
View page source
API reference
Event loop
anyio.run(func, *args, backend='asyncio', backend_options=None)

Run the given coroutine function in an asynchronous event loop.

The current thread must not be already running an event loop.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], Awaitable[TypeVar(T_Retval)]]) – a coroutine function

args (Unpack[TypeVarTuple]) – positional arguments to func

backend (str) – name of the asynchronous event loop implementation – currently either asyncio or trio

backend_options (dict[str, Any] | None) – keyword arguments to call the backend run() implementation with (documented here)

Return type
:

TypeVar(T_Retval)

Returns
:

the return value of the coroutine function

Raises
:

RuntimeError – if an asynchronous event loop is already running in this thread

LookupError – if the named backend is not found

anyio.get_all_backends()

Return a tuple of the names of all built-in backends.

Return type
:

tuple[str, ...]

anyio.get_available_backends()

Test for the availability of built-in backends.

:return a tuple of the built-in backend names that were successfully imported

Added in version 4.12.

Return type
:

tuple[str, ...]

anyio.get_cancelled_exc_class()

Return the current async library’s cancellation exception class.

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Return type
:

type[BaseException]

asyncanyio.sleep(delay)

Pause the current task for the specified duration.

Parameters
:

delay (float) – the duration, in seconds

Return type
:

None

asyncanyio.sleep_forever()

Pause the current task until it’s cancelled.

This is a shortcut for sleep(math.inf).

Added in version 3.1.

Return type
:

None

asyncanyio.sleep_until(deadline)

Pause the current task until the given time.

Parameters
:

deadline (float) – the absolute time to wake up at (according to the internal monotonic clock of the event loop)

Return type
:

None

Added in version 3.1.

anyio.current_time()

Return the current value of the event loop’s internal clock.

Return type
:

float

Returns
:

the clock value (seconds)

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Asynchronous resources
asyncanyio.aclose_forcefully(resource)

Close an asynchronous resource in a cancelled scope.

Doing this closes the resource without waiting on anything.

Parameters
:

resource (AsyncResource) – the resource to close

Return type
:

None

classanyio.abc.AsyncResource

Bases: object

Abstract base class for all closeable asynchronous resources.

Works as an asynchronous context manager which returns the instance itself on enter, and calls aclose() on exit.

abstractmethod asyncaclose()

Close the resource.

Return type
:

None

Typed attributes
anyio.typed_attribute()

Return a unique object, used to mark typed attributes.

Return type
:

Any

classanyio.TypedAttributeSet

Bases: object

Superclass for typed attribute collections.

Checks that every public attribute of every subclass has a type annotation.

classanyio.TypedAttributeProvider

Bases: object

Base class for classes that wish to provide typed extra attributes.

extra(attribute, default=<object object>)

Return the value of the given typed extra attribute.

Parameters
:

attribute (Any) – the attribute (member of a TypedAttributeSet) to look for

default (object) – the value that should be returned if no value is found for the attribute

Raises
:

TypedAttributeLookupError – if the search failed and no default value was given

Return type
:

object

propertyextra_attributes: Mapping[T_Attr, Callable[[], T_Attr]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

Timeouts and cancellation
anyio.move_on_after(delay, shield=False)

Create a cancel scope with a deadline that expires after the given delay.

Parameters
:

delay (float | None) – maximum allowed time (in seconds) before exiting the context block, or None to disable the timeout

shield (bool) – True to shield the cancel scope from external cancellation

Return type
:

CancelScope

Returns
:

a cancel scope

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

anyio.fail_after(delay, shield=False)

Create a context manager which raises a TimeoutError if does not finish in time.

Parameters
:

delay (float | None) – maximum allowed time (in seconds) before raising the exception, or None to disable the timeout

shield (bool) – True to shield the cancel scope from external cancellation

Returns
:

a context manager that yields a cancel scope

Return type
:

ContextManager[CancelScope]

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

anyio.current_effective_deadline()

Return the nearest deadline among all the cancel scopes effective for the current task.

Returns
:

a clock value from the event loop’s internal clock (or float('inf') if there is no deadline in effect, or float('-inf') if the current scope has been cancelled)

Return type
:

float

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

classanyio.CancelScope(*, deadline: float = inf, shield: bool = False)

Bases: object

Wraps a unit of work that can be made separately cancellable.

Parameters
:

deadline – The time (clock value) when this scope is cancelled automatically

shield – True to shield the cancel scope from external cancellation

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

cancel(reason=None)

Cancel this scope immediately.

Parameters
:

reason (str | None) – a message describing the reason for the cancellation

Return type
:

None

propertycancel_called: bool

True if cancel() has been called.

 
propertycancelled_caught: bool

True if this scope suppressed a cancellation exception it itself raised.

This is typically used to check if any work was interrupted, or to see if the scope was cancelled due to its deadline being reached. The value will, however, only be True if the cancellation was triggered by the scope itself (and not an outer scope).

 
propertydeadline: float

The time (clock value) when this scope is cancelled automatically.

Will be float('inf') if no timeout has been set.

 
propertyshield: bool

True if this scope is shielded from external cancellation.

While a scope is shielded, it will not receive cancellations from outside.

Task groups
anyio.create_task_group()

Create a task group.

Return type
:

TaskGroup

Returns
:

a task group

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

classanyio.abc.TaskGroup

Bases: object

Groups several asynchronous tasks together.

Variables
:

cancel_scope (CancelScope) – the cancel scope inherited by all child tasks

Note

On asyncio, support for eager task factories is considered to be experimental. In particular, they don’t follow the usual semantics of new tasks being scheduled on the next iteration of the event loop, and may thus cause unexpected behavior in code that wasn’t written with such semantics in mind.

abstractmethod asyncstart(func, *args, name=None)

Start a new task and wait until it signals for readiness.

The target callable must accept a keyword argument task_status (of type TaskStatus). Awaiting on this method will return whatever was passed to task_status.started() (None by default).

Note

The TaskStatus class is generic, and the type argument should indicate the type of the value that will be passed to task_status.started().

Parameters
:

func (Callable[..., Awaitable[Any]]) – a coroutine function that accepts the task_status keyword argument

args (object) – positional arguments to call the function with

name (object) – an optional name for the task, for introspection and debugging

Return type
:

Any

Returns
:

the value passed to task_status.started()

Raises
:

RuntimeError – if the task finishes without calling task_status.started()

See also

Starting and initializing tasks

Added in version 3.0.

abstractmethodstart_soon(func, *args, name=None)

Start a new task in this task group.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], Awaitable[Any]]) – a coroutine function

args (Unpack[TypeVarTuple]) – positional arguments to call the function with

name (object) – name of the task, for the purposes of introspection and debugging

Return type
:

None

Added in version 3.0.

classanyio.abc.TaskStatus(*args, **kwargs)

Bases: Protocol[T_contra]

started(value=None)

Signal that the task has started.

Parameters
:

value (Optional[TypeVar(T_contra, contravariant=True)]) – object passed back to the starter of the task

Return type
:

None

Running code in worker threads
asyncanyio.to_thread.run_sync(func, *args, abandon_on_cancel=False, cancellable=None, limiter=None)

Call the given function with the given arguments in a worker thread.

If the cancellable option is enabled and the task waiting for its completion is cancelled, the thread will still run its course but its return value (or any raised exception) will be ignored.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], TypeVar(T_Retval)]) – a callable

args (Unpack[TypeVarTuple]) – positional arguments for the callable

abandon_on_cancel (bool) – True to abandon the thread (leaving it to run unchecked on own) if the host task is cancelled, False to ignore cancellations in the host task until the operation has completed in the worker thread

cancellable (bool | None) – deprecated alias of abandon_on_cancel; will override abandon_on_cancel if both parameters are passed

limiter (CapacityLimiter | None) – capacity limiter to use to limit the total amount of threads running (if omitted, the default limiter is used)

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Return type
:

TypeVar(T_Retval)

Returns
:

an awaitable that yields the return value of the function.

anyio.to_thread.current_default_thread_limiter()

Return the capacity limiter that is used by default to limit the number of concurrent threads.

Return type
:

CapacityLimiter

Returns
:

a capacity limiter object

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Running code in subinterpreters
asyncanyio.to_interpreter.run_sync(func, *args, limiter=None)

Call the given function with the given arguments in a subinterpreter.

Warning

On Python 3.13, the concurrent.interpreters module was not yet available, so the code path for that Python version relies on an undocumented, private API. As such, it is recommended to not rely on this function for anything mission-critical on Python 3.13.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], TypeVar(T_Retval)]) – a callable

args (Unpack[TypeVarTuple]) – the positional arguments for the callable

limiter (CapacityLimiter | None) – capacity limiter to use to limit the total number of subinterpreters running (if omitted, the default limiter is used)

Return type
:

TypeVar(T_Retval)

Returns
:

the result of the call

Raises
:

BrokenWorkerInterpreter – if there’s an internal error in a subinterpreter

anyio.to_interpreter.current_default_interpreter_limiter()

Return the capacity limiter used by default to limit the number of concurrently running subinterpreters.

Defaults to the number of CPU cores.

Return type
:

CapacityLimiter

Returns
:

a capacity limiter object

Running code in worker processes
asyncanyio.to_process.run_sync(func, *args, cancellable=False, limiter=None)

Call the given function with the given arguments in a worker process.

If the cancellable option is enabled and the task waiting for its completion is cancelled, the worker process running it will be abruptly terminated using SIGKILL (or terminateProcess() on Windows).

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], TypeVar(T_Retval)]) – a callable

args (Unpack[TypeVarTuple]) – positional arguments for the callable

cancellable (bool) – True to allow cancellation of the operation while it’s running

limiter (CapacityLimiter | None) – capacity limiter to use to limit the total amount of processes running (if omitted, the default limiter is used)

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Return type
:

TypeVar(T_Retval)

Returns
:

an awaitable that yields the return value of the function.

anyio.to_process.current_default_process_limiter()

Return the capacity limiter that is used by default to limit the number of worker processes.

Return type
:

CapacityLimiter

Returns
:

a capacity limiter object

Running asynchronous code from other threads
anyio.from_thread.run(func, *args, token=None)

Call a coroutine function from a worker thread.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], Awaitable[TypeVar(T_Retval)]]) – a coroutine function

args (Unpack[TypeVarTuple]) – positional arguments for the callable

token (EventLoopToken | None) – an event loop token to use to get back to the event loop thread (required if calling this function from outside an AnyIO worker thread)

Return type
:

TypeVar(T_Retval)

Returns
:

the return value of the coroutine function

Raises
:

MissingTokenError – if no token was provided and called from outside an AnyIO worker thread

RunFinishedError – if the event loop tied to token is no longer running

Changed in version 4.11.0: Added the token parameter.

anyio.from_thread.run_sync(func, *args, token=None)

Call a function in the event loop thread from a worker thread.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], TypeVar(T_Retval)]) – a callable

args (Unpack[TypeVarTuple]) – positional arguments for the callable

token (EventLoopToken | None) – an event loop token to use to get back to the event loop thread (required if calling this function from outside an AnyIO worker thread)

Return type
:

TypeVar(T_Retval)

Returns
:

the return value of the callable

Raises
:

MissingTokenError – if no token was provided and called from outside an AnyIO worker thread

RunFinishedError – if the event loop tied to token is no longer running

Changed in version 4.11.0: Added the token parameter.

anyio.from_thread.check_cancelled()

Check if the cancel scope of the host task’s running the current worker thread has been cancelled.

If the host task’s current cancel scope has indeed been cancelled, the backend-specific cancellation exception will be raised.

Raises
:

RuntimeError – if the current thread was not spawned by to_thread.run_sync()

Return type
:

None

anyio.from_thread.start_blocking_portal(backend='asyncio', backend_options=None, *, name=None)

Start a new event loop in a new thread and run a blocking portal in its main task.

The parameters are the same as for run().

Parameters
:

backend (str) – name of the backend

backend_options (dict[str, Any] | None) – backend options

name (str | None) – name of the thread

Return type
:

Generator[BlockingPortal, Any, None]

Returns
:

a context manager that yields a blocking portal

Changed in version 3.0: Usage as a context manager is now required.

classanyio.from_thread.BlockingPortal

Bases: object

An object that lets external threads run code in an asynchronous event loop.

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

call(func, *args)

Call the given function in the event loop thread.

If the callable returns a coroutine object, it is awaited on.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], Union[Awaitable[TypeVar(T_Retval)], TypeVar(T_Retval)]]) – any callable

Raises
:

RuntimeError – if the portal is not running or if this method is called from within the event loop thread

Return type
:

TypeVar(T_Retval)

asyncsleep_until_stopped()

Sleep until stop() is called.

Return type
:

None

start_task(func, *args, name=None)

Start a task in the portal’s task group and wait until it signals for readiness.

This method works the same way as abc.TaskGroup.start().

Parameters
:

func (Callable[..., Awaitable[TypeVar(T_Retval)]]) – the target function

args (object) – positional arguments passed to func

name (object) – name of the task (will be coerced to a string if not None)

Returns
:

a tuple of (future, task_status_value) where the task_status_value is the value passed to task_status.started() from within the target function

Return type
:

tuple[concurrent.futures.Future[T_Retval], Any]

Added in version 3.0.

start_task_soon(func, *args, name=None)

Start a task in the portal’s task group.

The task will be run inside a cancel scope which can be cancelled by cancelling the returned future.

Parameters
:

func (Callable[[Unpack[TypeVarTuple]], Union[Awaitable[TypeVar(T_Retval)], TypeVar(T_Retval)]]) – the target function

args (Unpack[TypeVarTuple]) – positional arguments passed to func

name (object) – name of the task (will be coerced to a string if not None)

Returns
:

a future that resolves with the return value of the callable if the task completes successfully, or with the exception raised in the task

Raises
:

RuntimeError – if the portal is not running or if this method is called from within the event loop thread

Return type
:

concurrent.futures.Future[T_Retval]

Added in version 3.0.

asyncstop(cancel_remaining=False)

Signal the portal to shut down.

This marks the portal as no longer accepting new calls and exits from sleep_until_stopped().

Parameters
:

cancel_remaining (bool) – True to cancel all the remaining tasks, False to let them finish before returning

Return type
:

None

wrap_async_context_manager(cm)

Wrap an async context manager as a synchronous context manager via this portal.

Spawns a task that will call both __aenter__() and __aexit__(), stopping in the middle until the synchronous context manager exits.

Parameters
:

cm (AbstractAsyncContextManager[TypeVar(T_co, covariant=True)]) – an asynchronous context manager

Return type
:

AbstractContextManager[TypeVar(T_co, covariant=True)]

Returns
:

a synchronous context manager

Added in version 2.1.

classanyio.from_thread.BlockingPortalProvider(backend='asyncio', backend_options=None)

Bases: object

A manager for a blocking portal. Used as a context manager. The first thread to enter this context manager causes a blocking portal to be started with the specific parameters, and the last thread to exit causes the portal to be shut down. Thus, there will be exactly one blocking portal running in this context as long as at least one thread has entered this context manager.

The parameters are the same as for run().

Parameters
:

backend (str) – name of the backend

backend_options (dict[str, Any] | None) – backend options

Added in version 4.4.

Async file I/O
asyncanyio.open_file(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Open a file asynchronously.

The arguments are exactly the same as for the builtin open().

Return type
:

AsyncFile[Any]

Returns
:

an asynchronous file object

anyio.wrap_file(file)

Wrap an existing file as an asynchronous file.

Parameters
:

file (IO[AnyStr]) – an existing file-like object

Return type
:

AsyncFile[AnyStr]

Returns
:

an asynchronous file object

classanyio.AsyncFile(fp)

Bases: AsyncResource, Generic

An asynchronous file object.

This class wraps a standard file object and provides async friendly versions of the following blocking methods (where available on the original file object):

read

read1

readline

readlines

readinto

readinto1

write

writelines

truncate

seek

tell

flush

All other methods are directly passed through.

This class supports the asynchronous context manager protocol which closes the underlying file at the end of the context block.

This class also supports asynchronous iteration:

async with await open_file(...) as f:
    async for line in f:
        print(line)

asyncaclose()

Close the resource.

Return type
:

None

propertywrapped: IO

The wrapped file object.

classanyio.Path(*args)

Bases: object

An asynchronous version of pathlib.Path.

This class cannot be substituted for pathlib.Path or pathlib.PurePath, but it is compatible with the os.PathLike interface.

It implements the Python 3.10 version of pathlib.Path interface, except for the deprecated link_to() method.

Some methods may be unavailable or have limited functionality, based on the Python version:

copy() (available on Python 3.14 or later)

copy_into() (available on Python 3.14 or later)

from_uri() (available on Python 3.13 or later)

full_match() (available on Python 3.13 or later)

info (available on Python 3.14 or later)

is_junction() (available on Python 3.12 or later)

match() (the case_sensitive parameter is only available on Python 3.13 or later)

move() (available on Python 3.14 or later)

move_into() (available on Python 3.14 or later)

relative_to() (the walk_up parameter is only available on Python 3.12 or later)

walk() (available on Python 3.12 or later)

Any methods that do disk I/O need to be awaited on. These methods are:

absolute()

chmod()

cwd()

exists()

expanduser()

group()

hardlink_to()

home()

is_block_device()

is_char_device()

is_dir()

is_fifo()

is_file()

is_junction()

is_mount()

is_socket()

is_symlink()

lchmod()

lstat()

mkdir()

open()

owner()

read_bytes()

read_text()

readlink()

rename()

replace()

resolve()

rmdir()

samefile()

stat()

symlink_to()

touch()

unlink()

walk()

write_bytes()

write_text()

Additionally, the following methods return an async iterator yielding Path objects:

glob()

iterdir()

rglob()

Temporary files and directories
asyncanyio.mkstemp(suffix=None, prefix=None, dir=None, text=False)

Asynchronously create a temporary file and return an OS-level handle and the file name.

This function wraps tempfile.mkstemp and executes it in a background thread.

Parameters
:

suffix (Optional[AnyStr]) – Suffix to be added to the file name.

prefix (Optional[AnyStr]) – Prefix to be added to the file name.

dir (Optional[AnyStr]) – Directory in which the temporary file is created.

text (bool) – Whether the file is opened in text mode.

Return type
:

tuple[int, str | bytes]

Returns
:

A tuple containing the file descriptor and the file name.

asyncanyio.mkdtemp(suffix=None, prefix=None, dir=None)

Asynchronously create a temporary directory and return its path.

This function wraps tempfile.mkdtemp and executes it in a background thread.

Parameters
:

suffix (Optional[AnyStr]) – Suffix to be added to the directory name.

prefix (Optional[AnyStr]) – Prefix to be added to the directory name.

dir (Optional[AnyStr]) – Parent directory where the temporary directory is created.

Return type
:

str | bytes

Returns
:

The path of the created temporary directory.

asyncanyio.gettempdir()

Asynchronously return the name of the directory used for temporary files.

This function wraps tempfile.gettempdir and executes it in a background thread.

Return type
:

str

Returns
:

The path of the temporary directory as a string.

asyncanyio.gettempdirb()

Asynchronously return the name of the directory used for temporary files in bytes.

This function wraps tempfile.gettempdirb and executes it in a background thread.

Return type
:

bytes

Returns
:

The path of the temporary directory as bytes.

classanyio.TemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

Bases: Generic

An asynchronous temporary file that is automatically created and cleaned up.

This class provides an asynchronous context manager interface to a temporary file. The file is created using Python’s standard tempfile.TemporaryFile function in a background thread, and is wrapped as an asynchronous file using AsyncFile.

Parameters
:

mode (OpenTextMode | OpenBinaryMode) – The mode in which the file is opened. Defaults to “w+b”.

buffering (int) – The buffering policy (-1 means the default buffering).

encoding (str | None) – The encoding used to decode or encode the file. Only applicable in text mode.

newline (str | None) – Controls how universal newlines mode works (only applicable in text mode).

suffix (str | None) – The suffix for the temporary file name.

prefix (str | None) – The prefix for the temporary file name.

dir (str | None) – The directory in which the temporary file is created.

errors (str | None) – The error handling scheme used for encoding/decoding errors.

classanyio.NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None, delete_on_close=True)

Bases: Generic

An asynchronous named temporary file that is automatically created and cleaned up.

This class provides an asynchronous context manager for a temporary file with a visible name in the file system. It uses Python’s standard NamedTemporaryFile() function and wraps the file object with AsyncFile for asynchronous operations.

Parameters
:

mode (OpenBinaryMode | OpenTextMode) – The mode in which the file is opened. Defaults to “w+b”.

buffering (int) – The buffering policy (-1 means the default buffering).

encoding (str | None) – The encoding used to decode or encode the file. Only applicable in text mode.

newline (str | None) – Controls how universal newlines mode works (only applicable in text mode).

suffix (str | None) – The suffix for the temporary file name.

prefix (str | None) – The prefix for the temporary file name.

dir (str | None) – The directory in which the temporary file is created.

delete (bool) – Whether to delete the file when it is closed.

errors (str | None) – The error handling scheme used for encoding/decoding errors.

delete_on_close (bool) – (Python 3.12+) Whether to delete the file on close.

classanyio.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)

Bases: AsyncFile

An asynchronous spooled temporary file that starts in memory and is spooled to disk.

This class provides an asynchronous interface to a spooled temporary file, much like Python’s standard SpooledTemporaryFile. It supports asynchronous write operations and provides a method to force a rollover to disk.

Parameters
:

max_size (int) – Maximum size in bytes before the file is rolled over to disk.

mode (OpenBinaryMode | OpenTextMode) – The mode in which the file is opened. Defaults to “w+b”.

buffering (int) – The buffering policy (-1 means the default buffering).

encoding (str | None) – The encoding used to decode or encode the file (text mode only).

newline (str | None) – Controls how universal newlines mode works (text mode only).

suffix (str | None) – The suffix for the temporary file name.

prefix (str | None) – The prefix for the temporary file name.

dir (str | None) – The directory in which the temporary file is created.

errors (str | None) – The error handling scheme used for encoding/decoding errors.

asyncaclose()

Close the resource.

Return type
:

None

asyncwrite(b)

Asynchronously write data to the spooled temporary file.

If the file has not yet been rolled over, the data is written synchronously, and a rollover is triggered if the size exceeds the maximum size.

Parameters
:

s – The data to write.

Return type
:

int

Returns
:

The number of bytes written.

Raises
:

RuntimeError – If the underlying file is not initialized.

asyncwritelines(lines)

Asynchronously write a list of lines to the spooled temporary file.

If the file has not yet been rolled over, the lines are written synchronously, and a rollover is triggered if the size exceeds the maximum size.

Parameters
:

lines (Iterable[str] | Iterable[ReadableBuffer]) – An iterable of lines to write.

Raises
:

RuntimeError – If the underlying file is not initialized.

Return type
:

None

classanyio.TemporaryDirectory(suffix=None, prefix=None, dir=None, *, ignore_cleanup_errors=False, delete=True)

Bases: Generic

An asynchronous temporary directory that is created and cleaned up automatically.

This class provides an asynchronous context manager for creating a temporary directory. It wraps Python’s standard TemporaryDirectory to perform directory creation and cleanup operations in a background thread.

Parameters
:

suffix (Optional[AnyStr]) – Suffix to be added to the temporary directory name.

prefix (Optional[AnyStr]) – Prefix to be added to the temporary directory name.

dir (Optional[AnyStr]) – The parent directory where the temporary directory is created.

ignore_cleanup_errors (bool) – Whether to ignore errors during cleanup (Python 3.10+).

delete (bool) – Whether to delete the directory upon closing (Python 3.12+).

Context manager mix-in classes
classanyio.ContextManagerMixin

Bases: object

Mixin class providing context manager functionality via a generator-based implementation.

This class allows you to implement a context manager via __contextmanager__() which should return a generator. The mechanics are meant to mirror those of @contextmanager.

Note

Classes using this mix-in are not reentrant as context managers, meaning that once you enter it, you can’t re-enter before first exiting it.

See also

Context manager mix-in classes

abstractmethod__contextmanager__()

Implement your context manager logic here.

This method must be decorated with @contextmanager.

Note

Remember that the yield will raise any exception raised in the enclosed context block, so use a finally: block to clean up resources!

Return type
:

AbstractContextManager[object, bool | None]

Returns
:

a context manager object

classanyio.AsyncContextManagerMixin

Bases: object

Mixin class providing async context manager functionality via a generator-based implementation.

This class allows you to implement a context manager via __asynccontextmanager__(). The mechanics are meant to mirror those of @asynccontextmanager.

Note

Classes using this mix-in are not reentrant as context managers, meaning that once you enter it, you can’t re-enter before first exiting it.

See also

Context manager mix-in classes

abstractmethod__asynccontextmanager__()

Implement your async context manager logic here.

This method must be decorated with @asynccontextmanager.

Note

Remember that the yield will raise any exception raised in the enclosed context block, so use a finally: block to clean up resources!

Return type
:

AbstractAsyncContextManager[object, bool | None]

Returns
:

an async context manager object

Streams and stream wrappers
anyio.create_memory_object_stream(max_buffer_size: float = 0, item_type: object = None)→ tuple[MemoryObjectSendStream[T_Item], MemoryObjectReceiveStream[T_Item]]

Create a memory object stream.

The stream’s item type can be annotated like create_memory_object_stream[T_Item]().

Parameters
:

max_buffer_size – number of items held in the buffer until send() starts blocking

item_type –

old way of marking the streams with the right generic type for static typing (does nothing on AnyIO 4)

Deprecated since version 4.0: Use create_memory_object_stream[YourItemType](...) instead.

Returns
:

a tuple of (send stream, receive stream)

classanyio.abc.UnreliableObjectReceiveStream

Bases: Generic[T_co], AsyncResource, TypedAttributeProvider

An interface for receiving objects.

This interface makes no guarantees that the received messages arrive in the order in which they were sent, or that no messages are missed.

Asynchronously iterating over objects of this type will yield objects matching the given type parameter.

abstractmethod asyncreceive()

Receive the next item.

Raises
:

ClosedResourceError – if the receive stream has been explicitly closed

EndOfStream – if this stream has been closed from the other end

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

TypeVar(T_co, covariant=True)

classanyio.abc.UnreliableObjectSendStream

Bases: Generic[T_contra], AsyncResource, TypedAttributeProvider

An interface for sending objects.

This interface makes no guarantees that the messages sent will reach the recipient(s) in the same order in which they were sent, or at all.

abstractmethod asyncsend(item)

Send an item to the peer(s).

Parameters
:

item (TypeVar(T_contra, contravariant=True)) – the item to send

Raises
:

ClosedResourceError – if the send stream has been explicitly closed

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

None

classanyio.abc.UnreliableObjectStream

Bases: UnreliableObjectReceiveStream[T_Item], UnreliableObjectSendStream[T_Item]

A bidirectional message stream which does not guarantee the order or reliability of message delivery.

classanyio.abc.ObjectReceiveStream

Bases: UnreliableObjectReceiveStream[T_co]

A receive message stream which guarantees that messages are received in the same order in which they were sent, and that no messages are missed.

classanyio.abc.ObjectSendStream

Bases: UnreliableObjectSendStream[T_contra]

A send message stream which guarantees that messages are delivered in the same order in which they were sent, without missing any messages in the middle.

classanyio.abc.ObjectStream

Bases: ObjectReceiveStream[T_Item], ObjectSendStream[T_Item], UnreliableObjectStream[T_Item]

A bidirectional message stream which guarantees the order and reliability of message delivery.

abstractmethod asyncsend_eof()

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does nothing on successive calls).

Return type
:

None

classanyio.abc.ByteReceiveStream

Bases: AsyncResource, TypedAttributeProvider

An interface for receiving bytes from a single peer.

Iterating this byte stream will yield a byte string of arbitrary length, but no more than 65536 bytes.

abstractmethod asyncreceive(max_bytes=65536)

Receive at most max_bytes bytes from the peer.

Note

Implementers of this interface should not return an empty bytes object, and users should ignore them.

Parameters
:

max_bytes (int) – maximum number of bytes to receive

Return type
:

bytes

Returns
:

the received bytes

Raises
:

EndOfStream – if this stream has been closed from the other end

classanyio.abc.ByteSendStream

Bases: AsyncResource, TypedAttributeProvider

An interface for sending bytes to a single peer.

abstractmethod asyncsend(item)

Send the given bytes to the peer.

Parameters
:

item (bytes) – the bytes to send

Return type
:

None

classanyio.abc.ByteStream

Bases: ByteReceiveStream, ByteSendStream

A bidirectional byte stream.

abstractmethod asyncsend_eof()

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does nothing on successive calls).

Return type
:

None

classanyio.abc.Listener

Bases: Generic[T_co], AsyncResource, TypedAttributeProvider

An interface for objects that let you accept incoming connections.

abstractmethod asyncserve(handler, task_group=None)

Accept incoming connections as they come in and start tasks to handle them.

Parameters
:

handler (Callable[[TypeVar(T_co, covariant=True)], Any]) – a callable that will be used to handle each accepted connection

task_group (TaskGroup | None) – the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task group will be created)

Return type
:

None

classanyio.abc.ObjectStreamConnectable

Bases: Generic[T_co]

abstractmethod asyncconnect()

Connect to the remote endpoint.

Return type
:

ObjectStream[TypeVar(T_co, covariant=True)]

Returns
:

an object stream connected to the remote end

Raises
:

ConnectionFailed – if the connection fails

classanyio.abc.ByteStreamConnectable

Bases: object

abstractmethod asyncconnect()

Connect to the remote endpoint.

Return type
:

ByteStream

Returns
:

a bytestream connected to the remote end

Raises
:

ConnectionFailed – if the connection fails

anyio.abc.AnyUnreliableByteReceiveStream

alias of UnreliableObjectReceiveStream[bytes] | ByteReceiveStream

anyio.abc.AnyUnreliableByteSendStream

alias of UnreliableObjectSendStream[bytes] | ByteSendStream

anyio.abc.AnyUnreliableByteStream

alias of UnreliableObjectStream[bytes] | ByteStream

anyio.abc.AnyByteReceiveStream

alias of ObjectReceiveStream[bytes] | ByteReceiveStream

anyio.abc.AnyByteSendStream

alias of ObjectSendStream[bytes] | ByteSendStream

anyio.abc.AnyByteStream

alias of ObjectStream[bytes] | ByteStream

anyio.abc.AnyByteStreamConnectable

alias of ObjectStreamConnectable[bytes] | ByteStreamConnectable

classanyio.streams.buffered.BufferedByteReceiveStream(receive_stream)

Bases: ByteReceiveStream

Wraps any bytes-based receive stream and uses a buffer to provide sophisticated receiving capabilities in the form of a byte stream.

asyncaclose()

Close the resource.

Return type
:

None

propertybuffer: bytes

The bytes currently in the buffer.

 
propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

feed_data(data, /)

Append data directly into the buffer.

Any data in the buffer will be consumed by receive operations before receiving anything from the wrapped stream.

Parameters
:

data (Iterable[SupportsIndex]) – the data to append to the buffer (can be bytes or anything else that supports __index__())

Return type
:

None

asyncreceive(max_bytes=65536)

Receive at most max_bytes bytes from the peer.

Note

Implementers of this interface should not return an empty bytes object, and users should ignore them.

Parameters
:

max_bytes (int) – maximum number of bytes to receive

Return type
:

bytes

Returns
:

the received bytes

Raises
:

EndOfStream – if this stream has been closed from the other end

asyncreceive_exactly(nbytes)

Read exactly the given amount of bytes from the stream.

Parameters
:

nbytes (int) – the number of bytes to read

Return type
:

bytes

Returns
:

the bytes read

Raises
:

IncompleteRead – if the stream was closed before the requested amount of bytes could be read from the stream

asyncreceive_until(delimiter, max_bytes)

Read from the stream until the delimiter is found or max_bytes have been read.

Parameters
:

delimiter (bytes) – the marker to look for in the stream

max_bytes (int) – maximum number of bytes that will be read before raising DelimiterNotFound

Return type
:

bytes

Returns
:

the bytes read (not including the delimiter)

Raises
:

IncompleteRead – if the stream was closed before the delimiter was found

DelimiterNotFound – if the delimiter is not found within the bytes read up to the maximum allowed

classanyio.streams.buffered.BufferedByteStream(stream)

Bases: BufferedByteReceiveStream, ByteStream

A full-duplex variant of BufferedByteReceiveStream. All writes are passed through to the wrapped stream as-is.

asyncsend(item)

Send the given bytes to the peer.

Parameters
:

item (bytes) – the bytes to send

Return type
:

None

asyncsend_eof()

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does nothing on successive calls).

Return type
:

None

classanyio.streams.file.FileStreamAttribute

Bases: TypedAttributeSet

file: BinaryIO= <object object>

the open file descriptor

fileno: int= <object object>

the file number, if available (file must be a real file or a TTY)

path: Path= <object object>

the path of the file on the file system, if available (file must be a real file)

classanyio.streams.file.FileReadStream(file)

Bases: _BaseFileStream, ByteReceiveStream

A byte stream that reads from a file in the file system.

Parameters
:

file (BinaryIO) – a file that has been opened for reading in binary mode

Added in version 3.0.

async classmethodfrom_path(path)

Create a file read stream by opening the given file.

Parameters
:

path (str | PathLike[str]) – path of the file to read from

Return type
:

FileReadStream

asyncreceive(max_bytes=65536)

Receive at most max_bytes bytes from the peer.

Note

Implementers of this interface should not return an empty bytes object, and users should ignore them.

Parameters
:

max_bytes (int) – maximum number of bytes to receive

Return type
:

bytes

Returns
:

the received bytes

Raises
:

EndOfStream – if this stream has been closed from the other end

asyncseek(position, whence=0)

Seek the file to the given position.

See also

io.IOBase.seek()

Note

Not all file descriptors are seekable.

Parameters
:

position (int) – position to seek the file to

whence (int) – controls how position is interpreted

Return type
:

int

Returns
:

the new absolute position

Raises
:

OSError – if the file is not seekable

asynctell()

Return the current stream position.

Note

Not all file descriptors are seekable.

Return type
:

int

Returns
:

the current absolute position

Raises
:

OSError – if the file is not seekable

classanyio.streams.file.FileWriteStream(file)

Bases: _BaseFileStream, ByteSendStream

A byte stream that writes to a file in the file system.

Parameters
:

file (BinaryIO) – a file that has been opened for writing in binary mode

Added in version 3.0.

async classmethodfrom_path(path, append=False)

Create a file write stream by opening the given file for writing.

Parameters
:

path (str | PathLike[str]) – path of the file to write to

append (bool) – if True, open the file for appending; if False, any existing file at the given path will be truncated

Return type
:

FileWriteStream

asyncsend(item)

Send the given bytes to the peer.

Parameters
:

item (bytes) – the bytes to send

Return type
:

None

classanyio.streams.memory.MemoryObjectReceiveStream(_state)

Bases: Generic[T_co], ObjectReceiveStream[T_co]

asyncaclose()

Close the resource.

Return type
:

None

clone()

Create a clone of this receive stream.

Each clone can be closed separately. Only when all clones have been closed will the receiving end of the memory stream be considered closed by the sending ends.

Return type
:

MemoryObjectReceiveStream[TypeVar(T_co, covariant=True)]

Returns
:

the cloned stream

close()

Close the stream.

This works the exact same way as aclose(), but is provided as a special case for the benefit of synchronous callbacks.

Return type
:

None

asyncreceive()

Receive the next item.

Raises
:

ClosedResourceError – if the receive stream has been explicitly closed

EndOfStream – if this stream has been closed from the other end

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

TypeVar(T_co, covariant=True)

receive_nowait()

Receive the next item if it can be done without waiting.

Return type
:

TypeVar(T_co, covariant=True)

Returns
:

the received item

Raises
:

ClosedResourceError – if this send stream has been closed

EndOfStream – if the buffer is empty and this stream has been closed from the sending end

WouldBlock – if there are no items in the buffer and no tasks waiting to send

statistics()

Return statistics about the current state of this stream.

Added in version 3.0.

Return type
:

MemoryObjectStreamStatistics

classanyio.streams.memory.MemoryObjectSendStream(_state)

Bases: Generic[T_contra], ObjectSendStream[T_contra]

asyncaclose()

Close the resource.

Return type
:

None

clone()

Create a clone of this send stream.

Each clone can be closed separately. Only when all clones have been closed will the sending end of the memory stream be considered closed by the receiving ends.

Return type
:

MemoryObjectSendStream[TypeVar(T_contra, contravariant=True)]

Returns
:

the cloned stream

close()

Close the stream.

This works the exact same way as aclose(), but is provided as a special case for the benefit of synchronous callbacks.

Return type
:

None

asyncsend(item)

Send an item to the stream.

If the buffer is full, this method blocks until there is again room in the buffer or the item can be sent directly to a receiver.

Parameters
:

item (TypeVar(T_contra, contravariant=True)) – the item to send

Raises
:

ClosedResourceError – if this send stream has been closed

BrokenResourceError – if the stream has been closed from the receiving end

Return type
:

None

send_nowait(item)

Send an item immediately if it can be done without waiting.

Parameters
:

item (TypeVar(T_contra, contravariant=True)) – the item to send

Raises
:

ClosedResourceError – if this send stream has been closed

BrokenResourceError – if the stream has been closed from the receiving end

WouldBlock – if the buffer is full and there are no tasks waiting to receive

Return type
:

None

statistics()

Return statistics about the current state of this stream.

Added in version 3.0.

Return type
:

MemoryObjectStreamStatistics

classanyio.streams.memory.MemoryObjectStreamStatistics(current_buffer_used, max_buffer_size, open_send_streams, open_receive_streams, tasks_waiting_send, tasks_waiting_receive)

Bases: NamedTuple

current_buffer_used: int

number of items stored in the buffer

max_buffer_size: float

maximum number of items that can be stored on this stream (or math.inf)

open_receive_streams: int

number of unclosed clones of the receive stream

open_send_streams: int

number of unclosed clones of the send stream

tasks_waiting_receive: int

number of tasks blocked on MemoryObjectReceiveStream.receive()

tasks_waiting_send: int

number of tasks blocked on MemoryObjectSendStream.send()

classanyio.streams.stapled.MultiListener(listeners)

Bases: Generic[T_Stream], Listener[T_Stream]

Combines multiple listeners into one, serving connections from all of them at once.

Any MultiListeners in the given collection of listeners will have their listeners moved into this one.

Extra attributes are provided from each listener, with each successive listener overriding any conflicting attributes from the previous one.

Parameters
:

listeners (Sequence[Listener[T_Stream]]) – listeners to serve

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

asyncserve(handler, task_group=None)

Accept incoming connections as they come in and start tasks to handle them.

Parameters
:

handler (Callable[[TypeVar(T_Stream)], Any]) – a callable that will be used to handle each accepted connection

task_group (TaskGroup | None) – the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task group will be created)

Return type
:

None

classanyio.streams.stapled.StapledByteStream(send_stream, receive_stream)

Bases: ByteStream

Combines two byte streams into a single, bidirectional byte stream.

Extra attributes will be provided from both streams, with the receive stream providing the values in case of a conflict.

Parameters
:

send_stream (ByteSendStream) – the sending byte stream

receive_stream (ByteReceiveStream) – the receiving byte stream

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

asyncreceive(max_bytes=65536)

Receive at most max_bytes bytes from the peer.

Note

Implementers of this interface should not return an empty bytes object, and users should ignore them.

Parameters
:

max_bytes (int) – maximum number of bytes to receive

Return type
:

bytes

Returns
:

the received bytes

Raises
:

EndOfStream – if this stream has been closed from the other end

asyncsend(item)

Send the given bytes to the peer.

Parameters
:

item (bytes) – the bytes to send

Return type
:

None

asyncsend_eof()

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does nothing on successive calls).

Return type
:

None

classanyio.streams.stapled.StapledObjectStream(send_stream, receive_stream)

Bases: Generic[T_Item], ObjectStream[T_Item]

Combines two object streams into a single, bidirectional object stream.

Extra attributes will be provided from both streams, with the receive stream providing the values in case of a conflict.

Parameters
:

send_stream (ObjectSendStream) – the sending object stream

receive_stream (ObjectReceiveStream) – the receiving object stream

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

asyncreceive()

Receive the next item.

Raises
:

ClosedResourceError – if the receive stream has been explicitly closed

EndOfStream – if this stream has been closed from the other end

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

TypeVar(T_Item)

asyncsend(item)

Send an item to the peer(s).

Parameters
:

item (TypeVar(T_Item)) – the item to send

Raises
:

ClosedResourceError – if the send stream has been explicitly closed

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

None

asyncsend_eof()

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does nothing on successive calls).

Return type
:

None

classanyio.streams.text.TextReceiveStream(transport_stream, encoding='utf-8', errors='strict')

Bases: ObjectReceiveStream[str]

Stream wrapper that decodes bytes to strings using the given encoding.

Decoding is done using IncrementalDecoder which returns any completely received unicode characters as soon as they come in.

Parameters
:

transport_stream (Union[ObjectReceiveStream[bytes], ByteReceiveStream]) – any bytes-based receive stream

encoding (InitVar) – character encoding to use for decoding bytes to strings (defaults to utf-8)

errors (InitVar) – handling scheme for decoding errors (defaults to strict; see the codecs module documentation for a comprehensive list of options)

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

asyncreceive()

Receive the next item.

Raises
:

ClosedResourceError – if the receive stream has been explicitly closed

EndOfStream – if this stream has been closed from the other end

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

str

classanyio.streams.text.TextSendStream(transport_stream, encoding='utf-8', errors='strict')

Bases: ObjectSendStream[str]

Sends strings to the wrapped stream as bytes using the given encoding.

Parameters
:

transport_stream (AnyByteSendStream) – any bytes-based send stream

encoding (str) – character encoding to use for encoding strings to bytes (defaults to utf-8)

errors (str) – handling scheme for encoding errors (defaults to strict; see the codecs module documentation for a comprehensive list of options)

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

asyncsend(item)

Send an item to the peer(s).

Parameters
:

item (str) – the item to send

Raises
:

ClosedResourceError – if the send stream has been explicitly closed

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

None

classanyio.streams.text.TextStream(transport_stream, encoding='utf-8', errors='strict')

Bases: ObjectStream[str]

A bidirectional stream that decodes bytes to strings on receive and encodes strings to bytes on send.

Extra attributes will be provided from both streams, with the receive stream providing the values in case of a conflict.

Parameters
:

transport_stream (AnyByteStream) – any bytes-based stream

encoding (str) – character encoding to use for encoding/decoding strings to/from bytes (defaults to utf-8)

errors (str) – handling scheme for encoding errors (defaults to strict; see the codecs module documentation for a comprehensive list of options)

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

asyncreceive()

Receive the next item.

Raises
:

ClosedResourceError – if the receive stream has been explicitly closed

EndOfStream – if this stream has been closed from the other end

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

str

asyncsend(item)

Send an item to the peer(s).

Parameters
:

item (str) – the item to send

Raises
:

ClosedResourceError – if the send stream has been explicitly closed

BrokenResourceError – if this stream has been rendered unusable due to external causes

Return type
:

None

asyncsend_eof()

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does nothing on successive calls).

Return type
:

None

classanyio.streams.text.TextConnectable(connectable)

Bases: ObjectStreamConnectable[str]

asyncconnect()

Connect to the remote endpoint.

Return type
:

TextStream

Returns
:

an object stream connected to the remote end

Raises
:

ConnectionFailed – if the connection fails

classanyio.streams.tls.TLSAttribute

Bases: TypedAttributeSet

Contains Transport Layer Security related attributes.

alpn_protocol: str | None= <object object>

the selected ALPN protocol

channel_binding_tls_unique: bytes= <object object>

the channel binding for type tls-unique

cipher: tuple[str, str, int]= <object object>

the selected cipher

peer_certificate_binary: bytes | None= <object object>

the peer certificate in binary form

server_side: bool= <object object>

True if this is the server side of the connection

shared_ciphers: list[tuple[str, str, int]] | None= <object object>

ciphers shared by the client during the TLS handshake (None if this is the client side)

ssl_object: SSLObject= <object object>

the SSLObject used for encryption

standard_compatible: bool= <object object>

True if this stream does (and expects) a closing TLS handshake when the stream is being closed

tls_version: str= <object object>

the TLS protocol version (e.g. TLSv1.2)

classanyio.streams.tls.TLSStream(transport_stream, standard_compatible, _ssl_object, _read_bio, _write_bio)

Bases: ByteStream

A stream wrapper that encrypts all sent data and decrypts received data.

This class has no public initializer; use wrap() instead. All extra attributes from TLSAttribute are supported.

Variables
:

transport_stream (AnyByteStream) – the wrapped stream

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

asyncreceive(max_bytes=65536)

Receive at most max_bytes bytes from the peer.

Note

Implementers of this interface should not return an empty bytes object, and users should ignore them.

Parameters
:

max_bytes (int) – maximum number of bytes to receive

Return type
:

bytes

Returns
:

the received bytes

Raises
:

EndOfStream – if this stream has been closed from the other end

asyncsend(item)

Send the given bytes to the peer.

Parameters
:

item (bytes) – the bytes to send

Return type
:

None

asyncsend_eof()

Send an end-of-file indication to the peer.

You should not try to send any further data to this stream after calling this method. This method is idempotent (does nothing on successive calls).

Return type
:

None

asyncunwrap()

Does the TLS closing handshake.

Return type
:

tuple[Union[ObjectStream[bytes], ByteStream], bytes]

Returns
:

a tuple of (wrapped byte stream, bytes left in the read buffer)

async classmethodwrap(transport_stream, *, server_side=None, hostname=None, ssl_context=None, standard_compatible=True)

Wrap an existing stream with Transport Layer Security.

This performs a TLS handshake with the peer.

Parameters
:

transport_stream (Union[ObjectStream[bytes], ByteStream]) – a bytes-transporting stream to wrap

server_side (bool | None) – True if this is the server side of the connection, False if this is the client side (if omitted, will be set to False if hostname has been provided, False otherwise). Used only to create a default context when an explicit context has not been provided.

hostname (str | None) – host name of the peer (if host name checking is desired)

ssl_context (SSLContext | None) – the SSLContext object to use (if not provided, a secure default will be created)

standard_compatible (bool) – if False, skip the closing handshake when closing the connection, and don’t raise an exception if the peer does the same

Raises
:

SSLError – if the TLS handshake fails

Return type
:

TLSStream

classanyio.streams.tls.TLSListener(listener, ssl_context, standard_compatible=True, handshake_timeout=30)

Bases: Listener[TLSStream]

A convenience listener that wraps another listener and auto-negotiates a TLS session on every accepted connection.

If the TLS handshake times out or raises an exception, handle_handshake_error() is called to do whatever post-mortem processing is deemed necessary.

Supports only the standard_compatible extra attribute.

Parameters
:

listener (Listener) – the listener to wrap

ssl_context (SSLContext) – the SSL context object

standard_compatible (bool) – a flag passed through to TLSStream.wrap()

handshake_timeout (float) – time limit for the TLS handshake (passed to fail_after())

asyncaclose()

Close the resource.

Return type
:

None

propertyextra_attributes: Mapping[Any, Callable[[], Any]]

A mapping of the extra attributes to callables that return the corresponding values.

If the provider wraps another provider, the attributes from that wrapper should also be included in the returned mapping (but the wrapper may override the callables from the wrapped instance).

async statichandle_handshake_error(exc, stream)

Handle an exception raised during the TLS handshake.

This method does 3 things:

Forcefully closes the original stream

Logs the exception (unless it was a cancellation exception) using the anyio.streams.tls logger

Reraises the exception if it was a base exception or a cancellation exception

Parameters
:

exc (BaseException) – the exception

stream (Union[ObjectStream[bytes], ByteStream]) – the original stream

Return type
:

None

asyncserve(handler, task_group=None)

Accept incoming connections as they come in and start tasks to handle them.

Parameters
:

handler (Callable[[TLSStream], Any]) – a callable that will be used to handle each accepted connection

task_group (TaskGroup | None) – the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task group will be created)

Return type
:

None

classanyio.streams.tls.TLSConnectable(connectable, *, hostname=None, ssl_context=None, standard_compatible=True)

Bases: ByteStreamConnectable

Wraps another connectable and does TLS negotiation after a successful connection.

Parameters
:

connectable (Union[ObjectStreamConnectable[bytes], ByteStreamConnectable]) – the connectable to wrap

hostname (str | None) – host name of the server (if host name checking is desired)

ssl_context (SSLContext | None) – the SSLContext object to use (if not provided, a secure default will be created)

standard_compatible (bool) – if False, skip the closing handshake when closing the connection, and don’t raise an exception if the server does the same

asyncconnect()

Connect to the remote endpoint.

Return type
:

TLSStream

Returns
:

a bytestream connected to the remote end

Raises
:

ConnectionFailed – if the connection fails

Sockets and networking
anyio.as_connectable(remote, /, *, tls=False, ssl_context=None, tls_hostname=None, tls_standard_compatible=True)

Return a byte stream connectable from the given object.

If a bytestream connectable is given, it is returned unchanged. If a tuple of (host, port) is given, a TCP connectable is returned. If a string or bytes path is given, a UNIX connectable is returned.

If tls=True, the connectable will be wrapped in a TLSConnectable.

Parameters
:

remote (ByteStreamConnectable | tuple[str | IPv4Address | IPv6Address, int] | str | bytes | PathLike[str]) – a connectable, a tuple of (host, port) or a path to a UNIX socket

tls (bool) – if True, wrap the plaintext connectable in a TLSConnectable, using the provided TLS settings)

ssl_context (SSLContext | None) – if tls=True, the SSLContext object to use (if not provided, a secure default will be created)

tls_hostname (str | None) – if tls=True, host name of the server to use for checking the server certificate (defaults to the host portion of the address for TCP connectables)

tls_standard_compatible (bool) – if False and tls=True, makes the TLS stream skip the closing handshake when closing the connection, so it won’t raise an exception if the server does the same

Return type
:

ByteStreamConnectable

asyncanyio.connect_tcp(remote_host, remote_port, *, local_host=None, tls=False, ssl_context=None, tls_standard_compatible=True, tls_hostname=None, happy_eyeballs_delay=0.25)

Connect to a host using the TCP protocol.

This function implements the stateless version of the Happy Eyeballs algorithm (RFC 6555). If remote_host is a host name that resolves to multiple IP addresses, each one is tried until one connection attempt succeeds. If the first attempt does not connected within 250 milliseconds, a second attempt is started using the next address in the list, and so on. On IPv6 enabled systems, an IPv6 address (if available) is tried first.

When the connection has been established, a TLS handshake will be done if either ssl_context or tls_hostname is not None, or if tls is True.

Parameters
:

remote_host (Union[str, IPv4Address, IPv6Address]) – the IP address or host name to connect to

remote_port (int) – port on the target host to connect to

local_host (Union[str, IPv4Address, IPv6Address, None]) – the interface address or name to bind the socket to before connecting

tls (bool) – True to do a TLS handshake with the connected stream and return a TLSStream instead

ssl_context (SSLContext | None) – the SSL context object to use (if omitted, a default context is created)

tls_standard_compatible (bool) – If True, performs the TLS shutdown handshake before closing the stream and requires that the server does this as well. Otherwise, SSLEOFError may be raised during reads from the stream. Some protocols, such as HTTP, require this option to be False. See wrap_socket() for details.

tls_hostname (str | None) – host name to check the server certificate against (defaults to the value of remote_host)

happy_eyeballs_delay (float) – delay (in seconds) before starting the next connection attempt

Return type
:

SocketStream | TLSStream

Returns
:

a socket stream object if no TLS handshake was done, otherwise a TLS stream

Raises
:

ConnectionFailed – if the connection fails

asyncanyio.connect_unix(path)

Connect to the given UNIX socket.

Not available on Windows.

Parameters
:

path (str | bytes | PathLike[Any]) – path to the socket

Return type
:

UNIXSocketStream

Returns
:

a socket stream object

Raises
:

ConnectionFailed – if the connection fails

asyncanyio.create_tcp_listener(*, local_host=None, local_port=0, family=AddressFamily.AF_UNSPEC, backlog=65536, reuse_port=False)

Create a TCP socket listener.

Parameters
:

local_port (int) – port number to listen on

local_host (Union[str, IPv4Address, IPv6Address, None]) – IP address of the interface to listen on. If omitted, listen on all IPv4 and IPv6 interfaces. To listen on all interfaces on a specific address family, use 0.0.0.0 for IPv4 or :: for IPv6.

family (Literal[<AddressFamily.AF_UNSPEC: 0>, <AddressFamily.AF_INET: 2>, <AddressFamily.AF_INET6: 10>]) – address family (used if local_host was omitted)

backlog (int) – maximum number of queued incoming connections (up to a maximum of 2**16, or 65536)

reuse_port (bool) – True to allow multiple sockets to bind to the same address/port (not supported on Windows)

Return type
:

MultiListener[SocketStream]

Returns
:

a multi-listener object containing one or more socket listeners

Raises
:

OSError – if there’s an error creating a socket, or binding to one or more interfaces failed

asyncanyio.create_unix_listener(path, *, mode=None, backlog=65536)

Create a UNIX socket listener.

Not available on Windows.

Parameters
:

path (str | bytes | PathLike[Any]) – path of the socket

mode (int | None) – permissions to set on the socket

backlog (int) – maximum number of queued incoming connections (up to a maximum of 2**16, or 65536)

Return type
:

SocketListener

Returns
:

a listener object

Changed in version 3.0: If a socket already exists on the file system in the given path, it will be removed first.

asyncanyio.create_udp_socket(family=AddressFamily.AF_UNSPEC, *, local_host=None, local_port=0, reuse_port=False)

Create a UDP socket.

If port has been given, the socket will be bound to this port on the local machine, making this socket suitable for providing UDP based services.

Parameters
:

family (Literal[<AddressFamily.AF_UNSPEC: 0>, <AddressFamily.AF_INET: 2>, <AddressFamily.AF_INET6: 10>]) – address family (AF_INET or AF_INET6) – automatically determined from local_host if omitted

local_host (Union[str, IPv4Address, IPv6Address, None]) – IP address or host name of the local interface to bind to

local_port (int) – local port to bind to

reuse_port (bool) – True to allow multiple sockets to bind to the same address/port (not supported on Windows)

Return type
:

UDPSocket

Returns
:

a UDP socket

asyncanyio.create_connected_udp_socket(remote_host, remote_port, *, family=AddressFamily.AF_UNSPEC, local_host=None, local_port=0, reuse_port=False)

Create a connected UDP socket.

Connected UDP sockets can only communicate with the specified remote host/port, an any packets sent from other sources are dropped.

Parameters
:

remote_host (Union[str, IPv4Address, IPv6Address]) – remote host to set as the default target

remote_port (int) – port on the remote host to set as the default target

family (Literal[<AddressFamily.AF_UNSPEC: 0>, <AddressFamily.AF_INET: 2>, <AddressFamily.AF_INET6: 10>]) – address family (AF_INET or AF_INET6) – automatically determined from local_host or remote_host if omitted

local_host (Union[str, IPv4Address, IPv6Address, None]) – IP address or host name of the local interface to bind to

local_port (int) – local port to bind to

reuse_port (bool) – True to allow multiple sockets to bind to the same address/port (not supported on Windows)

Return type
:

ConnectedUDPSocket

Returns
:

a connected UDP socket

asyncanyio.getaddrinfo(host, port, *, family=0, type=0, proto=0, flags=0)

Look up a numeric IP address given a host name.

Internationalized domain names are translated according to the (non-transitional) IDNA 2008 standard.

Note

4-tuple IPv6 socket addresses are automatically converted to 2-tuples of (host, port), unlike what socket.getaddrinfo() does.

Parameters
:

host (bytes | str | None) – host name

port (str | int | None) – port number

family (int | AddressFamily) – socket family (‘AF_INET`, …)

type (int | SocketKind) – socket type (SOCK_STREAM, …)

proto (int) – protocol number

flags (int) – flags to pass to upstream getaddrinfo()

Return type
:

list[tuple[AddressFamily, SocketKind, int, str, tuple[str, int]]]

Returns
:

list of tuples containing (family, type, proto, canonname, sockaddr)

See also

socket.getaddrinfo()

anyio.getnameinfo(sockaddr, flags=0)

Look up the host name of an IP address.

Parameters
:

sockaddr (tuple[str, int]) – socket address (e.g. (ipaddress, port) for IPv4)

flags (int) – flags to pass to upstream getnameinfo()

Return type
:

Awaitable[tuple[str, str]]

Returns
:

a tuple of (host name, service name)

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

See also

socket.getnameinfo()

anyio.wait_readable(obj)

Wait until the given object has data to be read.

On Unix systems, obj must either be an integer file descriptor, or else an object with a .fileno() method which returns an integer file descriptor. Any kind of file descriptor can be passed, though the exact semantics will depend on your kernel. For example, this probably won’t do anything useful for on-disk files.

On Windows systems, obj must either be an integer SOCKET handle, or else an object with a .fileno() method which returns an integer SOCKET handle. File descriptors aren’t supported, and neither are handles that refer to anything besides a SOCKET.

On backends where this functionality is not natively provided (asyncio ProactorEventLoop on Windows), it is provided using a separate selector thread which is set to shut down when the interpreter shuts down.

Warning

Don’t use this on raw sockets that have been wrapped by any higher level constructs like socket streams!

Parameters
:

obj (object) – an object with a .fileno() method or an integer handle

Raises
:

ClosedResourceError – if the object was closed while waiting for the object to become readable

BusyResourceError – if another task is already waiting for the object to become readable

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Return type
:

Awaitable[None]

anyio.wait_socket_readable(sock)

Deprecated since version 4.7.0: Use wait_readable() instead.

Wait until the given socket has data to be read.

Warning

Only use this on raw sockets that have not been wrapped by any higher level constructs like socket streams!

Parameters
:

sock (socket) – a socket object

Raises
:

ClosedResourceError – if the socket was closed while waiting for the socket to become readable

BusyResourceError – if another task is already waiting for the socket to become readable

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Return type
:

Awaitable[None]

anyio.wait_socket_writable(sock)

Deprecated since version 4.7.0: Use wait_writable() instead.

Wait until the given socket can be written to.

This does NOT work on Windows when using the asyncio backend with a proactor event loop (default on py3.8+).

Warning

Only use this on raw sockets that have not been wrapped by any higher level constructs like socket streams!

Parameters
:

sock (socket) – a socket object

Raises
:

ClosedResourceError – if the socket was closed while waiting for the socket to become writable

BusyResourceError – if another task is already waiting for the socket to become writable

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Return type
:

Awaitable[None]

anyio.wait_writable(obj)

Wait until the given object can be written to.

Parameters
:

obj (FileDescriptorLike) – an object with a .fileno() method or an integer handle

Raises
:

ClosedResourceError – if the object was closed while waiting for the object to become writable

BusyResourceError – if another task is already waiting for the object to become writable

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Return type
:

Awaitable[None]

See also

See the documentation of wait_readable() for the definition of obj and notes on backend compatibility.

Warning

Don’t use this on raw sockets that have been wrapped by any higher level constructs like socket streams!

classanyio.abc.SocketAttribute

Bases: TypedAttributeSet

family: socket.AddressFamily

the address family of the underlying socket

local_address: tuple[str, int] | str

the local address the underlying socket is connected to

local_port: int

for IP based sockets, the local port the underlying socket is bound to

raw_socket: socket.socket

the underlying stdlib socket object

remote_address: tuple[str, int] | str

the remote address the underlying socket is connected to

remote_port: int

for IP based sockets, the remote port the underlying socket is connected to

classanyio.abc.SocketStream

Bases: ByteStream, _SocketProvider

Transports bytes over a socket.

Supports all relevant extra attributes from SocketAttribute.

async classmethodfrom_socket(sock_or_fd)

Wrap an existing socket object or file descriptor as a socket stream.

The newly created socket wrapper takes ownership of the socket being passed in. The existing socket must already be connected.

Parameters
:

sock_or_fd (socket | int) – a socket object or file descriptor

Return type
:

SocketStream

Returns
:

a socket stream

classanyio.abc.SocketListener

Bases: Listener[SocketStream], _SocketProvider

Listens to incoming socket connections.

Supports all relevant extra attributes from SocketAttribute.

abstractmethod asyncaccept()

Accept an incoming connection.

Return type
:

SocketStream

async classmethodfrom_socket(sock_or_fd)

Wrap an existing socket object or file descriptor as a socket listener.

The newly created listener takes ownership of the socket being passed in.

Parameters
:

sock_or_fd (socket | int) – a socket object or file descriptor

Return type
:

SocketListener

Returns
:

a socket listener

asyncserve(handler, task_group=None)

Accept incoming connections as they come in and start tasks to handle them.

Parameters
:

handler (Callable[[SocketStream], Any]) – a callable that will be used to handle each accepted connection

task_group (TaskGroup | None) – the task group that will be used to start tasks for handling each accepted connection (if omitted, an ad-hoc task group will be created)

Return type
:

None

classanyio.abc.UDPSocket

Bases: UnreliableObjectStream[tuple[bytes, tuple[str, int]]], _SocketProvider

Represents an unconnected UDP socket.

Supports all relevant extra attributes from SocketAttribute.

async classmethodfrom_socket(sock_or_fd)

Wrap an existing socket object or file descriptor as a UDP socket.

The newly created socket wrapper takes ownership of the socket being passed in. The existing socket must be bound to a local address.

Parameters
:

sock_or_fd (socket | int) – a socket object or file descriptor

Return type
:

UDPSocket

Returns
:

a UDP socket

asyncsendto(data, host, port)

Alias for send() ((data, (host, port))).

Return type
:

None

classanyio.abc.ConnectedUDPSocket

Bases: UnreliableObjectStream[bytes], _SocketProvider

Represents an connected UDP socket.

Supports all relevant extra attributes from SocketAttribute.

async classmethodfrom_socket(sock_or_fd)

Wrap an existing socket object or file descriptor as a connected UDP socket.

The newly created socket wrapper takes ownership of the socket being passed in. The existing socket must already be connected.

Parameters
:

sock_or_fd (socket | int) – a socket object or file descriptor

Return type
:

ConnectedUDPSocket

Returns
:

a connected UDP socket

classanyio.abc.UNIXSocketStream

Bases: SocketStream

async classmethodfrom_socket(sock_or_fd)

Wrap an existing socket object or file descriptor as a UNIX socket stream.

The newly created socket wrapper takes ownership of the socket being passed in. The existing socket must already be connected.

Parameters
:

sock_or_fd (socket | int) – a socket object or file descriptor

Return type
:

UNIXSocketStream

Returns
:

a UNIX socket stream

abstractmethod asyncreceive_fds(msglen, maxfds)

Receive file descriptors along with a message from the peer.

Parameters
:

msglen (int) – length of the message to expect from the peer

maxfds (int) – maximum number of file descriptors to expect from the peer

Return type
:

tuple[bytes, list[int]]

Returns
:

a tuple of (message, file descriptors)

abstractmethod asyncsend_fds(message, fds)

Send file descriptors along with a message to the peer.

Parameters
:

message (bytes) – a non-empty bytestring

fds (Collection[int | IOBase]) – a collection of files (either numeric file descriptors or open file or socket objects)

Return type
:

None

classanyio.abc.UNIXDatagramSocket

Bases: UnreliableObjectStream[tuple[bytes, str]], _SocketProvider

Represents an unconnected Unix datagram socket.

Supports all relevant extra attributes from SocketAttribute.

async classmethodfrom_socket(sock_or_fd)

Wrap an existing socket object or file descriptor as a UNIX datagram socket.

The newly created socket wrapper takes ownership of the socket being passed in.

Parameters
:

sock_or_fd (socket | int) – a socket object or file descriptor

Return type
:

UNIXDatagramSocket

Returns
:

a UNIX datagram socket

asyncsendto(data, path)

Alias for send() ((data, path)).

Return type
:

None

classanyio.abc.ConnectedUNIXDatagramSocket

Bases: UnreliableObjectStream[bytes], _SocketProvider

Represents a connected Unix datagram socket.

Supports all relevant extra attributes from SocketAttribute.

async classmethodfrom_socket(sock_or_fd)

Wrap an existing socket object or file descriptor as a connected UNIX datagram socket.

The newly created socket wrapper takes ownership of the socket being passed in. The existing socket must already be connected.

Parameters
:

sock_or_fd (socket | int) – a socket object or file descriptor

Return type
:

ConnectedUNIXDatagramSocket

Returns
:

a connected UNIX datagram socket

classanyio.TCPConnectable(host, port)

Bases: ByteStreamConnectable

Connects to a TCP server at the given host and port.

Parameters
:

host (str | IPv4Address | IPv6Address) – host name or IP address of the server

port (int) – TCP port number of the server

asyncconnect()

Connect to the remote endpoint.

Return type
:

SocketStream

Returns
:

a bytestream connected to the remote end

Raises
:

ConnectionFailed – if the connection fails

classanyio.UNIXConnectable(path)

Bases: ByteStreamConnectable

Connects to a UNIX domain socket at the given path.

Parameters
:

path (str | bytes | PathLike[str] | PathLike[bytes]) – the file system path of the socket

asyncconnect()

Connect to the remote endpoint.

Return type
:

UNIXSocketStream

Returns
:

a bytestream connected to the remote end

Raises
:

ConnectionFailed – if the connection fails

Subprocesses
asyncanyio.run_process(command, *, input=None, stdin=None, stdout=-1, stderr=-1, check=True, cwd=None, env=None, startupinfo=None, creationflags=0, start_new_session=False, pass_fds=(), user=None, group=None, extra_groups=None, umask=-1)

Run an external command in a subprocess and wait until it completes.

See also

subprocess.run()

Parameters
:

command (Union[str, bytes, PathLike[str], PathLike[bytes], Sequence[Union[str, bytes, PathLike[str], PathLike[bytes]]]]) – either a string to pass to the shell, or an iterable of strings containing the executable name or path and its arguments

input (bytes | None) – bytes passed to the standard input of the subprocess

stdin (Union[int, IO[Any], None]) – one of subprocess.PIPE, subprocess.DEVNULL, a file-like object, or None; input overrides this

stdout (Union[int, IO[Any], None]) – one of subprocess.PIPE, subprocess.DEVNULL, a file-like object, or None

stderr (Union[int, IO[Any], None]) – one of subprocess.PIPE, subprocess.DEVNULL, subprocess.STDOUT, a file-like object, or None

check (bool) – if True, raise CalledProcessError if the process terminates with a return code other than 0

cwd (Union[str, bytes, PathLike[str], PathLike[bytes], None]) – If not None, change the working directory to this before running the command

env (Mapping[str, str] | None) – if not None, this mapping replaces the inherited environment variables from the parent process

startupinfo (Any) – an instance of subprocess.STARTUPINFO that can be used to specify process startup parameters (Windows only)

creationflags (int) – flags that can be used to control the creation of the subprocess (see subprocess.Popen for the specifics)

start_new_session (bool) – if true the setsid() system call will be made in the child process prior to the execution of the subprocess. (POSIX only)

pass_fds (Sequence[int]) – sequence of file descriptors to keep open between the parent and child processes. (POSIX only)

user (str | int | None) – effective user to run the process as (Python >= 3.9, POSIX only)

group (str | int | None) – effective group to run the process as (Python >= 3.9, POSIX only)

extra_groups (Iterable[str | int] | None) – supplementary groups to set in the subprocess (Python >= 3.9, POSIX only)

umask (int) – if not negative, this umask is applied in the child process before running the given command (Python >= 3.9, POSIX only)

Return type
:

CompletedProcess[bytes]

Returns
:

an object representing the completed process

Raises
:

CalledProcessError – if check is True and the process exits with a nonzero return code

asyncanyio.open_process(command, *, stdin=-1, stdout=-1, stderr=-1, cwd=None, env=None, startupinfo=None, creationflags=0, start_new_session=False, pass_fds=(), user=None, group=None, extra_groups=None, umask=-1)

Start an external command in a subprocess.

See also

subprocess.Popen

Parameters
:

command (Union[str, bytes, PathLike[str], PathLike[bytes], Sequence[Union[str, bytes, PathLike[str], PathLike[bytes]]]]) – either a string to pass to the shell, or an iterable of strings containing the executable name or path and its arguments

stdin (Union[int, IO[Any], None]) – one of subprocess.PIPE, subprocess.DEVNULL, a file-like object, or None

stdout (Union[int, IO[Any], None]) – one of subprocess.PIPE, subprocess.DEVNULL, a file-like object, or None

stderr (Union[int, IO[Any], None]) – one of subprocess.PIPE, subprocess.DEVNULL, subprocess.STDOUT, a file-like object, or None

cwd (Union[str, bytes, PathLike[str], PathLike[bytes], None]) – If not None, the working directory is changed before executing

env (Mapping[str, str] | None) – If env is not None, it must be a mapping that defines the environment variables for the new process

creationflags (int) – flags that can be used to control the creation of the subprocess (see subprocess.Popen for the specifics)

startupinfo (Any) – an instance of subprocess.STARTUPINFO that can be used to specify process startup parameters (Windows only)

start_new_session (bool) – if true the setsid() system call will be made in the child process prior to the execution of the subprocess. (POSIX only)

pass_fds (Sequence[int]) – sequence of file descriptors to keep open between the parent and child processes. (POSIX only)

user (str | int | None) – effective user to run the process as (POSIX only)

group (str | int | None) – effective group to run the process as (POSIX only)

extra_groups (Iterable[str | int] | None) – supplementary groups to set in the subprocess (POSIX only)

umask (int) – if not negative, this umask is applied in the child process before running the given command (POSIX only)

Return type
:

Process

Returns
:

an asynchronous process object

classanyio.abc.Process

Bases: AsyncResource

An asynchronous version of subprocess.Popen.

abstractmethodkill()

Kills the process.

On Windows, this calls TerminateProcess(). On POSIX systems, this sends SIGKILL to the process.

See also

subprocess.Popen.kill()

Return type
:

None

abstract propertypid: int

The process ID of the process.

 
abstract propertyreturncode: int | None

The return code of the process. If the process has not yet terminated, this will be None.

abstractmethodsend_signal(signal)

Send a signal to the subprocess.

See also

subprocess.Popen.send_signal()

Parameters
:

signal (Signals) – the signal number (e.g. signal.SIGHUP)

Return type
:

None

abstract propertystderr: ByteReceiveStream | None

The stream for the standard error output of the process.

 
abstract propertystdin: ByteSendStream | None

The stream for the standard input of the process.

 
abstract propertystdout: ByteReceiveStream | None

The stream for the standard output of the process.

abstractmethodterminate()

Terminates the process, gracefully if possible.

On Windows, this calls TerminateProcess(). On POSIX systems, this sends SIGTERM to the process.

See also

subprocess.Popen.terminate()

Return type
:

None

abstractmethod asyncwait()

Wait until the process exits.

Return type
:

int

Returns
:

the exit code of the process

Synchronization
classanyio.Event

Bases: object

is_set()

Return True if the flag is set, False if not.

Return type
:

bool

set()

Set the flag, notifying all listeners.

Return type
:

None

statistics()

Return statistics about the current state of this event.

Return type
:

EventStatistics

asyncwait()

Wait until the flag has been set.

If the flag has already been set when this method is called, it returns immediately.

Return type
:

None

classanyio.Lock(*, fast_acquire: bool = False)

Bases: object

asyncacquire()

Acquire the lock.

Return type
:

None

acquire_nowait()

Acquire the lock, without blocking.

Raises
:

WouldBlock – if the operation would block

Return type
:

None

locked()

Return True if the lock is currently held.

Return type
:

bool

release()

Release the lock.

Return type
:

None

statistics()

Return statistics about the current state of this lock.

Added in version 3.0.

Return type
:

LockStatistics

classanyio.Condition(lock=None)

Bases: object

asyncacquire()

Acquire the underlying lock.

Return type
:

None

acquire_nowait()

Acquire the underlying lock, without blocking.

Raises
:

WouldBlock – if the operation would block

Return type
:

None

locked()

Return True if the lock is set.

Return type
:

bool

notify(n=1)

Notify exactly n listeners.

Return type
:

None

notify_all()

Notify all the listeners.

Return type
:

None

release()

Release the underlying lock.

Return type
:

None

statistics()

Return statistics about the current state of this condition.

Added in version 3.0.

Return type
:

ConditionStatistics

asyncwait()

Wait for a notification.

Return type
:

None

asyncwait_for(predicate)

Wait until a predicate becomes true.

Parameters
:

predicate (Callable[[], TypeVar(T)]) – a callable that returns a truthy value when the condition is met

Return type
:

TypeVar(T)

Returns
:

the result of the predicate

Added in version 4.11.0.

classanyio.Semaphore(initial_value, *, max_value=None, fast_acquire=False)

Bases: object

asyncacquire()

Decrement the semaphore value, blocking if necessary.

Return type
:

None

acquire_nowait()

Acquire the underlying lock, without blocking.

Raises
:

WouldBlock – if the operation would block

Return type
:

None

propertymax_value: int | None

The maximum value of the semaphore.

release()

Increment the semaphore value.

Return type
:

None

statistics()

Return statistics about the current state of this semaphore.

Added in version 3.0.

Return type
:

SemaphoreStatistics

propertyvalue: int

The current value of the semaphore.

classanyio.CapacityLimiter(total_tokens: float)

Bases: object

asyncacquire()

Acquire a token for the current task, waiting if necessary for one to become available.

Return type
:

None

acquire_nowait()

Acquire a token for the current task without waiting for one to become available.

Raises
:

WouldBlock – if there are no tokens available for borrowing

Return type
:

None

asyncacquire_on_behalf_of(borrower)

Acquire a token, waiting if necessary for one to become available.

Parameters
:

borrower (object) – the entity borrowing a token

Return type
:

None

acquire_on_behalf_of_nowait(borrower)

Acquire a token without waiting for one to become available.

Parameters
:

borrower (object) – the entity borrowing a token

Raises
:

WouldBlock – if there are no tokens available for borrowing

Return type
:

None

propertyavailable_tokens: float

The number of tokens currently available to be borrowed

 
propertyborrowed_tokens: int

The number of tokens that have currently been borrowed.

release()

Release the token held by the current task.

Raises
:

RuntimeError – if the current task has not borrowed a token from this limiter.

Return type
:

None

release_on_behalf_of(borrower)

Release the token held by the given borrower.

Raises
:

RuntimeError – if the borrower has not borrowed a token from this limiter.

Return type
:

None

statistics()

Return statistics about the current state of this limiter.

Added in version 3.0.

Return type
:

CapacityLimiterStatistics

propertytotal_tokens: float

The total number of tokens available for borrowing.

This is a read-write property. If the total number of tokens is increased, the proportionate number of tasks waiting on this limiter will be granted their tokens.

Changed in version 3.0: The property is now writable.

Changed in version 4.12: The value can now be set to 0.

classanyio.ResourceGuard(action='using')

Bases: object

A context manager for ensuring that a resource is only used by a single task at a time.

Entering this context manager while the previous has not exited it yet will trigger BusyResourceError.

Parameters
:

action (str) – the action to guard against (visible in the BusyResourceError when triggered, e.g. “Another task is already {action} this resource”)

Added in version 4.1.

classanyio.LockStatistics(locked, owner, tasks_waiting)

Bases: object

Variables
:

locked (bool) – flag indicating if this lock is locked or not

owner (TaskInfo) – task currently holding the lock (or None if the lock is not held by any task)

tasks_waiting (int) – number of tasks waiting on acquire()

classanyio.EventStatistics(tasks_waiting)

Bases: object

Variables
:

tasks_waiting (int) – number of tasks waiting on wait()

classanyio.ConditionStatistics(tasks_waiting, lock_statistics)

Bases: object

Variables
:

tasks_waiting (int) – number of tasks blocked on wait()

lock_statistics (LockStatistics) – statistics of the underlying Lock

classanyio.CapacityLimiterStatistics(borrowed_tokens, total_tokens, borrowers, tasks_waiting)

Bases: object

Variables
:

borrowed_tokens (int) – number of tokens currently borrowed by tasks

total_tokens (float) – total number of available tokens

borrowers (tuple) – tasks or other objects currently holding tokens borrowed from this limiter

tasks_waiting (int) – number of tasks waiting on acquire() or acquire_on_behalf_of()

classanyio.SemaphoreStatistics(tasks_waiting)

Bases: object

Variables
:

tasks_waiting (int) – number of tasks waiting on acquire()

Operating system signals
anyio.open_signal_receiver(*signals)

Start receiving operating system signals.

Parameters
:

signals (Signals) – signals to receive (e.g. signal.SIGINT)

Return type
:

AbstractContextManager[AsyncIterator[Signals]]

Returns
:

an asynchronous context manager for an asynchronous iterator which yields signal numbers

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Warning

Windows does not support signals natively so it is best to avoid relying on this in cross-platform applications.

Warning

On asyncio, this permanently replaces any previous signal handler for the given signals, as set via add_signal_handler().

Asynchronous functools
anyio.functools.cache(func, /)

A convenient shortcut for lru_cache() with maxsize=None.

This is the asynchronous equivalent to functools.cache().

anyio.functools.lru_cache(func=None, /, *, maxsize=128, typed=False, always_checkpoint=False)

An asynchronous version of functools.lru_cache().

If a synchronous function is passed, the standard library functools.lru_cache() is applied instead.

Parameters
:

always_checkpoint – if True, every call to the cached function will be guaranteed to yield control to the event loop at least once

Note

Caches and locks are managed on a per-event loop basis.

asyncanyio.functools.reduce(function, iterable, /, initial=<anyio.functools._InitialMissingType object>)

Asynchronous version of functools.reduce().

Parameters
:

function (Callable[[TypeVar(T), TypeVar(T)], Awaitable[TypeVar(T)]] | Callable[[TypeVar(T), TypeVar(S)], Awaitable[TypeVar(T)]]) – a coroutine function that takes two arguments: the accumulated value and the next element from the iterable

iterable (Iterable[TypeVar(T)] | Iterable[TypeVar(S)] | AsyncIterable[TypeVar(T)] | AsyncIterable[TypeVar(S)]) – an iterable or async iterable

initial (Union[TypeVar(T), _InitialMissingType]) – the initial value (if missing, the first element of the iterable is used as the initial value)

Return type
:

TypeVar(T)

Low level operations
asyncanyio.lowlevel.checkpoint()

Check for cancellation and allow the scheduler to switch to another task.

Equivalent to (but more efficient than):

await checkpoint_if_cancelled()
await cancel_shielded_checkpoint()


Added in version 3.0.

Return type
:

None

asyncanyio.lowlevel.checkpoint_if_cancelled()

Enter a checkpoint if the enclosing cancel scope has been cancelled.

This does not allow the scheduler to switch to a different task.

Added in version 3.0.

Return type
:

None

asyncanyio.lowlevel.cancel_shielded_checkpoint()

Allow the scheduler to switch to another task but without checking for cancellation.

Equivalent to (but potentially more efficient than):

with CancelScope(shield=True):
    await checkpoint()


Added in version 3.0.

Return type
:

None

anyio.lowlevel.current_token()

Return a token object that can be used to call code in the current event loop from another thread.

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

Added in version 4.11.0.

Return type
:

EventLoopToken

classanyio.lowlevel.RunVar(name, default=_NoValueSet.NO_VALUE_SET)

Bases: Generic[T]

Like a ContextVar, except scoped to the running event loop.

Can be used as a context manager, Just like ContextVar, that will reset the variable to its previous value when the context block is exited.

final classanyio.lowlevel.EventLoopToken(backend_class, native_token)

Bases: object

An opaque object that holds a reference to an event loop.

Added in version 4.11.0.

Testing and debugging
classanyio.TaskInfo(id, parent_id, name, coro)

Bases: object

Represents an asynchronous task.

Variables
:

id (int) – the unique identifier of the task

parent_id (Optional[int]) – the identifier of the parent task, if any

name (str) – the description of the task (if any)

coro (Coroutine) – the coroutine object of the task

has_pending_cancellation()

Return True if the task has a cancellation pending, False otherwise.

Return type
:

bool

classanyio.pytest_plugin.FreePortFactory(kind)

Bases: object

Manages port generation based on specified socket kind, ensuring no duplicate ports are generated.

This class provides functionality for generating available free ports on the system. It is initialized with a specific socket kind and can generate ports for given address families while avoiding reuse of previously generated ports.

Users should not instantiate this class directly, but use the free_tcp_port_factory and free_udp_port_factory fixtures instead. For simple uses cases, free_tcp_port and free_udp_port can be used instead.

propertykind: SocketKind

The type of socket connection (e.g., SOCK_STREAM or SOCK_DGRAM) used to bind for checking port availability

anyio.get_current_task()

Return the current task.

Return type
:

TaskInfo

Returns
:

a representation of the current task

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

anyio.get_running_tasks()

Return a list of running tasks in the current event loop.

Return type
:

list[TaskInfo]

Returns
:

a list of task info objects

Raises
:

NoEventLoopError – if no supported asynchronous event loop is running in the current thread

asyncanyio.wait_all_tasks_blocked()

Wait until all other tasks are waiting for something.

Return type
:

None

Exceptions
exceptionanyio.BrokenResourceError

Bases: Exception

Raised when trying to use a resource that has been rendered unusable due to external causes (e.g. a send stream whose peer has disconnected).

exceptionanyio.BrokenWorkerInterpreter(excinfo)

Bases: Exception

Raised by run_sync() if an unexpected exception is raised in the subinterpreter.

exceptionanyio.BrokenWorkerProcess

Bases: Exception

Raised by run_sync() if the worker process terminates abruptly or otherwise misbehaves.

exceptionanyio.BusyResourceError(action)

Bases: Exception

Raised when two tasks are trying to read from or write to the same resource concurrently.

exceptionanyio.ClosedResourceError

Bases: Exception

Raised when trying to use a resource that has been closed.

exceptionanyio.ConnectionFailed

Bases: OSError

Raised when a connection attempt fails.

Note

This class inherits from OSError for backwards compatibility.

exceptionanyio.DelimiterNotFound(max_bytes)

Bases: Exception

Raised during receive_until() if the maximum number of bytes has been read without the delimiter being found.

exceptionanyio.EndOfStream

Bases: Exception

Raised when trying to read from a stream that has been closed from the other end.

exceptionanyio.IncompleteRead

Bases: Exception

Raised during receive_exactly() or receive_until() if the connection is closed before the requested amount of bytes has been read.

exceptionanyio.NoEventLoopError

Bases: RuntimeError

Raised by several functions that require an event loop to be running in the current thread when there is no running event loop.

This is also raised by from_thread.run() and from_thread.run_sync() if not calling from an AnyIO worker thread, and no token was passed.

exceptionanyio.RunFinishedError

Bases: RuntimeError

Raised by from_thread.run() and from_thread.run_sync() if the event loop associated with the explicitly passed token has already finished.

exceptionanyio.TypedAttributeLookupError

Bases: LookupError

Raised by extra() when the given typed attribute is not found and no default value has been given.

exceptionanyio.WouldBlock

Bases: Exception

Raised by X_nowait functions if X() would block.

 Previous
Next 

© Copyright 2018, Alex Grönholm.

Built with Sphinx using a theme provided by Read the Docs.
Augment Code Review Benchmarked #1 Against Cursor, Copilot, Claude Install Now
Ads by EthicalAds
Close Ad
