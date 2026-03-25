# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/anomaly_config_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.anomaly_config_response

## Classes

### AnomalyConfigResponse

```python  theme={"system"}
edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse(
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

| Class variables             |                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------- |
| `Config`                    | ` `                                                                             |
| `axes`                      | `List[edgeimpulse_api.models.anomaly_config_axes_inner.AnomalyConfigAxesInner]` |
| `cluster_count`             | `pydantic.v1.types.StrictInt \| None`                                           |
| `dependencies`              | `edgeimpulse_api.models.dependency_data.DependencyData`                         |
| `error`                     | `pydantic.v1.types.StrictStr \| None`                                           |
| `minimum_confidence_rating` | `float`                                                                         |
| `name`                      | `pydantic.v1.types.StrictStr`                                                   |
| `selected_axes`             | `List[pydantic.v1.types.StrictInt]`                                             |
| `success`                   | `pydantic.v1.types.StrictBool`                                                  |
| `thresholds`                | `List[edgeimpulse_api.models.block_threshold.BlockThreshold]`                   |
| `trained`                   | `pydantic.v1.types.StrictBool`                                                  |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse
```

Create an instance of AnomalyConfigResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse
```

Create an instance of AnomalyConfigResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse.to_json(
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
edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse.to_str(
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