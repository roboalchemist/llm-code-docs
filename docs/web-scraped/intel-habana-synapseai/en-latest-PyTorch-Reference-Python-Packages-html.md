# Source: https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html

Title: Intel Gaudi PyTorch Python API (habana_frameworks.torch) — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html

Markdown Content:
Intel Gaudi PyTorch Python API (habana_frameworks.torch)[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#intel-gaudi-pytorch-python-api-habana-frameworks-torch "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This package provides Intel® Gaudi® PyTorch bridge interfaces and modules such as optimizers, mixed precision configuration, fused kernels for training on Gaudi.

The various modules are organized as listed in the below example:

habana_frameworks.torch
  core
  distributed
     hccl
  gpu_migration
  hpex
     kernels
     normalization
     optimizers
  hpu
  utils

The following sections provided a brief description of each module.

PyTorch Autoloading[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#pytorch-autoloading "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------

Starting from Intel Gaudi software version 1.18.0, importing the `habana_frameworks.torch` package including `core`, `hpu`, and `distributed/hccl` modules is enabled using only `import torch` command. As a result, an extra import with `import habana_frameworks.torch`, `import habana_frameworks.torch.core`, `import habana_frameworks.torch.hpu`, and `import habana_frameworks.torch.distributed.hccl` is no longer required.

Example without autoloading:

import torch
import torchvision.models as models
import habana_frameworks.torch # <-- extra import
model = models.resnet50().eval().to(“hpu”)
input = torch.rand(128, 3, 224, 224).to(“hpu”)
output = model(input)

Example with autoloading:

import torch
import torchvision.models as models
model = models.resnet50().eval().to(“hpu”)
input = torch.rand(128, 3, 224, 224).to(“hpu”)
output = model(input)

Note

*   Running models with the extra import is currently possible, but will be deprecated in future releases.

*   Autoloading can be disabled by setting `PT_HPU_AUTOLOAD=0` before running your model script.

*   The feature is not supported in Lazy mode.

*   The environment variables that affect the importing must be set before `import torch`.

core[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#core "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------

`core` module provides Python bindings to Intel Gaudi PyTorch bridge interfaces. For example, `mark_step` which is used to trigger execution of accumulated graphs in Lazy mode.

distributed/hccl[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#distributed-hccl "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------

*   `distributed/hccl` - Registers and adds support for HCCL communication backend.

*   `from habana_frameworks.torch.distributed.hccl import initialize_distributed_hpu` - API imports.

*   `initialize_distributed_hpu()` - Helper function used to return world_size, rank and local_rank if the processes are launched using either MPI or with torchrun related APIs.

You can find a usage code in the [ResNet50 Model References GitHub page](https://github.com/HabanaAI/Model-References/blob/cb8230e63db23694fe067955f12ab4411783fcc6/PyTorch/computer_vision/classification/torchvision/utils.py#L250).

**Example:**

from habana_frameworks.torch.distributed.hccl import initialize_distributed_hpu
world_size, rank, local_rank = initialize_distributed_hpu()

gpu_migration[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#gpu-migration "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------

`gpu_migration` can be utilized to quickly migrate your model that strongly depends on CUDA to HPU. Refer to [GPU Migration Toolkit](https://docs.habana.ai/en/latest/PyTorch/PyTorch_Model_Porting/GPU_Migration_Toolkit/GPU_Migration_Toolkit.html#gpu-migration-toolkit) for further details.

hpex/kernels/CustomSoftmax[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpex-kernels-customsoftmax "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

CustomSoftmax is an optimized version of [torch.nn.Softmax](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html) operator. It only supports bfloat16 input and computes Softmax along the last dimension (`dim=-1`). Additionally, its second argument is `flavor`. The following flavors are available:

*   `flavor=0` - Equivalent to the original `torch.nn.Softmax`.

*   `flavor=1` - Uses fast approximation of exp and reciprocal.

*   `flavor=2` - Does not subtract the maximum and uses fast approximation of exp and reciprocal.

This operator is useful in optimizing performance of inference workloads. For example, [Stable Diffusion](https://github.com/HabanaAI/Model-References/blob/1.23.0/PyTorch/generative_models/stable-diffusion-v-2-1/ldm/modules/attention.py#L196) which uses `flavor=1`.

Some layers can be sensitive to Softmax accuracy and its numerical stability so applying the fastest option (2) for all the layers may harm model output. Therefore, collecting statistics for each layer (min and max of maximums along the last dimensions) can help to find layers suitable for applying this optimization: if min and max are far away from 0 then subtracting the maximum will be required for numerical stability. Also, using `CustomSoftmax` only in selected layers may help with optimizing the model if some layers are very sensitive to Softmax accuracy.

**Example:**

import habana_frameworks.torch.hpex.kernels as hpu_kernels

attn_weights = attn_weights * self.inv_scale_attn
attn_weights = attn_weights + attention_mask
attn_weights = hpu_kernels.CustomSoftmax.apply(attn_weights, 2) # flavor=2

hpex/kernels/FBGEMM[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpex-kernels-fbgemm "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------

FBGEMM (Facebook GEneral Matrix Multiplication Kernels Library) is a collection of high-performance operator libraries designed for training and inference. The `habana_frameworks.torch.hpex.kernels.fbgemm` package provides the following APIs:

*   `bounds_check_indices` - Checks and corrects any invalid values of the provided indices and offsets.

*   `expand_into_jagged_permute` - Expands the permute index for sparse data from the table dimension to the batch dimension in cases where the sparse features have different batch sizes across ranks.

*   `permute_1D_sparse_data` - Shuffles lengths, indices and weights tensors according to the values in permute tensor.

*   `permute_2D_sparse_data` - Shuffles lengths, indices and weights tensors according to the values in permute tensor.

*   `split_embedding_codegen_lookup_function` - A simple lookup table that stores embeddings for a fixed dictionary of a specific size.

*   `split_permute_cat` - Replaces the combination of `split_with_sizes`, permute, and cat operations.

**Example:**

> import torch
> from test_utils import hpu
> from habana_frameworks.torch.hpex.kernels.fbgemm import split_permute_cat
> 
> B = 3; F = 3; D = 8
> input = torch.randn(B, F * D, dtype=torch.float32)
> indices = torch.randperm(F)
> 
> output = split_permute_cat(input.to(hpu), indices.to(hpu), B, F, D)
> print(output.cpu())

hpex/kernels/FusedSDPA[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpex-kernels-fusedsdpa "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------

FusedSDPA is a fused implementation of `torch.nn.functional.scaled_dot_product_attention()` for Gaudi. It maintains the same functionality as the original function with reduced memory usage and implements selected Flash Attention optimization approaches.

The below table presents API parameters of the original `torch.nn.functional.scaled_dot_product_attention()` supported by FusedSDPA as well as custom parameters. For a full description of the custom features, refer to [Using Fused Scaled Dot Product Attention (FusedSDPA)](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Optimization_in_PyTorch_Models.html#using-fused-sdpa).

Note

PyTorch 2.5 introduces a new API parameter, `enable_gqa`, to support the GQA feature. FusedSDPA internally detects whether it is being used in a GQA scenario (based on the query/key shapes) and, if so, automatically supports GQA. Therefore, FusedSDPA does not require this parameter to enable GQA support.

| Parameter | Details |
| --- | --- |
| `query` | Same as the original. |
| `key` | Same as the original. |
| `value` | Same as the original. |
| `attn_mask=None` | Same as the original. In addition, FusedSDPA supports the following: * Shape (N,…,1,S). * Passing user a provided mask via `attn_mask` even when `is_causal=True` in inference. |
| `dropout_p=0.0` | Same as the original. |
| `is_causal=False` | Same as the original. In addition, FusedSDPA supports passing user a provided mask via `attn_mask` even when `is_causal=True` in inference. |
| `scale=None` | Same as the original. |
| `softmax_mode='None'` | Custom parameter. Options: * ‘None’ (default) - Use default Softmax. * ‘fast’ - Use fast Softmax. * ‘fp32’ - Use Softmax in FP32 precision when Q, K, V are in BF16 or FP8. When softmax_mode = ‘None’, when Q, K V are in BF16 or FP8, GEMM output for Q@K.t() is in BF16 and the softmax that follows runs in BF16 or FP8 mode. Some topologies may have accuracy issues with this flow. When setting the softmax mode to ‘fp32’, the GEMM output will be set to FP32 and softmax will run in FP32 precision providing better accuracy. However, this can have impact on perf. This mode is supported only in inference. |
| `recompute_mode=None` | Custom parameter. Options: * None (default) - Mode is read from the context API variable. * False - FusedSDPA runs in non-recompute mode. * True - FusedSDPA runs in recompute mode. > Setting recompute_mode to True or False in a call to FusedSDPA overrides the context manager API variable and any global setting of the mode during the call. > > > > Note > > > Do not use the context manager mechanism to set the operation mode when running workloads in `torch.compile` mode as this causes breaks in the compiled graphs. These breaks occur due to PyTorch’s current handling of context managers in `torch.compile`. Instead, set the `recompute_mode` API variable to True or False to run FusedSDPA in recompute or non-recompute mode respectively. |
| `valid_seq_len=None` | Custom parameter. Options: * None (default) - Valid sequence length is not set. * 1-D, 32 bit integer tensor of size batch-size (N) indicating valid sequence length in a batch. This tensor is supported (not None) only with `is_causal=True`. This feature is supported only in inference. |
| `seq_padding_type="left"` | Custom parameter. Options: * “left” (default) - Sequences are padded on the left. * “right”- Sequences were padded on the right. This parameter is relevant only when `valid_seq_len` is not `None`. |
| `return_dropout_mask=False` | Custom parameter. Options: * False (default) - FusedSDPA does not return dropout mask. * True - FusedSDPA returns dropout mask. > This parameter is used for debug purposes only. Supported only in in no-recompute mode. |
| `return_attn_probs=False` | Custom parameter. Options: * False (default) - FusedSDPA does not return attention probabilities. * True - FusedSDPA returns probabilities. > This parameter is used for returning attention probabilities. (Softmax operation output). Supported only in inference when `query`, `key`, and `value` data type is either FP32 or BF16. |
| `window_size=(-1, -1)` | Custom parameter. Options: * `(wl, wr)` — A tuple specifying the left (`wl`) and right (`wr`) sliding window sizes. * `-1` disables windowing on that side (default: `(-1, -1)`). Query position _i_ attends only to keys in the range `[i - wl, i + wr]` (inclusive). Supported only in inference and only when `softmax_mode` is not FP32. Additional constraints apply when enabling sliding window attention. See [Additional Constraints for Sliding Window and Attention Sink](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#additional-constraints). |
| `sink=None` | Custom parameter. Options: * `None` (default) — Attention sink is disabled. * 1-D tensor of size equal to the number of query heads — sink tensor used for the attention sink feature. Supported only in inference. `sink` dtype should be FP32 when `query`, `key` and `value` data type is FP32 sink dtype should be BF16 when `query`, `key` and `value` data type is BF16 or FP8. Additional constraints apply when enabling attention sink. See [Additional Constraints for Sliding Window and Attention Sink](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#additional-constraints). |

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import FusedSDPA
import habana_frameworks.torch.hpu as ht

query = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
key = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
value = torch.rand(32, 8, 128, 64, dtype=torch.bfloat16, device="hpu")
# No attention mask, dropout = 0.1, is_causal = True and scale = None
# i.e. scale factor =1.0/sqrt(64)
# all other parameters set to defaults.
sdpa_out = FusedSDPA.apply(query, key, value, None, 0.1, True)
print(sdpa_out.to("cpu"))

### Additional Constraints for Sliding Window and Attention Sink[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#additional-constraints-for-sliding-window-and-attention-sink "Permalink to this headline")

The sliding window and attention sink features rely on slicing the sequence-length dimension of the Query, Key, and Value tensors (referred to as **QKVSlicing**). The following constraints must be met for these features to operate correctly. These requirements may change in future releases.

Let:

*   **Nt** - Query sequence length

*   **Ns** - Key/Value sequence length

*   **Br** - Block (slice size) on the Query sequence dimension

*   **Bc** - Block (slice size) on the Key/Value sequence dimension

Block sizes can be configured using environment variables:

PT_HPU_SDPA_BR_FACTOR=Br     # default: 1024
PT_HPU_SDPA_BC_FACTOR=Bc     # default: 1024

#### QKVSlicing Requirements[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#qkvslicing-requirements "Permalink to this headline")

The following conditions apply to all features that depend on QKVSlicing (sliding window, attention sink):

*   **QKVSlicing must be enabled** - It is enabled by default, but can be explicitly enabled with:

> PT_HPU_SDPA_QKV_SLICE_MODE_FWD=1

*   **Sequence length threshold** - QKVSlicing activates only when both `Nt` and `Ns` are greater than or equal to the configured threshold:
By default, QKVSlicing is enabled only when both sequence lengths are exactly `32768`:

PT_HPU_QKV_SLICE_SEQ_LEN_THLD=N 
*   **Sequence length alignment**:

> *   `Nt` must be an integer multiple of `Br`.
> 
>     *   `Ns` must be an integer multiple of `Bc`.
> 
>     *   `Br` must be equal to `Bc`.

#### Sliding Window Constraints[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#sliding-window-constraints "Permalink to this headline")

The following requirements apply when using sliding window attention:

*   **All QKVSlicing requirements must be satisfied** - see [QKVSlicing Requirements](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#qkvslicing-requirements).

*   **Window sizes must align with block sizes** - If the default block size (`1024`) does not divide `wl` or
`wr`, `Br` and `Bc` may be adjusted accordingly, provided all QKVSlicing requirements remain satisfied:

    *   `wl` must be an integer multiple of `Br` (unless `wl` is `0` or `-1`).

    *   `wr` must be an integer multiple of `Bc` (unless `wr` is `0` or `-1`).

*   **In case of causal masking**:

> *   `wr = 0` is functionally equivalent to `is_causal=True`.
> 
>     *   Prefer using `is_causal=True` rather than setting `wr = 0`.

#### Attention Sink Constraints[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#attention-sink-constraints "Permalink to this headline")

The attention sink feature has the following requirements: 1 - **All QKVSlicing requirements must be satisfied** - see [QKVSlicing Requirements](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#qkvslicing-requirements).

*   **Mixed topologies** - If some layers use only the sink feature while others use both sink and sliding window, the stricter **sliding window constraints** should be applied across the entire model.

hpex/kernels/RotaryPosEmbeddingHelper[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpex-kernels-rotaryposembeddinghelper "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`hpex/kernels/RotaryPosEmbeddingHelper` module implements Rotary Positional Embeddings (RoPE).

`apply_rotary_pos_emb` - Calculates the rotary positional embedding of each token in the input sequence.

| Parameter | Details |
| --- | --- |
| `p` | Input tensor. |
| `cos or rope_cache` | Cosine input tensor or cos and sin combined together. |
| `sin` | Sine input tensor. |
| `position_ids` | Indices of positions of each input sequence tokens in the position embeddings. |
| `offset` | Offset value defining from where to start loading the cos & sin values. Content is relevant only for mode BLOCKWISE. |
| `mode` | Indicates RoPE mode (BLOCKWISE or PAIRWISE), default BLOCKWISE. |

For mode BLOCKWISE calculates the output according to the following formula:

# Switches between the first half of the input tensor in the last dim,
# with the second half, while negating the second half.
def rotate_half(x):
    x1 = x[..., : x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2 :]
    return torch.cat((-x2, x1), dim=-1)

def apply_rotary_pos_emb(p, cos, sin, offset):
    cos = cos[..., offset : p.shape[0] + offset]
    sin = sin[..., offset : p.shape[0] + offset]
    return (p * cos) + (rotate_half(p) * sin)

For mode PAIRWISE calculates the output according to the following formula:

def rotate_every_two(x):
    x1 = x[:, :, :, ::2]
    x2 = x[:, :, :, 1::2]
    x = torch.stack((-x2, x1), dim=-1)
    return x.flatten(-2)  # in einsum notation: rearrange(x, '... d j -> ... (d j)')

def apply_rotary_pos_emb_gptj_ref(data_tensor, cos, sin):
    return (data_tensor * cos) + (rotate_every_two(data_tensor) * sin)

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import apply_rotary_pos_emb

device = "hpu"
dtype = torch.bfloat16

# Prepare input data
p = torch.rand((32, 1, 16, 64), dtype=dtype, device=device)
cos = torch.rand((1, 1, 32), dtype=dtype, device=device)
sin = torch.rand((1, 1, 32), dtype=dtype, device=device)

output_size = 2 * sin.shape[2]
sin = torch.repeat_interleave(sin, 2, dim=2, output_size=output_size).unsqueeze(2)
cos = torch.repeat_interleave(cos, 2, dim=2, output_size=output_size).unsqueeze(2)

output = apply_rotary_pos_emb(p, cos, sin, None, 0, RotaryPosEmbeddingMode.PAIRWISE)
print(output.cpu())

The module also provides classes with custom autograd functions by subclassing torch.autograd.Function and implementing the forward and backward passes which operate on tensors.

*   `RotaryPosEmbeddingHelperV1` - Based on apply_rotary_pos_emb() function from the GPT-NeoX model in Transformer version 4.27.4 or lower. Used, for example, in the LLaMA model.

*   `RotaryPosEmbeddingHelperV2` - Based on apply_rotary_pos_emb() function from Transformer version greater than 4.27.4. Used, for example, in the StableLM model.

*   `RotaryPosEmbeddingHelperV3` - Based on apply_rotary_pos_emb() function from ChatGLM model.

**Example:**

import torch
from habana_frameworks.torch.hpex.kernels import RotaryPosEmbeddingHelperV3

device = "hpu"
dtype = torch.bfloat16

# Prepare input data
p = torch.rand((2, 4, 2, 8), dtype=dtype, requires_grad=True, device=device)
cos = torch.rand((1, 2, 4), dtype=dtype, device=device)
sin = torch.rand((1, 2, 4), dtype=dtype, device=device)
rope_cache = torch.stack((cos, sin), dim=-1).to(device)

p_embed = RotaryPosEmbeddingHelperV3.apply(p, rope_cache)
loss = p_embed.sum()
loss.backward()

print(p.grad.to(cpu))

hpex/normalization[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpex-normalization "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------

`hpex/normalization` module contains Python interfaces to the Gaudi implementation for common normalize & clip operations performed on gradients in some models. Usage of Gaudi provided implementation can provide better performance (compared to equivalent operator provided in torch). Refer to [Custom Ops](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#pytorch-normalizations) for further details.

hpex/optimizers[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpex-optimizers "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------

`hpex/optimizers` contains Python interfaces to Gaudi implementation for some of the common optimizers used in DL models. Usage of Gaudi implementation can provide better performance (compared to corresponding optimizer implementations available in torch). Refer to [Fused Optimizers](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Custom_Ops_PyTorch.html#pytorch-optimizers) for further details.

hpex/experimental/transformer_engine[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpex-experimental-transformer-engine "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`hpex/experimental/transformer_engine` contains Python interfaces to Intel Gaudi Transformer Engine (TE) implementation. Intel Gaudi Transformer Engine provides optimized implementations of PyTorch modules for popular Transformer architectures that perform the computations in 8bit floating point data type (FP8). Usage of TE and the FP8 data type can provide better performance with lower memory utilization. Refer to [FP8 Training with Intel Gaudi Transformer Engine](https://docs.habana.ai/en/latest/PyTorch/PyTorch_FP8_Training/index.html#pytorch-fp8-training) for further details.

hpu APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpu-apis "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------

Support for HPU tensors is provided with this package. The following APIs provide the same functionality as CPU tensors but HPU is used for the underlying implementation. This package can be imported on demand.

*   `import habana_frameworks.torch.hpu as hthpu` - Imports the package.

*   `hthpu.is_available()` - Returns a boolean indicating if a HPU device is currently available.

*   `hthpu.device_count()` - Returns the number of compute-capable devices.

*   `hthpu.get_device_name()` - Returns the name of the HPU device.

*   `hthpu.current_device()` - Returns the index of the current selected HPU device.

*   `torch.hpu.can_device_access_peer(device, peer_device)` - Returns a boolean indicating whether peer access is possible between two HPU devices.

*   `torch.hpu.get_arch_list()` - Returns a list of HPU architectures this library was compiled for.

*   `torch.hpu.get_device_capability(device)` - Returns the (major, minor) capability of the specified HPU device.

*   `torch.hpu.get_device_name(device)` - Returns the name of the specified HPU device.

*   `torch.hpu.get_device_properties(device)` - Returns the properties of the specified HPU device as a structured object.

*   `torch.hpu.get_gencode_flags()` - Returns the HPU gencode flags used during library compilation.

*   `torch.hpu.get_sync_debug_mode()` - Returns the current debug mode setting for HPU synchronization operations.

*   `torch.hpu.utilization(device)` - Returns the percentage of time the device was actively executing kernels during the last sample period.

*   `torch.hpu.synchronize(device)` - Blocks until all kernels on all streams of the specified HPU device have completed.

utils[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#utils "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------

`utils` module contains general Python utilities required for training on HPU.

Memory Stats APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#memory-stats-apis "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------

*   `htorch.hpu.max_memory_allocated` - Returns peak HPU memory allocated by tensors (in bytes). `reset_peak_memory_stats()` can be used to reset the starting point in tracing stats.

*   `htorch.hpu.memory_allocated` - Returns the current HPU memory occupied by tensors.

*   `htorch.hpu.memory_stats` - Returns list of HPU memory stats. The below summarizes the sample memory stats printout and details:

> *   Limit - Amount of total memory on HPU device
> 
>     *   InUse - Amount of allocated memory at any instance. Starting point after reset_peak_memory_stats()
> 
>     *   MaxInUse - Amount of total active memory allocated
> 
>     *   NumAllocs - Number of allocations
> 
>     *   NumFrees - Number of freed chunks
> 
>     *   ActiveAllocs - Number of active allocations
> 
>     *   MaxAllocSize - Maximum allocated size
> 
>     *   TotalSystemAllocs - Total number of system allocations
> 
>     *   TotalSystemFrees - Total number of system frees
> 
>     *   TotalActiveAllocs - Total number of active allocations

*   `htorch.hpu.memory_summary` - Returns human readable printout of current memory stats.

*   `htorch.hpu.reset_accumulated_memory_stats` - Resets accumulated memory stats tracked by the memory allocator.

*   `htorch.hpu.reset_peak_memory_stats` - Resets starting point of memory occupied by tensors.

*   `torch.hpu.memory_usage(device)` - Returns the percentage of time during which global memory was being accessed on the specified HPU device.

*   `torch.hpu.max_memory_reserved(device)` - Returns the maximum memory (in bytes) managed by the allocator for the specified HPU device since the last reset.

*   `torch.hpu.memory_reserved(device)` - Returns the current memory (in bytes) reserved by the allocator for the specified HPU device.

**Example:**

import torch
import habana_frameworks.torch as htorch
device = torch.device("hpu")
import torch.nn as nn
import torch.nn.functional as F

if  __name__  == '__main__':
    hpu = torch.device('hpu')
    cpu = torch.device('cpu')
    input1 = torch.randn((64,28,28,20),dtype=torch.float, requires_grad=True)
    input1_hpu = input1.contiguous(memory_format=torch.channels_last).to(hpu)
    mem_summary1 = htorch.hpu.memory_summary()
    print('memory_summary1:')
    print(mem_summary1)
    htorch.hpu.reset_peak_memory_stats()
    input2 = torch.randn((64,28,28,20),dtype=torch.float, requires_grad=True)
    input2_hpu = input2.contiguous(memory_format=torch.channels_last).to(hpu)
    mem_summary2 = htorch.hpu.memory_summary()
    print('memory_summary2:')
    print(mem_summary2)
    mem_allocated = htorch.hpu.memory_allocated()
    print('memory_allocated: ', mem_allocated)
    mem_stats = htorch.hpu.memory_stats()
    print('memory_stats:')
    print(mem_stats)
    max_mem_allocated = htorch.hpu.max_memory_allocated()
    print('max_memory_allocated: ', max_mem_allocated)

Metric APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#metric-apis "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

The Metric APIs provide various performance-related metrics, such as the number of graph compilations, the total time of graph compilations, and more. The metrics can be retrieved by using Python APIs listed below. You can also obtain metrics by saving them to a file without requiring any changes to the script using the environment variables listed in [Runtime Environment Variables](https://docs.habana.ai/en/latest/PyTorch/Reference/Runtime_Flags.html#pytorch-runtime-flags).

Metric APIs functions are defined in `habana_frameworks.torch.hpu.metrics` module as described below:

*   `habana_frameworks.torch.hpu.metrics.metrics_global` - Returns a global metric object based on the name provided. The object is active and present during the entire execution process.

> **Example:**
> 
> import torch
> from habana_frameworks.torch.hpu.metrics import metric_global
> 
> gc_metric = metric_global("graph_compilation")
> 
> print(gc_metric.stats())
> 
> device = torch.device('hpu')
> do_computation(device)
> 
> print(gc_metric.stats())
> # 'gc_metric.stats' returns the list of counters collected during the entire execution process. Each counter is expressed as a tuple of the counter's name and its value.

*   `habana_frameworks.torch.hpu.metrics.metrics_localcontext` - Returns a context manager object for the requested metric. The metric collection is limited to the scope of the context manager defined within the `with` statement.

> **Example:**
> 
> import torch
> from habana_frameworks.torch.hpu.metrics import metric_localcontext
> with metric_localcontext("graph_compilation") as local_metric:
>     do_computation()
> 
> print(local_metric.stats())
> # 'local_metric.stats' returns only the list of counters reflecting the data collected within the "with" statement. Each counter is expressed as a tuple of the counter's name and its value.

*   `habana_frameworks.torch.hpu.metrics.metrics_dump` - Stores the contents collected by the **global metrics only** in a file. Both JSON and TEXT formats are supported.

> **Example:**
> 
> import torch
> from habana_frameworks.torch.hpu.metrics import metrics_dump
> 
> device = torch.device('hpu')
> do_computation(device)
> 
> metrics_dump("metrics.json", "json")
> # Only global metrics will be saved in 'metric.json' file in JSON format. The local metrics created through 'metric_localcontext' will not be stored.

Below is the list of metrics that are currently supported along with their respective properties:

| Metric | Properties |
| --- | --- |
| `graph_compilation` | * `TotalNumber` - Total number of graph compilations. * `TotalTime` - Total time of graph compilations in microseconds (μs). * `AvgTime` - Average time of graph compilation in microseconds (μs). |
| `cpu_fallback` | * `TotalNumber` - Total number of CPU fallbacks. * `FallbackOps` - Total number of CPU fallbacks for each operator. |
| `memory_defragmentation` | * `TotalNumber` - Total number of memory defragmentations triggered. * `TotalSuccessful` - Total number of memory defragmentations completed successfully. * `AvgTime` - Average time of memory defragmentation (ms). * `MaxTime` - Maximum time of memory defragmentation (ms). |
| `recipe_cache` | * `TotalHit` - Total number of graph recipe cache hits. * `TotalMiss` - Total number of graph recipe cache misses. * `RecipeHit` - Total number of graph recipe cache hits for each recipe. * `RecipeMiss` - Total number of graph recipe cache misses for each recipe. |

Stream APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#stream-apis "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------

Streams and events are advanced features for concurrency that allow users to manage multiple asynchronous tasks running on the HPU:

*   `import habana_frameworks.torch as htorch` - Imports the package.

*   `htorch.hpu.Stream` - Returns a wrapper around a HPU stream.

*   `htorch.hpu.stream` - Wrapper around the Context-manager StreamContext that selects a given stream.

*   `htorch.hpu.set_stream` - Sets the current stream.

*   `htorch.hpu.current_stream` - Gets the current stream.

*   `htorch.hpu.default_stream` - Gets the default stream.

APIs available on Stream object:

*   `query()` - Checks if all the work submitted on a HPU stream has completed.

*   `synchronize()` - Waits for all the kernels in a HPU stream to complete.

*   `record_event()` - Records an event on the HPU stream.

*   `wait_event()` - Makes all future work submitted to the stream wait for an event.

*   `wait_stream()` - All future work submitted to this stream will wait until all kernels submitted to a given stream at the time of call are completed.

**Example:**

import torch
import habana_frameworks.torch.hpu as htcore
import habana_frameworks.torch as ht

s0 = ht.hpu.Stream()
in_shape = (10,2)
tA_h = torch.zeros(in_shape).to('hpu')
tB_h = torch.ones(in_shape).to('hpu')

tOut1 = torch.add(tA_h,tA_h) #executes on default stream

with ht.hpu.stream(s0):
    tOut2 = torch.add(tB_h,tB_h) #executes on stream s0

s0.synchronize() #synchronize with s0
print(s0.query()) #returns True as all operations on s0 have finished

Event APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#event-apis "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------

*   `import habana_frameworks.torch as htorch` - Imports the package.

*   `htorch.hpu.Event` - Returns a wrapper around a HPU event.

APIs available on Event object:

*   `query()` - Checks if all work currently captured by event has completed.

*   `synchronize()` - Waits until the completion of all work currently captured in this event.

*   `record()` - Records the event in a given stream.

*   `wait()` - Makes all future work submitted to the given stream wait for this event.

*   `elapsed_time(end_event)` - Returns the time elapsed in milliseconds after the event was recorded and before the end_event was recorded.

**Example:**

import torch
import habana_frameworks.torch.hpu as htcore
import habana_frameworks.torch as ht

in_shape = (10,2)
tA_h = torch.zeros(in_shape).to('hpu')
tB_h = torch.ones(in_shape).to('hpu')

startEv =ht.hpu.Event(enable_timing=True)
endEv = ht.hpu.Event(enable_timing=True)
startEv.record()
for _ in range(100):
  tA_h = torch.add(tA_h,tB_h)
endEv.record()
endEv.synchronize()
print(f'Time Elapsed={startEv.elapsed_time(endEv)}')

HPU Graph APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpu-graph-apis "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------

### HPU Graph APIs for Inference[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpu-graph-apis-for-inference "Permalink to this headline")

*   `import habana_frameworks.torch as htorch` - Imports the package.

*   `htorch.hpu.HPUGraph` - Returns a wrapper around a HPU Graphs.

*   `htorch.hpu.wrap_in_hpu_graph(module, asynchronous=False, disable_tensor_cache=False, dry_run=False, max_graphs=None, free_inplace=False, verbose=False, log_frequency=100)` - Wraps module forward function with HPU Graphs.

    *   `module` (torch.nn.Module) - The torch.nn.Module object to be cached.

    *   `asynchronous` (bool, optional) - If True, replays for the HPU Graphs will be launched asynchronously. Set this based on the model used. This flag can be used along with stream and async D2H to copy outputs for reducing host overheads. Default: False

    *   `disable_tensor_cache` (bool, optional) - If False, HPU Graphs cache all input, intermediate and output tensors. Setting this to True frees up previously cached input tensors, intermediate tensors except in-place, views and output tensors, thereby reducing the model’s memory requirements. Since the intermediate tensors are freed by enabling this flag, this feature cannot be used in scenarios where intermediate tensors are saved and used outside the scope of the current graph’s forward pass.Using this flag sets `dry_run=True`, so if any print statements are present for non-input tensors in wrapped module, they will print wrong values. Default: False

    *   `dry_run` (bool, optional) - If True, the model’s HPU Graph is cached while avoiding the initial lazy execution. Subsequent replays launch the cached HPU Graphs. This option will be deprecated in a future release. Default: False

    *   `max_graphs` (int, optional) - Specifies the maximum number of HPU graphs that can be cached. Any change in input combinations will lead to the creation of a new graph. Setting this to None indicates no limit, but this may lead to out-of-memory issues if memory requirements are not met. Default: None

    *   `free_inplace` (bool, optional) - Whether to free the inplace tensors after graph replay, used with disable_tensor_cache = True. Default: True

    *   `verbose` (bool, optional) - If set to True, enables verbose mode to print HPUGraph statistics such as total cached graphs, cache hits, and more. Default: False

    *   `log_frequency` (int, optional) - Sets how often HPUGraph statistics are logged. Each call is counted once for the interval. Default: 100

**Example:**

import torch
import habana_frameworks.torch as ht

model = GetModel()
model = ht.hpu.wrap_in_hpu_graph(model) 

*   `htorch.hpu.wrap_in_hpu_graph_func(module, asynchronous=False, disable_tensor_cache=False, dry_run=False, max_graphs=None, free_inplace=False, verbose=False, log_frequency=100)` - Wraps a function with HPU Graphs.

    *   `module` (torch.nn.Module) - The torch.nn.Module object to be cached.

    *   `asynchronous` (bool, optional) - If True, replays for the HPU Graphs will be launched asynchronously. Set this based on the model used. This flag can be used along with stream and async D2H to copy outputs for reducing host overheads. Default: False

    *   `disable_tensor_cache` (bool, optional) - If False, HPU Graphs cache all input, intermediate and output tensors. Setting this to True frees up previously cached input tensors, intermediate tensors except in-place, views and output tensors, thereby reducing the model’s memory requirements. Since the intermediate tensors are freed by enabling this flag, this feature cannot be used in scenarios where intermediate tensors are saved and used outside the scope of the current graph’s forward pass.Using this flag sets `dry_run=True`, so if any print statements are present for non-input tensors in wrapped module, they will print wrong values. Default: False

    *   `dry_run` (bool, optional) - If True, the model’s HPU Graph is cached while avoiding the initial lazy execution. Subsequent replays launch the cached HPU Graphs. This option will be deprecated in a future release. Default: False

    *   `max_graphs` (int, optional) - Specifies the maximum number of HPU graphs that can be cached. Any change in input combinations will lead to the creation of a new graph. Setting this to None indicates no limit, but this may lead to out-of-memory issues if memory requirements are not met. Default: None

    *   `free_inplace` (bool, optional) - Whether to free the inplace tensors after graph replay, used with disable_tensor_cache = True. Default: True

    *   `verbose` (bool, optional) - If set to True, enables verbose mode to print HPUGraph statistics such as total cached graphs, cache hits, and more. Default: False

    *   `log_frequency` (int, optional) - Sets how often HPUGraph statistics are logged. Each call is counted once for the interval. Default: 100

**Example:**

import torch
import habana_frameworks.torch as ht

def func(inp):
    a = torch.full((100,), 1, device="hpu")
    return a @ inp

wrapped_func = ht.hpu.wrap_in_hpu_graph(func)
inp = torch.randn((100,), device="hpu")
wrapped_func(inp) 

APIs available on HPU Graphs object for inference:

*   `capture_begin()` - Begins capturing HPU work on the current stream.

*   `capture_end()` - Ends capturing HPU work on the current stream.

*   `replay()` - Replays the HPU work captured by this graph.

**Example:**

import torch
import habana_frameworks.torch as ht

g = ht.hpu.HPUGraph()
s = ht.hpu.Stream()

with ht.hpu.stream(s):
    g.capture_begin()
    a = torch.full((100,), 1, device="hpu")
    b = a
    b = b + 1
    g.capture_end()

g.replay()
ht.hpu.synchronize() 

### HPU Graph APIs for Training[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpu-graph-apis-for-training "Permalink to this headline")

*   `import habana_frameworks.torch as htorch` - Imports the package.

*   `htorch.hpu.HPUGraph` - Returns a wrapper around a HPU Graphs.

APIs available on HPU Graphs object for training:

*   `make_graphed_callables(callables, sample_args, warmup=0, allow_unused_input=False, asynchronous=False, disable_tensor_cache=False, dry_run=False)` - Makes the training graph. Each graph callable is made to forward and backward pass by overloading the autograd function. This API requires the model to have only tuples for tensors as input and output which is incompatible with workloads using data structures such as dicts and lists. Refer to `ModuleCacher` parameter description below.

**Example:**

> def test_graph_training():
>     N, D_in, H, D_out = 2, 2, 2, 2
>     module = torch.nn.Linear(D_in, H).to('hpu')
>     loss_fn = torch.nn.MSELoss()
>     optimizer = torch.optim.SGD(module.parameters(), lr=0.1)
>     x = torch.randn(N, D_in, device='hpu')
>     module = ht.hpu.make_graphed_callables(module, (x,))
>     real_inputs = [torch.rand_like(x) for _ in range(100)]
>     real_targets= [torch.randn(N, D_out, device="hpu") for _ in range(100)]
> 
>     for data, target in zip(real_inputs, real_targets):
>         optimizer.zero_grad(set_to_none=True)
>         output = module(data)
>         loss = loss_fn(output, target)
>         loss.backward()
>         optimizer.step()

*   `ht.hpu.ModuleCacher(max_graphs=10)(model=model, use_lfu=False, inplace=True, allow_unused_input=False, asynchronous=False, have_grad_accumulation=False, log_frequency=100, verbose=False, disable_tensor_cache=False, dry_run=False)``ModuleCacher` is a wrapper over the `make_graphed_callables` API to simplify caching graphs with static/dynamic input shapes. An object of this class can be called with a `torch.nn.Module` model to return a version of the model which automatically caches a static graph for unique input combinations. When an input combination which was seen before is encountered, the cached version of the model’s graph is used. To check equivalence between two input combinations, a hashed value of the set of input variables is used. To compute the hash, the values are used for all Pythonic variables and only the shape attribute is considered for `torch.Tensor` objects.

> *   `model` (torch.nn.Module) - The `torch.nn.Module` object to be cached.
> 
>     *   `max_graphs` (int, optional) - Specifies the maximum number of HPU Graphs that can be cached. This value indirectly controls the maximum device memory that caching can utilize. The exact memory utilized will depend on the module being cached. If `use_lfu` is not specified, the cache is not updated after reaching the limit. After the cache limit is hit, new shapes will not be cached and will run in Lazy mode. Default: 10
> 
>     *   `use_lfu` (bool, optional) - If True, enables priority based least-frequently-used (LFU) caching. When enabled, the `capture_start` and `capture_end` methods need to be invoked, during which the most frequently occurring input combinations will be identified. Top candidates (up to max_graphs) will be cached the next time it is encountered, and the subsequent runs replay the cached HPU Graphs. The disadvantage with `use_lfu` is that caching begins only after `capture_end` is triggered. When `use_lfu` is disabled, caching starts automatically without any external triggers, but there is no guarantee of optimal caching, since only the first `max_graphs` number of input combinations occupy the cache. This is useful in cases where we have dynamic inputs, so internally during first epoch we calculate stats based on repetition of input shapes. During next epoch, those stats are used to cache specified `max_graphs`. Default: False
> 
> 
> **Example:**
> 
> htorch.hpu.ModuleCacher()(model=model, use_lfu=True, inplace=True)
> for epoch in epochs:
>     if epoch == 0: model.capture_start()
>     ## Training loop
>     if epoch == 0: model.capture_end() 
>     *   `inplace` (bool, optional) - If True, the passed model will be modified in-place to prepare it for caching. Otherwise, a copy of the model is created. Default: True
> 
>     *   `allow_unused_input` (bool, optional) - If False, specifying inputs that are irrelevant for computing outputs (and therefore their grad is always zero) is an error. Setting this to True ignores the inputs that do not contribute to gradient computations, and bypasses the error. Refer to [torch.autograd.grad](https://pytorch.org/docs/stable/generated/torch.autograd.grad.html) for details. Please note that `materialize_grads` is set to the same value as `allow_unused`` Default: False
> 
>     *   `asynchronous` (bool, optional) - If True, replays for the HPU Graphs will be launched asynchronously. Set this based on the model used. This flag can be used along with stream and async D2H to copy outputs for reducing host overheads. It is also useful in use cases where user knows it does not need output immediately after forward call and it can carry on with other tasks and then use streams to see if output is ready, when it is actually needed. Some checks such as input data asserts are in place to detect anomalies, but these may not be exhaustive checks. User is advised to check asynchronous use cases and revert this value to False, in case of any numerical issues with result. Default: False
> 
>     *   `have_grad_accumulation` (bool, optional) - Specifies whether the training employs gradient accumulation to have separate HPU Graphs for first and rest of the iterations. If `have_grad_accumulation` is set to True, it is expected that the user will call `model.set_iteration_count(int)` for the models, to identify if the forward pass was called just after setting gradients to zero. Enable this option when the model necessitates distinct graphs for forward passes that immediately follows a `zero_grad`. Candidate model configuration has gradient accumulation steps greater than 1. Default: False
> 
>     *   `log_frequency` (int, optional) - Specifies the logging frequency of `ModuleCacher` stats in terms of steps per log. Default: 100
> 
>     *   `verbose` (bool, optional) - If True, enables debug logs. Default: False
> 
>     *   `disable_tensor_cache` (bool, optional) - If False, HPU Graphs cache all input, intermediate and output tensors. Setting this to True frees up previously cached input and output tensors, thereby reducing the model’s memory requirements. This option cannot be used in certain conditions such as output is passed as input to forward. This option will be deprecated in a future release. Default: False
> 
>     *   `dry_run` (bool, optional) - If True, the model’s HPU Graphs are cached while avoiding the initial lazy execution. Subsequent replays launch the cached HPU Graphs. This option will be deprecated in a future release. Default: False

**Example:**

> import torch
> import habana_frameworks.torch as htorch
> from random import choice
> 
> class Net(torch.nn.Module):
>     def  __init__ (self):
>         super(Net, self). __init__ ()
>         self.fc1 = torch.nn.Linear(4, 4)
>         self.fc2 = torch.nn.Linear(4, 4)
>         self.fc3 = torch.nn.Linear(4, 4)
> 
>     def forward(self, x, condition=False):
>         N, _, _ = x.shape
>         x = self.fc1(x)
>         if condition:
>             x = self.fc2(x)
>         else:
>             x = self.fc3(x)
> 
>         x = x.view(N, -1)
>         return x
> 
> def generate_data(n_samples):
>     shapes = [(2, 3, 4), (3, 11, 4), (3, 4, 4)]
>     conditions = [True, False]
> 
>     inputs = [{'x': torch.randn(choice(shapes)).to('hpu'), 'condition': choice(conditions)} for _ in range(n_samples)]
>     targets = [torch.randn(item['x'].shape[0]).to('hpu') for item in inputs]
> 
>     return inputs, targets
> 
> rand_inputs, rand_targets = generate_data(n_samples=10)
> 
> model = Net().to('hpu')
> optimizer = torch.optim.SGD(model.parameters(),lr=0.1)
> htorch.hpu.ModuleCacher()(model=model, inplace=True, allow_unused_input=True, verbose=True, log_frequency=1)
> 
> for x, y in zip(rand_inputs, rand_targets):
>     optimizer.zero_grad(set_to_none=True)
>     y_pred = torch.mean(model(**x), 1)
>     loss = torch.nn.functional.mse_loss(y_pred, y)
>     loss.backward()
>     optimizer.step()
>     htorch.core.mark_step()

Note

*   The training interfaces, `ModuleCacher` and `make_graphed_callables`, should be called before the DDP hook registration.

*   The module to be wrapped should not contain any print statements. Since only HPU ops are cached, a print statement is only executed once. If `dry_run` is set to True, it may print incorrect values.

Random Number Generator APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#random-number-generator-apis "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

`import habana_frameworks.torch.hpu.random as htrandom` imports the HPU random package.

Below are the APIs available in torch.hpu.random package:

*   `htrandom.get_rng_state` - Returns the random number generator state of the specified HPU as a ByteTensor.

*   `htrandom.get_rng_state_all` - Returns a list of ByteTensor representing the random number states of all devices.

*   `htrandom.set_rng_state` - Sets the random number generator state of the specified HPU.

*   `htrandom.set_rng_state_all` - Sets the random number generator state of all devices.

*   `htrandom.manual_seed` - Sets the seed for generating random numbers for the current HPU device.

*   `htrandom.manual_seed_all` - Sets the seed for generating random numbers on all HPUs.

*   `htrandom.seed` - Sets the seed for generating random numbers to a random number for the current HPU.

*   `htrandom.seed_all` - Sets the seed for generating random numbers to a random number on all HPUs.

*   `htrandom.initial_seed` - Returns the current random seed of the current HPU.

**Example:**

import torch
import habana_frameworks.torch.hpu.random as htrandom
state = htrandom.get_rng_state()
htrandom.set_rng_state(state)
initial_seed = htrandom.initial_seed()
htrandom.manual_seed(2)
htrandom.seed()
print (hrandom.initial_seed())

Dynamic Shape APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#dynamic-shape-apis "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------

The dynamic shape APIs control how the Intel Gaudi PyTorch bridge and graph compiler manage dynamic shapes in model scripts. Dynamic shapes enabling is disabled by default. See the [Dynamic Shapes Optimization](https://docs.habana.ai/en/latest/PyTorch/Model_Optimization_PyTorch/Dynamic_Shapes.html#handling-dynamic-shapes) section for more information on how to optimize for dynamic shapes in data and models.

*   `import habana_frameworks.torch.hpu as ht` - Imports the package.

*   `ht.disable_dynamic_shape()` - Disables dynamic shape feature.

*   `ht.enable_dynamic_shape()` - Enables dynamic shape feature.

**Example:**

import habana_frameworks.torch.hpu as ht
    ht.disable_dynamic_shape()
    ht.enable_dynamic_shape()

HPU Inference APIs[¶](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#hpu-inference-apis "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------------------------

HPU Inference APIs enable the initialization of FP8 inference mode and facilitate the marking of model parameters as constant. For further details, refer to [Run Inference Using FP8](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#inference-using-fp8) section. The following APIs are available to initialize inference mode:

*   `hpu_initialize(model=None, mark_only_scales_as_const=False, mark_scales=True, mark_non_scales=True)` - Initializes inference mode and performs constant marking. This API is deprecated in favor of `hpu_inference_initialize`.

> *   `model` (torch.nn.Module) - The `torch.nn.Module` object to be initialized.
> 
>     *   `mark_only_scales_as_const` (bool) - Enables constant marking only for quantization scale parameters. Default is False. This parameter is deprecated in favor of `mark_scales`.
> 
>     *   `mark_scales` (bool) - Enables constant marking for quantization scale parameters. Default value is True.
> 
>     *   `mark_non_scales` (bool) - Enables constant marking for all parameters other than scales. Default value is True.

**Example:**

> import habana_frameworks.torch.core as htcore
> htcore.hpu_initialize(model=model, mark_scales=True, mark_non_scales=False)

*   `hpu_inference_initialize(model=None, mark_only_scales_as_const=False, mark_scales=True, mark_non_scales=True)` - Initializes inference mode and performs constant marking.

> > *   `model` (torch.nn.Module) - The `torch.nn.Module` object to be initialized.
> > 
> >     *   `mark_only_scales_as_const` (bool) - Enables constant marking only for quantization scale parameters. Default value is False. This parameter is deprecated with `mark_scales`.
> > 
> >     *   `mark_scales` (bool) - Enables constant marking for quantization scale parameters. Default value is True.
> > 
> >     *   `mark_non_scales` (bool) - Enables constant marking for all parameters other than scales. Default value is True.
> 
> 
> **Example:**
> 
> 
> > import habana_frameworks.torch.core as htcore
> > htcore.hpu_inference_initialize(model=model, mark_scales=True, mark_non_scales=False)
