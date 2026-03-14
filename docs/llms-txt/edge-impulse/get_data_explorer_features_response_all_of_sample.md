# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_data_explorer_features_response_all_of_sample.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample

## Classes

### GetDataExplorerFeaturesResponseAllOfSample

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample(
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

| Class variables |                               |
| --------------- | ----------------------------- |
| `Config`        | ` `                           |
| `category`      | `pydantic.v1.types.StrictStr` |
| `end_ms`        | `float`                       |
| `id`            | `float`                       |
| `name`          | `pydantic.v1.types.StrictStr` |
| `start_ms`      | `float`                       |

***

**STATIC METHODS**

#### category\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample.category_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample
```

Create an instance of GetDataExplorerFeaturesResponseAllOfSample from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample
```

Create an instance of GetDataExplorerFeaturesResponseAllOfSample from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample.to_json(
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
edgeimpulse_api.models.get_data_explorer_features_response_all_of_sample.GetDataExplorerFeaturesResponseAllOfSample.to_str(
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