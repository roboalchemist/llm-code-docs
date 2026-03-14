# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/sample_proposed_changes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.sample_proposed_changes

## Classes

### SampleProposedChanges

```python  theme={"system"}
edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges(
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

| Class variables     |                                                                         |
| ------------------- | ----------------------------------------------------------------------- |
| `Config`            | ` `                                                                     |
| `bounding_boxes`    | `List[edgeimpulse_api.models.bounding_box.BoundingBox] \| None`         |
| `is_disabled`       | `pydantic.v1.types.StrictBool \| None`                                  |
| `label`             | `pydantic.v1.types.StrictStr \| None`                                   |
| `metadata`          | `Dict[str, pydantic.v1.types.StrictStr] \| None`                        |
| `structured_labels` | `List[edgeimpulse_api.models.structured_label.StructuredLabel] \| None` |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges
```

Create an instance of SampleProposedChanges from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges
```

Create an instance of SampleProposedChanges from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges.to_json(
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
edgeimpulse_api.models.sample_proposed_changes.SampleProposedChanges.to_str(
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