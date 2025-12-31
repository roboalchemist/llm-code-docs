# Source: https://docs.vllm.ai/en/stable/training/rlhf/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/training/rlhf.md "Edit this page")

# Reinforcement Learning from Human Feedback[¶](#reinforcement-learning-from-human-feedback "Permanent link")

Reinforcement Learning from Human Feedback (RLHF) is a technique that fine-tunes language models using human-generated preference data to align model outputs with desired behaviors. vLLM can be used to generate the completions for RLHF.

The following open-source RL libraries use vLLM for fast rollouts (sorted alphabetically and non-exhaustive):

-   [Cosmos-RL](https://github.com/nvidia-cosmos/cosmos-rl)
-   [ms-swift](https://github.com/modelscope/ms-swift/tree/main)
-   [NeMo-RL](https://github.com/NVIDIA-NeMo/RL)
-   [Open Instruct](https://github.com/allenai/open-instruct)
-   [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)
-   [PipelineRL](https://github.com/ServiceNow/PipelineRL)
-   [Prime-RL](https://github.com/PrimeIntellect-ai/prime-rl)
-   [SkyRL](https://github.com/NovaSky-AI/SkyRL)
-   [TRL](https://github.com/huggingface/trl)
-   [Unsloth](https://github.com/unslothai/unsloth)
-   [verl](https://github.com/volcengine/verl)

See the following basic examples to get started if you don\'t want to use an existing library:

-   [Training and inference processes are located on separate GPUs (inspired by OpenRLHF)](../../examples/offline_inference/rlhf/)
-   [Training and inference processes are colocated on the same GPUs using Ray](../../examples/offline_inference/rlhf_colocate/)
-   [Utilities for performing RLHF with vLLM](../../examples/offline_inference/rlhf_utils/)

See the following notebooks showing how to use vLLM for GRPO:

-   [Efficient Online Training with GRPO and vLLM in TRL](https://huggingface.co/learn/cookbook/grpo_vllm_online_training)
-   [Qwen-3 4B GRPO using Unsloth + vLLM](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(4B)-GRPO.ipynb)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [October 24, 2025] ]