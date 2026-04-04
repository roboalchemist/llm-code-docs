# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_organization_data_response_all_of_data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_organization_data_response_all_of_data

## Classes

### ListOrganizationDataResponseAllOfData

```python  theme={"system"}
edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData(
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

| Class variables           |                                          |
| ------------------------- | ---------------------------------------- |
| `Config`                  | ` `                                      |
| `bucket_id`               | `pydantic.v1.types.StrictInt`            |
| `bucket_name`             | `pydantic.v1.types.StrictStr`            |
| `bucket_path`             | `pydantic.v1.types.StrictStr`            |
| `created`                 | `datetime.datetime`                      |
| `dataset`                 | `pydantic.v1.types.StrictStr`            |
| `full_bucket_path`        | `pydantic.v1.types.StrictStr`            |
| `id`                      | `pydantic.v1.types.StrictInt`            |
| `metadata`                | `Dict[str, pydantic.v1.types.StrictStr]` |
| `metadata_string_for_cli` | `pydantic.v1.types.StrictStr`            |
| `name`                    | `pydantic.v1.types.StrictStr`            |
| `total_file_count`        | `pydantic.v1.types.StrictInt`            |
| `total_file_size`         | `pydantic.v1.types.StrictInt`            |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData
```

Create an instance of ListOrganizationDataResponseAllOfData from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData
```

Create an instance of ListOrganizationDataResponseAllOfData from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData.to_json(
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
edgeimpulse_api.models.list_organization_data_response_all_of_data.ListOrganizationDataResponseAllOfData.to_str(
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