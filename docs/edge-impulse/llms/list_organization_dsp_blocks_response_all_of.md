# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_organization_dsp_blocks_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of

## Classes

### ListOrganizationDspBlocksResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf(
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

| Class variables |                                                                            |
| --------------- | -------------------------------------------------------------------------- |
| `Config`        | ` `                                                                        |
| `dsp_blocks`    | `List[edgeimpulse_api.models.organization_dsp_block.OrganizationDspBlock]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf
```

Create an instance of ListOrganizationDspBlocksResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf
```

Create an instance of ListOrganizationDspBlocksResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf.to_json(
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
edgeimpulse_api.models.list_organization_dsp_blocks_response_all_of.ListOrganizationDspBlocksResponseAllOf.to_str(
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