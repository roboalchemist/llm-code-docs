# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html

Title: Logical Clocks and Synchronization - kombu.clocks — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.clocks.html).

Logical Clocks and Synchronization.

_class_ kombu.clocks.LamportClock(_initial\_value:int=0_, _Lock:type[~\_thread.allocate\_lock]=<built-in function allocate\_lock>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/clocks.html#LamportClock)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.LamportClock "Link to this definition")
Lamport’s logical clock.

From Wikipedia:

A Lamport logical clock is a monotonically incrementing software counter maintained in each process. It follows some simple rules:

> *   A process increments its counter before each event in that process;
> 
> *   When a process sends a message, it includes its counter value with the message;
> 
> *   On receiving a message, the receiver process sets its counter to be greater than the maximum of its own value and the received value before it considers the message received.

Conceptually, this logical clock can be thought of as a clock that only has meaning in relation to messages moving between processes. When a process receives a message, it resynchronizes its logical clock with the sender.

_Usage_

When sending a message use [`forward()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.LamportClock.forward "kombu.clocks.LamportClock.forward") to increment the clock, when receiving a message use [`adjust()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.LamportClock.adjust "kombu.clocks.LamportClock.adjust") to sync with the time stamp of the incoming message.

adjust(_other:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_)→[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/clocks.html#LamportClock.adjust)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.LamportClock.adjust "Link to this definition")forward()→[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/clocks.html#LamportClock.forward)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.LamportClock.forward "Link to this definition")sort_heap(_h:[list](https://docs.python.org/dev/library/stdtypes.html#list "(in Python v3.15)")[[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")]]_)→[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)"),[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")][[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/clocks.html#LamportClock.sort_heap)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.LamportClock.sort_heap "Link to this definition")
Sort heap of events.

List of tuples containing at least two elements, representing an event, where the first element is the event’s scalar clock value, and the second element is the id of the process (usually `"hostname:pid"`): `sh([(clock, processid, ...?), (...)])`

The list must already be sorted, which is why we refer to it as a heap.

The tuple will not be unpacked, so more than two elements can be present.

Will return the latest event.

value _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.LamportClock.value "Link to this definition")
The clocks current value.

_class_ kombu.clocks.timetuple(_clock:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")_, _timestamp:[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")_, _id:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _obj:Any=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/clocks.html#timetuple)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.timetuple "Link to this definition")
Tuple of event clock information.

Can be used as part of a heap to keep events ordered.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#arguments "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

> clock (Optional[int]): Event clock value. timestamp (float): Event UNIX timestamp value. id (str): Event host id (e.g. `hostname:pid`). obj (Any): Optional obj to associate with this event.

_property_ clock[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.timetuple.clock "Link to this definition")
itemgetter(item, …) –> itemgetter object

Return a callable object that fetches the given item(s) from its operand. After f = itemgetter(2), the call f(r) returns r[2]. After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])

_property_ id[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.timetuple.id "Link to this definition")
itemgetter(item, …) –> itemgetter object

Return a callable object that fetches the given item(s) from its operand. After f = itemgetter(2), the call f(r) returns r[2]. After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])

_property_ obj[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.timetuple.obj "Link to this definition")
itemgetter(item, …) –> itemgetter object

Return a callable object that fetches the given item(s) from its operand. After f = itemgetter(2), the call f(r) returns r[2]. After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])

_property_ timestamp[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.clocks.html#kombu.clocks.timetuple.timestamp "Link to this definition")
itemgetter(item, …) –> itemgetter object

Return a callable object that fetches the given item(s) from its operand. After f = itemgetter(2), the call f(r) returns r[2]. After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
