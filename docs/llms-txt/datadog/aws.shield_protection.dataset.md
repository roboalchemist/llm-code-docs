# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.shield_protection.dataset.md

---
title: Shield Protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Shield Protection
---

# Shield Protection

AWS Shield Protection is a resource that provides DDoS protection for AWS applications. It allows you to associate protection with specific AWS resources such as Elastic IPs, CloudFront distributions, or Route 53 hosted zones. This helps safeguard applications against network and transport layer attacks, reducing downtime and improving availability.

```
aws.shield_protection
```

## Fields

| Title                                              | ID   | Type          | Data Type                                                                                                                                                                                                                                                                         | Description |
| -------------------------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                               | core | string        |
| account_id                                         | core | string        |
| application_layer_automatic_response_configuration | core | json          | The automatic application layer DDoS mitigation settings for the protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks. |
| health_check_ids                                   | core | array<string> | The unique identifier (ID) for the Route 53 health check that's associated with the protection.                                                                                                                                                                                   |
| id                                                 | core | string        | The unique identifier (ID) of the protection.                                                                                                                                                                                                                                     |
| name                                               | core | string        | The name of the protection. For example, My CloudFront distributions.                                                                                                                                                                                                             |
| protection_arn                                     | core | string        | The ARN (Amazon Resource Name) of the protection.                                                                                                                                                                                                                                 |
| resource_arn                                       | core | string        | The ARN (Amazon Resource Name) of the Amazon Web Services resource that is protected.                                                                                                                                                                                             |
| tags                                               | core | hstore_csv    |
