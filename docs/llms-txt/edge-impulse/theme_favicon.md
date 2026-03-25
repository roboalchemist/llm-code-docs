# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/theme_favicon.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.theme_favicon

## Classes

### ThemeFavicon

```python  theme={"system"}
edgeimpulse_api.models.theme_favicon.ThemeFavicon(
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
| `favicon120`    | `pydantic.v1.types.StrictStr \| None` |
| `favicon128`    | `pydantic.v1.types.StrictStr \| None` |
| `favicon144`    | `pydantic.v1.types.StrictStr \| None` |
| `favicon152`    | `pydantic.v1.types.StrictStr \| None` |
| `favicon180`    | `pydantic.v1.types.StrictStr \| None` |
| `favicon228`    | `pydantic.v1.types.StrictStr \| None` |
| `favicon32`     | `pydantic.v1.types.StrictStr \| None` |
| `favicon57`     | `pydantic.v1.types.StrictStr \| None` |
| `favicon76`     | `pydantic.v1.types.StrictStr \| None` |
| `favicon96`     | `pydantic.v1.types.StrictStr \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.theme_favicon.ThemeFavicon.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.theme_favicon.ThemeFavicon
```

Create an instance of ThemeFavicon from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                             |
| --------------------------------------------------- |
| `edgeimpulse_api.models.theme_favicon.ThemeFavicon` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.theme_favicon.ThemeFavicon.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.theme_favicon.ThemeFavicon
```

Create an instance of ThemeFavicon from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                             |
| --------------------------------------------------- |
| `edgeimpulse_api.models.theme_favicon.ThemeFavicon` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.theme_favicon.ThemeFavicon.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.theme_favicon.ThemeFavicon.to_json(
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
edgeimpulse_api.models.theme_favicon.ThemeFavicon.to_str(
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