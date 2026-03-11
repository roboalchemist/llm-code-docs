# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_data_explorer_features_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_data_explorer_features_response

## Classes

### GetDataExplorerFeaturesResponse

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse(
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

| Class variables |                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                                                                     |
| `data`          | `List[edgeimpulse_api.models.get_data_explorer_features_response_all_of_data.GetDataExplorerFeaturesResponseAllOfData]` |
| `error`         | `pydantic.v1.types.StrictStr \| None`                                                                                   |
| `has_features`  | `pydantic.v1.types.StrictBool`                                                                                          |
| `input_block`   | `edgeimpulse_api.models.impulse_input_block.ImpulseInputBlock \| None`                                                  |
| `success`       | `pydantic.v1.types.StrictBool`                                                                                          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse
```

Create an instance of GetDataExplorerFeaturesResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse
```

Create an instance of GetDataExplorerFeaturesResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse.to_json(
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
edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse.to_str(
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