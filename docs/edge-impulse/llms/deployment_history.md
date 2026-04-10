# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/deployment_history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.deployment_history

## Classes

### DeploymentHistory

```python  theme={"system"}
edgeimpulse_api.models.deployment_history.DeploymentHistory(
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

| Class variables                        |                                                                                    |
| -------------------------------------- | ---------------------------------------------------------------------------------- |
| `Config`                               | ` `                                                                                |
| `created`                              | `datetime.datetime`                                                                |
| `created_by_user`                      | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None`      |
| `deployment_format`                    | `pydantic.v1.types.StrictStr`                                                      |
| `deployment_target`                    | `edgeimpulse_api.models.project_deployment_target.ProjectDeploymentTarget \| None` |
| `deployment_version`                   | `pydantic.v1.types.StrictInt`                                                      |
| `download_url`                         | `pydantic.v1.types.StrictStr`                                                      |
| `engine`                               | `edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine`           |
| `impulse_has_changed_since_deployment` | `pydantic.v1.types.StrictBool`                                                     |
| `impulse_id`                           | `pydantic.v1.types.StrictInt`                                                      |
| `impulse_is_deleted`                   | `pydantic.v1.types.StrictBool`                                                     |
| `impulse_name`                         | `pydantic.v1.types.StrictStr`                                                      |
| `model_type`                           | `edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum \| None`          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.deployment_history.DeploymentHistory.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.deployment_history.DeploymentHistory
```

Create an instance of DeploymentHistory from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                       |
| ------------------------------------------------------------- |
| `edgeimpulse_api.models.deployment_history.DeploymentHistory` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.deployment_history.DeploymentHistory.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.deployment_history.DeploymentHistory
```

Create an instance of DeploymentHistory from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                       |
| ------------------------------------------------------------- |
| `edgeimpulse_api.models.deployment_history.DeploymentHistory` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.deployment_history.DeploymentHistory.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.deployment_history.DeploymentHistory.to_json(
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
edgeimpulse_api.models.deployment_history.DeploymentHistory.to_str(
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