# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_dataset

## Classes

### OrganizationDataset

```python  theme={"system"}
edgeimpulse_api.models.organization_dataset.OrganizationDataset(
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

| Class variables                     |                                                                                        |
| ----------------------------------- | -------------------------------------------------------------------------------------- |
| `Config`                            | ` `                                                                                    |
| `bucket`                            | `edgeimpulse_api.models.organization_dataset_bucket.OrganizationDatasetBucket \| None` |
| `bucket_path`                       | `pydantic.v1.types.StrictStr \| None`                                                  |
| `category`                          | `pydantic.v1.types.StrictStr \| None`                                                  |
| `dataset`                           | `pydantic.v1.types.StrictStr`                                                          |
| `last_file_created`                 | `datetime.datetime`                                                                    |
| `tags`                              | `List[pydantic.v1.types.StrictStr]`                                                    |
| `total_file_count`                  | `pydantic.v1.types.StrictInt`                                                          |
| `total_file_size`                   | `pydantic.v1.types.StrictInt`                                                          |
| `total_item_count`                  | `pydantic.v1.types.StrictInt`                                                          |
| `total_item_count_checklist_failed` | `pydantic.v1.types.StrictInt`                                                          |
| `total_item_count_checklist_ok`     | `pydantic.v1.types.StrictInt`                                                          |
| `type`                              | `edgeimpulse_api.models.organization_dataset_type_enum.OrganizationDatasetTypeEnum`    |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_dataset.OrganizationDataset.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_dataset.OrganizationDataset
```

Create an instance of OrganizationDataset from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                           |
| ----------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_dataset.OrganizationDataset` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_dataset.OrganizationDataset.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_dataset.OrganizationDataset
```

Create an instance of OrganizationDataset from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                           |
| ----------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_dataset.OrganizationDataset` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_dataset.OrganizationDataset.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_dataset.OrganizationDataset.to_json(
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
edgeimpulse_api.models.organization_dataset.OrganizationDataset.to_str(
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