# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/object_detection_auto_label_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.object_detection_auto_label_response

## Classes

### ObjectDetectionAutoLabelResponse

```python  theme={"system"}
edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse(
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

| Class variables |                                                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                                                                             |
| `all_labels`    | `List[pydantic.v1.types.StrictStr]`                                                                                             |
| `error`         | `pydantic.v1.types.StrictStr \| None`                                                                                           |
| `results`       | `List[edgeimpulse_api.models.object_detection_auto_label_response_all_of_results.ObjectDetectionAutoLabelResponseAllOfResults]` |
| `success`       | `pydantic.v1.types.StrictBool`                                                                                                  |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse
```

Create an instance of ObjectDetectionAutoLabelResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                        |
| ---------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse
```

Create an instance of ObjectDetectionAutoLabelResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                        |
| ---------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse.to_json(
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
edgeimpulse_api.models.object_detection_auto_label_response.ObjectDetectionAutoLabelResponse.to_str(
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