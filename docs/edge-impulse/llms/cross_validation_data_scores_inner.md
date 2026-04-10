# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/cross_validation_data_scores_inner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.cross_validation_data_scores_inner

## Classes

### CrossValidationDataScoresInner

```python  theme={"system"}
edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner(
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

| Class variables |                                                |
| --------------- | ---------------------------------------------- |
| `Config`        | ` `                                            |
| `id`            | `pydantic.v1.types.StrictInt`                  |
| `label`         | `pydantic.v1.types.StrictInt`                  |
| `probability`   | `float`                                        |
| `sample`        | `edgeimpulse_api.models.sample.Sample \| None` |
| `score`         | `float`                                        |
| `window_end`    | `pydantic.v1.types.StrictInt`                  |
| `window_start`  | `pydantic.v1.types.StrictInt`                  |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner
```

Create an instance of CrossValidationDataScoresInner from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner
```

Create an instance of CrossValidationDataScoresInner from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner.to_json(
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
edgeimpulse_api.models.cross_validation_data_scores_inner.CrossValidationDataScoresInner.to_str(
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