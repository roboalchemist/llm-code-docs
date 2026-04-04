# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/optimize_config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.optimize_config

## Classes

### OptimizeConfig

```python  theme={"system"}
edgeimpulse_api.models.optimize_config.OptimizeConfig(
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

| Class variables                  |                                                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `Config`                         | ` `                                                                                                                            |
| `accuracy_sem`                   | `float \| None`                                                                                                                |
| `compiler`                       | `List[pydantic.v1.types.StrictStr] \| None`                                                                                    |
| `disable_constraints`            | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `disable_deduplicate`            | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `early_stopping`                 | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `early_stopping_improvement_bar` | `float \| None`                                                                                                                |
| `early_stopping_window_size`     | `float \| None`                                                                                                                |
| `enable_sem`                     | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `import_project_metrics`         | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `import_resource_metrics`        | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `initial_trials`                 | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `latency_sem`                    | `float \| None`                                                                                                                |
| `max_maccs`                      | `float \| None`                                                                                                                |
| `max_total_training_time`        | `float \| None`                                                                                                                |
| `min_maccs`                      | `float \| None`                                                                                                                |
| `momf`                           | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `name`                           | `pydantic.v1.types.StrictStr \| None`                                                                                          |
| `notification_on_completion`     | `pydantic.v1.types.StrictBool \| None`                                                                                         |
| `num_import_project_metrics`     | `float \| None`                                                                                                                |
| `num_import_resource_metrics`    | `float \| None`                                                                                                                |
| `optimization_objectives`        | `List[edgeimpulse_api.models.optimize_config_optimization_objectives_inner.OptimizeConfigOptimizationObjectivesInner] \| None` |
| `optimization_precision`         | `pydantic.v1.types.StrictStr \| None`                                                                                          |
| `optimization_rounds`            | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `precision`                      | `List[pydantic.v1.types.StrictStr] \| None`                                                                                    |
| `raw_objectives`                 | `pydantic.v1.types.StrictStr \| None`                                                                                          |
| `search_space_source`            | `edgeimpulse_api.models.optimize_config_search_space_source.OptimizeConfigSearchSpaceSource \| None`                           |
| `search_space_template`          | `edgeimpulse_api.models.optimize_config_search_space_template.OptimizeConfigSearchSpaceTemplate \| None`                       |
| `space`                          | `List[edgeimpulse_api.models.tuner_space_impulse.TunerSpaceImpulse] \| None`                                                   |
| `target_device`                  | `edgeimpulse_api.models.optimize_config_target_device.OptimizeConfigTargetDevice`                                              |
| `target_latency`                 | `pydantic.v1.types.StrictInt`                                                                                                  |
| `training_cycles`                | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `trials_per_optimization_round`  | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `tuner_space_options`            | `Dict[str, List[pydantic.v1.types.StrictStr]] \| None`                                                                         |
| `tuning_algorithm`               | `pydantic.v1.types.StrictStr \| None`                                                                                          |
| `tuning_max_trials`              | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `tuning_workers`                 | `pydantic.v1.types.StrictInt \| None`                                                                                          |
| `verbose_logging`                | `pydantic.v1.types.StrictBool \| None`                                                                                         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.optimize_config.OptimizeConfig.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.optimize_config.OptimizeConfig
```

Create an instance of OptimizeConfig from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                 |
| ------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_config.OptimizeConfig` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.optimize_config.OptimizeConfig.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.optimize_config.OptimizeConfig
```

Create an instance of OptimizeConfig from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                 |
| ------------------------------------------------------- |
| `edgeimpulse_api.models.optimize_config.OptimizeConfig` |

#### optimization\_precision\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.optimize_config.OptimizeConfig.optimization_precision_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### tuning\_algorithm\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.optimize_config.OptimizeConfig.tuning_algorithm_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.optimize_config.OptimizeConfig.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.optimize_config.OptimizeConfig.to_json(
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
edgeimpulse_api.models.optimize_config.OptimizeConfig.to_str(
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