# Source: https://docs.datadoghq.com/api/latest/scopes.md

---
title: Authorization Scopes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Authorization Scopes
---

## Authorization scopes for OAuth clients{% #authorization-scopes-for-oauth-clients %}

Scopes are an authorization mechanism that allow you to limit and define the specific access applications have to an organization's Datadog data. When authorized to access data on behalf of a user or service account, applications can only access the information explicitly permitted by their assigned scopes.

{% alert level="danger" %}
This page lists only the authorization scopes that can be assigned to OAuth clients. To view the full list of assignable permissions for scoped application keys, see [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#permissions-list).
- **OAuth clients** â Can only be assigned authorization scopes (limited set).
- **Scoped application keys** â Can be assigned any Datadog permission.

{% /alert %}

The best practice for scoping applications is to follow the principle of least privilege. Assign only the minimum scopes necessary for an application to function as intended. This enhances security and provides visibility into how applications interact with your organization's data. For example, a third-party application that only reads dashboards does not need permissions to delete or manage users.

You can use authorization scopes with OAuth2 clients for your [Datadog Apps](https://docs.datadoghq.com/developers/datadog_apps/#oauth-api-access).

#### API Management, Synthetics

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### APM, Spans

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Agentless Scanning, Domain Allowlist, Downtimes, IP Allowlist, Monitors

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Agentless Scanning, Domain Allowlist, IP Allowlist, Monitors, Security Monitoring

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Agentless Scanning, Domain Allowlist, IP Allowlist, Security Monitoring, Static Analysis

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Agentless Scanning, Security Monitoring, Static Analysis

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### CI Visibility Pipelines, CI Visibility Tests, Test Optimization

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### CI Visibility Tests, Test Optimization

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Case Management, Error Tracking

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Cloud Cost Management

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Dashboard Lists, Dashboards, Powerpack

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Datasets, Roles, Users

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Domain Allowlist, Downtimes, Monitors

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Downtimes, Monitors

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Events

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Hosts

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Incident Services, Incident Teams, Incidents

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Metrics

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Org Connections

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Service Definition, Service Scorecards, Software Catalog

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Service Level Objective Corrections, Service Level Objectives

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Teams

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Usage Metering

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Webhooks Integration

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |

#### Workflow Automation

| Scope name | Description | Endpoints that require this scope |
| ---------- | ----------- | --------------------------------- |
