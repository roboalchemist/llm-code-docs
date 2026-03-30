# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/add_organization_data_campaign_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.add_organization_data_campaign_request

## Classes

### AddOrganizationDataCampaignRequest

```python  theme={"system"}
edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest(
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

| Class variables              |                                                                      |
| ---------------------------- | -------------------------------------------------------------------- |
| `Config`                     | ` `                                                                  |
| `coordinator_uids`           | `List[pydantic.v1.types.StrictInt]`                                  |
| `created`                    | `datetime.datetime \| None`                                          |
| `data_campaign_dashboard_id` | `pydantic.v1.types.StrictInt`                                        |
| `datasets`                   | `List[pydantic.v1.types.StrictStr]`                                  |
| `description`                | `pydantic.v1.types.StrictStr`                                        |
| `id`                         | `pydantic.v1.types.StrictInt \| None`                                |
| `links`                      | `List[edgeimpulse_api.models.data_campaign_link.DataCampaignLink]`   |
| `logo`                       | `pydantic.v1.types.StrictStr \| None`                                |
| `name`                       | `pydantic.v1.types.StrictStr`                                        |
| `pipeline_ids`               | `List[pydantic.v1.types.StrictInt]`                                  |
| `project_ids`                | `List[pydantic.v1.types.StrictInt]`                                  |
| `queries`                    | `List[edgeimpulse_api.models.data_campaign_query.DataCampaignQuery]` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest
```

Create an instance of AddOrganizationDataCampaignRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest
```

Create an instance of AddOrganizationDataCampaignRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                            |
| -------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest.to_json(
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
edgeimpulse_api.models.add_organization_data_campaign_request.AddOrganizationDataCampaignRequest.to_str(
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