# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/batch_edit_labels200_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# batch_edit_labels200_response

## BatchEditLabels200Response

```python  theme={"system"}
class edgeimpulse_api.models.batch_edit_labels200_response.BatchEditLabels200Response(
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

* `actual_instance: Any`

* `any_of_schemas: List[str]`

* `anyof_schema_1_validator: edgeimpulse_api.models.generic_api_response.GenericApiResponse | None`

* `anyof_schema_2_validator: edgeimpulse_api.models.start_job_response.StartJobResponse | None`

## Static methods

### actual\_instance\_must\_validate\_anyof

```python  theme={"system"}
edgeimpulse_api.models.batch_edit_labels200_response.actual_instance_must_validate_anyof(
		v
)
```

**Parameters**

* v

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.batch_edit_labels200_response.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.batch_edit_labels200_response.BatchEditLabels200Response
```

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.batch\_edit\_labels200\_response.BatchEditLabels200Response

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.batch_edit_labels200_response.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.batch_edit_labels200_response.BatchEditLabels200Response
```

Returns the object represented by the json string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.batch\_edit\_labels200\_response.BatchEditLabels200Response

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.batch_edit_labels200_response.to_dict(
		self
) ‑> dict
```

Returns the dict representation of the actual instance

**Parameters**

* self

**Return**

dict

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.batch_edit_labels200_response.to_json(
		self,
		indent=None
) ‑> str
```

Returns the JSON representation of the actual instance

**Parameters**

* self
* indent=None

**Return**

str

### to\_str

```python  theme={"system"}
edgeimpulse_api.models.batch_edit_labels200_response.to_str(
		self
) ‑> str
```

Returns the string representation of the actual instance

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).