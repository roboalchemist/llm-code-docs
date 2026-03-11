# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/save_auto_labeler_clusters_request_clusters_inner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# save_auto_labeler_clusters_request_clusters_inner

## SaveAutoLabelerClustersRequestClustersInner

```python  theme={"system"}
class edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.SaveAutoLabelerClustersRequestClustersInner(
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

* `index: pydantic.types.StrictInt`

* `label: pydantic.types.StrictStr`

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.SaveAutoLabelerClustersRequestClustersInner
```

Create an instance of SaveAutoLabelerClustersRequestClustersInner from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.save\_auto\_labeler\_clusters\_request\_clusters\_inner.SaveAutoLabelerClustersRequestClustersInner

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.SaveAutoLabelerClustersRequestClustersInner
```

Create an instance of SaveAutoLabelerClustersRequestClustersInner from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.save\_auto\_labeler\_clusters\_request\_clusters\_inner.SaveAutoLabelerClustersRequestClustersInner

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.to_json(
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
edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).