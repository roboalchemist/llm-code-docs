# Source: https://docs.perplexity.ai/guides/perplexity-sdk-performance

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#overview)
Overview
The Perplexity SDKs provide several features to optimize performance for high-throughput applications. This guide covers async operations, connection pooling, raw response access, and other performance optimization techniques.
## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#async-support)
Async Support
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#basic-async-usage)
Basic Async Usage
For applications that need to handle multiple requests concurrently:
Python Installation
TypeScript/JavaScript Installation
Copy
Ask AI
```
pip install perplexityai[aiohttp]

```

Python
TypeScript/JavaScript
Copy
Ask AI
```
import asyncio
from perplexity import AsyncPerplexity, DefaultAioHttpClient
async def main():
    async with AsyncPerplexity(
        http_client=DefaultAioHttpClient()
    ) as client:
        # Single async request
        search = await client.search.create(query="machine learning")
        print(search.results)
asyncio.run(main())

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#concurrent-requests)
Concurrent Requests
Process multiple requests simultaneously for better throughput:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import asyncio
from perplexity import AsyncPerplexity, DefaultAioHttpClient
async def concurrent_searches():
    async with AsyncPerplexity(
        http_client=DefaultAioHttpClient()
    ) as client:
        # Concurrent requests
        queries = ["AI", "machine learning", "deep learning", "neural networks"]
        tasks = [
            client.search.create(query=query)
            for query in queries
        ]
        results = await asyncio.gather(*tasks)
        for i, result in enumerate(results):
            print(f"Query '{queries[i]}': {len(result.results)} results")
asyncio.run(concurrent_searches())

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#batch-processing-with-rate-limiting)
Batch Processing with Rate Limiting
Process large numbers of requests while respecting rate limits:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import asyncio
from perplexity import AsyncPerplexity, DefaultAioHttpClient
async def batch_process_with_limit(queries, batch_size=5, delay=1.0):
    async with AsyncPerplexity(
        http_client=DefaultAioHttpClient()
    ) as client:
        results = []
        for i in range(0, len(queries), batch_size):
            batch = queries[i:i + batch_size]
            # Process batch concurrently
            tasks = [
                client.search.create(query=query)
                for query in batch
            ]
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            results.extend(batch_results)
            # Delay between batches to respect rate limits
            if i + batch_size < len(queries):
                await asyncio.sleep(delay)
        return results
# Usage
queries = [f"query {i}" for i in range(20)]
results = asyncio.run(batch_process_with_limit(queries))

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#raw-response-access)
Raw Response Access
Access headers, status codes, and raw response data for advanced use cases:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
# Get raw response with headers
response = client.search.with_raw_response.create(
    query="machine learning"
)
print(f"Status Code: {response.status_code}")
print(f"Request ID: {response.headers.get('X-Request-ID')}")
print(f"Rate Limit Remaining: {response.headers.get('X-RateLimit-Remaining')}")
print(f"Rate Limit Reset: {response.headers.get('X-RateLimit-Reset')}")
# Parse the actual search results
search = response.parse()
print(f"Found {len(search.results)} results")

```

### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#response-streaming)
Response Streaming
For chat completions, use streaming to get partial results as they arrive:
Python
TypeScript/JavaScript
Copy
Ask AI
```
from perplexity import Perplexity
client = Perplexity()
# Stream chat completion responses
stream = client.chat.completions.create(
    model="llama-3.1-sonar-large-128k-online",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#connection-pooling)
Connection Pooling
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#optimized-connection-settings)
Optimized Connection Settings
Configure connection pooling for better performance:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import httpx
from perplexity import Perplexity, DefaultHttpxClient, AsyncPerplexity, DefaultAioHttpClient
# Sync client with optimized connection pooling
limits = httpx.Limits(
    max_keepalive_connections=50,  # Keep connections alive
    max_connections=100,           # Total connection pool size
    keepalive_expiry=30.0         # Keep-alive timeout
)
sync_client = Perplexity(
    http_client=DefaultHttpxClient(limits=limits)
)
# Async client with optimized connection pooling
async_limits = httpx.Limits(
    max_keepalive_connections=100,
    max_connections=200,
    keepalive_expiry=60.0
)
async def create_async_client():
    return AsyncPerplexity(
        http_client=DefaultAioHttpClient(limits=async_limits)
    )

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#performance-monitoring)
Performance Monitoring
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#request-timing-and-metrics)
Request Timing and Metrics
Monitor performance metrics to identify bottlenecks:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import time
import asyncio
from perplexity import AsyncPerplexity, DefaultAioHttpClient
class PerformanceMonitor:
    def __init__(self):
        self.request_times = []
        self.error_count = 0
    async def timed_request(self, client, query):
        start_time = time.time()
        try:
            result = await client.search.create(query=query)
            duration = time.time() - start_time
            self.request_times.append(duration)
            return result
        except Exception as e:
            self.error_count += 1
            raise e
    def get_stats(self):
        if not self.request_times:
            return {"error": "No successful requests"}
        return {
            "total_requests": len(self.request_times),
            "error_count": self.error_count,
            "avg_response_time": sum(self.request_times) / len(self.request_times),
            "min_response_time": min(self.request_times),
            "max_response_time": max(self.request_times)
        }
async def run_performance_test():
    monitor = PerformanceMonitor()
    async with AsyncPerplexity(
        http_client=DefaultAioHttpClient()
    ) as client:
        queries = [f"test query {i}" for i in range(10)]
        tasks = [
            monitor.timed_request(client, query)
            for query in queries
        ]
        await asyncio.gather(*tasks, return_exceptions=True)
    print(monitor.get_stats())
asyncio.run(run_performance_test())

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#memory-optimization)
Memory Optimization
### 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#efficient-data-processing)
Efficient Data Processing
Process large datasets efficiently with streaming and pagination:
Python
TypeScript/JavaScript
Copy
Ask AI
```
import asyncio
from perplexity import AsyncPerplexity, DefaultAioHttpClient
async def process_large_dataset(queries, process_fn):
    """Process queries in batches to manage memory usage"""
    async with AsyncPerplexity(
        http_client=DefaultAioHttpClient()
    ) as client:
        async def process_single(query):
            try:
                result = await client.search.create(query=query)
                # Process immediately to avoid storing in memory
                processed = process_fn(result)
                # Clear the original result from memory
                del result
                return processed
            except Exception as e:
                return f"Error processing {query}: {e}"
        # Process in small batches
        batch_size = 5
        for i in range(0, len(queries), batch_size):
            batch = queries[i:i + batch_size]
            # Process batch
            tasks = [process_single(query) for query in batch]
            batch_results = await asyncio.gather(*tasks)
            # Yield results instead of accumulating
            for result in batch_results:
                yield result
            # Optional: Small delay to prevent overwhelming the API
            await asyncio.sleep(0.1)
# Usage
async def summarize_result(search_result):
    """Process function that extracts only what we need"""
    return {
        "query": search_result.query,
        "result_count": len(search_result.results),
        "top_title": search_result.results[0].title if search_result.results else None
    }
async def main():
    queries = [f"query {i}" for i in range(100)]
    async for processed_result in process_large_dataset(queries, summarize_result):
        print(processed_result)
asyncio.run(main())

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#best-practices)
Best Practices
1
Use async for concurrent operations
Always use async clients when you need to process multiple requests simultaneously.
For CPU-bound processing after API calls, consider using worker threads or processes.
2
Implement connection pooling
Configure appropriate connection limits based on your application’s needs.
Python
TypeScript/JavaScript
Copy
Ask AI
```
# Good: Optimized for your use case
limits = httpx.Limits(
    max_keepalive_connections=20,  # Based on expected concurrency
    max_connections=50,
    keepalive_expiry=30.0
)

```

3
Monitor and tune performance
Use metrics to identify bottlenecks and optimize accordingly.
Don’t optimize prematurely - measure first, then optimize based on actual performance data.
4
Handle backpressure
Implement proper rate limiting and backpressure handling for high-throughput applications.
Python
TypeScript/JavaScript
Copy
Ask AI
```
# Use semaphores to limit concurrent requests
semaphore = asyncio.Semaphore(10)  # Max 10 concurrent requests
async def rate_limited_request(client, query):
    async with semaphore:
        return await client.search.create(query=query)

```

## 
[​](https://docs.perplexity.ai/guides/perplexity-sdk-performance#related-resources)
Related Resources
## [Configuration Optimize connection pooling and timeouts ](https://docs.perplexity.ai/guides/perplexity-sdk-configuration)## [Error Handling Handle errors in async operations ](https://docs.perplexity.ai/guides/perplexity-sdk-error-handling)
