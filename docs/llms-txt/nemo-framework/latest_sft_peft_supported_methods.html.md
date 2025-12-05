# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/supported_methods.html.md

Title: Supported PEFT Methods — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/supported_methods.html

Published Time: Fri, 18 Jul 2025 19:27:33 GMT

Markdown Content:
Supported PEFT Methods[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/supported_methods.html.md#supported-peft-methods "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

NeMo 2.0[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/supported_methods.html.md#nemo-2-0 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

NeMo 2.0 supports the following PEFT tuning methods:

1.   **LoRA**: [LoRA: Low-Rank Adaptation of Large Language Models](http://arxiv.org/abs/2106.09685.md)

    *   LoRA makes fine-tuning efficient by representing weight updates with two low rank decomposition matrices. The original model weights remain frozen, while the low-rank decomposition matrices are updated to adapt to the new data, keeping the number of trainable parameters low. In contrast with adapters, the original model weights and adapted weights can be combined during inference, avoiding any architectural change or additional latency in the model at inference time.

    *   In NeMo, you can customize the adapter bottleneck dimension and the target modules to apply LoRA. LoRA can be applied to any linear layer. In a transformer model, this includes 1) Q, K, V attention projections, 2) attention output projection layer, and 3) either or both of the two transformer MLP layers. For QKV, NeMo’s attention implementation fuses QKV into a single projection, so our LoRA implementation learns a single low-rank projection for QKV combined.

2.   **DoRA**: [DoRA: Weight-Decomposed Low-Rank Adaptation](https://arxiv.org/abs/2402.09353.md)

    *   DoRA decomposes the pre-trained weight into magnitude and direction. It learns a separate magnitude parameter while employing LoRA for directional updates, efficiently minimizing the number of trainable parameters. DoRA enhances both the learning capacity and training stability of LoRA while avoiding any additional inference overhead. DoRA has been shown to consistently outperform LoRA on various downstream tasks.

    *   In NeMo, DoRA leverages the same adapter structure as LoRA. NeMo adds support for Tensor Parallelism and Pipeline Parallelism for DoRA, enabling DoRA to be scaled to larger model variants.

NeMo 1.0 (Legacy)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/supported_methods.html.md#nemo-1-0-legacy "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

1.   **LoRA**: [LoRA: Low-Rank Adaptation of Large Language Models](http://arxiv.org/abs/2106.09685.md)

2.   **QLoRA**: [QLoRA: Efficient Finetuning of Quantized LLMs](http://arxiv.org/abs/2305.14314.md)

    *   Similar to LoRA, QLoRA keeps the original model weights frozen while introducing low-rank adapters for customization. However, QLoRA goes a step further by quantizing the frozen linear weights with a custom 4-bit data type called Normal Float 4 (NF4). The adapters are identical to those of LoRA and kept in BF16.

    *   Compared to LoRA, QLoRA is up to 60% more memory-efficient, allowing for fine-tuning large models with smaller/less GPUs and/or higher batch size. QLoRA is able to achieve the same accuracy, although a different convergence recipe may be required. However, the drawback is that QLoRA training is slower than LoRA by 50% to 200%.

    *   For more details, please visit the NeMo QLoRA Guide.

3.   **P-Tuning**: [GPT Understands, Too](https://arxiv.org/abs/2103.10385.md)

    *   P-Tuning is an example of the prompt learning family of methods, in which trainable virtual tokens are inserted into the model input prompt to induce it to perform a task. Virtual tokens (also called “continuous” or “soft” tokens) are embeddings that have no concrete mapping to strings or characters within the model’s vocabulary. They are simply 1D vectors that match the dimensionality of real tokens which make up the model’s vocabulary.

    *   In P-Tuning, an intermediate MLP model is used to generate virtual token embeddings. We refer to this intermediate model as our `prompt_encoder`. The prompt encoder parameters are randomly initialized at the start of p-tuning. All base model parameters are frozen, and only the prompt encoder weights are updated at each training step.

    *   In Nemo, you can customize the number of virtual tokens, as well as the embedding and MLP bottleneck dimensions.

4.   **Adapters (Canonical)**: [Parameter-Efficient Transfer Learning for NLP](http://arxiv.org/abs/1902.00751.md)

    *   Adapters (Houlsby setup) is one of the first PEFT methods applied to NLP. Adapter tuning is more efficient than full fine-tuning because the base model weights are frozen, while only a small number of adapter module weights are updated. In this method, two linear layers with a bottleneck and a non-linear activation are inserted into each transformer layer via a residual connection. In each case, the output linear layer is initialized to 0 to ensure that an untrained adapter does not affect the normal forward pass of the transformer layer.

    *   In NeMo, you can customize the adapter bottleneck dimension, adapter dropout amount, as well as the type and position of normalization layer.

5.   **IA3**: [Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning](http://arxiv.org/abs/2205.05638.md)

    *   IA3 makes fine-tuning efficient by rescaling activations with learned vectors. The rescaling layers are injected in the attention (for key and value) and feedforward modules in the base model. Similar to other PEFT methods, only the rescaling vectors are updated during fine-tuning to adapt to the new data so the number of updated parameters is low. However, since rescaling vectors are much smaller than low rank matrices (LoRA) and bottleneck layers (Adapters), IA3 cuts down the number of trainable parameters further by an order of magnitude. The learning rescaling vectors can also be merged with the base weights, leading to no architectural change and no additional latency at inference time.

    *   There is no hyperparameter to tune for the IA3 adapter.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/sft_peft/supported_methods.html.md#nemo-1-0-legacy)
- [LoRA: Low-Rank Adaptation of Large Language Models](http://arxiv.org/abs/2106.09685.md)
- [DoRA: Weight-Decomposed Low-Rank Adaptation](https://arxiv.org/abs/2402.09353.md)
- [QLoRA: Efficient Finetuning of Quantized LLMs](http://arxiv.org/abs/2305.14314.md)
- [GPT Understands, Too](https://arxiv.org/abs/2103.10385.md)
- [Parameter-Efficient Transfer Learning for NLP](http://arxiv.org/abs/1902.00751.md)
- [Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning](http://arxiv.org/abs/2205.05638.md)
