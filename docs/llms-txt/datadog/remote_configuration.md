# Source: https://docs.datadoghq.com/remote_configuration.md

---
title: Remote Configuration
description: >-
  Remotely configure and change behavior of Datadog components like Agents,
  tracing libraries, and Observability Pipelines Workers deployed in your
  infrastructure.
breadcrumbs: Docs > Remote Configuration
---

# Remote Configuration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Remote Configuration is a Datadog capability that allows you to remotely configure and change the behavior of select product features in Datadog components such as Agents, tracing libraries, and Observability Pipelines Workers deployed in your infrastructure. Use Remote Configuration to apply configurations to Datadog components in your environment on demand, decreasing management costs, reducing friction between teams, and accelerating issue resolution times.

For Datadog security products, App and API Protection and Workload Protection, Remote Configuration-enabled Agents and compatible tracing libraries provide real-time security updates and responses, enhancing security posture for your applications and cloud infrastructure.

## How it works{% #how-it-works %}

When Remote Configuration is enabled, Datadog components such as the Datadog Agent securely poll the configured [Datadog site](https://docs.datadoghq.com/getting_started/site/) for configuration changes that are ready to apply. Pending changes are then automatically applied to Datadog components. For example, after you submit configuration changes in the Datadog UI for a Remote Configuration-enabled product feature, the changes are stored in Datadog.

The following diagram illustrates how Remote Configuration works:

{% image
   source="https://datadog-docs.imgix.net/images/agent/remote_config/RC_Diagram_v5.2446702b0db5ae41ca37b96bc4224a40.png?auto=format"
   alt="Users configure features in the UI, the config is stored in Datadog, the Agent requests config updates." /%}

1. You configure select product features in the Datadog UI.
1. The product feature configurations are securely stored within Datadog.
1. Remote-configuration enabled Datadog components in your environments securely poll, receive, and automatically apply configuration updates from Datadog. Tracing libraries that are deployed in your environments communicate with Agents to request and receive configuration updates from Datadog instead of directly polling Datadog.

## Supported environments{% #supported-environments %}

Remote Configuration works in environments where supported Datadog components are deployed. Supported Datadog components include:

- Agents
- Tracers (indirectly)
- Observability Pipeline Workers
- Private action runners and serverless container cloud services such as AWS Fargate.

Remote Configuration does not support serverless container managed apps, such as AWS App Runner, Azure Container Apps, Google Cloud Run; or functions deployed with container packaging, such as AWS Lambda, Azure Functions, and Google Cloud Functions.

## Supported products and features{% #supported-products-and-features %}

The following products and features are supported with Remote Configuration.

{% dl %}

{% dt %}
Fleet Automation
{% /dt %}

{% dd %}

- [Send flares](https://docs.datadoghq.com/agent/fleet_automation/#send-a-remote-flare) directly from the Datadog site. Seamlessly troubleshoot the Datadog Agent without directly accessing the host.

{% /dd %}

{% dd %}

- [Upgrade your Agents](https://docs.datadoghq.com/agent/fleet_automation/remote_management#remotely-upgrade-your-agents) (Preview).

{% /dd %}

{% dt %}
App and API Protection (AAP)
{% /dt %}

{% dd %}

- [1-click AAP activation](https://docs.datadoghq.com/security/application_security/setup/): Enable AAP in 1-click from the Datadog UI.

{% /dd %}

{% dd %}

- [In-App attack patterns updates](https://docs.datadoghq.com/security/application_security/): Receive the newest Web Application Firewall (WAF) attack patterns automatically as Datadog releases them, following newly disclosed vulnerabilities or attack vectors.

{% /dd %}

{% dd %}

- [Protect](https://docs.datadoghq.com/security/application_security/): Block attackers' IPs, authenticated users, and suspicious requests that are flagged in AAP Security Signals and Traces temporarily or permanently through the Datadog UI.

{% /dd %}

{% dt %}
Application Performance Monitoring (APM)
{% /dt %}

{% dd %}

- Configuration at runtime: Change a service's trace sampling rate, Log Injection enablement, and HTTP header tags from within the Software Catalog UI, without having to restart the service. Read [Configuration at Runtime](https://docs.datadoghq.com/tracing/trace_collection/runtime_config/) for more information.

{% /dd %}

{% dd %}

- [Remotely set Agent sampling rate](https://docs.datadoghq.com/tracing/trace_pipeline/adaptive_sampling/): Remotely configure the Datadog Agent to change its trace sampling rates and set rules to scale your organization's trace ingestion according to your needs, without needing to restart your Datadog Agent.

{% /dd %}

{% dt %}
[Dynamic Instrumentation](https://docs.datadoghq.com/tracing/dynamic_instrumentation/#explore-dynamic-instrumentation)
{% /dt %}

{% dd %}

- Send critical metrics, traces, and logs from your live applications with no code changes.

{% /dd %}

{% dt %}
Workload Protection
{% /dt %}

{% dd %}

- Automatic default Agent rule updates: Automatically receive and update the default Agent rules maintained by Datadog as new Agent detections and enhancements are released. See [Setting Up Workload Protection](https://docs.datadoghq.com/security/workload_protection/) for more information.

{% /dd %}

{% dd %}

- Automatic deployment of custom Agent rules: Automatically deploy your custom Agent rules to designated hosts (all hosts or a defined subset of hosts).

{% /dd %}

{% dt %}
Observability Pipelines
{% /dt %}

{% dd %}

- Remotely deploy and update [Observability Pipelines Workers](https://docs.datadoghq.com/observability_pipelines/#observability-pipelines-worker) (OPW): Build and edit pipelines in the Datadog UI, rolling out your configuration changes to OPW instances running in your environment.

{% /dd %}

{% dt %}
[Autoscaling](https://docs.datadoghq.com/containers/autoscaling)
{% /dt %}

{% dd %}

- Remotely manage autoscaling cluster and workload scaling configurations for your containerized environments. See [Autoscaling](https://docs.datadoghq.com/containers/autoscaling) for more information.

{% /dd %}

{% dt %}
Private action runner
{% /dt %}

{% dd %}

- Run Datadog workflows and apps that interact with services hosted on your private network without exposing your services to the public internet. For more information, see [Private Actions](https://docs.datadoghq.com/actions/private_actions/use_private_actions/).

{% /dd %}

{% /dl %}

## Security considerations{% #security-considerations %}

Datadog implements the following safeguards to protect the confidentiality, integrity, and availability of configurations received and applied by your Datadog components:

- Remote Configuration enabled Datadog components deployed in your infrastructure request configurations from Datadog.Important alert (level: info): Some components like private action runners are always remote configuration enabled. Others, like Agents, can be enabled or disabled using in-disk configuration options.
- Datadog never sends configuration changes unless requested by Datadog components. If it does send configuration changes, Datadog only sends changes relevant to the requesting component.
- The configuration requests are initiated from your infrastructure to Datadog over HTTPS (port 443). This is the same port that the Agent uses by default to send observability data.
- The communication between your datadog components and Datadog is encrypted using HTTPS and is authenticated and authorized using your Datadog API key except in the case of private action runners where a JWT token is used instead.
- Only users with the [`api_keys_write`](https://docs.datadoghq.com/account_management/rbac/permissions#api-and-application-keys) permission are authorized to enable or disable Remote Configuration capability on API keys and use the supported product features.
- Your configuration changes submitted through the Datadog UI are signed and validated by the requesting Datadog component, verifying the integrity of the configuration.

### Role-based access{% #role-based-access %}

Enabling Remote Configuration impacts the following products. Each product defines a set of role-based access controls that need to be granted to their users. For general information on access management, see [Access Control](https://docs.datadoghq.com/account_management/rbac).

| Remote Configuration Enabled Product   | Role-Based Access Controls                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fleet Automation                       | `FLEET_POLICIES_WRITE``AGENT_UPGRADE_WRITE``FLEET_FLARE`For more information, see [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/#control-access-to-fleet-automation).                                                                                                                                                            |
| App and API Protection                 | `APPSEC_ACTIVATION_READ``APPSEC_ACTIVATION_WRITE``APPSEC_PROTECT_READ``APPSEC_PROTECT_WRITE`For more information, see [Access Control](https://docs.datadoghq.com/security/access_control/#permissions).                                                                                                                                                |
| APM                                    | `APM_SERVICE_INGEST_READ``APM_SERVICE_INGEST_WRITE``APM_REMOTE_CONFIGURATION_READ``APM_REMOTE_CONFIGURATION_WRITE`For more information, see [Adaptive Sampling](https://docs.datadoghq.com/tracing/trace_pipeline/adaptive_sampling/#permissions).                                                                                                      |
| Dynamic Instrumentation                | `DEBUGGER_READ``DEBUGGER_WRITE``DEBUGGER_WRITE_PRE_PROD``APM_REMOTE_CONFIGURATION_READ``APM_REMOTE_CONFIGURATION_WRITE`For more information, see [APM](https://docs.datadoghq.com/account_management/rbac/permissions/#apm).                                                                                                                            |
| Workload Protection                    | `SECURITY_MONITORING_CWS_AGENT_RULES_WRITE``SECURITY_MONITORING_CWS_AGENT_RULES_READ``SECURITY_MONITORING_CWS_AGENT_RULES_ACTIONS`For more information, see [Security](https://docs.datadoghq.com/account_management/rbac/permissions/#cloud-security-platform).                                                                                        |
| CSM Side Scanning                      | `ORG_MANAGEMENT``MANAGE_INTEGRATIONS`For more information, see [Enable Agentless Scanning](https://docs.datadoghq.com/security/cloud_security_management/setup/#enable-agentless-scanning).                                                                                                                                                             |
| Observability Pipelines                | `OBSERVABILITY_PIPELINES_READ``OBSERVABILITY_PIPELINES_WRITE``OBSERVABILITY_PIPELINES_DELETE``OBSERVABILITY_PIPELINES_DEPLOY``OBSERVABILITY_PIPELINES_CAPTURE_WRITE``OBSERVABILITY_PIPELINES_CAPTURE_READ`For more information, see [Observability Pipelines](https://docs.datadoghq.com/account_management/rbac/permissions/#observability-pipelines). |
| Private Action Runner                  | `ON_PREM_RUNNER_WRITE``ON_PREM_RUNNER_READ``ON_PREM_RUNNER_USE`For more information, see [App Builder & Workflow Automation](https://docs.datadoghq.com/account_management/rbac/permissions/#app-builder--workflow-automation).                                                                                                                         |
| Network Device Monitoring (NDM)        | `NDM_DEVICE_PROFILES_VIEW``NDM_DEVICE_PROFILES_EDIT`                                                                                                                                                                                                                                                                                                    |
| Container Autoscaling                  | `ORCHESTRATION_AUTOSCALING_MANAGE``ORCHESTRATION_WORKLOAD_SCALING_WRITE``ORCHESTRATION_WORKLOAD_SCALING_READ`                                                                                                                                                                                                                                           |
| Serverless Lambda Auto-instrumentation | `SERVERLESS_AWS_INSTRUMENTATION_READ``SERVERLESS_AWS_INSTRUMENTATION_WRITE`For more information, see [Serverless](https://docs.datadoghq.com/account_management/rbac/permissions/#serverless).                                                                                                                                                          |

## Enable Remote Configuration{% #enable-remote-configuration %}

In most cases, Remote Configuration is enabled by default for your organization. You can check if Remote Configuration is enabled on your organization from the [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config) settings page. If you need to enable it:

1. Ensure your RBAC permissions include [`org_management`](https://docs.datadoghq.com/account_management/rbac/permissions#access-management), so you can enable Remote Configuration for your organization.
1. From your Organization Settings page, enable [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config). This enables Datadog components across your organization to receive configurations from Datadog.
1. Follow the product-specific configuration guidance below to finish setting up Remote Configuration.

### Product-specific configuration{% #product-specific-configuration %}

Consult the documentation below for instructions specific to the product you're configuring.

| Product                 | Setup instructions                                                                                                                                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fleet Automation        | [Setup Fleet Automation](https://docs.datadoghq.com/agent/guide/setup_remote_config)                                                                                                                                         |
| APM                     | [Configuration at runtime](https://docs.datadoghq.com/tracing/guide/remote_config/)                                                                                                                                          |
| Dynamic Instrumentation | [Getting started with Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/#getting-started)                                                                                                          |
| Workload Protection     | [Workload Protection](https://docs.datadoghq.com/security/workload_protection/)                                                                                                                                              |
| Observability Pipelines | Ensure that you've [enabled Remote Configuration on the API key](https://app.datadoghq.com/organization-settings/remote-config/setup?page_id=api-key-enablement-step&standalone=1) you're using for Observability Pipelines. |
| Sensitive Data Scanner  | [Cloud storage](https://docs.datadoghq.com/security/sensitive_data_scanner/setup/cloud_storage/?tab=newawsaccount)                                                                                                           |
| Private Action Runner   | [Private Actions Overview](https://docs.datadoghq.com/actions/private_actions/)                                                                                                                                              |

## Best practices{% #best-practices %}

### Datadog Audit Trail{% #datadog-audit-trail %}

Use [Datadog Audit Trail](https://docs.datadoghq.com/account_management/audit_trail) to monitor organization access and Remote Configuration enabled events. Audit Trail allows your administrators and security teams to track the creation, deletion, and modification of Datadog API and application keys. After Audit Trail is configured, you can view events related to Remote Configuration enabled features and who has requested these changes. Audit Trail allows you to reconstruct sequences of events, and establish robust Datadog monitoring for Remote Configuration.

### Monitors{% #monitors %}

Configure [monitors](https://docs.datadoghq.com/monitors/) to receive notifications when an event of interest is encountered.

## Opting out of Remote Configuration{% #opting-out-of-remote-configuration %}

Instead of disabling Remote Configuration globally, Datadog recommends opting out for specific Datadog products. For more information, see the documentation for the relevant product.

## Further Reading{% #further-reading %}

- [How Application Security Monitoring Works](https://docs.datadoghq.com/security/application_security/how-appsec-works/#built-in-protection)
- [Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/?tab=configurationyaml#enable-remote-configuration)
- [Setting Up Workload Protection](https://docs.datadoghq.com/security/workload_protection/)
- [Using Datadog Audit Trail](https://www.datadoghq.com/blog/compliance-governance-transparency-with-datadog-audit-trail/)
- [Apply real-time updates to Datadog components with Remote Configuration](https://www.datadoghq.com/blog/remote-configuration-for-datadog/)
