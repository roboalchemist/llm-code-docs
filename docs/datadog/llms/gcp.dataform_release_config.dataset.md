# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataform_release_config.dataset.md

---
title: Dataform ReleaseConfig
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataform ReleaseConfig
---

# Dataform ReleaseConfig

Dataform ReleaseConfig in Google Cloud defines the configuration for creating and managing Dataform releases. It specifies how Dataform workflows are built, tested, and deployed, including references to repositories, compilation settings, and scheduling options. This resource helps automate and standardize the release process for data transformation projects in BigQuery.

```
gcp.dataform_release_config
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| -------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| ancestors                        | core | array<string> |
| code_compilation_config          | core | json          | Optional. If set, fields of `code_compilation_config` override the default compilation settings that are specified in dataform.json.                                                                                                                                                                                                                                                                                                                                      |
| cron_schedule                    | core | string        | Optional. Optional schedule (in cron format) for automatic creation of compilation results.                                                                                                                                                                                                                                                                                                                                                                               |
| datadog_display_name             | core | string        |
| disabled                         | core | bool          | Optional. Disables automatic creation of compilation results.                                                                                                                                                                                                                                                                                                                                                                                                             |
| git_commitish                    | core | string        | Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` - a tag: `tag1` - a branch name: `branch1`                                                                                                                                                                                                                                                                     |
| internal_metadata                | core | string        | Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.                                                                                                                                                                                                                                                                                   |
| labels                           | core | array<string> |
| name                             | core | string        | Identifier. The release config's name.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| organization_id                  | core | string        |
| parent                           | core | string        |
| project_id                       | core | string        |
| project_number                   | core | string        |
| recent_scheduled_release_records | core | json          | Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.                                                                                                                                                                                                                                                          |
| region_id                        | core | string        |
| release_compilation_result       | core | string        | Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is automatically created from this release config (using cron_schedule), or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`. |
| resource_name                    | core | string        |
| tags                             | core | hstore_csv    |
| time_zone                        | core | string        | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC.                                                                                                                                                                                                                               |
| zone_id                          | core | string        |
