# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/auto_labeler_segment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# auto_labeler_segment

## AutoLabelerSegment

```python  theme={"system"}
class edgeimpulse_api.models.auto_labeler_segment.AutoLabelerSegment(
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

* `cluster: pydantic.types.StrictInt`

* `id: pydantic.types.StrictInt`

* `mask_height: pydantic.types.StrictInt`

* `mask_url: pydantic.types.StrictStr`

* `mask_width: pydantic.types.StrictInt`

* `mask_x: pydantic.types.StrictInt`

* `mask_y: pydantic.types.StrictInt`

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.auto_labeler_segment.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.auto_labeler_segment.AutoLabelerSegment
```

Create an instance of AutoLabelerSegment from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.auto\_labeler\_segment.AutoLabelerSegment

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.auto_labeler_segment.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.auto_labeler_segment.AutoLabelerSegment
```

Create an instance of AutoLabelerSegment from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.auto\_labeler\_segment.AutoLabelerSegment

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.auto_labeler_segment.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.auto_labeler_segment.to_json(
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
edgeimpulse_api.models.auto_labeler_segment.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).