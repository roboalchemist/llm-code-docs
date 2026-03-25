# Source: https://docs.anyscale.com/llm/fine-tuning.md

# Post-training for LLMs on Anyscale

[View Markdown](/llm/fine-tuning.md)

# Post-training for LLMs on Anyscale

LLM development typically has two phases: pretraining and post-training. Pretraining uses self-supervised next-token prediction on large, diverse corpora to learn general-purpose capabilities (a "base" model). Post-training adapts that model to excel at your specific application, domain, or behavioral requirements. This guide provides a comprehensive overview of the core LLM post-training methodologies, from continued pre-training (CPT) and supervised fine-tuning (SFT) to Reinforcement Learning from Human Feedback (RLHF), Reinforcement Learning from Verifiable Rewards (RLVR), and agentic tuning. By understanding these approaches, you can select the right strategy to build a powerful and specialized LLM on Anyscale.

## LLM post-training capabilities on Anyscale[​](#llm-post-training-capabilities-on-anyscale "Direct link to LLM post-training capabilities on Anyscale")

* **Various open-source models**: A curated collection of models ready for training, including gpt-oss, Llama, Mistral, Qwen, Gemma, and multimodal models such as LLaVA-Next.
* **Integrated training methods**: Easily switch between CPT, SFT, and RLHF with algorithms such as PPO, DPO, KTO, and ORPO, or RLVR with GRPO and DAPO.
* **Scalable compute**: Support for both full fine-tuning and parameter-efficient methods (LoRA, QLoRA, freeze-tuning).
* **Distributed GPU acceleration**: Memory-efficient scaling compatible with FSDP, DeepSpeed, and Megatron.
* **Monitoring and observability**: Integrations with Weights & Biases, MLflow, and TensorBoard for tracking performance and debugging.
* **Evaluation and serving**: Evaluate checkpoints with Ray Data and deploy them for inference with Ray Serve.

note

Feature availability and exact configurations can vary by model family and framework. Consult the latest Ray and Anyscale docs for specifics.

## Choose your framework[​](#choose-framework "Direct link to Choose your framework")

Anyscale supports multiple frameworks for LLM post-training, including LLaMA-Factory, SkyRL, and Ray Train. Each framework has different strengths for various use cases, from RLHF to RLVR and agentic tuning. To compare frameworks and choose the best fit for your needs, see [Choose a framework for LLM post-training](/llm/fine-tuning/comparison.md).

For hands-on tutorials, see the following:

* [Fine-tuning with LLaMA-Factory](https://console.anyscale.com/template-preview/llm_finetuning)
* [Fine-tune an LLM with Ray Train and DeepSpeed](https://console.anyscale.com/template-preview/deepspeed_finetune)
* [GRPO with SkyRL](/tutorials/train-llm-with-skyrl.md)

## Understand pre-training vs. post-training[​](#understand-pre-training-vs-post-training "Direct link to Understand pre-training vs. post-training")

Post-training is the process of adapting a pre-trained LLM to align with your specific domain, tasks, and behavioral goals. It starts with a general-purpose base model and applies specialized training techniques to enhance its performance, safety, and reliability for a particular application. For a detailed breakdown of the benefits, see [Why post-train your LLM](/llm/fine-tuning/why-post-train.md).

Pre-training builds general knowledge by training a model from scratch on massive, unlabeled text corpora, often containing trillions of tokens. This process is computationally extensive and costly. In contrast, post-training efficiently specializes the model using smaller, targeted datasets, allowing you to shape the model's behavior without the immense cost of training from scratch.

## Choose the right approach: fine-tuning vs. RAG vs. prompt engineering[​](#choose-the-right-approach-fine-tuning-vs-rag-vs-prompt-engineering "Direct link to Choose the right approach: fine-tuning vs. RAG vs. prompt engineering")

Before committing to post-training, it's crucial to select the right approach for your problem.

| Approach                             | When to use                                         | Advantages                                                     | Trade-offs                                                                      |
| ------------------------------------ | --------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Prompt engineering                   | Quick prototypes, simple tasks, single queries.     | Zero training cost, instant iteration.                         | Brittle, prompt length grows, can't inject new knowledge.                       |
| Retrieval-Augmented Generation (RAG) | Answering questions over a changing knowledge base. | Keeps model weights frozen, allows real-time data and updates. | Requires vector store (in-memory or external DB), relies on retrieval accuracy. |
| Fine-tuning (post-training)          | Adapting to a specific style, domain, or behavior.  | Lowest inference latency, strongest control over model.        | Requires training data and GPUs; weights are static until retrained.            |

## Core post-training methodologies[​](#core-post-training-methodologies "Direct link to Core post-training methodologies")

Post-training encompasses several key techniques, including CPT, SFT, and RLHF.

### Continued pre-training (CPT)[​](#continued-pretraining "Direct link to Continued pre-training (CPT)")

Continued pre-training extends the foundational learning process of an LLM on large amounts of unlabeled text. You use CPT to adapt a model to a new domain (for example, medical, legal, or scientific text) or to continue its general training.

Although its name is “continued pre-training,” it's classified as a post-training technique in this guide because you apply it after initial pre-training to a checkpoint, typically using domain-specific unlabeled text.

### Supervised fine-tuning (SFT)[​](#supervised-fine-tuning "Direct link to Supervised fine-tuning (SFT)")

SFT is a technique to adapt a pre-trained LLM to perform specific tasks. It refines the model's behavior by training it on a smaller, labeled dataset. SFT is often used to establish baseline instruction-following before preference optimization.

### Traditional RLHF: Reward modeling and PPO[​](#traditional-rlhf "Direct link to Traditional RLHF: Reward modeling and PPO")

RLHF refines a model's behavior (for example, helpfulness, safety, politeness) based on human preferences. Instead of learning from a single "correct" answer, the model learns from feedback on which of two or more responses is better.

The traditional RLHF process involves three steps:

1. **Collect preference data**: For a given prompt, generate multiple responses and have human labelers choose the preferred response over the rejected ones.
2. **Train a reward model (RM)**: Train a separate model to predict a scalar "reward" score that reflects the human preference. Preferred responses should receive higher scores.
3. **Optimize the LLM with PPO**: Apply a reinforcement learning algorithm such as Proximal Policy Optimization (PPO) with the trained RM to adjust the LLM's weights while regularizing with a KL penalty, guiding it to produce responses that achieve higher predicted reward scores.

### Other RLHF algorithms[​](#other-rlhf-algorithms "Direct link to Other RLHF algorithms")

Researchers have developed several simpler and more stable alternatives to the classic RM and PPO-based RLHF pipeline, including:

* **Direct Preference Optimization (DPO)**: Removes the explicit reward model and RL loop by directly optimizing a pairwise loss on chosen versus rejected responses, using a fixed reference model to implicitly regularize the policy.
* **Simple Preference Optimization (SimPO)**: Uses a reference-free objective that treats the (average) log-probability of a sequence as an implicit reward and adds a target-margin term—eliminating the frozen reference model and reducing memory while retaining strong performance.
* **Odds-Ratio Preference Optimization (ORPO)**: A single-stage, reference-free method that integrates preference learning into SFT by adding an odds-ratio penalty to the standard NLL loss—so you fine-tune once while contrasting favored versus disfavored responses.
* **Kahneman-Tversky Optimization (KTO)**: Trains from unary "thumbs-up/down" feedback using a prospect-theoretic (Kahneman—Tversky) utility, avoiding pairwise comparisons while matching or exceeding preference-based methods at various scales.

Anyscale supports DPO, SimPO, ORPO, and KTO—providing a flexible suite of preference optimization algorithms that make advanced alignment techniques more accessible to developers.

### Reinforcement Learning with Verifiable Rewards (RLVR)[​](#rlvr "Direct link to Reinforcement Learning with Verifiable Rewards (RLVR)")

Reinforcement Learning from Verifiable Rewards (RLVR) uses automated, verifiable rewards to train LLMs for tasks where correctness can be objectively determined. Instead of relying on human preferences, RLVR uses rule-based reward models, tests, tools, or simulations to verify if outputs meet specific criteria—such as whether code executes successfully or a query returns correct results.

Use RLVR with policy-optimization algorithms such as PPO, Group Relative Policy Optimization (GRPO), and Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO) to enhance the LLM's or agent's capability to utilize tools or perform in targeted environments. Common applications include coding tasks (for example, SWE-Bench) and text-to-SQL generation.

**Group Relative Policy Optimization (GRPO)**: Simplifies PPO by removing the critic or value model, reducing memory and complexity. It uses the group's average reward as the baseline, making GRPO well-suited for tasks with verifiable correctness such as code execution or format validation.

**Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO)**: Extends GRPO with four enhancements: Clip-Higher promotes diversity, Dynamic Sampling improves efficiency, Token-Level Policy Gradient Loss enables better long chain-of-thought reasoning, and Overlong Reward Shaping reduces noise for lengthy outputs.

## Agentic tuning, tools and environment interactions[​](#agentic-tuning "Direct link to Agentic tuning, tools and environment interactions")

Agentic tuning extends the paradigm of LLM post-training by shifting the focus from generating static text to creating autonomous agents. These agents learn to reason, plan, and interact with external tools and environments to accomplish complex, multi-step goals. Instead of optimizing for a single, high-quality response, agentic tuning optimizes a model's policy for a sequence of actions—such as making API calls, running code, or querying a database.

The training process often employs RLVR, where the model receives rewards based on verifiable outcomes from its interactions. For instance, an agent might receive a positive reward for successfully executing code that passes a unit test or for using a search tool to find a correct answer. This makes it a natural application for RLVR methodologies and algorithms such as PPO, GRPO, and DAPO, which are effective at refining an agent's ability to use tools reliably and complete tasks efficiently in specific environments.

## Compare full vs. freeze vs. parameter-efficient fine-tuning (PEFT)[​](#compare-full-freeze-peft "Direct link to Compare full vs. freeze vs. parameter-efficient fine-tuning (PEFT)")

Once you choose a methodology, you must decide how to apply the weight updates.

### Full fine-tuning[​](#full-fine-tuning "Direct link to Full fine-tuning")

Full fine-tuning updates all parameters of the model. It offers maximum control over the model's behavior but is computationally expensive and requires a significant amount of data.

* **Use case**: Critical applications such as safety alignment for a public model release.
* **Requires**: Significant GPU memory (often requiring distributed training with DeepSpeed ZeRO-3) and careful evaluation to prevent "catastrophic forgetting" of the model's original capabilities.

### Freeze tuning[​](#freeze-tuning "Direct link to Freeze tuning")

Layer freezing is a straightforward fine-tuning strategy that freezes some layers of the model and trains only selected layers—commonly freezing lower layers that capture fundamental language patterns while adapting upper layers that learn more abstract, task-specific representations. The intuition is that freezing helps preserve core capabilities, mitigates catastrophic forgetting, and reduces compute.

### Parameter-efficient fine-tuning (PEFT)[​](#peft "Direct link to Parameter-efficient fine-tuning (PEFT)")

PEFT methods freeze the vast majority of the base model's weights and only train a small number of new parameters (often less than 1% of the total). This dramatically reduces memory requirements and training time.

#### Low-rank adaptation (LoRA)[​](#lora "Direct link to Low-rank adaptation (LoRA)")

LoRA is a widely adopted PEFT method. Instead of updating the original weights (W) it learns a low-rank decomposition of the weight update (ΔW). It injects small, trainable matrices (A and B) into the model layers and learns the update as ΔW ≈ A × B.

**Why it matters:** The backpropagation runs only through the small A and B matrices, slashing VRAM usage and compute costs. Because you can insert adapters across layers (including lower ones responsible for basic linguistic features), LoRA can handle large domain shifts or tasks requiring new representations without touching most base weights.

**LoRA adapter deployment:** You can merge the learned ΔW back into the base weights for zero inference overhead, or load multiple LoRA adapters simultaneously to serve different tasks with a single base model. See [Deploy multi-LoRA adapters on LLMs](/llm/serving/multi-lora.md).

#### Quantized LoRA (QLoRA)[​](#qlora "Direct link to Quantized LoRA (QLoRA)")

QLoRA extends LoRA by applying quantization to the frozen base model weights. This further reduces memory footprint, making it possible to fine-tune very large models using fewer GPUs.

## Tips for LLM post-training[​](#tips-for-llm-post-training "Direct link to Tips for LLM post-training")

* Start with prompt engineering. Add RAG when you need up-to-date knowledge and traceable sources. Move to fine-tuning when you want more consistent behavior and lower latency.
* Use CPT when you want to adapt a base model to a new domain using unlabeled text.
* For most teams, begin with supervised fine-tuning (SFT), then add a light preference-optimization pass (such as DPO, ORPO, KTO, or SimPO). Reserve RLHF with PPO for cases that truly need strong behavioral shaping.
* Use parameter-efficient fine-tuning (PEFT, such as LoRA or QLoRA) for cost efficiency. Use full-model fine-tuning only when there's a large distribution shift and you've collected substantial training data.
* Invest in data quality—diverse instructions, hard/negative examples, and safety red-teaming. Good data yields better results than extra epochs.
* Always evaluate task performance alongside safety and robustness, and monitor for regressions and model drift.

## Summary[​](#summary "Direct link to Summary")

In this guide, you learned about the key concepts and methodologies for LLM post-training, including continued pre-training, supervised fine-tuning, RLHF techniques, RLVR, and parameter-efficient methods. You also learned how to choose between different approaches based on your specific requirements and constraints.
