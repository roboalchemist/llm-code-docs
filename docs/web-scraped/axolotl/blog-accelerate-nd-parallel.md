# Source: https://huggingface.co/blog/accelerate-nd-parallel

Title: Accelerate ND-Parallel: A guide to Efficient Multi-GPU Training

URL Source: https://huggingface.co/blog/accelerate-nd-parallel

Markdown Content:
Accelerate ND-Parallel: A guide to Efficient Multi-GPU Training
===============

[![Image 1: Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)Hugging Face](https://huggingface.co/)

* [Models](https://huggingface.co/models)
* [Datasets](https://huggingface.co/datasets)
* [Spaces](https://huggingface.co/spaces)
* Community  
* [Docs](https://huggingface.co/docs)
* [Enterprise](https://huggingface.co/enterprise)
* [Pricing](https://huggingface.co/pricing)
*
*

* * *

* [Log In](https://huggingface.co/login)
* [Sign Up](https://huggingface.co/join)

[Back to Articles](https://huggingface.co/blog)

[](https://huggingface.co/blog/accelerate-nd-parallel#accelerate-nd-parallel-a-guide-to-efficient-multi-gpu-training) Accelerate ND-Parallel: A guide to Efficient Multi-GPU Training
=====================================================================================================================================================================================

Published August 8, 2025

[Update on GitHub](https://github.com/huggingface/blog/blob/main/accelerate-nd-parallel.md)

[- [x] Upvote 93](https://huggingface.co/login?next=%2Fblog%2Faccelerate-nd-parallel)

* [![Image 2](https://cdn-avatars.huggingface.co/v1/production/uploads/1594651707950-noauth.jpeg)](https://huggingface.co/lewtun "lewtun")
* [![Image 3](https://huggingface.co/avatars/46e4669ef1b08e449fd46bec60eb66e8.svg)](https://huggingface.co/0xe69756 "0xe69756")
* [![Image 4](https://huggingface.co/avatars/2d3760a0ab378c7ce9769a8fa0614b55.svg)](https://huggingface.co/chewkokwah "chewkokwah")
* [![Image 5](https://cdn-avatars.huggingface.co/v1/production/uploads/5fd5e18a90b6dc4633f6d292/gZXHW5dd9R86AV9LMZ--y.png)](https://huggingface.co/MaziyarPanahi "MaziyarPanahi")
* [![Image 6](https://cdn-avatars.huggingface.co/v1/production/uploads/600a8fbd1dcb38f00c1ccb0a/BBnD0KtX9-MVBVHMQYqzA.jpeg)](https://huggingface.co/dev7halo "dev7halo")
* [![Image 7](https://huggingface.co/avatars/bfcfd7c222e2cea4f02d314c35734150.svg)](https://huggingface.co/Pratik "Pratik")
* +87

[![Image 8: Salman Mohammadi's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/64e4d0707d26615b5d4bf775/c8EbVvgGvQW7fgHdKI6fh.jpeg)](https://huggingface.co/smohammadi)

[Salman Mohammadi smohammadi Follow](https://huggingface.co/smohammadi)

[![Image 9: Axolotl AI's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/641dfddf3bae5a77636817c5/Wa6Qn38GOAlhl6ClMv_Q3.png)](https://huggingface.co/axolotl-ai-co "Axolotl AI")[axolotl-ai-co](https://huggingface.co/axolotl-ai-co)

[![Image 10: Matej Sirovatka's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/658f19cfa02954c982f540eb/qN2eqJZnWQ2H1xlGYeAKj.jpeg)](https://huggingface.co/siro1)

[Matej Sirovatka siro1 Follow](https://huggingface.co/siro1)

[![Image 11: wing lian's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/641dfddf3bae5a77636817c5/2IwNwh9kK98eCHUmOGoWD.png)](https://huggingface.co/winglian)

[wing lian winglian Follow](https://huggingface.co/winglian)

[![Image 12: Axolotl AI's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/641dfddf3bae5a77636817c5/Wa6Qn38GOAlhl6ClMv_Q3.png)](https://huggingface.co/axolotl-ai-co "Axolotl AI")[axolotl-ai-co](https://huggingface.co/axolotl-ai-co)

[![Image 13: Marc Sun's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/63ce875d199b36f7552d4f07/bpUrvhXDagzRqZ3vxTcSF.jpeg)](https://huggingface.co/marcsun13)

[Marc Sun marcsun13 Follow](https://huggingface.co/marcsun13)

[![Image 14: Dan Saunders's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/1647406334843-noauth.jpeg)](https://huggingface.co/djsaunde)

[Dan Saunders djsaunde Follow](https://huggingface.co/djsaunde)

[![Image 15: Axolotl AI's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/641dfddf3bae5a77636817c5/Wa6Qn38GOAlhl6ClMv_Q3.png)](https://huggingface.co/axolotl-ai-co "Axolotl AI")[axolotl-ai-co](https://huggingface.co/axolotl-ai-co)

* [Contents](https://huggingface.co/blog/accelerate-nd-parallel#contents "Contents")

* [Data Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#data-parallelism "Data Parallelism")

* [Fully Sharded Data Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism "Fully Sharded Data Parallelism")

* [Tensor Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#tensor-parallelism "Tensor Parallelism")

* [Context Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#context-parallelism "Context Parallelism")

* [ND Parallelisms](https://huggingface.co/blog/accelerate-nd-parallel#nd-parallelisms "ND Parallelisms")
  * [Hybrid Sharded Data Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#hybrid-sharded-data-parallelism "Hybrid Sharded Data Parallelism")

  * [Fully Sharded Data Parallelism + Tensor Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism--tensor-parallelism "Fully Sharded Data Parallelism + Tensor Parallelism")

  * [Fully Sharded Data Parallelism + Context Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism--context-parallelism "Fully Sharded Data Parallelism + Context Parallelism")

  * [Hybrid Sharded Data Parallelism + Tensor Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#hybrid-sharded-data-parallelism--tensor-parallelism "Hybrid Sharded Data Parallelism + Tensor Parallelism")

* [Usage notes](https://huggingface.co/blog/accelerate-nd-parallel#usage-notes "Usage notes")

Training large models across multiple GPUs can be challenging due to the complexities of different parallelism strategies. In Accelerate, together with [Axolotl](https://github.com/axolotl-ai-cloud/axolotl/), we have integrated a quick and easy way to use any combination of parallelism strategies in your training script!
Here is how to add it to your training script:

```python
from transformers import AutoModelForCausalLM
from accelerate import Accelerator
from accelerate.parallelism_config import ParallelismConfig
from accelerate.utils import FullyShardedDataParallelPlugin

# configure your desired parallelisms here - this particular configuration requires at least 2 nodes with 8 GPUs each. 
# setting any parallelism degree to 1 disables it i.e. dp_replicate_size=1 disables DP.
pc = ParallelismConfig(
    dp_shard_size=2, # Fully Sharded Data Parallel degree
    dp_replicate_size=2, # Data Parallel degree
    cp_size=2, # Context Parallel degree
    tp_size=2, # Tensor Parallel degree
)

fsdp_plugin = FullyShardedDataParallelPlugin(
    fsdp_version=2,
    auto_wrap_policy="transformer_based_wrap",
    transformer_cls_names_to_wrap=["LlamaDecoderLayer"],
    state_dict_type="SHARDED_STATE_DICT",
)

accelerator = Accelerator(
    parallelism_config=pc,
    fsdp_plugin=fsdp_plugin
)

model = AutoModelForCausalLM.from_pretrained(
    "NousResearch/Hermes-3-Llama-3.1-8B", 
    device_mesh=accelerator.torch_device_mesh
)

model = accelerator.prepare(model)
```

We've also included a more comprehensive end-to-end [training script](https://github.com/huggingface/accelerate/blob/main/examples/torch_native_parallelism/nd_parallel.py) in the Accelerate repo which demonstrates how to setup your dataloader, optimizer, and training loop, and how to save your model after training.

To further streamline fine-tuning models at scale and compose parallelism strategies with a variety of fine-tuning techniques, we've also integrated this technique into Axolotl. To help you get started right away we've tested some [example configs](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/distributed-parallel) which you can modify to suit your needs - try one out with:

```bash
# note: this requires a minimum world size of 16 
axolotl train examples/distributed-parallel/llama-3_1-8b-hsdp-tp.yaml
```

You can also check out the [Axolotl ND-Parallelism docs](https://docs.axolotl.ai/docs/nd_parallelism.html) for more details - adding ND parallel techniques to your existing configs is as simple as adding one or more of the following fields to your Axolotl config file:

```yaml
# Fully Sharded Data Parallel degree (note: also requires the fsdp_config field) 
# see https://docs.axolotl.ai/docs/multi-gpu.html#sec-fsdp for more details
dp_shard_size: 2
# Data Parallel degree
dp_replicate_size: 2
# Context Parallel Degree
context_parallel_size: 2
# Tensor Parallel Degree
tensor_parallel_size: 2
```

We've made it easy to configure the degrees of different parallelism strategies and how they are combined through the [`ParallelismConfig`](https://github.com/huggingface/accelerate/blob/v1.10.0/src/accelerate/parallelism_config.py) class in Accelerate, or through config fields in Axolotl, but how do we know which configuration will work best for our use case? As we scale to training models with tens or even hundreds of billions of parameters, the primary challenge comes from understanding the different parallelism strategies and how they interact to minimise communication overhead across devices. In this post, we'll walk through how the different parallelism strategies work, and when and how you might want to compose them.

[](https://huggingface.co/blog/accelerate-nd-parallel#contents) Contents
------------------------------------------------------------------------

* [Data Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#data-parallelism)
* [Fully Sharded Data Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism)
* [Tensor Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#tensor-parallelism)
* [Context Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#context-parallelism)
* [ND Parallelisms](https://huggingface.co/blog/accelerate-nd-parallel#nd-parallelisms)
  * [Hybrid Sharded Data Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#hybrid-sharded-data-parallelism)
  * [Fully Sharded Data Parallelism + Tensor Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism--tensor-parallelism)
  * [Fully Sharded Data Parallelism + Context Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism--context-parallelism)
  * [Hybrid Sharded Data Parallelism + Tensor Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#hybrid-sharded-data-parallelism--tensor-parallelism)

* [Usage Notes](https://huggingface.co/blog/accelerate-nd-parallel#usage-notes)

[](https://huggingface.co/blog/accelerate-nd-parallel#data-parallelism) Data Parallelism
----------------------------------------------------------------------------------------

![Image 16: Diagram for Data Parallel](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/accelerate-nd-parallel/dp.png)

 Distributed Data Parallel replicates the entire model across each device, and evenly divides the data into sub-batches for each device. (**_Source: [Martynas Šubonis](https://martynassubonis.substack.com/p/tensor-and-fully-sharded-data-parallelism)_**).

Data parallelism (DP) is the most common technique for training models across multiple GPUs, and involves replicating the model, gradients and optimizer states across each device, whilst evenly distributing data batches between GPUs, and synchronising gradients across devices before updating parameters. This can significantly increase throughput compared to single-device training, but requires that your model is able to fit on a single device.

We can control the number of replicas of the model with the `dp_replicate_size` parameter in Accelerate's `ParallelismConfig` or config field in Axolotl. It's worth noting that DP is a _top-most-level_ parallelism strategy, meaning that if we use `dp_replicate_size=2` and we compose it with other parallelism strategies, there would be 2 replicas of the model, each also influenced by the other parallelism strategies. For example, if we use `dp_replicate_size=2` and `tp_size=2`, we would have 2 replicas of the model, each with 2 tensor parallel shards.

> We use the term _shard_ to describe data on a single device which is a partition of a larger piece of data.

[](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism) Fully Sharded Data Parallelism
--------------------------------------------------------------------------------------------------------------------

![Image 17: Diagram for Fully Sharded Data Parallel](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/accelerate-nd-parallel/fsdp.png)

 Fully Sharded Data Parallel evenly divides each of the model's parameters across each device, and, like DDP, evenly divides the data into sub-batches for each device. To complete a forward and backwards pass, FSDP must _gather_ the weights of each parameter before the forwards/backwards pass so that each device obtains a full copy of the parameter. (**_Source: [Martynas Šubonis](https://martynassubonis.substack.com/p/tensor-and-fully-sharded-data-parallelism)_**).

What if our model is too large to fit on a single device? Fully sharded data parallel (FSDP) addresses this issue by sharding (distributing evenly) the model’s weights, gradients, and optimizer states across GPUs (this is inspired by DeepSpeed’s ZeRO-3), whilst each device still receives its portion of the full batch of data. As you may notice from the diagram above, rather than requiring a full copy of the entire model on each device, we only gather the weights for a single layer at a time before the forward pass, after which the weights may be sharded again.

In this way, we trade memory usage for the communication overhead of gathering sharded parameters before each forward and backward pass, and reduce-scatter-ing local gradients. We can control this trade-off in FSDP by tuning the granularity at which parameters are gathered. On one extreme, we can gather and re-shard every layer of our model, which would result in the lowest peak memory usage, but incur the highest communication costs. In practice, a common approach is to gather the weights for an entire transformer decoder block at a time.

Whilst we can make further memory-compute trade-offs and offload model parameters and gradients to the CPU to train larger models, this can be prohibitively slow. Instead, let’s consider how we can effectively utilise even more devices to train larger models whilst maintaining high data throughput.

We use the term _node_ to refer to a single machine which hosts multiple GPUs (up to a maximum of 8), with fast intra-node communication channels using e.g. NVLink between GPUs. When using multiple nodes for training, we rely on relatively slower inter-node communication channels between machines using e.g. Infiniband. We also refer to the total number of devices in the process pool as the world size - e.g. a single node with 8 GPUs represents a world size of 8, and 4 nodes would represent a world size of 32.

When using FSDP across multiple nodes, we treat the entire set of devices across nodes as if we were training on a single node. For example, with 4 nodes containing 8 GPUs each, we perform our sharding across 32 devices, and perform our collective all-reduce and reduce-scatter operations using both inter-and-intra-node communication backends. In this manner, FSDP alone can scale to a substantial number of GPUs with a large global batch size to increase data throughput. However, there comes a point where several challenges arise that may require composing FSDP with other parallelism techniques. We usually try to avoid doing FSDP across more than a full node, as the communication overhead can become too high, we'll talk about how to address this in the section on [Hybrid Sharded Data Parallelism](https://huggingface.co/blog/accelerate-nd-parallel#hybrid-sharded-data-parallelism).

> You can use the `dp_shard_size` parameter in Accelerate's `ParallelismConfig` together with a prepared [`FullyShardedDataParallelPlugin`](https://huggingface.co/docs/accelerate/v1.10.0/en/package_reference/utilities#accelerate.FullyShardedDataParallelPlugin), or set the `dp_shard_size` config field in Axolotl to set the degree of FSDP applied to your model.

[](https://huggingface.co/blog/accelerate-nd-parallel#tensor-parallelism) Tensor Parallelism
--------------------------------------------------------------------------------------------

![Image 18: Diagram for Tensor Parallel](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/accelerate-nd-parallel/tp.png)

 Tensor Parallelism splits large linear layers across devices, typically using column-wise sharding for the first layer and row-wise sharding for the subsequent layer. This approach requires only a single AllReduce communication operation to combine the sharded outputs, minimizing communication overhead while distributing both memory and compute across devices within a node.

Tensor Parallel (TP) is a kind of model parallelism technique, where shards of the model permanently live on separate devices, and in contrast to data parallel techniques, each device receives an identical batch of data. TP works by distributing the computation of linear layers across devices, so each device only computes a portion of the matrix multiplication. This technique works best when there are large linear layers, such as the feed-forward layers in transformer models, which can be split across devices. We can also use TP on each of the query, key, value, and output projections in the attention layers with almost no extra communication cost.

To achieve the best performance, parameters of consecutive layers can be distributed in a specific fashion, minimizing the required communication. When working with pairs of linear layers, we can split the first layer column-wise, and the subsequent layer row-wise, allowing us to compute the output with only a single all-reduce operation to combine the sharded outputs.

Unlike the dynamic sharding behaviour of FSDP, TP creates static memory partitions which result in a constant memory usage reduction scaling with the TP group size. This becomes crucial for massive models where even a single decoder layer is too large to fit into memory during the FSDP all-gather (recall that common practice in FSDP is to gather the weights of an entire decoder layer at a time). However, unlike FSDP which scales relatively linearly across nodes (up to a point - ~512 GPUs on a homogenous cluster, significantly less across lower-bandwidth connections), TP is only effective within the boundaries of a single node. TP requires frequent activation synchronization between devices during computation, as each device computes only a portion of the output, requiring the outputs from other devices to be communicated before continuing the forward pass. Thus, if we wish to utilise TP in a multi-node setup, we must consider composing TP with other parallelism techniques, while keeping TP only within a single node. Due to its large communications overhead, TP is not recommended for PCIe linked GPUs.

> In Accelerate, the TP size is configured through `tp_size` in `ParallelismConfig`, whilst in Axolotl you can use the `tensor_parallel_size` config field.

[](https://huggingface.co/blog/accelerate-nd-parallel#context-parallelism) Context Parallelism
----------------------------------------------------------------------------------------------

Recently, reasoning capabilities in LLMs resulted in sequence lengths skyrocketing as models use more and more tokens to solve complex tasks. To achieve this behaviour through fine-tuning, we need a way to train models on very large sequence lengths - which can sometimes reach up to a million tokens!

Since the attention operation in transformers scales quadratically with context length, this becomes impossible on a single GPU. For example, when fine-tuning a relatively small model such as Mistral-7B (which uses 32 attention heads), if we use a sequence length of 128k a single attention matrix will utilise 128k *128k* 2 bytes *`num_heads=32` = ~32GB* 32 = ~1TB of activations memory! Whilst this example is not realistic when using optimised attention implementations such as FlashAttention, it helps illustrate the growth in memory requirements from increasing the context length.

With context parallelism (CP), we can shard the inputs across the sequence dimension, resulting in each device only processing a chunk of the full context and computing a smaller portion of the full, prohibitively large, attention matrix. To see how this works, recall that the attention computation is described by the equation: Attention(Q,K,V)=softmax(Q K T)V \text{Attention}(Q, K, V) = \text{softmax}(QK^T)V Attention(Q,K,V)=softmax(Q K T)V

Where Q Q Q, K K K, and V V V are the query, key, and value matrices respectively. Each query vector (row, or input embedding) of Q Q Q must compute the attention scores against _every_ key vector of K K K in the entire sequence to correctly apply the softmax normalisation. These attention scores are then weighted with _all_ value vectors in V V V.

The crucial detail here lies in the fact that each row in Q Q Q can compute its attention score independently of one another, but each query vector still requires the full K K K and V V V matrices. In other words, given an input with sequence length $n$, we can expand our above attention equation as:

Attention(Q,K,V)1=softmax(Q 1 K T)V Attention(Q,K,V)2=softmax(Q 2 K T)V⋮Attention(Q,K,V)n=softmax(Q n K T)V \begin{align} \text{Attention}(Q, K, V)_1 &= \text{softmax}(Q_1 K^T) V \\ \text{Attention}(Q, K, V)_2 &= \text{softmax}(Q_2 K^T) V \\ &\vdots \\ \text{Attention}(Q, K, V)_n &= \text{softmax}(Q_n K^T) V \end{align} Attention(Q,K,V)1​Attention(Q,K,V)2​Attention(Q,K,V)n​​=softmax(Q 1​K T)V=softmax(Q 2​K T)V⋮=softmax(Q n​K T)V​​

where we denote each row of the query matrix as Q 1,Q 2,...,Q n Q_1, Q_2, ..., Q_n Q 1​,Q 2​,...,Q n​. This can be generalized as: Attention(Q,K,V)i=softmax(Q i K T)V∀i∈{1,2,...,n} \text{Attention}(Q, K, V)_i = \text{softmax}(Q_i K^T) V \quad \forall i \in \{1, 2, ..., n\} Attention(Q,K,V)i​=softmax(Q i​K T)V∀i∈{1,2,...,n}

When we shard the inputs across devices, the resulting Q Q Q, K K K, and V V V matrices (computed from these input shards) are also automatically sharded along the sequence dimension - each GPU computes queries, keys, and values only for its portion of the sequence. For example, with a world size of W W W GPUs and sequence length n n n:

* GPU 0 computes Q 1:n/W Q_{1:n/W} Q 1:n/W​, K 1:n/W K_{1:n/W} K 1:n/W​, V 1:n/W V_{1:n/W} V 1:n/W​
* GPU 1 computes Q n/W+1:2 n/W Q_{n/W+1:2n/W} Q n/W+1:2 n/W​, K n/W+1:2 n/W K_{n/W+1:2n/W} K n/W+1:2 n/W​, V n/W+1:2 n/W V_{n/W+1:2n/W} V n/W+1:2 n/W​
* ...
* GPU (W−1) (W-1) (W−1) computes Q(W−1)n/W+1:n Q_{(W-1)n/W+1:n} Q(W−1)n/W+1:n​, K(W−1)n/W+1:n K_{(W-1)n/W+1:n} K(W−1)n/W+1:n​, V(W−1)n/W+1:n V_{(W-1)n/W+1:n} V(W−1)n/W+1:n​

How do we ensure the attention is computed correctly? As established above, each device only needs its own shard of Q Q Q, but requires the full K K K and V V V matrices to compute the attention correctly. We can achieve this by using a technique called [RingAttention](https://openreview.net/forum?id=WsRHpHH4s0), which works as follows:

1. Initially, each GPU holds its shard of Q Q Q, K K K, V V V (e.g., GPU 0 holds Q 1:n/W Q_{1:n/W} Q 1:n/W​, K 1:n/W K_{1:n/W} K 1:n/W​, V 1:n/W V_{1:n/W} V 1:n/W​).
2. Each GPU then computes a partial attention matrix A i,j A_{i,j} A i,j​ for its shard of Q i Q_i Q i​ and its local shard of K j K_j K j​, V j V_j V j​.
3. Each GPU sends its shard of K K K, V V V to the next GPU in the ring.
4. Each GPU receives a different shard of K K K, V V V from the previous GPU in the ring.
5. Each GPU computes additional partial attention matrices A i,j+1 A_{i,j+1} A i,j+1​, A i,j+2 A_{i,j+2} A i,j+2​, etc. using the received K K K, V V V shards.
6. Each GPU repeats this process until all shards of K K K, V V V have been received and all partial attention matrices A i,∗ A_{i,*} A i,∗​ have been computed.

![Image 19: Diagram for Context Parallel](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/accelerate-nd-parallel/cp.png)

 Context Parallelism shards the input sequence across GPUs, with each device holding queries and key-value pairs for its assigned segment. Ring-attention circulates K,V shards between GPUs (shown by the arrows), allowing each query to compute attention scores against keys and values from the entire sequence. The final attention output combines information from all sequence positions while distributing memory and compute across devices.

Accelerate enables this with the [`accelerator.maybe_context_parallel`](https://huggingface.co/docs/accelerate/v1.10.0/en/package_reference/accelerator#accelerate.Accelerator.maybe_context_parallel) decorator, which is also showcased in the Accelerate [example script](https://github.com/huggingface/accelerate/blob/main/examples/torch_native_parallelism/nd_parallel.py). You can also learn more about how it works and its limitations in our [CP concept guide](https://huggingface.co/docs/accelerate/main/en/concept_guides/context_parallelism).

> Similar to TP, in Accelerate the CP size is configured through `cp_size` in `ParallelismConfig`, whilst in Axolotl you can use the `context_parallel_size` config field.

[](https://huggingface.co/blog/accelerate-nd-parallel#nd-parallelisms) ND Parallelisms
--------------------------------------------------------------------------------------

In the multi-node setting, data parallel techniques such as FSDP treat the entire network topology as if it existed along a single dimension. You may find this approach limiting for a variety of reasons:

* When scaling to more nodes, FSDP's collective operations become bottlenecked by inter-node latency, making training prohibitively slow.
* As we mentioned above, massive models may have decoder layers which cannot fit into GPU memory, or which may be too large to perform a forward pass with, even in a sharded state.
* It could be impossible to achieve your ideal batch size - either the batch becomes too large for pure data parallelism to handle efficiently, or too small due to memory constraints from model size.

To try and address some of these problems, we can think of multi-node clusters as having a two-dimensional topology: fast intra-node communication between devices along one axis, and relatively slower inter-node communication along another axis. Let’s consider how we can compose the parallelism techniques we’ve introduced so far to take advantage of this.

### [](https://huggingface.co/blog/accelerate-nd-parallel#hybrid-sharded-data-parallelism) Hybrid Sharded Data Parallelism

![Image 20: Diagram for Hybrid Sharded Data Parallel](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/accelerate-nd-parallel/hsdp.png)

 Hybrid Sharded Data Parallelism performs FSDP within each replica group and synchronizes gradients across replica groups via AllReduce, combining the memory efficiency of FSDP with the communication efficiency of DP across nodes.

Hybrid Sharded Data Parallelism (HSDP) is a kind of 2D parallelism which performs FSDP within a node, and DP across nodes - that is to say the model is replicated across each node, and sharded using FSDP within each node. This allows the greater communication overhead of FSDP to utilize the faster intra-node links, whilst DP minimises the slower inter-node communication overhead to a single gradient synchronisation step. You might consider this approach if you were facing problem 1 and wished to speed up training at the cost of increased memory usage.

It’s important to note that we can freely configure the shape of our 2D network topology, as we aren’t constrained to the dimensions being aligned with physical node boundaries - you might apply FSDP across 2 nodes whilst replicating across groups of 2 nodes, which would result in lower memory usage but slower throughput, but still reduce the intra-node FSDP communication overhead by a factor of two. This is a knob we encourage you to tune to your specific hardware setup and fine-tuning needs.

> You can enable HSDP by defining both `dp_shard_size` and `dp_replicate_size` in Accelerate's `ParallelismConfig` or through Axolotl's config fields.

### [](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism--tensor-parallelism) Fully Sharded Data Parallelism + Tensor Parallelism

As we mentioned earlier, TP should be applied within a node to utilize the high-bandwidth intra-node communications, thus, combining TP and FSDP involves sharding the model across nodes using FSDP, and within a node using TP. To a certain degree, this potentially offers a neat solution to all three of the issues above: the latency costs from FSDP could be reduced by a factor of 8, layers that are too large to fit on a single device are now evenly distributed across devices, and since each TP group receives an identical batch of data, we can also reduce our global batch size by a factor of 8. However, if this remains insufficient, we are unable to increase the TP size across nodes and must consider an alternative approach.

> In Accelerate you can combine TP and FSDP by defining both `dp_shard_size` and `tp_size` in `ParallelismConfig`, whilst in Axolotl you can add both of the `dp_shard_size` and `tensor_parallel_size` config fields.

### [](https://huggingface.co/blog/accelerate-nd-parallel#fully-sharded-data-parallelism--context-parallelism) Fully Sharded Data Parallelism + Context Parallelism

This is a 2D parallelism strategy that combines FSDP and CP, and while this is not very commonly used as CP already combines with FSDP (more on why in the [accelerate concept guide](https://huggingface.co/docs/accelerate/main/en/concept_guides/context_parallelism)), it can be useful in some cases i.e. when requiring a large sequence length, consequently requiring a large `cp_size`. If this still doesn't fit into your memory budget, you can apply FSDP on top of this, further reducing the memory usage.

> In Accelerate you can combine CP and FSDP by defining both `dp_shard_size` and `cp_size` in `ParallelismConfig`, whilst in Axolotl you can add both of the `dp_shard_size` and `context_parallel_size` config fields.

### [](https://huggingface.co/blog/accelerate-nd-parallel#hybrid-sharded-data-parallelism--tensor-parallelism) Hybrid Sharded Data Parallelism + Tensor Parallelism

With a sufficiently large world size (note: while the minimum world size for 3D parallelism is 8, it is most effective at much larger scales), we can consider combining HSDP with TP which creates a hierarchy where DP first replicates the model across groups of nodes, FSDP then shards the model within each group, and TP splits individual layers within each node. You might consider this approach when facing all of the scaling constraints we mentioned above, as it provides the most flexibility to adapt to your specific training setup by making trade-offs between memory usage and throughput.

> In Accelerate you can combine HSDP and TP by defining all of `dp_shard_size`, `dp_replicate_size`, and `tp_size` in `ParallelismConfig`. Similarly in Axolotl you can add all of the `dp_shard_size`, `dp_replicate_size`, and `tensor_parallel_size` config fields.

[](https://huggingface.co/blog/accelerate-nd-parallel#usage-notes) Usage notes
------------------------------------------------------------------------------

There are additional ways to combine multiple parallelisms which we haven't covered, such as 4D parallel using HSDP + TP + CP, but they operate very similarly to the techniques we've already covered. Most of all, we encourage you to play with different techniques and configurations - this is the best way to gain an intuition for the different ways in which you can make memory/throughput trade-offs.

Below are some additional tips you may find useful when working in distributed settings:

* When using FSDP and working with models that are too large to fit in a single device, enabling both CPU RAM efficient loading and sharded state dict checkpointing technique is crucial. You can enable this through the `cpu_ram_efficient_loading` and `state_dict_type` parameters in Accelerate's [`FullyShardedDataParallelPlugin`](https://huggingface.co/docs/accelerate/v1.10.0/en/package_reference/utilities#accelerate.FullyShardedDataParallelPlugin),

```python
fsdp2_plugin = FullyShardedDataParallelPlugin(
    fsdp_version=2,
    auto_wrap_policy="transformer_based_wrap",
    transformer_cls_names_to_wrap=["LlamaDecoderLayer"],
    state_dict_type="SHARDED_STATE_DICT", 
    cpu_ram_efficient_loading=True
)
```

or through the `cpu_ram_efficient_loading` and `state_dict_type` config fields inside the `fsdp_config` in Axolotl:

```yaml
fsdp_version: 2
fsdp_config:
  auto_wrap_policy: TRANSFORMER_BASED_WRAP
  transformer_layer_cls_to_wrap: LlamaDecoderLayer
  state_dict_type: SHARDED_STATE_DICT
  cpu_ram_efficient_loading: True
```

* The total batch size used during training plays an important factor in training stability, memory usage, and data throughput. When using DP and/or FSDP the effective batch size is calculated as:

`effective_batch_size = micro_batch_size * gradient_accumulation_steps * dp_world_size`.

where `dp_world_size = (dp_shard_size * dp_replicate_size) / tp_size`. You can increase your batch size by increasing your total micro batch size or gradient accumulation steps in your training loop, or setting the `micro_batch_size` and `gradient_accumulation_steps` config fields in Axolotl, or increasing the total `dp_world_size` by adding more GPUs. As we mentioned above, this imposes a _minimum_ total batch size of `dp_world_size` - when using pure DP/FSDP, this will be your total world size, and if this is too high the only way to decrease the total batch size is by introducing tensor parallelism. Finally, with a fixed number of GPUs and in memory-constrained scenarios, we recommend increasing `gradient_accumulation_steps` instead of `micro_batch_size` to achieve larger effective batch sizes, and vice-versa.

* Correspondingly, when your effective batch size increases due to introducing data parallelism, you should scale your learning rate to maintain training stability. Common approaches include linear scaling `scaled_lr = base_lr * (effective_batch_size / base_batch_size)` or square root scaling `scaled_lr = base_lr * sqrt(effective_batch_size / base_batch_size)`.

* When memory constraints persist even with parallelism strategies, gradient checkpointing can provide additional memory savings by trading compute for memory. During the forward pass, only a subset of activations are kept in memory (typically at transformer block boundaries), and intermediate activations are recomputed during the backward pass. This technique works seamlessly with all parallelism strategies covered above. In Accelerate, you can enable it by setting `activation_checkpointing=true` in `FullyShardedDataParallelPlugin`:

```python
fsdp2_plugin = FullyShardedDataParallelPlugin(
    fsdp_version=2,
    auto_wrap_policy="transformer_based_wrap",
    transformer_cls_names_to_wrap=["LlamaDecoderLayer"],
    state_dict_type="SHARDED_STATE_DICT", 
    cpu_ram_efficient_loading=True,
    activation_checkpointing=True
)
```

and similarly in Axolotl:

```yaml
fsdp_version: 2
fsdp_config:
  auto_wrap_policy: TRANSFORMER_BASED_WRAP
  transformer_layer_cls_to_wrap: LlamaDecoderLayer
  state_dict_type: SHARDED_STATE_DICT
  cpu_ram_efficient_loading: True
  activation_checkpointing: True
```

Note that gradient checkpointing typically increases training time by ~20-30% due to activation recomputation, but can reduce activation memory by 60-80%, making it particularly valuable when training very large models or using long sequence lengths.

More Articles from our Blog

[![Image 21](https://huggingface.co/blog/assets/ulysses/thumbnail.png) guide distributed-training accelerate Ulysses Sequence Parallelism: Training with Million-Token Contexts ------------------------------------------------------------------ * ![Image 22](https://cdn-avatars.huggingface.co/v1/production/uploads/1669189789447-629f3b18ee05727ce328ccbe.jpeg) * ![Image 23](https://cdn-avatars.huggingface.co/v1/production/uploads/1594311341799-5f07383b19cb630495b812cd.jpeg) 5 March 9, 2026](https://huggingface.co/blog/ulysses-sp)

[![Image 24](https://huggingface.co/blog/assets/intel-qwen3-agent/smolagents-1300-650.png) llm intel nlp Accelerating Qwen3-8B Agent on Intel® Core™ Ultra with Depth-Pruned Draft Models -------------------------------------------------------------------------------- * ![Image 25](https://huggingface.co/avatars/a09cbec3bcd29b5093ce30b3c47e27f6.svg) * ![Image 26](https://cdn-avatars.huggingface.co/v1/production/uploads/1616423186722-5f8907c65d083370c711f284.jpeg) * ![Image 27](https://huggingface.co/avatars/bd13e3c006573db51fcdf74b016d1aa3.svg) * ![Image 28](https://huggingface.co/avatars/06df4ead5a2014480c128103b9862f98.svg) * +1 24 September 29, 2025](https://huggingface.co/blog/intel-qwen3-agent)

### Community

![Image 29](https://huggingface.co/avatars/d0a9a39f4cf4ec392600c58393d169fb.svg)

[cynricfu](https://huggingface.co/cynricfu)

[Aug 12, 2025](https://huggingface.co/blog/accelerate-nd-parallel#689aa8096040093e9947cae1)

•

[edited Aug 12, 2025](https://huggingface.co/blog/accelerate-nd-parallel#689aa8096040093e9947cae1 "Edited by cynricfu")

May I ask why is `dp_world_size` realted to `tp_size`?

Based on my understanding, it should be just `dp_world_size = dp_shard_size * dp_replicate_size`. Or am I missing some points here?

* [![Image 30](https://cdn-avatars.huggingface.co/v1/production/uploads/658f19cfa02954c982f540eb/qN2eqJZnWQ2H1xlGYeAKj.jpeg)](https://huggingface.co/siro1 "siro1")
* [![Image 31](https://cdn-avatars.huggingface.co/v1/production/uploads/6360cc93a46f0cdd62e1f687/PNLw1QrH45HnzWaU_khix.jpeg)](https://huggingface.co/flymin "flymin")
* 5 replies

·

![Image 32](https://cdn-avatars.huggingface.co/v1/production/uploads/658f19cfa02954c982f540eb/qN2eqJZnWQ2H1xlGYeAKj.jpeg)

[siro1](https://huggingface.co/siro1)

Article author[Aug 14, 2025](https://huggingface.co/blog/accelerate-nd-parallel#689d287e706bebc050b2e192)

•

[edited Aug 14, 2025](https://huggingface.co/blog/accelerate-nd-parallel#689d287e706bebc050b2e192 "Edited by siro1")

> May I ask why is `dp_world_size` realted to `tp_size`?
>
>
> Based on my understanding, it should be just `dp_world_size = dp_shard_size * dp_replicate_size`. Or am I missing some points here?

Correct, I think we had a previous version where it was `dp_world_size = world_size / tp_size`, which we then changed to this version and forgot to remove the denominator. Will push a fix 🤗

 Expand 4 replies

![Image 33](https://huggingface.co/avatars/dc165cba58aa1e8a915ce5bdeec54909.svg)

[npuichigo](https://huggingface.co/npuichigo)

[Aug 16, 2025](https://huggingface.co/blog/accelerate-nd-parallel#68a019f9b71dd5645d5a7cfb)

How to use accelerate config with this feature？

* [![Image 34](https://cdn-avatars.huggingface.co/v1/production/uploads/658f19cfa02954c982f540eb/qN2eqJZnWQ2H1xlGYeAKj.jpeg)](https://huggingface.co/siro1 "siro1")
* 1 reply

·

![Image 35](https://cdn-avatars.huggingface.co/v1/production/uploads/658f19cfa02954c982f540eb/qN2eqJZnWQ2H1xlGYeAKj.jpeg)

[siro1](https://huggingface.co/siro1)

Article author[Aug 16, 2025](https://huggingface.co/blog/accelerate-nd-parallel#68a0f4c364637e64a5d6743d)

Hi, currently it's only available if you use fsdp2 too, as the composability without fsdp2 is limited (will change in next release). You can use `accelerate config` in the command line to specify it.

![Image 36](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/6DTmh7MOemA6xYMWGY9Ce.jpeg)

[Sierkinhane](https://huggingface.co/Sierkinhane)

[Sep 18, 2025](https://huggingface.co/blog/accelerate-nd-parallel#68cb7834936258ed60ca5105)

•

[edited Sep 18, 2025](https://huggingface.co/blog/accelerate-nd-parallel#68cb7834936258ed60ca5105 "Edited by Sierkinhane")

Does this pipeline work for a custom model?

* [![Image 37](https://cdn-avatars.huggingface.co/v1/production/uploads/658f19cfa02954c982f540eb/qN2eqJZnWQ2H1xlGYeAKj.jpeg)](https://huggingface.co/siro1 "siro1")
* [![Image 38](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/6DTmh7MOemA6xYMWGY9Ce.jpeg)](https://huggingface.co/Sierkinhane "Sierkinhane")
* 2 replies

·

![Image 39](https://cdn-avatars.huggingface.co/v1/production/uploads/658f19cfa02954c982f540eb/qN2eqJZnWQ2H1xlGYeAKj.jpeg)

[siro1](https://huggingface.co/siro1)

Article author[Sep 21, 2025](https://huggingface.co/blog/accelerate-nd-parallel#68d06efded0555e8b73e48ad)

Hello, the pipeline works for custom models, IF you implement tensor parallelism yourself. This change is sadly model architecture aware, so we can't possibly do this instead of you.

 Expand 1 reply

![Image 40](https://huggingface.co/avatars/2d3760a0ab378c7ce9769a8fa0614b55.svg)

[chewkokwah](https://huggingface.co/chewkokwah)

[Oct 24, 2025](https://huggingface.co/blog/accelerate-nd-parallel#68fb9d90643c4e88e54a6c8d)

•

[edited Oct 24, 2025](https://huggingface.co/blog/accelerate-nd-parallel#68fb9d90643c4e88e54a6c8d "Edited by chewkokwah")

What is the different between FSDP vs Deepspeed Zero 3? Is it save to say FSDP is better than Zero 3 in term of speed and memory saving?

Reply

Edit Preview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

 Comment
·[Sign up](https://huggingface.co/join?next=%2Fblog%2Faccelerate-nd-parallel) or [log in](https://huggingface.co/login?next=%2Fblog%2Faccelerate-nd-parallel) to comment

[- [x] Upvote 93](https://huggingface.co/login?next=%2Fblog%2Faccelerate-nd-parallel)

* [![Image 41](https://cdn-avatars.huggingface.co/v1/production/uploads/1594651707950-noauth.jpeg)](https://huggingface.co/lewtun "lewtun")
* [![Image 42](https://huggingface.co/avatars/46e4669ef1b08e449fd46bec60eb66e8.svg)](https://huggingface.co/0xe69756 "0xe69756")
* [![Image 43](https://huggingface.co/avatars/2d3760a0ab378c7ce9769a8fa0614b55.svg)](https://huggingface.co/chewkokwah "chewkokwah")
* [![Image 44](https://cdn-avatars.huggingface.co/v1/production/uploads/5fd5e18a90b6dc4633f6d292/gZXHW5dd9R86AV9LMZ--y.png)](https://huggingface.co/MaziyarPanahi "MaziyarPanahi")
* [![Image 45](https://cdn-avatars.huggingface.co/v1/production/uploads/600a8fbd1dcb38f00c1ccb0a/BBnD0KtX9-MVBVHMQYqzA.jpeg)](https://huggingface.co/dev7halo "dev7halo")
* [![Image 46](https://huggingface.co/avatars/bfcfd7c222e2cea4f02d314c35734150.svg)](https://huggingface.co/Pratik "Pratik")
* [![Image 47](https://cdn-avatars.huggingface.co/v1/production/uploads/6033c55f60e3dd96631c908d/jy7cHHCBhnlzHKGbXIbj0.jpeg)](https://huggingface.co/theainerd "theainerd")
* [![Image 48](https://cdn-avatars.huggingface.co/v1/production/uploads/1617264212503-603d25b75f9d390ab190b777.jpeg)](https://huggingface.co/pcuenq "pcuenq")
* [![Image 49](https://cdn-avatars.huggingface.co/v1/production/uploads/604643c112ce0713cb6394e8/XZ26qD7V0ec-qkholq_mP.png)](https://huggingface.co/dmaniss "dmaniss")
* [![Image 50](https://huggingface.co/avatars/80e890c0c0b3c3e2b89d0bb555d2c658.svg)](https://huggingface.co/dim "dim")
* [![Image 51](https://huggingface.co/avatars/25ab2549a0a846f06cf0936924769c15.svg)](https://huggingface.co/Ajax0564 "Ajax0564")
* [![Image 52](https://cdn-avatars.huggingface.co/v1/production/uploads/608aabf24955d2bfc3cd99c6/-YxmtpzEmf3NKOTktODRP.jpeg)](https://huggingface.co/ariG23498 "ariG23498")
* +81

 System theme

Company

[TOS](https://huggingface.co/terms-of-service)[Privacy](https://huggingface.co/privacy)[About](https://huggingface.co/huggingface)[Careers](https://apply.workable.com/huggingface/)[](https://huggingface.co/)

Website

[Models](https://huggingface.co/models)[Datasets](https://huggingface.co/datasets)[Spaces](https://huggingface.co/spaces)[Pricing](https://huggingface.co/pricing)[Docs](https://huggingface.co/docs)
