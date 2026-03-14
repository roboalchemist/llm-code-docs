# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_metrics_response_all_of_metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_metrics_response_all_of_metrics

## Classes

### OrganizationMetricsResponseAllOfMetrics

```python  theme={"system"}
edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics(
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

| Class variables                        |                               |
| -------------------------------------- | ----------------------------- |
| `Config`                               | ` `                           |
| `cpu_compute_time_current_contract`    | `float`                       |
| `gpu_compute_time_current_contract`    | `float`                       |
| `jobs_compute_time_current_year`       | `float`                       |
| `jobs_compute_time_current_year_since` | `datetime.datetime`           |
| `project_count`                        | `pydantic.v1.types.StrictInt` |
| `total_jobs_compute_time`              | `float`                       |
| `total_storage`                        | `float`                       |
| `user_count`                           | `pydantic.v1.types.StrictInt` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics
```

Create an instance of OrganizationMetricsResponseAllOfMetrics from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics
```

Create an instance of OrganizationMetricsResponseAllOfMetrics from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics.to_json(
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
edgeimpulse_api.models.organization_metrics_response_all_of_metrics.OrganizationMetricsResponseAllOfMetrics.to_str(
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