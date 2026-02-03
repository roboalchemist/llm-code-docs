# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataform_repository.dataset.md

---
title: Dataform Repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataform Repository
---

# Dataform Repository

A Dataform Repository in Google Cloud is a managed workspace for organizing and versioning SQL workflows used in data transformation. It allows teams to define, test, and schedule transformations on BigQuery data using a structured, code-based approach.

```
gcp.dataform_repository
```

## Fields

| Title                                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                       | core | string        |
| ancestors                                  | core | array<string> |
| create_time                                | core | timestamp     | Output only. The timestamp of when the repository was created.                                                                                                                                                                                                                                                                        |
| data_encryption_state                      | core | json          | Output only. A data encryption state of a Git repository if this Repository is protected by a KMS key.                                                                                                                                                                                                                                |
| datadog_display_name                       | core | string        |
| gcp_display_name                           | core | string        | Optional. The repository's user-friendly name.                                                                                                                                                                                                                                                                                        |
| git_remote_settings                        | core | json          | Optional. If set, configures this repository to be linked to a Git remote.                                                                                                                                                                                                                                                            |
| internal_metadata                          | core | string        | Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.                                                                                                                                               |
| kms_key_name                               | core | string        | Optional. The reference to a KMS encryption key. If provided, it will be used to encrypt user data in the repository and all child resources. It is not possible to add or update the encryption key after the repository is created. Example: `projects/{kms_project}/locations/{location}/keyRings/{key_location}/cryptoKeys/{key}` |
| labels                                     | core | array<string> | Optional. Repository user labels.                                                                                                                                                                                                                                                                                                     |
| name                                       | core | string        | Identifier. The repository's name.                                                                                                                                                                                                                                                                                                    |
| npmrc_environment_variables_secret_version | core | string        | Optional. The name of the Secret Manager secret version to be used to interpolate variables into the .npmrc file for package installation operations. Must be in the format `projects/*/secrets/*/versions/*`. The file itself must be in a JSON format.                                                                              |
| organization_id                            | core | string        |
| parent                                     | core | string        |
| project_id                                 | core | string        |
| project_number                             | core | string        |
| region_id                                  | core | string        |
| resource_name                              | core | string        |
| service_account                            | core | string        | Optional. The service account to run workflow invocations under.                                                                                                                                                                                                                                                                      |
| set_authenticated_user_admin               | core | bool          | Optional. Input only. If set to true, the authenticated user will be granted the roles/dataform.admin role on the created repository. To modify access to the created repository later apply setIamPolicy from https://cloud.google.com/dataform/reference/rest#rest-resource:-v1beta1.projects.locations.repositories                |
| tags                                       | core | hstore_csv    |
| workspace_compilation_overrides            | core | json          | Optional. If set, fields of `workspace_compilation_overrides` override the default compilation settings that are specified in dataform.json when creating workspace-scoped compilation results. See documentation for `WorkspaceCompilationOverrides` for more information.                                                           |
| zone_id                                    | core | string        |
