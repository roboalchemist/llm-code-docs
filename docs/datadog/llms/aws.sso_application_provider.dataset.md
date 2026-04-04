# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sso_application_provider.dataset.md

---
title: IAM Identity Center Application Provider
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > IAM Identity Center Application
  Provider
---

# IAM Identity Center Application Provider

IAM Identity Center Application Provider in AWS represents an external application that can be integrated with AWS IAM Identity Center (formerly AWS SSO). It defines the configuration and metadata needed for establishing trust and enabling single sign-on between AWS and the third-party application. This resource helps manage how users access external applications through IAM Identity Center, ensuring secure authentication and streamlined user access management.

```
aws.sso_application_provider
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                             | Description |
| ------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| application_provider_arn | core | string     | The ARN of the application provider.                                                                  |
| display_data             | core | json       | A structure that describes how IAM Identity Center represents the application provider in the portal. |
| federation_protocol      | core | string     | The protocol that the application provider uses to perform federation.                                |
| resource_server_config   | core | json       | A structure that describes the application provider's resource server.                                |
| tags                     | core | hstore_csv |
