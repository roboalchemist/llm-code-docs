# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/oauth_client.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.oauth_client

## Classes

### OauthClient

```python  theme={"system"}
edgeimpulse_api.models.oauth_client.OauthClient(
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

| Class variables         |                                                                        |
| ----------------------- | ---------------------------------------------------------------------- |
| `Config`                | ` `                                                                    |
| `allowed_grant_types`   | `List[edgeimpulse_api.models.oauth_grant_type.OauthGrantType] \| None` |
| `client_id`             | `pydantic.v1.types.StrictStr`                                          |
| `created_at`            | `datetime.datetime`                                                    |
| `created_by_user_email` | `pydantic.v1.types.StrictStr \| None`                                  |
| `created_by_user_id`    | `pydantic.v1.types.StrictInt`                                          |
| `created_by_user_name`  | `pydantic.v1.types.StrictStr \| None`                                  |
| `description`           | `pydantic.v1.types.StrictStr \| None`                                  |
| `id`                    | `pydantic.v1.types.StrictInt`                                          |
| `logo_url`              | `pydantic.v1.types.StrictStr \| None`                                  |
| `name`                  | `pydantic.v1.types.StrictStr`                                          |
| `owner_name`            | `pydantic.v1.types.StrictStr \| None`                                  |
| `owner_url`             | `pydantic.v1.types.StrictStr \| None`                                  |
| `redirect_uris`         | `List[pydantic.v1.types.StrictStr] \| None`                            |
| `requires_consent`      | `pydantic.v1.types.StrictBool \| None`                                 |
| `scopes`                | `List[edgeimpulse_api.models.o_auth_scope.OAuthScope] \| None`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.oauth_client.OauthClient.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.oauth_client.OauthClient
```

Create an instance of OauthClient from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                           |
| ------------------------------------------------- |
| `edgeimpulse_api.models.oauth_client.OauthClient` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.oauth_client.OauthClient.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.oauth_client.OauthClient
```

Create an instance of OauthClient from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                           |
| ------------------------------------------------- |
| `edgeimpulse_api.models.oauth_client.OauthClient` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.oauth_client.OauthClient.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.oauth_client.OauthClient.to_json(
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
edgeimpulse_api.models.oauth_client.OauthClient.to_str(
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