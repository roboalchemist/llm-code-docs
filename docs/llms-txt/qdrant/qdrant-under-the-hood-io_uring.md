# Qdrant under the hood: io\_uring

Andre Bogus

·

June 21, 2023

![Qdrant under the hood: io_uring](https://qdrant.tech/articles_data/io_uring/preview/title.jpg)

With Qdrant [version 1.3.0](https://github.com/qdrant/qdrant/releases/tag/v1.3.0) we
introduce the alternative io\_uring based _async uring_ storage backend on
Linux-based systems. Since its introduction, io\_uring has been known to improve
async throughput wherever the OS syscall overhead gets too high, which tends to
occur in situations where software becomes _IO bound_ (that is, mostly waiting
on disk).

## [Anchor](https://qdrant.tech/articles/io_uring/\#inputoutput) Input+Output

Around the mid-90s, the internet took off. The first servers used a process-
per-request setup, which was good for serving hundreds if not thousands of
concurrent request. The POSIX Input + Output (IO) was modeled in a strictly
synchronous way. The overhead of starting a new process for each request made
this model unsustainable. So servers started forgoing process separation, opting
for the thread-per-request model. But even that ran into limitations.

I distinctly remember when someone asked the question whether a server could
serve 10k concurrent connections, which at the time exhausted the memory of
most systems (because every thread had to have its own stack and some other
metadata, which quickly filled up available memory). As a result, the
synchronous IO was replaced by asynchronous IO during the 2.5 kernel update,
either via `select` or `epoll` (the latter being Linux-only, but a small bit
more efficient, so most servers of the time used it).

However, even this crude form of asynchronous IO carries the overhead of at
least one system call per operation. Each system call incurs a context switch,
and while this operation is itself not that slow, the switch disturbs the
caches. Today’s CPUs are much faster than memory, but if their caches start to
miss data, the memory accesses required led to longer and longer wait times for
the CPU.

### [Anchor](https://qdrant.tech/articles/io_uring/\#memory-mapped-io) Memory-mapped IO

Another way of dealing with file IO (which unlike network IO doesn’t have a hard
time requirement) is to map parts of files into memory - the system fakes having
that chunk of the file in memory, so when you read from a location there, the
kernel interrupts your process to load the needed data from disk, and resumes
your process once done, whereas writing to the memory will also notify the
kernel. Also the kernel can prefetch data while the program is running, thus
reducing the likelyhood of interrupts.

Thus there is still some overhead, but (especially in asynchronous
applications) it’s far less than with `epoll`. The reason this API is rarely
used in web servers is that these usually have a large variety of files to
access, unlike a database, which can map its own backing store into memory
once.

### [Anchor](https://qdrant.tech/articles/io_uring/\#combating-the-poll-ution) Combating the Poll-ution

There were multiple experiments to improve matters, some even going so far as
moving a HTTP server into the kernel, which of course brought its own share of
problems. Others like Intel added their own APIs that ignored the kernel and
worked directly on the hardware.

Finally, Jens Axboe took matters into his own hands and proposed a ring buffer
based interface called _io\_uring_. The buffers are not directly for data, but
for operations. User processes can setup a Submission Queue (SQ) and a
Completion Queue (CQ), both of which are shared between the process and the
kernel, so there’s no copying overhead.

![io_uring diagram](https://qdrant.tech/articles_data/io_uring/io-uring.png)

Apart from avoiding copying overhead, the queue-based architecture lends
itself to multithreading as item insertion/extraction can be made lockless,
and once the queues are set up, there is no further syscall that would stop
any user thread.

Servers that use this can easily get to over 100k concurrent requests. Today
Linux allows asynchronous IO via io\_uring for network, disk and accessing
other ports, e.g. for printing or recording video.

## [Anchor](https://qdrant.tech/articles/io_uring/\#and-what-about-qdrant) And what about Qdrant?

Qdrant can store everything in memory, but not all data sets may fit, which can
require storing on disk. Before io\_uring, Qdrant used mmap to do its IO. This
led to some modest overhead in case of disk latency. The kernel may
stop a user thread trying to access a mapped region, which incurs some context
switching overhead plus the wait time until the disk IO is finished. Ultimately,
this works very well with the asynchronous nature of Qdrant’s core.

One of the great optimizations Qdrant offers is quantization (either
[scalar](https://qdrant.tech/articles/scalar-quantization/) or
[product](https://qdrant.tech/articles/product-quantization/)-based).
However unless the collection resides fully in memory, this optimization
method generates significant disk IO, so it is a prime candidate for possible
improvements.

If you run Qdrant on Linux, you can enable io\_uring with the following in your
configuration:

```yaml