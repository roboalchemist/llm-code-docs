# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/create_pipeline_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# create_pipeline_response

## CreatePipelineResponse

```python  theme={"system"}
class edgeimpulse_api.models.create_pipeline_response.CreatePipelineResponse(
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

* `error: pydantic.types.StrictStr | None`

* `id: pydantic.types.StrictInt`

* `success: pydantic.types.StrictBool`

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_pipeline_response.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.create_pipeline_response.CreatePipelineResponse
```

Create an instance of CreatePipelineResponse from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.create\_pipeline\_response.CreatePipelineResponse

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.create_pipeline_response.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.create_pipeline_response.CreatePipelineResponse
```

Create an instance of CreatePipelineResponse from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.create\_pipeline\_response.CreatePipelineResponse

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_pipeline_response.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.create_pipeline_response.to_json(
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
edgeimpulse_api.models.create_pipeline_response.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).