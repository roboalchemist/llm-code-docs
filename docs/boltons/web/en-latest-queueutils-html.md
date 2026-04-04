# Source: https://boltons.readthedocs.io/en/latest/queueutils.html

Title: Priority queues — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/queueutils.html

Markdown Content:
`queueutils` - Priority queues[](https://boltons.readthedocs.io/en/latest/queueutils.html#module-boltons.queueutils "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

Python comes with a many great data structures, from [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") to [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "(in Python v3.14)"), and no shortage of serviceable algorithm implementations, from [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "(in Python v3.14)") to [`bisect`](https://docs.python.org/3/library/bisect.html#module-bisect "(in Python v3.14)"). But priority queues are curiously relegated to an example documented in [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq "(in Python v3.14)"). Even there, the approach presented is not full-featured and object-oriented. There is a built-in priority queue, `Queue.PriorityQueue`, but in addition to its austere API, it carries the double-edged sword of threadsafety, making it fine for multi-threaded, multi-consumer applications, but high-overhead for cooperative/single-threaded use cases.

The `queueutils` module currently provides two Queue implementations: [`HeapPriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.HeapPriorityQueue "boltons.queueutils.HeapPriorityQueue"), based on a heap, and [`SortedPriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.SortedPriorityQueue "boltons.queueutils.SortedPriorityQueue"), based on a sorted list. Both use a unified API based on [`BasePriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue "boltons.queueutils.BasePriorityQueue") to facilitate testing the slightly different performance characteristics on various application use cases.

>>> pq = PriorityQueue()
>>> pq.add('low priority task', 0)
>>> pq.add('high priority task', 2)
>>> pq.add('medium priority task 1', 1)
>>> pq.add('medium priority task 2', 1)
>>> len(pq)
4
>>> pq.pop()
'high priority task'
>>> pq.peek()
'medium priority task 1'
>>> len(pq)
3

_class_ boltons.queueutils.BasePriorityQueue(_**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/queueutils.html#BasePriorityQueue)[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue "Link to this definition")
The abstract base class for the other PriorityQueues in this module. Override the `_backend_type` class attribute, as well as the `_push_entry()` and `_pop_entry()` staticmethods for custom subclass behavior. (Don’t forget to use [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod "(in Python v3.14)")).

Parameters:
**priority_key** (_callable_) – A function that takes _priority_ as passed in by [`add()`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue.add "boltons.queueutils.BasePriorityQueue.add") and returns a real number representing the effective priority.

add(_task_, _priority=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/queueutils.html#BasePriorityQueue.add)[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue.add "Link to this definition")
Add a task to the queue, or change the _task_’s priority if _task_ is already in the queue. _task_ can be any hashable object, and _priority_ defaults to `0`. Higher values representing higher priority, but this behavior can be controlled by setting _priority\_key_ in the constructor.

peek(_default=\_REMOVED_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/queueutils.html#BasePriorityQueue.peek)[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue.peek "Link to this definition")
Read the next value in the queue without removing it. Returns _default_ on an empty queue, or raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") if _default_ is not set.

pop(_default=\_REMOVED_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/queueutils.html#BasePriorityQueue.pop)[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue.pop "Link to this definition")
Remove and return the next value in the queue. Returns _default_ on an empty queue, or raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") if _default_ is not set.

remove(_task_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/queueutils.html#BasePriorityQueue.remove)[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue.remove "Link to this definition")
Remove a task from the priority queue. Raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") if the _task_ is absent.

_class_ boltons.queueutils.HeapPriorityQueue(_**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/queueutils.html#HeapPriorityQueue)[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.HeapPriorityQueue "Link to this definition")
A priority queue inherited from [`BasePriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue "boltons.queueutils.BasePriorityQueue"), backed by a list and based on the [`heapq.heappop()`](https://docs.python.org/3/library/heapq.html#heapq.heappop "(in Python v3.14)") and [`heapq.heappush()`](https://docs.python.org/3/library/heapq.html#heapq.heappush "(in Python v3.14)") functions in the built-in [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq "(in Python v3.14)") module.

boltons.queueutils.PriorityQueue[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.PriorityQueue "Link to this definition")
alias of [`SortedPriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.SortedPriorityQueue "boltons.queueutils.SortedPriorityQueue")

_class_ boltons.queueutils.SortedPriorityQueue(_**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/queueutils.html#SortedPriorityQueue)[](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.SortedPriorityQueue "Link to this definition")
A priority queue inherited from [`BasePriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue "boltons.queueutils.BasePriorityQueue"), based on the [`bisect.insort()`](https://docs.python.org/3/library/bisect.html#bisect.insort "(in Python v3.14)") approach for in-order insertion into a sorted list.
