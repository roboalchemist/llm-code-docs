# Source: https://curio.readthedocs.io/

Title: Curio — Curio 1.2 documentation

URL Source: https://curio.readthedocs.io/

Markdown Content:
Curio is a coroutine-based library for concurrent Python systems programming. It provides standard programming abstractions such as as tasks, sockets, files, locks, and queues. You’ll find it to be familiar, small, fast, and fun.

Curio is the work of David Beazley ([https://www.dabeaz.com](https://www.dabeaz.com/)), who has been teaching and talking about concurrency related topics for more than 20 years, both as a university professor and as an independent researcher.

Requirements[¶](https://curio.readthedocs.io/#requirements "Permalink to this headline")
----------------------------------------------------------------------------------------

Curio requires Python 3.7 or newer. It has no third-party dependencies and works on both POSIX and Windows.

Documentation[¶](https://curio.readthedocs.io/#documentation "Permalink to this headline")
------------------------------------------------------------------------------------------

*   [A Tutorial Introduction](https://curio.readthedocs.io/en/latest/tutorial.html)
    *   [Getting Started](https://curio.readthedocs.io/en/latest/tutorial.html#getting-started)
    *   [Tasks and Concurrency](https://curio.readthedocs.io/en/latest/tutorial.html#tasks-and-concurrency)
    *   [Task Groups](https://curio.readthedocs.io/en/latest/tutorial.html#task-groups)
    *   [Long-Running Operations](https://curio.readthedocs.io/en/latest/tutorial.html#long-running-operations)
    *   [An Echo Server](https://curio.readthedocs.io/en/latest/tutorial.html#an-echo-server)
    *   [Intertask Communication](https://curio.readthedocs.io/en/latest/tutorial.html#intertask-communication)
    *   [A Chat Server](https://curio.readthedocs.io/en/latest/tutorial.html#a-chat-server)
    *   [Programming Advice](https://curio.readthedocs.io/en/latest/tutorial.html#programming-advice)
    *   [Debugging Tips](https://curio.readthedocs.io/en/latest/tutorial.html#debugging-tips)
    *   [More Information](https://curio.readthedocs.io/en/latest/tutorial.html#more-information)

*   [How-To](https://curio.readthedocs.io/en/latest/howto.html)
    *   [How do you write a TCP server?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-write-a-tcp-server)
    *   [How do you write a UDP Server?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-write-a-udp-server)
    *   [How do you make an outgoing connection?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-make-an-outgoing-connection)
    *   [How do you write an SSL-enabled server?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-write-an-ssl-enabled-server)
    *   [How do you perform a blocking operation?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-perform-a-blocking-operation)
    *   [How do you perform a CPU intensive operation?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-perform-a-cpu-intensive-operation)
    *   [How do you apply a timeout?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-apply-a-timeout)
    *   [How can a timeout be applied to a block of statements?](https://curio.readthedocs.io/en/latest/howto.html#how-can-a-timeout-be-applied-to-a-block-of-statements)
    *   [How do you shield operations from timeouts or cancellation?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-shield-operations-from-timeouts-or-cancellation)
    *   [How can tasks communicate?](https://curio.readthedocs.io/en/latest/howto.html#how-can-tasks-communicate)
    *   [How can a task and a thread communicate?](https://curio.readthedocs.io/en/latest/howto.html#how-can-a-task-and-a-thread-communicate)
    *   [How can synchronous code set an asynchronous event?](https://curio.readthedocs.io/en/latest/howto.html#how-can-synchronous-code-set-an-asynchronous-event)
    *   [How do you catch signals?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-catch-signals)
    *   [How do you run external commands in a subprocess?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-run-external-commands-in-a-subprocess)
    *   [How can you communicate with a subprocess over a pipe?](https://curio.readthedocs.io/en/latest/howto.html#how-can-you-communicate-with-a-subprocess-over-a-pipe)
    *   [How can two different Python interpreters send messages to each other?](https://curio.readthedocs.io/en/latest/howto.html#how-can-two-different-python-interpreters-send-messages-to-each-other)
    *   [How does a coroutine get its enclosing Task instance?](https://curio.readthedocs.io/en/latest/howto.html#how-does-a-coroutine-get-its-enclosing-task-instance)
    *   [How do you use contextvars?](https://curio.readthedocs.io/en/latest/howto.html#how-do-you-use-contextvars)

*   [Reference Manual](https://curio.readthedocs.io/en/latest/reference.html)
    *   [Coroutines](https://curio.readthedocs.io/en/latest/reference.html#coroutines)
    *   [Basic Execution](https://curio.readthedocs.io/en/latest/reference.html#basic-execution)
    *   [Tasks](https://curio.readthedocs.io/en/latest/reference.html#tasks)
    *   [Task Groups](https://curio.readthedocs.io/en/latest/reference.html#task-groups)
    *   [Time](https://curio.readthedocs.io/en/latest/reference.html#time)
    *   [Timeouts](https://curio.readthedocs.io/en/latest/reference.html#timeouts)
    *   [Cancellation Control](https://curio.readthedocs.io/en/latest/reference.html#cancellation-control)
    *   [Synchronization Primitives](https://curio.readthedocs.io/en/latest/reference.html#synchronization-primitives)
    *   [Queues](https://curio.readthedocs.io/en/latest/reference.html#queues)
    *   [Universal Synchronizaton](https://curio.readthedocs.io/en/latest/reference.html#universal-synchronizaton)
    *   [Blocking Operations and External Work](https://curio.readthedocs.io/en/latest/reference.html#blocking-operations-and-external-work)
    *   [I/O Classes](https://curio.readthedocs.io/en/latest/reference.html#i-o-classes)
    *   [Networking](https://curio.readthedocs.io/en/latest/reference.html#networking)
    *   [Subprocesses](https://curio.readthedocs.io/en/latest/reference.html#subprocesses)
    *   [Asynchronous Threads](https://curio.readthedocs.io/en/latest/reference.html#asynchronous-threads)
    *   [Scheduler Activations](https://curio.readthedocs.io/en/latest/reference.html#scheduler-activations)
    *   [Asynchronous Metaprogramming](https://curio.readthedocs.io/en/latest/reference.html#asynchronous-metaprogramming)
    *   [Exceptions](https://curio.readthedocs.io/en/latest/reference.html#exceptions)
    *   [Low-level Traps and Scheduling](https://curio.readthedocs.io/en/latest/reference.html#low-level-traps-and-scheduling)
    *   [Debugging and Diagnostics](https://curio.readthedocs.io/en/latest/reference.html#debugging-and-diagnostics)

Curio University[¶](https://curio.readthedocs.io/#curio-university "Permalink to this headline")
------------------------------------------------------------------------------------------------

Curio is based on ideas resulting from more than 12 years of exploration into various facets of Python’s concurrency and coroutine model. Dave has given numerous talks/tutorials on this topic at PyCon and elsewhere. Here is a detailed list of presentations to help you understand how Curio works and some of the system thinking that has gone into it. All of these talks are more general than Curio–you’ll learn a lot about Python concurrency in general.

*   [Build Your Own Async](https://www.youtube.com/watch?v=Y4Gt3Xjd7G8)Workshop talk at PyCon India, 2019. This workshop talks about the fundamentals of building a simple async concurrency library from scratch using both callbacks and coroutines.
*   [Die Threads](https://www.youtube.com/watch?v=U66KuyD3T0M)Keynote talk at EuroPython, 2018. Asynchronous programming is most commonly described as an alternative to thread programming. But what if you reinvented thread programming run on top of asynchronous programming? This talk explores this concept. It might be the most “experimental” talk related to Curio.
*   [The Other Async (Threads + Asyncio = Love)](https://www.youtube.com/watch?v=x1ndXuw7S0s)Keynote talk at PyGotham, 2017. This talk steps through the thinking and design of building a so-called “Universal Queue” that works with both async programs and threads using a common programming interface.
*   [Fear and Awaiting in Async](https://www.youtube.com/watch?v=E-1Y4kSsAFc)Keynote talk at PyOhio 2016. A no-holds-barred tour through the possibilities that await programmers who embrace the new async/await syntax in Python. Covers the basics of coroutines, async iteration, async context managers, and a lot of advanced metaprogramming including decorators, descriptors, and metaclasses. Also discusses the importance of API design in async programming.
*   [Topics of Interest (Async)](https://www.youtube.com/watch?v=ZzfHjytDceU)Keynote talk at Python Brasil 2015. Perhaps the first “Curio” talk. A small concurrency library similar to Curio is live-coded and discussed along with other topics related to async.
*   [Python Concurrency from the Ground Up (LIVE)](https://www.youtube.com/watch?v=MCs5OvhV9S4)Conference talk at PyCon 2015. This live-coded talk discusses threads, generators, coroutines, the Global Interpreter Lock (GIL), and more.
*   [Understanding the Python GIL](https://www.youtube.com/watch?v=Obt-vMVdM8s)Conference talk from PyCon 2010. Understand the inner workings of the infamous Global Interpreter Lock and how it impacts thread performance. See also this related [talk](https://www.youtube.com/watch?v=5jbG7UKT1l4) from the RuPy 2011 conference.
*   [A Curious Course on Coroutines and Concurrency](https://www.youtube.com/watch?v=Z_OAlIhXziw) [[Materials](https://www.dabeaz.com/coroutines)]Tutorial at PyCon 2009. Coroutines were first introduced in Python 2.5. This tutorial explores the foundations of using coroutines for various problems in data processing and concurrency. This tutorial gives much of the background that led to the current incarnation of Python coroutines.
*   [An Introduction to Python Concurrency](https://speakerdeck.com/dabeaz/an-introduction-to-python-concurrency)Tutorial at USENIX Technical Conference, 2009. A comprehensive overview of concurrency programming in Python. Includes threads, processes, and event-driven I/O. A good overview of basic programming concepts.
