# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.datadog_agent_integrations.dataset.md

---
title: Datadog Agent Integrations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Datadog Agent Integrations
---

# Datadog Agent Integrations

The Datadog Agent Integrations table provides information about integrations (checks) configured on Datadog Agents across your infrastructure. Each row represents an integration instance running on an agent and includes configuration details (init_config and instance_config), metadata, version information (semantic versioning with major, minor, patch), category, provider, and associated tags. This table enables you to inventory all configured integrations, audit integration versions, review configuration parameters, track which services are being monitored, and troubleshoot integration setup. Configuration files for Agent checks and integrations are stored in the conf.d directory with YAML format. Datadog offers hundreds of integrations for databases, web servers, monitoring systems, and other technologies.

```
dd.datadog_agent_integrations
```

## Fields

| Title                  | ID              | Type | Data Type | Description                                                                                                             |
| ---------------------- | --------------- | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| Category               | category        | core | string    | The category of the integration (e.g., database, web server, monitoring).                                               |
| Host ID                | host_id         | core | int64     | The numeric identifier of the host running the integration.                                                             |
| Hostname               | hostname        | core | string    | The hostname where the integration is configured.                                                                       |
| Init Configuration     | init_config     | core | string    | The initialization configuration for the integration in string format.                                                  |
| Instance Configuration | instance_config | core | string    | The instance-specific configuration for the integration in string format.                                               |
| Metadata               | metadata        | core | string    | Additional metadata about the integration in string format.                                                             |
| Integration Name       | name            | core | string    | The name of the integration (e.g., postgres, nginx, redis).                                                             |
| Port                   | port            | core | int64     | The port number the integration is configured to monitor.                                                               |
| Provider               | provider        | core | string    | The provider or source of the integration.                                                                              |
| Resource Tags          | tags            | core | hstore    | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the integration. |
| Integration Type       | type            | core | string    | The type classification of the integration.                                                                             |
| Version Major          | version_major   | core | string    | The major version number of the integration.                                                                            |
| Version Minor          | version_minor   | core | string    | The minor version number of the integration.                                                                            |
| Version Patch          | version_patch   | core | string    | The patch version number of the integration.                                                                            |
| Version Raw            | version_raw     | core | string    | The complete raw version string of the integration.                                                                     |
| Version Scheme         | version_scheme  | core | string    | The versioning scheme used by the integration (e.g., semver).                                                           |
