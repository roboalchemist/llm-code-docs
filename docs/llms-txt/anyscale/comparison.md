# Source: https://docs.anyscale.com/llm/fine-tuning/comparison.md

# Choose a framework for LLM post-training

[View Markdown](/llm/fine-tuning/comparison.md)

# Choose a framework for LLM post-training

This page helps you choose the right framework for post-training large language models (LLMs) on Anyscale.

## Recommended approaches[​](#recommended-approaches "Direct link to Recommended approaches")

Anyscale supports post-training techniques including Supervised Fine-Tuning (SFT), Reinforcement Learning from Human Feedback (RLHF), Reinforcement Learning from Verifiable Rewards (RLVR) and agentic tuning. For more details, see [Post-training for LLMs on Anyscale](/llm/fine-tuning.md). The following table compares three frameworks for LLM post-training and agentic tuning on Anyscale:

| Framework         | Use cases and key features                                                                                                                                                                                                                                                                                            | Setup effort                                                                                | Integration with Anyscale and Ray                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **LLaMA-Factory** | - SFT and RLHF (DPO, KTO, PPO) for open-source LLMs; continued pretraining; multimodal recipes.<br />- Config-driven YAML runs; minimal code with provided configs.<br />- Guides for dataset prep, checkpointing, and experiment tracking (in Anyscale docs).<br />- Supports FSDP and DeepSpeed.                    | **Easy** — official guides and examples; minimal code when using provided configs.          | Use Ray train as orchestration; official Anyscale guides; runs on Ray clusters on Anyscale for scale-out training. |
| **SkyRL**         | - RLVR and agentic tuning with real environment interactions; long-horizon tasks (for example, SWE-Bench, Text2SQL).<br />- Modular full-stack RLVR algorithms (PPO, GRPO, DAPO).<br />- Async rollouts, custom environments, flexible model placement and colocation.<br />- Supports FSDP, DeepSpeed, and Megatron. | **Medium** — powerful and flexible; requires environment setup and Ray cluster familiarity. | Uses Ray for orchestration; deployable on Anyscale Ray clusters.                                                   |
| **Ray Train**     | - Custom LLM and reward-model training and other architectures; low-level control with PyTorch, Lightning, and HF Accelerate.<br />- Scalable distributed training across nodes.<br />- GPU and accelerator targeting; checkpoints; fault tolerance.<br />- Rich Hugging Face integrations.                           | **Medium** — you write training code, but many end-to-end examples exist.                   | Core Ray training library; first-class on Anyscale (Ray clusters on Anyscale; Train scales across nodes natively). |

## Other LLM post-training and RL frameworks[​](#other-llm-post-training-and-rl-frameworks "Direct link to Other LLM post-training and RL frameworks")

While the above recommendations cover most practical needs, many other open-source RL libraries using Ray are easy to run on Anyscale as well, such as verl and NeMo-RL. For more information on these libraries, see the [Open Source RL Libraries for LLMs](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms) blog post.

Because most of these libraries are built on Ray, they can run on any Ray cluster, including the ones provided on Anyscale. For an example of running SkyRL on Anyscale, see [GRPO with SkyRL](/tutorials/train-llm-with-skyrl.md). For a detailed overview and comparison of additional libraries, see [Open Source RL Libraries for LLMs](https://www.anyscale.com/blog/open-source-rl-libraries-for-llms).

note

This comparison reflects current practices and may evolve with new releases. For the latest information, consult Anyscale documentation or the linked resources.
