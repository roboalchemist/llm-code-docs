# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.signer_signing_profile.dataset.md

---
title: Signer Signing Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Signer Signing Profile
---

# Signer Signing Profile

A Signer Signing Profile in AWS is a resource that defines the code signing configuration used to sign software artifacts. It specifies details such as the signing platform, signature validity period, and policies for revocation. Signing profiles help ensure the integrity and authenticity of applications by applying cryptographic signatures, making them essential for secure software distribution and compliance.

```
aws.signer_signing_profile
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                       | Description |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | The Amazon Resource Name (ARN) for the signing profile.                                         |
| overrides                 | core | json       | A list of overrides applied by the target signing profile for signing operations.               |
| platform_display_name     | core | string     | A human-readable name for the signing platform associated with the signing profile.             |
| platform_id               | core | string     | The ID of the platform that is used by the target signing profile.                              |
| profile_name              | core | string     | The name of the target signing profile.                                                         |
| profile_version           | core | string     | The current version of the signing profile.                                                     |
| profile_version_arn       | core | string     | The signing profile ARN, including the profile version.                                         |
| revocation_record         | core | json       | Revocation information for a signing profile.                                                   |
| signature_validity_period | core | json       | The validity period for a signing job.                                                          |
| signing_material          | core | json       | The ARN of the certificate that the target profile uses for signing operations.                 |
| signing_parameters        | core | hstore     | A map of key-value pairs for signing operations that is attached to the target signing profile. |
| status                    | core | string     | The status of the target signing profile.                                                       |
| status_reason             | core | string     | Reason for the status of the target signing profile.                                            |
| tags                      | core | hstore_csv |
