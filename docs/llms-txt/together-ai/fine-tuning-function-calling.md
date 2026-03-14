# Source: https://docs.together.ai/docs/fine-tuning-function-calling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Function Calling Fine-tuning

> Learn how to fine-tune models with function calling capabilities using Together AI.

## Introduction

Function calling fine-tuning allows you to adapt models to reliably invoke tools and structured functions in response to user queries. This is useful for building agents and models that can reliably call APIs.

This guide covers the specific steps for function calling fine-tuning. For general fine-tuning concepts, environment setup, and hyperparameter details, refer to the [Fine-tuning Guide](/docs/fine-tuning-quickstart).

## Quick Links

* [Dataset Requirements](#function-calling-dataset)
* [Supported Models](#supported-models)
* [Check and Upload Dataset](#check-and-upload-dataset)
* [Start a Fine-tuning Job](#starting-a-fine-tuning-job)
* [Monitor Progress](#monitoring-your-fine-tuning-job)
* [Deploy Your Model](#using-your-fine-tuned-model)

## Function Calling Dataset

**Dataset Requirements:**

* **Format**: `.jsonl` file
* **Supported types**: Conversational, Preferential — more details on their purpose [here](/docs/fine-tuning-data-preparation#text-data)
* Each line may contain a `tools` field listing the tools the model can use
* Assistant messages can include `tool_calls` (structured invocation requests) instead of `content`
* Tool call results are provided via messages with the `tool` role

### Conversation Tool Calling Format

This is what one row/example from the function calling dataset looks like in conversation format:

```json  theme={null}
{
  "messages": [
    {"role": "system", "content": "You are a helpful travel planning assistant."},
    {"role": "user", "content": "What is the current temperature in San Francisco?"},
    {"role": "assistant", "tool_calls": [
      {
        "id": "call_abc123",
        "type": "function",
        "function": {
          "name": "getCurrentWeather",
          "arguments": "{\"location\": \"San Francisco, CA\"}"
        }
      }
    ]},
    {"role": "tool", "content": "{\"location\": \"San Francisco\", \"temperature\": \"65\", \"unit\": \"fahrenheit\"}"}
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "getCurrentWeather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA."
            }
          },
          "required": ["location"]
        }
      }
    }
  ]
}
```

### Preference Tool Calling Format

For preference fine-tuning, the `tools` field should be defined inside `input`:

```json  theme={null}
{
  "input": {
    "messages": [
      {"role": "system", "content": "You are a helpful travel planning assistant."},
      {"role": "user", "content": "What is the current temperature in San Francisco?"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "getCurrentWeather",
          "description": "Get the current weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA."
              }
            },
            "required": ["location"]
          }
        }
      }
    ]
  },
  "preferred_output": [
    {
      "role": "assistant",
      "tool_calls": [
        {
          "id": "call_abc123",
          "type": "function",
          "function": {
            "name": "getCurrentWeather",
            "arguments": "{\"location\": \"San Francisco, CA\"}"
          }
        }
      ]
    }
  ],
  "non_preferred_output": [
    {
      "role": "assistant",
      "content": "Sorry, I can't help you with that."
    }
  ]
}
```

## Supported Models

The following models support function calling fine-tuning:

| Organization | Model Name                      | Model String for API                  |
| :----------- | :------------------------------ | :------------------------------------ |
| Qwen         | Qwen 2.5 1.5B                   | `Qwen/Qwen2.5-1.5B`                   |
| Qwen         | Qwen 2.5 1.5B Instruct          | `Qwen/Qwen2.5-1.5B-Instruct`          |
| Qwen         | Qwen 2.5 3B                     | `Qwen/Qwen2.5-3B`                     |
| Qwen         | Qwen 2.5 3B Instruct            | `Qwen/Qwen2.5-3B-Instruct`            |
| Qwen         | Qwen 2.5 7B                     | `Qwen/Qwen2.5-7B`                     |
| Qwen         | Qwen 2.5 7B Instruct            | `Qwen/Qwen2.5-7B-Instruct`            |
| Qwen         | Qwen 2.5 14B                    | `Qwen/Qwen2.5-14B`                    |
| Qwen         | Qwen 2.5 14B Instruct           | `Qwen/Qwen2.5-14B-Instruct`           |
| Qwen         | Qwen 2.5 32B                    | `Qwen/Qwen2.5-32B`                    |
| Qwen         | Qwen 2.5 32B Instruct           | `Qwen/Qwen2.5-32B-Instruct`           |
| Qwen         | Qwen 2.5 72B                    | `Qwen/Qwen2.5-72B`                    |
| Qwen         | Qwen 2.5 72B Instruct           | `Qwen/Qwen2.5-72B-Instruct`           |
| Qwen         | Qwen 3 0.6B                     | `Qwen/Qwen3-0.6B`                     |
| Qwen         | Qwen 3 1.7B                     | `Qwen/Qwen3-1.7B`                     |
| Qwen         | Qwen 3 4B                       | `Qwen/Qwen3-4B`                       |
| Qwen         | Qwen 3 8B                       | `Qwen/Qwen3-8B`                       |
| Qwen         | Qwen 3 14B                      | `Qwen/Qwen3-14B`                      |
| Qwen         | Qwen 3 32B                      | `Qwen/Qwen3-32B`                      |
| Qwen         | Qwen 3 32B 16k                  | `Qwen/Qwen3-32B-16k`                  |
| Qwen         | Qwen 3 30B A3B                  | `Qwen/Qwen3-30B-A3B`                  |
| Qwen         | Qwen 3 30B A3B Instruct 2507    | `Qwen/Qwen3-30B-A3B-Instruct-2507`    |
| Qwen         | Qwen 3 235B A22B                | `Qwen/Qwen3-235B-A22B`                |
| Qwen         | Qwen 3 235B A22B Instruct 2507  | `Qwen/Qwen3-235B-A22B-Instruct-2507`  |
| Qwen         | Qwen 3 VL 8B Instruct           | `Qwen/Qwen3-VL-8B-Instruct`           |
| Qwen         | Qwen 3 VL 32B Instruct          | `Qwen/Qwen3-VL-32B-Instruct`          |
| Qwen         | Qwen 3 VL 30B A3B Instruct      | `Qwen/Qwen3-VL-30B-A3B-Instruct`      |
| Qwen         | Qwen 3 VL 235B A22B Instruct    | `Qwen/Qwen3-VL-235B-A22B-Instruct`    |
| Qwen         | Qwen 3 Coder 30B A3B Instruct   | `Qwen/Qwen3-Coder-30B-A3B-Instruct`   |
| Qwen         | Qwen 3 Coder 480B A35B Instruct | `Qwen/Qwen3-Coder-480B-A35B-Instruct` |
| Qwen         | Qwen 3 Next 80B A3B Instruct    | `Qwen/Qwen3-Next-80B-A3B-Instruct`    |
| Qwen         | Qwen 3 Next 80B A3B Thinking    | `Qwen/Qwen3-Next-80B-A3B-Thinking`    |
| Moonshot AI  | Kimi K2 Instruct                | `moonshotai/Kimi-K2-Instruct`         |
| Moonshot AI  | Kimi K2 Thinking                | `moonshotai/Kimi-K2-Thinking`         |
| Moonshot AI  | Kimi K2 Base                    | `moonshotai/Kimi-K2-Base`             |
| Moonshot AI  | Kimi K2 Instruct 0905           | `moonshotai/Kimi-K2-Instruct-0905`    |
| Moonshot AI  | Kimi K2.5                       | `moonshotai/Kimi-K2.5`                |
| Z.ai         | GLM 4.6                         | `zai-org/GLM-4.6`                     |
| Z.ai         | GLM 4.7                         | `zai-org/GLM-4.7`                     |

## Check and Upload Dataset

To upload your data, use the CLI or our Python library:

<CodeGroup>
  ```sh CLI theme={null}
  together files check "function_calling_dataset.jsonl"

  together files upload "function_calling_dataset.jsonl"
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  file_resp = client.files.upload(
      file="function_calling_dataset.jsonl", check=True
  )

  print(file_resp.model_dump())
  ```
</CodeGroup>

You'll see the following output once the upload finishes:

```json  theme={null}
{
  "id": "file-629e58b4-ff73-438c-b2cc-f69542b27980",
  "object": "file",
  "created_at": 1732573871,
  "type": null,
  "purpose": "fine-tune",
  "filename": "function_calling_dataset.jsonl",
  "bytes": 0,
  "line_count": 0,
  "processed": false,
  "FileType": "jsonl"
}
```

You'll be using your file's ID (the string that begins with `file-`) to start your fine-tuning job, so store it somewhere before moving on.

## Starting a Fine-tuning Job

We support both LoRA and full fine-tuning for function calling models.

For an exhaustive list of all the available fine-tuning parameters, refer to the [Together AI Fine-tuning API Reference](/reference/cli/finetune).

### LoRA Fine-tuning (Recommended)

<CodeGroup>
  ```sh CLI theme={null}
  together fine-tuning create \
    --training-file "file-629e58b4-ff73-438c-b2cc-f69542b27980" \
    --model "Qwen/Qwen3-8B" \
    --lora
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  response = client.fine_tuning.create(
      training_file=file_resp.id,
      model="Qwen/Qwen3-8B",
      lora=True,
  )

  print(response)
  ```
</CodeGroup>

### Full Fine-tuning

<CodeGroup>
  ```sh CLI theme={null}
  together fine-tuning create \
    --training-file "file-629e58b4-ff73-438c-b2cc-f69542b27980" \
    --model "Qwen/Qwen3-8B" \
    --no-lora
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  response = client.fine_tuning.create(
      training_file="file-629e58b4-ff73-438c-b2cc-f69542b27980",
      model="Qwen/Qwen3-8B",
      lora=False,
  )

  print(response)
  ```
</CodeGroup>

You can specify many more fine-tuning parameters to customize your job. See the full list of hyperparameters and their definitions [here](/reference/cli/finetune).

## Monitoring Your Fine-tuning Job

Fine-tuning can take time depending on the model size, dataset size, and hyperparameters. Your job will progress through several states: Pending, Queued, Running, Uploading, and Completed.

**Dashboard Monitoring**

You can monitor your job on the [Together AI jobs dashboard](https://api.together.ai/jobs).

**Check Status via API**

<CodeGroup>
  ```sh CLI theme={null}
  together fine-tuning retrieve "your-job-id"

  together fine-tuning list-events "your-job-id"
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  # Check status of the job
  resp = client.fine_tuning.retrieve("your-job-id")
  print(resp.status)

  # List events for the job
  for event in client.fine_tuning.list_events(id="your-job-id").data:
      print(event.message)
  ```
</CodeGroup>

## Using Your Fine-tuned Model

Once your fine-tuning job completes, your model will be available for use. You can view your fine-tuned models in [your models dashboard](https://api.together.xyz/models).

### Dedicated Endpoint Deployment

You can deploy your fine-tuned model on a dedicated endpoint for production use:

1. Visit [your models dashboard](https://api.together.xyz/models)
2. Find your fine-tuned model and click **"+ CREATE DEDICATED ENDPOINT"**
3. Select your hardware configuration and scaling options
4. Click **"DEPLOY"**

You can also deploy programmatically:

```python  theme={null}
import os
from together import Together

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

response = client.endpoints.create(
    display_name="Fine-tuned Qwen3-8B Function Calling",
    model="your-username/Qwen3-8B-your-suffix",
    hardware="4x_nvidia_h100_80gb_sxm",
    autoscaling={"min_replicas": 1, "max_replicas": 1},
)

print(response)
```

Running this code will deploy a dedicated endpoint, which incurs charges. For detailed documentation around how to deploy, delete and modify endpoints see the [Endpoints API Reference](/reference/createendpoint).

For more details, read the detailed walkthrough [How-to: Fine-tuning](/docs/finetuning).


Built with [Mintlify](https://mintlify.com).