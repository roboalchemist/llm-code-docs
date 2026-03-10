# [Anchor](https://qdrant.tech/documentation/database-tutorials/async-api/\#using-qdrants-async-api-for-efficient-python-applications) Using Qdrant’s Async API for Efficient Python Applications

Asynchronous programming is being broadly adopted in the Python ecosystem. Tools such as FastAPI [have embraced this new\\
paradigm](https://fastapi.tiangolo.com/async/), but it is also becoming a standard for ML models served as SaaS. For example, the Cohere SDK
[provides an async client](https://github.com/cohere-ai/cohere-python/blob/856a4c3bd29e7a75fa66154b8ac9fcdf1e0745e0/src/cohere/client.py#L189) next to its synchronous counterpart.

Databases are often launched as separate services and are accessed via a network. All the interactions with them are IO-bound and can
be performed asynchronously so as not to waste time actively waiting for a server response. In Python, this is achieved by
using [`async/await`](https://docs.python.org/3/library/asyncio-task.html) syntax. That lets the interpreter switch to another task
while waiting for a response from the server.

## [Anchor](https://qdrant.tech/documentation/database-tutorials/async-api/\#when-to-use-async-api) When to use async API

There is no need to use async API if the application you are writing will never support multiple users at once (e.g it is a script that runs once per day). However, if you are writing a web service that multiple users will use simultaneously, you shouldn’t be
blocking the threads of the web server as it limits the number of concurrent requests it can handle. In this case, you should use
the async API.

Modern web frameworks like [FastAPI](https://fastapi.tiangolo.com/) and [Quart](https://quart.palletsprojects.com/en/latest/) support
async API out of the box. Mixing asynchronous code with an existing synchronous codebase might be a challenge. The `async/await` syntax
cannot be used in synchronous functions. On the other hand, calling an IO-bound operation synchronously in async code is considered
an antipattern. Therefore, if you build an async web service, exposed through an [ASGI](https://asgi.readthedocs.io/en/latest/) server,
you should use the async API for all the interactions with Qdrant.

### [Anchor](https://qdrant.tech/documentation/database-tutorials/async-api/\#using-qdrant-asynchronously) Using Qdrant asynchronously

The simplest way of running asynchronous code is to use define `async` function and use the `asyncio.run` in the following way to run it:

```python
from qdrant_client import models

import qdrant_client
import asyncio

async def main():
    client = qdrant_client.AsyncQdrantClient("localhost")

    # Create a collection
    await client.create_collection(
        collection_name="my_collection",
        vectors_config=models.VectorParams(size=4, distance=models.Distance.COSINE),
    )

    # Insert a vector
    await client.upsert(
        collection_name="my_collection",
        points=[\
            models.PointStruct(\
                id="5c56c793-69f3-4fbf-87e6-c4bf54c28c26",\
                payload={\
                    "color": "red",\
                },\
                vector=[0.9, 0.1, 0.1, 0.5],\
            ),\
        ],
    )

    # Search for nearest neighbors
    points = await client.query_points(
        collection_name="my_collection",
        query=[0.9, 0.1, 0.1, 0.5],
        limit=2,
    ).points

    # Your async code using AsyncQdrantClient might be put here
    # ...

asyncio.run(main())

```

The `AsyncQdrantClient` provides the same methods as the synchronous counterpart `QdrantClient`. If you already have a synchronous
codebase, switching to async API is as simple as replacing `QdrantClient` with `AsyncQdrantClient` and adding `await` before each
method call.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/async-api.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/async-api.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-132-lllmstxt|>
## qdrant-dspy-medicalbot
- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Building a Chain-of-Thought Medical Chatbot with Qdrant and DSPy