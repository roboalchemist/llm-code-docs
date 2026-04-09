# Scheduler

The scheduler component receives requests from the engine
and stores them into persistent and/or non-persistent data structures.
It also gets those requests and feeds them back to the engine when it
asks for a next request to be downloaded.

## Overriding the default scheduler

You can use your own custom scheduler class by supplying its full
Python path in the `SCHEDULER` setting.

## Minimal scheduler interface

*class *scrapy.core.scheduler.BaseScheduler

The scheduler component is responsible for storing requests received
from the engine, and feeding them back upon request (also to the engine).

The original sources of said requests are:

- 

Spider: `start` method, requests created for URLs in the `start_urls` attribute, request callbacks

- 

Spider middleware: `process_spider_output` and `process_spider_exception` methods

- 

Downloader middleware: `process_request`, `process_response` and `process_exception` methods

The order in which the scheduler returns its stored requests (via the `next_request` method)
plays a great part in determining the order in which those requests are downloaded. See Request order.

The methods defined in this class constitute the minimal interface that the Scrapy engine will interact with.

close(*reason: str [https://docs.python.org/3/library/stdtypes.html#str]*) → Deferred [https://docs.twisted.org/en/stable/api/twisted.internet.defer.Deferred.html][None [https://docs.python.org/3/library/constants.html#None]] | None [https://docs.python.org/3/library/constants.html#None]

Called when the spider is closed by the engine. It receives the reason why the crawl
finished as argument and it’s useful to execute cleaning code.

Parameters:

**reason** (`str` [https://docs.python.org/3/library/stdtypes.html#str]) – a string which describes the reason why the spider was closed

*abstract *enqueue_request(*request: Request*) → bool [https://docs.python.org/3/library/functions.html#bool]

Process a request received by the engine.

Return `True` if the request is stored correctly, `False` otherwise.

If `False`, the engine will fire a `request_dropped` signal, and
will not make further attempts to schedule the request at a later time.
For reference, the default Scrapy scheduler returns `False` when the
request is rejected by the dupefilter.

*classmethod *from_crawler(*crawler: Crawler*) → Self

Factory method which receives the current `Crawler` object as argument.

*abstract *has_pending_requests() → bool [https://docs.python.org/3/library/functions.html#bool]

`True` if the scheduler has enqueued requests, `False` otherwise

*abstract *next_request() → Request | None [https://docs.python.org/3/library/constants.html#None]

Return the next `Request` to be processed, or `None`
to indicate that there are no requests to be considered ready at the moment.

Returning `None` implies that no request from the scheduler will be sent
to the downloader in the current reactor cycle. The engine will continue
calling `next_request` until `has_pending_requests` is `False`.

open(*spider: Spider*) → Deferred [https://docs.twisted.org/en/stable/api/twisted.internet.defer.Deferred.html][None [https://docs.python.org/3/library/constants.html#None]] | None [https://docs.python.org/3/library/constants.html#None]

Called when the spider is opened by the engine. It receives the spider
instance as argument and it’s useful to execute initialization code.

Parameters:

**spider** (`Spider`) – the spider object for the current crawl

## Default scheduler

*class *scrapy.core.scheduler.Scheduler

Default scheduler.

Requests are stored into priority queues
(`SCHEDULER_PRIORITY_QUEUE`) that sort requests by
`priority`.

By default, a single, memory-based priority queue is used for all requests.
When using `JOBDIR`, a disk-based priority queue is also created,
and only unserializable requests are stored in the memory-based priority
queue. For a given priority value, requests in memory take precedence over
requests in disk.

Each priority queue stores requests in separate internal queues, one per
priority value. The memory priority queue uses
`SCHEDULER_MEMORY_QUEUE` queues, while the disk priority queue
uses `SCHEDULER_DISK_QUEUE` queues. The internal queues determine
request order when requests have the same priority.
Start requests are stored into separate internal
queues by default, and ordered differently.

Duplicate requests are filtered out with an instance of
`DUPEFILTER_CLASS`.

### Request order

With default settings, pending requests are stored in a LIFO [https://en.wikipedia.org/wiki/Stack_(abstract_data_type)] queue
(except for start requests). As a result,
crawling happens in DFO order [https://en.wikipedia.org/wiki/Depth-first_search], which is usually the most convenient
crawl order. However, you can enforce BFO or a custom
order (except for the first few requests).

#### Start request order

Start requests are sent in the order they are
yielded from `start()`, and given the same
`priority`, other requests take precedence over
start requests.

You can set `SCHEDULER_START_MEMORY_QUEUE` and
`SCHEDULER_START_DISK_QUEUE` to `None` to handle start requests
the same as other requests when it comes to order and priority.

#### Crawling in BFO order

If you do want to crawl in BFO order [https://en.wikipedia.org/wiki/Breadth-first_search], you can do it by setting the
following settings:

`DEPTH_PRIORITY` = `1`