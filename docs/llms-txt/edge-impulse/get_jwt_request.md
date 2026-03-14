# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_jwt_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_jwt_request

## Classes

### GetJWTRequest

```python  theme={"system"}
edgeimpulse_api.models.get_jwt_request.GetJWTRequest(
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
| `password`      | `pydantic.v1.types.StrictStr`         |
| `session_id`    | `pydantic.v1.types.StrictStr \| None` |
| `sso_type`      | `pydantic.v1.types.StrictStr \| None` |
| `totp_token`    | `pydantic.v1.types.StrictStr \| None` |
| `username`      | `pydantic.v1.types.StrictStr`         |
| `uuid`          | `pydantic.v1.types.StrictStr \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_jwt_request.GetJWTRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_jwt_request.GetJWTRequest
```

Create an instance of GetJWTRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                |
| ------------------------------------------------------ |
| `edgeimpulse_api.models.get_jwt_request.GetJWTRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_jwt_request.GetJWTRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_jwt_request.GetJWTRequest
```

Create an instance of GetJWTRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                |
| ------------------------------------------------------ |
| `edgeimpulse_api.models.get_jwt_request.GetJWTRequest` |

#### sso\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.get_jwt_request.GetJWTRequest.sso_type_validate_enum(
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
edgeimpulse_api.models.get_jwt_request.GetJWTRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_jwt_request.GetJWTRequest.to_json(
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
edgeimpulse_api.models.get_jwt_request.GetJWTRequest.to_str(
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