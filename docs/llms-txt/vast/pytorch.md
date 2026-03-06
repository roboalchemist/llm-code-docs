# Source: https://docs.vast.ai/pytorch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PyTorch

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Running PyTorch on Vast.ai: A Complete Guide",
  "description": "Step-by-step guide to setting up and running PyTorch workloads on Vast.ai GPU cloud computing platform",
  "image": "https://docs.vast.ai/images/pytorch-logo.webp",
  "totalTime": "PT30M",
  "supply": [
    {
      "@type": "HowToSupply",
      "name": "Vast.ai Account"
    },
    {
      "@type": "HowToSupply",
      "name": "GPU Instance"
    },
    {
      "@type": "HowToSupply",
      "name": "PyTorch Framework"
    }
  ],
  "tool": [
    {
      "@type": "HowToTool",
      "name": "SSH Client"
    },
    {
      "@type": "HowToTool",
      "name": "Jupyter Notebook"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Set up Prerequisites",
      "text": "Create a Vast.ai account and install necessary tools like SSH client",
      "url": "https://docs.vast.ai/pytorch#prerequisites"
    },
    {
      "@type": "HowToStep",
      "name": "Launch GPU Instance",
      "text": "Create a GPU instance with PyTorch template on Vast.ai",
      "url": "https://docs.vast.ai/pytorch#launch-instance"
    },
    {
      "@type": "HowToStep",
      "name": "Configure Environment",
      "text": "Set up PyTorch environment and install dependencies",
      "url": "https://docs.vast.ai/pytorch#configure"
    }
  ],
  "author": {
    "@type": "Organization",
    "name": "Vast.ai Team"
  },
  "datePublished": "2025-01-13",
  "dateModified": "2025-05-12"
})
}}
/>

# Running PyTorch on Vast.ai: A Complete Guide

## Introduction

This guide walks you through setting up and running PyTorch workloads on Vast.ai, a marketplace for renting GPU compute power. Whether you're training large models or running inference, this guide will help you get started efficiently.

## Prerequisites

* A Vast.ai account
* Basic familiarity with PyTorch
* [Install TLS Certificate for Jupyter](/documentation/instances/jupyter)
* [(Optional) SSH client installed on your local machine and SSH public key added in Account tab at cloud.vast.ai](/documentation/instances/sshscp)
* [(Optional) Install and use vast-cli](/cli/get-started)
* [(Optional) Docker knowledge for custom environments](https://docs.docker.com/get-started/)

## Setting Up Your Environment

### 1. Selecting PyTorch Template

Navigate to the [Templates tab](https://cloud.vast.ai/templates/) to view available templates. Before choosing a specific instance, you'll need to select the appropriate PyTorch template for your needs:

* **Choose recommended** [**PyTorch**](https://cloud.vast.ai?ref_id=62897\&template_id=a33b72bd045341cfcd678ce7c932a614) **template:**
  * A container is built on the Vast.ai base image, inheriting its core functionality
  * It provides a flexible development environment with pre-configured libraries
  * PyTorch is pre-installed at `/venv/main/` for immediate use
  * Supports for both **AMD64** and **ARM64**(Grace) architectures, especially on CUDA 12.4+
  * You can select specific PyTorch versions via the Version Tag selector

<Frame caption="PyTorch">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=526bc758ee1c18649a5892b706149678" alt="PyTorch" data-og-width="800" width="800" data-og-height="607" height="607" data-path="images/use-cases-ai-ml-pytorch.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=06c9ab6a75fd74b5ac4cd3a93e186bed 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=5ca551d6e5805f20c5453b90afcf4790 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=bdd2054149f7a7eb96de51fe119a66a0 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=a81dce8541135bb78511f0618da55ff0 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=e0b91d1f5281bd4fab1366de683a5905 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c0a246ad87d85addc78d1b67964966a1 2500w" />
</Frame>

### 2. Choosing an Instance

Click the play button to select the template and see GPUs you can rent. For PyTorch workloads, consider:

* GPU Memory: Minimum 8GB for most models
* CUDA Version: PyTorch 2.0+ works best with CUDA 11.7 or newer
* Disk Space: Minimum 50GB for datasets and checkpoints
* Internet Speed: Look for instances with >100 Mbps for dataset downloads

Rent the GPU of your choice.

### 3. Connecting to Your Instance

Click blue button on instance card in Instances tab when it says "Open" to access Jupyter.

## Setting Up Your PyTorch Environment

### 1. Basic Environment Check

Open Python's Interactive Shell in the jupyter terminal

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-2.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=8bedff75376a9102d9cff148bcc38ccf" alt="" data-og-width="1264" width="1264" data-og-height="502" height="502" data-path="images/use-cases-ai-ml-pytorch-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-2.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=0d75bf7960e6110aa60c642db1aa118a 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-2.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=7c526fade72dadcbaf617817e80f1e8b 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-2.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=0a869fc781c09bfc2b90fe54596b2a5f 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-2.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=bcde22844d119a35ad0a77776edfc77e 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-2.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=6f506ce40f67d8ccf363f6346cea6836 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-2.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=1ba26feb72fa09cc4ad90f1964801509 2500w" />

<img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-3.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=9269f46f24f54e7f9a4013cb96323e98" alt="" data-og-width="800" width="800" data-og-height="104" height="104" data-path="images/use-cases-ai-ml-pytorch-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-3.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=453e09a6d491ae4d62f37ddcca967683 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-3.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=d4a759cebd74d5e099202c2b451275de 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-3.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c2b42c4ce87a0986e7a3ff232fc18da9 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-3.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c3b413ce5cc06314166081a7885eb578 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-3.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=5496ff8769b30cbae5abd6413c7f70aa 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/use-cases-ai-ml-pytorch-3.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=dc9edbbac948582c13e4201702625404 2500w" />

Verify your setup by executing these commands in Python's Interactive Shell in a Jupyter terminal:

```python icon="python" Python icon="python" Python theme={null}
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU device: {torch.cuda.get_device_name(0)}")
```

### 2. Data Management

For efficient data handling:

a) Fast local storage:

```bash  theme={null}
mkdir /workspace/data
cd /workspace/data
```

b) Dataset downloads:

```bash  theme={null}
# Using wget
wget your_dataset_url

# Using git lfs for larger files: https://git-lfs.com/
sudo apt-get install git-lfs
git lfs install
git clone your_dataset_repo
```

## Training Best Practices

### Checkpoint Management

Always save checkpoints to prevent data loss:

```python icon="python" Python theme={null}
checkpoint_dir = '/workspace/checkpoints'
os.makedirs(checkpoint_dir, exist_ok=True)

checkpoint = {
    'epoch': epoch,
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}
torch.save(checkpoint, f'{checkpoint_dir}/checkpoint_{epoch}.pt')
```

### Resource Monitoring

Monitor GPU usage:

```bash  theme={null}
watch -n 1 nvidia-smi
```

Or in Python:

```python icon="python" Python theme={null}
def print_gpu_utilization():
    print(torch.cuda.memory_allocated() / 1024**2, "MB Allocated")
    print(torch.cuda.memory_reserved() / 1024**2, "MB Reserved")
```

## Cost Optimization

### Instance Selection

* Use [vast cli search offers command ](https://vast.ai/docs/cli/commands#search-offers)to search for machines that fit your budget
* Monitor your spending in Vast.ai's Billing tab

### Resource Utilization

* Use appropriate batch sizes to maximize GPU utilization
* Enable gradient checkpointing for large models
* Implement early stopping to avoid unnecessary compute time

## Troubleshooting

### Common Issues and Solutions

* Out of Memory (OOM) Errors
  * Reduce batch size
  * Enable gradient checkpointing
  * Use mixed precision training

```python icon="python" Python theme={null}
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
with autocast():
    outputs = model(inputs)
    loss = criterion(outputs, labels)
scaler.scale(loss).backward()
```

* Slow Training
  * Check GPU utilization
  * Verify data loading pipeline
  * Consider using `torch.compile()` for PyTorch 2.0+

```python icon="python" Python theme={null}
model = torch.compile(model)
```

* Connection Issues
  * Use `tmux` or `screen` for persistent sessions
  * Set up automatic reconnection in your SSH config

## Best Practices

### Environment Management

* Document your setup and requirements
* Keep track of software versions

### Data Management

* Use data versioning tools
* Implement proper data validation
* Set up efficient data loading pipelines

### Training Management

* Implement logging (e.g., WandB, TensorBoard)
* Set up experiment tracking
* Use configuration files for hyperparameters

## Advanced Topics

### Multi-GPU Training

For distributed training:

```python icon="python" Python theme={null}
model = torch.nn.DataParallel(model)
```

### Mixed Precision Training

Enable AMP for faster training:

```python icon="python" Python theme={null}
from torch.cuda.amp import autocast

with autocast():
    outputs = model(inputs)
```

### Custom Docker Images

Create a custom Docker image from your own Dockerfile and [create your own template](https://vast.ai/docs/use-cases/create-your-own-template) as needed:

```dockerfile  theme={null}
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Install additional dependencies
RUN pip install wandb tensorboard

# Add your custom requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
```

## Conclusion

Running PyTorch on Vast.ai provides a cost-effective way to rent cheap GPUs and accelerate deep learning workloads. By following this guide and best practices, you can efficiently set up and manage your PyTorch workloads while optimizing costs and performance.

## Additional Resources

* [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
* [Vast.ai Documentation](/documentation/get-started/index)
* [PyTorch Performance Tuning Guide](https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html)
