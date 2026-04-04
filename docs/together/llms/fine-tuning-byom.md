# Source: https://docs.together.ai/docs/fine-tuning-byom.md

> Bring Your Own Model: Fine-tune Custom Models from the Hugging Face Hub

# Fine-tuning BYOM

> Note: This feature extends our fine-tuning capabilities to support models from the Hugging Face ecosystem, enabling you to leverage community innovations and your own custom checkpoints.

## Overview

The Together Fine-Tuning Platform now supports training custom models beyond our official model catalog. If you've found a promising model on Hugging Face Hub, whether it's a community model, a specialized variant, or your own previous experiment, you can now fine-tune it using our service.

**Why Use This Feature?**

* **Leverage specialized models**: Use domain-specific or task-optimized models as your starting point
* **Continue previous work**: Resume training from your own checkpoints or experiments
* **Access community innovations**: Fine-tune cutting-edge models not yet in our official catalog

**Key Concept: Base Model + Custom Model**

Understanding BYOM requires grasping our **dual-model approach**:

* **Base Model** (`model` parameter): A model from Together's official catalog that provides the infrastructure configuration, training settings, and inference setup
* **Custom Model** (`from_hf_model` parameter): Your actual HuggingFace model that gets fine-tuned

**Think of it this way**: The base model acts as a "template" that tells our system how to optimally train and serve your custom model. Your custom model should have a similar architecture, size, and sequence length to the base model for best results.

**Example**:

```python  theme={null}
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model (training template)
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Your custom model
    training_file="file-id-from-upload",
)
```

In this example, we use Llama-2-7B as the base model template because SmolLM2 has Llama architecture and similar characteristics.

**How It Works**

Simply provide a Hugging Face repository URL, and our API will:

1. Load your model checkpoint
2. Apply your fine-tuning data
3. Make the trained model available through our inference endpoints

### Prerequisites

Before you begin, ensure your model meets these requirements:

**Model Architecture**

* **Supported type**: CausalLM models only (models designed for text generation tasks)
* **Size limit**: A maximum of 100 billion parameters
* **Framework version**: Compatible with Transformers library v4.55 or earlier

**Technical Requirements**

* Model weights must be in the `.safetensors` format for security and efficiency
* The model configuration must not require custom code execution (no `trust_remote_code`)
* The repository must be publicly accessible, or you must provide an API token that has access to the private repository

**What You'll Need**

* The Hugging Face repository URL containing your model
* (Optional) The Hugging Face API token for accessing private repositories
* Your training data prepared according to [one of our standard formats](./fine-tuning-data-preparation.mdx)
* Your training hyperparameters for the fine-tuning job

### Compatibility Check

Before starting your fine-tuning job, validate that your model meets our requirements:

1. **Architecture Check**: Visit your model's HuggingFace page and verify it's a "text-generation" or "causal-lm" model
2. **Size Check**: Look for parameter count in model card (should be ≤100B)
3. **Format Check**: Verify model files include `.safetensors` format
4. **Code Check**: Ensure the model doesn't require `trust_remote_code=True`

## Quick Start

Fine-tune a custom model from Hugging Face in three simple steps:

```python  theme={null}
from together import Together

client = Together(api_key="your-api-key")

# Start fine-tuning with your custom model
job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model family for configuration
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Your custom model from HF
    training_file="file-id-from-upload",
    # Optional: for private repositories
    hf_api_token="hf_xxxxxxxxxxxx",
)

# Monitor progress
print(f"Job ID: {job.id}")
print(f"Status: {job.status}")
```

The custom model should be as close (have similar architecture, similar model sizes and max sequence length) to the base model family as possible. In the example above, `HuggingFaceTB/SmolLM2-1.7B-Instruct` has Llama architecture, and the closest model size and max sequence length.

### Parameter Explanation

| Parameter           | Purpose                                                                              | Example                                                      |
| ------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| `model`             | Specifies the base model family for optimal configuration and inference setup        | `"togethercomputer/llama-2-7b-chat"`, `"meta-llama/Llama-3"` |
| `from_hf_model`     | The Hugging Face repository containing your custom model weights                     | `"username/model-name"`                                      |
| `hf_model_revision` | (Optional) Use only if you need a specific commit hash instead of the latest version | `"abc123def456"`                                             |
| `hf_api_token`      | (Optional) API token for accessing private repositories                              | `"hf_xxxxxxxxxxxx"`                                          |

## Detailed Implementation Guide

**Step 1: Prepare Your Training Data**

Ensure your training data is formatted correctly and uploaded to the Together platform. Refer to [our data preparation guide](./fine-tuning-data-preparation.mdx) for detailed instructions on supported formats.

**Step 2: Start Fine-Tuning**

Launch your fine-tuning job with your custom model:

```python  theme={null}
job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    training_file="your-file-id",
    # Recommended training parameters
    n_epochs=3,
    learning_rate=1e-5,
    batch_size=4,
    # Optional parameters
    suffix="custom-v1",  # Helps track different versions
    wandb_api_key="...",  # For training metrics monitoring
    # Add other training parameters for your training
)

# Only include if you need a specific commit:
# hf_model_revision="abc123def456"
```

**Step 3: Monitor and Use Your Model**

Once training completes successfully, your model will appear in the models dashboard and can be used for inference. You can create a dedicated endpoint or start using the model using LoRA Serverless endpoints. For more information, please go to the page [Deploying a Fine-tuned Model](./deploying-a-fine-tuned-model.mdx).

## Common Use Cases & Examples

### Architecture-Specific Examples

**Llama Family Models**

```python  theme={null}
# Example 1: Fine-tune SmolLM2 (Llama architecture)
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model template
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Custom model
    training_file="file-id",
    n_epochs=3,
    learning_rate=1e-5,
)

# Example 2: Fine-tune a Code Llama variant
client.fine_tuning.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    from_hf_model="codellama/CodeLlama-7b-Instruct-hf",
    training_file="code-dataset-id",
    batch_size=2,  # Reduce for code models
    n_epochs=2,
)
```

**Qwen Family Models**

```python  theme={null}
# Example 1: Fine-tune Qwen2.5 model
client.fine_tuning.create(
    model="Qwen/Qwen3-4B",  # Base template
    from_hf_model="Qwen/Qwen2.5-7B-Instruct",  # Custom Qwen model
    training_file="file-id",
    learning_rate=5e-6,  # Lower LR for larger models
    n_epochs=3,
)

# Example 2: Fine-tune specialized Qwen model
client.fine_tuning.create(
    model="Qwen/Qwen3-7B",
    from_hf_model="Qwen/Qwen2.5-Math-7B-Instruct",  # Math-specialized
    training_file="math-problems-dataset",
    suffix="math-tuned-v1",
)
```

**Mistral Family Models**

```python  theme={null}
# Example 1: Fine-tune Mistral 7B variant
client.fine_tuning.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",  # Base template
    from_hf_model="mistralai/Mistral-7B-Instruct-v0.3",  # Newer version
    training_file="file-id",
    n_epochs=3,
    batch_size=4,
)

# Example 2: Fine-tune Mixtral model
client.fine_tuning.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    from_hf_model="mistralai/Mixtral-8x22B-Instruct-v0.1",  # Larger variant
    training_file="large-dataset-id",
    batch_size=1,  # Very large model, small batch
    learning_rate=1e-6,
)
```

**Gemma Family Models**

```python  theme={null}
# Example 1: Fine-tune Gemma 2 model
client.fine_tuning.create(
    model="google/gemma-2-9b-it",  # Base template
    from_hf_model="google/gemma-2-2b-it",  # Smaller Gemma variant
    training_file="file-id",
    n_epochs=4,
    learning_rate=2e-5,
)

# Example 2: Fine-tune CodeGemma
client.fine_tuning.create(
    model="google/gemma-3-4b-it",
    from_hf_model="google/codegemma-7b-it",  # Code-specialized
    training_file="code-instruction-dataset",
    learning_rate=1e-5,
)
```

### End-to-End Workflow Examples

**Complete Domain Adaptation Workflow**

```python  theme={null}
from together import Together
import json

# Step 1: Initialize client and prepare data
client = Together(api_key="your-api-key")

# Step 2: Upload training data
with open("legal_qa_dataset.jsonl", "rb") as f:
    file_upload = client.files.upload(file=f, purpose="fine-tune")

# Step 3: Choose compatible model based on requirements
# For this example, we'll use a compatible Phi-3 model
target_model = "microsoft/phi-3-medium-4k-instruct"

# Step 4: Start fine-tuning
job = client.fine_tuning.create(
    model="microsoft/phi-3-medium-4k-instruct",  # Base model
    from_hf_model=target_model,  # Your custom model
    training_file=file_upload.id,
    suffix="legal-specialist-v1",
    n_epochs=3,
    learning_rate=1e-5,
    wandb_api_key="your-wandb-key",  # Optional: for monitoring
)

# Step 5: Monitor training
print(f"Job started: {job.id}")
while job.status in ["pending", "running"]:
    job = client.fine_tuning.retrieve(job.id)
    print(f"Status: {job.status}")
    time.sleep(30)

# Step 6: Deploy for inference (once completed)
if job.status == "succeeded":
    # Create dedicated endpoint
    endpoint = client.endpoints.create(
        model=job.fine_tuned_model, type="dedicated", hardware="A100-40GB"
    )
    print(f"Endpoint created: {endpoint.id}")
```

**Iterative Model Improvement Workflow**

```python  theme={null}
# Workflow: Start → Fine-tune → Evaluate → Improve → Repeat

# Iteration 1: Initial fine-tuning
initial_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="huggingface/CodeBERTa-small-v1",  # Starting model
    training_file="initial-dataset-id",
    suffix="v1",
    n_epochs=3,
)

# Wait for completion...

# Iteration 2: Improve with more data
improved_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="your-username/model-v1",  # Use previous result
    training_file="expanded-dataset-id",  # More/better data
    suffix="v2",
    n_epochs=2,  # Fewer epochs for fine-tuning
    learning_rate=5e-6,  # Lower learning rate
)

# Iteration 3: Specialized fine-tuning
specialized_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="your-username/model-v2",
    training_file="specialized-task-dataset",
    suffix="specialized-v3",
    n_epochs=1,
    learning_rate=1e-6,
)
```

### Continuing Training from a Previous Fine-tune

Resume training from a checkpoint you previously created to add more data or continue the adaptation process:

```python  theme={null}
client.fine_tuning.create(
    model="google/gemma-3-4b-it",
    from_hf_model="your-username/previous-finetune-v1",
    training_file="new-training-data",
    n_epochs=2,  # Additional training epochs
)
```

### Fine-tuning a Community Specialist Model

Leverage community models that have already been optimized for specific domains:

```python  theme={null}
# Example: Fine-tune a medical domain model with your proprietary data
client.fine_tuning.create(
    model="Qwen/Qwen3-4B",  # Base architecture it's built on
    from_hf_model="community/medical-Qwen3-4B",  # Specialized variant
    training_file="your-medical-data",
)
```

## Troubleshooting

**Understanding Training Stages**

Your fine-tuning job progresses through several stages. Understanding these helps you identify where issues might occur:

1. **Data Download**: The system downloads your model weights from Hugging Face and your training data from Together
2. **Initialization**: Model is loaded onto GPUs and the data pipeline is prepared for training
3. **Training**: The actual fine-tuning occurs based on your specified hyperparameters
4. **Saving**: The trained model is saved to temporary storage
5. **Upload**: The final model is moved to permanent storage for inference availability

**Common Errors and Solutions**

Due to the number of diverse model families hosted on the Hugging Face Hub, understanding these error types helps you quickly resolve issues:

* **Internal Errors**: Training failed due to an internal problem with the Fine-tuning API. Our team gets automatically notified and usually starts investigating the issue shortly after it occurs. If this persists for long periods of time, please contact support with your job ID.
* **CUDA OOM (Out of Memory) Errors**: Training failed because it exceeded available GPU memory. To resolve this, reduce the `batch_size` parameter or consider using a smaller model variant.
* **Value Errors and Assertions**: Training failed due to a checkpoint validation error. These typically occur when model hyperparameters are incompatible or when the model architecture doesn't match expectations. Check that your model is actually CausalLM and that all parameters are within valid ranges.
* **Runtime Errors**: Training failed due to computational exceptions raised by PyTorch. These often indicate issues with model weights or tensor operations. Verify that your model checkpoint is complete and uncorrupted.

## Frequently Asked Questions

**Question: How to choose the base model?**

There are three variables to consider:

* Model Architecture
* Model Size
* Maximum Sequence Length

You want to use the model with the same architecture, the closest number of parameters as possible to the base model and the max seq length for the base model should not exceed the maximum length for the external model.

For example, `HuggingFaceTB/SmolLM2-135M-Instruct`. It has Llama architecture, the model size is 135M parameters and the max sequence length is 8k. Looking into the Llama models, Fine-tuning API supports llama2, llama3, llama3.1 and llama3.2 families. The closest model by number of parameters is `meta-llama/Llama-3.2-1B-Instruct`, but the max seq length is 131k, which is much higher than the model can support. It's better to use `togethercomputer/llama-2-7b-chat`, which is larger than the provided model, but the max seq length is not exceeding the model's limits.

**Issue**: "No exact architecture match available"

* **Solution**: Choose the closest architecture family (e.g., treat CodeLlama as Llama)

**Issue**: "All base models are much larger than my custom model"

* **Solution**: Use the smallest available base model; the system will adjust automatically

**Issue**: "Unsure about sequence length limits"

* **Solution**: Check your model's `config.json` for `max_position_embeddings` or use our compatibility checker

***

**Question: Which models are supported?**

Any CausalLM model under 100B parameters that has a corresponding base model in [our official catalog](./fine-tuning-models.mdx). The base model determines the inference configuration. If your checkpoint significantly differs from the base model architecture, you'll receive warnings, but training will proceed.

***

**Question: Can I fine-tune an adapter/LoRA model?**

Yes, you can continue training from an existing adapter model. However, the Fine-tuning API will merge the adapter with the base model during training, resulting in a full checkpoint rather than a separate adapter.

***

**Question: Will my model work with inference?**

Your model will work with inference if:

* The base model you specified is officially supported
* The architecture matches the base model configuration
* Training completed successfully without errors

Models based on unsupported architectures may not function correctly during inference. If you want to run a trained model with unsupported architecture, please submit a support ticket on [the support page](https://support.together.ai/).

***

**Question: Can I load a custom model for dedicated endpoint and train it?**

No, you cannot use uploaded models for training in Fine-tuning API. Models uploaded for inference will not appear in the fine-tunable models. To learn more about what you can do with the uploaded models for dedicated endpoint, see this [page](./custom-models.mdx).

However, you can upload your model to the Hugging Face Hub and use the repo id to train it. The trained model will be available for the inference after the training.

***

**Question: How do I handle private repositories?**

Include your Hugging Face API token with read permissions for those repositories when creating the fine-tuning job:

```python  theme={null}
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="private-org/private-model",
    hf_api_token="hf_xxxxxxxxxxxx",
    training_file="your-file-id",
)
```

***

**Question: What if my model requires custom code?**

Models requiring `trust_remote_code=True` are not currently supported for security reasons. Consider these alternatives:

* Use a similar model that doesn't require custom code
* Contact our support team and request adding the model to our official catalog
* Wait for the architecture to be supported officially

***

**Question: How do I specify a particular model version?**

If you need to use a specific commit hash instead of the latest version, use the `hf_model_revision` parameter:

```python  theme={null}
# Use a specific commit hash
client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    hf_model_revision="abc123def456",  # Specific commit hash
    training_file="your-file-id",
)
```

## Support

Need help with your custom model fine-tuning?

* **Documentation**: Check our [error guide](/docs/error-codes)
* **Community**: Join our [Discord Community](https://discord.gg/9Rk6sSeWEG) for peer support and tips
* **Direct Support**: Contact our support team with your job ID for investigation of specific issues

When reporting issues, please include:

* Your fine-tuning job ID
* The Hugging Face model repository you're using
* Any error messages you're encountering


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt