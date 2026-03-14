# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/project_deployment_target.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.project_deployment_target

## Classes

### ProjectDeploymentTarget

```python  theme={"system"}
edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget(
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

| Class variables                 |                                                                                  |
| ------------------------------- | -------------------------------------------------------------------------------- |
| `Config`                        | ` `                                                                              |
| `badge`                         | `edgeimpulse_api.models.deployment_target_badge.DeploymentTargetBadge \| None`   |
| `custom_deploy_id`              | `pydantic.v1.types.StrictInt \| None`                                            |
| `custom_deploy_organization_id` | `pydantic.v1.types.StrictInt \| None`                                            |
| `description`                   | `pydantic.v1.types.StrictStr`                                                    |
| `disabled_for_project`          | `pydantic.v1.types.StrictBool`                                                   |
| `docs_url`                      | `pydantic.v1.types.StrictStr`                                                    |
| `firmware_repo_url`             | `pydantic.v1.types.StrictStr \| None`                                            |
| `format`                        | `pydantic.v1.types.StrictStr`                                                    |
| `has_akida`                     | `pydantic.v1.types.StrictBool`                                                   |
| `has_ceva_npn`                  | `pydantic.v1.types.StrictBool`                                                   |
| `has_drpai`                     | `pydantic.v1.types.StrictBool`                                                   |
| `has_eon_compiler`              | `pydantic.v1.types.StrictBool`                                                   |
| `has_memryx`                    | `pydantic.v1.types.StrictBool`                                                   |
| `has_nordic_axon`               | `pydantic.v1.types.StrictBool`                                                   |
| `has_st_aton`                   | `pydantic.v1.types.StrictBool`                                                   |
| `has_tensai_flow`               | `pydantic.v1.types.StrictBool`                                                   |
| `has_tensor_rt`                 | `pydantic.v1.types.StrictBool`                                                   |
| `has_tidl`                      | `pydantic.v1.types.StrictBool`                                                   |
| `hide_optimizations`            | `pydantic.v1.types.StrictBool`                                                   |
| `image`                         | `pydantic.v1.types.StrictStr`                                                    |
| `image_classes`                 | `pydantic.v1.types.StrictStr`                                                    |
| `integrate_url`                 | `pydantic.v1.types.StrictStr \| None`                                            |
| `latency_device`                | `pydantic.v1.types.StrictStr \| None`                                            |
| `model_variants`                | `List[edgeimpulse_api.models.deployment_target_variant.DeploymentTargetVariant]` |
| `name`                          | `pydantic.v1.types.StrictStr`                                                    |
| `owner_organization_name`       | `pydantic.v1.types.StrictStr \| None`                                            |
| `parameters`                    | `List[edgeimpulse_api.models.dsp_group_item.DSPGroupItem]`                       |
| `preferred_engine`              | `edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine`         |
| `reason_target_disabled`        | `pydantic.v1.types.StrictStr \| None`                                            |
| `recommended_for_project`       | `pydantic.v1.types.StrictBool`                                                   |
| `supported_engines`             | `List[edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine]`   |
| `ui_section`                    | `pydantic.v1.types.StrictStr`                                                    |
| `url`                           | `pydantic.v1.types.StrictStr \| None`                                            |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget
```

Create an instance of ProjectDeploymentTarget from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                    |
| -------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget
```

Create an instance of ProjectDeploymentTarget from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                    |
| -------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget` |

#### ui\_section\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget.ui_section_validate_enum(
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
edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget.to_json(
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
edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget.to_str(
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