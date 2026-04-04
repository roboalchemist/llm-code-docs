# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-utilities-schemas-serializers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# serializers

# `prefect.server.utilities.schemas.serializers`

## Functions

### `orjson_dumps` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/schemas/serializers.py#L10" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
orjson_dumps(v: Any) -> str
```

Utility for dumping a value to JSON using orjson.

orjson.dumps returns bytes, to match standard json.dumps we need to decode.

### `orjson_dumps_extra_compatible` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/utilities/schemas/serializers.py#L19" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
orjson_dumps_extra_compatible(v: Any) -> str
```

Utility for dumping a value to JSON using orjson, but allows for

1. non-string keys: this is helpful for situations like pandas dataframes,
   which can result in non-string keys
2. numpy types: for serializing numpy arrays

orjson.dumps returns bytes, to match standard json.dumps we need to decode.


Built with [Mintlify](https://mintlify.com).