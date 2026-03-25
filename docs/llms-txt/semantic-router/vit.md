# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/vit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.vit

## VitEncoder Objects

```python  theme={null}
class VitEncoder(DenseEncoder)
```

Encoder for Vision Transformer models.

This class provides functionality to encode images using a Vision Transformer
model via Hugging Face. It supports various image processing and model initialization
options.

#### \_\_init\_\_

```python  theme={null}
def __init__(**data)
```

Initialize the VitEncoder.

**Arguments**:

* `**data` (`dict`): Additional keyword arguments for the encoder.

#### \_\_call\_\_

```python  theme={null}
def __call__(imgs: List[Any], batch_size: int = 32) -> List[List[float]]
```

Encode a list of images into embeddings using the Vision Transformer model.

**Arguments**:

* `imgs` (`List[Any]`): The images to encode.
* `batch_size` (`int`): The batch size for encoding.

**Returns**:

`List[List[float]]`: The embeddings for the images.


Built with [Mintlify](https://mintlify.com).