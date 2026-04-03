# Source: https://huggingface.co/docs/bitsandbytes/v0.49.0/reference/optim/adamw.md

# AdamW

[AdamW](https://hf.co/papers/1711.05101) is a variant of the `Adam` optimizer that separates weight decay from the gradient update based on the observation that the weight decay formulation is different when applied to `SGD` and `Adam`.

bitsandbytes also supports paged optimizers which take advantage of CUDAs unified memory to transfer memory from the GPU to the CPU when GPU memory is exhausted.

## AdamW[[api-class]][[bitsandbytes.optim.AdamW]]

#### bitsandbytes.optim.AdamW[[bitsandbytes.optim.AdamW]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L9)

__init__bitsandbytes.optim.AdamW.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L10[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
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
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

Base AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## AdamW8bit[[bitsandbytes.optim.AdamW8bit]]

#### bitsandbytes.optim.AdamW8bit[[bitsandbytes.optim.AdamW8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L70)

__init__bitsandbytes.optim.AdamW8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L71[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in AdamW8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in AdamW8bit as it always uses 8-bit optimization.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

8-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in AdamW8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in AdamW8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## AdamW32bit[[bitsandbytes.optim.AdamW32bit]]

#### bitsandbytes.optim.AdamW32bit[[bitsandbytes.optim.AdamW32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L142)

__init__bitsandbytes.optim.AdamW32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L143[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
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
- **is_paged** (`bool`, defaults to `False`) --
  Whether the optimizer is a paged optimizer or not.0

32-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdamW[[bitsandbytes.optim.PagedAdamW]]

#### bitsandbytes.optim.PagedAdamW[[bitsandbytes.optim.PagedAdamW]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L203)

__init__bitsandbytes.optim.PagedAdamW.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L204[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
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

Paged AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## PagedAdamW8bit[[bitsandbytes.optim.PagedAdamW8bit]]

#### bitsandbytes.optim.PagedAdamW8bit[[bitsandbytes.optim.PagedAdamW8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L261)

__init__bitsandbytes.optim.PagedAdamW8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L262[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in PagedAdamW8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in PagedAdamW8bit as it always uses 8-bit optimization.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Paged 8-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in PagedAdamW8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in PagedAdamW8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## PagedAdamW32bit[[bitsandbytes.optim.PagedAdamW32bit]]

#### bitsandbytes.optim.PagedAdamW32bit[[bitsandbytes.optim.PagedAdamW32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L330)

__init__bitsandbytes.optim.PagedAdamW32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adamw.py#L331[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0.01"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.Tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
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

Paged 32-bit AdamW optimizer.

**Parameters:**

params (`torch.Tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

