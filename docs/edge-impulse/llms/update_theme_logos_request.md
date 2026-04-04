# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/update_theme_logos_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.update_theme_logos_request

## Classes

### UpdateThemeLogosRequest

```python  theme={"system"}
edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest(
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

| Class variables |                                       |
| --------------- | ------------------------------------- |
| `Config`        | ` `                                   |
| `device_logo`   | `pydantic.v1.types.StrictStr \| None` |
| `login`         | `pydantic.v1.types.StrictStr \| None` |
| `login_white`   | `pydantic.v1.types.StrictStr \| None` |
| `mark`          | `pydantic.v1.types.StrictStr \| None` |
| `mark_white`    | `pydantic.v1.types.StrictStr \| None` |
| `primary`       | `pydantic.v1.types.StrictStr \| None` |
| `primary_white` | `pydantic.v1.types.StrictStr \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest
```

Create an instance of UpdateThemeLogosRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest
```

Create an instance of UpdateThemeLogosRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest.to_json(
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
edgeimpulse_api.models.update_theme_logos_request.UpdateThemeLogosRequest.to_str(
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