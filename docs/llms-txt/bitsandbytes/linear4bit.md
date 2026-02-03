# Source: https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/linear4bit.md

# 4-bit quantization

[QLoRA](https://hf.co/papers/2305.14314) is a finetuning method that quantizes a model to 4-bits and adds a set of low-rank adaptation (LoRA) weights to the model and tuning them through the quantized weights. This method also introduces a new data type, 4-bit NormalFloat (`LinearNF4`) in addition to the standard Float4 data type (`LinearFP4`). `LinearNF4` is a quantization data type for normally distributed data and can improve performance.

## Linear4bit[[bitsandbytes.nn.Linear4bit]]

#### bitsandbytes.nn.Linear4bit[[bitsandbytes.nn.Linear4bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L422)

This class is the base module for the 4-bit quantization algorithm presented in [QLoRA](https://arxiv.org/abs/2305.14314).
QLoRA 4-bit linear layers uses blockwise k-bit quantization under the hood, with the possibility of selecting various
compute datatypes such as FP4 and NF4.

In order to quantize a linear layer one should first load the original fp16 / bf16 weights into
the Linear4bit module, then call `quantized_module.to("cuda")` to quantize the fp16 / bf16 weights.

Example:

```python
import torch
import torch.nn as nn

import bitsandbytes as bnb
from bnb.nn import Linear4bit

fp16_model = nn.Sequential(
    nn.Linear(64, 64),
    nn.Linear(64, 64)
)

quantized_model = nn.Sequential(
    Linear4bit(64, 64),
    Linear4bit(64, 64)
)

quantized_model.load_state_dict(fp16_model.state_dict())
quantized_model = quantized_model.to(0) # Quantization happens here
```

__init__bitsandbytes.nn.Linear4bit.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L455[{"name": "input_features", "val": ""}, {"name": "output_features", "val": ""}, {"name": "bias", "val": " = True"}, {"name": "compute_dtype", "val": " = None"}, {"name": "compress_statistics", "val": " = True"}, {"name": "quant_type", "val": " = 'fp4'"}, {"name": "quant_storage", "val": " = torch.uint8"}, {"name": "device", "val": " = None"}]- **input_features** (`str`) --
  Number of input features of the linear layer.
- **output_features** (`str`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

Initialize Linear4bit class.

**Parameters:**

input_features (`str`) : Number of input features of the linear layer.

output_features (`str`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## LinearFP4[[bitsandbytes.nn.LinearFP4]]

#### bitsandbytes.nn.LinearFP4[[bitsandbytes.nn.LinearFP4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L560)

Implements the FP4 data type.

__init__bitsandbytes.nn.LinearFP4.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L565[{"name": "input_features", "val": ""}, {"name": "output_features", "val": ""}, {"name": "bias", "val": " = True"}, {"name": "compute_dtype", "val": " = None"}, {"name": "compress_statistics", "val": " = True"}, {"name": "quant_storage", "val": " = torch.uint8"}, {"name": "device", "val": " = None"}]- **input_features** (`str`) --
  Number of input features of the linear layer.
- **output_features** (`str`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

**Parameters:**

input_features (`str`) : Number of input features of the linear layer.

output_features (`str`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## LinearNF4[[bitsandbytes.nn.LinearNF4]]

#### bitsandbytes.nn.LinearNF4[[bitsandbytes.nn.LinearNF4]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L596)

Implements the NF4 data type.

Constructs a quantization data type where each bin has equal area under a standard normal distribution N(0, 1) that
is normalized into the range [-1, 1].

For more information read the paper: QLoRA: Efficient Finetuning of Quantized LLMs (https://arxiv.org/abs/2305.14314)

Implementation of the NF4 data type in bitsandbytes can be found in the `create_normal_map` function in
the `functional.py` file: https://github.com/TimDettmers/bitsandbytes/blob/main/bitsandbytes/functional.py#L236.

__init__bitsandbytes.nn.LinearNF4.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L608[{"name": "input_features", "val": ""}, {"name": "output_features", "val": ""}, {"name": "bias", "val": " = True"}, {"name": "compute_dtype", "val": " = None"}, {"name": "compress_statistics", "val": " = True"}, {"name": "quant_storage", "val": " = torch.uint8"}, {"name": "device", "val": " = None"}]- **input_features** (`str`) --
  Number of input features of the linear layer.
- **output_features** (`str`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

**Parameters:**

input_features (`str`) : Number of input features of the linear layer.

output_features (`str`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## Params4bit[[bitsandbytes.nn.Params4bit]]

#### bitsandbytes.nn.Params4bit[[bitsandbytes.nn.Params4bit]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L212)

__init__bitsandbytes.nn.Params4bit.__init__[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]
Initialize self.  See help(type(self)) for accurate signature.

