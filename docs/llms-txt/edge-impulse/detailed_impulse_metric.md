# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/detailed_impulse_metric.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.detailed_impulse_metric

## Classes

### DetailedImpulseMetric

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric(
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

| Class variables     |                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| `Config`            | ` `                                                                                                        |
| `category`          | `edgeimpulse_api.models.detailed_impulse_metric_category.DetailedImpulseMetricCategory`                    |
| `description`       | `pydantic.v1.types.StrictStr`                                                                              |
| `filtering_type`    | `edgeimpulse_api.models.detailed_impulse_metric_filtering_type.DetailedImpulseMetricFilteringType \| None` |
| `name`              | `pydantic.v1.types.StrictStr`                                                                              |
| `title`             | `pydantic.v1.types.StrictStr \| None`                                                                      |
| `type`              | `pydantic.v1.types.StrictStr`                                                                              |
| `value`             | `edgeimpulse_api.models.detailed_impulse_metric_value.DetailedImpulseMetricValue`                          |
| `value_for_sorting` | `pydantic.v1.types.StrictInt \| None`                                                                      |
| `value_hint`        | `pydantic.v1.types.StrictStr \| None`                                                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric
```

Create an instance of DetailedImpulseMetric from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric
```

Create an instance of DetailedImpulseMetric from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric` |

#### type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric.type_validate_enum(
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
edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric.to_json(
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
edgeimpulse_api.models.detailed_impulse_metric.DetailedImpulseMetric.to_str(
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