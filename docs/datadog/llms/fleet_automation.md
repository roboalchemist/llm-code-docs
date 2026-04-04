# Source: https://docs.datadoghq.com/agent/fleet_automation.md

---
title: Fleet Automation
description: >-
  Centrally govern and remotely manage Datadog Agents and OpenTelemetry
  Collectors at scale with configuration views, upgrades, flare collection, and
  API key rotation.
breadcrumbs: Docs > Agent > Fleet Automation
---

# Fleet Automation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
Fleet Automation for OpenTelemetry Collectors is currently in preview.
{% /alert %}

## Overview{% #overview %}

Datadog Fleet Automation allows you to centrally govern and remotely manage Datadog Agents and OpenTelemetry (OTel) Collectors at scale to support your evolving observability needs.

{% image
   source="https://datadog-docs.imgix.net/images/agent/fleet_automation/fleet_automation2.5264fe5b008d2cd3004947db7c50bc79.png?auto=format"
   alt="The fleet automation page" /%}

## Use cases{% #use-cases %}

For the following use cases, ensure your fleet of Datadog Agents and OTel Collectors are using the latest feature enhancements. With Fleet Automation, you gain the capabilities to:

- **View the latest Agent and OTel Collector configurations** along with historical changes to help confirm deployment updates and ensure configuration consistency.
- **Ensure your fleet of Agents and OTel Collectors are using the latest feature enhancements** by identifying and upgrading outdated versions.
- **Configure your Datadog Agents directly from Fleet Automation**, enabling your teams to centralize setup and get visibility into your environments faster.
- **Send a support flare remotely from the Datadog UI**, reducing the time it takes to debug issues on an Agent or DDOT Collector.

## Setup{% #setup %}

### Remotely manage your fleet{% #remotely-manage-your-fleet %}

Fleet Automation enables you to centrally manage Datadog Agents across all your hosts directly from the Datadog UI. With remote management, you can view the current state of every Agent, apply configuration changes, and roll out version upgrades without needing direct access to individual systems. This provides a consistent, controlled workflow for keeping your fleet secure, up to date, and aligned with your organization's standards.

- **Remotely Upgrade and Configure Agents**: For setup and enablement steps, see [Enable Remote Agent Management](https://docs.datadoghq.com/agent/fleet_automation/remote_management/#setup).
- **View Agent and OTel Collector configurations**:
  - The Agent and Datadog Distribution of OTel Collector (DDOT) configuration view is enabled by default in Agent versions 7.47.0 or later. To enable Agent configuration manually, set `inventories_configuration_enabled` in your [Agent configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) to `true`. Alternatively, use the `DD_INVENTORIES_CONFIGURATION_ENABLED` environment variable.
  - The upstream OTel Collector configuration view is enabled by setting the [Datadog Extension](https://docs.datadoghq.com/opentelemetry/integrations/datadog_extension/#setup) in your collector configuration file.
- **View Agent integration configuration**: Agent integration configuration is enabled by default on Agent versions 7.49 or later. To enable Agent integration configuration manually, set `inventories_checks_configuration_enabled` in your [Agent configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) to `true`. Alternatively, use the environment variable `DD_INVENTORIES_CHECKS_CONFIGURATION_ENABLED`.

### Fleet Automation API{% #fleet-automation-api %}

Fleet Automation provides a public API that allows you to programmatically view and manage Datadog Agents at scale. For full endpoint details and usage examples, see the [Fleet Automation API documentation](https://docs.datadoghq.com/api/latest/fleet-automation/).

**Note**: The Fleet Automation API does not support all Datadog Agent configuration capabilities.

{% alert level="info" %}
Remote management of Agents in containerized workloads is not supported.
{% /alert %}

## Observe your fleet{% #observe-your-fleet %}

Use the [**Fleet Automation**](https://app.datadoghq.com/fleet) page to gain insight into observability gaps on your hosts, outdated Agents or OTel Collectors, and Agents with integration issues.

For each Datadog Agent, you can see:

- The Agent version
- Whether the Agent has any unconfigured or misconfigured integrations
- The services that the Agent is monitoring
- The Agent's Remote Configuration status
- The products that are enabled on the Agent
- Agent Audit Trail events including configuration changes, upgrades and flares

For each OTel Collector, you can see:

- The Collector version
- The distribution of the Collector
- The configuration YAML of the Collector

### Examine a Datadog Agent or OpenTelemetry Collector{% #examine-a-datadog-agent-or-opentelemetry-collector %}

Selecting a Datadog Agent or OTel Collector gives you more information about it, including its configuration, connected integrations, audit events, and a support tab that you can use to send a remote flare.

{% image
   source="https://datadog-docs.imgix.net/images/agent/fleet_automation/fleet-automation-view-config.765ac9cfeb655d626d63655dba190e24.png?auto=format"
   alt="An Agent's integration information" /%}

### View Agent Audit Trail events{% #view-agent-audit-trail-events %}

The Audit Events tab displays Audit Trail events associated with the selected Agent. Use this tab to:

- Identify configuration changes, API key updates, installs, upgrades and support flares.
- Determine when changes were made and from where

Audit Trail event visibility depends on your plan. When Audit Trail is enabled in your organization, you can view Agent events for up to 90 days based on your Audit Trail retention settings. If Audit Trail is not enabled in your organization, you can view the past 24 hours of events.

### Send a remote flare{% #send-a-remote-flare %}

You can send a flare from the Datadog Agent or DDOT Collector after enabling Remote Configuration on the Agent. For instructions on sending a flare, see [Send a flare from the Datadog site](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/#send-a-flare-from-the-datadog-site).

When contacting Datadog Support with Remote Configuration enabled for an Agent, the Support team may initiate a flare from your environment in order to better assist you in a timely manner. Flares provide troubleshooting information to Datadog Support to help you resolve your issue.

{% image
   source="https://datadog-docs.imgix.net/images/agent/fleet_automation/fleet_automation_remote_flare.eddc4a71c702b7900e16f7116bee56e5.png?auto=format"
   alt="Send a remote flare" /%}

## Control access to Fleet Automation{% #control-access-to-fleet-automation %}

Fleet Automation is available to all users in a Datadog organization. You can control access to specific functionality:

| Permission                       | Description                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------- |
| `API Keys Read`                  | Restricts which users can view and search Agents by API key.                 |
| `Agent Flare Collection`         | Restricts which users can remotely send flares from Fleet Automation.        |
| `Agent Upgrade`                  | Restricts which users have access to upgrade Agents from Fleet Automation.   |
| `Agent Configuration Management` | Restricts which users have access to configure Agents from Fleet Automation. |

For information on setting up roles and permissions, see [Access Control](https://docs.datadoghq.com/account_management/rbac/).

## Further Reading{% #further-reading %}

- [Centrally set up and scale monitoring of your infrastructure and apps with Datadog Fleet Automation](https://www.datadoghq.com/blog/fleet-automation-central-configuration)
- [Manage all your OpenTelemetry collectors with Datadog Fleet Automation](https://www.datadoghq.com/blog/manage-opentelemetry-collectors-with-datadog-fleet-automation)
- [Centralize and govern your OpenTelemetry pipeline with the DDOT gateway](https://www.datadoghq.com/blog/ddot-gateway)
- [Find out more about Remote Configuration](https://docs.datadoghq.com/remote_configuration)
- [Learn about the Agent configuration view](https://docs.datadoghq.com/infrastructure/list/#agent-configuration)
- [Centrally govern and remotely manage Datadog Agents at scale with Fleet Automation](https://www.datadoghq.com/blog/fleet-automation/)
