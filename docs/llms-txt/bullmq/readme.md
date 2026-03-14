# Source: https://docs.bullmq.io/readme.md

# What is BullMQ

BullMQ is a [Node.js](https://nodejs.org) library that implements a fast and robust queue system built on top of [Redis](https://redis.io) that helps in resolving many modern age micro-services architectures.

The library is designed so that it will fulfill the following goals:

* Exactly once queue semantics, i.e., attempts to deliver every message exactly one time, but it will deliver at least once in the worst case scenario\*.
* Easy to scale horizontally. Add more workers for processing jobs in parallel.
* Consistent.
* High performant. Try to get the highest possible throughput from Redis by combining efficient .lua scripts and pipelining.

View the repository, see open issues, and contribute back [on GitHub](https://github.com/taskforcesh/bullmq)!

## **Features**

If you are new to Message Queues, you may wonder why they are needed after all. Queues can solve many different problems in an elegant way, from smoothing out processing peaks to creating robust communication channels between micro-services or offloading heavy work from one server to many smaller workers, and many other use cases. Check the [Patterns](https://docs.bullmq.io/patterns/adding-bulks) section for getting some inspiration and information about best practices.

* [x] **Minimal CPU usage due to a polling-free design**
* [x] **Distributed job execution based on Redis**
* [x] **LIFO and FIFO jobs**
* [x] **Priorities**
* [x] **Delayed jobs**
* [x] **Scheduled and repeatable jobs according to cron specifications**
* [x] **Retries of failed jobs**
* [x] **Concurrency setting per worker**
* [x] **Threaded (sandboxed) processing functions**
* [x] **Automatic recovery from process crashes**
* [x] **Parent-Child dependencies**

### Used by

BullMQ is used by many organizations big and small, here are some notable examples:

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-7eabf625a2932b111c2a5b7a651e2eaae6ad1b7a%2Fclipart1565701.png?alt=media)

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-7ffcd73605e901be045c7cf43cb61eb9a7a00ee4%2Fwordmark-logo.png?alt=media)

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-33c0c65bd9d6936b8ac33f4be7cbba2814b83ead%2Fdatawrapper-logo.png?alt=media)

![](https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-2038c9549e2aa39e1e8ce1a1017074c98953a7f4%2Fcurri-small.png?alt=media)
