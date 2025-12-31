# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md

Title: Metrics — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html

Published Time: Fri, 05 Sep 2025 19:01:20 GMT

Markdown Content:
Metrics[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#metrics "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.collections.common.metrics.Perplexity(_*args:Any_, _**kwargs:Any_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity "Link to this definition")
Bases: `Metric`

This class computes mean perplexity of distributions in the last dimension of inputs. It is a wrapper around torch.distributions.Categorical.perplexity method. You have to provide either `probs` or `logits` to the [`update()`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.update "nemo.collections.common.metrics.Perplexity.update") method. The class computes perplexities for distributions passed to [`update()`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.update "nemo.collections.common.metrics.Perplexity.update") method in `probs` or `logits` arguments and averages the perplexities. Reducing results between all workers is done via SUM operations. See the [TorchMetrics in PyTorch Lightning guide](https://lightning.ai/docs/torchmetrics/stable/pages/lightning.html) for the metric usage instructions.

Parameters:
*   **dist_sync_on_step** – Synchronize metric state across processes at each `forward()` before returning the value at the step.

*   **process_group** –

Specify the process group on which synchronization is called. default: `None` (which selects the entire
world)

*   **validate_args** – If `True` values of [`update()`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.update "nemo.collections.common.metrics.Perplexity.update") method parameters are checked. `logits` has to not contain NaNs and `probs` last dim has to be valid probability distribution.

compute()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.compute "Link to this definition")
Returns perplexity across all workers and resets to 0 `perplexities_sum` and `num_distributions`.

full_state_update _=True_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.full_state_update "Link to this definition")update(_probs=None_, _logits=None_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.update "Link to this definition")
Updates `perplexities_sum` and `num_distributions`. :param probs: A `torch.Tensor` which innermost dimension is valid probability distribution. :param logits: A `torch.Tensor` without NaNs.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.full_state_update)
- [update()](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/common/metrics.html.md#nemo.collections.common.metrics.Perplexity.update)
- [TorchMetrics in PyTorch Lightning guide](https://lightning.ai/docs/torchmetrics/stable/pages/lightning.html)
