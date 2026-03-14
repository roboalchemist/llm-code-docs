# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/data_campaign.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.data_campaign

## Classes

### DataCampaign

```python  theme={"system"}
edgeimpulse_api.models.data_campaign.DataCampaign(
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
| `created`                    | `datetime.datetime`                                                  |
| `data_campaign_dashboard_id` | `pydantic.v1.types.StrictInt`                                        |
| `datasets`                   | `List[pydantic.v1.types.StrictStr]`                                  |
| `description`                | `pydantic.v1.types.StrictStr`                                        |
| `id`                         | `pydantic.v1.types.StrictInt`                                        |
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
edgeimpulse_api.models.data_campaign.DataCampaign.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.data_campaign.DataCampaign
```

Create an instance of DataCampaign from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                             |
| --------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign.DataCampaign` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign.DataCampaign.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.data_campaign.DataCampaign
```

Create an instance of DataCampaign from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                             |
| --------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign.DataCampaign` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.data_campaign.DataCampaign.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign.DataCampaign.to_json(
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
edgeimpulse_api.models.data_campaign.DataCampaign.to_str(
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