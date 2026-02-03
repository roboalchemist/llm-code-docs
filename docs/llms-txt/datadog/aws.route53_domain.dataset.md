# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_domain.dataset.md

---
title: Route 53 Domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Route 53 Domain
---

# Route 53 Domain

This table represents the Route 53 Domain resource from Amazon Web Services.

```
aws.route53_domain
```

## Fields

| Title         | ID   | Type       | Data Type                                                                               | Description |
| ------------- | ---- | ---------- | --------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| auto_renew    | core | bool       | Indicates whether the domain is automatically renewed upon expiration.                  |
| domain_arn    | core | string     |
| domain_name   | core | string     | The name of the domain that the summary information applies to.                         |
| expiry        | core | timestamp  | Expiration date of the domain in Unix time format and Coordinated Universal Time (UTC). |
| tags          | core | hstore_csv |
| transfer_lock | core | bool       | Indicates whether a domain is locked from unauthorized transfer to another party.       |
