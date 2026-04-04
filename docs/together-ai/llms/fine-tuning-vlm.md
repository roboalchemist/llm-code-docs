# Source: https://docs.together.ai/docs/fine-tuning-vlm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vision-Language Fine-tuning

> Learn how to fine-tune Vision-Language Models (VLMs) on image+text data using Together AI.

## Introduction

Vision-Language Models (VLMs) combine the power of language understanding with visual comprehension. Fine-tuning a VLM allows you to adapt it to your specific image+text tasks, such as visual question answering, image captioning, or document understanding.

This guide covers the specific steps for VLM fine-tuning. For general fine-tuning concepts, environment setup, and hyperparameter details, refer to the [Fine-tuning Guide](/docs/fine-tuning-quickstart).

## Quick Links

* [Dataset Requirements](#vlm-fine-tuning-dataset)
* [Supported Models](#supported-models)
* [Check and Upload Dataset](#check-and-upload-dataset)
* [Start a Fine-tuning Job](#starting-a-fine-tuning-job)
* [Monitor Progress](#monitoring-your-fine-tuning-job)
* [Deploy Your Model](#using-your-fine-tuned-model)

## VLM Fine-tuning Dataset

**Dataset Requirements:**

* **Format**: OpenAI-style `.jsonl` file
* **Supported types**: Conversational, Instruction, Preferential - more details on their purpose [here](/docs/fine-tuning-data-preparation#text-data)
* **Images**: Must be base64 encoded with proper MIME type prefixes, maximum 10 images per example, each image is a maximum of 10MB in size.
  * If you have image URLs, please download and encode them in base64 first
* **Supported image formats**: PNG, JPEG, WEBP

<Tip>
  ### Converting Image URLs to Base64

  If your images are stored as URLs, you can convert them to base64 using Python:

  ```python  theme={null}
  import base64
  import requests


  def url_to_base64(url: str, mime_type: str = "image/jpeg") -> str:
      response = requests.get(url)
      encoded = base64.b64encode(response.content).decode("utf-8")
      return f"data:{mime_type};base64,{encoded}"
  ```
</Tip>

**Message Schema:** Each training example must include a `messages` array where each message has:

* `role`: one of `system`, `user`, or `assistant`
* `content`: an array containing text and image objects or just text. Only `user` messages can contain images.

### Conversational Format

This is what one row/example from the VLM dataset looks like in conversation format:

```json  theme={null}
{
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You're helpful AI assistant with vision capabilities."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "How many oranges are in the bowl?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAA..."
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "There are at least 7 oranges in this bowl."
        }
      ]
    }
  ]
}
```

### Instruction Format

```json  theme={null}
{
  "prompt": [
    {
      "type": "text",
      "text": "How many oranges are in the bowl?"
    },
    {
      "type": "image_url",
      "image_url": {
        "url": "data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAA..."
      }
    }
  ],
  "completion": [
    {
      "type": "text",
      "text": "There are at least 7 oranges in this bowl."
    }
  ]
}
```

### Preferential Format

```json  theme={null}
{
  "input": {
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "How many oranges are in the bowl?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAA..."
            }
          }
        ]
      }
    ]
  },
  "preferred_output": [
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "There are at least 7 oranges in this bowl."
        }
      ]
    }
  ],
  "non_preferred_output": [
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "There are a total of 11 oranges in this bowl."
        }
      ]
    }
  ]
}
```

## Supported Models

The following models support VLM fine-tuning:

| Model                                               | Full Fine-tuning | LoRA Fine-tuning |
| --------------------------------------------------- | :--------------: | :--------------: |
| `Qwen/Qwen3-VL-8B-Instruct`                         |         ✅        |         ✅        |
| `Qwen/Qwen3-VL-30B-A3B-Instruct`                    |         ✅        |         ✅        |
| `Qwen/Qwen3-VL-235B-A22B-Instruct`                  |         ❌        |         ✅        |
| `meta-llama/Llama-4-Maverick-17B-128E-Instruct-VLM` |         ❌        |         ✅        |
| `meta-llama/Llama-4-Scout-17B-16E-Instruct-VLM`     |         ❌        |         ✅        |
| `google/gemma-3-4b-it-VLM`                          |         ✅        |         ✅        |
| `google/gemma-3-12b-it-VLM`                         |         ✅        |         ✅        |
| `google/gemma-3-27b-it-VLM`                         |         ✅        |         ✅        |

## Check and Upload Dataset

To upload your data, use the CLI or our Python library:

<CodeGroup>
  ```sh CLI theme={null}
  together files check "vlm_dataset.jsonl"

  together files upload "vlm_dataset.jsonl"
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  file_resp = client.files.upload(file="vlm_dataset.jsonl", check=True)

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
  "filename": "vlm_dataset.jsonl",
  "bytes": 0,
  "line_count": 0,
  "processed": false,
  "FileType": "jsonl"
}
```

You'll be using your file's ID (the string that begins with `file-`) to start your fine-tuning job, so store it somewhere before moving on.

You're now ready to kick off your first fine-tuning job!

## Starting a Fine-tuning Job

We support both LoRA and full fine-tuning for VLMs. See how to start a fine-tuning job with either method below.

### VLM-Specific Parameters

| Parameter                         | Description                                                                                           | Default |
| --------------------------------- | ----------------------------------------------------------------------------------------------------- | :-----: |
| `--train-vision` / `train_vision` | Enable updates to the VLM's vision encoder. When `false`, only language model parameters are updated. | `false` |

<Icon icon="link" iconType="solid" /> For an exhaustive list of all the available fine-tuning parameters, refer to the [Together AI Fine-tuning API Reference](/reference/cli/finetune).

### LoRA Fine-tuning (Recommended)

<CodeGroup>
  ```sh CLI theme={null}
  together fine-tuning create \
    --training-file "file-629e58b4-ff73-438c-b2cc-f69542b27980" \
    --model "Qwen/Qwen3-VL-8B-Instruct" \
    --train-vision false \
    --lora
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  response = client.fine_tuning.create(
      training_file=file_resp.id,
      model="Qwen/Qwen3-VL-8B-Instruct",
      lora=True,
      train_vision=False,
  )

  print(response)
  ```
</CodeGroup>

Specify optional `--train-vision true`  param to enable updates to VLM's vision encoder as well. By default, only language model params are updated.

### Full Fine-tuning

<CodeGroup>
  ```sh CLI theme={null}
  together fine-tuning create \
    --training-file "file-629e58b4-ff73-438c-b2cc-f69542b27980" \
    --model "Qwen/Qwen3-VL-8B-Instruct" \
    --train-vision false \
    --no-lora
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  response = client.fine_tuning.create(
      training_file="file-629e58b4-ff73-438c-b2cc-f69542b27980",
      model="Qwen/Qwen3-VL-8B-Instruct",
      lora=False,
      train_vision=False,
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

### Option 1: Serverless LoRA Inference

If you used LoRA fine-tuning, your model will be instantly available for use without deployment:

<CodeGroup>
  ```sh cURL theme={null}
  curl -X POST https://api.together.xyz/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "your-username/Qwen3-VL-8B-Instruct-your-suffix",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What do you see in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "data:image/jpeg;base64,..."
              }
            }
          ]
        }
      ],
      "max_tokens": 512
    }'
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  response = client.chat.completions.create(
      model="your-username/Qwen3-VL-8B-Instruct-your-suffix",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What do you see in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {"url": "data:image/jpeg;base64,..."},
                  },
              ],
          }
      ],
      max_tokens=512,
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

### Option 2: Dedicated Endpoint Deployment

You can also deploy your fine-tuned VLM on a dedicated endpoint for production use:

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
    display_name="Fine-tuned Qwen3-VL-8B",
    model="your-username/Qwen3-VL-8B-Instruct-your-suffix",
    hardware="4x_nvidia_h100_80gb_sxm",
    autoscaling={"min_replicas": 1, "max_replicas": 1},
)

print(response)
```

⚠️ Running this code will deploy a dedicated endpoint for you, which incurs charges. For detailed documentation around how to deploy, delete and modify endpoints see the [Endpoints API Reference](/reference/createendpoint).

For more details, read the detailed walkthrough [How-to: Fine-tuning](/docs/finetuning).


Built with [Mintlify](https://mintlify.com).