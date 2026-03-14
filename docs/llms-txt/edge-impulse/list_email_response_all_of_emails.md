# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/list_email_response_all_of_emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.list_email_response_all_of_emails

## Classes

### ListEmailResponseAllOfEmails

```python  theme={"system"}
edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails(
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

| Class variables     |                                       |
| ------------------- | ------------------------------------- |
| `Config`            | ` `                                   |
| `body_html`         | `pydantic.v1.types.StrictStr`         |
| `body_text`         | `pydantic.v1.types.StrictStr`         |
| `created`           | `datetime.datetime`                   |
| `project_id`        | `pydantic.v1.types.StrictInt \| None` |
| `provider_response` | `pydantic.v1.types.StrictStr`         |
| `sent`              | `pydantic.v1.types.StrictBool`        |
| `subject`           | `pydantic.v1.types.StrictStr`         |
| `to`                | `pydantic.v1.types.StrictStr`         |
| `user_id`           | `pydantic.v1.types.StrictInt \| None` |
| `var_from`          | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails
```

Create an instance of ListEmailResponseAllOfEmails from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails
```

Create an instance of ListEmailResponseAllOfEmails from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails.to_json(
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
edgeimpulse_api.models.list_email_response_all_of_emails.ListEmailResponseAllOfEmails.to_str(
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