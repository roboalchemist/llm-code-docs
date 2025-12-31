# Source: https://docs.baseten.co/development/model/performance/engine-builder-customization.md

# Engine control in Python

> Use `model.py` to customize engine behavior

When you create a new Truss with `truss init`, it creates two files: `config.yaml` and `model/model.py`. While you configure the Engine Builder in `config.yaml`, you may use `model/model.py` to access and control the engine object during inference.

You have two options:

1. Delete the `model/model.py` file and your TensorRT-LLM engine will run according to its base spec.
2. Update the code to support TensorRT-LLM.

<Warning>
  You must either update `model/model.py` to pass `trt_llm` as an argument to the `__init__` method OR delete the file. Otherwise you will get an error on deployment as the default `model/model.py` file is not written for TensorRT-LLM.
</Warning>

The `engine` object is a property of the `trt_llm` argument and must be initialized in `__init__` to be accessed in `load()` (which runs once on server start-up) and `predict()` (which runs for each request handled by the server).

This example applies a chat template with the Llama 3.1 8B tokenizer to the model prompt:

```python model/model.py theme={"system"}
import orjson  # faster serialization/deserialization than built-in json
from typing import Any, AsyncIterator
from transformers import AutoTokenizer
from fastapi.responses import StreamingResponse

SSE_PREFIX = "data: "

class Model:
    def __init__(self, trt_llm, **kwargs) -> None:
        self._secrets = kwargs["secrets"]
        self._engine = trt_llm["engine"]
        self._model = None
        self._tokenizer = None

    def load(self) -> None:
        self._tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct", token=self._secrets["hf_access_token"])

    async def predict(self, model_input: Any) -> Any:
        # Apply chat template to prompt
        model_input["prompt"] = self._tokenizer.apply_chat_template(model_input["prompt"], tokenize=False)
        response = await self._engine.predict(model_input)

        # If the response is streaming, post-process each chunk
        if isinstance(response, StreamingResponse):
            token_gen = response.body_iterator

            async def processed_stream():
                async for chunk in some_post_processing_function(token_gen):
                    yield chunk

            return StreamingResponse(processed_stream(), media_type="text/event-stream")

        # Otherwise, return the raw output
        else:
            return response

# --- Post-processing helpers for SSE ---

def parse_sse_chunk(chunk: bytes) -> dict | None:
    """Parses an SSE-formatted chunk and returns the JSON payload."""
    try:
        text = chunk.decode("utf-8").strip()
        if not text.startswith(SSE_PREFIX):
            return None
        return orjson.loads(text[len(SSE_PREFIX):])
    except Exception:
        return None

def format_sse_chunk(payload: dict) -> bytes:
    """Formats a JSON payload back into an SSE chunk."""
    return f"{SSE_PREFIX}".encode("utf-8") + orjson.dumps(payload) + b"\n\n"

def transform_payload(payload: dict) -> dict:
    """Add a new field to the SSE payload."""
    payload["my_new_field"] = "my_new_value"
    return payload

async def some_post_processing_function(
    token_gen: AsyncIterator[bytes]
) -> AsyncIterator[bytes]:
    """Post-process each SSE chunk in the stream."""
    async for chunk in token_gen:
        payload = parse_sse_chunk(chunk)
        if payload is None:
            yield chunk
            continue

        transformed = transform_payload(payload)
        yield format_sse_chunk(transformed)
```
