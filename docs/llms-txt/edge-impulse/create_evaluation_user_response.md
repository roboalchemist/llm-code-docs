# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/create_evaluation_user_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# create_evaluation_user_response

## CreateEvaluationUserResponse

```python  theme={"system"}
class edgeimpulse_api.models.create_evaluation_user_response.CreateEvaluationUserResponse(
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
  The type of the None singleton.

* `error: pydantic.types.StrictStr | None`
  The type of the None singleton.

* `redirect_url: pydantic.types.StrictStr`
  The type of the None singleton.

* `success: pydantic.types.StrictBool`
  The type of the None singleton.

* `token: pydantic.types.StrictStr`
  The type of the None singleton.

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_evaluation_user_response.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.create_evaluation_user_response.CreateEvaluationUserResponse
```

Create an instance of CreateEvaluationUserResponse from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.create\_evaluation\_user\_response.CreateEvaluationUserResponse

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.create_evaluation_user_response.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.create_evaluation_user_response.CreateEvaluationUserResponse
```

Create an instance of CreateEvaluationUserResponse from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.create\_evaluation\_user\_response.CreateEvaluationUserResponse

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.create_evaluation_user_response.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.create_evaluation_user_response.to_json(
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
edgeimpulse_api.models.create_evaluation_user_response.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).