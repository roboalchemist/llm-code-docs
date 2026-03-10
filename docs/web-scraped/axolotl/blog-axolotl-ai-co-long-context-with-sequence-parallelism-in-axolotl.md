# Source: https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl

Title: Enabling Long Context Training with Sequence Parallelism in Axolotl

URL Source: https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl

Markdown Content:
[Back to Articles](https://huggingface.co/blog)

[![Image 1: Dan Saunders's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1647406334843-noauth.jpeg)](https://huggingface.co/djsaunde)

[![Image 2: wing lian's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/641dfddf3bae5a77636817c5/2IwNwh9kK98eCHUmOGoWD.png)](https://huggingface.co/winglian)

_This post originally appeared on Axolotl's Substack. You can read the [original version here](https://axolotlai.substack.com/p/enabling-long-context-training-with)._

Training large language models (LLMs) with long contexts has become an important capability as models continue to expand in both size and context length. However, handling these extended sequences presents significant memory challenges, often resulting in out-of-memory (OOM) errors on even the largest GPUs. Axolotl now offers a solution to this problem through the implementation of sequence parallelism (SP), allowing researchers and developers to train models with significantly longer contexts than previously possible.

[![Image 3: Generated with ChatGPT 4o Image Generation](https://cdn-uploads.huggingface.co/production/uploads/62316d0ab43b2177c781e5af/Z1bnW2xb5x-7qH57_Ns_B.png)](https://cdn-uploads.huggingface.co/production/uploads/62316d0ab43b2177c781e5af/Z1bnW2xb5x-7qH57_Ns_B.png)

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#what-is-sequence-parallelism) What is Sequence Parallelism?
----------------------------------------------------------------------------------------------------------------------------------------------------------

Sequence parallelism is a technique that distributes the processing of a single sequence across multiple GPUs. Unlike other parallelism methods that split model parameters (tensor parallelism) or training examples (data parallelism), SP splits the input sequence itself into chunks, with each GPU handling a portion of the sequence.

This approach is particularly effective for long context training because it directly addresses the primary limitation: the quadratic memory growth related to sequence length in attention mechanisms.

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#sequence-parallelism-implementation-in-axolotl) Sequence Parallelism Implementation in Axolotl
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Axolotl's implementation of sequence parallelism uses the `ring-flash-attn` library, specifically employing the `llama3_flash_attn_varlen_func` implementation from the LLaMA-3 technical report. This approach distributes attention calculations across multiple GPUs while maintaining computational efficiency.

The key benefits of this implementation include:

* **Memory Efficiency**: By splitting sequences across GPUs, the memory required per GPU is significantly reduced
* **Scaling Capability**: Enables training with sequence lengths that would otherwise be impossible on available hardware
* **Composability**: Works with sample packing and variable length sequences, as well as many other advanced features that Axolotl supports (Liger kernel, `torch.compile`, FSDP, DeepSpeed, etc.)

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#how-sequence-parallelism-works) How Sequence Parallelism Works
-------------------------------------------------------------------------------------------------------------------------------------------------------------

When sequence parallelism is enabled, the attention computation is distributed across GPUs according to the specified `sequence_parallel_degree`. If you set this value to 4, for example, each sequence will be split into 4 equal-length chunks, with each chunk processed on a different GPU.

The implementation handles:

* Splitting the sequences
* Distributing the computation
* Managing the communication between GPUs
* Ensuring correct gradient flow during backpropagation

Several of these features are inherited as a result of integrating the `ring-flash-attn` package!

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#configuring-sequence-parallelism-in-axolotl) Configuring Sequence Parallelism in Axolotl
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Setting up sequence parallelism in Axolotl is straightforward. After installing `ring-flash-attn`(recommended via `pip install axolotl[ring-flash-attn]`, you just need to add the `sequence_parallel_degree` parameter to your configuration file:

```
sequence_parallel_degree: 4  # Set to the number of GPUs to split sequences across
flash_attention: true  # SP requires flash attention
micro_batch_size: 1  # SP requires this is set to 1
# (optional) strides across the key dimension; larger values use more memory but should make training a bit faster
heads_k_stride: 1
```

The `sequence_parallel_degree` should be set to a divisor of the number of available GPUs. For example, if you have 8 GPUs available, you could set this to 2, 4, or 8 depending on your memory requirements.

Important considerations:

* The SP degree must evenly divide your available GPU count, sequence length, and the number of attention heads in your model
* Flash attention must be enabled for sequence parallelism to work
* Micro batch size must be set to 1
* Sample packing is supported
* Using GPUs with NVLink connections will improve performance due to inter-GPU communication in the `ring-flash-attn` implementation
* RL trainer support is coming soon!

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#memory-savings-and-scaling) Memory Savings and Scaling
-----------------------------------------------------------------------------------------------------------------------------------------------------

The memory savings from sequence parallelism are substantial. In theory, with a sequence parallel degree of `n`, you can expect to reduce the memory required for attention operations by approximately a factor of `n`. In practice, due to overhead from communication between GPUs, memory savings are somewhat lower, and interact with other training configuration parameters.

For example, with a SP degree of 4, you should be able to handle sequences up to 3-4X longer than what would fit on a single GPU.

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#benchmark-results) Benchmark Results
-----------------------------------------------------------------------------------------------------------------------------------

This benchmark evaluates sequence parallelism scaling with LLaMA 3.1 8B across different training approaches with various GPU models. We generated artificial data, and then determined the maximum sequence length (that doesn’t OOM during training) that could be run for a given model on a given number of GPUs (equal to the SP degree). To push the sequence length limits and training speed further, we enabled [Liger kernels](https://axolotl-ai-cloud.github.io/axolotl/docs/custom_integrations.html#liger-kernels) and used the [AdamW 8bit optimizer](https://axolotl-ai-cloud.github.io/axolotl/docs/torchao.html).

Note that, in these benchmarks, we _don’t_ use techniques like gradient checkpointing, which would tradeoff speed for even more VRAM savings. For example, with `gradient_checkpointing: true`, we were successful in running the fine-tuning of LLaMA 3.1 8B with 250K+ context length on 8 x H100s, although single training steps took upwards of 1 minute (!). Set this value (or `gradient_checkpointing: offload` for even more VRAM savings, while trading off more speed) in your Axolotl config to test this yourself, and experiment to find the best settings of these values for your use case.

Configs for these benchmark runs can be found [here](https://gist.github.com/djsaunde/ba03c2113bba5ea1d523d5b1e5cbdb54) and [here](https://gist.github.com/djsaunde/17978f54d0b205115f0d4564382e01f5). Benchmark code can be found [here](https://gist.github.com/djsaunde/17978f54d0b205115f0d4564382e01f5) and [here](https://gist.github.com/djsaunde/a38836c72343a30cc99637bf4e3e1c90).

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#llama-31-8b-full-finetune) LLaMA 3.1 8B Full Finetune
----------------------------------------------------------------------------------------------------------------------------------------------------

Full fine-tuning shows solid context length scaling, reaching 5x the single-GPU context length when using 8 GPUs.

As expected, the “speedup / num. GPUs” metric decreases with increased parallelism due to inter-GPU communication overhead, but the primary benefit remains the ability to handle progressively longer sequences. Be sure to choose SP degree and sequence length wisely in order to balance your VRAM savings and training speed!

### [](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#h100-benchmark) H100 Benchmark

| SP Degree | Max Context Length | Context Scaling | Tokens/sec | Avg Time (sec) | Speedup | Speedup / num. GPUs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 9,216 | 1.00x | 7,317.50 | 1.2594 | 1.00x | 100.0% |
| 2 | 12,288 | 1.33x | 11,010.05 | 1.1161 | 1.50x | 75.2% |
| 4 | 24,576 | 2.67x | 14,278.66 | 1.7212 | 1.95x | 48.8% |
| 8 | 46,080 | 5.00x | 16,035.84 | 2.8736 | 2.19x | 27.4% |

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#llama-31-8b-qlora-finetune) LLaMA 3.1 8B QLoRA Finetune
------------------------------------------------------------------------------------------------------------------------------------------------------

QLoRA demonstrates exceptional context length scaling, with near linear scaling in our H100 benchmark, and exact linear scaling in our 4090 benchmark. The reduced memory footprint of 4-bit quantization enables this improved context handling capability.

The declining “speedup / num. GPUs” metric follows the expected pattern as inter-GPU communication increases. Once again, please experiment with SP degree and sequence length to balance VRAM savings and training speed.

### [](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#h100-benchmark-1) H100 Benchmark

| SP Degree | Max Context Length | Context Scaling | Tokens/sec | Avg Time (sec) | Speedup | Speedup / num. GPUs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 17,408 | 1.00x | 9,104.38 | 1.912 | 1.00x | 100.0% |
| 2 | 34,816 | 2.00x | 15,806.46 | 2.2026 | 1.74x | 86.8% |
| 4 | 66,560 | 3.82x | 12,313.60 | 5.4054 | 1.35x | 33.8% |
| 8 | 129,024 | 7.41x | 11,096.06 | 11.6279 | 1.22x | 15.2% |

[![Image 4: Max context length scaling with GPU count / SP degree on NVIDIA H100s, for full-finetuning and 4-bit QLoRA training, respectively.](https://cdn-uploads.huggingface.co/production/uploads/62316d0ab43b2177c781e5af/HCXmoDMd85KGVD9P08Az4.png)](https://cdn-uploads.huggingface.co/production/uploads/62316d0ab43b2177c781e5af/HCXmoDMd85KGVD9P08Az4.png) Max context length scaling with GPU count / SP degree on NVIDIA H100s, for full-finetuning and 4-bit QLoRA training, respectively.

### [](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#4090-benchmark) 4090 Benchmark

| SP Degree | Max Context Length | Context Scaling | Tokens/sec | Avg Time (sec) | Speedup | Speedup / num. GPUs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 4,096 | 1.00x | 3,674.11 | 1.1148 | 1.00x | 100.0% |
| 2 | 8,192 | 2.00x | 5,021.70 | 1.6313 | 1.37x | 68.3% |
| 4 | 16,384 | 4.00x | 6,455.30 | 2.5381 | 1.76x | 43.9% |
| 8 | 32,768 | 8.00x | 3,244.03 | 10.101 | 0.88x | -11.0% |

[![Image 5: Exact linear context length scaling with GPU count / SP degree on NVIDIA 4090s for QLoRA training.](https://cdn-uploads.huggingface.co/production/uploads/62316d0ab43b2177c781e5af/hdZax1cb4HCEvMJz9NFNR.png)](https://cdn-uploads.huggingface.co/production/uploads/62316d0ab43b2177c781e5af/hdZax1cb4HCEvMJz9NFNR.png) Exact linear context length scaling with GPU count / SP degree on NVIDIA 4090s for QLoRA training.

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#feature-composability) Feature Composability
-------------------------------------------------------------------------------------------------------------------------------------------

Our SP implementation is compatible with several other important time- and memory-saving optimizations supported in Axolotl, including (but not limited to):

* Liger kernels
* FSDP
* DeepSpeed ZeRO 1-3
* `torch.compile`
* Sample packing

Try it out with your favorite Axolotl features (and please open a [GitHub issue](https://github.com/axolotl-ai-cloud/axolotl/issues) if you run into any problems)!

[](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl#getting-started) Getting Started
-------------------------------------------------------------------------------------------------------------------------------

To start using sequence parallelism in your Axolotl configurations, make sure you have multiple GPUs available, enable flash attention, and set the sequence parallel degree appropriately.

For more information, check out the [sequence parallelism documentation](https://axolotl-ai-cloud.github.io/axolotl/docs/sequence_parallelism.html) and the [sequence parallelism pull request](https://github.com/axolotl-ai-cloud/axolotl/pull/2412).

* GitHub:[https://github.com/axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl)
* Website:[https://axolotl.ai/](https://axolotl.ai/)
* Docs:[https://axolotl-ai-cloud.github.io/axolotl/](https://axolotl-ai-cloud.github.io/axolotl/)
