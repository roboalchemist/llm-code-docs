# Source: https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html

Title: Common API — Transformer Engine 2.6.0 documentation

URL Source: https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html

Published Time: Wed, 10 Sep 2025 02:24:06 GMT

Markdown Content:
Common API[](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html.md#common-api "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

_class_ transformer_engine.common.recipe.Format(_*args_, _**kwds_)[](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html.md#transformer_engine.common.recipe.Format "Link to this definition")
Supported FP8 formats.

Values:
*   **E4M3** – All FP8 tensors are in e4m3 format

*   **E5M2** – All FP8 tensors are in e5m2 format

*   **HYBRID** – FP8 tensors in the forward pass are in e4m3 format, FP8 tensors in the backward pass are in e5m2 format

_class_ transformer_engine.common.recipe.DelayedScaling(_margin=0_, _fp8\_format=Format.HYBRID_, _amax\_history\_len=1024_, _amax\_compute\_algo='max'_, _scaling\_factor\_compute\_algo=None_)[](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html.md#transformer_engine.common.recipe.DelayedScaling "Link to this definition")
Use the delayed scaling factor strategy. Use scale factor from previous iteration and record amax history of amax_history_len steps.

Parameters:
*   **margin** (_int_ _,_ _default = 0_) – Margin for the scaling factor computation.

*   **fp8_format** (_{Format.E4M3_ _,_ _Format.HYBRID}_ _,_ _default = Format.HYBRID_) – Controls the FP8 data format used during forward and backward pass.

*   **amax_history_len** (_int_ _,_ _default = 1024_) – The length of the amax history window used for scaling factor computation.

*   **amax_compute_algo** (_{'max'_ _,_ _'most\_recent'_ _,_ _Callable}_ _,_ _default = 'max'_) –

Algorithm used for choosing the amax value for the scaling factor computation. There are 2 predefined choices: max chooses the largest amax in the history window, while most_recent always chooses the most recently seen value. Alternatively, one may pass a function of the signature:

def amax_compute(amax_history: Tensor) -> Tensor 
where Tensor is a framework tensor type.

*   **scaling_factor_compute_algo** (_Callable_ _,_ _default = None_) –

Algorithm used for computing the new scaling factor based on the value of amax. It should be a function of the signature:

def scaling_factor_compute(amax: Tensor,
                           old_scaling_factor: Tensor,
                           fp8_max: Tensor,
                           recipe: DelayedScaling) -> Tensor 
where Tensor is a framework tensor type.

*   **reduce_amax** (bool, default = True) – By default, if torch.distributed is initialized, the amax value for FP8 tensors is reduced across the fp8_group (specified in the fp8_autocast call). This keeps the amaxes and scaling factors synced across the given distributed group. If set to False, this reduction is skipped and every GPU maintains local amaxes and scaling factors. To ensure results are numerically identical across checkpointing boundaries in this case, all ranks must checkpoint in order to store the local tensors.

*   **fp8_dpa** (bool, default = False) – Whether to enable FP8 dot product attention (DPA). When the model is placed in an fp8_autocast(enabled=True) region and fp8_dpa is set to True, DPA casts the inputs from higher precision to FP8, performs attention in FP8, and casts tensors back to higher precision as outputs. FP8 DPA currently is only supported in the FusedAttention backend.

*   **fp8_mha** (bool, default = False) – Whether to enable FP8 multi-head attention (MHA). When True, it removes the casting operations mentioned above at the DPA boundaries. Currently only standard MHA modules i.e. LayerNormLinear/Linear + DPA + Linear, are supported for this feature. When fp8_mha = False, fp8_dpa = True, a typical MHA module works as LayerNormLinear (BF16 output) -> (cast to FP8 ) FP8 DPA (cast to BF16) -> Linear. When fp8_mha = True, fp8_dpa = True, it becomes LayerNormLinear (FP8 output) -> FP8 DPA -> Linear.

Notes

*   By default (when scaling_factor_compute_algo is left as None) the scaling factor is computed from the final amax value using the formula:

FP8_MAX = maximum_representable_value(fp8_format)
new_scaling_factor = (FP8_MAX / amax) / (2 ^ margin) 
*   fp8_dpa and fp8_mha are Beta features, and their API and functionality are subject to change in future Transformer Engine releases.

_class_ transformer_engine.common.recipe.MXFP8BlockScaling(_fp8\_format=Format.E4M3_)[](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html.md#transformer_engine.common.recipe.MXFP8BlockScaling "Link to this definition")
Use the MXFP8 scaling factor strategy.

In this strategy, tensors are scaled in blockwise fashion. Each group of 32 consecutive values is scaled together using their own scaling factor. The type of the scaling factor is E8M0 (8 bits of exponent, 0 bits of mantissa), equivalent to scaling by a power of 2.

Since the scaling happens in a particular direction (either rowwise or columnwise), in this recipe the quantized tensor and its transpose are not numerically equivalent. Due to this, when Transformer Engine needs both the MXFP8 tensor and its transpose (e.g. to calculate both forward and backward pass), during the quantization both versions are computed from the high precision input to avoid double quantization errors.

Parameters:
**fp8_format** (_{Format.E4M3_ _,_ _Format.HYBRID}_ _,_ _default = Format.E4M3_) – Controls the FP8 data format used during forward and backward pass.

_class_ transformer_engine.common.recipe.Float8CurrentScaling(_fp8\_format=Format.HYBRID_)[](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html.md#transformer_engine.common.recipe.Float8CurrentScaling "Link to this definition")
Use the per-tensor current scaling factor strategy.

Parameters:
**fp8_format** (_{Format.E4M3_ _,_ _Format.HYBRID}_ _,_ _default = Format.HYBRID_) – Controls the FP8 data format used during forward and backward pass.

_class_ transformer_engine.common.recipe.Float8BlockScaling(_fp8\_format=Format.E4M3_)[](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html.md#transformer_engine.common.recipe.Float8BlockScaling "Link to this definition")
Use block-wise scaling for FP8 tensors.

In this strategy, tensors are scaled in blockwise fashion. Values within each block share a common scaling factor. The block dimensionality can be configured. The scaling factors are float32 containers. They will by default be constrained to powers of 2.

Since the scaling happens in a particular direction (either rowwise or columnwise), the quantized tensor and its transpose are not numerically equivalent. Due to this, when Transformer Engine needs both the FP8 tensor and its transpose (e.g. to calculate both forward and backward pass), during the quantization both versions are computed from the high precision input to avoid double quantization errors.

NOTE: To relax the default constraint that scales be powers of 2, set env variable NVTE_FP8_BLOCK_SCALING_FP32_SCALES=1 to override it for the recipe defaults.

Parameters:
**fp8_format** (_{Format.E4M3_ _,_ _Format.HYBRID}_ _,_ _default = Format.E4M3_) – Controls the FP8 data format used during forward and backward pass.

Links/Buttons:
- [](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/index.html)
- [View page source](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/_sources/api/common.rst.txt)
- [](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html.md#transformer_engine.common.recipe.Float8BlockScaling)
- [Previous](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/faq.html.md)
- [Next](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/framework.html.md)
- [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy.md/)
- [Manage My Privacy](https://www.nvidia.com/en-us/about-nvidia/privacy-center.md/)
- [Do Not Sell or Share My Data](https://www.nvidia.com/en-us/preferences/start.md/)
- [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service.md/)
- [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility.md/)
- [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies.md/)
- [Product Security](https://www.nvidia.com/en-us/product-security.md/)
- [Contact](https://www.nvidia.com/en-us/contact/)
