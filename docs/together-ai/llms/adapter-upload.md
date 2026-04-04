# Source: https://docs.together.ai/docs/adapter-upload.md

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

| Organization | Base Model Name           | Base Model String                                | Quantization |
| :----------- | :------------------------ | :----------------------------------------------- | :----------- |
| Meta         | Llama 4 Maverick Instruct | meta-llama/Llama-4-Maverick-17B-128E-Instruct    | FP8          |
| Meta         | Llama 3.1 8B Instruct     | meta-llama/Meta-Llama-3.1-8B-Instruct-Reference  | BF16         |
| Meta         | Llama 3.1 70B Instruct    | meta-llama/Meta-Llama-3.1-70B-Instruct-Reference | BF16         |
| Alibaba      | Qwen2.5 14B Instruct      | Qwen/Qwen2.5-14B-Instruct                        | FP8          |
| Alibaba      | Qwen2.5 72B Instruct      | Qwen/Qwen2.5-72B-Instruct                        | FP8          |

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
  HF_URL="https://huggingface.co/reissbaker/llama-3.1-8b-abliterated-lora"

  MODEL_TYPE="adapter"
  BASE_MODEL="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference"
  DESCRIPTION="test_lora_8B"
  ADAPTER_MODEL_NAME=test-lora-model-creation-8b
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

#### Q: What are the adapter limits based on my tier?

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f27e607b8a55dfa1016c1954168ed2cd" alt="" data-og-width="1210" width="1210" data-og-height="800" height="800" data-path="images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5a87885e453221fd1c1916bffa8fa683 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d9b1785fa2d5bb1ff45b88abd4ba4d31 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c3bd41e1355239974123600a03114b7c 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d96222e04affc12d32d58c64c4b2cd71 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=72eeecb9e1a069c700ce19539a7ab5c8 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/bc98169540fb29568558f6882c1a1ac8d2fb988269c49742b26a91afa1241094-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a188a9c10919e3006d5adfb866bb5a0e 2500w" />
</Frame>

#### Q: Can I upload adapters trained on platforms other than Together AI?

A: Yes, as long as the adapter is compatible with one of our supported base models and includes the required files

#### Q: Can I update an existing adapter?

A: Currently, you need to upload with a new model name. Adapter versioning is not yet supported.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt