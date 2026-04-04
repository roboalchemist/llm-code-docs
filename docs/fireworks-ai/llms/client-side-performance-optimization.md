# Source: https://docs.fireworks.ai/deployments/client-side-performance-optimization.md

# Client-side performance optimization

> Optimize your client code for maximum performance with dedicated deployments

When using a dedicated deployment, it is important to optimize the client-side
HTTP connection pooling for maximum performance. We recommend using our [Python
SDK](/tools-sdks/python-client/sdk-introduction) as it has good defaults for
connection pooling and utilizes
[aiohttp](https://docs.aiohttp.org/en/stable/index.html) for optimal performance
with Python's `asyncio` library. It also includes retry logic for handling `429`
errors that Fireworks returns when the server is overloaded. We have run
benchmarks that demonstrate the performance benefits.

## General optimization recommendations

Based on our benchmarks, we recommend the following:

1. Use a client library optimized for high concurrency, such as
   [aiohttp](https://docs.aiohttp.org/en/stable/index.html) in Python or
   [http.Agent](https://nodejs.org/api/http.html#class-httpagent) in Node.js.
2. Keep the [`connection pool size`](https://docs.aiohttp.org/en/stable/client_advanced.html#limiting-connection-pool-size) high (1000+).
3. Increase concurrency until performance stops improving or you observe too many `429` errors.
4. Use [direct routing](/deployments/direct-routing) to avoid the global API load balancer and route requests directly to your deployment.

## Code example: Optimal concurrent requests (Python)

Here's how to implement optimal concurrent requests using `asyncio` and the `LLM` class:

```python main.py theme={null}
import asyncio
from fireworks import LLM

async def make_concurrent_requests(
    messages: list[str],
    max_workers: int = 1000,
    max_connections: int = 1000, # this is the default value in the SDK
):
    """Make concurrent requests with optimized connection pooling"""
    
    llm = LLM(
        model="your-model-name",
        deployment_type="on-demand", 
        id="your-deployment-id",
        max_connections=max_connections
    )
    
    # Apply deployment configuration to Fireworks
    llm.apply()
    
    # Semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(max_workers)
    
    async def single_request(message: str):
        """Make a single request with semaphore control"""
        async with semaphore:
            response = await llm.chat.completions.acreate(
                messages=[{"role": "user", "content": message}],
                max_tokens=100
            )
            return response.choices[0].message.content
    
    # Create all request tasks
    tasks = [
        single_request(message) 
        for message in messages
    ]
    
    # Execute all requests concurrently
    results = await asyncio.gather(*tasks)
    return results

# Usage example
async def main():
    messages = ["Hello!"] * 1000  # 1000 requests
    
    results = await make_concurrent_requests(
        messages=messages,
    )
    
    print(f"Completed {len(results)} requests")

if __name__ == "__main__":
    asyncio.run(main())
```

This implementation:

* Uses `asyncio.Semaphore` to control concurrency to avoid overwhelming the server
* Allows configuration of the maximum number of concurrent connections to the Fireworks API
