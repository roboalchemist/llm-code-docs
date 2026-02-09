# Source: https://huggingface.co/docs/bitsandbytes/v0.49.1/reference/nn/embeddings.md

# Embedding

The embedding class is used to store and retrieve word embeddings from their indices. There are two types of embeddings in bitsandbytes, the standard PyTorch `Embedding` class and the `StableEmbedding` class.

The `StableEmbedding` class was introduced in the [8-bit Optimizers via Block-wise Quantization](https://hf.co/papers/2110.02861) paper to reduce gradient variance as a result of the non-uniform distribution of input tokens. This class is designed to support quantization.

## Embedding[[bitsandbytes.nn.Embedding]]

#### bitsandbytes.nn.Embedding[[bitsandbytes.nn.Embedding]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L133)

Embedding class to store and retrieve word embeddings from their indices.

__init__bitsandbytes.nn.Embedding.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L138[{"name": "num_embeddings", "val": ": int"}, {"name": "embedding_dim", "val": ": int"}, {"name": "padding_idx", "val": ": typing.Optional[int] = None"}, {"name": "max_norm", "val": ": typing.Optional[float] = None"}, {"name": "norm_type", "val": ": float = 2.0"}, {"name": "scale_grad_by_freq", "val": ": bool = False"}, {"name": "sparse", "val": ": bool = False"}, {"name": "_weight", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "device", "val": ": typing.Optional[torch.device] = None"}]- **num_embeddings** (`int`) --
  The number of unique embeddings (vocabulary size).
- **embedding_dim** (`int`) --
  The dimensionality of the embedding.
- **padding_idx** (`Optional[int]`) --
  Pads the output with zeros at the given index.
- **max_norm** (`Optional[float]`) --
  Renormalizes embeddings to have a maximum L2 norm.
- **norm_type** (`float`, defaults to `2.0`) --
  The p-norm to compute for the `max_norm` option.
- **scale_grad_by_freq** (`bool`, defaults to `False`) --
  Scale gradient by frequency during backpropagation.
- **sparse** (`bool`, defaults to `False`) --
  Computes dense gradients. Set to `True` to compute sparse gradients instead.
- **_weight** (`Optional[Tensor]`) --
  Pretrained embeddings.0

**Parameters:**

num_embeddings (`int`) : The number of unique embeddings (vocabulary size).

embedding_dim (`int`) : The dimensionality of the embedding.

padding_idx (`Optional[int]`) : Pads the output with zeros at the given index.

max_norm (`Optional[float]`) : Renormalizes embeddings to have a maximum L2 norm.

norm_type (`float`, defaults to `2.0`) : The p-norm to compute for the `max_norm` option.

scale_grad_by_freq (`bool`, defaults to `False`) : Scale gradient by frequency during backpropagation.

sparse (`bool`, defaults to `False`) : Computes dense gradients. Set to `True` to compute sparse gradients instead.

_weight (`Optional[Tensor]`) : Pretrained embeddings.

## StableEmbedding[[bitsandbytes.nn.StableEmbedding]]

#### bitsandbytes.nn.StableEmbedding[[bitsandbytes.nn.StableEmbedding]]

[Source](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L27)

Custom embedding layer designed to improve stability during training for NLP tasks by using 32-bit optimizer states. It is designed to reduce gradient variations that can result from quantization. This embedding layer is initialized with Xavier uniform initialization followed by layer normalization.

Example:

```
# Initialize StableEmbedding layer with vocabulary size 1000, embedding dimension 300
embedding_layer = StableEmbedding(num_embeddings=1000, embedding_dim=300)

# Reset embedding parameters
embedding_layer.reset_parameters()

# Perform a forward pass with input tensor
input_tensor = torch.tensor([1, 2, 3])
output_embedding = embedding_layer(input_tensor)
```

Methods:
reset_parameters(): Reset embedding parameters using Xavier uniform initialization.
forward(input: Tensor) -> Tensor: Forward pass through the stable embedding layer.

__init__bitsandbytes.nn.StableEmbedding.__init__https://github.com/bitsandbytes-foundation/bitsandbytes/blob/v0.49.1/bitsandbytes/nn/modules.py#L53[{"name": "num_embeddings", "val": ": int"}, {"name": "embedding_dim", "val": ": int"}, {"name": "padding_idx", "val": ": typing.Optional[int] = None"}, {"name": "max_norm", "val": ": typing.Optional[float] = None"}, {"name": "norm_type", "val": ": float = 2.0"}, {"name": "scale_grad_by_freq", "val": ": bool = False"}, {"name": "sparse", "val": ": bool = False"}, {"name": "_weight", "val": ": typing.Optional[torch.Tensor] = None"}, {"name": "device", "val": " = None"}, {"name": "dtype", "val": " = None"}]- **num_embeddings** (`int`) --
  The number of unique embeddings (vocabulary size).
- **embedding_dim** (`int`) --
  The dimensionality of the embedding.
- **padding_idx** (`Optional[int]`) --
  Pads the output with zeros at the given index.
- **max_norm** (`Optional[float]`) --
  Renormalizes embeddings to have a maximum L2 norm.
- **norm_type** (`float`, defaults to `2.0`) --
  The p-norm to compute for the `max_norm` option.
- **scale_grad_by_freq** (`bool`, defaults to `False`) --
  Scale gradient by frequency during backpropagation.
- **sparse** (`bool`, defaults to `False`) --
  Computes dense gradients. Set to `True` to compute sparse gradients instead.
- **_weight** (`Optional[Tensor]`) --
  Pretrained embeddings.0

**Parameters:**

norm (`torch.nn.LayerNorm`) : Layer normalization applied after the embedding.

