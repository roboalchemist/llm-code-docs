# Source: https://huggingface.co/docs/bitsandbytes/v0.49.0/reference/optim/lars.md

# LARS

[LARS (Layer-wise Adaptive Rate Scaling)](https:/hf.co/papers/1708.03888) is an optimizer designed for training with large batch sizes to accelerate training. LARS uses a separate learning rate for each *layer* instead of each parameter. The learning rate is calculated from a *trust ratio* between the weight and gradient norm in a layer. This helps calibrate a stable update size.

## LARS[[api-class]][[bitsandbytes.optim.LARS]]

#### bitsandbytes.optim.LARS[[bitsandbytes.optim.LARS]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lars.py#L11)

__init__bitsandbytes.optim.LARS.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lars.py#L12[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "max_unorm", "val": " = 0.02"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **optim_bits** (`int`, defaults to 32) --
  The number of bits of the optimizer state.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **max_unorm** (`float`, defaults to 0.02) --
  The maximum gradient norm.0

Base LARS optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

max_unorm (`float`, defaults to 0.02) : The maximum gradient norm.

## LARS8bit[[bitsandbytes.optim.LARS8bit]]

#### bitsandbytes.optim.LARS8bit[[bitsandbytes.optim.LARS8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lars.py#L71)

__init__bitsandbytes.optim.LARS8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lars.py#L72[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "max_unorm", "val": " = 0.02"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **max_unorm** (`float`, defaults to 0.02) --
  The maximum gradient norm.0

8-bit LARS optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

max_unorm (`float`, defaults to 0.02) : The maximum gradient norm.

## LARS32bit[[bitsandbytes.optim.LARS32bit]]

#### bitsandbytes.optim.LARS32bit[[bitsandbytes.optim.LARS32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lars.py#L128)

__init__bitsandbytes.optim.LARS32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/optim/lars.py#L129[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "max_unorm", "val": " = 0.02"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 1e-2) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **max_unorm** (`float`, defaults to 0.02) --
  The maximum gradient norm.0

32-bit LARS optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 1e-2) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

max_unorm (`float`, defaults to 0.02) : The maximum gradient norm.

