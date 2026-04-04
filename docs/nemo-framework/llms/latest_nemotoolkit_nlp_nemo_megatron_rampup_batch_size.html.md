# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html.md

Title: Ramp Up Batch Size — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html

Published Time: Thu, 30 Oct 2025 07:07:32 GMT

Markdown Content:
Ramp Up Batch Size[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html.md#ramp-up-batch-size "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ramp up batch size is a feature that allows training to start with a smaller global batch size and linearly increase to a target global batch size over a given number of training samples with specified incremental steps.

Usage[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html.md#usage "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

To enable global batch size rampup during training, set the rampup_batch_size parameter under the model section of training configuration. This parameter should be a list of three values:

*   `start_batch_size`: The initial batch size.

*   `batch_size_increment`: The amount by which the batch size will increase at each step.

*   `rampup_samples`: The number of training samples over which the batch size will be ramped up.

`model.global_batch_size=1024 model.rampup_batch_size=[256, 128, 50000000]`

In this example, the training will start with a batch size of 256, increment by 128, and reach the target global batch size of 1024 over 50,000,000 training samples.

Ramp Up Stages and Training Interruption[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html.md#ramp-up-stages-and-training-interruption "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once the next rampup stage is reached (the point in training when the global batch size increases), NeMo will stop the training. It allows to rerun the training job with a larger number of GPUs or nodes for the next stage of ramp up batch size.

Automatic Node Scheduling[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html.md#automatic-node-scheduling "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the [NeMo-Framework-Launcher](https://github.com/NVIDIA/NeMo-Framework-Launcher), when using rampup batch size, a node scheduler is created automatically. This scheduler allows the use smaller number of nodes for smaller batch size stages and scales up according to the `training.trainer.num_nodes` parameter. This parameter corresponds to the maximum number of nodes you want to use for the maximum global batch size.

Example[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html.md#example "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

Detailed example of ramp up batch size feature usage with GPT3 5B model and [NeMo-Framework-Launcher](https://github.com/NVIDIA/NeMo-Framework-Launcher). In this example, the training started with a global batch size of 256, increased by 256 at each ramp up stage, and reached the target global batch size of 2048 over 10,000,000 training samples.

Node schedule looks as follows:

| global_batch_size | num_nodes |
| --- | --- |
| 256 | 8 |
| 512 | 8 |
| 768 | 8 |
| 1024 | 8 |
| 1280 | 10 |
| 1536 | 12 |
| 1792 | 14 |
| 2048 | 16 |

Plot of `global_batch_size` increase during training:

[![Image 1](https://github.com/NVIDIA/NeMo/releases/download/v2.0.0rc0/asset-post-rampup-batch-size-example.png)](https://github.com/NVIDIA/NeMo/releases/download/v2.0.0rc0/asset-post-rampup-batch-size-example.png)

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/nlp/nemo_megatron/rampup_batch_size.html.md#example)
- [NeMo-Framework-Launcher](https://github.com/NVIDIA/NeMo-Framework-Launcher)
- [](https://github.com/NVIDIA/NeMo/releases/download/v2.0.0rc0/asset-post-rampup-batch-size-example.png)
