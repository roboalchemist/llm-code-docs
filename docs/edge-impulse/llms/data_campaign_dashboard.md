# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/data_campaign_dashboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.data_campaign_dashboard

## Classes

### DataCampaignDashboard

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard(
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

| Class variables        |                                       |
| ---------------------- | ------------------------------------- |
| `Config`               | ` `                                   |
| `created`              | `datetime.datetime`                   |
| `email_recipient_uids` | `List[pydantic.v1.types.StrictInt]`   |
| `id`                   | `pydantic.v1.types.StrictInt`         |
| `latest_screenshot`    | `pydantic.v1.types.StrictStr \| None` |
| `name`                 | `pydantic.v1.types.StrictStr`         |
| `show_no_of_days`      | `pydantic.v1.types.StrictInt`         |
| `when_to_email`        | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard
```

Create an instance of DataCampaignDashboard from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard
```

Create an instance of DataCampaignDashboard from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard` |

#### when\_to\_email\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard.when_to_email_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard.to_json(
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
edgeimpulse_api.models.data_campaign_dashboard.DataCampaignDashboard.to_str(
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