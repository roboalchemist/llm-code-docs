# Source: https://docs.baseten.co/development/model/responses.md

# Custom Responses

> Get more control by directly creating the response object.

By default, Truss wraps prediction results into an HTTP response. For **advanced use cases**, you can create response objects manually to:

* **Control HTTP status codes.**
* **Use server-sent events (SSEs) for streaming responses.**

<Tip>You can return a response from predict or postprocess, but not both.</Tip>

## Returning Custom Response Objects

Any subclass of starlette.responses.Response is supported.

```python  theme={"system"}
import fastapi

class Model:
    def predict(self, inputs) -> fastapi.Response:
        return fastapi.Response(...)
```

<Tip>If `predict` returns a response, `postprocess` cannot be used.</Tip>

## Example: Streaming with SSEs

For **server-sent events (SSEs)**, use `StreamingResponse`:

```python  theme={"system"}
import time
from starlette.responses import StreamingResponse

class Model:
    def predict(self, model_input):
        def event_stream():
            while True:
                time.sleep(1)
                yield f"data: Server Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")
```

## Limitations

* **Response headers are not fully propagated** – include metadata in the response body.

<Info>
  Also see [Using Request Objects](/development/model/requests)
  for handling raw requests.
</Info>
