# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_label_noise_data_response_all_of_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_label_noise_data_response_all_of_data

## Classes

### GetLabelNoiseDataResponseAllOfData

```python  theme={"system"}
edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData(
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

| Class variables     |                                                                              |
| ------------------- | ---------------------------------------------------------------------------- |
| `Config`            | ` `                                                                          |
| `cosine_similarity` | `edgeimpulse_api.models.cosine_similarity_data.CosineSimilarityData \| None` |
| `cross_validation`  | `edgeimpulse_api.models.cross_validation_data.CrossValidationData \| None`   |
| `neighbors`         | `edgeimpulse_api.models.neighbors_data.NeighborsData \| None`                |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData
```

Create an instance of GetLabelNoiseDataResponseAllOfData from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData
```

Create an instance of GetLabelNoiseDataResponseAllOfData from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData.to_json(
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
edgeimpulse_api.models.get_label_noise_data_response_all_of_data.GetLabelNoiseDataResponseAllOfData.to_str(
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