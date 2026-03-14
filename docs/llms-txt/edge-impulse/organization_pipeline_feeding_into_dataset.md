# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_pipeline_feeding_into_dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_pipeline_feeding_into_dataset

## Classes

### OrganizationPipelineFeedingIntoDataset

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset(
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

| Class variables              |                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| `Config`                     | ` `                                                                                         |
| `dataset`                    | `pydantic.v1.types.StrictStr`                                                               |
| `dataset_link`               | `pydantic.v1.types.StrictStr`                                                               |
| `dataset_type`               | `edgeimpulse_api.models.organization_dataset_type_enum.OrganizationDatasetTypeEnum \| None` |
| `item_count`                 | `pydantic.v1.types.StrictInt`                                                               |
| `item_count_checklist_error` | `pydantic.v1.types.StrictInt`                                                               |
| `item_count_checklist_ok`    | `pydantic.v1.types.StrictInt`                                                               |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset
```

Create an instance of OrganizationPipelineFeedingIntoDataset from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset
```

Create an instance of OrganizationPipelineFeedingIntoDataset from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset.to_json(
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
edgeimpulse_api.models.organization_pipeline_feeding_into_dataset.OrganizationPipelineFeedingIntoDataset.to_str(
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