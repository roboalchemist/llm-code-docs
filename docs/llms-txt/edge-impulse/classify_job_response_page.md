# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/classify_job_response_page.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.classify_job_response_page

## Classes

### ClassifyJobResponsePage

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage(
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

| Class variables |                                                                 |
| --------------- | --------------------------------------------------------------- |
| `Config`        | ` `                                                             |
| `error`         | `pydantic.v1.types.StrictStr \| None`                           |
| `predictions`   | `List[edgeimpulse_api.models.model_prediction.ModelPrediction]` |
| `result`        | `List[edgeimpulse_api.models.model_result.ModelResult]`         |
| `success`       | `pydantic.v1.types.StrictBool`                                  |
| `total_count`   | `pydantic.v1.types.StrictInt`                                   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage
```

Create an instance of ClassifyJobResponsePage from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage
```

Create an instance of ClassifyJobResponsePage from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage.to_json(
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
edgeimpulse_api.models.classify_job_response_page.ClassifyJobResponsePage.to_str(
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