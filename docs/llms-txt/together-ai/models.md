# Source: https://docs.together.ai/reference/models.md

# Source: https://docs.together.ai/reference/cli/models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Models

## Setup

See our [Getting Started](/reference/cli/getting-started) guide for initial setup.

## Upload

You can upload models from Hugging Face or S3 and run inference on a dedicated endpoint through Together AI.
For more information, see our Dedicated Inference [docs](/docs/custom-models)

<CodeGroup>
  ```sh Basic Example theme={null}
  together models upload
      --model-name [TEXT]
      --model-source [URI]
  ```

  ```sh HF Upload theme={null}
  # Upload model from HF.
  together models upload
      --model-name together-m1-3b-personal-clone
      --model-source https://huggingface.co/togethercomputer/M1-3B
      --hf-token $(echo $HUGGINGFACEHUB_API_TOKEN)
  ```

  ```sh S3 Upload theme={null}
  # Upload model from S3.
  PRESIGNED_URL = $(sh ./get-presigned-url)

  together models upload
    --model-name my-s3-upload-model
    --model-source $(echo $PRESIGNED_URL)
  ```
</CodeGroup>

### Options

| Name             | Arguments            | Description                                                                                                                   |
| ---------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `--model-name`   | string               | The name to give to your uploaded model \[**required**]                                                                       |
| `--model-source` | string               | The source uri of the model  \[**required**]                                                                                  |
| `--model-type`   | `model` or `adapter` | Whether the model is a full model or an adapter                                                                               |
| `--hf-token`     | string               | Hugging Face token (if uploading from Hugging Face)                                                                           |
| `--description`  | string               | A description of your model                                                                                                   |
| `--base-model`   | string               | The base model to use for an adapter if setting it to run against a serverless pool. Only used for model\_type 'adapter'.     |
| `--lora-model`   | string               | The lora pool to use for an adapter if setting it to run against, say, a dedicated pool. Only used for model\_type 'adapter'. |
| `--json`         |                      | Output in JSON format                                                                                                         |

## List all models

<CodeGroup>
  ```sh Basic Usage theme={null}
  # List Models
  $ together models list
  ```

  ```sh List Deployable Models theme={null}
  # List models that can be deployed on `together endpoints`
  together models list --type dedicated
  ```

  ```sh JSON output and scripting theme={null}
  # Output in JSON mode and pipe to jq
  together models list --json | jq 'length'
  ```
</CodeGroup>

### Options

| Name     | Description                                                     |
| -------- | --------------------------------------------------------------- |
| `--type` | Filter models by type. `dedicated` is the only available option |
| `--json` | Output in JSON format                                           |


Built with [Mintlify](https://mintlify.com).