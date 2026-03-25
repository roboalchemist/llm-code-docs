# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/detailed_impulse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.detailed_impulse

## Classes

### DetailedImpulse

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse.DetailedImpulse(
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

| Class variables                 |                                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                        | ` `                                                                                                                                |
| `complete`                      | `pydantic.v1.types.StrictBool`                                                                                                     |
| `configured`                    | `pydantic.v1.types.StrictBool`                                                                                                     |
| `created_by_user`               | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None`                                                      |
| `created_from_tuner_trial_id`   | `float \| None`                                                                                                                    |
| `dsp_block_configs`             | `List[edgeimpulse_api.models.detailed_impulse_dsp_block_configs_inner.DetailedImpulseDspBlockConfigsInner]`                        |
| `impulse`                       | `edgeimpulse_api.models.impulse.Impulse`                                                                                           |
| `is_stale`                      | `pydantic.v1.types.StrictBool`                                                                                                     |
| `learn_block_anomaly_configs`   | `List[edgeimpulse_api.models.detailed_impulse_learn_block_anomaly_configs_inner.DetailedImpulseLearnBlockAnomalyConfigsInner]`     |
| `learn_block_keras_configs`     | `List[edgeimpulse_api.models.detailed_impulse_learn_block_keras_configs_inner.DetailedImpulseLearnBlockKerasConfigsInner]`         |
| `metrics`                       | `List[edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric]`                                                       |
| `post_processing_block_configs` | `List[edgeimpulse_api.models.detailed_impulse_post_processing_block_configs_inner.DetailedImpulsePostProcessingBlockConfigsInner]` |
| `pretrained_model_info`         | `edgeimpulse_api.models.detailed_impulse_pretrained_model_info.DetailedImpulsePretrainedModelInfo \| None`                         |
| `tags`                          | `List[pydantic.v1.types.StrictStr]`                                                                                                |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse.DetailedImpulse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.detailed_impulse.DetailedImpulse
```

Create an instance of DetailedImpulse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                   |
| --------------------------------------------------------- |
| `edgeimpulse_api.models.detailed_impulse.DetailedImpulse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse.DetailedImpulse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.detailed_impulse.DetailedImpulse
```

Create an instance of DetailedImpulse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                   |
| --------------------------------------------------------- |
| `edgeimpulse_api.models.detailed_impulse.DetailedImpulse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse.DetailedImpulse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse.DetailedImpulse.to_json(
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
edgeimpulse_api.models.detailed_impulse.DetailedImpulse.to_str(
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