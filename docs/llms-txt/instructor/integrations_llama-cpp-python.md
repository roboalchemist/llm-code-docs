# Source: https://python.useinstructor.com/integrations/llama-cpp-python/index.md

# Structured outputs with llama-cpp-python, a complete guide w/ instructor

This guide demonstrates how to use llama-cpp-python with Instructor to generate structured outputs. You'll learn how to use JSON schema mode and speculative decoding to create type-safe responses from local LLMs.

Open-source LLMS are gaining popularity, and llama-cpp-python has made the `llama-cpp` model available to obtain structured outputs using JSON schema via a mixture of [constrained sampling](https://llama-cpp-python.readthedocs.io/en/latest/#json-schema-mode) and [speculative decoding](https://llama-cpp-python.readthedocs.io/en/latest/#speculative-decoding).

They also support a [OpenAI compatible client](https://llama-cpp-python.readthedocs.io/en/latest/#openai-compatible-web-server), which can be used to obtain structured output as a in process mechanism to avoid any network dependency.

## Patching

Instructor's patch enhances an create call it with the following features:

- `response_model` in `create` calls that returns a pydantic model
- `max_retries` in `create` calls that retries the call if it fails by using a backoff strategy

Learn More

To learn more, please refer to the [docs](https://python.useinstructor.com/index.md). To understand the benefits of using Pydantic with Instructor, visit the tips and tricks section of the [why use Pydantic](https://python.useinstructor.com/why/index.md) page. If you want to check out examples of using Pydantic with Instructor, visit the [examples](https://python.useinstructor.com/examples/index.md) page.

### See Also

- [Getting Started](https://python.useinstructor.com/getting-started/index.md) - Quick start guide
- [Ollama Integration](https://python.useinstructor.com/integrations/ollama/index.md) - Alternative local model setup
- [Local Classification](https://python.useinstructor.com/examples/local_classification/index.md) - Classification with local models
- [Open Source Models](https://python.useinstructor.com/examples/open_source/index.md) - More open-source model examples

# llama-cpp-python

Recently llama-cpp-python added support for structured outputs via JSON schema mode. This is a time-saving alternative to extensive prompt engineering and can be used to obtain structured outputs.

In this example we'll cover a more advanced use case of JSON_SCHEMA mode to stream out partial models. To learn more [partial streaming](https://github.com/jxnl/instructor/concepts/partial.md) check out partial streaming.

## Quick Start with `from_provider`

If you run the `llama-cpp-python` server in OpenAI compatible mode, you can use the unified `from_provider` API to patch the client. Simply point the base URL at your local server:

```python
import instructor

# Sync client
client = instructor.from_provider(
    "ollama/openhermes", base_url="http://localhost:8080/v1"
)

# Async client
async_client = instructor.from_provider(
    "ollama/openhermes", async_client=True, base_url="http://localhost:8080/v1"
)
```

You can then call `chat.completions.create` just like with any other provider.

```python
import llama_cpp
import instructor
from llama_cpp.llama_speculative import LlamaPromptLookupDecoding
from pydantic import BaseModel


llama = llama_cpp.Llama(
    model_path="../../models/OpenHermes-2.5-Mistral-7B-GGUF/openhermes-2.5-mistral-7b.Q4_K_M.gguf",
    n_gpu_layers=-1,
    chat_format="chatml",
    n_ctx=2048,
    draft_model=LlamaPromptLookupDecoding(num_pred_tokens=2),
    logits_all=True,
    verbose=False,
)


create = instructor.patch(
    create=llama.create_chat_completion_openai_v1,
    mode=instructor.Mode.JSON_SCHEMA,
)


class UserDetail(BaseModel):
    name: str
    age: int


user = create(
    messages=[
        {
            "role": "user",
            "content": "Extract `Jason is 30 years old`",
        }
    ],
    response_model=UserDetail,
)

print(user)
#> name='Jason' age=30
```
