# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_pretrained_model_response_all_of_model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_pretrained_model_response_all_of_model

## Classes

### GetPretrainedModelResponseAllOfModel

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel(
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

| Class variables      |                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`             | ` `                                                                                                                                      |
| `file_name`          | `pydantic.v1.types.StrictStr`                                                                                                            |
| `inputs`             | `List[edgeimpulse_api.models.pretrained_model_tensor.PretrainedModelTensor]`                                                             |
| `outputs`            | `List[edgeimpulse_api.models.pretrained_model_tensor.PretrainedModelTensor]`                                                             |
| `profile_info`       | `edgeimpulse_api.models.get_pretrained_model_response_all_of_model_profile_info.GetPretrainedModelResponseAllOfModelProfileInfo \| None` |
| `profile_job_failed` | `pydantic.v1.types.StrictBool \| None`                                                                                                   |
| `profile_job_id`     | `pydantic.v1.types.StrictInt \| None`                                                                                                    |
| `supports_tf_lite`   | `pydantic.v1.types.StrictBool \| None`                                                                                                   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel
```

Create an instance of GetPretrainedModelResponseAllOfModel from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                  |
| -------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel
```

Create an instance of GetPretrainedModelResponseAllOfModel from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                  |
| -------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel.to_json(
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
edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel.to_str(
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