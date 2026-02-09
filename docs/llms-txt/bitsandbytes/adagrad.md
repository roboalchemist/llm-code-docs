# Source: https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/adagrad.md

# AdaGrad

[AdaGrad (Adaptive Gradient)](https://jmlr.org/papers/v12/duchi11a.html) is an adaptive learning rate optimizer. AdaGrad stores a sum of the squared past gradients for each parameter and uses it to scale their learning rate. This allows the learning rate to be automatically lower or higher depending on the magnitude of the gradient, eliminating the need to manually tune the learning rate.

## Adagrad[[api-class]][[bitsandbytes.optim.Adagrad]]

#### bitsandbytes.optim.Adagrad[[bitsandbytes.optim.Adagrad]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L8)

__init__bitsandbytes.optim.Adagrad.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L9[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.01"}, {"name": "lr_decay", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "initial_accumulator_value", "val": " = 0"}, {"name": "eps", "val": " = 1e-10"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-2) --
  The learning rate.
- **lr_decay** (`int`, defaults to 0) --
  The learning rate decay.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **initial_accumulator_value** (`int`, defaults to 0) --
  The initial momemtum values.
- **eps** (`float`, defaults to 1e-10) --
  The epsilon value prevents division by zero in the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Base Adagrad optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-2) : The learning rate.

lr_decay (`int`, defaults to 0) : The learning rate decay.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

initial_accumulator_value (`int`, defaults to 0) : The initial momemtum values.

eps (`float`, defaults to 1e-10) : The epsilon value prevents division by zero in the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## Adagrad8bit[[bitsandbytes.optim.Adagrad8bit]]

#### bitsandbytes.optim.Adagrad8bit[[bitsandbytes.optim.Adagrad8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L75)

__init__bitsandbytes.optim.Adagrad8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L76[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.01"}, {"name": "lr_decay", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "initial_accumulator_value", "val": " = 0"}, {"name": "eps", "val": " = 1e-10"}, {"name": "optim_bits", "val": " = 8"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-2) --
  The learning rate.
- **lr_decay** (`int`, defaults to 0) --
  The learning rate decay.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **initial_accumulator_value** (`int`, defaults to 0) --
  The initial momemtum values.
- **eps** (`float`, defaults to 1e-10) --
  The epsilon value prevents division by zero in the optimizer.
- **optim_bits** (`int`, defaults to 8) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

8-bit Adagrad optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-2) : The learning rate.

lr_decay (`int`, defaults to 0) : The learning rate decay.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

initial_accumulator_value (`int`, defaults to 0) : The initial momemtum values.

eps (`float`, defaults to 1e-10) : The epsilon value prevents division by zero in the optimizer.

optim_bits (`int`, defaults to 8) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## Adagrad32bit[[bitsandbytes.optim.Adagrad32bit]]

#### bitsandbytes.optim.Adagrad32bit[[bitsandbytes.optim.Adagrad32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L143)

__init__bitsandbytes.optim.Adagrad32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/adagrad.py#L144[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.01"}, {"name": "lr_decay", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "initial_accumulator_value", "val": " = 0"}, {"name": "eps", "val": " = 1e-10"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-2) --
  The learning rate.
- **lr_decay** (`int`, defaults to 0) --
  The learning rate decay.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **initial_accumulator_value** (`int`, defaults to 0) --
  The initial momemtum values.
- **eps** (`float`, defaults to 1e-10) --
  The epsilon value prevents division by zero in the optimizer.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

32-bit Adagrad optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-2) : The learning rate.

lr_decay (`int`, defaults to 0) : The learning rate decay.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

initial_accumulator_value (`int`, defaults to 0) : The initial momemtum values.

eps (`float`, defaults to 1e-10) : The epsilon value prevents division by zero in the optimizer.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

