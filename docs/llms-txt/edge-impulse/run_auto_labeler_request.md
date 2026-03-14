# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/run_auto_labeler_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# run_auto_labeler_request

## RunAutoLabelerRequest

```python  theme={"system"}
class edgeimpulse_api.models.run_auto_labeler_request.RunAutoLabelerRequest(
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

* `max_object_size_px: Optional[pydantic.types.StrictInt]`

* `min_object_size_px: pydantic.types.StrictInt`

* `sim_threshold: float`

* `which_items_to_include: pydantic.types.StrictStr`

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.run_auto_labeler_request.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.run_auto_labeler_request.RunAutoLabelerRequest
```

Create an instance of RunAutoLabelerRequest from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.run\_auto\_labeler\_request.RunAutoLabelerRequest

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.run_auto_labeler_request.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.run_auto_labeler_request.RunAutoLabelerRequest
```

Create an instance of RunAutoLabelerRequest from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.run\_auto\_labeler\_request.RunAutoLabelerRequest

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.run_auto_labeler_request.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.run_auto_labeler_request.to_json(
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
edgeimpulse_api.models.run_auto_labeler_request.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).