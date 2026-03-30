# Source: https://docs.together.ai/docs/nanochat-on-instant-clusters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to run nanochat on Instant Clusters⚡️

> Learn how to train Andrej Karpathy's end-to-end ChatGPT clone on Together's on-demand GPU clusters

## Overview

[nanochat](https://github.com/karpathy/nanochat) is Andrej Karpathy's end-to-end ChatGPT clone that demonstrates how a full conversational AI stack, from tokenizer to web UI—can, be trained and deployed for \$100 on 8×H100 hardware. In this guide, you'll learn how to train and deploy nanochat using Together's [Instant Clusters](https://api.together.ai/clusters).

The entire process takes approximately 4 hours on an 8×H100 cluster and includes:

* Training a BPE tokenizer on [FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)
* Pretraining a base transformer model
* Midtraining on curated tasks
* Supervised fine-tuning for conversational alignment
* Deploying a FastAPI web server with a chat interface

## Prerequisites

Before you begin, make sure you have:

* A Together AI account with access to [Instant Clusters](https://api.together.ai/clusters)
* Basic familiarity with SSH and command line operations
* `kubectl` installed on your local machine ([installation guide](https://kubernetes.io/docs/tasks/tools/))

# Training nanochat

## Step 1: Create an Instant Cluster

First, let's create an 8×H100 cluster to train nanochat.

1. Log into [api.together.ai](https://api.together.ai)
2. Click **GPU Clusters** in the top navigation menu
3. Click **Create Cluster**
4. Select **On-demand** capacity
5. Choose **8xH100** as your cluster size
6. Enter a cluster name (e.g., `nanochat-training`)
7. Select **Slurm on Kubernetes** as the cluster type
8. Choose your preferred region
9. Create a shared volume, min 1 TB storage
10. Click **Preview CLuster** and then "Confirm & Create"
    <Frame><img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=bb1efef1417b404fd8b8aaa50e74eb4c" alt="" width="3136" height="2598" data-path="images/guides/nanochat/1.png" /></Frame>

Your cluster will be ready in a few minutes. Once the status shows **Ready**, you can proceed to the next step.

<Info>
  For detailed information about Instant Clusters features and options, see the [Instant Clusters documentation](/docs/instant-clusters).
</Info>

## Step 2: SSH into Your Cluster

From the Instant Clusters UI, you'll find SSH access details for your cluster.

A command like the one below can be copied from the instant clusters dashboard.
<Frame><img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4a050ff646ed47e2170097444194b3f3" alt="" width="3136" height="2598" data-path="images/guides/nanochat/2.png" /></Frame>

<CodeGroup>
  ```bash Shell theme={null}
  ssh <username>@<cluster-hostname>
  ```
</CodeGroup>

You can also use `ssh -o ServerAliveInterval=60` - it sends a ping to the ssh server every 60s, so it keeps the TCP ssh session alive, even if there's no terminal input/output for a long time during training.

Once connected, you'll be in the login node of your Slurm cluster.

## Step 3: Clone nanochat and Set Up Environment

Let's clone the nanochat repository and set up the required dependencies.

<CodeGroup>
  ```bash Shell theme={null}
  # Clone the repository
  git clone https://github.com/karpathy/nanochat.git
  cd nanochat

  # Add ~/.local/bin to your PATH
  export PATH="$HOME/.local/bin:$PATH"

  # Source the Cargo environment
  source "$HOME/.cargo/env"
  ```
</CodeGroup>

**Install System Dependencies**

nanochat requires Python 3.10 and development headers:

<CodeGroup>
  ```bash Shell theme={null}
  # Update package manager and install Python dependencies
  sudo apt-get update
  sudo apt-get install -y python3.10-dev

  # Verify Python installation
  python3 -c "import sysconfig; print(sysconfig.get_path('include'))"
  ```
</CodeGroup>

## Step 4: Access GPU Resources

Use Slurm's `srun` command to allocate 8 GPUs for your training job:

<CodeGroup>
  ```bash Shell theme={null}
  srun --gres=gpu:8 --pty bash
  ```
</CodeGroup>

This command requests 8 GPUs and gives you an interactive bash session on a compute node. Once you're on the compute node, verify GPU access:

<CodeGroup>
  ```bash Shell theme={null}
  nvidia-smi
  ```
</CodeGroup>

You should see all 8 H100 GPUs listed with their memory and utilization stats like below.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=93378a3fae8db4f27c53c61d4f3c86aa" alt="" width="2222" height="2196" data-path="images/guides/nanochat/3.png" />
</Frame>

## Step 5: Configure Cache Directory

To optimize data loading performance, set the nanochat cache directory to the `/scratch` volume, which is optimized for high-throughput I/O:

<CodeGroup>
  ```bash Shell theme={null}
  export NANOCHAT_BASE_DIR="/scratch/$USER/nanochat/.cache/nanochat"
  ```
</CodeGroup>

This needs to be changed inside the `speedrun.sh` file and ensures that dataset streaming, checkpoints, and intermediate artifacts don't bottleneck your training.

<Info>
  This step is critical and without it, during training, you'll notice that your FLOP utilization is only \~13% instead of \~50%. This is due to dataloading bottlenecks.
</Info>

## Step 6: Run the Training Pipeline

Now you're ready to kick off the full training pipeline! nanochat includes a `speedrun.sh` script that orchestrates all training phases:

<CodeGroup>
  ```bash Shell theme={null}
  bash speedrun.sh

  # or you can use screen

  screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh
  ```
</CodeGroup>

This script will execute the following stages:

1. **Tokenizer Training** - Trains a GPT-4 style BPE tokenizer on FineWeb-Edu data
2. **Base Model Pretraining** - Trains the base transformer model with rotary embeddings and Muon optimizer
3. **Midtraining** - Fine-tunes on a curated mixture of SmolTalk, MMLU, and GSM8K tasks
4. **Supervised Fine-Tuning (SFT)** - Aligns the model for conversational interactions
5. **Evaluation** - Runs CORE benchmarks and generates a comprehensive report

The entire training process takes approximately **4 hours** on 8×H100 GPUs.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=d77d394dee60ff4576f461932ba317df" alt="" width="2606" height="2212" data-path="images/guides/nanochat/4.png" />
</Frame>

**Monitor Training Progress**

During training, you can monitor several key metrics:

* **Model Flops Utilization (MFU)**: Should be around 50% for optimal performance
* **tok/sec**: Tracks tokens processed per second of training
* **Step timing**: Each step should complete in a few seconds

The scripts automatically log progress and save checkpoints under `$NANOCHAT_BASE_DIR`.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=82bdc348257581badd6ef22c819dcd10" alt="" width="2606" height="2212" data-path="images/guides/nanochat/5.png" />
</Frame>

# nanochat Inference

## Step 1: Download Your Cluster's Kubeconfig

While training is running (or after it completes), download your cluster's kubeconfig from the Together AI dashboard. This will allow you to access the cluster using kubectl.

1. Go to your cluster in the Together AI dashboard
2. Click on the **View Kubeconfig** button
3. Copy and save the kubeconfig file to your local machine (e.g., `~/.kube/nanochat-cluster-config`)

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=c879f73961de55cfb06f4dd83602260b" alt="" width="3136" height="2598" data-path="images/guides/nanochat/6.png" />
</Frame>

## Step 2: Access the Compute Pod via kubectl

From your **local machine**, set up kubectl access to your cluster:

<CodeGroup>
  ```bash Shell theme={null}
  # Set the KUBECONFIG environment variable
  export KUBECONFIG=/path/to/nanochat-cluster-config

  # List pods in the slurm namespace
  kubectl -n slurm get pods
  ```
</CodeGroup>

You should see your Slurm compute pods listed. Identify the production pod where your training ran:

<CodeGroup>
  ```bash Shell theme={null}
  # Example output:
  # NAME                              READY   STATUS    RESTARTS   AGE
  # slurm-compute-production-abc123   1/1     Running   0          2h

  # Exec into the pod
  kubectl -n slurm exec -it <your-slurm-compute-production-pod> -- /bin/bash
  ```
</CodeGroup>

Once inside the pod, navigate to the nanochat directory:

<CodeGroup>
  ```bash Shell theme={null}
  cd /path/to/nanochat
  ```
</CodeGroup>

**Set Up Python Virtual Environment**

Inside the compute pod, set up the Python virtual environment using `uv`:

<CodeGroup>
  ```bash Shell theme={null}
  # Install uv (if not already installed)
  command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh

  # Create a local virtual environment
  [ -d ".venv" ] || uv venv

  # Install the repo dependencies with GPU support
  uv sync --extra gpu

  # Activate the virtual environment
  source .venv/bin/activate
  ```
</CodeGroup>

## Step 3: Launch the nanochat Web Server

Now that training is complete and your environment is set up, launch the FastAPI web server:

<CodeGroup>
  ```bash Shell theme={null}
  python -m scripts.chat_web
  ```
</CodeGroup>

The server will start on port 8000 inside the pod. You should see output indicating the server is running:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/7.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=7fec3be4e92c726b1f9490dfae41c6bc" alt="" width="2422" height="1666" data-path="images/guides/nanochat/7.png" />
</Frame>

## Step 4: Port Forward to Access the UI

In a **new terminal window on your local machine**, set up port forwarding to access the web UI:

<CodeGroup>
  ```bash Shell theme={null}
  # Set the KUBECONFIG (if not already set in this terminal)
  export KUBECONFIG=/path/to/nanochat-cluster-config

  # Forward port 8000 from the pod to local port 6818
  kubectl -n slurm port-forward <your-slurm-compute-production-pod> 6818:8000
  ```
</CodeGroup>

The port forwarding will remain active as long as this terminal session is open.

## Step 5: Chat with nanochat!

Open your web browser and navigate to:

```
http://localhost:6818/
```

You should see the nanochat web interface! You can now have conversations with your trained model. Go ahead and ask it its favorite question and see what reaction you get!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/8.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=3d5b642098e9f0a713cd231187bde974" alt="" width="2134" height="2172" data-path="images/guides/nanochat/8.png" />
</Frame>

## Understanding Training Costs and Performance

The nanochat training pipeline on 8×H100 Instant Clusters typically:

* **Training time**: \~4 hours for the full speedrun pipeline
* **Model Flops Utilization**: \~50% (indicating efficient GPU utilization)
* **Cost**: Approximately \$100 depending on your selected hardware and duration
* **Final model**: A fully functional conversational AI

After training completes, check the generated report `report.md` for detailed metrics.

## Troubleshooting

**GPU Not Available**

If `nvidia-smi` doesn't show GPUs after `srun`:

<CodeGroup>
  ```bash Shell theme={null}
  # Try requesting GPUs explicitly
  srun --gres=gpu:8 --nodes=1 --pty bash
  ```
</CodeGroup>

**Out of Memory Errors**

If you encounter OOM errors during training:

1. Check that `NANOCHAT_BASE_DIR` is set to `/scratch`
2. Ensure no other processes are using GPU memory
3. The default batch sizes should work on H100 80GB

**Port Forwarding Connection Issues**

If you can't connect to the web UI:

1. Verify the pod name matches exactly: `kubectl -n slurm get pods`
2. Ensure the web server is running: check logs in the pod terminal
3. Try a different local port if 6818 is in use

## Next Steps

Now that you have nanochat running, you can:

1. **Experiment with different prompts** - Test the model's conversational abilities and domain knowledge
2. **Fine-tune further** - Modify the SFT data or run additional RL training for specific behaviors
3. **Deploy to production** - Extend `chat_web.py` with authentication and persistence layers
4. **Scale the model** - Try the `run1000.sh` script for a larger model with better performance
5. **Integrate with other tools** - Use the inference API to build custom applications

For more details on the nanochat architecture and training process, visit the [nanochat GitHub repository](https://github.com/karpathy/nanochat).

## Additional Resources

* [Instant Clusters Documentation](/docs/instant-clusters)
* [Instant Clusters API Reference](/reference/clusters-create)
* [nanochat Repository](https://github.com/karpathy/nanochat)
* [Together AI Models](/docs/serverless-models)

***


Built with [Mintlify](https://mintlify.com).