# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/project_data_axes_summary_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.project_data_axes_summary_response

## Classes

### ProjectDataAxesSummaryResponse

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse(
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

| Class variables     |                                          |
| ------------------- | ---------------------------------------- |
| `Config`            | ` `                                      |
| `data_axis_summary` | `Dict[str, pydantic.v1.types.StrictInt]` |
| `error`             | `pydantic.v1.types.StrictStr \| None`    |
| `success`           | `pydantic.v1.types.StrictBool`           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse
```

Create an instance of ProjectDataAxesSummaryResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse
```

Create an instance of ProjectDataAxesSummaryResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse.to_json(
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
edgeimpulse_api.models.project_data_axes_summary_response.ProjectDataAxesSummaryResponse.to_str(
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