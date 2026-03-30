# Source: https://docs.salad.com/container-engine/how-to-guides/job-processing/build-redis-queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build Your Own Redis-Based Queue

> Enable Real-Time AI Inference on SaladCloud

*Last Updated: February 28, 2025*

## Real-Time AI Inference with a Redis-Based Queue

Several customers have successfully implemented a Redis-based, flexible and platform-independent queue for real-time
applications on SaladCloud, showcasing the following advantages:

* The Redis cluster, client applications, and Salad nodes are all strategically deployed within the same region to
  **ensure local access and minimize latency.**
* Supports multiple clients and servers, providing real-time request/response functionality **in streaming and
  non-streaming modes with support for synchronous and asynchronous processing.**
* More resilient to burst traffic, node failures, and the variability in AI inference times, while allowing easy
  customization for specific applications, such as using different timeout settings per request and adjusting streaming
  granularity (tokens or chunks).
* The input and output data of a task can be embedded within the request and response. For large datasets, data exchange
  can occur directly between client applications or SCE instances and cloud storage, with the request and response
  containing only a reference to the data.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2brq.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=517dcef212ed707b535b40f945c3ee3c" data-og-width="965" width="965" data-og-height="688" height="688" data-path="container-engine/images/2brq.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2brq.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=f67b18b4b41537a4bc004641d56e274a 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2brq.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4d7b448001ced8ceae9b85b6533f9eda 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2brq.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=039aca95889bfc9f9fa0a0f46cdd0ea3 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2brq.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=60b267d2c9d323a7d6394f4d78596790 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2brq.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5355d2892dae9d7eeed46907ab0dddf1 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/2brq.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=05a43e5fc8fd8ac1b40a94adc7f44681 2500w" />

However, implementing this solution requires effort and comes with certain limitations:

* A self-hosted Redis cluster or a managed service from public cloud providers (considering cost factors).
* Integrate the Redis worker in both client applications and inference servers.
* IP whitelisting for access control is not applicable from Salad nodes to the Redis cluster; instead, application-level
  authentication can be used.

The Redis-based solution is generally used for **low-latency, real-time applications** where responses or partial
responses must be returned immediately as soon as they are ready, or for **node-to-node communication** within the same
container group or across different groups. It may be applied to batch jobs or long-running tasks, but this requires
additional logic and effort. For these scenarios, we typically rely on Salad Kelpie and AWS SQS.

## Key Concepts in Redis

Redis is single-threaded but handles high levels of concurrency efficiently using asynchronous I/O and event-driven
architecture, and it supports asynchronous concurrency at the client level.

A **list** in Redis is an ordered collection of elements where items are added in the order they are inserted. It
supports efficient insertion and removal of elements from both ends. A list will be automatically removed from Redis
once it contains no elements. It also supports blocking operations, such as blocking reads on a non-existent list, with
a specified timeout.

A **zset** (sorted set) in Redis is a data structure that contains unique elements, each assigned a score. The elements
are stored in order of their scores, allowing efficient retrieval, with the highest-scoring element being accessed and
removed first.

A **hash** in Redis is a collection of key-value pairs, where each key is unique and maps to a specific value. It is
ideal for representing objects with multiple fields.

The [Python Redis client](https://github.com/redis/redis-py) uses a connection pool to manage connections efficiently,
reducing overhead. Instead of establishing a new connection for each request, it initializes the connection lazily on
the first command and reuses it for subsequent requests. The **socket\_timeout** setting defines the maximum time (in
seconds) the client will wait for a response from the Redis cluster before timing out. If the cluster does not respond
within this duration, the client raises a timeout error.

[pydantic\_redis](https://sopherapps.github.io/pydantic-redis/) simplifies working with Redis and Pydantic models
together by providing tools for serializing and deserializing Pydantic models, making it easier to manage data between a
Redis store and your application.

## Reference Design: Non-streaming

Please refer to the example code
([client](https://github.com/SaladTechnologies/rq/blob/main/python_redis_v1/rq_non_streaming_client.py),
[server](https://github.com/SaladTechnologies/rq/blob/main/python_redis_v1/rq_non_streaming_server.py) and
[common code](https://github.com/SaladTechnologies/rq/blob/main/python_redis_v1/rq_common.py)) in this senario.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3rqns.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2caed3e3311d76e1c1a5dd971dbb4d06" data-og-width="1688" width="1688" data-og-height="868" height="868" data-path="container-engine/images/3rqns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3rqns.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=fcce7ba388ecfb33074b123223755360 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3rqns.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=6d1bff0da138bacc63558430fd3735be 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3rqns.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1b6ba66d7c51578ea4fb499a215f7ce4 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3rqns.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=1810676298e245a1e26e119367501458 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3rqns.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=8d897ed93daf7acfe0d2cc5f533b3ecc 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/3rqns.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=f2e36ba6713caba5763230ac8ebd4ccd 2500w" />

The solution functions as both a real-time queue and a storage system, keeping historical I/O data and information about
client applications and servers.

The interaction between client applications and servers can be further simplified. For example, servers can directly
save the result to 'Temporary:Request\_1', eliminating the need for one write operation (S7) from servers and one read
operation (C9) by client applications from the Redis cluster.

The SCE instance can automatically retrieve and process new requests based on its current load and available resources.
During node failure, the SCE instance immediately stops fetching new requests, and any existing request IDs are lost, as
they have already been removed from the 'REQUEST:PENDING' in Redis.

**Client applications may encounter timeout errors when performing a blocking read from ‘Temporary:Request\_1’ due to the
following reasons:**

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsf.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=295fab1328ad8293b2db4851ed883da8" data-og-width="616" width="616" data-og-height="225" height="225" data-path="container-engine/images/5rqnsf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsf.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=dbbfe92e24fae054d52b6fc278a83170 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsf.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=7a7ea1ee5edc51df96e2ea282ddb9bec 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsf.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=8b4d4edc64c7e7a88365406a73e6355d 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsf.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=e0e6226aeedf7c6e0a5de5bd70066dec 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsf.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=00eec6c5dd8b3f395e35b92b558535b7 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsf.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=320da64dc37e6ff931037bfb9283fad8 2500w" />

When a timeout error occurs, applications can perform additional reads for an extended waiting time for specific
requests (flexible and customizable). Applications can also resend the request using a new ID and higher priority, while
disregarding the previous request (which may still be in the queue or being processed), or simply return an error to
users.

Rather than implementing a complex logic, applications can query the number of pending requests in the Redis cluster
before submitting a large quantity of requests and apply flow control as needed, such as rejecting new user requests
during periods of congestion. The system monitor should regularly track the pending requests in the cluster and
upscale/downscale the GPU resource pool accordingly.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsa.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2d6ae02aea91a94b2946557f6c34e993" data-og-width="535" width="535" data-og-height="431" height="431" data-path="container-engine/images/5rqnsa.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsa.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=0e296a633f10c9656cebc3e81db27c2c 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsa.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=96502daf149bbfcc8944c70c44b9cdd7 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsa.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=44537f33c1f548d3698aac54d610a730 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsa.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=eb411a4bdf5ce74bba47cebcd3e9620e 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsa.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=9edb732d7aafabb9c9f6eb93d31a1449 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/5rqnsa.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=359f1ef5ea2e05a4cda59418134edf21 2500w" />

To enhance I/O throughput and AI inference efficiency, your may run multiple Redis worker instances (processes or
coroutines) alongside the inference server (running as a separate process), which supports multiple threads or
asynchronous concurrency with batched inference.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4rqnsm.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=2508c4907798012b90fe6a8a47f07809" data-og-width="936" width="936" data-og-height="241" height="241" data-path="container-engine/images/4rqnsm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4rqnsm.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=3091ac9f4106096bafcb623dc776ac85 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4rqnsm.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=686d98d27a4437b82f34acf0e05c725b 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4rqnsm.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c0130bc00e3ab35e501ce7a1caff0036 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4rqnsm.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=c693217557ecb3e2e2cab71d190cac77 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4rqnsm.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=43984b4830a1c8cc8c1fdc4fd2e03192 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/4rqnsm.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=354b446fc24ee654df4cd47fac6ca47d 2500w" />

## Reference Design: Streaming

Please refer to the example code
([client](https://github.com/SaladTechnologies/rq/blob/main/python_redis_v1/rq_streaming_client.py),
[server](https://github.com/SaladTechnologies/rq/blob/main/python_redis_v1/rq_streaming_server.py) and
[common code](https://github.com/SaladTechnologies/rq/blob/main/python_redis_v1/rq_common.py)) in this senario.

<img src="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6rqs.png?fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=308193638ae354b384464ad83fba1f72" data-og-width="1264" width="1264" data-og-height="608" height="608" data-path="container-engine/images/6rqs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6rqs.png?w=280&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=5ea5ad4cc464ba76362dd135d3e2ff16 280w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6rqs.png?w=560&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4d25546a031364ef416690f1afeeff64 560w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6rqs.png?w=840&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=bd1a7aa9641a003c1db35a643dbe21a0 840w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6rqs.png?w=1100&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=47e87c98c2b365594b54910896cd4e35 1100w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6rqs.png?w=1650&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=a61f79075a285cf0da24f1c895962cd6 1650w, https://mintcdn.com/salad/0wRVwK9znuIbUvV3/container-engine/images/6rqs.png?w=2500&fit=max&auto=format&n=0wRVwK9znuIbUvV3&q=85&s=4e3cde52b0cc2e5e84d9b9601fc96a0a 2500w" />

The streaming solution is similar to the non-streaming solution, differing only in how results are generated by servers
and delivered to client applications.

**In Redis, a list is used to achieve the streaming effect, with servers writing to the left and clients reading from
the right. Both writes and reads are performed in chunks (tokens or sentences) by clients and servers.**

On the server side, specifically for LLMs, the Redis worker retrieves partial responses from the inference server, such
as Hugging Face's TGI, and writes them into Redis. Instead of calling the TGI server directly, the Redis worker can also
run custom inference code built on
[the Hugging Face's library](https://huggingface.co/docs/transformers/en/internal/generation_utils#transformers.TextIteratorStreamer.example),
enabling streaming results that are then returned to Redis.

The **socket\_timeout** can be set to a smaller value in this case, as partial inference results can be returned when
they are ready, enabling quicker error detection and response handling.

Client applications may encounter timeout errors when performing a blocking read from ‘Streaming:Request\_1’. A similar
logic can be applied—**if some chunks have already been received for a request, it is highly likely that a server
failure has occurred.**

The streaming granularity can be customized and changing based on application needs, such as **token-by-token**,
**chunk-by-chunk**, **chunk-by-sentence**, or **image-by-video**, as long as the data can be converted to strings,
providing flexibility in how data is processed and delivered.

## Local Performance Test

From the test, we can see that the real-time queue does not impose an intensive read/write workload on Redis, and its
throughput scales linearly with the number of clients and servers. However, a smaller chunk size may reduce transmission
efficiency and overall system throughput.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7lt.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=3255443a4d728611060d773b10c49d1c" data-og-width="1213" width="1213" data-og-height="489" height="489" data-path="container-engine/images/7lt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7lt.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=7b4e95081834fb23e01b51459c88fe37 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7lt.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=397befc0beab61dd26604c70bdcb928c 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7lt.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=236109c7ef0eff076096b09d2a0d0536 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7lt.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=ac7ca3139cdfd47190046ad880048418 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7lt.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=069c7772190384ac41cb7442de42449c 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/7lt.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=031d8226a75f2abefe6759566ac9e4ec 2500w" />
