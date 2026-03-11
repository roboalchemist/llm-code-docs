# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_update_pipeline_body.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_update_pipeline_body

## Classes

### OrganizationUpdatePipelineBody

```python  theme={"system"}
edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody(
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

| Class variables        |                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------- |
| `Config`               | ` `                                                                                |
| `archived`             | `pydantic.v1.types.StrictBool \| None`                                             |
| `dataset`              | `pydantic.v1.types.StrictStr \| None`                                              |
| `description`          | `pydantic.v1.types.StrictStr`                                                      |
| `email_recipient_uids` | `List[pydantic.v1.types.StrictInt]`                                                |
| `interval_str`         | `pydantic.v1.types.StrictStr \| None`                                              |
| `name`                 | `pydantic.v1.types.StrictStr`                                                      |
| `notification_webhook` | `pydantic.v1.types.StrictStr \| None`                                              |
| `project_id`           | `pydantic.v1.types.StrictInt \| None`                                              |
| `steps`                | `List[edgeimpulse_api.models.organization_pipeline_step.OrganizationPipelineStep]` |
| `when_to_email`        | `pydantic.v1.types.StrictStr`                                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody
```

Create an instance of OrganizationUpdatePipelineBody from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                   |
| ----------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody
```

Create an instance of OrganizationUpdatePipelineBody from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                   |
| ----------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody` |

#### when\_to\_email\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody.when_to_email_validate_enum(
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
edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody.to_json(
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
edgeimpulse_api.models.organization_update_pipeline_body.OrganizationUpdatePipelineBody.to_str(
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