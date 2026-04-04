# Source: https://docs.baseten.co/development/model/requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Using request objects / cancellation

> Get more control by directly using the request object.

Truss processes client requests by extracting and validating payloads. For **advanced use cases**, you can access the raw request object to:

* **Customize payload deserialization** (e.g., binary protocol buffers).
* **Handle disconnections and cancel long-running predictions.**

<Tip>You can mix request objects with standard inputs or use requests exclusively for performance optimization.</Tip>

## Using Request Objects in Truss

You can define request objects in `preprocess`, `predict`, and `postprocess`:

```python  theme={"system"}
import fastapi

class Model:
    def preprocess(self, request: fastapi.Request):
        ...

    def predict(self, inputs, request: fastapi.Request):
        ...

    def postprocess(self, inputs, request: fastapi.Request):
        ...
```

### Rules for Using Requests

* The request must be **type-annotated** as `fastapi.Request`.
* If **only** requests are used, Truss **skips payload extraction** for better performance.
* If **both** request objects and standard inputs are used:
  * Request **must be the second argument**.
  * **Preprocessing transforms inputs**, but the request object remains unchanged.
  * `postprocess` cannot use only the request—it must receive the model’s output.
  * If `predict` only uses the request, `preprocess` cannot be used.

```python  theme={"system"}
import fastapi, asyncio, logging

class Model:
    async def predict(self, inputs, request: fastapi.Request):
        await asyncio.sleep(1)
        if await request.is_disconnected():
            logging.warning("Cancelled before generation.")
            return  # Cancel request on the model engine here.

        for i in range(5):
            await asyncio.sleep(1.0)
            logging.warning(i)
            yield str(i)  # Streaming response
            if await request.is_disconnected():
                logging.warning("Cancelled during generation.")
                return  # Cancel request on the model engine here.
```

<Tip>You must implement request cancellation at the model level, which varies by framework.</Tip>

## Cancelling Requests in Specific Frameworks

### TRT-LLM (Polling-Based Cancellation)

For TensorRT-LLM, use `response_iterator.cancel()` to terminate streaming requests:

```python  theme={"system"}
async for request_output in response_iterator:
    if await is_cancelled_fn():
        logging.info("Request cancelled. Cancelling Triton request.")
        response_iterator.cancel()
        return
```

<Note>See full example in [TensorRT-LLM Docs](https://developer.nvidia.com/tensorrt-llm).</Note>

### vLLM (Abort API)

For vLLM, use `engine.abort()` to stop processing:

```python  theme={"system"}
async for request_output in results_generator:
    if await request.is_disconnected():
        await engine.abort(request_id)
        return
```

<Note>See full example in [vLLM Docs](https://docs.vllm.ai/en/latest/dev/engine/async_llm_engine.html#vllm.AsyncLLMEngine.generate).</Note>

## Unsupported Request Features

* **Streaming file uploads** – Use URLs instead of embedding large data in the request.
* **Client-side headers** – Most headers are stripped; include necessary metadata in the payload.
