# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/verify_organization_bucket_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.verify_organization_bucket_response

## Classes

### VerifyOrganizationBucketResponse

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse(
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

| Class variables           |                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `Config`                  | ` `                                                                                                                                |
| `connection_error`        | `pydantic.v1.types.StrictStr \| None`                                                                                              |
| `connection_status`       | `pydantic.v1.types.StrictStr`                                                                                                      |
| `connection_status_since` | `datetime.datetime \| None`                                                                                                        |
| `endpoint`                | `pydantic.v1.types.StrictStr \| None`                                                                                              |
| `error`                   | `pydantic.v1.types.StrictStr \| None`                                                                                              |
| `files`                   | `List[edgeimpulse_api.models.verify_organization_bucket_response_all_of_files.VerifyOrganizationBucketResponseAllOfFiles] \| None` |
| `has_info_labels_file`    | `pydantic.v1.types.StrictBool \| None`                                                                                             |
| `signed_url`              | `pydantic.v1.types.StrictStr \| None`                                                                                              |
| `success`                 | `pydantic.v1.types.StrictBool`                                                                                                     |

***

**STATIC METHODS**

#### connection\_status\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse.connection_status_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse
```

Create an instance of VerifyOrganizationBucketResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse
```

Create an instance of VerifyOrganizationBucketResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse.to_json(
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
edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse.to_str(
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