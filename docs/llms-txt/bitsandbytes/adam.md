# Source: https://huggingface.co/docs/bitsandbytes/v0.49.0/reference/optim/adam.md

# Adam

[Adam (Adaptive moment estimation)](https://hf.co/papers/1412.6980) is an adaptive learning rate optimizer, combining ideas from `SGD` with momentum and `RMSprop` to automatically scale the learning rate:

- a weighted average of the past gradients to provide direction (first-moment)
- a weighted average of the *squared* past gradients to adapt the learning rate to each parameter (second-moment)

bitsandbytes also supports paged optimizers which take advantage of CUDAs unified memory to transfer memory from the GPU to the CPU when GPU memory is exhausted.

## Adam[[api-class]][[bitsandbytes.optim.Adam]]

#### bitsandbytes.optim.Adam[[bitsandbytes.optim.Adam]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L9)

__init__bitsandbytes.optim.Adam.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L10[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
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

Base Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Adam8bit[[bitsandbytes.optim.Adam8bit]]

#### bitsandbytes.optim.Adam8bit[[bitsandbytes.optim.Adam8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L70)

__init__bitsandbytes.optim.Adam8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L71[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in Adam8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in Adam8bit as it always uses 8-bit optimization.
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

8-bit Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in Adam8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in Adam8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## Adam32bit[[bitsandbytes.optim.Adam32bit]]

#### bitsandbytes.optim.Adam32bit[[bitsandbytes.optim.Adam32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L142)

__init__bitsandbytes.optim.Adam32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L143[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
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

32-bit Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdam[[bitsandbytes.optim.PagedAdam]]

#### bitsandbytes.optim.PagedAdam[[bitsandbytes.optim.PagedAdam]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L203)

__init__bitsandbytes.optim.PagedAdam.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L204[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
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

Paged Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdam8bit[[bitsandbytes.optim.PagedAdam8bit]]

#### bitsandbytes.optim.PagedAdam8bit[[bitsandbytes.optim.PagedAdam8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L264)

__init__bitsandbytes.optim.PagedAdam8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L265[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
  Note: This parameter is not supported in PagedAdam8bit and must be False.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
  Note: This parameter is not used in PagedAdam8bit as it always uses 8-bit optimization.
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

8-bit paged Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead. Note: This parameter is not supported in PagedAdam8bit and must be False.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state. Note: This parameter is not used in PagedAdam8bit as it always uses 8-bit optimization.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

## PagedAdam32bit[[bitsandbytes.optim.PagedAdam32bit]]

#### bitsandbytes.optim.PagedAdam32bit[[bitsandbytes.optim.PagedAdam32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L336)

__init__bitsandbytes.optim.PagedAdam32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/adam.py#L337[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}, {"name": "is_paged", "val": " = False"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
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

Paged 32-bit Adam optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

is_paged (`bool`, defaults to `False`) : Whether the optimizer is a paged optimizer or not.

