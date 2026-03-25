# Source: https://docs.anyscale.com/llm/fine-tuning/checkpointing.md

# Save and resume checkpoints and finalize models

[View Markdown](/llm/fine-tuning/checkpointing.md)

# Save and resume checkpoints and finalize models

tip

This guide uses LlamaFactory as an example framework. Anyscale supports multiple frameworks for LLM post-training. See [Choose a framework for LLM post-training](/llm/fine-tuning/comparison.md).

This guide covers the lifecycle of fine-tuning or post-training artifacts when using LLaMA-Factory on Anyscale. You learn how to locate training artifacts and checkpoints, resume a paused or failed run, and merge a LoRA adapter with a pretrained model into a single, low-latency inference model.

## Understand the training artifacts directory[​](#artifacts-directory "Direct link to Understand the training artifacts directory")

Given this configuration:

```
# qwen_lora_sft.yaml
### output
save_strategy: steps # Or 'epoch' to save at the end of every epoch.
save_steps: 100

### Train
per_device_train_batch_size: 2
gradient_accumulation_steps: 4
num_train_epochs: 3

### Ray
ray_run_name: qwen2_7b_sft_lora # Save directory name.
ray_storage_path: /mnt/cluster_storage/ # Shared storage between head and worker nodes.
ray_num_workers: 4
```

Training writes checkpoints, configs, and logs to the `ray_storage_path` and `ray_run_name` that you specify in the YAML config.

## Locate checkpoint paths[​](#checkpoint-paths "Direct link to Locate checkpoint paths")

**Checkpoints** are snapshots of training state that let you resume runs without starting over. These checkpoints usually include optimizer state, schedulers, and weight tensors.

The weight tensors depend on the fine-tuning method:

* **LoRA or QLoRA** → adapter weights only (`adapter_model.safetensors`), about 1% of the model weights.

* **Full or freeze tuning** outputs the full model weights (`model.safetensors`).

  * **Full fine-tuning**: Saves all parameters in a uniform, high-precision format (FP32).
  * **Freeze tuning**: Saves a mix of data types, with updated layers in FP32 and frozen layers in their original precision (for example, BF16).

note

For both methods, consider applying post-training quantization (PTQ). It unifies precision, reduces model size, and accelerates inference. See [Post-training quantization (PTQ)](#ptq).

The output directory contains a folder named `{ray_storage_path}/{ray_run_name}/TorchTrainer_{x}/checkpoint_{x}/checkpoint` with the following structure:

```
checkpoint/
├── adapter_model.safetensors  # LoRA adapter weights for LoRA / QLoRA
├── model.safetensors          # Full model weights for Full fine-tuning or Freeze tuning
├── optimizer.pt               # States of the trainer including the current step, epoch, and metric history
├── scheduler.pt               # States of the learning rate scheduler
├── trainer_state.json         # State for resuming training
├── tokenizer.json             # Tokenizer data
└── ... and other files
```

## Choose checkpoint frequency[​](#checkpoint-frequency "Direct link to Choose checkpoint frequency")

You can control checkpoint frequency using the `save_strategy` parameter, which accepts two options: 'epoch' or 'steps'.

### Save by epoch[​](#save-by-epoch "Direct link to Save by epoch")

When you set `save_strategy: 'epoch'`, the system saves a checkpoint after each complete pass through the training data. This is straightforward but can be infrequent for very large datasets. The system ignores the `save_steps` parameter with this strategy.

### Save by step[​](#save-by-step "Direct link to Save by step")

Setting `save_strategy: 'steps'` provides more granular control. The system saves checkpoints every `save_steps` optimizer updates.

The `save_steps` parameter controls the frequency of saved checkpoints. A "step" isn't a single batch, but one optimizer update.

Each update processes a batch of examples. The total number of examples in one step is the effective batch size, calculated as:

```
effective_batch_size = per_device_train_batch_size × gradient_accumulation_steps × world_size
```

In this case, `world_size` is the total number of GPUs you're using (for example, `ray_num_workers` × `gpus_per_worker`).

### Example calculation[​](#example-calculation "Direct link to Example calculation")

Using the settings from the configuration:

* `per_device_train_batch_size`: 2
* `gradient_accumulation_steps`: 4
* `world_size`: 4

The effective batch size is `2 × 4 × 4 = 32` examples per step.

With `save_steps: 100`, the system saves a checkpoint every 100 optimizer steps. This saves progress after approximately every 3,200 examples.

## Resume training from checkpoints[​](#resume-from-checkpoints "Direct link to Resume training from checkpoints")

Update the YAML config to point to the saved checkpoint path:

```
# qwen_lora_sft_resume.yaml
resume_from_checkpoint: /mnt/cluster_storage/qwen2_7b_sft_lora/TorchTrainer_x/checkpoint_x/checkpoint # Path to the previously trained checkpoints directory; leave empty to start fresh.
```

note

Resuming is primarily for recovering from interrupted runs. If you resume from a checkpoint of a completed run to train for more epochs, ensure that you configure the number of epochs and learning rate scheduler correctly.

## Increase disk space for checkpoints[​](#disk-space "Direct link to Increase disk space for checkpoints")

If you need more storage capacity for saved checkpoints including model weights, adapters, and logs, increase the default disk size of your instance. For Google Cloud, see [Change the default disk size](/configuration/compute/gcp.md#disk-size). For AWS, see [Change the default disk size](/configuration/compute/aws.md#disk-size).

## Save checkpoints to cloud storage[​](#cloud-checkpoints "Direct link to Save checkpoints to cloud storage")

warning

At this time, LLaMA-Factory doesn't support Azure for cloud-hosted datasets.

LLaMA-Factory supports writing checkpoints directly to cloud object storage when you run training on Ray. You configure this behavior in your training YAML by setting a storage path and filesystem, in addition to the run name.

* Amazon S3
* Google Cloud Storage

```
### Ray
ray_run_name: llama3_8b_sft_lora
ray_storage_path: my-checkpoints-bucket/llama-factory-runs
ray_storage_filesystem: s3
```

This configuration writes checkpoints for the run to a directory such as:

```
s3://my-checkpoints-bucket/llama-factory-runs/llama3_8b_sft_lora/
```

```
### Ray
ray_run_name: llama3_8b_sft_lora
ray_storage_path: my-checkpoints-bucket/llama-factory-runs
ray_storage_filesystem: gs  # Or use 'gcs'
```

This configuration writes checkpoints for the run to a directory such as:

```
gs://my-checkpoints-bucket/llama-factory-runs/llama3_8b_sft_lora/
```

If you omit `ray_storage_filesystem`, LLaMA-Factory keeps using the local filesystem at `ray_storage_path` (for example, `/mnt/cluster_storage/`).

### Configure cloud credentials[​](#cloud-credentials "Direct link to Configure cloud credentials")

You must ensure that both the Ray head node and all worker nodes can access the target bucket. This typically means:

* The nodes run in a project or account with permissions for the bucket.
* The environment on each node has valid cloud credentials and a region or location that matches your storage configuration.

For example, if you use Amazon S3 on instances that aren't already configured with an IAM role, you can export AWS credentials on the head node:

```
export AWS_REGION=...
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...  # If you use temporary credentials.
```

Then, in your post-training config YAML, propagate these environment variables to Ray workers through `ray_init_kwargs` so that all training processes see the same credentials:

```
### Ray
ray_init_kwargs:
  runtime_env:
    env_vars:
      AWS_REGION: ${AWS_REGION}
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      AWS_SESSION_TOKEN: ${AWS_SESSION_TOKEN}
```

With this setup, Ray workers can upload checkpoints to the S3 path you configured.

## Finalize the post-trained or fine-tuned model[​](#finalize-model "Direct link to Finalize the post-trained or fine-tuned model")

### Merge LoRA adapters[​](#merge-lora "Direct link to Merge LoRA adapters")

After fine-tuning or post-training with LoRA, a standalone model provides more efficient inference than loading a base model and an adapter separately.

**Merge the adapters** when you want a single-purpose deployment with the highest throughput. **Keep the adapters and model separate** if you have multi-tenant endpoints, A/B tests, or any scenario where you need to swap LoRA specializations on the fly. See [Deploy multi-LoRA adapters on LLMs](/llm/serving/multi-lora.md).

Use the LLaMA-Factory CLI to merge a trained LoRA adapter into the base model weights.

Create a YAML file (for example, `merge_config.yaml`) to define the paths for the merge.

```
# merge_config.yaml

### model
model_name_or_path: Qwen/Qwen2.5-7B-Instruct
adapter_name_or_path: /mnt/cluster_storage/qwen2_7b_sft_lora/TorchTrainer_x/checkpoint_x/checkpoint # Path to the previously trained checkpoints directory.
template: qwen
finetuning_type: lora

### export
export_dir: /mnt/cluster_storage/models/qwen_lora_sft # Where to save the merged model.
export_size: 2                  # GiB per shard.
export_device: cpu
export_legacy_format: false
```

* `model_name_or_path` must exist and match the chosen `template`.
* When merging a LoRA adapter, don't use a quantized base model. Merge with the original, unquantized model.
* Ensure your `export_device` has enough memory to fit 2 copies of the pretrained model.

Run this command:

```
llamafactory-cli export merge_config.yaml
```

### Post-training quantization (PTQ)[​](#ptq "Direct link to Post-training quantization (PTQ)")

Apply an additional post-training quantization step to your merged model. This makes the final model significantly smaller and can lead to faster inference speeds, which is ideal for production deployment.

FP8 quantization is a recommended option for reducing model size while keeping quality loss minimal.

note

The specific type of FP8 quantization you can use depends on your GPU architecture:

* Full FP8 (W8A8) is supported on newer NVIDIA Ada-generation GPUs, such as the L4.
* W8A16 (8-bit weights, 16-bit activation) is used for Ampere-generation GPUs, such as the A10G.

Use this script to quantize your model from 16-bit to 8-bit using `llmcompressor` in an Anyscale workspace:

```
import ray

@ray.remote(num_gpus=1, accelerator_type="L4", memory=16*1024**3)
def quantize():
    from transformers import AutoTokenizer, AutoModelForCausalLM
    from llmcompressor.transformers import oneshot
    from llmcompressor.modifiers.quantization import QuantizationModifier

    MODEL_ID = "Qwen/Qwen2.5-14B-Instruct"
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID, device_map="auto", torch_dtype="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    # Configure simple PTQ quantization.
    recipe = QuantizationModifier(
        targets="Linear", scheme="FP8_DYNAMIC", ignore=["lm_head"]
    )

    # Apply the quantization algorithm.
    oneshot(model=model, recipe=recipe)

    # Save the model: {MODEL_ID}-FP8-Dynamic under shared storage.
    SAVE_DIR = "/mnt/cluster_storage/" + MODEL_ID.split("/")[-1] + "-FP8-Dynamic"
    model.save_pretrained(SAVE_DIR)
    tokenizer.save_pretrained(SAVE_DIR)

ray.get(quantize.remote())
```

When you enable **Auto-select worker nodes**, the `@ray.remote()` decorator provisions and runs the `quantize` function on a dedicated worker node that matches your specified hardware requirements.

* **GPU requirement**: The script requests a single GPU per worker (`num_gpus=1`). Distributed quantization across multiple GPUs isn't supported.
* **Memory requirement**: The entire model must fit into a combination of GPU memory and host (CPU) memory. When GPU VRAM is insufficient, the framework offloads tensors to CPU RAM. Request a node with sufficient total memory (`memory=16*1024**3` ensures at least 16 GB of CPU RAM). As a rule of thumb, allocate at least 2× the model's parameter size in GB. For example, a 14B parameter model (about 14 GB) requires at least 28 GB of memory.

For a detailed, step-by-step guide on how to create an FP8-quantized model, follow the official documentation:

* [FP8 Quantization Guide](https://docs.vllm.ai/en/stable/features/quantization/fp8.html)
* [Quantization Hardware Compatibility Matrix](https://docs.vllm.ai/en/stable/features/quantization/#supported-hardware)
