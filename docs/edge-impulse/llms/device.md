# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/device.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.device

## Classes

### Device

```python  theme={"system"}
edgeimpulse_api.models.device.Device(
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

| Class variables               |                                                                            |
| ----------------------------- | -------------------------------------------------------------------------- |
| `Config`                      | ` `                                                                        |
| `created`                     | `datetime.datetime`                                                        |
| `device_id`                   | `pydantic.v1.types.StrictStr`                                              |
| `device_type`                 | `pydantic.v1.types.StrictStr`                                              |
| `id`                          | `pydantic.v1.types.StrictInt`                                              |
| `inference_info`              | `edgeimpulse_api.models.device_inference_info.DeviceInferenceInfo \| None` |
| `last_seen`                   | `datetime.datetime`                                                        |
| `name`                        | `pydantic.v1.types.StrictStr`                                              |
| `remote_mgmt_connected`       | `pydantic.v1.types.StrictBool`                                             |
| `remote_mgmt_host`            | `pydantic.v1.types.StrictStr \| None`                                      |
| `remote_mgmt_mode`            | `pydantic.v1.types.StrictStr`                                              |
| `sensors`                     | `List[edgeimpulse_api.models.device_sensors_inner.DeviceSensorsInner]`     |
| `supports_snapshot_streaming` | `pydantic.v1.types.StrictBool`                                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.device.Device.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.device.Device
```

Create an instance of Device from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                |
| -------------------------------------- |
| `edgeimpulse_api.models.device.Device` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.device.Device.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.device.Device
```

Create an instance of Device from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                |
| -------------------------------------- |
| `edgeimpulse_api.models.device.Device` |

#### remote\_mgmt\_mode\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.device.Device.remote_mgmt_mode_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.device.Device.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.device.Device.to_json(
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
edgeimpulse_api.models.device.Device.to_str(
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