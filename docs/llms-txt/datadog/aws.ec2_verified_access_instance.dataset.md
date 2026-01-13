# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_verified_access_instance.dataset.md

---
title: EC2 Verified Access Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Verified Access Instance
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_verified_access_instance.dataset/index.html
---

# EC2 Verified Access Instance

An EC2 Verified Access Instance is an AWS resource that provides secure, direct access to applications without requiring a traditional VPN. It uses policies to verify user identity and device posture before granting access, helping organizations enforce zero-trust principles. This service simplifies secure connectivity for end users while reducing the complexity of managing network-based access controls.

```
aws.ec2_verified_access_instance
```

## Fields

| Title                            | ID   | Type   | Data Type                                                                                                 | Description |
| -------------------------------- | ---- | ------ | --------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string |
| account_id                       | core | string |
| cidr_endpoints_custom_sub_domain | core | json   | The custom subdomain.                                                                                     |
| creation_time                    | core | string | The creation time.                                                                                        |
| description                      | core | string | A description for the Amazon Web Services Verified Access instance.                                       |
| fips_enabled                     | core | bool   | Indicates whether support for Federal Information Processing Standards (FIPS) is enabled on the instance. |
| last_updated_time                | core | string | The last updated time.                                                                                    |
| tags                             | core | hstore |
| verified_access_instance_id      | core | string | The ID of the Amazon Web Services Verified Access instance.                                               |
| verified_access_trust_providers  | core | json   | The IDs of the Amazon Web Services Verified Access trust providers.                                       |
