# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.artifactregistry_repository.dataset.md

---
title: Artifact Registry Repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Artifact Registry Repository
---

# Artifact Registry Repository

Artifact Registry Repository in GCP is a managed service for storing and managing build artifacts such as container images, language packages, and other dependencies. It provides secure, scalable, and regional storage with fine-grained access control and integration with CI/CD pipelines. This helps teams centralize artifact management, improve security, and streamline software delivery.

```
gcp.artifactregistry_repository
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                | Description |
| ----------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| ancestors                     | core | array<string> |
| cleanup_policy_dry_run        | core | bool          | Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository.                                                                                                                                                                                          |
| create_time                   | core | timestamp     | Output only. The time when the repository was created.                                                                                                                                                                                                                                   |
| datadog_display_name          | core | string        |
| description                   | core | string        | The user-provided description of the repository.                                                                                                                                                                                                                                         |
| disallow_unspecified_mode     | core | bool          | Optional. If this is true, an unspecified repo type will be treated as error rather than defaulting to standard.                                                                                                                                                                         |
| docker_config                 | core | json          | Docker repository config contains repository level configuration for the repositories of docker type.                                                                                                                                                                                    |
| format                        | core | string        | Optional. The format of packages that are stored in the repository.                                                                                                                                                                                                                      |
| kms_key_name                  | core | string        | The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created. |
| labels                        | core | array<string> | Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes.                |
| maven_config                  | core | json          | Maven repository config contains repository level configuration for the repositories of maven type.                                                                                                                                                                                      |
| mode                          | core | string        | Optional. The mode of the repository.                                                                                                                                                                                                                                                    |
| name                          | core | string        | The name of the repository, for example: `projects/p1/locations/us-central1/repositories/repo1`. For each location in a project, repository names must be unique.                                                                                                                        |
| organization_id               | core | string        |
| parent                        | core | string        |
| project_id                    | core | string        |
| project_number                | core | string        |
| region_id                     | core | string        |
| registry_uri                  | core | string        | Output only. The repository endpoint, for example: `us-docker.pkg.dev/my-proj/my-repo`.                                                                                                                                                                                                  |
| remote_repository_config      | core | json          | Configuration specific for a Remote Repository.                                                                                                                                                                                                                                          |
| resource_name                 | core | string        |
| satisfies_pzi                 | core | bool          | Output only. Whether or not this repository satisfies PZI.                                                                                                                                                                                                                               |
| satisfies_pzs                 | core | bool          | Output only. Whether or not this repository satisfies PZS.                                                                                                                                                                                                                               |
| size_bytes                    | core | int64         | Output only. The size, in bytes, of all artifact storage in this repository. Repositories that are generally available or in public preview use this to calculate storage costs.                                                                                                         |
| tags                          | core | hstore_csv    |
| update_time                   | core | timestamp     | Output only. The time when the repository was last updated.                                                                                                                                                                                                                              |
| virtual_repository_config     | core | json          | Configuration specific for a Virtual Repository.                                                                                                                                                                                                                                         |
| vulnerability_scanning_config | core | json          | Optional. Config and state for vulnerability scanning of resources within this Repository.                                                                                                                                                                                               |
| zone_id                       | core | string        |
