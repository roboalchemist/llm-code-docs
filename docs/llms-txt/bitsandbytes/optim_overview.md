# Source: https://huggingface.co/docs/bitsandbytes/v0.49.0/reference/optim/optim_overview.md

# Overview

[8-bit optimizers](https://hf.co/papers/2110.02861) reduce the memory footprint of 32-bit optimizers without any performance degradation which means you can train large models with many parameters faster. At the core of 8-bit optimizers is block-wise quantization which enables quantization accuracy, computational efficiency, and stability.

bitsandbytes provides 8-bit optimizers through the base `Optimizer8bit` class, and additionally provides `Optimizer2State` and `Optimizer1State` for 2-state (for example, `Adam`) and 1-state (for example, `Adagrad`) optimizers respectively. To provide custom optimizer hyperparameters, use the `GlobalOptimManager` class to configure the optimizer.

## Optimizer8bit[[bitsandbytes.optim.optimizer.Optimizer8bit]]

#### bitsandbytes.optim.optimizer.Optimizer8bit[[bitsandbytes.optim.optimizer.Optimizer8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L113)

__init__bitsandbytes.optim.optimizer.Optimizer8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L114[{"name": "params", "val": ""}, {"name": "defaults", "val": ""}, {"name": "optim_bits", "val": " = 32"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base 8-bit optimizer class.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Optimizer2State[[bitsandbytes.optim.optimizer.Optimizer2State]]

#### bitsandbytes.optim.optimizer.Optimizer2State[[bitsandbytes.optim.optimizer.Optimizer2State]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L347)

__init__bitsandbytes.optim.optimizer.Optimizer2State.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L348[{"name": "optimizer_name", "val": ""}, {"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.0"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "max_unorm", "val": " = 0.0"}, {"name": "skip_zeros", "val": " = False"}, {"name": "is_paged", "val": " = False"}, {"name": "alpha", "val": " = 0.0"}, {"name": "t_alpha", "val": ": typing.Optional[int] = None"}, {"name": "t_beta3", "val": ": typing.Optional[int] = None"}]- **optimizer_name** (`str`) --
  The name of the optimizer.
- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple`, defaults to (0.9, 0.999)) --
  The beta values for the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value for the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 0.0) --
  The maximum value to normalize each block with.
- **skip_zeros** (`bool`, defaults to `False`) --
  Whether to skip zero values for sparse gradients and models to ensure correct updates.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.
- **alpha** (`float`, defaults to 0.0) --
  The alpha value for the AdEMAMix optimizer.
- **t_alpha** (`Optional[int]`, defaults to `None`) --
  Number of iterations for alpha scheduling with AdEMAMix.
- **t_beta3** (`Optional[int]`, defaults to `None`) --
  Number of iterations for beta scheduling with AdEMAMix.0

Base 2-state update optimizer class.

**Parameters:**

optimizer_name (`str`) : The name of the optimizer.

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple`, defaults to (0.9, 0.999)) : The beta values for the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value for the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 0.0) : The maximum value to normalize each block with.

skip_zeros (`bool`, defaults to `False`) : Whether to skip zero values for sparse gradients and models to ensure correct updates.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

alpha (`float`, defaults to 0.0) : The alpha value for the AdEMAMix optimizer.

t_alpha (`Optional[int]`, defaults to `None`) : Number of iterations for alpha scheduling with AdEMAMix.

t_beta3 (`Optional[int]`, defaults to `None`) : Number of iterations for beta scheduling with AdEMAMix.

## Optimizer1State[[bitsandbytes.optim.optimizer.Optimizer1State]]

#### bitsandbytes.optim.optimizer.Optimizer1State[[bitsandbytes.optim.optimizer.Optimizer1State]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L591)

__init__bitsandbytes.optim.optimizer.Optimizer1State.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L592[{"name": "optimizer_name", "val": ""}, {"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.0)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.0"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "max_unorm", "val": " = 0.0"}, {"name": "skip_zeros", "val": " = False"}, {"name": "is_paged", "val": " = False"}]- **optimizer_name** (`str`) --
  The name of the optimizer.
- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple`, defaults to (0.9, 0.0)) --
  The beta values for the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value for the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 0.0) --
  The maximum value to normalize each block with.
- **skip_zeros** (`bool`, defaults to `False`) --
  Whether to skip zero values for sparse gradients and models to ensure correct updates.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base 1-state update optimizer class.

**Parameters:**

optimizer_name (`str`) : The name of the optimizer.

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple`, defaults to (0.9, 0.0)) : The beta values for the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value for the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 0.0) : The maximum value to normalize each block with.

skip_zeros (`bool`, defaults to `False`) : Whether to skip zero values for sparse gradients and models to ensure correct updates.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Utilities[[bitsandbytes.optim.GlobalOptimManager]]

#### bitsandbytes.optim.GlobalOptimManager[[bitsandbytes.optim.GlobalOptimManager]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L22)

A global optimizer manager for enabling custom optimizer configs.

override_configbitsandbytes.optim.GlobalOptimManager.override_confighttps://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/optimizer.py#L56[{"name": "parameters", "val": ""}, {"name": "key", "val": " = None"}, {"name": "value", "val": " = None"}, {"name": "key_value_dict", "val": " = None"}]- **parameters** (`torch.Tensor` or `list(torch.Tensors)`) --
  The input parameters.
- **key** (`str`) --
  The hyperparameter to override.
- **value** --
  The hyperparameter value.
- **key_value_dict** (`dict`) --
  A dictionary with multiple key-values to override.0

Override initial optimizer config with specific hyperparameters.

The key-values of the optimizer config for the input parameters are overridden
This can be both, optimizer parameters like `betas` or `lr`, or it can be
8-bit specific parameters like `optim_bits` or `percentile_clipping`.

Example:

```py
import torch
import bitsandbytes as bnb

mng = bnb.optim.GlobalOptimManager.get_instance()

model = MyModel()
mng.register_parameters(model.parameters()) # 1. register parameters while still on CPU

model = model.cuda()
# use 8-bit optimizer states for all parameters
adam = bnb.optim.Adam(model.parameters(), lr=0.001, optim_bits=8)

# 2. override: the parameter model.fc1.weight now uses 32-bit Adam
mng.override_config(model.fc1.weight, 'optim_bits', 32)
```

**Parameters:**

parameters (`torch.Tensor` or `list(torch.Tensors)`) : The input parameters.

key (`str`) : The hyperparameter to override.

value : The hyperparameter value.

key_value_dict (`dict`) : A dictionary with multiple key-values to override.

