# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/enterprise_limits_increase_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.enterprise_limits_increase_request

## Classes

### EnterpriseLimitsIncreaseRequest

```python  theme={"system"}
edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest(
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

| Class variables |                                                                 |
| --------------- | --------------------------------------------------------------- |
| `Config`        | ` `                                                             |
| `limits`        | `List[edgeimpulse_api.models.enterprise_limit.EnterpriseLimit]` |
| `reason`        | `pydantic.v1.types.StrictStr \| None`                           |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest
```

Create an instance of EnterpriseLimitsIncreaseRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest
```

Create an instance of EnterpriseLimitsIncreaseRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest.to_json(
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
edgeimpulse_api.models.enterprise_limits_increase_request.EnterpriseLimitsIncreaseRequest.to_str(
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