# Source: https://huggingface.co/docs/bitsandbytes/v0.49.0/reference/nn/linear8bit.md

# LLM.int8()
[LLM.int8()](https://hf.co/papers/2208.07339) is a quantization method that aims to make large language model inference more accessible without significant degradation. Unlike naive 8-bit quantization, which can result in loss of critical information and accuracy, LLM.int8() dynamically adapts to ensure sensitive components of the computation retain higher precision when needed. The key is to extract the outliers from the inputs and weights and multiply them in 16-bit. All other values are multiplied in 8-bit before being dequantized back to 16-bits. The outputs from the 16-bit and 8-bit multiplication are combined to produce the final output.

[Further Resources](../../explanations/resources#llm-int8)

## Linear8bitLt[[bitsandbytes.nn.Linear8bitLt]]

#### bitsandbytes.nn.Linear8bitLt[[bitsandbytes.nn.Linear8bitLt]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/nn/modules.py#L935)

This class is the base module for the [LLM.int8()](https://arxiv.org/abs/2208.07339) algorithm.
To read more about it, have a look at the paper.

In order to quantize a linear layer one should first load the original fp16 / bf16 weights into
the Linear8bitLt module, then call `int8_module.to("cuda")` to quantize the fp16 weights.

Example:

```python
import torch
import torch.nn as nn

import bitsandbytes as bnb
from bnb.nn import Linear8bitLt

fp16_model = nn.Sequential(
    nn.Linear(64, 64),
    nn.Linear(64, 64)
)

int8_model = nn.Sequential(
    Linear8bitLt(64, 64, has_fp16_weights=False),
    Linear8bitLt(64, 64, has_fp16_weights=False)
)

int8_model.load_state_dict(fp16_model.state_dict())
int8_model = int8_model.to(0) # Quantization happens here
```

__init__bitsandbytes.nn.Linear8bitLt.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/nn/modules.py#L967[{"name": "input_features", "val": ": int"}, {"name": "output_features", "val": ": int"}, {"name": "bias", "val": " = True"}, {"name": "has_fp16_weights", "val": " = True"}, {"name": "threshold", "val": " = 0.0"}, {"name": "index", "val": " = None"}, {"name": "device", "val": " = None"}]- **input_features** (`int`) --
  Number of input features of the linear layer.
- **output_features** (`int`) --
  Number of output features of the linear layer.
- **bias** (`bool`, defaults to `True`) --
  Whether the linear class uses the bias term as well.0

Initialize Linear8bitLt class.

**Parameters:**

input_features (`int`) : Number of input features of the linear layer.

output_features (`int`) : Number of output features of the linear layer.

bias (`bool`, defaults to `True`) : Whether the linear class uses the bias term as well.

## Int8Params[[bitsandbytes.nn.Int8Params]]

#### bitsandbytes.nn.Int8Params[[bitsandbytes.nn.Int8Params]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.0/bitsandbytes/nn/modules.py#L637)

__init__bitsandbytes.nn.Int8Params.__init__[{"name": "*args", "val": ""}, {"name": "**kwargs", "val": ""}]
Initialize self.  See help(type(self)) for accurate signature.

