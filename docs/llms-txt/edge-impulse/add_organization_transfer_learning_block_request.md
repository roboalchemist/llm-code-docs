# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/add_organization_transfer_learning_block_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.add_organization_transfer_learning_block_request

## Classes

### AddOrganizationTransferLearningBlockRequest

```python  theme={"system"}
edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest(
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

| Class variables                    |                                                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                           | ` `                                                                                                                                       |
| `block_no_longer_available_reason` | `pydantic.v1.types.StrictStr \| None`                                                                                                     |
| `custom_model_variants`            | `List[edgeimpulse_api.models.organization_transfer_learning_block_custom_variant.OrganizationTransferLearningBlockCustomVariant] \| None` |
| `description`                      | `pydantic.v1.types.StrictStr`                                                                                                             |
| `display_category`                 | `edgeimpulse_api.models.block_display_category.BlockDisplayCategory \| None`                                                              |
| `docker_container`                 | `pydantic.v1.types.StrictStr`                                                                                                             |
| `image_input_scaling`              | `edgeimpulse_api.models.image_input_scaling.ImageInputScaling \| None`                                                                    |
| `implementation_version`           | `pydantic.v1.types.StrictInt`                                                                                                             |
| `ind_block_no_longer_available`    | `pydantic.v1.types.StrictBool \| None`                                                                                                    |
| `ind_requires_gpu`                 | `pydantic.v1.types.StrictBool \| None`                                                                                                    |
| `is_public`                        | `pydantic.v1.types.StrictBool \| None`                                                                                                    |
| `is_public_for_devices`            | `List[pydantic.v1.types.StrictStr] \| None`                                                                                               |
| `name`                             | `pydantic.v1.types.StrictStr`                                                                                                             |
| `object_detection_last_layer`      | `edgeimpulse_api.models.object_detection_last_layer.ObjectDetectionLastLayer \| None`                                                     |
| `operates_on`                      | `edgeimpulse_api.models.organization_transfer_learning_operates_on.OrganizationTransferLearningOperatesOn`                                |
| `parameters`                       | `List[Dict[str, Any]] \| None`                                                                                                            |
| `public_project_tier_availability` | `edgeimpulse_api.models.public_project_tier_availability.PublicProjectTierAvailability \| None`                                           |
| `repository_url`                   | `pydantic.v1.types.StrictStr \| None`                                                                                                     |
| `source_code_download_staff_only`  | `pydantic.v1.types.StrictBool \| None`                                                                                                    |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest
```

Create an instance of AddOrganizationTransferLearningBlockRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest
```

Create an instance of AddOrganizationTransferLearningBlockRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest.to_json(
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
edgeimpulse_api.models.add_organization_transfer_learning_block_request.AddOrganizationTransferLearningBlockRequest.to_str(
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