# Source: https://docs.anyscale.com/resources/troubleshooting.md

# Source: https://docs.anyscale.com/llm/serving/troubleshooting.md

# Troubleshoot LLM serving

[View Markdown](/llm/serving/troubleshooting.md)

# Troubleshoot LLM serving

This guide helps you diagnose and resolve common issues when deploying large language models with Ray Serve on Anyscale. Each section provides quick fixes and explains the underlying causes to help you troubleshoot efficiently.

## Hugging Face authentication errors[​](#hf-auth "Direct link to Hugging Face authentication errors")

Some models, such as the LLaMA family, are gated on Hugging Face. To use them, navigate to the model's card and follow the prompt to request access. Approval timelines can take anywhere from a few hours to several weeks.

Once access is granted, share your Hugging Face token to your Ray cluster. You can share it in your runtime environment with `HF_TOKEN` or to your vLLM engine with `hf-token`.

```
applications:
- ...
  args:
    llm_configs:
      ...
      runtime_env:
        env_vars:
            # Share your Hugging Face token to the vLLM engine.
            HF_TOKEN: <YOUR-HUGGINGFACE-TOKEN>
```

## Model loading issues and optimizations[​](#model-loading "Direct link to Model loading issues and optimizations")

For troubleshooting slow downloads, loading errors, and other related issues, see [Model loading: Troubleshooting](https://docs.ray.io/en/latest/serve/llm/user-guides/model-loading.html#troubleshooting). For strategies to reduce replica startup times, see [Deployment initialization](https://docs.ray.io/en/latest/serve/llm/user-guides/deployment-initialization.html) and [Replica startup latency benchmarks](https://docs.ray.io/en/latest/serve/llm/benchmarks.html#replica-startup-latency).

## Multi-node deployment hangs[​](#multi-node-hang "Direct link to Multi-node deployment hangs")

When deploying multiple LLMs across multiple nodes, all `LLMServer` replicas might show as ready while `OpenAIIngress` remains stuck in an `UPDATING` state. This happens because `OpenAIIngress` queries against each `LLMServer` before marking itself ready. If node-to-node network communication isn't configured properly, these queries can fail silently.

To diagnose, SSH into the node running `OpenAIIngress` and test connectivity to the other nodes using `ping` or `curl`. If these fail, review your cloud network configuration—check security groups, firewall rules, and VPC settings to ensure nodes within the cluster can communicate with each other.

## GPU out of memory (OOM) errors[​](#gpu-oom "Direct link to GPU out of memory (OOM) errors")

OOM errors are common when deploying large models. Symptoms include `CUDA out of memory` messages, allocation failures, or Ray Serve replicas getting stuck in `STARTING` or `UNHEALTHY` states. Consider upgrading to GPUs with higher memory capacity or better adapted for your system. See [Choose a GPU for LLM serving](/llm/serving/gpu-guidance.md) and [Tune parameters for LLMs on Anyscale services](/llm/serving/parameter-tuning.md) for more details.

Several strategies can help resolve OOM errors, though they often involve trade-offs in latency or cost:

### GPU selection and vRAM adjustment[​](#gpu-selection "Direct link to GPU selection and vRAM adjustment")

* Select a GPU with more memory, but also consider other GPU factors such as memory bandwidth and intercommunication methods.
* Adjust GPU memory utilization: By default, vLLM reserves 90% of VRAM. You can increase this by setting `gpu_memory_utilization` (for example, to `0.95`).

warning

Higher values reduce headroom for other GPU operations and can cause system-level OOM errors. Avoid exceeding `0.95`.

### System reserved GPU memory[​](#system-reserved-memory "Direct link to System reserved GPU memory")

vLLM can't detect memory that the system reserves for features such as ECC (error-correcting code), driver/firmware overhead, display output, and MIG/vGPU configurations. This can cause vLLM to attempt to allocate more memory than is available, resulting in OOM errors.

To determine how much GPU memory the system reserves, run the following command:

```
nvidia-smi -i 0 -q -d MEMORY
```

By default, vLLM reserves 90% of available GPU memory. If system-level reserved memory exceeds 10%, reduce `gpu_memory_utilization` accordingly. Anyscale recommends leaving at least 10% headroom to accommodate dynamic memory allocation, such as CUDA kernel overhead during inference.

For example, if using ECC takes 12% of total GPU memory, set `gpu_memory_utilization` to `0.78` (100% - 12% ECC - 10% headroom = 78%):

```
applications:
- ...
  args:
    llm_configs:
      ...
      engine_kwargs:
        gpu_memory_utilization: 0.78
```

If your model still doesn't fit after adjusting `gpu_memory_utilization`, consider alternative strategies such as [Model parallelism](#model-parallelism).

### Model parallelism[​](#model-parallelism "Direct link to Model parallelism")

Distribute a large model across multiple GPUs when it doesn't fit on a single device.

* **Tensor parallelism**: Splits model layers across multiple GPUs on the same node. Set `tensor_parallel_size` to the number of GPUs per replica.
* **Pipeline parallelism**: Splits the entire model across GPUs on different nodes. Set `pipeline_parallel_size` to the number of nodes per replica.

### Reduce model memory footprint[​](#reduce-memory "Direct link to Reduce model memory footprint")

Decrease the model's size before vLLM loads it onto the GPU.

* **Apply quantization**: Reduce model weight precision (for example, from FP16 to FP8 or AWQ) to significantly cut memory usage. Set `quantization` in your vLLM engine.
* **Use a smaller model**: Consider smaller model variants (for example, 7B instead of 70B) if performance is acceptable.
* **Fine-tune LLMs with knowledge distillation**: Train a smaller or more efficient model to mimic a larger model's behavior, reducing memory requirements while retaining much of the original performance.

### Reduce vLLM pre-allocated memory[​](#reduce-vllm-memory "Direct link to Reduce vLLM pre-allocated memory")

The KV cache stores attention keys and values for generated tokens and is a primary consumer of GPU memory.

* **Reduce `max_model_len`**: Reduce memory usage by limiting the model's context length.
* **Set `enforce_eager: true`**: Setting this in `engine_kwargs` turns CUDA Graphs off. You regain some GPU memory, but you typically get higher per-token latency and lower throughput, especially at small batch sizes. You can also adjust `compilation_config` to achieve a better balance between inference speed and memory usage.

### Configure multi-modal models[​](#multimodal-config "Direct link to Configure multi-modal models")

For multi-modal models, inputs such as images and videos consume significant memory. Control this behavior with the following:

* **`limit_mm_per_prompt`**: Set limits per modality (for example, `{images: 2, videos: 0}`) to cap memory allocation. Setting a modality to `0` disables it.
* **`disable_mm_preprocessor_cache`**: Set to `True` to avoid caching preprocessed multi-modal inputs if they aren't frequently reused.

## GPU compatibility errors[​](#gpu-compatibility "Direct link to GPU compatibility errors")

Some GPUs might not support all features required by modern LLMs, which can result in errors during model loading or inference. For example, T4 GPUs don't support `bfloat16` data types, which many models use by default, or the `mxfp4` quantization method used by `gpt-oss` models.

If you encounter compatibility errors, try the following:

* **Switch to a different GPU**: Use GPUs that support the required features, such as A10G, L4, or A100 for `bfloat16` data types.
* **Use supported data types**: If you must use a GPU with limited feature support, configure your model accordingly. For example, use `float16` instead of `bfloat16` by setting `dtype` in your vLLM engine configuration.

For guidance on GPU selection and capabilities, see [Choose a GPU for LLM serving](/llm/serving/gpu-guidance.md).

## Disk out of space errors[​](#disk-space "Direct link to Disk out of space errors")

If you need more storage capacity for model weights, logs, or datasets, you can increase the default disk size of your instance. See [Change the default disk size](/configuration/compute/gcp.md#disk-size) for Google Cloud or [Change the default disk size](/configuration/compute/aws.md#disk-size) for AWS.

For example, you can set the default disk size of your worker nodes in the Anyscale service config file:

```
# service.yaml
...
compute_config:
  ...
  # Change default disk size to 1000GB.
  advanced_instance_config:
    ## AWS example ##
    BlockDeviceMappings:
      - Ebs:
          VolumeSize: 1000
          VolumeType: gp3
          DeleteOnTermination: true
        DeviceName: "/dev/sda1"
    #########
    ## GCP example ##
    #instanceProperties:
    #  disks:
    #    - boot: true
    #      auto_delete: true
    #      initialize_params:
    #        disk_size_gb: 1000
    #########
```
