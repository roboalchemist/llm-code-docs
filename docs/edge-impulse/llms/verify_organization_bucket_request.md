# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/verify_organization_bucket_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.verify_organization_bucket_request

## Classes

### VerifyOrganizationBucketRequest

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest(
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

| Class variables    |                                                                   |
| ------------------ | ----------------------------------------------------------------- |
| `Config`           | ` `                                                               |
| `access_key`       | `pydantic.v1.types.StrictStr`                                     |
| `bucket`           | `pydantic.v1.types.StrictStr`                                     |
| `bucket_id`        | `pydantic.v1.types.StrictInt \| None`                             |
| `endpoint`         | `pydantic.v1.types.StrictStr`                                     |
| `prefix`           | `pydantic.v1.types.StrictStr \| None`                             |
| `region`           | `pydantic.v1.types.StrictStr \| None`                             |
| `secret_key`       | `pydantic.v1.types.StrictStr \| None`                             |
| `storage_provider` | `edgeimpulse_api.models.storage_provider.StorageProvider \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest
```

Create an instance of VerifyOrganizationBucketRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest
```

Create an instance of VerifyOrganizationBucketRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest.to_json(
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
edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest.to_str(
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