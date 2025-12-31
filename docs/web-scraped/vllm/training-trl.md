# Source: https://docs.vllm.ai/en/stable/training/trl/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/training/trl.md "Edit this page")

# Transformers Reinforcement Learning[¶](#transformers-reinforcement-learning "Permanent link")

[Transformers Reinforcement Learning](https://huggingface.co/docs/trl) (TRL) is a full stack library that provides a set of tools to train transformer language models with methods like Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), Direct Preference Optimization (DPO), Reward Modeling, and more. The library is integrated with 🤗 transformers.

Online methods such as GRPO or Online DPO require the model to generate completions. vLLM can be used to generate these completions!

See the [vLLM integration guide](https://huggingface.co/docs/trl/main/en/vllm_integration) in the TRL documentation for more information.

TRL currently supports the following online trainers with vLLM:

-   [GRPO](https://huggingface.co/docs/trl/main/en/grpo_trainer)
-   [Online DPO](https://huggingface.co/docs/trl/main/en/online_dpo_trainer)
-   [RLOO](https://huggingface.co/docs/trl/main/en/rloo_trainer)
-   [Nash-MD](https://huggingface.co/docs/trl/main/en/nash_md_trainer)
-   [XPO](https://huggingface.co/docs/trl/main/en/xpo_trainer)

To enable vLLM in TRL, set the `use_vllm` flag in the trainer configuration to `True`.

## Modes of Using vLLM During Training[¶](#modes-of-using-vllm-during-training "Permanent link")

TRL supports **two modes** for integrating vLLM during training: **server mode** and **colocate mode**. You can control how vLLM operates during training with the `vllm_mode` parameter.

### Server mode[¶](#server-mode "Permanent link")

In **server mode**, vLLM runs as an independent process on dedicated GPUs and communicates with the trainer through HTTP requests. This configuration is ideal when you have separate GPUs for inference, as it isolates generation workloads from training, ensuring stable performance and easier scaling.

    from trl import GRPOConfig

    training_args = GRPOConfig(
        ...,
        use_vllm=True,
        vllm_mode="server",  # default value, can be omitted
    )

### Colocate mode[¶](#colocate-mode "Permanent link")

In **colocate mode**, vLLM runs inside the trainer process and shares GPU memory with the training model. This avoids launching a separate server and can improve GPU utilization, but may lead to memory contention on the training GPUs.

    from trl import GRPOConfig

    training_args = GRPOConfig(
        ...,
        use_vllm=True,
        vllm_mode="colocate",
    )

Some trainers also support **vLLM sleep mode**, which offloads parameters and caches to GPU RAM during training, helping reduce memory usage. Learn more in the [memory optimization docs](https://huggingface.co/docs/trl/main/en/reducing_memory_usage#vllm-sleep-mode).

Info

For detailed configuration options and flags, refer to the documentation of the specific trainer you are using.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [September 30, 2025] ]