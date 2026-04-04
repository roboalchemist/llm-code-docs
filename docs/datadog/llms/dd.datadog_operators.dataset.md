# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.datadog_operators.dataset.md

---
title: Datadog Operator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Datadog Operator
---

# Datadog Operator

This dataset stores metadata information about Datadog Operator usage. The Datadog Operator is a Kubernetes operator that manages the lifecycle of Datadog custom resources. Each record describes an application, including its version, how it was installed, and which features are enabled.

```
dd.datadog_operators
```
Datadog Operator Repository
{% icon name="icon-external-link" /%}

## Fields

| Title                       | ID                          | Type | Data Type | Description                                                           |
| --------------------------- | --------------------------- | ---- | --------- | --------------------------------------------------------------------- |
| Operator Version            | operator_version            | core | string    | Application version of the Datadog Operator.                          |
| Kubernetes Version          | kubernetes_version          | core | string    | Kubernetes version of the cluster the Datadog Operator is running on. |
| Install Method Tool         | install_method_tool         | core | string    | Tool used to install the Datadog Operator.                            |
| Install Method Tool Version | install_method_tool_version | core | string    | Version of the tool used to install the Datadog Operator.             |
| Is Leader                   | is_leader                   | core | bool      | True if this instance of the Datadog Operator is the leader.          |
| Enabled CRDs                | enabled_crds                | core | hstore    | List of CRDs enabled in the Datadog Operator.                         |
| Leader Election Enabled     | leader_election_enabled     | core | bool      | True if Leader Election is enabled.                                   |
| ExtendedDaemonSet Enabled   | extended_daemonset_enabled  | core | bool      | True if usage of the ExtendedDaemonSet is enabled.                    |
| Remote Config Enabled       | remote_config_enabled       | core | bool      | True if the Remote Configuration feature is enabled.                  |
| Introspection Enabled       | introspection_enabled       | core | bool      | True if the Introspection feature is enabled.                         |
| Cluster Name                | cluster_name                | core | string    | Cluster Name of the cluster the Datadog Operator is running on.       |
| Config DD_URL               | config_dd_url               | core | string    | If present, configured DD_URL of the Datadog Operator.                |
| Config DD_SITE              | config_site                 | core | string    | If present, configured DD_SITE of the Datadog Operator.               |
