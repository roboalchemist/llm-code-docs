# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/dsp_metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.dsp_metadata

## Classes

### DSPMetadata

```python  theme={"system"}
edgeimpulse_api.models.dsp_metadata.DSPMetadata(
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

| Class variables                 |                                                                                                    |
| ------------------------------- | -------------------------------------------------------------------------------------------------- |
| `Config`                        | ` `                                                                                                |
| `created`                       | `datetime.datetime`                                                                                |
| `dsp_config`                    | `Dict[str, pydantic.v1.types.StrictStr]`                                                           |
| `feature_count`                 | `pydantic.v1.types.StrictInt`                                                                      |
| `feature_explorer_job_failed`   | `pydantic.v1.types.StrictBool \| None`                                                             |
| `feature_explorer_job_id`       | `pydantic.v1.types.StrictInt \| None`                                                              |
| `feature_importance_job_failed` | `pydantic.v1.types.StrictBool \| None`                                                             |
| `feature_importance_job_id`     | `pydantic.v1.types.StrictInt \| None`                                                              |
| `feature_labels`                | `List[pydantic.v1.types.StrictStr] \| None`                                                        |
| `fft_used`                      | `List[pydantic.v1.types.StrictInt] \| None`                                                        |
| `frequency`                     | `float`                                                                                            |
| `generated`                     | `pydantic.v1.types.StrictBool`                                                                     |
| `included_samples`              | `List[edgeimpulse_api.models.dsp_metadata_included_samples_inner.DSPMetadataIncludedSamplesInner]` |
| `labels`                        | `List[pydantic.v1.types.StrictStr]`                                                                |
| `output_config`                 | `edgeimpulse_api.models.dsp_metadata_output_config.DSPMetadataOutputConfig`                        |
| `pad_zeros`                     | `pydantic.v1.types.StrictBool`                                                                     |
| `resampling_algorithm_version`  | `float \| None`                                                                                    |
| `window_count`                  | `pydantic.v1.types.StrictInt`                                                                      |
| `window_increase_ms`            | `pydantic.v1.types.StrictInt`                                                                      |
| `window_size_ms`                | `pydantic.v1.types.StrictInt`                                                                      |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_metadata.DSPMetadata.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.dsp_metadata.DSPMetadata
```

Create an instance of DSPMetadata from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                           |
| ------------------------------------------------- |
| `edgeimpulse_api.models.dsp_metadata.DSPMetadata` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_metadata.DSPMetadata.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.dsp_metadata.DSPMetadata
```

Create an instance of DSPMetadata from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                           |
| ------------------------------------------------- |
| `edgeimpulse_api.models.dsp_metadata.DSPMetadata` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.dsp_metadata.DSPMetadata.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.dsp_metadata.DSPMetadata.to_json(
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
edgeimpulse_api.models.dsp_metadata.DSPMetadata.to_str(
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