# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html

Title: kombu.asynchronous.semaphore — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.asynchronous.semaphore.html).

Semaphores - `kombu.asynchronous.semaphore`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#semaphores-kombu-asynchronous-semaphore "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Semaphores and concurrency primitives.

_class_ kombu.asynchronous.semaphore.DummyLock[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/semaphore.html#DummyLock)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#kombu.asynchronous.semaphore.DummyLock "Link to this definition")
Pretending to be a lock.

_class_ kombu.asynchronous.semaphore.LaxBoundedSemaphore(_value:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/semaphore.html#LaxBoundedSemaphore)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#kombu.asynchronous.semaphore.LaxBoundedSemaphore "Link to this definition")
Asynchronous Bounded Semaphore.

Lax means that the value will stay within the specified range even if released more times than it was acquired.

Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#example "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

>>> x = LaxBoundedSemaphore(2)

>>> x.acquire(print, 'HELLO 1')
HELLO 1

>>> x.acquire(print, 'HELLO 2')
HELLO 2

>>> x.acquire(print, 'HELLO 3')
>>> x._waiters   # private, do not access directly
[print, ('HELLO 3',)]

>>> x.release()
HELLO 3

acquire(_callback:Callable[P,[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")]_, _*partial\_args:P.args_, _**partial\_kwargs:P.kwargs_)→[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/semaphore.html#LaxBoundedSemaphore.acquire)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#kombu.asynchronous.semaphore.LaxBoundedSemaphore.acquire "Link to this definition")
Acquire semaphore.

This will immediately apply `callback` if the resource is available, otherwise the callback is suspended until the semaphore is released.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#arguments "Link to this heading")

> callback (Callable): The callback to apply. [*](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#id1)partial_args (Any): partial arguments to callback.

clear()→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/semaphore.html#LaxBoundedSemaphore.clear)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#kombu.asynchronous.semaphore.LaxBoundedSemaphore.clear "Link to this definition")
Reset the semaphore, which also wipes out any waiting callbacks.

grow(_n:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")=1_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/semaphore.html#LaxBoundedSemaphore.grow)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#kombu.asynchronous.semaphore.LaxBoundedSemaphore.grow "Link to this definition")
Change the size of the semaphore to accept more users.

release()→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/semaphore.html#LaxBoundedSemaphore.release)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#kombu.asynchronous.semaphore.LaxBoundedSemaphore.release "Link to this definition")
Release semaphore.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#note "Link to this heading")

> If there are any waiters this will apply the first waiter that is waiting for the resource (FIFO order).

shrink(_n:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")=1_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/semaphore.html#LaxBoundedSemaphore.shrink)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.semaphore.html#kombu.asynchronous.semaphore.LaxBoundedSemaphore.shrink "Link to this definition")
Change the size of the semaphore to accept less users.
