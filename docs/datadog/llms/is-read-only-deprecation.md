# Source: https://docs.datadoghq.com/dashboards/guide/is-read-only-deprecation.md

---
title: 'Dashboards API: Migrate from is_read_only'
description: >-
  Migrate from deprecated is_read_only attribute to restricted_roles or
  Restriction Policies for dashboard access control.
breadcrumbs: >-
  Docs > Dashboards > Graphing Guides > Dashboards API: Migrate from
  is_read_only
---

# Dashboards API: Migrate from is_read_only

## Overview{% #overview %}

Datadog is removing support for the `is_read_only` attribute in the Dashboards API's. For customers who manage Dashboards with the API directly, Datadog recommends that you transition to `restricted_roles` or Restriction Policies.

## Actions to take{% #actions-to-take %}

Migrate off of `is_read_only` to `restricted_roles` or consider participating in Preview for Restriction Policies.

### Migrate to `restricted_roles`{% #migrate-to-restricted_roles %}

The `restricted_roles` parameter allows Dashboard owners to assign specific permissions to users with roles.

Migrating to `restricted_roles` can be done independently. For more information, see the [Dashboard API](https://docs.datadoghq.com/api/latest/dashboards/) documentation.

### Restriction Policies{% #restriction-policies %}

Restriction Policies for Dashboards defines the access control rules for a resource. It maps a set of relations (editor and viewer) to a set of allowed principals (roles, teams, or users).

If you're managing Dashboards through Terraform:

1. Ensure that you're using Datadog Terraform Provider v3.27.0 or higher.
1. Remove `is_read_only` and `restricted_role` from your Dashboard Terraform resources.
1. Create a new [datadog_restriction_policy](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/restriction_policy) resource, referencing the respective Dashboard id and principals from the recently removed attributes.
1. Run `terraform apply`.

For an example of a Terraform resources, see the guide on [How to use Terraform to restrict the editing of a dashboard](https://docs.datadoghq.com/dashboards/guide/how-to-use-terraform-to-restrict-dashboard-edit/#restricting-a-dashboard-using-a-restriction-policy).

## Further reading{% #further-reading %}

- [How to use Terraform to restrict the editing of a dashboard](https://docs.datadoghq.com/dashboards/guide/how-to-use-terraform-to-restrict-dashboard-edit/)
- [Restriction Policies](https://docs.datadoghq.com/api/latest/restriction-policies/)
