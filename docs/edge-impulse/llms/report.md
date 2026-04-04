# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/report.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.report

## Classes

### Report

```python  theme={"system"}
edgeimpulse_api.models.report.Report(
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

| Class variables           |                                                                               |
| ------------------------- | ----------------------------------------------------------------------------- |
| `Config`                  | ` `                                                                           |
| `created`                 | `datetime.datetime`                                                           |
| `created_by_user`         | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `download_link`           | `pydantic.v1.types.StrictStr \| None`                                         |
| `id`                      | `pydantic.v1.types.StrictInt`                                                 |
| `job_finished`            | `pydantic.v1.types.StrictBool`                                                |
| `job_finished_successful` | `pydantic.v1.types.StrictBool`                                                |
| `job_id`                  | `pydantic.v1.types.StrictInt`                                                 |
| `report_end_date`         | `datetime.datetime`                                                           |
| `report_start_date`       | `datetime.datetime`                                                           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.report.Report.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.report.Report
```

Create an instance of Report from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                |
| -------------------------------------- |
| `edgeimpulse_api.models.report.Report` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.report.Report.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.report.Report
```

Create an instance of Report from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                |
| -------------------------------------- |
| `edgeimpulse_api.models.report.Report` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.report.Report.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.report.Report.to_json(
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
edgeimpulse_api.models.report.Report.to_str(
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