# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networksecurity_gateway_security_policy_rule.dataset.md

---
title: GatewaySecurityPolicyRule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GatewaySecurityPolicyRule
---

# GatewaySecurityPolicyRule

GatewaySecurityPolicyRule is a Google Cloud resource that defines a rule within a Gateway Security Policy. It specifies conditions and actions used to control and secure traffic passing through a Google Cloud Gateway, such as allowing, denying, or redirecting requests based on defined match criteria.

```
gcp.networksecurity_gateway_security_policy_rule
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                              | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| application_matcher    | core | string        | Optional. CEL expression for matching on L7/application level criteria.                                                                                                                                                                                |
| basic_profile          | core | string        | Required. Profile which tells what the primitive action should be.                                                                                                                                                                                     |
| create_time            | core | timestamp     | Output only. Time when the rule was created.                                                                                                                                                                                                           |
| datadog_display_name   | core | string        |
| description            | core | string        | Optional. Free-text description of the resource.                                                                                                                                                                                                       |
| enabled                | core | bool          | Required. Whether the rule is enforced.                                                                                                                                                                                                                |
| labels                 | core | array<string> |
| name                   | core | string        | Required. Immutable. Name of the resource. ame is the full resource name so projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}/rules/{rule} rule should match the pattern: (^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). |
| organization_id        | core | string        |
| parent                 | core | string        |
| priority               | core | int64         | Required. Priority of the rule. Lower number corresponds to higher precedence.                                                                                                                                                                         |
| project_id             | core | string        |
| project_number         | core | string        |
| region_id              | core | string        |
| resource_name          | core | string        |
| session_matcher        | core | string        | Required. CEL expression for matching on session criteria.                                                                                                                                                                                             |
| tags                   | core | hstore_csv    |
| tls_inspection_enabled | core | bool          | Optional. Flag to enable TLS inspection of traffic matching on , can only be true if the parent GatewaySecurityPolicy references a TLSInspectionConfig.                                                                                                |
| update_time            | core | timestamp     | Output only. Time when the rule was updated.                                                                                                                                                                                                           |
| zone_id                | core | string        |
