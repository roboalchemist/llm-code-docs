# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_data_explorer_settings_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_data_explorer_settings_response

## Classes

### GetDataExplorerSettingsResponse

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse(
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

| Class variables                           |                                       |
| ----------------------------------------- | ------------------------------------- |
| `Config`                                  | ` `                                   |
| `dimensionality_reduction_recommendation` | `pydantic.v1.types.StrictStr`         |
| `dimensionality_reduction_technique`      | `pydantic.v1.types.StrictStr \| None` |
| `error`                                   | `pydantic.v1.types.StrictStr \| None` |
| `impulse_id`                              | `pydantic.v1.types.StrictInt \| None` |
| `preset`                                  | `pydantic.v1.types.StrictStr \| None` |
| `success`                                 | `pydantic.v1.types.StrictBool`        |

***

**STATIC METHODS**

#### dimensionality\_reduction\_recommendation\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.dimensionality_reduction_recommendation_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### dimensionality\_reduction\_technique\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.dimensionality_reduction_technique_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse
```

Create an instance of GetDataExplorerSettingsResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse
```

Create an instance of GetDataExplorerSettingsResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse` |

#### preset\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.preset_validate_enum(
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
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.to_json(
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
edgeimpulse_api.models.get_data_explorer_settings_response.GetDataExplorerSettingsResponse.to_str(
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