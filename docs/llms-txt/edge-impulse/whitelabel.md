# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/whitelabel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.whitelabel

## Classes

### Whitelabel

```python  theme={"system"}
edgeimpulse_api.models.whitelabel.Whitelabel(
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

| Class variables              |                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `Config`                     | ` `                                                                                                                    |
| `all_deployment_targets`     | `List[pydantic.v1.types.StrictStr]`                                                                                    |
| `all_development_boards`     | `List[edgeimpulse_api.models.development_board_response.DevelopmentBoardResponse]`                                     |
| `all_learning_blocks`        | `List[edgeimpulse_api.models.whitelabel_all_learning_blocks_inner.WhitelabelAllLearningBlocksInner]`                   |
| `allow_free_projects`        | `pydantic.v1.types.StrictBool`                                                                                         |
| `allow_new_project_ui`       | `pydantic.v1.types.StrictBool`                                                                                         |
| `allow_password_auth`        | `pydantic.v1.types.StrictBool`                                                                                         |
| `allow_signup`               | `pydantic.v1.types.StrictBool`                                                                                         |
| `custom_deployment_blocks`   | `List[edgeimpulse_api.models.whitelabel_custom_deployment_blocks_inner.WhitelabelCustomDeploymentBlocksInner] \| None` |
| `custom_limits`              | `Dict[str, Any] \| None`                                                                                               |
| `default_deployment_target`  | `pydantic.v1.types.StrictStr \| None`                                                                                  |
| `deployment_options_order`   | `List[pydantic.v1.types.StrictStr] \| None`                                                                            |
| `deployment_targets`         | `List[pydantic.v1.types.StrictStr]`                                                                                    |
| `development_boards`         | `List[edgeimpulse_api.models.development_board_response.DevelopmentBoardResponse]`                                     |
| `disable_forum_access`       | `pydantic.v1.types.StrictBool \| None`                                                                                 |
| `disable_marketing_features` | `pydantic.v1.types.StrictBool \| None`                                                                                 |
| `disable_public_entities`    | `pydantic.v1.types.StrictBool \| None`                                                                                 |
| `domain`                     | `pydantic.v1.types.StrictStr`                                                                                          |
| `expose_public_projects`     | `pydantic.v1.types.StrictBool \| None`                                                                                 |
| `id`                         | `pydantic.v1.types.StrictInt`                                                                                          |
| `identity_providers`         | `List[pydantic.v1.types.StrictStr]`                                                                                    |
| `learning_blocks`            | `List[pydantic.v1.types.StrictStr]`                                                                                    |
| `name`                       | `pydantic.v1.types.StrictStr`                                                                                          |
| `organizations_limit`        | `pydantic.v1.types.StrictInt \| None`                                                                                  |
| `owner_organization_id`      | `pydantic.v1.types.StrictInt \| None`                                                                                  |
| `supported_project_types`    | `List[edgeimpulse_api.models.project_type.ProjectType]`                                                                |
| `theme`                      | `edgeimpulse_api.models.theme.Theme \| None`                                                                           |
| `theme_id`                   | `pydantic.v1.types.StrictInt`                                                                                          |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.whitelabel.Whitelabel.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.whitelabel.Whitelabel
```

Create an instance of Whitelabel from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                        |
| ---------------------------------------------- |
| `edgeimpulse_api.models.whitelabel.Whitelabel` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.whitelabel.Whitelabel.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.whitelabel.Whitelabel
```

Create an instance of Whitelabel from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                        |
| ---------------------------------------------- |
| `edgeimpulse_api.models.whitelabel.Whitelabel` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.whitelabel.Whitelabel.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.whitelabel.Whitelabel.to_json(
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
edgeimpulse_api.models.whitelabel.Whitelabel.to_str(
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