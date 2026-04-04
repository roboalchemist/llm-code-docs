# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_organization_transfer_learning_block_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of

## Classes

### GetOrganizationTransferLearningBlockResponseAllOf

```python  theme={"system"}
edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf(
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

| Class variables           |                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| `Config`                  | ` `                                                                                             |
| `transfer_learning_block` | `edgeimpulse_api.models.organization_transfer_learning_block.OrganizationTransferLearningBlock` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf
```

Create an instance of GetOrganizationTransferLearningBlockResponseAllOf from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf
```

Create an instance of GetOrganizationTransferLearningBlockResponseAllOf from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf.to_json(
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
edgeimpulse_api.models.get_organization_transfer_learning_block_response_all_of.GetOrganizationTransferLearningBlockResponseAllOf.to_str(
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