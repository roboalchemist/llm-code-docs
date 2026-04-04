# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/upload_portal_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.upload_portal_api

## Classes

### UploadPortalApi

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### create\_signed\_upload\_link

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi.create_signed_upload_link(
	self,
	portal_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})],
	create_signed_upload_link_request: edgeimpulse_api.models.create_signed_upload_link_request.CreateSignedUploadLinkRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_signed_upload_link_response.CreateSignedUploadLinkResponse
```

Create pre-signed S3 upload link

Creates a signed link to securely upload data to s3 bucket directly from the client.

| Parameters                          |                                                                                                          |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                                      |
| `portal_id`                         | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})]` |
| `create_signed_upload_link_request` | `edgeimpulse_api.models.create_signed_upload_link_request.CreateSignedUploadLinkRequest`                 |
| `**kwargs`                          | ` `                                                                                                      |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.create_signed_upload_link_response.CreateSignedUploadLinkResponse` |

#### delete\_portal\_file

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi.delete_portal_file(
	self,
	portal_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})],
	delete_portal_file_request: edgeimpulse_api.models.delete_portal_file_request.DeletePortalFileRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete file from portal

Delete a file from an upload portal (requires JWT auth).

| Parameters                   |                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                      |
| `portal_id`                  | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})]` |
| `delete_portal_file_request` | `edgeimpulse_api.models.delete_portal_file_request.DeletePortalFileRequest`                              |
| `**kwargs`                   | ` `                                                                                                      |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### download\_portal\_file

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi.download_portal_file(
	self,
	portal_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})],
	download_portal_file_request: edgeimpulse_api.models.download_portal_file_request.DownloadPortalFileRequest,
	**kwargs
) ‑> edgeimpulse_api.models.download_portal_file_response.DownloadPortalFileResponse
```

Download file from portal

Download a file from an upload portal (requires JWT auth). Will return a signed URL to the bucket.

| Parameters                     |                                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                      |
| `portal_id`                    | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})]` |
| `download_portal_file_request` | `edgeimpulse_api.models.download_portal_file_request.DownloadPortalFileRequest`                          |
| `**kwargs`                     | ` `                                                                                                      |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.download_portal_file_response.DownloadPortalFileResponse` |

#### get\_portal\_info

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi.get_portal_info(
	self,
	portal_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})],
	**kwargs
) ‑> edgeimpulse_api.models.portal_info_response.PortalInfoResponse
```

Portal info

Get information about a portal

| Parameters  |                                                                                                          |
| ----------- | -------------------------------------------------------------------------------------------------------- |
| `self`      | ` `                                                                                                      |
| `portal_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})]` |
| `**kwargs`  | ` `                                                                                                      |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.portal_info_response.PortalInfoResponse` |

#### list\_portal\_files\_in\_folder

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi.list_portal_files_in_folder(
	self,
	portal_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})],
	list_portal_files_in_folder_request: edgeimpulse_api.models.list_portal_files_in_folder_request.ListPortalFilesInFolderRequest,
	**kwargs
) ‑> edgeimpulse_api.models.list_portal_files_in_folder_response.ListPortalFilesInFolderResponse
```

List files in portal

List all files and directories in specified prefix.

| Parameters                            |                                                                                                          |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                      |
| `portal_id`                           | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})]` |
| `list_portal_files_in_folder_request` | `edgeimpulse_api.models.list_portal_files_in_folder_request.ListPortalFilesInFolderRequest`              |
| `**kwargs`                            | ` `                                                                                                      |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_portal_files_in_folder_response.ListPortalFilesInFolderResponse` |

#### rename\_portal\_file

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi.rename_portal_file(
	self,
	portal_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})],
	rename_portal_file_request: edgeimpulse_api.models.rename_portal_file_request.RenamePortalFileRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Rename file from portal

Rename a file on an upload portal (requires JWT auth).

| Parameters                   |                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                      |
| `portal_id`                  | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})]` |
| `rename_portal_file_request` | `edgeimpulse_api.models.rename_portal_file_request.RenamePortalFileRequest`                              |
| `**kwargs`                   | ` `                                                                                                      |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### view\_portal\_file

```python  theme={"system"}
edgeimpulse_api.api.upload_portal_api.UploadPortalApi.view_portal_file(
	self,
	portal_id: Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})],
	path: Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Path to file in portal', extra={})],
	**kwargs
) ‑> str
```

View file from portal

View a file that's located in an upload portal (requires JWT auth). File might be converted (e.g. Parquet) or truncated (e.g. CSV).

| Parameters  |                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------- |
| `self`      | ` `                                                                                                                   |
| `portal_id` | `Annotated[pydantic.v1.types.StrictInt, FieldInfo(default=Ellipsis, description='Portal ID', extra={})]`              |
| `path`      | `Annotated[pydantic.v1.types.StrictStr, FieldInfo(default=Ellipsis, description='Path to file in portal', extra={})]` |
| `**kwargs`  | ` `                                                                                                                   |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).