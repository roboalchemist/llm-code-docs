# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/model/input_type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.model.input_type

## Classes

### AudioInput

```python  theme={"system"}
edgeimpulse.model.input_type.AudioInput(
	frequency_hz: float
)
```

| Parameters     |         |
| -------------- | ------- |
| `frequency_hz` | `float` |

| Bases           |
| --------------- |
| `builtins.dict` |

### ImageInput

```python  theme={"system"}
edgeimpulse.model.input_type.ImageInput(
	scaling_range: Literal['0..1', '0..255', 'torch'] = '0..1'
)
```

| Parameters      |                                               |
| --------------- | --------------------------------------------- |
| `scaling_range` | `Literal['0..1', '0..255', 'torch'] = '0..1'` |

| Bases           |
| --------------- |
| `builtins.dict` |

### OtherInput

```python  theme={"system"}
edgeimpulse.model.input_type.OtherInput(
	
)
```

| Bases           |
| --------------- |
| `builtins.dict` |

### TimeSeriesInput

```python  theme={"system"}
edgeimpulse.model.input_type.TimeSeriesInput(
	frequency_hz: float,
	windowlength_ms: int
)
```

| Parameters        |         |
| ----------------- | ------- |
| `frequency_hz`    | `float` |
| `windowlength_ms` | `int`   |

| Bases           |
| --------------- |
| `builtins.dict` |


Built with [Mintlify](https://mintlify.com).