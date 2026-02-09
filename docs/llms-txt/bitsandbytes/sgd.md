# Source: https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/optim/sgd.md

# SGD

Stochastic gradient descent (SGD) is a basic gradient descent optimizer to minimize loss given a set of model parameters and updates the parameters in the opposite direction of the gradient. The update is performed on a randomly sampled mini-batch of data from the dataset.

bitsandbytes also supports momentum and Nesterov momentum to accelerate SGD by adding a weighted average of past gradients to the current gradient.

## SGD[[api-class]][[bitsandbytes.optim.SGD]]

#### bitsandbytes.optim.SGD[[bitsandbytes.optim.SGD]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L8)

__init__bitsandbytes.optim.SGD.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L9[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "optim_bits", "val": " = 32"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
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
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

Base SGD optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

optim_bits (`int`, defaults to 32) : The number of bits of the optimizer state.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## SGD8bit[[bitsandbytes.optim.SGD8bit]]

#### bitsandbytes.optim.SGD8bit[[bitsandbytes.optim.SGD8bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L67)

__init__bitsandbytes.optim.SGD8bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L68[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

8-bit SGD optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

## SGD32bit[[bitsandbytes.optim.SGD32bit]]

#### bitsandbytes.optim.SGD32bit[[bitsandbytes.optim.SGD32bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L123)

__init__bitsandbytes.optim.SGD32bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/optim/sgd.py#L124[{"name": "params", "val": ""}, {"name": "lr", "val": ""}, {"name": "momentum", "val": " = 0"}, {"name": "dampening", "val": " = 0"}, {"name": "weight_decay", "val": " = 0"}, {"name": "nesterov", "val": " = False"}, {"name": "args", "val": " = None"}, {"name": "min_8bit_size", "val": " = 4096"}, {"name": "percentile_clipping", "val": " = 100"}, {"name": "block_wise", "val": " = True"}]- **params** (`torch.tensor`) --
  The input parameters to optimize.
- **lr** (`float`) --
  The learning rate.
- **momentum** (`float`, defaults to 0) --
  The momentum value speeds up the optimizer by taking bigger steps.
- **dampening** (`float`, defaults to 0) --
  The dampening value reduces the momentum of the optimizer.
- **weight_decay** (`float`, defaults to 0.0) --
  The weight decay value for the optimizer.
- **nesterov** (`bool`, defaults to `False`) --
  Whether to use Nesterov momentum.
- **args** (`object`, defaults to `None`) --
  An object with additional arguments.
- **min_8bit_size** (`int`, defaults to 4096) --
  The minimum number of elements of the parameter tensors for 8-bit optimization.
- **percentile_clipping** (`int`, defaults to 100) --
  Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.
- **block_wise** (`bool`, defaults to `True`) --
  Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.0

32-bit SGD optimizer.

**Parameters:**

params (`torch.tensor`) : The input parameters to optimize.

lr (`float`) : The learning rate.

momentum (`float`, defaults to 0) : The momentum value speeds up the optimizer by taking bigger steps.

dampening (`float`, defaults to 0) : The dampening value reduces the momentum of the optimizer.

weight_decay (`float`, defaults to 0.0) : The weight decay value for the optimizer.

nesterov (`bool`, defaults to `False`) : Whether to use Nesterov momentum.

args (`object`, defaults to `None`) : An object with additional arguments.

min_8bit_size (`int`, defaults to 4096) : The minimum number of elements of the parameter tensors for 8-bit optimization.

percentile_clipping (`int`, defaults to 100) : Adapts clipping threshold automatically by tracking the last 100 gradient norms and clipping the gradient at a certain percentile to improve stability.

block_wise (`bool`, defaults to `True`) : Whether to independently quantize each block of tensors to reduce outlier effects and improve stability.

