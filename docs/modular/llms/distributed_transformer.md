# DistributedTransformer {#max.nn.transformer.distributed_transformer.DistributedTransformer}

## `DistributedTransformer`

> class max.nn.transformer.distributed_transformer.DistributedTransformer(dim, n_heads, layers, norm, output, embedding, kv_params, devices, rope, return_logits=ReturnLogits.LAST_TOKEN, use_subgraphs=False, subgraph_layer_groups=None, logits_scaling=1.0)

Transformer model consisting for TransformerBlock layers.

### Parameters:

- **dim** ([int](https://docs.python.org/3/library/functions.html#int))
- **n_heads** ([int](https://docs.python.org/3/library/functions.html#int))
- **layers** ([list](https://docs.python.org/3/library/stdtypes.html#list)[ShardableCallable](#max.nn.transformer.distributed_transformer.ShardableCallable))
- **norm** ([ShardableCallable](#max.nn.transformer.distributed_transformer.ShardableCallable))
- **output** ([ColumnParallelLinear](/max/api/python/nn/linear#max.nn.linear.ColumnParallelLinear))
- **embedding** ([vocab_parallel_embedding](/max/api/python/nn/embedding#max.nn.embedding.VocabParallelEmbedding))
- **kv_params** ([KVCacheParams](/max/api/python/nn/kv_cache/cache_params#max.nn.kv_cache.cache_params.KVCacheParams))
- **devices** ([list](https://docs.python.org/3/library/stdtypes.html#list)[DeviceRef](/max/api/python/graph/ops#max.graph.ops.DeviceRef))
- **rope** ([RotaryEmbedding](/max/api/python/nn/rotary_embedding#max.nn.rotary_embedding.RotaryEmbedding))
- **return_logits** ([ReturnLogits](/max/api/python/nn/transformer/transformer#max.nn.transformer.transformer.ReturnLogits))
- **use_subgraphs** ([bool](https://docs.python.org/3/library/functions.html#bool))
- **subgraph_layer_groups** ([list](https://docs.python.org/3/library/stdtypes.html#list)[list](https://docs.python.org/3/library/stdtypes.html#list)[[int](https://docs.python.org/3/library/functions.html#int)])
- **logits_scaling** ([float](https://docs.python.org/3/library/functions.html#float))

## `DistributedTransformerBlock`

> class max.nn.transformer.distributed_transformer.DistributedTransformerBlock(attention, mlp, attention_norm, mlp_norm, devices, distributed_gemm_config=None)

Stack of Attention, FeedForward, and RMSNorm layers.

### Parameters:

- **attention** ([Module](/max/api/python/nn/layer#max.nn.layer.Module))
- **mlp** ([ShardableCallable](#max.nn.transformer.distributed_transformer.ShardableCallable))
- **attention_norm** ([ShardableCallable](#max.nn.transformer.distributed_transformer.ShardableCallable))
- **mlp_norm** ([ShardableCallable](#max.nn.transformer.distributed_transformer.ShardableCallable))
- **devices** ([list](https://docs.python.org/3/library/stdtypes.html#list)[DeviceRef](/max/api/python/graph/ops#max.graph.ops.DeviceRef))
- **distributed_gemm_config** ([DistributedGemmConfig](/max/api/python/nn/linear#max.nn.linear.DistributedGemmConfig) | None)

## `ShardableCallable`

> class max.nn.transformer.distributed_transformer.ShardableCallable(*args, **kwargs)

## `distribute_value()`

> max.nn.transformer.distributed_transformer.distribute_value(v, devices)

### Parameters:

- **v** ([TensorValue](/max/api/python/graph/TensorValue#max.graph.TensorValue))
- **devices** ([list](https://docs.python.org/3/library/stdtypes.html#list)[DeviceRef](/max/api/python/graph/ops#max.graph.ops.DeviceRef))

### Return type:

- [list](https://docs.python.org/3/library/stdtypes.html#list)[TensorValue](/max/api/python/graph/TensorValue#max.graph.TensorValue)

## `forward_sharded_layers()`

> max.nn.transformer.distributed_transformer.forward_sharded_layers(layers, xs)

Forward pass through sharded layers.

### Parameters:

- **layers** ([Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[ShardableCallable](#max.nn.transformer.distributed_transformer.ShardableCallable)[[[TensorValue](/max/api/python/graph/TensorValue#max.graph.TensorValue)], TensorValue]]
- **xs** ([Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[TensorValue])

### Returns:

- List of output tensors from each layer

### Raises:

- **AssertionError** - If the number of layers and input tensors don't match

### Return type:

- [list](https://docs.python.org/3/library/stdtypes.html#list)[TensorValue](/max/api/python/graph/TensorValue#max.graph.TensorValue)

## `take()`

> max.nn.transformer.distributed_transformer.take(it, n)

Return the next _n_ items from _it_ as a list.

### Parameters:

- **it** ([Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[Value](/max/api/python/graph/Value#max.graph.Value)[\[Any\]](https://docs.python.org/3/library/typing.html#typing.Any))
- **n** ([int](https://docs.python.org/3/library/functions.html#int))

### Return type:

- [list](https://docs.python.org/3/library/stdtypes.html#list)[Value](/max/api/python/graph/Value#max.graph.Value)[\[Any\]](https://docs.python.org/3/library/typing.html#typing.Any)