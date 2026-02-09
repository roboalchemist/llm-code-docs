# Source: https://docs.fireworks.ai/models/uploading-custom-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Models

> Upload, verify, and deploy your own models from Hugging Face or elsewhere

Upload your own models from Hugging Face or elsewhere to deploy fine-tuned or custom-trained models optimized for your use case.

* **Multiple upload options** – Upload from local files or directly from S3 buckets or Azure Blob Storage
* **Secure uploads** – All uploads are encrypted and models remain private to your account by default

## Requirements

### Supported architectures

Fireworks supports most popular model architectures, including:

* [DeepSeek V1, V2 & V3](https://huggingface.co/deepseek-ai)
* [Qwen, Qwen2, Qwen2.5, Qwen2.5-VL, Qwen3](https://huggingface.co/Qwen)
* [Kimi K2 family](https://huggingface.co/moonshotai)
* [GLM 4.X family](https://huggingface.co/zai-org)
* [Llama 1, 2, 3, 3.1, 4](https://huggingface.co/docs/transformers/en/model_doc/llama2)
* [Mistral & Mixtral](https://huggingface.co/docs/transformers/en/model_doc/mistral)
* [Gemma](https://huggingface.co/docs/transformers/en/model_doc/gemma)
* [GPT-OSS 120B and 20B](https://huggingface.co/openai/gpt-oss-120b)

<Accordion title="View all supported architectures">
  - [DBRX](https://huggingface.co/docs/transformers/en/model_doc/dbrx)
  - [DeepSeek V1, V2 & V3](https://huggingface.co/deepseek-ai)
  - [Falcon](https://huggingface.co/docs/transformers/en/model_doc/falcon)
  - [Gemma](https://huggingface.co/docs/transformers/en/model_doc/gemma)
  - [GPT NeoX](https://huggingface.co/docs/transformers/en/model_doc/gpt_neox)
  - [Idefics3](https://huggingface.co/docs/transformers/en/model_doc/idefics3)
  - [Llama 1, 2, 3, 3.1, 4](https://huggingface.co/docs/transformers/en/model_doc/llama2)
  - [LLaVA](https://huggingface.co/docs/transformers/main/en/model_doc/llava)
  - [Mistral](https://huggingface.co/docs/transformers/en/model_doc/mistral) & [Mixtral](https://huggingface.co/docs/transformers/en/model_doc/mixtral)
  - [Phi, Phi-3, Phi-3V, Phi-4](https://huggingface.co/docs/transformers/en/model_doc/phi)
  - [Pythia](https://huggingface.co/docs/transformers/en/model_doc/gpt_neox)
  - [Qwen](https://huggingface.co/docs/transformers/en/model_doc/qwen), [Qwen2](https://huggingface.co/docs/transformers/en/model_doc/qwen2), [Qwen2.5](https://huggingface.co/collections/Qwen/qwen25-66e81a666513e518adb90d9e), [Qwen2.5-VL](https://huggingface.co/collections/Qwen/qwen25-vl-6795ffac22b334a837c0f9a5), [Qwen3](https://huggingface.co/Qwen)
  - [Solar](https://huggingface.co/upstage/SOLAR-10.7B-v1.0)
  - [StableLM](https://huggingface.co/docs/transformers/main/en/model_doc/stablelm)
  - [Starcoder (GPTBigCode)](https://huggingface.co/docs/transformers/en/model_doc/gpt_bigcode) & [Starcoder2](https://huggingface.co/docs/transformers/main/en/model_doc/starcoder2)
  - [Vision Llama](https://huggingface.co/docs/transformers/en/model_doc/llama2)
</Accordion>

### Required files

You'll need standard Hugging Face model files: `config.json`, model weights (`.safetensors` or `.bin`), and tokenizer files.

<Accordion title="View detailed file requirements">
  The model files you will need to provide depend on the model architecture. In general, you will need:

  * **Model configuration**: `config.json`

    <Note>
      Fireworks does not support the `quantization_config` option in `config.json`.
    </Note>
  * **Model weights** in one of the following formats:
    * `*.safetensors`
    * `*.bin`
  * **Weights index**: `*.index.json`
  * **Tokenizer file(s)**, e.g.:
    * `tokenizer.model`
    * `tokenizer.json`
    * `tokenizer_config.json`

  If the requisite files are not present, model deployment may fail.
</Accordion>

### Customizing base model configuration

For base models (not LoRA adapters), you can customize the chat template and generation defaults by modifying the standard Hugging Face configuration files:

* **Chat template**: Add or modify the `chat_template` field in `tokenizer_config.json`. See the Hugging Face guide on [Templates for Chat Models](https://huggingface.co/docs/transformers/main/en/chat_templating) for details.
* **Generation defaults**: Modify `generation_config.json` to set default generation parameters like `max_new_tokens`, `temperature`, `top_p`, etc.

You can also use a `fireworks.json` file with base models. If present, `fireworks.json` takes priority over both `tokenizer_config.json` and `generation_config.json`. See [Customizing chat template and generation defaults](#customizing-chat-template-and-generation-defaults) for the full `fireworks.json` schema.

<Warning>
  For LoRA adapters, you must use `fireworks.json` to customize configuration. Modifying `tokenizer_config.json` or `generation_config.json` in the adapter folder won't work because adapters inherit these settings from their base model.
</Warning>

## Uploading your model

For larger models, you can upload directly from cloud storage (S3 or Azure Blob Storage) for faster transfer instead of uploading from your local machine.

<Tabs>
  <Tab title="Local files (CLI)">
    Upload from your local machine:

    ```bash  theme={null}
    firectl model create <MODEL_ID> /path/to/files/
    ```
  </Tab>

  <Tab title="S3 bucket (CLI)">
    Upload directly from an Amazon S3 bucket:

    ```bash  theme={null}
    firectl model create <MODEL_ID> s3://<BUCKET_NAME>/<PATH_TO_MODEL>/ \
      --aws-access-key-id <ACCESS_KEY_ID> \
      --aws-secret-access-key <SECRET_ACCESS_KEY>
    ```

    See the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) for how to generate an access key ID and secret access key pair.

    <Note>
      Ensure the IAM user has read access to the S3 bucket containing the model.
    </Note>
  </Tab>

  <Tab title="Azure Blob Storage (CLI)">
    Upload directly from Azure Blob Storage using either SAS token or federated identity authentication.

    <Tabs>
      <Tab title="SAS token">
        First, create a Fireworks secret containing your Azure SAS token:

        ```bash  theme={null}
        firectl secret create --name <SECRET_NAME> --value <SAS_TOKEN>
        ```

        Then, upload the model using the secret:

        ```bash  theme={null}
        firectl model create <MODEL_ID> https://<STORAGE_ACCOUNT>.blob.core.windows.net/<CONTAINER>/<PATH> \
          --azure-sas-token-secret accounts/<ACCOUNT_ID>/secrets/<SECRET_NAME>
        ```

        See the [Azure documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview) for how to generate a SAS token.

        <Note>
          Ensure the SAS token has read access to the Azure Blob Storage container containing the model.
        </Note>
      </Tab>

      <Tab title="Federated identity">
        Use Azure AD federated identity for passwordless authentication.

        **Setup:** Register an Azure AD application and add a federated credential with:

        * **Issuer:** `https://accounts.google.com`
        * **Subject:** `114308823136673488563`
        * **Audience:** `api://AzureADTokenExchange`

        Then grant **Storage Blob Data Reader** role to the application on your storage account.

        ```bash  theme={null}
        firectl model create <MODEL_ID> https://<STORAGE_ACCOUNT>.blob.core.windows.net/<CONTAINER>/<PATH> \
          --azure-client-id <CLIENT_ID> \
          --azure-tenant-id <TENANT_ID>
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="REST API">
    For programmatic uploads (automation, CI/CD pipelines), use the Fireworks REST API with a 4-step process: create model → get upload URLs → upload files → validate.

    See the [REST API upload guide](/models/uploading-custom-models-api) for a complete Python example.
  </Tab>
</Tabs>

<Note>
  If you're uploading an embedding model, add the `--embedding` flag.
</Note>

## Verifying your upload

After uploading, verify your model is ready to deploy:

```bash  theme={null}
firectl model get accounts/<ACCOUNT_ID>/models/<MODEL_NAME>
```

Look for `State: READY` in the output. Once ready, you can create a deployment.

## Deploying your model

Once your model shows `State: READY`, create a deployment:

```bash  theme={null}
firectl deployment create accounts/<ACCOUNT_ID>/models/<MODEL_NAME> --wait
```

See the [On-demand deployments guide](/guides/ondemand-deployments) for configuration options like GPU types, autoscaling, and quantization.

## Publishing your model

By default, models are private to your account. Publish a model to make it available to other Fireworks users.

**When published:**

* Listed in the public model catalog
* Deployable by anyone with a Fireworks account
* Still hosted and controlled by your account

**Publish a model:**

```bash  theme={null}
firectl model update <MODEL_ID> --public
```

**Unpublish a model:**

```bash  theme={null}
firectl model update <MODEL_ID> --public=false
```

## Importing fine-tuned models

In addition to models you fine-tune on the Fireworks platform, you can also upload your own custom fine-tuned models as LoRA adapters.

### Requirements

Your custom LoRA addon must contain the following files:

* `adapter_config.json` - The Hugging Face adapter configuration file
* `adapter_model.bin` or `adapter_model.safetensors` - The saved addon file

The `adapter_config.json` must contain the following fields:

* `r` - The number of LoRA ranks. Must be an integer between 4 and 64, inclusive
* `target_modules` - A list of target modules. Currently the following target modules are supported:
  * `q_proj`
  * `k_proj`
  * `v_proj`
  * `o_proj`
  * `up_proj` or `w1`
  * `down_proj` or `w2`
  * `gate_proj` or `w3`
  * `block_sparse_moe.gate`

Additional fields may be specified but are ignored.

### Customizing chat template and generation defaults

For LoRA adapters, use a `fireworks.json` file to customize the chat template and generation defaults. This is the recommended approach because adapters inherit configuration from their base model—modifying `generation_config.json` or `tokenizer_config.json` in the adapter folder won't work.

Add a `fireworks.json` file to the directory containing your adapter files:

```json fireworks.json theme={null}
{
  "conversation_config": {
    "style": "jinja",
    "args": {
      "template": "{% for message in messages %}...",
      "system": "optional system prompt",
      "special_tokens_map": {
        "bos_token": "<s>",
        "eos_token": "</s>",
        "unk_token": "<unk>"
      },
      "keep_leading_spaces": true,
      "function_call_prefix": "...",
      "function_call_suffix": "...",
      "disable_grammar": false
    }
  },
  "defaults": {
    "stop": ["<|im_end|>", "</s>"],
    "max_tokens": 1024,
    "temperature": 0.7,
    "top_k": 50,
    "top_p": 0.9,
    "min_p": 0.0,
    "typical_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "repetition_penalty": 1.0
  },
  "model_arch": null,
  "model_config_name": null,
  "has_lora": true,
  "has_teft": false
}
```

<AccordionGroup>
  <Accordion title="conversation_config options">
    | Field                       | Required          | Description                                              |
    | --------------------------- | ----------------- | -------------------------------------------------------- |
    | `style`                     | Yes               | Template style (see supported styles below)              |
    | `args.template`             | Yes (for `jinja`) | Jinja2 template string for formatting messages           |
    | `args.system`               | No                | Default system prompt                                    |
    | `args.special_tokens_map`   | No                | Token mappings for `bos_token`, `eos_token`, `unk_token` |
    | `args.keep_leading_spaces`  | No                | Preserve leading whitespace in the template output       |
    | `args.function_call_prefix` | No                | Prefix for tool/function calls                           |
    | `args.function_call_suffix` | No                | Suffix for tool/function calls                           |
    | `args.disable_grammar`      | No                | Disable grammar constraints                              |

    **Supported conversation styles:**

    | Style                    | Description                                       |
    | ------------------------ | ------------------------------------------------- |
    | `jinja`                  | Custom Jinja2 template (requires `args.template`) |
    | `huggingface`            | Uses the model's HuggingFace chat template        |
    | `alpaca`                 | Alpaca instruction format                         |
    | `chatml`                 | ChatML format                                     |
    | `codellama-70b-instruct` | CodeLlama 70B instruction format                  |
    | `deepseek`               | DeepSeek format                                   |
    | `deepseek-v3p1`          | DeepSeek V3.1 format                              |
    | `deepseek-v3p2`          | DeepSeek V3.2 format                              |
    | `glm`                    | GLM format                                        |
    | `glm_47`                 | GLM 4.7 format                                    |
    | `harmony`                | Harmony format                                    |
    | `kimi`                   | Kimi format                                       |
    | `kimi-k2-instruct`       | Kimi K2 instruction format                        |
    | `llama-chat`             | Llama chat format                                 |
    | `llama-infill`           | Llama infilling format                            |
    | `llama4`                 | Llama 4 format                                    |
    | `minimax`                | MiniMax format                                    |
    | `minimax_m2`             | MiniMax M2 format                                 |
    | `mistral-chat`           | Mistral chat format                               |
    | `passthrough`            | No formatting applied                             |
    | `qwen2`                  | Qwen2 format                                      |
    | `qwen3`                  | Qwen3 format                                      |
    | `qwen3-coder`            | Qwen3 Coder format                                |
    | `qwen3-vl`               | Qwen3 Vision-Language format                      |
    | `qwen3-vl-moe`           | Qwen3 Vision-Language MoE format                  |
    | `stablelm-zephyr`        | StableLM Zephyr format                            |
    | `vicuna`                 | Vicuna chat format                                |
  </Accordion>

  <Accordion title="defaults options">
    These defaults are applied when the user doesn't specify values in their API request:

    | Field                | Type    | Example                    | Description                           |
    | -------------------- | ------- | -------------------------- | ------------------------------------- |
    | `stop`               | array   | `["<\|im_end\|>", "</s>"]` | Default stop sequences                |
    | `max_tokens`         | integer | `1024`                     | Default maximum tokens to generate    |
    | `temperature`        | float   | `0.7`                      | Default sampling temperature          |
    | `top_k`              | integer | `50`                       | Default top-k sampling                |
    | `top_p`              | float   | `0.9`                      | Default nucleus sampling probability  |
    | `min_p`              | float   | `0.0`                      | Default minimum probability threshold |
    | `typical_p`          | float   | `1.0`                      | Default typical sampling probability  |
    | `frequency_penalty`  | float   | `0.0`                      | Default frequency penalty             |
    | `presence_penalty`   | float   | `0.0`                      | Default presence penalty              |
    | `repetition_penalty` | float   | `1.0`                      | Default repetition penalty            |
  </Accordion>

  <Accordion title="Additional options">
    | Field               | Default | Description                                                                            |
    | ------------------- | ------- | -------------------------------------------------------------------------------------- |
    | `model_arch`        | null    | Model architecture (e.g., `"qwen2"`, `"llama"`). Usually auto-detected from base model |
    | `model_config_name` | null    | Model configuration name (e.g., `"4B"`). Usually auto-detected from base model         |
    | `has_lora`          | true    | Set to `true` for LoRA adapters                                                        |
    | `has_teft`          | false   | Set to `true` if using TEFT (Token-Efficient Fine-Tuning)                              |
  </Accordion>
</AccordionGroup>

<Note>
  All fields in `fireworks.json` are optional except for `conversation_config.style` when customizing the chat template. Include only the fields you need to override.
</Note>

### Uploading the LoRA adapter

To upload a LoRA addon, run the following command. The MODEL\_ID is an arbitrary [resource ID](/getting-started/concepts#resource-names-and-ids) to refer to the model within Fireworks.

<Note>
  Only some base models support LoRA addons.
</Note>

```bash  theme={null}
firectl model create <MODEL_ID> /path/to/files/ --base-model "accounts/fireworks/models/<BASE_MODEL_ID>"
```

## Next steps

<CardGroup cols={3}>
  <Card title="Deploy your model" icon="rocket" href="/guides/ondemand-deployments">
    Configure GPU types, autoscaling, and optimization
  </Card>

  <Card title="Quantization" icon="compress" href="/models/quantization">
    Reduce serving costs with model quantization
  </Card>

  <Card title="Fine-tuning" icon="wand-magic-sparkles" href="/fine-tuning/finetuning-intro">
    Fine-tune models before deploying them
  </Card>
</CardGroup>
