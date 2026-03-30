# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/data_campaign_graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.data_campaign_graph

## Classes

### DataCampaignGraph

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph(
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

| Class variables |                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------- |
| `Config`        | ` `                                                                                         |
| `link`          | `pydantic.v1.types.StrictStr`                                                               |
| `next_update`   | `datetime.datetime`                                                                         |
| `title`         | `pydantic.v1.types.StrictStr`                                                               |
| `x_data`        | `List[edgeimpulse_api.models.data_campaign_graph_x_data_inner.DataCampaignGraphXDataInner]` |
| `y_ticks`       | `List[datetime.datetime]`                                                                   |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph
```

Create an instance of DataCampaignGraph from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph
```

Create an instance of DataCampaignGraph from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph.to_json(
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
edgeimpulse_api.models.data_campaign_graph.DataCampaignGraph.to_str(
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