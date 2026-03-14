# Source: https://anyio.readthedocs.io/en/stable/why.html

Title: Why you should be using AnyIO APIs instead of asyncio APIs — AnyIO 0.0.post50 documentation

URL Source: https://anyio.readthedocs.io/en/stable/why.html

Markdown Content:
AnyIO is not just a compatibility layer for bridging asyncio and [Trio](https://github.com/python-trio/trio). For one, it comes with its own diverse set of Trio-inspired APIs which have been designed to be a step up from asyncio. Secondly, asyncio has numerous design issues and missing features that AnyIO fixes for you. Therefore there are strong merits in switching to AnyIO APIs even if you are developing an application and not a library.

Design problems with task management[](https://anyio.readthedocs.io/en/stable/why.html#design-problems-with-task-management "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

While the [`asyncio.TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "(in Python v3.14)") class, introduced in Python 3.11, is a major step towards structured concurrency, it only provides a very narrow API that severely limits its usefulness.

First and foremost, the [`asyncio.TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "(in Python v3.14)") class does not offer any way to cancel, or even list all of the contained tasks, so in order to do that, you would still have to keep track of any tasks you create. This also makes it problematic to pass the task group to a child tasks, as tracking the tasks becomes a lot more tedious in such cases.

Secondly, while AnyIO (and [Trio](https://github.com/python-trio/trio)) has long provided a way to wait until a newly launched task signals readiness, [`asyncio.TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "(in Python v3.14)") still does not provide any such mechanism, leaving users to devise their own, often error-prone methods to achieve this.

### How does AnyIO fix these problems?[](https://anyio.readthedocs.io/en/stable/why.html#how-does-anyio-fix-these-problems "Link to this heading")

An AnyIO task group contains its own cancel scope which can be used to cancel all the child tasks, regardless of where they were launched from. Furthermore, if the task group’s cancel scope is cancelled, any tasks launched from the task group since then are _also_ automatically subject to cancellation, thus ensuring that nothing can accidentally hang the task group and prevent it from exiting.

As for tasks signalling readiness, [here](https://anyio.readthedocs.io/en/stable/tasks.html#start-initialize) is an example of waiting until a child task is ready.

Note

In all fairness, AnyIO’s task groups have their own ergonomics issues, like the inability to retrieve the tasks’ return values and not being easily able to cancel individual tasks. This is something that [#890](https://github.com/agronholm/anyio/pull/890) aims to rectify.

Design problems with cancellation[](https://anyio.readthedocs.io/en/stable/why.html#design-problems-with-cancellation "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

The most significant problems with asyncio relate to its handling of cancellation. Asyncio employs a cancellation mechanism where cancelling a task schedules a [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "(in Python v3.14)") exception to be raised in the task (once). This mechanism is called _edge cancellation_.

The most common problem with edge cancellation is that if the task catches the [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "(in Python v3.14)") (which often happens by accident when the user code has a `except BaseException:` block and doesn’t re-raise the exception), then no further action is taken, and the task keeps happily running until it is explicitly cancelled again:

import asyncio

async def sleeper():
    try:
        await asyncio.sleep(1)
    except BaseException:
        pass  # the first cancellation is caught here

    # This call will never return unless the task is cancelled again
    await asyncio.sleep(float("inf"))

async def main():
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(sleeper())
        await asyncio.sleep(0)  # ensure that the task reaches the first sleep()
        task.cancel()

    print("done")

# Execution hangs
asyncio.run(main())

Another issue is that if a task that has already been scheduled to resume with a value (that is, the `await` is about to yield a result) is cancelled, a [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "(in Python v3.14)") will instead be raised in the task’s coroutine when it resumes, thus potentially causing the awaitable result to be lost, even if the task catches the exception:

import asyncio

async def receive(f):
    print(await f)
    await asyncio.sleep(1)
    print("The task will be cancelled before this is printed")

async def main():
    f = asyncio.get_running_loop().create_future()
    task = asyncio.create_task(receive(f))
    await asyncio.sleep(0)  # make sure the task has started
    f.set_result("hello")
    task.cancel()

    # The "hello" result is lost due to the cancellation
    try:
        await task
    except asyncio.CancelledError:
        pass

# No output
asyncio.run(main())

Similarly, if a newly created task is cancelled, its coroutine function may never get to run and thus react to the cancellation. While the [asyncio documentation](https://docs.python.org/3/library/asyncio-task.html "(in Python v3.14)") claims that:

> Tasks can easily and safely be cancelled. When a task is cancelled, [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "(in Python v3.14)") will be raised in the task at the next opportunity.

This is simply **not true** for tasks that are cancelled before they have had a chance to start! This is problematic in cases where the newly launched task is responsible for managing a resource. If the task is cancelled without getting to handle the [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "(in Python v3.14)"), it won’t have a chance to close the managed resource:

import asyncio

class Resource:
    async def  __aenter__ (self):
        return self

    async def  __aexit__ (self, exc_type, exc_val, exc_tb):
        # Here would be the code that cleanly closes the resource
        print("closed")

async def handle_resource(resource):
    async with resource:
        ...

async def main():
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(handle_resource(Resource()))
        task.cancel()

# No output
asyncio.run(main())

Note

[`Eager task factories`](https://docs.python.org/3/library/asyncio-task.html#asyncio.eager_task_factory "(in Python v3.14)") and, likewise, tasks started with `eager_start=True` do not suffer from this particular issue, as there is no opportunity to cancel the task before its first iteration.

### Asyncio cancellation shielding is a major footgun[](https://anyio.readthedocs.io/en/stable/why.html#asyncio-cancellation-shielding-is-a-major-footgun "Link to this heading")

Asyncio has a function, [`asyncio.shield()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.shield "(in Python v3.14)"), to shield a coroutine from cancellation. It launches a new task in such a way that the cancellation of the task awaiting on it will not propagate to the new task.

The trouble with this is that if the host task (the task that awaits for the shielded operation to complete) **is** cancelled, the shielded task is orphaned. If the shielded task then raises an exception, only a warning might be printed on the console, but the exception will not propagate anywhere. Worse yet, since asyncio only holds weak references to each task, there is nothing preventing the shielded task from being garbage collected, mid-execution:

import asyncio
import gc

async def shielded_task():
    fut = asyncio.get_running_loop().create_future()
    await fut

async def host_task():
    await asyncio.shield(shielded_task())

async def main():
    async with asyncio.TaskGroup() as tg:
        task = tg.create_task(host_task())
        await asyncio.sleep(0)  # allow the host task to start
        task.cancel()
        await asyncio.sleep(0)  # allow the cancellation to take effect on the host task
        gc.collect()

# Prints warning: Task was destroyed but it is pending!
asyncio.run(main())

To make matters even worse, the shielding only prevents indirect cancellation through the host task. If the event loop is shut down, it will automatically cancel all tasks, including the supposedly shielded one:

import asyncio
import signal

async def finalizer():
    await asyncio.sleep(1)
    print("Finalizer done")

async def main():
    ...  # the business logic goes here
    asyncio.get_running_loop().call_soon(signal.raise_signal, signal.SIGINT)  # simulate ctrl+C
    await asyncio.shield(finalizer())

# Prints a traceback containing a KeyboardInterrupt and a CancelledError, but not the "Finalizer done" message
asyncio.run(main())

A good practical example of the issues with [`shield()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.shield "(in Python v3.14)") can be drawn from the [Python Redis client](https://github.com/redis/redis-py) where the incorrect use of this function was responsible for a [significant outage of ChatGPT](https://openai.com/index/march-20-chatgpt-outage/). The point here is not to lay blame on the downstream developers, but to demonstrate that [`shield()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.shield "(in Python v3.14)") is difficult, if not impossible, to use correctly for any practical purpose.

### How does AnyIO fix these problems?[](https://anyio.readthedocs.io/en/stable/why.html#id2 "Link to this heading")

To provide for more precise and predictable cancellation control, AnyIO (and [Trio](https://github.com/python-trio/trio)) uses _cancel scopes_. Cancel scopes select sections of a coroutine function to be cancelled. Cancel scopes are stateful in nature, meaning once a cancel scope has been cancelled, it will stay that way. On asyncio, AnyIO cancel scopes work by cancelling the enclosed task(s) every time they try to await on something as long as the task’s active cancel scope is _effectively cancelled_ (i.e. either directly or via an ancestor scope). This mechanism of stateful cancellation is called _level cancellation_.

AnyIO’s cancel scopes have two notable differences from asyncio’s cancellation:

1.   Cancel scopes never try to cancel a task when it’s scheduled to resume with a value

2.   Cancel scopes always allow the task a chance to react to the cancellation

In addition to providing the ability to cancel specific code sections, cancel scopes also provide two important features: shielding and timeouts.

Shielding a section of code from cancellation also works in a more straightforward fashion – not by launching another task, but by preventing the propagation of cancellation from parent cancel scope to a shielded scope.

Cancel scopes with a set _deadline_ are roughly equivalent to [`asyncio.timeout()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.timeout "(in Python v3.14)"), except for the level cancellation semantics and the ability to combine timeouts with shielding to easily implement finalization with a timeout. The [`move_on_after()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.move_on_after "anyio.move_on_after") context manager is often used for this purpose.

Note

Shielded cancel scopes only protect against cancellation by other cancel scopes, not direct calls to [`cancel()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel "(in Python v3.14)").

The first asyncio example above demonstrated how a task cancellation is only delivered once, unless explicitly repeated. But with AnyIO’s cancel scopes, every attempt to yield control to the event loop from a cancelled task results in a new [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "(in Python v3.14)"):

import asyncio

import anyio

async def sleeper():
    try:
        await asyncio.sleep(1)
    except BaseException:
        pass  # the first cancellation is caught here

    # This will raise another CancelledError
    await asyncio.sleep(float("inf"))

async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(sleeper)
        await asyncio.sleep(0)  # ensure that the task reaches the first sleep()
        tg.cancel_scope.cancel()

    print("done")

# Output: "done"
asyncio.run(main())

The AnyIO version of the second example demonstrates that a task which is scheduled to resume will be able to process the result of the `await` before it gets cancelled:

import asyncio

import anyio

async def receive(f):
    print(await f)
    await asyncio.sleep(1)
    print("The task will be cancelled before this is printed")

async def main():
    f = asyncio.get_running_loop().create_future()
    async with anyio.create_task_group() as tg:
        tg.start_soon(receive, f)
        await asyncio.sleep(0)  # make sure the task has started
        f.set_result("hello")
        tg.cancel_scope.cancel()

# Output: "hello"
asyncio.run(main())

The third example demonstrated that if a newly created task is cancelled, it would not get an opportunity to react to the cancellation. With AnyIO’s task groups, they do:

import asyncio

import anyio

class Resource:
    async def  __aenter__ (self):
        return self

    async def  __aexit__ (self, exc_type, exc_val, exc_tb):
        # Here would be the code that cleanly closes the resource
        print("closed")

async def handle_resource(resource):
    async with resource:
        ...

async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(handle_resource, Resource())
        tg.cancel_scope.cancel()

# Output: "closed"
asyncio.run(main())

Design problems with asyncio queues[](https://anyio.readthedocs.io/en/stable/why.html#design-problems-with-asyncio-queues "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

While the [`asyncio.Queue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "(in Python v3.14)") class was upgraded in Python 3.13 to support the notion of shutting down, there are still a number of issues with it:

1.   Queues are unbounded by default

2.   Queues don’t support async iteration

3.   Queue shutdown doesn’t play nice with multiple producers

The problem with unbounded queues is that careless use of such queues may cause runaway memory use and thus lead to out of memory errors. This default behavior is unfortunately unfixable due to backwards compatibility reasons.

The second problem is mostly an ergonomics issue. A PR was made to address this, but was [declined](https://github.com/python/cpython/pull/120925#issuecomment-2370151879).

The third problem manifests itself when multiple producer tasks put items to the same queue. If one producer shuts down the queue, the others will get unwarranted errors when trying to put more items to the queue. Therefore the producers either need another means to coordinate the queue shutdown, or they need to be launched in a task group in such a manner that the host task shuts down the queue after the producer tasks have exited. Either way, the design is not ideal for multiple producer tasks.

### How does AnyIO fix these problems?[](https://anyio.readthedocs.io/en/stable/why.html#queue-fix "Link to this heading")

AnyIO offers an alternative to queues: [memory object streams](https://anyio.readthedocs.io/en/stable/streams.html#memory-object-streams). They were modeled after Trio’s [memory channels](https://trio.readthedocs.io/en/stable/reference-core.html#using-channels-to-pass-values-between-tasks). When you create a memory object stream, you get a “send” stream and a “receive” stream. The separation is necessary for the purpose of cloning (explained below). By default, memory object streams have an item capacity of 0, meaning the stream does not store anything. In other words, a send operation will not complete until another task shows up to receive the item.

Memory object streams support cloning. This enables each consumer and producer task to close its own clone of the receive or send stream. Only after all clones have been closed is the respective send or receive memory object stream considered to be closed.

Unlike [`asyncio.Queue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "(in Python v3.14)"), memory object receive streams support async iteration. The `async for` loop then ends naturally when all send stream clones have been closed. For send streams, attempting to send an item when all receive stream clones have been closed raises a [`BrokenResourceError`](https://anyio.readthedocs.io/en/stable/api.html#anyio.BrokenResourceError "anyio.BrokenResourceError").

Memory object streams also provide better debugging facilities via the [`statistics()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream.statistics "anyio.streams.memory.MemoryObjectReceiveStream.statistics") method which can tell you:

*   the number of queued items

*   the number of open send and receive streams

*   how many tasks are waiting to send or receive to/from the stream

Design problems with the streams API[](https://anyio.readthedocs.io/en/stable/why.html#design-problems-with-the-streams-api "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

While asyncio provides a limited set of [stream classes](https://docs.python.org/3/library/asyncio-stream.html), their callback-based design unfortunately shines through from the API. First of all, unlike regular sockets, you get a separate reader and writer object instead of a full-duplex stream which you would essentially get from the [`socket`](https://docs.python.org/3/library/socket.html#module-socket "(in Python v3.14)") functions. Second, in order to send data to the stream, you have to first call the synchronous [`write()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.write "(in Python v3.14)") method which adds data to the internal buffer, and then you have to remember to call the coroutine method [`drain()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.drain "(in Python v3.14)") which then _actually_ causes the data to be written to the underlying socket. Likewise, when you close a stream, you first have to call [`close()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.close "(in Python v3.14)") and _then_ await on [`wait_closed()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.wait_closed "(in Python v3.14)") to make sure the stream has _actually_ closed! To add insult to injury, these classes don’t even support the async context manager protocol so you can’t just do `async with writer: ...`.

Another issue lies with the [`get_extra_info()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.get_extra_info "(in Python v3.14)") method asyncio provides to get information like the remote address for socket connections, or the raw socket object:

1.   This method only exists in the writer class, not the reader (for whatever reason).

2.   It returns a dictionary, so to get the information you want, you’ll need to access one of the keys in the returned dict, based on the documentation.

3.   It is not type safe, as Typeshed specifies the return type as `dict[str, Any]`. Therefore, static type checkers cannot check the correctness of any access to the returned dict based on either the keys or the value types.

### How does AnyIO fix these problems?[](https://anyio.readthedocs.io/en/stable/why.html#id4 "Link to this heading")

AnyIO comes with hierarchy of base stream classes:

*   [`UnreliableObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectStream "anyio.abc.UnreliableObjectStream"), [`UnreliableObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectReceiveStream "anyio.abc.UnreliableObjectReceiveStream") and [`UnreliableObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.UnreliableObjectSendStream "anyio.abc.UnreliableObjectSendStream"): for transporting objects; no guarantees of reliable or ordered delivery, just like with UDP sockets

*   [`ObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectStream "anyio.abc.ObjectStream"), [`ObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectReceiveStream "anyio.abc.ObjectReceiveStream"), [`ObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ObjectSendStream "anyio.abc.ObjectSendStream"): like the above, but with added guarantees about reliable and ordered delivery

*   [`ByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteStream "anyio.abc.ByteStream"), [`ByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteReceiveStream "anyio.abc.ByteReceiveStream"), [`ByteSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.ByteSendStream "anyio.abc.ByteSendStream"): for transporting bytes; may split chunks arbitrarily, just like TCP sockets

*   [`SocketStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.abc.SocketStream "anyio.abc.SocketStream"): byte streams backed by actual sockets

These interfaces are then implemented by a number of concrete classes, such as:

*   [`MemoryObjectReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectReceiveStream "anyio.streams.memory.MemoryObjectReceiveStream") and [`MemoryObjectSendStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.memory.MemoryObjectSendStream "anyio.streams.memory.MemoryObjectSendStream"): for exchanging arbitrary objects between tasks within the same process (see [this section](https://anyio.readthedocs.io/en/stable/why.html#queue-fix) for the rationale for the sender/receiver split)

*   [`BufferedByteReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteReceiveStream "anyio.streams.buffered.BufferedByteReceiveStream") and [`BufferedByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.buffered.BufferedByteStream "anyio.streams.buffered.BufferedByteStream"): for adapting bytes-oriented object streams into byte streams, and for supporting read operations that require a buffer, such as needing to read a precise amount of bytes, or reading up to a specific delimiter

*   [`TLSStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "anyio.streams.tls.TLSStream"): for using TLS encryption over any arbitrary (bytes-oriented) stream

*   [`TextReceiveStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextReceiveStream "anyio.streams.text.TextReceiveStream") and [`TextStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.text.TextStream "anyio.streams.text.TextStream"): for turning a bytes-oriented stream into a unicode string-oriented stream

*   [`FileReadStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileReadStream "anyio.streams.file.FileReadStream") and [`FileWriteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.file.FileWriteStream "anyio.streams.file.FileWriteStream"): for reading from or writing to files

*   [`StapledObjectStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledObjectStream "anyio.streams.stapled.StapledObjectStream") and [`StapledByteStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.stapled.StapledByteStream "anyio.streams.stapled.StapledByteStream"): for combining different read and write streams into full-duplex streams

Important

In contrast with regular sockets or asyncio streams, AnyIO streams raise [`EndOfStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.EndOfStream "anyio.EndOfStream") instead of returning an empty bytes object or `None` when there is no more data to be read.

As a counterpart to [`get_extra_info()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.get_extra_info "(in Python v3.14)"), AnyIO offers a system of typed attributes where stream classes (and any kind of class, really) can offer such extra information in a type safe manner. This is especially useful with stream wrappers such as [`TLSStream`](https://anyio.readthedocs.io/en/stable/api.html#anyio.streams.tls.TLSStream "anyio.streams.tls.TLSStream"). Stream wrapper classes like that can pass through any typed attributes from the wrapped stream while adding their own on top. They can also choose to just override any attributes they like, all the while preserving type safety.

Design problems with the thread API[](https://anyio.readthedocs.io/en/stable/why.html#design-problems-with-the-thread-api "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

Asyncio comes with two ways to call blocking code in worker threads, each with its own caveats:

1.   [`asyncio.to_thread()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread "(in Python v3.14)")

2.   [`asyncio.loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "(in Python v3.14)")

The first function is the more modern one, and supports [`contextvar`](https://docs.python.org/3/library/contextvars.html#module-contextvars "(in Python v3.14)") propagation. However, there is no way to use it with a thread pool executor other than the default. And due to the design decision of allowing the pass-through of arbitrary positional and keyword arguments, no such option can ever be added without breaking backwards compatibility. The second function, on the other hand, allows for explicitly specifying a thread pool to use, but it doesn’t support context variable propagation.

Another inconvenience comes from the inability to synchronously call synchronous functions in the event loop thread from a worker thread. That is, running a synchronous function in the event loop thread and then returning its return value from that call. While asyncio provides a way to do this for coroutine functions ([`run_coroutine_threadsafe()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "(in Python v3.14)")), there is no counterpart for synchronous functions. The closest match would be [`call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "(in Python v3.14)"), this function only schedules a callback to be run on the event loop thread and does not provide any means to retrieve the return value.

### How does AnyIO fix these problems?[](https://anyio.readthedocs.io/en/stable/why.html#id5 "Link to this heading")

AnyIO uses its own thread pooling mechanism, based on [capacity limiters](https://anyio.readthedocs.io/en/stable/synchronization.html#capacity-limiters) which are similar to semaphores. To call a function in a worker thread, you would use [`to_thread.run_sync()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_thread.run_sync "anyio.to_thread.run_sync"). This function can be passed a specific capacity limiter to count against. All worker threads will be spawned in a thread pool specific to the current event loop, and can be reused in any call to [`to_thread.run_sync()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.to_thread.run_sync "anyio.to_thread.run_sync"), regardless of the capacity limiter used. More worker threads will be spawned as necessary, so long as the capacity limiter allows it. The event loop’s thread pool is homogeneous, meaning idle threads in it are reused regardless of which capacity limiter was passed to the call that spawned them.

From inside AnyIO worker threads, you can call functions in the event loop thread using [`from_thread.run()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.run "anyio.from_thread.run") and [`from_thread.run_sync()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.from_thread.run_sync "anyio.from_thread.run_sync"), for coroutine functions and synchronous functions, respectively. The former is a direct counterpart to asyncio’s [`run_coroutine_threadsafe()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "(in Python v3.14)"), but the latter will wait for the function to run and return its return value, unlike [`call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "(in Python v3.14)").

Design problems with signal handling APIs[](https://anyio.readthedocs.io/en/stable/why.html#design-problems-with-signal-handling-apis "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Asyncio only provides facilities to set or remove signal handlers. The [`add_signal_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "(in Python v3.14)") method will replace any existing handler for that signal, and won’t return the previous handler for potential chaining. There is also no way to get the current handler for a signal.

AnyIO provides an alternate mechanism to handle signals with its [`open_signal_receiver()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.open_signal_receiver "anyio.open_signal_receiver") context manager.

Missing file I/O and async path support[](https://anyio.readthedocs.io/en/stable/why.html#missing-file-i-o-and-async-path-support "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Asyncio contains no facilities to help with file I/O, forcing you to use [`to_thread()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread "(in Python v3.14)") or [`run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "(in Python v3.14)") with every single file operation to prevent blocking the event loop thread.

To overcome this shortcoming, users often turn to libraries such as [aiofiles](https://github.com/Tinche/aiofiles) and [aiopath](https://github.com/alexdelorenzo/aiopath) which offer async interfaces for file and path access. However, AnyIO provides its own set of async file I/O APIs, including an async compatible counterpart for the [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") class. Additionally, it should be noted that AnyIO provides [file streams](https://anyio.readthedocs.io/en/stable/streams.html#filestreams) compatible with its stream class hierarchy.

Features not in asyncio which you might be interested in[](https://anyio.readthedocs.io/en/stable/why.html#features-not-in-asyncio-which-you-might-be-interested-in "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

AnyIO doesn’t just offer replacements for asyncio APIs, but provides a bunch of its own conveniences which you may find helpful.

### Built-in pytest plugin[](https://anyio.readthedocs.io/en/stable/why.html#built-in-pytest-plugin "Link to this heading")

AnyIO contains its own [pytest](https://docs.pytest.org/) plugin for running asynchronous tests. It can completely replace [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) for testing asynchronous code. It is somewhat simpler to use too, in addition to supporting more event loop implementations such as [Trio](https://github.com/python-trio/trio).

### Connectables[](https://anyio.readthedocs.io/en/stable/why.html#connectables "Link to this heading")

To complement its stream class hierarchy, AnyIO offers an abstraction for producing connected streams, either object or bytes-oriented. This can be very useful when writing network clients, as abstracting out the connection mechanism allows for a lot of customization, including mocking connections without having to resort to monkey patching.

### Context manager mix-in classes[](https://anyio.readthedocs.io/en/stable/why.html#context-manager-mix-in-classes "Link to this heading")

AnyIO provides mix-in classes for safely implementing context managers which embed other context managers. Typically this would require implementing `__aenter__` and `__aexit__`, often requiring these classes to store state in the instance and dealing with exceptions raised in `__aenter__()`. The context manager mix-ins allow you to replace these method pairs with a single method where you write your logic just like with [`@asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager "(in Python v3.14)"), albeit at the cost of sacrificing re-entrancy.

### Asynchronous functools[](https://anyio.readthedocs.io/en/stable/why.html#asynchronous-functools "Link to this heading")

The [`functools`](https://docs.python.org/3/library/functools.html#module-functools "(in Python v3.14)") module does not support coroutine functions, so AnyIO offers its own version that does. See [Asynchronous functools](https://anyio.readthedocs.io/en/stable/api.html#async-functools) for the list of implemented functions.
