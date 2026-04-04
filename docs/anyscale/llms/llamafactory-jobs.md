# Source: https://docs.anyscale.com/llm/fine-tuning/llamafactory-jobs.md

# Run LLaMA-Factory fine-tuning as an Anyscale job

[View Markdown](/llm/fine-tuning/llamafactory-jobs.md)

# Run LLaMA-Factory fine-tuning as an Anyscale job

Run LLaMA-Factory fine-tuning workloads as Anyscale jobs for greater stability and automatic retry behavior.

Anyscale jobs run independently of your interactive workspace session. This provides greater stability, automatic retry behavior, and centralized logging, which is ideal for long-running or critical fine-tuning tasks. You can submit an Anyscale job from either your local machine using the Anyscale CLI or directly from a workspace.

## Step 1: Build a custom container image[​](#build-image "Direct link to Step 1: Build a custom container image")

To run LLaMA-Factory as an Anyscale job, first [Build a custom image in the console](/container-image/build-image.md#build-farm) with LLaMA-Factory pre-installed. See [Custom images on Anyscale](/container-image/custom-image.md) for more details on using container images on Anyscale.

Specify the required packages in a `Dockerfile`. For example, if you're following the [Supervised Fine-Tuning (SFT) at Scale with DeepSpeed template](https://console.anyscale.com/template-preview/llm_finetuning), create a `Dockerfile` using the `anyscale/ray-llm:2.48.0-py311-cu128` base image:

```
# Dockerfile

# Start with a recommended Anyscale base image
FROM anyscale/ray-llm:2.48.0-py311-cu128

WORKDIR /app

# Add your pip dependencies
RUN pip install --no-cache-dir --upgrade \
    llamafactory@git+https://github.com/hiyouga/LLaMA-Factory.git@v0.9.3 \
    deepspeed==0.16.9 \
    wandb==0.21.3 \
    hf_transfer==0.1.9
```

## Step 2: Prepare the LLaMA-Factory training configuration[​](#training-config "Direct link to Step 2: Prepare the LLaMA-Factory training configuration")

Prepare the training YAML file.

### Use shared storage for jobs[​](#shared-storage "Direct link to Use shared storage for jobs")

The LLaMA-Factory training configuration (for example, `qwen2.5_deepspeed_lora_sft.yaml`) and every file path it references must reside on storage that's **shared across all worker nodes**.

For example, in the YAML configuration below, the paths for `deepspeed`, `dataset_dir`, and `ray_storage_path` must all resolve to a shared location such as `/mnt/shared_storage` or `/mnt/user_storage`.

caution

Don't use `/mnt/cluster_storage` even if you launch the job from an Anyscale workspace. A workspace runs on its **own cluster**, and a job typically runs on a separate **execution cluster**. See [Shared storage on Anyscale](/storage/shared.md) for more details.

```
# qwen2.5_deepspeed_lora_sft.yaml

### Deepspeed config
deepspeed: /mnt/user_storage/ds_z3_config.json

### Dataset config
# Local dataset on shared storage
dataset: my_glaive_toolcall_en_demo
dataset_dir: /mnt/shared_storage/<user>

### Ray config
ray_run_name: qwen2.5_deepspeed_lora_sft
ray_storage_path: /mnt/user_storage

ray_init_kwargs:
  runtime_env:
    env_vars:
        # Only add environment variables here if they aren't defined in the Anyscale job configuration.
        # Don't define the same variable in both places.

        # Example for Weights & Biases tracking
        # WANDB_API_KEY: <your_wandb_token>

        # Example for gated models like meta-llama/Llama-3.1-8B-Instruct
        # HF_TOKEN: <your_huggingface_token>

        # Enable faster downloads with hf_transfer
        HF_HUB_ENABLE_HF_TRANSFER: '1'
```

## Step 3: Create the Anyscale job configuration[​](#job-config "Direct link to Step 3: Create the Anyscale job configuration")

Create a job configuration file (for example, `qwen-job.yaml`) to define the job parameters. This is the only file that doesn't need to reside on shared storage. However, every path it references, including the `entrypoint`, must be on shared storage.

```
# qwen-job.yaml

name: qwen2.5_deepspeed_lora_sft_job
image_uri: <your_image_uri>:<version> # Your custom image from Step 1
cloud: <your-cloud-name>
ray_version: 2.48.0
max_retries: 1

env_vars:
    # Set this to enable Ray Train in LLaMA-Factory
    USE_RAY: '1'
    # Add environment variables here (e.g., API keys)
    # WANDB_API_KEY: <your_wandb_token>
    # HF_TOKEN: <your_huggingface_token>

entrypoint: llamafactory-cli train /mnt/user_storage/qwen2.5_deepspeed_lora_sft.yaml
```

## Step 4: Submit and monitor the job[​](#submit-monitor "Direct link to Step 4: Submit and monitor the job")

You can submit the job from either an Anyscale workspace or your local machine's terminal.

note

When launching jobs from a workspace, use a clean environment. Job services inherit the workspace's pip packages and environment variables. Avoid extra installs to prevent version conflicts and verify that you set only the intended environment variables (API keys, tracking tokens, etc.) before submitting.

Submit your job using the Anyscale CLI:

```
anyscale job submit --wait --config-file qwen-job.yaml
```

Monitor your job's logs, status, and hardware metrics on the Anyscale jobs page. Once finished, the job's status changes to **Succeeded**.

### Terminate a job early[​](#terminate-job "Direct link to Terminate a job early")

If you need to stop a running job before it completes, use the following commands:

```
# First, list all jobs to find the ID of the one you want to stop
anyscale job list

# Then, terminate the job using its ID
anyscale job terminate --id <prodjob_...>
```
