# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/preview_default_files_in_folder_response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.preview_default_files_in_folder_response

## Classes

### PreviewDefaultFilesInFolderResponse

```python  theme={"system"}
edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse(
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

| Class variables     |                                                       |
| ------------------- | ----------------------------------------------------- |
| `Config`            | ` `                                                   |
| `error`             | `pydantic.v1.types.StrictStr \| None`                 |
| `files`             | `List[edgeimpulse_api.models.portal_file.PortalFile]` |
| `is_truncated`      | `pydantic.v1.types.StrictBool \| None`                |
| `success`           | `pydantic.v1.types.StrictBool`                        |
| `truncation_reason` | `pydantic.v1.types.StrictStr \| None`                 |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse
```

Create an instance of PreviewDefaultFilesInFolderResponse from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse
```

Create an instance of PreviewDefaultFilesInFolderResponse from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse` |

#### truncation\_reason\_validate\_enum

```python  theme={"system"}
edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse.truncation_reason_validate_enum(
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
edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse.to_json(
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
edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse.to_str(
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