# Source: https://huggingface.co/docs/bitsandbytes/v0.49.0/reference/optim/lamb.md

# LAMB

[LAMB (Layerwise adaptive large batch optimization)](https://hf.co/papers/1904.00962) is an adaptive optimizer designed for training with large batch sizes to accelerate training, combining ideas from `LARS` and `Adam` to automatically scale the learning rate for each layer:

- calculates a *trust ratio* between the weight and gradient norm in a layer and clips the ratio to prevent overly large or small updates
- updates weights with the first and second-moments

## LAMB[[api-class]][[bitsandbytes.optim.LAMB]]

#### bitsandbytes.optim.LAMB[[bitsandbytes.optim.LAMB]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lamb.py#L8)

__init__bitsandbytes.optim.LAMB.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lamb.py#L9[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "bias_correction", "val": " = True"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "adam_w_mode", "val": " = True"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = False"}, {"name": "max_unorm", "val": " = 1.0"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **bias_correction** (`bool`, defaults to `True`) --
  Whether to apply bias correction to the first and second-order moments.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **adam_w_mode** (`bool`, defaults to `True`) --
  Whether to use the AdamW variant.
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
- **max_unorm** (`float`, defaults to 1.0) --
  The maximum gradient norm.0

Base LAMB optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

bias_correction (`bool`, defaults to `True`) : Whether to apply bias correction to the first and second-order moments.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

adam_w_mode (`bool`, defaults to `True`) : Whether to use the AdamW variant.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 1.0) : The maximum gradient norm.

## LAMB8bit[[bitsandbytes.optim.LAMB8bit]]

#### bitsandbytes.optim.LAMB8bit[[bitsandbytes.optim.LAMB8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lamb.py#L75)

__init__bitsandbytes.optim.LAMB8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lamb.py#L76[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "bias_correction", "val": " = True"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "adam_w_mode", "val": " = True"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = False"}, {"name": "max_unorm", "val": " = 1.0"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **bias_correction** (`bool`, defaults to `True`) --
  Whether to apply bias correction to the first and second-order moments.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **adam_w_mode** (`bool`, defaults to `True`) --
  Whether to use the AdamW variant.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 1.0) --
  The maximum gradient norm.0

8-bit LAMB optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

bias_correction (`bool`, defaults to `True`) : Whether to apply bias correction to the first and second-order moments.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

adam_w_mode (`bool`, defaults to `True`) : Whether to use the AdamW variant.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 1.0) : The maximum gradient norm.

## LAMB32bit[[bitsandbytes.optim.LAMB32bit]]

#### bitsandbytes.optim.LAMB32bit[[bitsandbytes.optim.LAMB32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lamb.py#L139)

__init__bitsandbytes.optim.LAMB32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lamb.py#L140[{"name": "params", "val": ""}, {"name": "lr", "val": " = 0.001"}, {"name": "bias_correction", "val": " = True"}, {"name": "betas", "val": " = (0.9, 0.999)"}, {"name": "eps", "val": " = 1e-08"}, {"name": "weight_decay", "val": " = 0"}, {"name": "amsgrad", "val": " = False"}, {"name": "adam_w_mode", "val": " = True"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = False"}, {"name": "max_unorm", "val": " = 1.0"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`, defaults to 1e-3) --
  The learning rate.
- **bias_correction** (`bool`, defaults to `True`) --
  Whether to apply bias correction to the first and second-order moments.
- **betas** (`tuple(float, float)`, defaults to (0.9, 0.999)) --
  The beta values are the decay rates of the first and second-order moment of the optimizer.
- **eps** (`float`, defaults to 1e-8) --
  The epsilon value prevents division by zero in the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **amsgrad** (`bool`, defaults to `False`) --
  Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.
- **adam_w_mode** (`bool`, defaults to `True`) --
  Whether to use the AdamW variant.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.
- **max_unorm** (`float`, defaults to 1.0) --
  The maximum gradient norm.0

32-bit LAMB optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`, defaults to 1e-3) : The learning rate.

bias_correction (`bool`, defaults to `True`) : Whether to apply bias correction to the first and second-order moments.

betas (`tuple(float, float)`, defaults to (0.9, 0.999)) : The beta values are the decay rates of the first and second-order moment of the optimizer.

eps (`float`, defaults to 1e-8) : The epsilon value prevents division by zero in the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

amsgrad (`bool`, defaults to `False`) : Whether to use the [AMSGrad](https://hf.co/papers/1904.09237) variant of Adam that uses the maximum of past squared gradients instead.

adam_w_mode (`bool`, defaults to `True`) : Whether to use the AdamW variant.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

max_unorm (`float`, defaults to 1.0) : The maximum gradient norm.

