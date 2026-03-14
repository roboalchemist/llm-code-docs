# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_pretrained_model_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_pretrained_model_response

## Classes

### GetPretrainedModelResponse

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse(
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

| Class variables            |                                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `Config`                   | ` `                                                                                                                       |
| `available_model_types`    | `List[edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum]`                                                   |
| `error`                    | `pydantic.v1.types.StrictStr \| None`                                                                                     |
| `model`                    | `edgeimpulse_api.models.get_pretrained_model_response_all_of_model.GetPretrainedModelResponseAllOfModel \| None`          |
| `model_info`               | `edgeimpulse_api.models.get_pretrained_model_response_all_of_model_info.GetPretrainedModelResponseAllOfModelInfo \| None` |
| `specific_device_selected` | `pydantic.v1.types.StrictBool`                                                                                            |
| `success`                  | `pydantic.v1.types.StrictBool`                                                                                            |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse
```

Create an instance of GetPretrainedModelResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse
```

Create an instance of GetPretrainedModelResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse.to_json(
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
edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse.to_str(
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