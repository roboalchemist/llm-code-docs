# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/organization_info_response_all_of_cli_lists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.organization_info_response_all_of_cli_lists

## Classes

### OrganizationInfoResponseAllOfCliLists

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists(
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

| Class variables                       |                                                                                                                                                                                     |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                              | ` `                                                                                                                                                                                 |
| `image_input_scaling_options`         | `List[edgeimpulse_api.models.organization_info_response_all_of_cli_lists_image_input_scaling_options.OrganizationInfoResponseAllOfCliListsImageInputScalingOptions]`                |
| `object_detection_last_layer_options` | `List[edgeimpulse_api.models.organization_info_response_all_of_cli_lists_object_detection_last_layer_options.OrganizationInfoResponseAllOfCliListsObjectDetectionLastLayerOptions]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists
```

Create an instance of OrganizationInfoResponseAllOfCliLists from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists
```

Create an instance of OrganizationInfoResponseAllOfCliLists from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists.to_json(
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
edgeimpulse_api.models.organization_info_response_all_of_cli_lists.OrganizationInfoResponseAllOfCliLists.to_str(
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