# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/model_prediction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.model_prediction

## Classes

### ModelPrediction

```python  theme={"system"}
edgeimpulse_api.models.model_prediction.ModelPrediction(
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

| Class variables         |                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------- |
| `Config`                | ` `                                                                                 |
| `anomaly_scores`        | `List[List[float]] \| None`                                                         |
| `bounding_boxes`        | `List[edgeimpulse_api.models.bounding_box_with_score.BoundingBoxWithScore] \| None` |
| `end_ms`                | `float`                                                                             |
| `f1_score`              | `float \| None`                                                                     |
| `label`                 | `pydantic.v1.types.StrictStr \| None`                                               |
| `label_map_predictions` | `Dict[str, pydantic.v1.types.StrictStr] \| None`                                    |
| `prediction`            | `pydantic.v1.types.StrictStr`                                                       |
| `prediction_correct`    | `pydantic.v1.types.StrictBool \| None`                                              |
| `sample_id`             | `pydantic.v1.types.StrictInt`                                                       |
| `start_ms`              | `float`                                                                             |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.model_prediction.ModelPrediction.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.model_prediction.ModelPrediction
```

Create an instance of ModelPrediction from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                   |
| --------------------------------------------------------- |
| `edgeimpulse_api.models.model_prediction.ModelPrediction` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.model_prediction.ModelPrediction.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.model_prediction.ModelPrediction
```

Create an instance of ModelPrediction from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                   |
| --------------------------------------------------------- |
| `edgeimpulse_api.models.model_prediction.ModelPrediction` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.model_prediction.ModelPrediction.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.model_prediction.ModelPrediction.to_json(
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
edgeimpulse_api.models.model_prediction.ModelPrediction.to_str(
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