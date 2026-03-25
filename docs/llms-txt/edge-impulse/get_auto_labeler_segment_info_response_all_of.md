# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_auto_labeler_segment_info_response_all_of.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# get_auto_labeler_segment_info_response_all_of

## GetAutoLabelerSegmentInfoResponseAllOf

```python  theme={"system"}
class edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.GetAutoLabelerSegmentInfoResponseAllOf(
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

* `image_url: pydantic.types.StrictStr`

* `sample: edgeimpulse_api.models.sample.Sample`

* `segments: List[edgeimpulse_api.models.auto_labeler_segment.AutoLabelerSegment]`

## Static methods

### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.from_dict(
		obj: dict
) ‑> edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.GetAutoLabelerSegmentInfoResponseAllOf
```

Create an instance of GetAutoLabelerSegmentInfoResponseAllOf from a dict

**Parameters**

* obj: dict

**Return**

edgeimpulse\_api.models.get\_auto\_labeler\_segment\_info\_response\_all\_of.GetAutoLabelerSegmentInfoResponseAllOf

### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.from_json(
		json_str: str
) ‑> edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.GetAutoLabelerSegmentInfoResponseAllOf
```

Create an instance of GetAutoLabelerSegmentInfoResponseAllOf from a JSON string

**Parameters**

* json\_str: str

**Return**

edgeimpulse\_api.models.get\_auto\_labeler\_segment\_info\_response\_all\_of.GetAutoLabelerSegmentInfoResponseAllOf

## Methods

### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.to_dict(
		self
)
```

Returns the dictionary representation of the model using alias

**Parameters**

* self

### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.to_json(
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
edgeimpulse_api.models.get_auto_labeler_segment_info_response_all_of.to_str(
		self
) ‑> str
```

Returns the string representation of the model using alias

**Parameters**

* self

**Return**

str


Built with [Mintlify](https://mintlify.com).