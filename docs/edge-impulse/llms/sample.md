# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/sample.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.sample

## Classes

### Sample

```python  theme={"system"}
edgeimpulse_api.models.sample.Sample(
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

| Class variables                    |                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| `Config`                           | ` `                                                                            |
| `added`                            | `datetime.datetime`                                                            |
| `bounding_boxes`                   | `List[edgeimpulse_api.models.bounding_box.BoundingBox]`                        |
| `bounding_boxes_type`              | `pydantic.v1.types.StrictStr`                                                  |
| `category`                         | `edgeimpulse_api.models.raw_data_category.RawDataCategory`                     |
| `chart_type`                       | `pydantic.v1.types.StrictStr`                                                  |
| `coldstorage_filename`             | `pydantic.v1.types.StrictStr`                                                  |
| `created`                          | `datetime.datetime`                                                            |
| `created_by_synthetic_data_job_id` | `pydantic.v1.types.StrictInt \| None`                                          |
| `device_name`                      | `pydantic.v1.types.StrictStr \| None`                                          |
| `device_type`                      | `pydantic.v1.types.StrictStr`                                                  |
| `filename`                         | `pydantic.v1.types.StrictStr`                                                  |
| `frequency`                        | `float`                                                                        |
| `id`                               | `pydantic.v1.types.StrictInt`                                                  |
| `image_dimensions`                 | `edgeimpulse_api.models.sample_image_dimensions.SampleImageDimensions \| None` |
| `interval_ms`                      | `float`                                                                        |
| `is_cropped`                       | `pydantic.v1.types.StrictBool`                                                 |
| `is_disabled`                      | `pydantic.v1.types.StrictBool`                                                 |
| `is_processing`                    | `pydantic.v1.types.StrictBool`                                                 |
| `label`                            | `pydantic.v1.types.StrictStr`                                                  |
| `label_map`                        | `edgeimpulse_api.models.sample_label_map_labels.SampleLabelMapLabels \| None`  |
| `last_modified`                    | `datetime.datetime`                                                            |
| `metadata`                         | `Dict[str, pydantic.v1.types.StrictStr] \| None`                               |
| `original_frequency`               | `float`                                                                        |
| `original_interval_ms`             | `float`                                                                        |
| `processing_error`                 | `pydantic.v1.types.StrictBool`                                                 |
| `processing_error_string`          | `pydantic.v1.types.StrictStr \| None`                                          |
| `processing_job_id`                | `pydantic.v1.types.StrictInt \| None`                                          |
| `project_id`                       | `pydantic.v1.types.StrictInt`                                                  |
| `project_labeling_method`          | `edgeimpulse_api.models.project_labeling_method.ProjectLabelingMethod \| None` |
| `project_name`                     | `pydantic.v1.types.StrictStr \| None`                                          |
| `project_owner_name`               | `pydantic.v1.types.StrictStr \| None`                                          |
| `sensors`                          | `List[edgeimpulse_api.models.sensor.Sensor]`                                   |
| `sha256_hash`                      | `pydantic.v1.types.StrictStr`                                                  |
| `signature_key`                    | `pydantic.v1.types.StrictStr \| None`                                          |
| `signature_method`                 | `pydantic.v1.types.StrictStr \| None`                                          |
| `signature_validate`               | `pydantic.v1.types.StrictBool`                                                 |
| `structured_labels`                | `List[edgeimpulse_api.models.structured_label.StructuredLabel] \| None`        |
| `structured_labels_list`           | `List[pydantic.v1.types.StrictStr] \| None`                                    |
| `thumbnail_video`                  | `pydantic.v1.types.StrictStr \| None`                                          |
| `thumbnail_video_full`             | `pydantic.v1.types.StrictStr \| None`                                          |
| `total_length_ms`                  | `float \| None`                                                                |
| `values_count`                     | `pydantic.v1.types.StrictInt`                                                  |
| `video_url`                        | `pydantic.v1.types.StrictStr \| None`                                          |
| `video_url_full`                   | `pydantic.v1.types.StrictStr \| None`                                          |

***

**STATIC METHODS**

#### bounding\_boxes\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.sample.Sample.bounding_boxes_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### chart\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.sample.Sample.chart_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.sample.Sample.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.sample.Sample
```

Create an instance of Sample from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                |
| -------------------------------------- |
| `edgeimpulse_api.models.sample.Sample` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.sample.Sample.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.sample.Sample
```

Create an instance of Sample from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                |
| -------------------------------------- |
| `edgeimpulse_api.models.sample.Sample` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.sample.Sample.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.sample.Sample.to_json(
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
edgeimpulse_api.models.sample.Sample.to_str(
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