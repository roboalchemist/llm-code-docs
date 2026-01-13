# Source: https://docs.datadoghq.com/account_management/rbac/granular_access.md

---
title: Granular Access Control
description: >-
  Control access to individual Datadog resources like dashboards, monitors, and
  notebooks by teams, roles, or users for fine-grained permission management.
breadcrumbs: Docs > Account Management > Access Control > Granular Access Control
source_url: https://docs.datadoghq.com/rbac/granular_access/index.html
---

# Granular Access Control

## Manage access to individual resources{% #manage-access-to-individual-resources %}

Some resources allow you to restrict access to individual resources by roles, [Teams](https://docs.datadoghq.com/account_management/teams/), or users.

Use the different principals to control access patterns in your organization and encourage knowledge sharing and collaboration:

- Use Teams to map access to functional groups in your organizations. For example, restrict editing of a dashboard to the application team that owns it.
- Use roles to map access to personas. For example, restrict editing of payment methods to billing administrators.
- Allocate access to individual users only when necessary.

| Supported resources with granular access control                                                                          | Team-based access | Role-based access | User / service account-based access |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- | ----------------------------------- |
| [Apps](https://docs.datadoghq.com/actions/app_builder/access_and_auth/#restrict-access-to-a-specific-app)                 | yes               | yes               | yes                                 |
| [Case Management projects](https://docs.datadoghq.com/incident_response/case_management/settings#granular-access-control) | yes               | yes               | yes                                 |
| [Connections](https://docs.datadoghq.com/actions/connections/?tab=workflowautomation#connection-credentials)              | yes               | yes               | yes                                 |
| [Connection Groups](https://docs.datadoghq.com/actions/connections/?tab=workflowautomation#connection-groups)             | yes               | yes               | yes                                 |
| [Cross Org Connections](https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility/#permissions)     | yes               | yes               | yes                                 |
| [Dashboards](https://docs.datadoghq.com/dashboards/configure/#permissions)                                                | yes               | yes               | yes                                 |
| [Datastores](https://docs.datadoghq.com/actions/datastore/)                                                               | yes               | yes               | yes                                 |
| [Integration Accounts](https://docs.datadoghq.com/getting_started/integrations/#granular-access-control)                  | yes               | yes               | yes                                 |
| [Integration Services](https://docs.datadoghq.com/getting_started/integrations/#granular-access-control)                  | yes               | yes               | yes                                 |
| [Integration Webhooks](https://docs.datadoghq.com/getting_started/integrations/#granular-access-control)                  | yes               | yes               | yes                                 |
| [Logs Pipelines](https://docs.datadoghq.com/logs/log_configuration/pipelines/#pipeline-permissions)                       | yes               | yes               | yes                                 |
| [Monitors](https://docs.datadoghq.com/monitors/configuration/#permissions)                                                | yes               | yes               | yes                                 |
| [Notebooks](https://docs.datadoghq.com/notebooks/#limit-edit-access)                                                      | yes               | yes               | yes                                 |
| [Observability Pipelines](https://docs.datadoghq.com/observability_pipelines/configuration/access_control/)               | yes               | yes               | yes                                 |
| [On-Call](https://docs.datadoghq.com/incident_response/on-call/#granular-access-control)                                  | yes               | yes               | yes                                 |
| [Private Action Runner](https://docs.datadoghq.com/actions/private_actions)                                               | yes               | yes               | yes                                 |
| [Powerpacks](https://docs.datadoghq.com/dashboards/widgets/powerpack/#powerpack-permissions)                              | yes               | yes               | yes                                 |
| [Reference tables](https://docs.datadoghq.com/reference_tables/#permissions)                                              | yes               | yes               | yes                                 |
| [RUM apps](https://docs.datadoghq.com/real_user_monitoring)                                                               | yes               | yes               | yes                                 |
| [Security rules](https://docs.datadoghq.com/security/detection_rules/#restrict-edit-permissions)                          | yes               | yes               | yes                                 |
| [Security suppressions](https://docs.datadoghq.com/security/suppressions/#restrict-edit-permissions)                      | yes               | yes               | yes                                 |
| [Service Level Objectives](https://docs.datadoghq.com/service_level_objectives/#permissions)                              | yes               | yes               | yes                                 |
| [Sheets](https://docs.datadoghq.com/sheets/#permissions)                                                                  | yes               | yes               | yes                                 |
| [Synthetic tests](https://docs.datadoghq.com/synthetics/browser_tests/#permissions)                                       | yes               | yes               | yes                                 |
| [Workflows](https://docs.datadoghq.com/actions/workflows/access_and_auth/#restrict-access-on-a-specific-workflow)         | yes               | yes               | yes                                 |

### Elevate access to individual resources{% #elevate-access-to-individual-resources %}

A user with the `user_access_manage` permission can elevate their access to any individual resource that supports restrictions based on team, role, and user or service account. Resources with only role-based access restrictions are not supported. To get access, click the **Elevate Access** button in the granular access control modal.
