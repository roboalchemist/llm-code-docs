# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_ssl_policy.dataset.md

---
title: SSL Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SSL Policy
---

# SSL Policy

An SSL Policy in Google Cloud defines the SSL features and minimum TLS versions that can be used by load balancers. It allows you to control the security profile of connections between clients and your load balancer, ensuring compliance with organizational or regulatory requirements.

```
gcp.compute_ssl_policy
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                            |
| custom_features      | core | array<string> | A list of features enabled when the selected profile is CUSTOM. The method returns the set of features that can be specified in this list. This field must be empty if the profile is notCUSTOM.                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                   |
| enabled_features     | core | array<string> | Output only. [Output Only] The list of features enabled in the SSL policy.                                                                                                                                                                                                                                                                                                                      |
| id                   | core | string        | Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                    |
| kind                 | core | string        | Output only. [Output only] Type of the resource. Alwayscompute#sslPolicyfor SSL policies.                                                                                                                                                                                                                                                                                                       |
| labels               | core | array<string> |
| min_tls_version      | core | string        | The minimum version of SSL protocol that can be used by the clients to establish a connection with the load balancer. This can be one ofTLS_1_0, TLS_1_1, TLS_1_2,TLS_1_3. When set to TLS_1_3, the profile field must be set to RESTRICTED.                                                                                                                                                    |
| name                 | core | string        | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id      | core | string        |
| parent               | core | string        |
| profile              | core | string        | Profile specifies the set of SSL features that can be used by the load balancer when negotiating SSL with clients. This can be one ofCOMPATIBLE, MODERN, RESTRICTED, orCUSTOM. If using CUSTOM, the set of SSL features to enable must be specified in the customFeatures field.                                                                                                                |
| project_id           | core | string        |
| project_number       | core | string        |
| region               | core | string        | Output only. [Output Only] URL of the region where the regional SSL policy resides. This field is not applicable to global SSL policies.                                                                                                                                                                                                                                                        |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                 |
| tags                 | core | hstore_csv    |
| warnings             | core | json          | Output only. [Output Only] If potential misconfigurations are detected for this SSL policy, this field will be populated with warning messages.                                                                                                                                                                                                                                                 |
| zone_id              | core | string        |
