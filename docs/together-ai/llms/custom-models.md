# Source: https://docs.together.ai/docs/custom-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a Model

> Run inference on your custom or fine-tuned models

You can upload models from Hugging Face or S3 and run inference on a dedicated endpoint through Together AI.

## Getting Started

### Requirements

Currently, we support models that meet the following criteria:

* **Source**: We support uploads from Hugging Face or S3.
* **Type**: We support text generation and embedding models.
* **Scale**: We currently only support models that fit in a single node. Multi-node models are not supported.

### Model file structure

Your model files must be in standard Hugging Face model repository format, compatible with `from_pretrained` loading. A valid model directory should contain files like:

```
config.json
generation_config.json
model-00001-of-00004.safetensors
model-00002-of-00004.safetensors
model-00003-of-00004.safetensors
model-00004-of-00004.safetensors
model.safetensors.index.json
special_tokens_map.json
tokenizer.json
tokenizer_config.json
```

### Uploading from Hugging Face

When uploading from Hugging Face, simply provide the repository path (e.g., `meta-llama/Llama-2-7b-hf`). The model will be fetched directly from the Hugging Face Hub. You'll also need to provide your Hugging Face token.

### Uploading from S3

When uploading from S3, you must provide a presigned URL pointing to a single archive file containing the model files.

**Supported archive formats:**

* `.zip`
* `.tar`
* `.tar.gz`

**Archive structure requirements:**

The model files must be at the root of the archive, not nested inside an extra top-level directory.

✅ **Correct** - files at root:

```
config.json
model.safetensors
tokenizer.json
...
```

❌ **Incorrect** - files nested in a directory:

```
my-model/
  config.json
  model.safetensors
  tokenizer.json
  ...
```

If you have a model directory, create the archive from within the directory:

```bash  theme={null}
cd /path/to/your/model
tar -czvf ../model.tar.gz .
```

**Presigned URL requirements:**

* The presigned URL must point to the archive file in S3.
* The presigned URL expiration time must be at least **100 minutes**.

### Upload the model

Model uploads can be done via the UI or CLI.

#### UI

To upload via the web, log in and navigate to models > upload a model to reach [this page](https://api.together.xyz/models/upload):

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d389f0262abf19e2b6b1ca0946b52def" alt="Upload model" width="3066" height="1100" data-path="images/docs/c68be312d1d50dab706473dd648224e2a1a132a3149c19ba36a5a23243fdf901-Screenshot_2025-03-27_at_10.09.47.png" />
</Frame>

Then fill in the source URL (Hugging Face repo path or S3 presigned URL), the model name and how you would like it described in your Together account once uploaded.

#### CLI

Upload a model from Hugging Face or S3:

<CodeGroup>
  ```bash CLI theme={null}
  together models upload \
    --model-name <your_model_name> \
    --model-source <path_to_model_or_repo> \
    --hf-token <your_HF_token>
  ```
</CodeGroup>

| Option           | Required     | Description                                                    |
| ---------------- | ------------ | -------------------------------------------------------------- |
| `--model-name`   | Yes          | The name to give to your uploaded model                        |
| `--model-source` | Yes          | Hugging Face repo path or S3 presigned URL                     |
| `--hf-token`     | Yes (for HF) | Your Hugging Face token. Required for most Hugging Face models |
| `--model-type`   | No           | `model` (default) or `adapter`                                 |
| `--description`  | No           | A description of your model                                    |

### Checking the status of your upload

When an upload has been kicked off, it will return a job id. You can poll our API using the returned job id until the model has finished uploading.

<CodeGroup>
  ```curl cURL theme={null}
  curl -X GET "https://api.together.ai/v1/jobs/{jobId}" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
  ```
</CodeGroup>

The output contains a "status" field. When the "status" is "Complete", your model is ready to be deployed.

### Deploy the model

Uploaded models are treated like any other dedicated endpoint models. Deploying can be done via the UI or CLI.

#### UI

All models, custom and finetuned models as well as any model that has a dedicated endpoint will be listed under [My Models](https://api.together.ai/models). To deploy:

Select the model to open the model page.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7ac4fb3f82d0470fc70cecd4464e363f" alt="My Models" width="2828" height="560" data-path="images/docs/7b710ddcba7873b0154ef5945f5aa36bd0627ab3791882f8f73a30e2942e5470-Screenshot_2025-03-13_at_6.14.17_AM.png" />
</Frame>

The model page will display details from your uploaded model with an option to create a dedicated endpoint.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5b945031b73a5d2339b72b7610dc06ba" alt="Create Dedicated Endpoint" width="1996" height="1278" data-path="images/docs/2bdec7e6a9d20983e2279c0e5e7f41985db97a510fb71c5428bd2108e16cbdd7-Screenshot_2025-03-13_at_6.12.55_AM.png" />
</Frame>

When you select 'Create Dedicated Endpoint' you will see an option to configure the deployment.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fe01ff81c139d77cac9e2b06a73213e0" alt="Create Dedicated Endpoint" width="2014" height="1284" data-path="images/docs/c2a00bdf78bf334eabc05da86b06de88a35fe948c1462dd4dab003fa818f63fa-Screenshot_2025-03-13_at_6.13.14_AM.png" />
</Frame>

Once an endpoint has been deployed, you can interact with it on the playground or via the API.

#### CLI

After uploading your model, you can verify its registration and check available hardware options.

**List your uploaded models:**

<CodeGroup>
  ```bash CLI theme={null}
  together models list
  ```
</CodeGroup>

**View available GPU SKUs for a specific model:**

<CodeGroup>
  ```bash CLI theme={null}
  together endpoints hardware --model <model-name>
  ```
</CodeGroup>

Once your model is uploaded, create a dedicated inference endpoint:

<CodeGroup>
  ```bash CLI theme={null}
  together endpoints create \
    --display-name <endpoint-name> \
    --model <model-name> \
    --gpu h100 \
    --no-speculative-decoding \
    --gpu-count 2
  ```
</CodeGroup>

After deploying, you can view all your endpoints and retrieve connection details such as URL, scaling configuration, and status.

**List all endpoints:**

<CodeGroup>
  ```bash CLI theme={null}
  together endpoints list
  ```
</CodeGroup>

**Get details for a specific endpoint:**

<CodeGroup>
  ```bash CLI theme={null}
  together endpoints get <endpoint-id>
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).