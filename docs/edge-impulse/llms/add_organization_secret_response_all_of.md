# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/add_organization_secret_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# add_organization_secret_response_all_of

## AddOrganizationSecretResponseAllOf

```python  theme={"system"}
class edgeimpulse_api.models.add_organization_secret_response_all_of.AddOrganizationSecretResponseAllOf(
		**data: Any
)
```

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

**Parameters**

* \*\*data: Any

**Bases**

* pydantic.main.BaseModel
* pydantic.utils.Representation

**Class variables**

* `Config`

* `id: pydantic.types.StrictInt`

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.add_organization_secret_response_all_of.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.add_organization_secret_response_all_of.AddOrganizationSecretResponseAllOf
```

Create an instance of AddOrganizationSecretResponseAllOf from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.add\_organization\_secret\_response\_all\_of.AddOrganizationSecretResponseAllOf

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.add_organization_secret_response_all_of.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.add_organization_secret_response_all_of.AddOrganizationSecretResponseAllOf
```

Create an instance of AddOrganizationSecretResponseAllOf from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.add\_organization\_secret\_response\_all\_of.AddOrganizationSecretResponseAllOf

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.add_organization_secret_response_all_of.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.add_organization_secret_response_all_of.to_json(
		self,
		indent=None
) ‑> str
```

Returns the JSON representation of the model using alias

**Parameters**

* self
* indent=None

**Return**

str

### to\_str

```python  theme={"system"}
edgeimpulse_api.models.add_organization_secret_response_all_of.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).