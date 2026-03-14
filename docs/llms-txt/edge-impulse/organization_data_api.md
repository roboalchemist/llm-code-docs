# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/organization_data_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.organization_data_api

## Classes

### OrganizationDataApi

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### add\_organization\_bucket

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.add_organization_bucket(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	add_organization_bucket_request: edgeimpulse_api.models.add_organization_bucket_request.AddOrganizationBucketRequest,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add a storage bucket

Add a storage bucket.

| Parameters                        |                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                            | ` `                                                                                                                 |
| `organization_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `add_organization_bucket_request` | `edgeimpulse_api.models.add_organization_bucket_request.AddOrganizationBucketRequest`                               |
| `**kwargs`                        | ` `                                                                                                                 |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### add\_organization\_data\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.add_organization_data_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	files: List[Annotated[bytes, Strict(strict=True)]],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Add files

Add a new file to an existing data item.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`         |
| `files`           | `List[Annotated[bytes, Strict(strict=True)]]`                                                                       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### add\_organization\_data\_folder

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.add_organization_data_folder(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	organization_add_data_folder_request: edgeimpulse_api.models.organization_add_data_folder_request.OrganizationAddDataFolderRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Add data items from bucket

Bulk adds data items that already exist in a storage bucket. The bucket path specified should contain folders. Each folder is added as a data item in Edge Impulse.

| Parameters                             |                                                                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                 | ` `                                                                                                                 |
| `organization_id`                      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `organization_add_data_folder_request` | `edgeimpulse_api.models.organization_add_data_folder_request.OrganizationAddDataFolderRequest`                      |
| `**kwargs`                             | ` `                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### add\_organization\_data\_item

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.add_organization_data_item(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	name: Annotated[str, Strict(strict=True)],
	dataset: Annotated[str, Strict(strict=True)],
	metadata: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Key-value pair of metadata (in JSON format)')],
	files: List[Annotated[bytes, Strict(strict=True)]],
	bucket_id: Annotated[int, Strict(strict=True)] | None = None,
	bucket_name: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Name of the bucket name (as an Edge Impulse name)')] = None,
	bucket_path: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Optional path in the bucket to create this data item (files are created under this path).')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.entity_created_response.EntityCreatedResponse
```

Add new data

Add a new data item. You can add a maximum of 10000 files directly through this API. Use `addOrganizationDataFile` to add additional files.

| Parameters        |                                                                                                                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                     |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                     |
| `name`            | `Annotated[str, Strict(strict=True)]`                                                                                                                                                                                   |
| `dataset`         | `Annotated[str, Strict(strict=True)]`                                                                                                                                                                                   |
| `metadata`        | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Key-value pair of metadata (in JSON format)')]`                                                                         |
| `files`           | `List[Annotated[bytes, Strict(strict=True)]]`                                                                                                                                                                           |
| `bucket_id`       | `Annotated[int, Strict(strict=True)] \| None = None`                                                                                                                                                                    |
| `bucket_name`     | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Name of the bucket name (as an Edge Impulse name)')] = None`                                         |
| `bucket_path`     | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Optional path in the bucket to create this data item (files are created under this path).')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                     |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.entity_created_response.EntityCreatedResponse` |

#### add\_organization\_dataset

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.add_organization_dataset(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	organization_add_dataset_request: edgeimpulse_api.models.organization_add_dataset_request.OrganizationAddDatasetRequest,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Add dataset

Add a new research dataset

| Parameters                         |                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                                                 |
| `organization_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `organization_add_dataset_request` | `edgeimpulse_api.models.organization_add_dataset_request.OrganizationAddDatasetRequest`                             |
| `**kwargs`                         | ` `                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### change\_dataset\_organization\_data\_items

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.change_dataset_organization_data_items(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_ids: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')],
	set_organization_data_dataset_request: edgeimpulse_api.models.set_organization_data_dataset_request.SetOrganizationDataDatasetRequest,
	dataset: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None,
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Change dataset

Change the dataset for selected data items.

| Parameters                              |                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                  | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `data_ids`                              | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')]`                                                                                                                                                                                                                            |
| `set_organization_data_dataset_request` | `edgeimpulse_api.models.set_organization_data_dataset_request.SetOrganizationDataDatasetRequest`                                                                                                                                                                                                                                                    |
| `dataset`                               | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None`                                                                                                                                                                                                      |
| `filter`                                | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `**kwargs`                              | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### clear\_checklist\_organization\_data\_items

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.clear_checklist_organization_data_items(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_ids: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')],
	dataset: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None,
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Clear checklist for data

Clear all checklist flags for selected data items.

| Parameters        |                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `data_ids`        | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')]`                                                                                                                                                                                                                            |
| `dataset`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None`                                                                                                                                                                                                      |
| `filter`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### create\_signed\_upload\_link\_dataset

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.create_signed_upload_link_dataset(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	create_signed_upload_link_request: edgeimpulse_api.models.create_signed_upload_link_request.CreateSignedUploadLinkRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_signed_upload_link_response.CreateSignedUploadLinkResponse
```

Create pre-signed S3 upload link

Creates a signed link to securely upload data to s3 bucket directly from the client.

| Parameters                          |                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                                                 |
| `organization_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`                           | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `create_signed_upload_link_request` | `edgeimpulse_api.models.create_signed_upload_link_request.CreateSignedUploadLinkRequest`                            |
| `**kwargs`                          | ` `                                                                                                                 |

| Returns                                                                                    |
| ------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.create_signed_upload_link_response.CreateSignedUploadLinkResponse` |

#### delete\_dataset\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.delete_dataset_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	delete_portal_file_request: edgeimpulse_api.models.delete_portal_file_request.DeletePortalFileRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete file from dataset

Delete a file from a dataset

| Parameters                   |                                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                 |
| `organization_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`                    | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `delete_portal_file_request` | `edgeimpulse_api.models.delete_portal_file_request.DeletePortalFileRequest`                                         |
| `**kwargs`                   | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_data\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.delete_organization_data_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	file_name: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='File name')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete file

Delete a single file from a data item.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`         |
| `file_name`       | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='File name')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_data\_item

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.delete_organization_data_item(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete data

Delete a data item. This will remove items the items from the underlying storage if your dataset has "bucketPath" set.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`         |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_organization\_data\_items

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.delete_organization_data_items(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_ids: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')],
	dataset: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None,
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Delete data

Delete all data for selected data items. This removes all data in the underlying data bucket.

| Parameters        |                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `data_ids`        | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')]`                                                                                                                                                                                                                            |
| `dataset`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None`                                                                                                                                                                                                      |
| `filter`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### download\_dataset\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.download_dataset_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	download_portal_file_request: edgeimpulse_api.models.download_portal_file_request.DownloadPortalFileRequest,
	**kwargs
) ‑> edgeimpulse_api.models.download_portal_file_response.DownloadPortalFileResponse
```

Download file from dataset

Download a file from a dataset. Will return a signed URL to the bucket.

| Parameters                     |                                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                                                                 |
| `organization_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`                      | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `download_portal_file_request` | `edgeimpulse_api.models.download_portal_file_request.DownloadPortalFileRequest`                                     |
| `**kwargs`                     | ` `                                                                                                                 |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.download_portal_file_response.DownloadPortalFileResponse` |

#### download\_dataset\_folder

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.download_dataset_folder(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	path: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Path, relative to dataset')],
	**kwargs
) ‑> str
```

Download folder from dataset

Download all files in the given folder in a dataset, ignoring any subdirectories.

| Parameters        |                                                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                           |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`           |
| `dataset`         | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`              |
| `path`            | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Path, relative to dataset')]` |
| `**kwargs`        | ` `                                                                                                                           |

| Returns |
| ------- |
| `str`   |

#### download\_organization\_data\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.download_organization_data_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	file_name: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='File name')],
	**kwargs
) ‑> str
```

Download file

Download a single file from a data item.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`         |
| `file_name`       | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='File name')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns |
| ------- |
| `str`   |

#### download\_organization\_data\_item

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.download_organization_data_item(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_ids: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')],
	dataset: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None,
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	**kwargs
) ‑> str
```

Download data

Download all data for selected data items. This function does not query the underlying bucket.

| Parameters        |                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `data_ids`        | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data IDs as an Array')]`                                                                                                                                                                                                                            |
| `dataset`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None`                                                                                                                                                                                                      |
| `filter`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns |
| ------- |
| `str`   |

#### download\_organization\_single\_data\_item

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.download_organization_single_data_item(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	**kwargs
) ‑> str
```

Download data

Download all data for this data item.

| Parameters        |                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`                                                                                                                                                                                                                                         |
| `filter`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns |
| ------- |
| `str`   |

#### get\_organization\_bucket

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.get_organization_bucket(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	bucket_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_bucket_response.GetOrganizationBucketResponse
```

Get storage bucket

Get storage bucket details.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `bucket_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_bucket_response.GetOrganizationBucketResponse` |

#### get\_organization\_data\_item

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.get_organization_data_item(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_item_response.GetOrganizationDataItemResponse
```

Get data metadata

Get a data item. This will HEAD the underlying bucket to retrieve the last file information.

| Parameters        |                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`                                                                                                                                                                                                                                         |
| `filter`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_data_item_response.GetOrganizationDataItemResponse` |

#### get\_organization\_data\_item\_transform\_jobs

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.get_organization_data_item_transform_jobs(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_data_item_transform_jobs_response.GetOrganizationDataItemTransformJobsResponse
```

Get transformation jobs for data item

Get all transformation jobs that ran for a data item. If limit / offset is not provided then max. 20 results are returned.

| Parameters        |                                                                                                                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                         |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                         |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`                                                                                                                 |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                     |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None` |
| `**kwargs`        | ` `                                                                                                                                                                                                                         |

| Returns                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_organization_data_item_transform_jobs_response.GetOrganizationDataItemTransformJobsResponse` |

#### get\_organization\_dataset

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.get_organization_dataset(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	**kwargs
) ‑> edgeimpulse_api.models.get_organization_dataset_response.GetOrganizationDatasetResponse
```

Get dataset

Get information about a dataset

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`         | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                   |
| ----------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_organization_dataset_response.GetOrganizationDatasetResponse` |

#### hide\_organization\_dataset

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.hide_organization_dataset(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Hide dataset

Hide a dataset (does not remove underlying data)

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`         | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### list\_dataset\_files\_in\_folder

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.list_dataset_files_in_folder(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	list_portal_files_in_folder_request: edgeimpulse_api.models.list_portal_files_in_folder_request.ListPortalFilesInFolderRequest,
	**kwargs
) ‑> edgeimpulse_api.models.list_portal_files_in_folder_response.ListPortalFilesInFolderResponse
```

List files in dataset

List all files and directories in specified prefix.

| Parameters                            |                                                                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                                 |
| `organization_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`                             | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `list_portal_files_in_folder_request` | `edgeimpulse_api.models.list_portal_files_in_folder_request.ListPortalFilesInFolderRequest`                         |
| `**kwargs`                            | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_portal_files_in_folder_response.ListPortalFilesInFolderResponse` |

#### list\_organization\_buckets

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.list_organization_buckets(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_buckets_response.ListOrganizationBucketsResponse
```

List storage buckets

Retrieve all configured storage buckets. This does not list the secret key.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_buckets_response.ListOrganizationBucketsResponse` |

#### list\_organization\_data

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.list_organization_data(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None,
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_data_response.ListOrganizationDataResponse
```

List data

Lists all data items. This can be filtered by the ?filter parameter.

| Parameters        |                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `dataset`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None`                                                                                                                                                                                                      |
| `filter`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                                                                                                                                             |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None`                                                                                                                         |
| `**kwargs`        | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_data_response.ListOrganizationDataResponse` |

#### list\_organization\_files

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.list_organization_files(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None,
	filter: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None,
	limit: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None,
	offset: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_files_response.ListOrganizationFilesResponse
```

List files

Lists all files included by the filter.

| Parameters        |                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                                                                                                                                                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`                                                                                                                                                                                                                                 |
| `dataset`         | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Selected dataset')] = None`                                                                                                                                                                                                      |
| `filter`          | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description="Data filter in SQL WHERE format, where you can reference 'dataset', 'bucket', 'name', 'total_file_count', 'total_file_size', 'created' and any metadata label through 'metadata->' (dots are replaced by underscore).")] = None` |
| `limit`           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Maximum number of results')] = None`                                                                                                                                                                                             |
| `offset`          | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.')] = None`                                                                                                                         |
| `**kwargs`        | ` `                                                                                                                                                                                                                                                                                                                                                 |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_files_response.ListOrganizationFilesResponse` |

#### organization\_bulk\_update\_metadata

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.organization_bulk_update_metadata(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True)],
	csv_file: Annotated[str, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Bulk update metadata

Bulk update the metadata of many data items in one go. This requires you to submit a CSV file with headers, one of which the columns should be named 'name'. The other columns are used as metadata keys.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`         | `Annotated[str, Strict(strict=True)]`                                                                               |
| `csv_file`        | `Annotated[str, Strict(strict=True)]`                                                                               |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### preview\_default\_files\_in\_folder

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.preview_default_files_in_folder(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	preview_default_files_in_folder_request: edgeimpulse_api.models.preview_default_files_in_folder_request.PreviewDefaultFilesInFolderRequest,
	**kwargs
) ‑> edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse
```

Preview files in a default dataset

Preview files and directories in a default dataset for the given prefix, with support for wildcards. This is an internal API used when starting a transformation job.

| Parameters                                |                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                    | ` `                                                                                                                 |
| `organization_id`                         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`                                 | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `preview_default_files_in_folder_request` | `edgeimpulse_api.models.preview_default_files_in_folder_request.PreviewDefaultFilesInFolderRequest`                 |
| `**kwargs`                                | ` `                                                                                                                 |

| Returns                                                                                               |
| ----------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.preview_default_files_in_folder_response.PreviewDefaultFilesInFolderResponse` |

#### preview\_organization\_data\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.preview_organization_data_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	file_name: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='File name')],
	**kwargs
) ‑> str
```

Preview file

Preview a single file from a data item (same as downloadOrganizationDataFile but w/ content-disposition inline and could be truncated).

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `data_id`         | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`         |
| `file_name`       | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='File name')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns |
| ------- |
| `str`   |

#### refresh\_organization\_data

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.refresh_organization_data(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Selected dataset')],
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Refresh data

Update all data items. HEADs all underlying buckets to retrieve the last file information. Use this API after uploading data directly to S3. If your dataset has bucketId and bucketPath set then this will also remove items that have been removed from S3.

| Parameters        |                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                  |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`  |
| `dataset`         | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Selected dataset')]` |
| `**kwargs`        | ` `                                                                                                                  |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### remove\_organization\_bucket

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.remove_organization_bucket(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	bucket_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove storage bucket

Remove a storage bucket and associated datasets. This will render any data in this storage bucket unreachable.

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `bucket_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')]`       |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### rename\_dataset\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.rename_dataset_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	rename_portal_file_request: edgeimpulse_api.models.rename_portal_file_request.RenamePortalFileRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Rename file from dataset

Rename a file in a dataset

| Parameters                   |                                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                                 |
| `organization_id`            | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`                    | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `rename_portal_file_request` | `edgeimpulse_api.models.rename_portal_file_request.RenamePortalFileRequest`                                         |
| `**kwargs`                   | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_bucket

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.update_organization_bucket(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	bucket_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')],
	update_organization_bucket_request: edgeimpulse_api.models.update_organization_bucket_request.UpdateOrganizationBucketRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update storage bucket

Updates storage bucket details. This only updates fields that were set in the request body. Before updating the bucket details, it is required to verify the connection using the POST /api/organizations/`{organizationId}`/buckets/verify endpoint.  The verification process: 1. Call the verify endpoint with the new bucket details. 2. Poll the verify endpoint until it responds with `connectionStatus: connected`. 3. If the endpoint responds with `connectionStatus: error`, the verification has failed.  Only proceed with updating the bucket details after receiving a `connected` status. The polling interval and timeout should be determined based on your application's requirements.

| Parameters                           |                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                                 |
| `organization_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `bucket_id`                          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')]`       |
| `update_organization_bucket_request` | `edgeimpulse_api.models.update_organization_bucket_request.UpdateOrganizationBucketRequest`                         |
| `**kwargs`                           | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_data\_item

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.update_organization_data_item(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	data_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')],
	update_organization_data_item_request: edgeimpulse_api.models.update_organization_data_item_request.UpdateOrganizationDataItemRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update data metadata

Update the data item metadata.

| Parameters                              |                                                                                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                  | ` `                                                                                                                 |
| `organization_id`                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `data_id`                               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Data ID')]`         |
| `update_organization_data_item_request` | `edgeimpulse_api.models.update_organization_data_item_request.UpdateOrganizationDataItemRequest`                    |
| `**kwargs`                              | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_organization\_dataset

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.update_organization_dataset(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	update_organization_dataset_request: edgeimpulse_api.models.update_organization_dataset_request.UpdateOrganizationDatasetRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update dataset

Set information about a dataset

| Parameters                            |                                                                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                | ` `                                                                                                                 |
| `organization_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`                             | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `update_organization_dataset_request` | `edgeimpulse_api.models.update_organization_dataset_request.UpdateOrganizationDatasetRequest`                       |
| `**kwargs`                            | ` `                                                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### verify\_dataset

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.verify_dataset(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	**kwargs
) ‑> edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse
```

Verify dataset

Verify whether we can reach a dataset (and return some random files, used for data sources)

| Parameters        |                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                 |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `dataset`         | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`    |
| `**kwargs`        | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse` |

#### verify\_existing\_organization\_bucket

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.verify_existing_organization_bucket(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	bucket_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')],
	verify_organization_existing_bucket_request: edgeimpulse_api.models.verify_organization_existing_bucket_request.VerifyOrganizationExistingBucketRequest,
	**kwargs
) ‑> edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse
```

Verify existing bucket connectivity

Verify whether we can reach a bucket before adding it.

| Parameters                                    |                                                                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `self`                                        | ` `                                                                                                                 |
| `organization_id`                             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `bucket_id`                                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Bucket ID')]`       |
| `verify_organization_existing_bucket_request` | `edgeimpulse_api.models.verify_organization_existing_bucket_request.VerifyOrganizationExistingBucketRequest`        |
| `**kwargs`                                    | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse` |

#### verify\_organization\_bucket

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.verify_organization_bucket(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	verify_organization_bucket_request: edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest,
	**kwargs
) ‑> edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse
```

Verify bucket connectivity

Verify connectivity to a storage bucket and optionally list its contents. This endpoint allows you to: 1. Check if the provided bucket credentials are valid and the bucket is accessible. 2. Optionally list files in the bucket up to a specified limit. 3. Validate the bucket configuration before adding it to the organization.  The request can include details such as the bucket name, region, credentials, and listing options. The response provides information about the bucket's accessibility and, if requested, a list of files in the bucket.  Important note on verification process: - For S3-compatible storage backends: Verification is expected to be immediate. - For Azure buckets: Verification takes longer. Users are required to poll this endpoint until the connectionStatus changes from 'connecting' to 'connected'.  When dealing with Azure buckets, implement a polling mechanism to check the status periodically until it's confirmed as connected.

| Parameters                           |                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `self`                               | ` `                                                                                                                 |
| `organization_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]` |
| `verify_organization_bucket_request` | `edgeimpulse_api.models.verify_organization_bucket_request.VerifyOrganizationBucketRequest`                         |
| `**kwargs`                           | ` `                                                                                                                 |

| Returns                                                                                       |
| --------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.verify_organization_bucket_response.VerifyOrganizationBucketResponse` |

#### view\_dataset\_file

```python  theme={"system"}
edgeimpulse_api.api.organization_data_api.OrganizationDataApi.view_dataset_file(
	self,
	organization_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')],
	dataset: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')],
	path: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Path to file in portal')],
	**kwargs
) ‑> str
```

View file from dataset

View a file that's located in a dataset (requires JWT auth). File might be converted (e.g. Parquet) or truncated (e.g. CSV).

| Parameters        |                                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `self`            | ` `                                                                                                                        |
| `organization_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Organization ID')]`        |
| `dataset`         | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Dataset name')]`           |
| `path`            | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Path to file in portal')]` |
| `**kwargs`        | ` `                                                                                                                        |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).