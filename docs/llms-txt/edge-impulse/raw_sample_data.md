# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/raw_sample_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.raw_sample_data

## Classes

### RawSampleData

```python  theme={"system"}
edgeimpulse_api.models.raw_sample_data.RawSampleData(
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

| Class variables        |                                                              |
| ---------------------- | ------------------------------------------------------------ |
| `Config`               | ` `                                                          |
| `payload`              | `edgeimpulse_api.models.raw_sample_payload.RawSamplePayload` |
| `sample`               | `edgeimpulse_api.models.sample.Sample`                       |
| `total_payload_length` | `pydantic.v1.types.StrictInt`                                |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.raw_sample_data.RawSampleData.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.raw_sample_data.RawSampleData
```

Create an instance of RawSampleData from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                |
| ------------------------------------------------------ |
| `edgeimpulse_api.models.raw_sample_data.RawSampleData` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.raw_sample_data.RawSampleData.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.raw_sample_data.RawSampleData
```

Create an instance of RawSampleData from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                |
| ------------------------------------------------------ |
| `edgeimpulse_api.models.raw_sample_data.RawSampleData` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.raw_sample_data.RawSampleData.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.raw_sample_data.RawSampleData.to_json(
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
edgeimpulse_api.models.raw_sample_data.RawSampleData.to_str(
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