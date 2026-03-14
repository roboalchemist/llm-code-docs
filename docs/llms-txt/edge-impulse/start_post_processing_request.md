# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/start_post_processing_request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.start_post_processing_request

## Classes

### StartPostProcessingRequest

```python  theme={"system"}
edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest(
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

| Class variables             |                                                                         |
| --------------------------- | ----------------------------------------------------------------------- |
| `Config`                    | ` `                                                                     |
| `algorithm`                 | `pydantic.v1.types.StrictStr`                                           |
| `dataset`                   | `pydantic.v1.types.StrictStr`                                           |
| `design_space_tolerance`    | `float \| None`                                                         |
| `evaluation`                | `pydantic.v1.types.StrictStr`                                           |
| `max_generations`           | `pydantic.v1.types.StrictInt \| None`                                   |
| `objective_space_tolerance` | `float \| None`                                                         |
| `population`                | `pydantic.v1.types.StrictInt \| None`                                   |
| `termination_period`        | `pydantic.v1.types.StrictInt \| None`                                   |
| `variant`                   | `edgeimpulse_api.models.keras_model_variant_enum.KerasModelVariantEnum` |

***

**STATIC METHODS**

#### dataset\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest.dataset_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest
```

Create an instance of StartPostProcessingRequest from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest
```

Create an instance of StartPostProcessingRequest from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest.to_json(
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
edgeimpulse_api.models.start_post_processing_request.StartPostProcessingRequest.to_str(
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