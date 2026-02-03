# Source: https://docs.baseten.co/engines/performance-concepts/deployment-from-training-and-s3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy training and S3 checkpoints

> Deploy training checkpoints and cloud storage models with TensorRT-LLM optimization.

Deploy training checkpoints and cloud storage models with Engine-Builder-LLM, BEI, or BIS-LLM.

## Training checkpoint deployment

Deploy fine-tuned models from Baseten Training with Engine-Builder-LLM. Specify `BASETEN_TRAINING` as the source:

```yaml config.yaml theme={"system"}
model_name: My Fine-Tuned LLM
resources:
  accelerator: H100:1
  use_gpu: true
secrets:
  hf_access_token: null # do not set value here
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: BASETEN_TRAINING
      repo: YOUR_TRAINING_JOB_ID
      revision: checkpoint-100
```

**Key fields:**

* `base_model`: `decoder` for LLMs, `encoder`/`encoder_bert` for embeddings
* `source`: `BASETEN_TRAINING` for Baseten Training checkpoints
* `repo`: Your training job ID
* `revision`: Checkpoint folder name (e.g., `checkpoint-100`, `checkpoint-final`)

Find your checkpoint details with:

```sh  theme={"system"}
truss train get_checkpoint_urls --job-id=YOUR_TRAINING_JOB_ID
```

### Encoder model requirements

To deploy a fine-tuned encoder model (embeddings, rerankers) from training checkpoints, use `encoder` or `encoder_bert` as the base model:

```yaml config.yaml theme={"system"}
model_name: My Fine-Tuned Embeddings
resources:
  accelerator: L4:1
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: BASETEN_TRAINING
      repo: YOUR_TRAINING_JOB_ID
      revision: checkpoint-final
  runtime:
    webserver_default_route: /v1/embeddings
```

Use `encoder_bert` for BERT-based models (sentence-transformers, classification, reranking). Use `encoder` for causal embedding models.

Encoder models have specific requirements:

* **No tensor parallelism**: Omit `tensor_parallel_count` or set it to `1`.
* **Fast tokenizer required**: Your checkpoint must include a `tokenizer.json` file. Models using only the legacy `vocab.txt` format are not supported.
* **Embedding model files**: For sentence-transformer models, include `modules.json` and `1_Pooling/config.json` in your checkpoint.

The `webserver_default_route` configures the inference endpoint. Options include `/v1/embeddings` for embeddings, `/rerank` for rerankers, and `/predict` for classification.

## Cloud storage deployment

Deploy models directly from S3, GCS, or Azure. Specify the storage source and bucket path:

```yaml config.yaml theme={"system"}
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: S3  # or GCS, AZURE, HF
      repo: s3://your-bucket/path/to/model/
```

**Storage sources:**

* `S3`: Amazon S3 buckets
* `GCS`: Google Cloud Storage
* `AZURE`: Azure Blob Storage
* `HF`: Hugging Face repositories

### Private storage setup

All runtimes use the same downloader system as [model\_cache](/development/model/model-cache). As a result, you configure the `runtime_secret_name` and `repo` identically across model\_cache and runtimes like Engine-Builder-LLM or BEI.

**Secret Setup:**

Add these JSON secrets to your [Baseten secrets manager](https://app.baseten.co/settings/secrets).
For more details, refer to the documentation in [model\_cache](/development/model/model-cache).

**S3:**

```json  theme={"system"}
{
  "access_key_id": "XXXXX",
  "secret_access_key": "xxxxx/xxxxxx",
  "region": "us-west-2"
}
```

**GCS:**

```json  theme={"system"}
{
  "private_key_id": "xxxxxxx",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMI",
  "client_email": "b10-some@xxx-example.iam.gserviceaccount.com"
}
```

**Azure:**

```json  theme={"system"}
{
  "account_key": "xxxxx"
}
```

Reference the secret in your config:

```yaml  theme={"system"}
secrets:
  aws_secret_json: "set token in baseten workspace"
trt_llm:
  build:
    checkpoint_repository:
      source: S3
      repo: s3://your-private-bucket/model
      runtime_secret_name: aws_secret_json
```

**For Baseten Training deployments:** These secrets are automatically mounted and available to your deployment.

## Further reading

* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Complete build and runtime options for LLMs.
* [BEI reference configuration](/engines/bei/bei-reference): Complete configuration for encoder models.
* [Model cache documentation](/development/model/model-cache): Caching strategies used by the engines.
* [Secrets management](/development/model/secrets): Configure credentials for private storage.
