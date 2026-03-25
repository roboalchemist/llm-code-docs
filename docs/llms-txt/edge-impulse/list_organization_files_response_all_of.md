# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_organization_files_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_organization_files_response_all_of

## Classes

### ListOrganizationFilesResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf(
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

| Class variables         |                                                                            |
| ----------------------- | -------------------------------------------------------------------------- |
| `Config`                | ` `                                                                        |
| `data`                  | `List[edgeimpulse_api.models.organization_data_item.OrganizationDataItem]` |
| `filter_parse_error`    | `pydantic.v1.types.StrictStr \| None`                                      |
| `total_data_item_count` | `pydantic.v1.types.StrictInt`                                              |
| `total_file_count`      | `pydantic.v1.types.StrictInt`                                              |
| `total_file_size`       | `pydantic.v1.types.StrictInt`                                              |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf
```

Create an instance of ListOrganizationFilesResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf
```

Create an instance of ListOrganizationFilesResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                             |
| --------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf.to_json(
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
edgeimpulse_api.models.list_organization_files_response_all_of.ListOrganizationFilesResponseAllOf.to_str(
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