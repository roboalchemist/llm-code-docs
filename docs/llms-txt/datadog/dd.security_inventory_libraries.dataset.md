# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.security_inventory_libraries.dataset.md

---
title: Security Inventory Libraries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Inventory Libraries
---

# Security Inventory Libraries

Dataset representing **libraries** registered in the Datadog Security Inventory. Each record describes a software package and its relation with the organization resources.

```
dd.security_inventory_libraries
```
Cloud Security Infrastructure Packages UI 
{% icon name="icon-external-link" /%}
 Code Security Libraries Inventory UI 
{% icon name="icon-external-link" /%}
 
## Fields

| Title                       | ID                          | Type | Data Type     | Description                                                                                                                                                                           |
| --------------------------- | --------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asset Name                  | asset_name                  | core | string        | Human-readable name of the resource that uses the library.                                                                                                                            |
| Asset Type                  | asset_type                  | core | string        | Human-readable type of the resource that uses the library.                                                                                                                            |
| Block Location File Names   | block_locations_file_names  | core | array<string> | List of file names where the library is declared as a dependency.                                                                                                                     |
| Code Locations              | code_locations              | core | json          | JSON array with exact locations inside the code where the library is referenced.                                                                                                      |
| Default Branch              | default_branch              | core | string        | Default branch of the repository where the library is detected (e.g., main, master).                                                                                                  |
| Ecosystem                   | ecosystem                   | core | string        | Package-manager ecosystem to which the library belongs (e.g., Maven, RubyGems, NuGet).                                                                                                |
| End-of-Life Date            | eol                         | core | timestamp     | Timestamp (epoch milliseconds) when the library is expected to reach or has reached EOL.                                                                                              |
| First Commit                | first_commit                | core | string        | Commit SHA where the library was seen for the first time in this resource.                                                                                                            |
| First Detection             | first_detection             | core | timestamp     | Timestamp (epoch milliseconds) when the library was detected for the first time.                                                                                                      |
| First Seen At               | first_seen_at               | core | timestamp     | Timestamp (epoch milliseconds) when the library metadata was ingested for the first time.                                                                                             |
| Homepage                    | homepage                    | core | string        | URL of the library's official homepage or repository.                                                                                                                                 |
| Language                    | language                    | core | string        | Primary programming language of the library (e.g., ruby, java, dotnet).                                                                                                               |
| Last Commit                 | last_commit                 | core | string        | Commit ID where the library was detected for the last time on this resource.                                                                                                          |
| Latest Version              | latest_version              | core | string        | Most recent version of the library that we are aware of in the public repository.                                                                                                     |
| Latest Version Publish Date | latest_version_publish_date | core | timestamp     | Timestamp (epoch milliseconds) when the latest_version was published.                                                                                                                 |
| Library Name                | library_name                | core | string        | Canonical name of the library (as declared by the package manager).                                                                                                                   |
| Library Normalized Name     | library_normalized_name     | core | string        | Lower-cased, normalized version of library_name, used for de-duplication.                                                                                                             |
| Library Version             | library_version             | core | string        | Exact version string of the library that is in use in the resource.                                                                                                                   |
| License                     | license                     | core | string        | Name of the license under which the library is distributed (e.g., MIT, Apache-2.0).                                                                                                   |
| License Type                | license_type                | core | string        | Categorization of the license (permissive, copyleft, proprietary, etc.).                                                                                                              |
| Modification Detected At    | modification_detected_at    | core | timestamp     | Timestamp (epoch milliseconds) when a change in the library (version, hash, etc.) was first observed.                                                                                 |
| Newer Versions Number       | newer_versions_number       | core | int64         | Number of newer versions available in the upstream repository.                                                                                                                        |
| OpenSSF Level               | openssf_level               | core | string        | Security level of the project according to the OpenSSF Best Practices Badge (e.g., NONE, PASSING, SILVER, GOLD).                                                                      |
| Popularity Level            | popularity_level            | core | string        | Internal ranking that reflects how popular the library is (e.g., TOP_100, HIGH, MEDIUM, LOW).                                                                                         |
| Posture                     | posture                     | core | json          | JSON structure with detailed posture evaluation marks (legal_mark, openssf_mark, popularity_mark, version_mark, etc.).                                                                |
| Publish Date                | publish_date                | core | timestamp     | Timestamp (epoch milliseconds) when the specific library_version was originally published upstream.                                                                                   |
| Package URL (purl)          | purl                        | core | string        | Standard purl that uniquely identifies the library and version (e.g., pkg:gem/rails@8.0.1).                                                                                           |
| Related Services            | related_services            | core | array<string> | Array with names of services that are directly related or dependent on this library.                                                                                                  |
| Relation                    | relation                    | core | string        | Type of dependency relationship with the resource (DIRECT, TRANSITIVE, NOT_SUPPORTED).                                                                                                |
| Repository                  | repository                  | core | string        | URL or identifier of the upstream repository hosting the library's source code.                                                                                                       |
| Risks                       | risks                       | core | array<string> | Array of risk identifiers for this library                                                                                                                                            |
| Root Parent Name            | root_parent_name            | core | string        | Name of the highest-level dependency that ultimately requires this library.                                                                                                           |
| Root Parent Version         | root_parent_version         | core | string        | Version of the root_parent_name that brings in this library.                                                                                                                          |
| Scope                       | scope                       | core | string        | Dependency scope in which the library is used (e.g., PRODUCTION, TEST, DEVELOPMENT).                                                                                                  |
| Service Source              | service_source              | core | string        | Origin service or code base that reported the library information.                                                                                                                    |
| Tool                        | tool                        | core | string        | Name of the tool that detected or generated the library metadata (e.g., SCA, INFRA).                                                                                                  |
| Tree Location               | tree_location               | core | string        | Position of the library in the dependency tree, expressed as a breadcrumb-like path (e.g., '1' for the direct dependency, '1_1' for its first transitive, '2_3_4' for deeper levels). |
| Version Number              | version_number              | core | int64         | Numeric representation of the library, useful for sorting (e.g., 800000001).                                                                                                          |
| Environment                 | env                         | core | string        | Coma separated string array of active environments of the resource impacted by the vulnerability (e.g., env:prod, env:staging).                                                       |
| Origin                      | origin                      | core | string        | Coma separated string array of sources of the data or detection pipeline (e.g., origin:sci, origin:APM).                                                                              |
| Extended Environment        | extended_env                | core | string        | Coma separated string array of billed environments of the resource impacted by the vulnerability."                                                                                    |
| Team                        | team                        | core | string        | Coma separated string array of owning or responsible teams for the resource impacted by the vulnerability (e.g., team:profiling, team:k9_sca).                                        |
| Repository Digest           | repo_digest                 | core | string        | Coma separated string array of digests of the container impacted by the vulnerability (e.g., repo_digest:sha256:â¦).                                                                   |
| Image Layer Digest          | image_layer_digest          | core | string        | Coma separated string array of digests of an individual layer within the container image impacted by the vulnerability (e.g., image_layer_digest:sha256:â¦).                           |
| Image Layer Diff ID         | image_layer_diff_id         | core | string        | Coma separated string array of diff IDs of layers within the container image impacted by the vulnerability (e.g., image_layer_diff_id:sha256:â¦).                                      |
