# Source: https://docs.baseten.co/development/model/performance/performance-client.md

# Performance client

> The **Baseten Performance Client** is a high-performance library for interacting with model endpoints, supporting **embeddings, reranking, and classification**. It is available for both **Python (pip)** and **Node.js (npm)**.

<Card title="View on GitHub" icon="github" horizontal href="https://github.com/basetenlabs/truss/tree/main/baseten-performance-client" />

Built in Rust and integrated with Python and Node.js, the client is optimized for **massive concurrent POST requests**. It releases the Python GIL while executing requests, enabling simultaneous sync and async usage.

In our [benchmarks](https://www.baseten.co/blog/your-client-code-matters-10x-higher-embedding-throughput-with-python-and-rust/), the Performance Client reached **1200+ requests per second** per client.

It can be used when **deploying on Baseten**, as well as **third-party providers** such as OpenAI and Mixedbread.

<img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8b1df45b528b98df2154736919de105c" alt="benchmarks" data-og-width="1200" width="1200" data-og-height="565" height="565" data-path="images/performance-client-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=7974921583e72f195778a892e0fa9af1 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=6c97fe1f29ba0ac098d247965943f2eb 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=de2c7b3177be0adba10dc5c032523d08 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4545ef1bff98f1877d5c4adb4231d5ad 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=61697cd3af7479fac9e0bf497b538c82 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5c407d6f55103b325ca7547b3f11902b 2500w" />

***

## Installation

### Python

```bash  theme={"system"}
pip install baseten_performance_client
```

### Node.js

```bash  theme={"system"}
npm install baseten-performance-client
```

## Getting Started

### Python

```python  theme={"system"}
from baseten_performance_client import PerformanceClient

client = PerformanceClient(
    base_url="https://model-yqv4yjjq.api.baseten.co/environments/production/sync",
    api_key="YOUR_API_KEY"
)
```

### Node.js

```javascript  theme={"system"}
const { PerformanceClient } = require("baseten-performance-client");

const client = new PerformanceClient(
  "https://model-yqv4yjjq.api.baseten.co/environments/production/sync",
  process.env.BASETEN_API_KEY
);
```

You can also use **OpenAI** or **Mixedbread** endpoints by replacing the `base_url`.

## Embeddings

The client provides efficient embedding requests with configurable batching, concurrency, and latency optimizations.

### Example (Python)

```python  theme={"system"}
texts = ["Hello world", "Example text", "Another sample"] * 10

response = client.embed(
    input=texts,
    model="my_model",
    batch_size=16,
    max_concurrent_requests=256,
    max_chars_per_request=10000,
    hedge_delay=15,
    timeout_s=360
)
```

**Advanced parameters**

* `max_chars_per_request`, `batch_size`: Packs/Batches requests by number of entries or character count, whatever limit is reached first. Useful for optimial distribution across all your replicas on baseten.
* `hedge_delay`: Send duplicate requests after a delay (≥0.2s) to reduce the p99.5 latency. After hedge\_delay (s) is met, your request will be cloned once and race the original request. Limited by a 5% budget. Default: disabled.
* `timeout_s`: Timeout on each request. Raised a request.TimeoutError once a single request can't be retried. 429 and 5xx errors are always retried.

Async usage is also supported:

```python  theme={"system"}
response = await client.async_embed(input=texts, model="my_model")
```

### Example (Node.js)

```javascript  theme={"system"}
const response = await client.embed(
  ["Hello world", "Example text", "Another sample"],
  "my_model"
);
```

## Batch POST

Use `batch_post` for sending POST requests to any URL.
Built for benchmarks (p90/p95/p99 timings). Useful for starting off massive batch tasks, or benchmarking the performance of individual requests, while retaining a capped concurrency.
Releasing the GIL during all calls - you can do work in parallel without impacting performance.

### Example (Python) - completions/chat completions

```python  theme={"system"}
# requires stream=false / non-sse response.
payloads = [
    {"model": "my_model", "prompt": "Batch request 1", stream="false"},
    {"model": "my_model", "input": "Batch request 2", stream="false"}
] * 10

response = client.batch_post(
    url_path="/v1/completions",
    payloads=payloads,
    max_concurrent_requests=96,
    timeout_s=720,
    hedge_delay=30,
)
responses = response.data # array with 20 dicts
# timings = response.individual_request_times # array with the time.time() for each request
```

### Example (Node.js)

```javascript  theme={"system"}
const payloads = [
  { model: "my_model", input: ["Batch request 1"] },
  { model: "my_model", input: ["Batch request 2"] },
];

const response = await client.batchPost("/v1/embeddings", payloads, 96);
```

***

## Reranking

Compatible with BEI and text-embeddings-inference.

### Example (Python)

```python  theme={"system"}
response = client.rerank(
    query="What is the best framework?",
    texts=["Doc 1", "Doc 2", "Doc 3"]
)
```

***

## Classification

Supports classification endpoints such as BEI or text-embeddings-inference.

### Example (Python)

```python  theme={"system"}
response = client.classify(inputs=[
    "This is great!",
    "I did not like it.",
    "Neutral experience."
])
```

***

## Error Handling

The client raises standard Python/Node.js errors:

* **HTTPError**: Authentication failures, 4xx/5xx responses.
* **ValueError**: Invalid inputs (e.g., empty list, invalid batch size).

Example:

```python  theme={"system"}
try:
    response = client.embed(input=["Hello"], model="my_model")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
```

***

## More examples, contribute to the open-source libary or more detailed usage:

Check out the readme in in [Github truss repo: baseten-performance-client](https://github.com/basetenlabs/truss/tree/main/baseten-performance-client)
