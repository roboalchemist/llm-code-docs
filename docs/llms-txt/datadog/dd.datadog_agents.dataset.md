# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.datadog_agents.dataset.md

---
title: Datadog Agents
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Datadog Agents
---

# Datadog Agents

The Datadog Agents table provides comprehensive metadata about Datadog Agent installations and configurations across your infrastructure. Each row represents a Datadog Agent instance and includes information about version, configuration (both full and user-provided), enabled features, installation method, runtime settings, and deployment context (ECS/EKS Fargate clusters). This table enables you to audit agent deployments, track configuration drift, monitor enabled features (APM, logs, process monitoring), verify FIPS compliance mode, review Fleet Automation policies applied to agents, and troubleshoot agent configurations. The Datadog Agent is the core software that runs on your hosts to collect events, metrics, traces, and logs.

```
dd.datadog_agents
```

## Fields

| Title                            | ID                               | Type | Data Type     | Description                                                                                  |
| -------------------------------- | -------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------- |
| Agent Startup Time               | agent_startup_time_ms            | core | timestamp     | The timestamp when the Datadog Agent started.                                                |
| Agent Version                    | agent_version                    | core | string        | The version of the Datadog Agent.                                                            |
| API Key UUID                     | api_key_uuid                     | core | string        | The UUID identifier for the API key used by the agent.                                       |
| Configuration Site               | config_site                      | core | string        | The Datadog site configured for the agent (e.g., datadoghq.com, datadoghq.eu).               |
| ECS Fargate Cluster Name         | ecs_fargate_cluster_name         | core | string        | The name of the ECS Fargate cluster where the agent is running, if applicable.               |
| ECS Fargate Task ARN             | ecs_fargate_task_arn             | core | string        | The ARN of the ECS Fargate task where the agent is running, if applicable.                   |
| EKS Fargate Cluster Name         | eks_fargate_cluster_name         | core | string        | The name of the EKS Fargate cluster where the agent is running, if applicable.               |
| FIPS Mode                        | fips_mode                        | core | bool          | Indicates whether the agent is running in FIPS compliance mode.                              |
| Agent Flavor                     | flavor                           | core | string        | The flavor or distribution type of the Datadog Agent (e.g., agent, iot-agent, dogstatsd).    |
| Fleet Policies Applied           | fleet_policies_applied           | core | array<string> | List of fleet automation policies applied to this agent.                                     |
| Full Configuration               | full_configuration               | core | string        | The complete configuration of the Datadog Agent in string format.                            |
| Hostname                         | hostname                         | core | string        | The hostname where the Datadog Agent is running.                                             |
| Hostname Source                  | hostname_source                  | core | string        | Indicates the source from which the hostname was determined (e.g., configuration, AWS, GCE). |
| Install Method Installer Version | install_method_installer_version | core | string        | The version of the installer used to install the agent.                                      |
| Install Method Tool              | install_method_tool              | core | string        | The tool used to install the agent (e.g., chef, puppet, ansible).                            |
| Install Method Tool Version      | install_method_tool_version      | core | string        | The version of the installation tool used.                                                   |
| Logs Transport                   | logs_transport                   | core | string        | The transport method used for sending logs (e.g., HTTP, TCP).                                |
| Provided Configuration           | provided_configuration           | core | string        | The user-provided configuration for the Datadog Agent in string format.                      |
| Enabled Features                 | enabled_features                 | core | hstore        | A key-value map of features and their enabled status (e.g., apm, logs, process monitoring).  |
