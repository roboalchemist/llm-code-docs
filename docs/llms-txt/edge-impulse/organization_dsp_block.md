# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_dsp_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_dsp_block

## Classes

### OrganizationDspBlock

```python  theme={"system"}
edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock(
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

| Class variables                            |                                                                               |
| ------------------------------------------ | ----------------------------------------------------------------------------- |
| `Config`                                   | ` `                                                                           |
| `created`                                  | `datetime.datetime`                                                           |
| `created_by_user`                          | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `description`                              | `pydantic.v1.types.StrictStr`                                                 |
| `docker_container`                         | `pydantic.v1.types.StrictStr`                                                 |
| `docker_container_managed_by_edge_impulse` | `pydantic.v1.types.StrictBool`                                                |
| `error`                                    | `pydantic.v1.types.StrictStr \| None`                                         |
| `id`                                       | `pydantic.v1.types.StrictInt`                                                 |
| `is_connected`                             | `pydantic.v1.types.StrictBool`                                                |
| `last_updated`                             | `datetime.datetime \| None`                                                   |
| `last_updated_by_user`                     | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `limits_cpu`                               | `float \| None`                                                               |
| `limits_memory`                            | `pydantic.v1.types.StrictInt \| None`                                         |
| `name`                                     | `pydantic.v1.types.StrictStr`                                                 |
| `port`                                     | `pydantic.v1.types.StrictInt`                                                 |
| `requests_cpu`                             | `float \| None`                                                               |
| `requests_memory`                          | `pydantic.v1.types.StrictInt \| None`                                         |
| `source_code_available`                    | `pydantic.v1.types.StrictBool`                                                |
| `source_code_download_staff_only`          | `pydantic.v1.types.StrictBool`                                                |
| `user_id`                                  | `pydantic.v1.types.StrictInt \| None`                                         |
| `user_name`                                | `pydantic.v1.types.StrictStr \| None`                                         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock
```

Create an instance of OrganizationDspBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock
```

Create an instance of OrganizationDspBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                              |
| -------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock.to_json(
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
edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock.to_str(
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