# Source: https://docs.together.ai/docs/pythonv2-migration-guide.md

# Python v2 SDK Migration Guide

> Migrate from Together Python v1 to v2 - the new Together AI Python SDK with improved type safety and modern architecture.

## Overview

We're excited to announce the release of Python v2 an upgrade to the Together AI Python SDK. This guide will help you migrate from the legacy (v1) SDK to the new version.

**Why Migrate?**

The new SDK offers several advantages:

* **Modern Architecture**: Built with Stainless OpenAPI generator for consistency and reliability
* **Better Type Safety**: Comprehensive typing for better IDE support and fewer runtime errors
* **Broader Python Support**: Python 3.8+ (vs 3.10+ in legacy)
* **Modern HTTP Client**: Uses `httpx` instead of `requests`
* **Faster Performance**: \~20ms faster per request on internal benchmarks
* **uv Support**: Compatible with [uv](https://docs.astral.sh/uv/), the fast Python package installer - `uv add together --prerelease allow`

## Feature Parity Matrix

Use this table to quickly assess the migration effort for your specific use case:

**Legend:** ✅ No changes | ⚠️ Minor changes needed | 🆕 New capability

| Feature                         | Legacy SDK | New SDK | Migration Notes                                                         |
| :------------------------------ | :--------- | :------ | :---------------------------------------------------------------------- |
| Chat Completions                | ✅          | ✅       | No changes required                                                     |
| Text Completions                | ✅          | ✅       | No changes required                                                     |
| Vision                          | ✅          | ✅       | No changes required                                                     |
| Function Calling                | ✅          | ✅       | No changes required                                                     |
| Structured Decoding (JSON Mode) | ✅          | ✅       | No changes required                                                     |
| Embeddings                      | ✅          | ✅       | No changes required                                                     |
| Image Generation                | ✅          | ✅       | No changes required                                                     |
| Video Generation                | ✅          | ✅       | No changes required                                                     |
| Streaming                       | ✅          | ✅       | No changes required                                                     |
| Async Support                   | ✅          | ✅       | No changes required                                                     |
| Models List                     | ✅          | ✅       | No changes required                                                     |
| Rerank                          | ✅          | ✅       | No changes required                                                     |
| Audio Speech (TTS)              | ✅          | ✅       | ⚠️ Voice listing: dict access → attribute access                        |
| Audio Transcription             | ✅          | ✅       | ⚠️ File paths → file objects with context manager                       |
| Audio Translation               | ✅          | ✅       | ⚠️ File paths → file objects with context manager                       |
| Fine-tuning                     | ✅          | ✅       | ⚠️ `list_checkpoints` response changed, `download` → `content`          |
| File Upload/Download            | ✅          | ✅       | ⚠️ `retrieve_content` → `content`, no longer writes to disk             |
| Batches                         | ✅          | ✅       | ⚠️ Method names simplified, response shape changed                      |
| Endpoints                       | ✅          | ✅       | ⚠️ `get` → `retrieve`, `list_hardware` removed, response shapes changed |
| Evaluations                     | ✅          | ✅       | ⚠️ Namespace changed to `evals`, parameters restructured                |
| Code Interpreter                | ✅          | ✅       | ⚠️ `run` → `execute`                                                    |
| **Hardware API**                | ❌          | ✅       | 🆕 New feature (replaces `endpoints.list_hardware`)                     |
| **Jobs API**                    | ❌          | ✅       | 🆕 New feature                                                          |
| **Raw Response Access**         | ❌          | ✅       | 🆕 New feature                                                          |

## Installation & Setup

**1. Install the New SDK**

```bash  theme={null}
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a new project and enter it
uv init myproject
cd myproject

# Install the Together Python SDK (allowing prereleases)
uv add together --prerelease allow

# pip still works aswell
pip install --pre together
```

**2. Dependency Changes**

The new SDK uses different dependencies. You can remove legacy dependencies if not used elsewhere:

**Old dependencies (can remove):**

```
requests>=2.31.0
typer>=0.9
aiohttp>=3.9.3
```

**New dependencies (automatically installed):**

```
httpx>=0.23.0
pydantic>=1.9.0
typing-extensions>=4.10
```

**3. Client Initialization**

Basic client setup remains the same:

```python  theme={null}
from together import Together

# Using API key directly
client = Together(api_key="your-api-key")

# Using environment variable (recommended)
client = Together()  # Uses TOGETHER_API_KEY env var

# Async client
from together import AsyncTogether

async_client = AsyncTogether()
```

<Note>
  Some constructor parameters have changed. See [Constructor Parameters](#constructor-parameters) for details.
</Note>

## Global Breaking Changes

### Constructor Parameters

The client constructor has been updated with renamed and new parameters:

<CodeGroup>
  ```python Legacy SDK theme={null}
  client = Together(
      api_key="...",
      base_url="...",
      timeout=30,
      max_retries=3,
      supplied_headers={"X-Custom-Header": "value"},
  )
  ```

  ```python New SDK theme={null}
  client = Together(
      api_key="...",
      base_url="...",
      timeout=30,
      max_retries=3,
      default_headers={
          "X-Custom-Header": "value"
      },  # Renamed from supplied_headers
      default_query={"custom_param": "value"},  # New parameter
      http_client=httpx.Client(...),  # New parameter
  )
  ```
</CodeGroup>

**Key Changes:**

* `supplied_headers` → `default_headers` (renamed)
* New optional parameters: `default_query`, `http_client`

### Keyword-Only Arguments

All API method arguments must now be passed as keyword arguments. Positional arguments are no longer supported.

```python  theme={null}
# ❌ Legacy SDK (positional arguments worked)
response = client.chat.completions.create(
    "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", messages
)

# ✅ New SDK (keyword arguments required)
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", messages=messages
)
```

### Optional Parameters

The new SDK uses `NOT_GIVEN` instead of `None` for omitted optional parameters. In most cases, you can simply omit the parameter entirely:

```python  theme={null}
# ❌ Legacy approach
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[...],
    max_tokens=None,  # Don't pass None
)

# ✅ New SDK approach - just omit the parameter
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[...],
    # max_tokens omitted entirely
)
```

### Extra Parameters

The legacy `**kwargs` pattern has been replaced with explicit parameters for passing additional data:

```python  theme={null}
# ❌ Legacy SDK (**kwargs)
response = client.chat.completions.create(
    model="...",
    messages=[...],
    custom_param="value",  # Passed via **kwargs
)

# ✅ New SDK (explicit extra_* parameters)
response = client.chat.completions.create(
    model="...",
    messages=[...],
    extra_body={"custom_param": "value"},
    extra_headers={"X-Custom-Header": "value"},
    extra_query={"query_param": "value"},
)
```

### Response Type Names

Most API methods have renamed response type definitions. If you're importing response types for type hints, you'll need to update your imports:

```python  theme={null}
# ❌ Legacy imports
from together.types import ChatCompletionResponse

# ✅ New imports
from together.types.chat.chat_completion import ChatCompletion
```

### CLI Commands Removed

The following CLI commands have been removed in the new SDK:

* `together chat.completions`
* `together completions`
* `together images generate`

## APIs with No Changes Required

The following APIs work identically in both SDKs. No code changes are needed:

**Chat Completions**

```python  theme={null}
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello!"},
    ],
    max_tokens=512,
    temperature=0.7,
)

print(response.choices[0].message.content)
```

**Streaming**

```python  theme={null}
stream = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Write a story"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

**Embeddings**

```python  theme={null}
response = client.embeddings.create(
    model="togethercomputer/m2-bert-80M-32k-retrieval",
    input=["Hello, world!", "How are you?"],
)

embeddings = [data.embedding for data in response.data]
```

**Images**

```python  theme={null}
response = client.images.generate(
    prompt="a flying cat", model="black-forest-labs/FLUX.1-schnell", steps=4
)

print(response.data[0].url)
```

**Videos**

```python  theme={null}
import time

# Create a video generation job
job = client.videos.create(
    prompt="A serene sunset over the ocean with gentle waves",
    model="minimax/video-01-director",
    width=1366,
    height=768,
)

print(f"Job ID: {job.id}")

# Poll until completion
while True:
    status = client.videos.retrieve(job.id)
    if status.status == "completed":
        print(f"Video URL: {status.outputs.video_url}")
        break
    elif status.status == "failed":
        print("Video generation failed")
        break
    time.sleep(5)
```

**Rerank**

```python  theme={null}
response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query="What is the capital of France?",
    documents=["Paris is the capital", "London is the capital"],
    top_n=1,
)
```

**Fine-tuning (Basic Operations)**

```python  theme={null}
# Create fine-tune job
job = client.fine_tuning.create(
    training_file="file-abc123",
    model="meta-llama/Llama-3.2-3B-Instruct",
    n_epochs=3,
    learning_rate=1e-5,
)

# List jobs
jobs = client.fine_tuning.list()

# Get job details
job = client.fine_tuning.retrieve(id="ft-abc123")

# Cancel job
client.fine_tuning.cancel(id="ft-abc123")
```

## APIs with Changes Required

**Batches**

Method names have been simplified, and the response structure has changed slightly.

<CodeGroup>
  ```python Legacy SDK theme={null}
  # Create batch
  batch_job = client.batches.create_batch(
      file_id="file-abc123", endpoint="/v1/chat/completions"
  )

  # Get batch
  batch_job = client.batches.get_batch(batch_job.id)

  # List batches
  batches = client.batches.list_batches()

  # Cancel batch
  client.batches.cancel_batch("job_id")
  ```

  ```python New SDK theme={null}
  # Create batch
  response = client.batches.create(
      input_file_id="file-abc123",  # Parameter renamed
      endpoint="/v1/chat/completions",
  )
  batch_job = response.job  # Access .job from response

  # Get batch
  batch_job = client.batches.retrieve(batch_job.id)

  # List batches
  batches = client.batches.list()

  # Cancel batch
  client.batches.cancel("job_id")
  ```
</CodeGroup>

**Key Changes:**

* `create_batch()` → `create()`
* `get_batch()` → `retrieve()`
* `list_batches()` → `list()`
* `cancel_batch()` → `cancel()`
* `file_id` → `input_file_id`
* `create()` returns full response; access `.job` for the job object

**Endpoints**

<CodeGroup>
  ```python Legacy SDK theme={null}
  # List endpoints
  endpoints = client.endpoints.list()
  for ep in endpoints:  # Returned array directly
      print(ep.id)

  # Create endpoint
  endpoint = client.endpoints.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      hardware="80GB-H100",
      min_replicas=1,
      max_replicas=5,
      display_name="My Endpoint",
  )

  # Get endpoint
  endpoint = client.endpoints.get(endpoint_id="ep-abc123")

  # List available hardware
  hardware = client.endpoints.list_hardware()

  # Delete endpoint
  client.endpoints.delete(endpoint_id="ep-abc123")
  ```

  ```python New SDK theme={null}
  # List endpoints
  response = client.endpoints.list()
  for ep in response.data:  # Access .data from response object
      print(ep.id)

  # Create endpoint
  endpoint = client.endpoints.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      hardware="80GB-H100",
      autoscaling={  # Nested under autoscaling
          "min_replicas": 1,
          "max_replicas": 5,
      },
      display_name="My Endpoint",
  )

  # Get endpoint
  endpoint = client.endpoints.retrieve("ep-abc123")

  # List available hardware (moved to new Hardware API)
  hardware = client.hardware.list()

  # Delete endpoint
  client.endpoints.delete("ep-abc123")
  ```
</CodeGroup>

**Key Changes:**

* `get()` → `retrieve()`
* `min_replicas` and `max_replicas` are now nested inside `autoscaling` parameter
* `list()` response changed: previously returned array directly, now returns object with `.data`
* `list_hardware()` removed; use `client.hardware.list()` instead

**Files**

<CodeGroup>
  ```python Legacy SDK theme={null}
  # Upload file
  response = client.files.upload(file="training_data.jsonl", purpose="fine-tune")

  # Download file content to disk
  client.files.retrieve_content(
      id="file-abc123", output="downloaded_file.jsonl"  # Writes directly to disk
  )
  ```

  ```python New SDK theme={null}
  # Upload file (same)
  response = client.files.upload(file="training_data.jsonl", purpose="fine-tune")

  # Download file content (manual file writing)
  response = client.files.content("file-abc123")
  with open("downloaded_file.jsonl", "wb") as f:
      for chunk in response.iter_bytes():
          f.write(chunk)
  ```
</CodeGroup>

**Key Changes:**

* `retrieve_content()` → `content()`
* No longer writes to disk automatically; returns binary data for you to handle

**Fine-tuning Checkpoints**

<CodeGroup>
  ```python Legacy SDK theme={null}
  checkpoints = client.fine_tuning.list_checkpoints("ft-123")

  for checkpoint in checkpoints:
      print(checkpoint.type)
      print(checkpoint.timestamp)
      print(checkpoint.name)
  ```

  ```python New SDK theme={null}
  ft_id = "ft-123"
  response = client.fine_tuning.list_checkpoints(ft_id)

  for checkpoint in response.data:  # Access .data
      # Construct checkpoint name from step
      checkpoint_name = (
          f"{ft_id}:{checkpoint.step}"
          if "intermediate" in checkpoint.checkpoint_type.lower()
          else ft_id
      )

      print(checkpoint.checkpoint_type)
      print(checkpoint.created_at)
      print(checkpoint_name)
  ```
</CodeGroup>

**Key Changes:**

* Response is now an object with `.data` containing the list of checkpoints
* Checkpoint properties renamed: `type` → `checkpoint_type`, `timestamp` → `created_at`
* `name` no longer exists; construct from `ft_id` and `step`

**Fine-tuning Download**

<CodeGroup>
  ```python Legacy SDK theme={null}
  # Download fine-tuned model
  client.fine_tuning.download(
      id="ft-abc123", output="model_weights/"  # Writes directly to disk
  )
  ```

  ```python New SDK theme={null}
  # Download fine-tuned model (manual file writing)
  with client.fine_tuning.with_streaming_response.content(
      ft_id="ft-abc123"
  ) as response:
      with open("model_weights.tar.gz", "wb") as f:
          for chunk in response.iter_bytes():
              f.write(chunk)
  ```
</CodeGroup>

**Key Changes:**

* `download()` → `content()` with streaming response
* No longer writes to disk automatically

**Code Interpreter**

<CodeGroup>
  ```python Legacy SDK theme={null}
  # Execute code
  result = client.code_interpreter.run(
      code="print('Hello, World!')", language="python", session_id="session-123"
  )

  print(result.output)
  ```

  ```python New SDK theme={null}
  # Execute code
  result = client.code_interpreter.execute(
      code="print('Hello, World!')",
      language="python",
  )

  print(result.data.outputs[0].data)

  # Session management (new feature)
  sessions = client.code_interpreter.sessions.list()
  ```
</CodeGroup>

**Key Changes:**

* `run()` → `execute()`
* Output access: `result.output` → `result.data.outputs[0].data`
* New `sessions.list()` method for session management

**Audio Transcriptions & Translations**

The new SDK requires file objects instead of file paths for audio operations. Use context managers for proper resource handling.

<CodeGroup>
  ```python Legacy SDK theme={null}
  # Transcription with file path
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      language="en",
  )

  # Translation with file path
  response = client.audio.translations.create(
      file="french_audio.mp3",
      model="openai/whisper-large-v3",
  )
  ```

  ```python New SDK theme={null}
  # Transcription with file object (context manager)
  with open("audio.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          language="en",
      )

  # Translation with file object (context manager)
  with open("french_audio.mp3", "rb") as audio_file:
      response = client.audio.translations.create(
          file=audio_file,
          model="openai/whisper-large-v3",
      )
  ```
</CodeGroup>

**Key Changes:**

* File paths (strings) → file objects opened with `open(file, "rb")`
* Use context managers (`with open(...) as f:`) for proper resource cleanup

**Audio Speech (TTS) - Voice Listing**

When listing available voices, voice properties are now accessed as object attributes instead of dictionary keys.

<CodeGroup>
  ```python Legacy SDK theme={null}
  response = client.audio.voices.list()

  for model_voices in response.data:
      print(f"Model: {model_voices.model}")
      for voice in model_voices.voices:
          print(f"  - Voice: {voice['name']}")  # Dict access
  ```

  ```python New SDK theme={null}
  response = client.audio.voices.list()

  for model_voices in response.data:
      print(f"Model: {model_voices.model}")
      for voice in model_voices.voices:
          print(f"  - Voice: {voice.name}")  # Attribute access
  ```
</CodeGroup>

**Key Changes:**

* Voice properties: `voice['name']` → `voice.name` (dict access → attribute access)

**Evaluations**

The evaluations API has significant changes including a namespace rename and restructured parameters.

<CodeGroup>
  ```python Legacy SDK theme={null}
  # Create evaluation
  evaluation = client.evaluation.create(
      type="classify",
      judge_model_name="meta-llama/Llama-3.1-70B-Instruct-Turbo",
      judge_system_template="You are an expert evaluator...",
      input_data_file_path="file-abc123",
      labels=["good", "bad"],
      pass_labels=["good"],
      model_to_evaluate="meta-llama/Llama-3.1-8B-Instruct-Turbo",
  )

  # Get evaluation
  eval_job = client.evaluation.retrieve(workflow_id=evaluation.workflow_id)

  # Get status
  status = client.evaluation.status(eval_job.workflow_id)

  # List evaluations
  evaluations = client.evaluation.list()
  ```

  ```python New SDK theme={null}
  from together.types.eval_create_params import (
      ParametersEvaluationClassifyParameters,
      ParametersEvaluationClassifyParametersJudge,
  )

  # Create evaluation (restructured parameters)
  evaluation = client.evals.create(
      type="classify",
      parameters=ParametersEvaluationClassifyParameters(
          judge=ParametersEvaluationClassifyParametersJudge(
              model="meta-llama/Llama-3.1-70B-Instruct-Turbo",
              model_source="serverless",
              system_template="You are an expert evaluator...",
          ),
          input_data_file_path="file-abc123",
          labels=["good", "bad"],
          pass_labels=["good"],
          model_to_evaluate="meta-llama/Llama-3.1-8B-Instruct-Turbo",
      ),
  )

  # Get evaluation (no named argument)
  eval_job = client.evals.retrieve(evaluation.workflow_id)

  # Get status (no named argument)
  status = client.evals.status(eval_job.workflow_id)

  # List evaluations
  evaluations = client.evals.list()
  ```
</CodeGroup>

**Key Changes:**

* Namespace: `client.evaluation` → `client.evals`
* Parameters restructured with typed parameter objects
* `retrieve()` and `status()` no longer use named arguments

## New SDK-Only Features

**Hardware API**

Discover available hardware configurations:

```python  theme={null}
# List all available hardware
hardware_list = client.hardware.list()

# Filter by model compatibility
hardware_list = client.hardware.list(
    model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
)

for hw in hardware_list.data:
    price_per_hour = hw.pricing.cents_per_minute * 60 / 100
    print(f"Hardware: {hw.id} - Price: ${price_per_hour}/hour")
```

**Jobs API**

General job management capabilities:

```python  theme={null}
# Retrieve job details
job = client.jobs.retrieve(job_id="job-abc123")

# List all jobs
jobs = client.jobs.list()

print(f"Job {job.id} status: {job.status}")
```

**Raw Response Access**

Access raw HTTP responses for debugging:

```python  theme={null}
response = client.chat.completions.with_raw_response.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Hello"}],
)

print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
completion = response.parse()  # Get parsed response
```

**Streaming with Context Manager**

Better resource management for streaming:

```python  theme={null}
with client.chat.completions.with_streaming_response.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Write a story"}],
    stream=True,
) as response:
    for line in response.iter_lines():
        print(line)
# Response automatically closed
```

## Error Handling Migration

The exception hierarchy has been completely restructured with a new, more granular set of HTTP status-specific exceptions. Update your error handling code accordingly:

| Legacy SDK Exception      | New SDK Exception            | Notes                                   |
| :------------------------ | :--------------------------- | :-------------------------------------- |
| `TogetherException`       | `TogetherError`              | Base exception renamed                  |
| `AuthenticationError`     | `AuthenticationError`        | HTTP 401                                |
| `RateLimitError`          | `RateLimitError`             | HTTP 429                                |
| `Timeout`                 | `APITimeoutError`            | Renamed                                 |
| `APIConnectionError`      | `APIConnectionError`         | Unchanged                               |
| `ResponseError`           | `APIStatusError`             | Base class for HTTP errors              |
| `InvalidRequestError`     | `BadRequestError`            | HTTP 400                                |
| `ServiceUnavailableError` | `InternalServerError`        | HTTP 500+                               |
| `JSONError`               | `APIResponseValidationError` | Response parsing errors                 |
| `InstanceError`           | `APIStatusError`             | Use base class or specific status error |
| `APIError`                | `APIError`                   | Base for all API errors                 |
| `FileTypeError`           | `FileTypeError`              | Still exists (different module)         |
| `DownloadError`           | `DownloadError`              | Still exists (different module)         |

**New exceptions added:**

* `PermissionDeniedError` (403)
* `NotFoundError` (404)
* `ConflictError` (409)
* `UnprocessableEntityError` (422)

<Warning>
  Exception attributes have changed. For example, `http_status` is now `status_code`. Check your error handling code for attribute access.
</Warning>

**Updated Error Handling Example**

```python  theme={null}
import together

try:
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[{"role": "user", "content": "Hello"}],
    )
except together.APIConnectionError:
    print("Connection error - check your network")
except together.RateLimitError:
    print("Rate limit exceeded - slow down requests")
except together.AuthenticationError:
    print("Invalid API key")
except together.APITimeoutError:
    print("Request timed out")
except together.APIStatusError as e:
    print(f"API error: {e.status_code} - {e.message}")
```

## Troubleshooting

**Import Errors**

**Problem:**

```text  theme={null}
ImportError: No module named 'together.types.ChatCompletionResponse'
```

**Solution:** Response type imports have changed:

```python  theme={null}
# Old import
from together.types import ChatCompletionResponse

# New import
from together.types.chat.chat_completion import ChatCompletion
```

**Method Not Found Errors**

**Problem:**

```text  theme={null}
AttributeError: 'BatchesResource' object has no attribute 'create_batch'
```

**Solution:** Method names have been simplified:

```text  theme={null}
# Old → New
client.batches.create_batch(...)  →  client.batches.create(...)
client.batches.get_batch(...)     →  client.batches.retrieve(...)
client.batches.list_batches()     →  client.batches.list()
client.endpoints.get(...)         →  client.endpoints.retrieve(...)
client.code_interpreter.run(...)  →  client.code_interpreter.execute(...)
```

**Parameter Type Errors**

**Problem:**

```text  theme={null}
TypeError: Expected NotGiven, got None
```

**Solution:** Don't pass `None` for optional parameters; omit them instead:

```python  theme={null}
# ❌ Wrong
client.chat.completions.create(model="...", messages=[...], max_tokens=None)

# ✅ Correct - just omit the parameter
client.chat.completions.create(model="...", messages=[...])
```

**Namespace Errors**

**Problem:**

```text  theme={null}
AttributeError: 'Together' object has no attribute 'evaluation'
```

**Solution:** The namespace was renamed:

```python  theme={null}
# Old
client.evaluation.create(...)

# New
client.evals.create(...)
```

## Best Practices

**Type Safety**

Take advantage of improved typing:

```python  theme={null}
from together.types.chat import completion_create_params
from together.types.chat.chat_completion import ChatCompletion
from typing import List


def create_chat_completion(
    messages: List[completion_create_params.Message],
) -> ChatCompletion:
    return client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", messages=messages
    )
```

**HTTP Client Configuration**

The new SDK uses `httpx`. Configure it as needed:

```python  theme={null}
import httpx

client = Together(
    timeout=httpx.Timeout(60.0, connect=10.0),
    http_client=httpx.Client(verify=True, headers={"User-Agent": "MyApp/1.0"}),
)
```

## Getting Help

If you encounter issues during migration:

* To see the code check the [new SDK repo](https://github.com/togethercomputer/together-py)
* Review the [API Reference](/reference/chat-completions-1) which has updated v2 code examples
* Report issues and discuss changes on [discord](https://discord.com/channels/1082503318624022589/1228037496257118242)
* [Contact support](https://www.together.ai/contact) for additional help


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt