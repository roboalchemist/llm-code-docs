# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md

Title: The Link Between Lightning and Megatron Core#

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html

Published Time: Thu, 30 Oct 2025 07:07:29 GMT

Markdown Content:
In PyTorch Lightning, a Strategy is responsible for managing the distributed execution of a model during training, validation, and testing. Strategies typically wrap the user-defined model with a class that can handle distributed execution. For instance, the standard DDPStrategy (Distributed Data Parallel Strategy) wraps the model with PyTorch’s DistributedDataParallel class. This wrapper handles the distribution of data across multiple GPUs or nodes, synchronizes gradients during the backward pass, and ensures that model parameters remain consistent across all processes. Strategies in Lightning abstract away much of the complexity of distributed training, allowing users to focus on their model architecture and training logic while the framework handles the intricacies of distributed execution.

MegatronStrategy[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#megatronstrategy "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

The MegatronStrategy is a PyTorch Lightning strategy that enables distributed training of large language models using NVIDIA’s Megatron Core library. It’s designed to handle models that exceed the memory capacity of a single GPU by implementing various forms of model parallelism.

To use the MegatronStrategy, you initialize it with parameters that define the parallelism setup:

from nemo import lightning as nl

strategy = nl.MegatronStrategy(
    tensor_model_parallel_size=2,
    pipeline_model_parallel_size=2,
    virtual_pipeline_model_parallel_size=None,
    context_parallel_size=1,
    sequence_parallel=False,
    expert_model_parallel_size=1,
)

These parameters determine how the model will be split across available GPUs. The strategy then sets up the necessary distributed environment, initializing process groups for each type of parallelism.

The strategy is also responsible for configuring the checkpoint IO interface that handles saving and loading checkpoints. For a full list of options that can be configured via MegatronStrategy, refer to the [documentation](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/pytorch/strategies.py).

When you create your PyTorch Lightning Trainer, you pass this strategy:

trainer = nl.Trainer(strategy=strategy, devices=8, accelerator="gpu")

The MegatronStrategy utilizes Megatron’s distributed checkpointing system for model I/O. This system efficiently manages checkpoints for models partitioned across multiple GPUs, maintaining consistency across various parallelism configurations. It enables correct model reconstruction even when GPU setups differ between saving and loading.

The MegatronStrategy wraps the user-defined training_step, validation_step, and test_step methods to make them compatible with Megatron’s forward-backward pass implementation. This wrapping process allows these steps to be executed within the context of Megatron’s distributed execution framework, ensuring that all forms of parallelism are properly handled during each phase of the training loop. By doing this, the strategy maintains the familiar PyTorch Lightning interface for users while seamlessly integrating the complex distributed operations required for large-scale model training.

The `MegatronStrategy` employs the `MegatronParallel` class to manage the distributed execution of the user-defined model. This class breaks down the execution process into three key steps:

1.   Data Step: Prepares and distributes the input data across the model parallel groups.

2.   Forward Step: Executes the forward pass across the partitioned model.

3.   Loss Reduction: Computes and reduces the loss across the distributed setup.

MegatronParallel utilizes these steps to perform the forward-backward pass, which is derived from the user-defined `training_step`, `validation_step`, and `test_step` methods. It orchestrates the flow of data and gradients through the partitioned model, manages inter-GPU communication, and ensures proper gradient synchronization. This approach enables efficient execution across multiple GPUs while preserving the logical structure of the user’s Lightning module.

MegatronParallel[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#megatronparallel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

The `MegatronParallel` class is the core component that implements distributed model parallelism in the Megatron Core library. It manages the execution of the model across multiple GPUs, breaking down the process into three key steps:

1.   Data Step: This step prepares and distributes the input data across the model parallel groups. For the GPT model, it uses the `gpt_data_step` function:

def data_step(self, dataloader_iter):
    return gpt_data_step(dataloader_iter) 
This function handles:

    1.   Fetching a batch from the dataloader

    2.   Moving required tensors to CUDA

    3.   Slicing the batch for context parallelism using `get_batch_on_this_context_parallel_rank`

    4.   Preparing packed sequence parameters if necessary

2.   Forward Step: This step executes the forward pass across the partitioned model. For the GPT model, it uses the `gpt_forward_step` function:

def forward_step(self, model, batch):
    return gpt_forward_step(model, batch) 
This function:

    1.   Prepares the forward arguments from the batch

    2.   Calls the model’s forward method with these arguments

    3.   Handles both standard and packed sequence inputs

3.   Loss Reduction: After the forward pass, this step computes and reduces the loss across the distributed setup. The GPT model uses `MaskedTokenLossReduction`:

def loss_reduction(self, model):
    return model.training_loss_reduction() 
For validation:

def validation_loss_reduction(self, model):
    return model.validation_loss_reduction() 
These methods handle:

    1.   Calculating the loss using masked token loss

    2.   Reducing the loss across data parallel groups

    3.   Handling special cases for validation (e.g., not dropping the last batch)

The `MegatronParallel` class orchestrates these steps to perform the complete forward-backward pass.

By using these model-specific functions, `MegatronParallel` allows the GPT model to define its own data processing, forward pass, and loss calculation logic while still benefiting from the distributed execution framework. This approach enables researchers and engineers to work with large language models using familiar PyTorch Lightning interfaces, while the underlying distributed execution is handled transparently.

MegatronMixedPrecision[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#megatronmixedprecision "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The MegatronMixedPrecision class is a specialized precision plugin for Megatron Core library models in PyTorch Lightning. It extends the standard MixedPrecision plugin to handle the specific requirements of large language models trained with Megatron Core library.

from nemo import lightning as nl

precision = nl.MegatronMixedPrecision(precision="bf16-mixed")
trainer = nl.Trainer(strategy=strategy, plugins=precision)

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/features/megatron.html.md#megatronmixedprecision)
- [documentation](https://github.com/NVIDIA/NeMo/blob/main/nemo/lightning/pytorch/strategies.py)
