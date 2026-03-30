# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/project_data_axes_summary_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.project_data_axes_summary_response_all_of

## Classes

### ProjectDataAxesSummaryResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf(
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

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf
```

Create an instance of ProjectDataAxesSummaryResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                |
| ------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf
```

Create an instance of ProjectDataAxesSummaryResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                |
| ------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf.to_json(
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
edgeimpulse_api.models.project_data_axes_summary_response_all_of.ProjectDataAxesSummaryResponseAllOf.to_str(
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