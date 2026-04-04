# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_versions_response_all_of_versions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_versions_response_all_of_versions

## Classes

### ListVersionsResponseAllOfVersions

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions(
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

| Class variables             |                                                                                               |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| `Config`                    | ` `                                                                                           |
| `accuracy_based_on_impulse` | `pydantic.v1.types.StrictStr \| None`                                                         |
| `bucket`                    | `edgeimpulse_api.models.list_versions_response_all_of_bucket.ListVersionsResponseAllOfBucket` |
| `created`                   | `datetime.datetime`                                                                           |
| `description`               | `pydantic.v1.types.StrictStr`                                                                 |
| `id`                        | `pydantic.v1.types.StrictInt`                                                                 |
| `license`                   | `edgeimpulse_api.models.public_project_license.PublicProjectLicense \| None`                  |
| `public_project_id`         | `pydantic.v1.types.StrictInt \| None`                                                         |
| `public_project_url`        | `pydantic.v1.types.StrictStr \| None`                                                         |
| `test_accuracy`             | `float \| None`                                                                               |
| `total_samples_count`       | `pydantic.v1.types.StrictStr \| None`                                                         |
| `training_accuracy`         | `float \| None`                                                                               |
| `user_id`                   | `pydantic.v1.types.StrictInt \| None`                                                         |
| `user_name`                 | `pydantic.v1.types.StrictStr \| None`                                                         |
| `user_photo`                | `pydantic.v1.types.StrictStr \| None`                                                         |
| `version`                   | `pydantic.v1.types.StrictInt`                                                                 |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions
```

Create an instance of ListVersionsResponseAllOfVersions from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions
```

Create an instance of ListVersionsResponseAllOfVersions from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                           |
| ------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions.to_json(
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
edgeimpulse_api.models.list_versions_response_all_of_versions.ListVersionsResponseAllOfVersions.to_str(
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