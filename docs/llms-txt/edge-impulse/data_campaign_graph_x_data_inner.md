# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/data_campaign_graph_x_data_inner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.data_campaign_graph_x_data_inner

## Classes

### DataCampaignGraphXDataInner

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner(
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

| Class variables |                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                                                                 |
| `color`         | `pydantic.v1.types.StrictStr`                                                                                       |
| `data_type`     | `pydantic.v1.types.StrictStr`                                                                                       |
| `dataset`       | `pydantic.v1.types.StrictStr \| None`                                                                               |
| `legend_text`   | `pydantic.v1.types.StrictStr`                                                                                       |
| `popup_text`    | `pydantic.v1.types.StrictStr`                                                                                       |
| `query`         | `pydantic.v1.types.StrictStr \| None`                                                                               |
| `values`        | `List[edgeimpulse_api.models.data_campaign_graph_x_data_inner_values_inner.DataCampaignGraphXDataInnerValuesInner]` |

***

**STATIC METHODS**

#### data\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner.data_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner
```

Create an instance of DataCampaignGraphXDataInner from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner
```

Create an instance of DataCampaignGraphXDataInner from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner.to_json(
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
edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner.to_str(
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