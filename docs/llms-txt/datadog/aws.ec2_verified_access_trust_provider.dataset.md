# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_verified_access_trust_provider.dataset.md

---
title: EC2 Verified Access Trust Provider
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Verified Access Trust Provider
---

# EC2 Verified Access Trust Provider

EC2 Verified Access Trust Provider is an AWS resource that defines a trust relationship for Verified Access, a service that enables secure, identity-based access to applications without using a VPN. It integrates with identity providers or device-based trust systems to verify user or device attributes before granting access. This helps enforce zero-trust security policies by ensuring only authenticated and trusted entities can connect to protected applications.

```
aws.ec2_verified_access_trust_provider
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                  | Description |
| --------------------------------- | ---- | ---------- | -------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| creation_time                     | core | string     | The creation time.                                                         |
| description                       | core | string     | A description for the Amazon Web Services Verified Access trust provider.  |
| device_options                    | core | json       | The options for device-identity trust provider.                            |
| device_trust_provider_type        | core | string     | The type of device-based trust provider.                                   |
| last_updated_time                 | core | string     | The last updated time.                                                     |
| native_application_oidc_options   | core | json       | The OpenID Connect (OIDC) options.                                         |
| oidc_options                      | core | json       | The options for an OpenID Connect-compatible user-identity trust provider. |
| policy_reference_name             | core | string     | The identifier to be used when working with policy rules.                  |
| sse_specification                 | core | json       | The options in use for server side encryption.                             |
| tags                              | core | hstore_csv |
| trust_provider_type               | core | string     | The type of Verified Access trust provider.                                |
| user_trust_provider_type          | core | string     | The type of user-based trust provider.                                     |
| verified_access_trust_provider_id | core | string     | The ID of the Amazon Web Services Verified Access trust provider.          |
