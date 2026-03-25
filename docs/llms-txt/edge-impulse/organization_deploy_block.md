# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_deploy_block.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_deploy_block

## Classes

### OrganizationDeployBlock

```python  theme={"system"}
edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock(
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
| `category`                                 | `pydantic.v1.types.StrictStr`                                                 |
| `cli_arguments`                            | `pydantic.v1.types.StrictStr`                                                 |
| `created`                                  | `datetime.datetime`                                                           |
| `created_by_user`                          | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `description`                              | `pydantic.v1.types.StrictStr`                                                 |
| `docker_container`                         | `pydantic.v1.types.StrictStr`                                                 |
| `docker_container_managed_by_edge_impulse` | `pydantic.v1.types.StrictBool`                                                |
| `id`                                       | `pydantic.v1.types.StrictInt`                                                 |
| `integrate_url`                            | `pydantic.v1.types.StrictStr \| None`                                         |
| `last_updated`                             | `datetime.datetime \| None`                                                   |
| `last_updated_by_user`                     | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `limits_cpu`                               | `float \| None`                                                               |
| `limits_memory`                            | `pydantic.v1.types.StrictInt \| None`                                         |
| `mount_learn_block`                        | `pydantic.v1.types.StrictBool`                                                |
| `name`                                     | `pydantic.v1.types.StrictStr`                                                 |
| `parameters`                               | `List[Dict[str, Any]] \| None`                                                |
| `parameters_ui`                            | `List[edgeimpulse_api.models.dsp_group_item.DSPGroupItem] \| None`            |
| `photo`                                    | `pydantic.v1.types.StrictStr`                                                 |
| `privileged`                               | `pydantic.v1.types.StrictBool`                                                |
| `requests_cpu`                             | `float \| None`                                                               |
| `requests_memory`                          | `pydantic.v1.types.StrictInt \| None`                                         |
| `show_optimizations`                       | `pydantic.v1.types.StrictBool`                                                |
| `source_code_available`                    | `pydantic.v1.types.StrictBool`                                                |
| `source_code_download_staff_only`          | `pydantic.v1.types.StrictBool`                                                |
| `supports_eon_compiler`                    | `pydantic.v1.types.StrictBool`                                                |
| `user_id`                                  | `pydantic.v1.types.StrictInt \| None`                                         |
| `user_name`                                | `pydantic.v1.types.StrictStr \| None`                                         |

***

**STATIC METHODS**

#### category\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock.category_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock
```

Create an instance of OrganizationDeployBlock from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                    |
| -------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock
```

Create an instance of OrganizationDeployBlock from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                    |
| -------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock.to_json(
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
edgeimpulse_api.models.organization_deploy_block.OrganizationDeployBlock.to_str(
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