# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_organization_secrets_response_all_of_secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets

## Classes

### ListOrganizationSecretsResponseAllOfSecrets

```python  theme={"system"}
edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets(
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

| Class variables   |                                                                               |
| ----------------- | ----------------------------------------------------------------------------- |
| `Config`          | ` `                                                                           |
| `created`         | `datetime.datetime`                                                           |
| `created_by_user` | `edgeimpulse_api.models.created_updated_by_user.CreatedUpdatedByUser \| None` |
| `description`     | `pydantic.v1.types.StrictStr`                                                 |
| `id`              | `pydantic.v1.types.StrictInt`                                                 |
| `name`            | `pydantic.v1.types.StrictStr`                                                 |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets
```

Create an instance of ListOrganizationSecretsResponseAllOfSecrets from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets
```

Create an instance of ListOrganizationSecretsResponseAllOfSecrets from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets.to_json(
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
edgeimpulse_api.models.list_organization_secrets_response_all_of_secrets.ListOrganizationSecretsResponseAllOfSecrets.to_str(
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