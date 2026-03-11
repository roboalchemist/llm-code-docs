# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/latency_device.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.latency_device

## Classes

### LatencyDevice

```python  theme={"system"}
edgeimpulse_api.models.latency_device.LatencyDevice(
	**data: Any
)
```

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

| Parameters |       |
| ---------- | ----- |
| `**data`   | `Any` |

| Bases                              |
| ---------------------------------- |
| `pydantic.v1.main.BaseModel`       |
| `pydantic.v1.utils.Representation` |

| Class variables        |                                |
| ---------------------- | ------------------------------ |
| `Config`               | ` `                            |
| `float32_conv_latency` | `float`                        |
| `float32_latency`      | `float`                        |
| `help_text`            | `pydantic.v1.types.StrictStr`  |
| `int8_conv_latency`    | `float`                        |
| `int8_latency`         | `float`                        |
| `mcu`                  | `pydantic.v1.types.StrictStr`  |
| `name`                 | `pydantic.v1.types.StrictStr`  |
| `selected`             | `pydantic.v1.types.StrictBool` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.latency_device.LatencyDevice.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.latency_device.LatencyDevice
```

Create an instance of LatencyDevice from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                               |
| ----------------------------------------------------- |
| `edgeimpulse_api.models.latency_device.LatencyDevice` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.latency_device.LatencyDevice.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.latency_device.LatencyDevice
```

Create an instance of LatencyDevice from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                               |
| ----------------------------------------------------- |
| `edgeimpulse_api.models.latency_device.LatencyDevice` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.latency_device.LatencyDevice.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.latency_device.LatencyDevice.to_json(
	self,
	indent=None
) ‑> str
```

Returns the JSON representation of the model using alias

| Parameters    |     |
| ------------- | --- |
| `self`        | ` ` |
| `indent=None` | ` ` |

| Returns |
| ------- |
| `str`   |

#### to\_str

```python  theme={"system"}
edgeimpulse_api.models.latency_device.LatencyDevice.to_str(
	self
) ‑> str
```

Returns the string representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).