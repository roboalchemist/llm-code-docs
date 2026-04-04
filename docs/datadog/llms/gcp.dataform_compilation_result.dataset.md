# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataform_compilation_result.dataset.md

---
title: Dataform Compilation Result
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataform Compilation Result
---

# Dataform Compilation Result

Dataform Compilation Result in Google Cloud represents the output of compiling a Dataform workflow. It contains the processed SQLX files, dependency graph, and configuration details that define how data transformations will run in BigQuery. This resource helps validate and prepare Dataform projects before execution, ensuring that all definitions and dependencies are correctly resolved.

```
gcp.dataform_compilation_result
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                              | Description |
| ----------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| code_compilation_config | core | json          | Immutable. If set, fields of `code_compilation_config` override the default compilation settings that are specified in dataform.json.                                                                  |
| compilation_errors      | core | json          | Output only. Errors encountered during project compilation.                                                                                                                                            |
| create_time             | core | timestamp     | Output only. The timestamp of when the compilation result was created.                                                                                                                                 |
| data_encryption_state   | core | json          | Output only. Only set if the repository has a KMS Key.                                                                                                                                                 |
| datadog_display_name    | core | string        |
| dataform_core_version   | core | string        | Output only. The version of `@dataform/core` that was used for compilation.                                                                                                                            |
| git_commitish           | core | string        | Immutable. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` - a tag: `tag1` - a branch name: `branch1` |
| internal_metadata       | core | string        | Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.                |
| labels                  | core | array<string> |
| name                    | core | string        | Output only. The compilation result's name.                                                                                                                                                            |
| organization_id         | core | string        |
| parent                  | core | string        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| release_config          | core | string        | Immutable. The name of the release config to compile. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`.                                                                  |
| resolved_git_commit_sha | core | string        | Output only. The fully resolved Git commit SHA of the code that was compiled. Not set for compilation results whose source is a workspace.                                                             |
| resource_name           | core | string        |
| tags                    | core | hstore_csv    |
| workspace               | core | string        | Immutable. The name of the workspace to compile. Must be in the format `projects/*/locations/*/repositories/*/workspaces/*`.                                                                           |
| zone_id                 | core | string        |
