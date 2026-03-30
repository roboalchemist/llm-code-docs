# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/project_info_response_all_of_acquisition_settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.project_info_response_all_of_acquisition_settings

## Classes

### ProjectInfoResponseAllOfAcquisitionSettings

```python  theme={"system"}
edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings(
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

| Class variables              |                                       |
| ---------------------------- | ------------------------------------- |
| `Config`                     | ` `                                   |
| `default_page_size`          | `pydantic.v1.types.StrictInt`         |
| `grid_column_count`          | `pydantic.v1.types.StrictInt`         |
| `grid_column_count_detailed` | `pydantic.v1.types.StrictInt`         |
| `inline_edit_bounding_boxes` | `pydantic.v1.types.StrictBool`        |
| `interval_ms`                | `float`                               |
| `label`                      | `pydantic.v1.types.StrictStr \| None` |
| `length_ms`                  | `pydantic.v1.types.StrictInt`         |
| `segment_length`             | `float \| None`                       |
| `segment_shift`              | `pydantic.v1.types.StrictBool`        |
| `sensor`                     | `pydantic.v1.types.StrictStr \| None` |
| `show_exact_sample_length`   | `pydantic.v1.types.StrictBool`        |
| `view_type`                  | `pydantic.v1.types.StrictStr`         |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings
```

Create an instance of ProjectInfoResponseAllOfAcquisitionSettings from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings
```

Create an instance of ProjectInfoResponseAllOfAcquisitionSettings from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings` |

#### view\_type\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings.view_type_validate_enum(
	v
)
```

| Parameters |     |
| ---------- | --- |
| `v`        | ` ` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings.to_json(
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
edgeimpulse_api.models.project_info_response_all_of_acquisition_settings.ProjectInfoResponseAllOfAcquisitionSettings.to_str(
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