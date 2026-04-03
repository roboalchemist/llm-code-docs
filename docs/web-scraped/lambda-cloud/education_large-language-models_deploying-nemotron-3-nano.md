# Deploying NVIDIA Nemotron 3 Nano using vLLM -

Source: https://docs.lambda.ai/education/large-language-models/deploying-nemotron-3-nano/

---

[llm ](../../../tags/#tag:llm)
# Deploying NVIDIA Nemotron 3 Nano using vLLM [# ](#deploying-nvidia-nemotron-3-nano-using-vllm)

[NVIDIA Nemotron 3 Nano ](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)uses a [Mamba state layer ](https://github.com/state-spaces/mamba)on top of a transformer Mixture-of-Experts (MoE) backbone. This architecture yields up to four times the output-tokens-per-energy as Nemotron Nano 2 while still scoring at or above the current open frontier models on SWE-Bench, GPQA Diamond, and IFBench. This efficiency gain comes from introducing a user-supplied *thinking budget *parameter that caps per-request reasoning length, allowing users to tune latency and accuracy curves without touching the core model. 

This document provides an overview of Nemotron 3 Nano, and then shows you how to deploy and benchmark the model on Lambda Cloud. 

## Model details [# ](#model-details)

### Overview [# ](#overview)

- *Name: *`NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`
- *Author: *NVIDIA 
- *Architecture: *MoE 
- *Core capabilities: *Fast reasoning, long-context understanding, robust coding performance, robust tool-use performance 
- *License: *[NVIDIA Open Model License Agreement ](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/)
### Specifications [# ](#specifications)

- *Context window: *1,000,000 tokens 
- *Weights-on-disk: *58GB 
- *Idle VRAM usage: *120GB 
### Recommended Lambda VRAM configuration [# ](#recommended-lambda-vram-configuration)

- *Instances: ***1x B200 (180 GB SXM6) **or **1x H100 (80 GB SXM5) **(minimum recommended 4096 sequence length) 
- *1-Click Clusters: ***16x B200 (180 GB) **(max sequence length with FP8 KV cache) 
## Deployment and benchmarking [# ](#deployment-and-benchmarking)

### Deploying to a single-GPU instance [# ](#deploying-to-a-single-gpu-instance)

You can run NVIDIA Nemotron 3 Nano on any instance type that has enough VRAM to comfortably support it. For example, to deploy Nemotron 3 Nano on a **1x B200 (180 GB SXM6) **instance running the `Lambda Stack 22.04`image: 

- In the Lambda Cloud Console, navigate to the [Instances page ](https://cloud.lambda.ai/instances)and click **Launch instance **. A modal appears. 
- Follow the steps in the instance launch wizard. Select the following options: 
  - *Instance type: *Select **1x B200 (180 GB SXM6) **. 
  - *Base image: *Select **Lambda Stack 22.04 **. 
  - *Security: *Create a new firewall ruleset called `nemotron-3-nano`and add a rule to allow incoming traffic to port `TCP/8000`. 
- After your instance launches, find the row for your instance, and then click **Launch **in the **Cloud IDE **column. JupyterLab opens in a new window. 
- In JupyterLab's **Launcher **tab, under **Other **, click **Terminal **to open a new terminal. 
- 
In your terminal, install `uv`, set up a Python virtual environment, and then begin serving Nemotron 3 Nano with vLLM. 

```
`[](#__codelineno-0-1)curl -LsSf https://astral.sh/uv/install.sh | sh
[](#__codelineno-0-2)uv venv --python 3.12 --seed
[](#__codelineno-0-3)source .venv/bin/activate
[](#__codelineno-0-4)uv pip install vllm --torch-backend=auto
[](#__codelineno-0-5)VLLM_SERVER_DEV_MODE=1 vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 \
[](#__codelineno-0-6)  --port 8000 \
[](#__codelineno-0-7)  --served-model-name nemotron-3-nano \
[](#__codelineno-0-8)  --trust-remote-code \
[](#__codelineno-0-9)  --enable-sleep-mode
`
```
