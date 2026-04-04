# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/project_api_key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.project_api_key

## Classes

### ProjectApiKey

```python  theme={"system"}
edgeimpulse_api.models.project_api_key.ProjectApiKey(
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

| Class variables      |                                                                                  |
| -------------------- | -------------------------------------------------------------------------------- |
| `Config`             | ` `                                                                              |
| `api_key`            | `pydantic.v1.types.StrictStr`                                                    |
| `created`            | `datetime.datetime`                                                              |
| `created_by_user`    | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None`    |
| `id`                 | `pydantic.v1.types.StrictInt`                                                    |
| `is_development_key` | `pydantic.v1.types.StrictBool`                                                   |
| `last_used`          | `edgeimpulse_api.models.project_api_key_last_used.ProjectApiKeyLastUsed \| None` |
| `name`               | `pydantic.v1.types.StrictStr`                                                    |
| `role`               | `pydantic.v1.types.StrictStr`                                                    |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_api_key.ProjectApiKey.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.project_api_key.ProjectApiKey
```

Create an instance of ProjectApiKey from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                |
| ------------------------------------------------------ |
| `edgeimpulse_api.models.project_api_key.ProjectApiKey` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.project_api_key.ProjectApiKey.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.project_api_key.ProjectApiKey
```

Create an instance of ProjectApiKey from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                |
| ------------------------------------------------------ |
| `edgeimpulse_api.models.project_api_key.ProjectApiKey` |

#### role\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.project_api_key.ProjectApiKey.role_validate_enum(
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
edgeimpulse_api.models.project_api_key.ProjectApiKey.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.project_api_key.ProjectApiKey.to_json(
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
edgeimpulse_api.models.project_api_key.ProjectApiKey.to_str(
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