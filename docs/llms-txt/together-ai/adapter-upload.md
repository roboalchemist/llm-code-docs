# Source: https://docs.together.ai/docs/adapter-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a LoRA Adapter

> Bring Your Own Adapter: Upload your own LoRA adapter and run inference on Together AI

## Overview

Together AI supports uploading and running inference on custom [LoRA (Low-Rank Adaptation) adapters](/docs/lora-training-and-inference) that you've trained independently or obtained from sources like the Hugging Face Hub.

### Key benefits

* **Serverless deployment**: No infrastructure management required
* **Fast inference**: Optimized for low latency
* **Private models**: Your adapters remain private to your account
* **Multiple sources**: Support for AWS S3 and Hugging Face Hub repositories

### Supported base models

Currently, LoRA inference is supported for adapters based on the following base models in Together API. Whether using pre-fine-tuned models or bringing your own adapters, these are the only compatible models:

| Organization | Base Model Name               | Base Model String                             | Quantization |
| :----------- | :---------------------------- | :-------------------------------------------- | :----------- |
| Meta         | Llama 4 Maverick Instruct     | meta-llama/Llama-4-Maverick-17B-128E-Instruct | FP8          |
| Alibaba      | Qwen3 235B A22B Instruct 2507 | Qwen/Qwen3-235B-A22B-Instruct-2507-tput       | FP8          |

## Implemenation guide

### Prerequisites

* Together AI API key
* Compatible LoRA adapter files:
  If you are getting the adapter from Hugging Face Hub you can find information about the base model there as well.
  You need to make sure that the adapter you are trying to upload has an `adapter_config.json` and `adapter_model.safetensors` files.
* Adapter hosted on AWS S3 or Hugging Face Hub

### Upload from S3

<CodeGroup>
  ```curl cURL theme={null}
  #!/bin/bash
  # uploadadapter.sh

  # Generate presigned adapter url
  ADAPTER_URL="s3://test-s3-presigned-adapter/my-70B-lora-1.zip"
  PRESIGNED_ADAPTER_URL=$(aws s3 presign ${ADAPTER_URL})

  # Specify additional params
  MODEL_TYPE="adapter"
  ADAPTER_MODEL_NAME="test-lora-model-70B-1"
  BASE_MODEL="meta-llama/Meta-Llama-3.1-70B-Instruct"
  DESCRIPTION="test_70b_lora_description" # Lazy curl replace below, don't put spaces here.

  # Upload
  curl -v https://api.together.xyz/v0/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "model_name": "'${ADAPTER_MODEL_NAME}'",
    "model_source": "'${PRESIGNED_ADAPTER_URL}'",
    "model_type": "'${MODEL_TYPE}'",
    "base_model": "'${BASE_MODEL}'",
    "description": "'${DESCRIPTION}'"
  }'
  ```
</CodeGroup>

### Upload from the Hugging Face Hub

Make sure that the adapter contains `adapter_config.json` and `adapter_model.safetensors` files in Files and versions tab on the Hugging Face Hub.

<CodeGroup>
  ```curl cURL theme={null}
  # From the Hugging Face Hub
  HF_URL="https://huggingface.co/your-adapter-repo"

  MODEL_TYPE="adapter"
  BASE_MODEL="meta-llama/Llama-4-Maverick-17B-128E-Instruct"
  DESCRIPTION="test_lora"
  ADAPTER_MODEL_NAME=test-lora-model-creation
  HF_TOKEN=hf_token
  TOGETHER_API_KEY=together-api-key

  # Upload
  curl -v https://api.together.xyz/v0/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "model_name": "'${ADAPTER_MODEL_NAME}'",
    "model_source": "'${HF_URL}'",
    "model_type": "'${MODEL_TYPE}'",
    "description": "'${DESCRIPTION}'",
    "hf_token": "'${HF_TOKEN}'"
  }'
  ```
</CodeGroup>

### Upload response

Successful upload returns:

<CodeGroup>
  ```json JSON theme={null}
  {
    "data": {
      "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",   <------- Job ID
      "model_name": "devuser/test-lora-model-creation-8b",
      "model_source": "remote_archive"
    },
    "message": "job created"
  }
  ```
</CodeGroup>

### Monitor upload progress

You can poll the API using the `job_id` until the adapter has finished uploading.

<CodeGroup>
  ```curl cURL theme={null}
  curl https://api.together.xyz/v1/jobs/job-b641db51-38e8-40f2-90a0-5353aeda6f21 \
    -H "Authorization: Bearer $TOGETHER_API_KEY" | jq .
  ```
</CodeGroup>

Response when ready:

<CodeGroup>
  ```json JSON theme={null}
  {
    "type": "adapter_upload",
    "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
    "status": "Complete",
    "status_updates": []
  }
  ```
</CodeGroup>

### Run LoRA inference:

Use the `model_name` string from the adapter upload.

<CodeGroup>
  ```json JSON theme={null}
  {
    "data": {
      "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
      "model_name": "devuser/test-lora-model-creation-8b",      <------ Model Name
      "model_source": "remote_archive"
    },
    "message": "job created"
  }
  ```
</CodeGroup>

**Make Together API call to the model:**

<CodeGroup>
  ```curl cURL theme={null}
  MODEL_NAME_FOR_INFERENCE="devuser/test-lora-model-creation-8b"

   curl -X POST https://api.together.xyz/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "'$MODEL_NAME_FOR_INFERENCE'",
      "prompt": "Q: The capital of France is?\nA:",
      "temperature": 0.8,
      "max_tokens": 128
    }'
  ```
</CodeGroup>

Expected response:

<CodeGroup>
  ```json JSON theme={null}
  {
    "id": "8f3317dd3c3a39ef-YYZ",
    "object": "text.completion",
    "created": 1734398453,
    "model": "devuser/test-lora-model-creation-8b",
    "prompt": [],
    "choices": [
      {
        "text": " Paris\nB: Berlin\nC: Warsaw\nD: London\nAnswer: A",
        "finish_reason": "eos",
        "seed": 13424880326038300000,
        "logprobs": null,
        "index": 0
      }
    ],
    "usage": {
      "prompt_tokens": 10,
      "completion_tokens": 18,
      "total_tokens": 28,
      "cache_hit_rate": 0
    }
  }
  ```
</CodeGroup>

## Troubleshooting

#### 1. "Model name already exists" Error

**Problem:** Attempting to upload with a duplicate model name

**Solution:** Choose a unique model name for your adapter

#### 2. Missing Required Files

**Problem:** Adapter missing `adapter_config.json` or `adapter_model.safetensors`

**Solution:** Ensure both files are present in your source location before uploading

#### 3. Base Model Incompatibility

**Problem:** Adapter trained on unsupported base model

**Solution:** Verify your adapter was trained on one of the supported base models listed above

#### 4. Upload Job Stuck in "Processing"

**Problem:** Job status remains "Processing" for extended period

**Solution:**

* Check if file size exceeds limits for your tier
* Verify presigned URL hasn't expired (for S3)
* Ensure Hugging Face token has proper permissions (for private repos)

#### 5. Authentication Errors

**Problem:** 401 or 403 errors during upload

**Solution:**

* Verify your Together API key is valid
* For Hugging Face Hub private repos, ensure HF token is included
* For S3, check presigned URL is properly generated

### FAQs

#### Q: Can I upload adapters trained on platforms other than Together AI?

A: Yes, as long as the adapter is compatible with one of our supported base models and includes the required files

#### Q: Can I update an existing adapter?

A: Currently, you need to upload with a new model name. Adapter versioning is not yet supported.


Built with [Mintlify](https://mintlify.com).