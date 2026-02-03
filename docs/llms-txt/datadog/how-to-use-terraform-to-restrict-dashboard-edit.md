# Source: https://docs.datadoghq.com/dashboards/guide/how-to-use-terraform-to-restrict-dashboard-edit.md

---
title: How to use Terraform to restrict the editing of a dashboard
description: >-
  Use the restricted_roles attribute in Terraform to control dashboard editing
  permissions for specific user roles.
breadcrumbs: >-
  Docs > Dashboards > Graphing Guides > How to use Terraform to restrict the
  editing of a dashboard
---

# How to use Terraform to restrict the editing of a dashboard

## Restricting a dashboard using the restricted_roles attribute{% #restricting-a-dashboard-using-the-restricted_roles-attribute %}

The `restricted_roles` attribute can be used to restrict editing of the dashboard to specific roles. The field takes a list of IDs of roles, and authorizes any associated users.

Example usage:

```hcl
resource "datadog_dashboard" "example" {
  title         = "Example dashboard"
  restricted_roles = ["<role_id_1>", "<role_id_2>"]
}
```

**Note**: The `is_read_only` attribute is deprecated. It is recommended to use the `restricted_roles` attribute or restriction policies to manage access to your dashboards.

## Restricting a dashboard using a restriction policy{% #restricting-a-dashboard-using-a-restriction-policy %}

{% alert level="danger" %}
Restriction policies are in Preview. Contact [Datadog Support](https://docs.datadoghq.com/help/) or your Customer Success Manager for access.
{% /alert %}

[Restriction Policies](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/restriction_policy) allow you to restrict the editing of dashboards and other resources to specific principals, including roles, teams, users, and service accounts.

Example usage:

```hcl
resource "datadog_dashboard" "example" {
  title         = "Example dashboard"
  # Do not use restricted_roles or is_read_only attributes
}

resource "datadog_restriction_policy" "example" {
 resource_id = "dashboard:${datadog_dashboard.example.id}"
  bindings {
     principals = ["org:<org_id>"]
     relation = "viewer"
  }
  bindings {
     principals = ["role:<role_id_1>", "role:<role_id_2>"]
     relation = "editor"
  }
}
```

Role IDs can be retrieved from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles), [Roles UI](https://app.datadoghq.com/organization-settings/roles), or by using the role ID defined in Terraform for [datadog_role](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/role) resources.

Org ID can be obtained from the [GET /api/v2/current_user API](https://app.datadoghq.com/api/v2/current_user) request. Find it in the `data.relationships.org.data.id` field.
