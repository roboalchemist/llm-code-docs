# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/model_variant_stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.model_variant_stats

## Classes

### ModelVariantStats

```python  theme={"system"}
edgeimpulse_api.models.model_variant_stats.ModelVariantStats(
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

| Class variables              |                                                                            |
| ---------------------------- | -------------------------------------------------------------------------- |
| `Config`                     | ` `                                                                        |
| `accuracy`                   | `edgeimpulse_api.models.evaluate_result_value.EvaluateResultValue`         |
| `classification_labels`      | `List[pydantic.v1.types.StrictStr]`                                        |
| `confusion_matrix`           | `Dict[str, Dict[str, Dict[str, Any]]]`                                     |
| `learn_block_id`             | `pydantic.v1.types.StrictInt`                                              |
| `learn_block_type`           | `edgeimpulse_api.models.learn_block_type.LearnBlockType`                   |
| `model_type`                 | `edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum`          |
| `total_correct_window_count` | `edgeimpulse_api.models.evaluate_result_value.EvaluateResultValue \| None` |
| `total_window_count`         | `pydantic.v1.types.StrictInt \| None`                                      |
| `training_labels`            | `List[pydantic.v1.types.StrictStr]`                                        |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.model_variant_stats.ModelVariantStats.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.model_variant_stats.ModelVariantStats
```

Create an instance of ModelVariantStats from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.model_variant_stats.ModelVariantStats` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.model_variant_stats.ModelVariantStats.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.model_variant_stats.ModelVariantStats
```

Create an instance of ModelVariantStats from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.model_variant_stats.ModelVariantStats` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.model_variant_stats.ModelVariantStats.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.model_variant_stats.ModelVariantStats.to_json(
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
edgeimpulse_api.models.model_variant_stats.ModelVariantStats.to_str(
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