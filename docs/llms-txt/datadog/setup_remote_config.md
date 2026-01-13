# Source: https://docs.datadoghq.com/agent/guide/setup_remote_config.md

---
title: Remote Configuration for Fleet Automation
description: >-
  Configure Remote Configuration with Fleet Automation to enable Agent flares,
  remote upgrades, and centralized configuration management.
breadcrumbs: Docs > Agent > Agent Guides > Remote Configuration for Fleet Automation
source_url: https://docs.datadoghq.com/guide/setup_remote_config/index.html
---

# Remote Configuration for Fleet Automation

This page covers configuring and using Remote Configuration (Remote Configuration enables users to remotely configure and change the behavior of Datadog components deployed in their environment.) with [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/). The following Fleet Automation features require Remote Configuration:

| Feature                                                                                                                | Description                                               | Minimum Agent Version  |
| ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------- |
| **[Agent flares](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/#send-a-flare-from-the-datadog-site)**  | Send a flare from the Datadog site using Fleet Automation | 7.47+7.66+ recommended |
| **[Agent upgrades](https://docs.datadoghq.com/agent/fleet_automation/remote_management#remotely-upgrade-your-agents)** | Remotely upgrade your Agents                              | 7.66+                  |
| **[Agent configuration](https://docs.datadoghq.com/agent/fleet_automation/)**                                          | Remotely configure your Agents                            | 7.73+                  |

Datadog recommends upgrading your Agents regularly to make sure you have access to the latest features.

## Prerequisites{% #prerequisites %}

- Datadog recommends Datadog Agent version `7.66` or later. Although some features might work with earlier versions of the Agent, version `7.66` introduced [breaking changes](https://docs.datadoghq.com/agent/fleet_automation/remote_management#datadog-installer-incompatible-with-agent-pre-766) to Remote Agent Management.
- Ensure your RBAC permissions include [`org_management`](https://docs.datadoghq.com/account_management/rbac/permissions#access-management), so you can enable Remote Configuration for your organization.
- Ensure your RBAC permissions include [`api_keys_write`](https://docs.datadoghq.com/account_management/rbac/permissions#api-and-application-keys), so you can create a new API key with the Remote Configuration capability, or add the capability to an existing API key. Contact your organization's Datadog administrator to update your permissions if you don't have it. A key with this capability allows you to authenticate and authorize your Agent to use Remote Configuration.

## Enable Remote Configuration{% #enable-remote-configuration %}

In most cases, Remote Configuration is enabled by default for your organization. You can check if Remote Configuration is enabled on your organization from the [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config) settings page. If you need to enable it:

1. Ensure your RBAC permissions include [`org_management`](https://docs.datadoghq.com/agent/guide#cloud-infrastructure-guides), so you can enable Remote Configuration for your organization.
1. From your Organization Settings page, enable [**Remote Configuration**](https://app.datadoghq.com/organization-settings/remote-config). This enables Datadog components across your organization to receive configurations from Datadog.

## Agent Remote Configuration status{% #agent-remote-configuration-status %}

You can gain visibility into the Remote Configuration status of your Agent using the [Remote Configuration UI](https://app.datadoghq.com/organization-settings/remote-config).

The following table describes the meaning of each Agent status:

| Agent Status      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONNECTED         | The Agent deployed in your environment is able to reach, authenticate, and authorize successfully to Datadog. This is the optimal state you want your Agents to be in for Remote Configuration.                                                                                                                                                                                                                                                                                                                                 |
| UNAUTHORIZED      | The Agent deployed in your environment is able to reach Datadog but is not able to authenticate and authorize with Datadog for Remote Configuration operation. The most likely cause is the API Key used by the Agent is not Remote Configuration-enabled. To fix the issue, enable Remote Configuration capability on the API Key used by the Agent.                                                                                                                                                                           |
| CONNECTION ERROR  | The Agent deployed in your environment has `remote_config.enabled` set to true in its `datadog.yaml` configuration file, however, the Agent cannot be found in the Remote Configuration service. The most likely cause is that the Agent is unable to reach Remote Configuration [endpoints](https://docs.datadoghq.com/agent/configuration/network). To fix the issue, allow outbound HTTPS access to Remote Configuration endpoints from your environment. This status displays when the Agent version is `7.45.0` or higher. |
| DISABLED          | The Agent deployed in your environment has `remote_config.enabled` set to false in its `datadog.yaml` configuration file. Set `remote_config.enabled` to true if you want to enable Remote Configuration on the Agent. This status displays when the Agent version is `7.45.0` or higher.                                                                                                                                                                                                                                       |
| NOT CONNECTED     | The Agent cannot be found in the Remote Configuration service and could have `remote_config.enabled` set to true or false in its `datadog.yaml` configuration file. Check your local Agent configuration or your proxy settings. This status displays when the Agent version is higher than `7.41.1` but lower than `7.45.0`.                                                                                                                                                                                                   |
| UNSUPPORTED AGENT | The Agent is on a version that is not Remote Configuration capable. To fix this issue, update the Agent to the latest available version.                                                                                                                                                                                                                                                                                                                                                                                        |

## Opting out of Remote Configuration for Fleet Automation{% #opting-out-of-remote-configuration-for-fleet-automation %}

You can disable Remote Configuration capabilities:

- at the API key level
- at the Agent level
- at the organization level (**not recommended**)

### At the API key level{% #at-the-api-key-level %}

Disable the API key of your choice on the [API Keys](https://app.datadoghq.com/organization-settings/api-keys) page. You need the [`api_keys_write`](https://docs.datadoghq.com/account_management/rbac/permissions#api-and-application-keys) permission to disable Remote Configuration on an API key.

### At the Agent level{% #at-the-agent-level %}

Starting with Agent version 7.47.0, `remote_configuration.enabled` is set to `true` by default in the Agent. This setting causes the Agent to request configuration updates from the Datadog site.

If you don't want your Agent to send configuration requests to Datadog, you can set `remote_configuration.enabled` to `false` in the Agent.

{% tab title="Configuration YAML file" %}
Change `remote_configuration.enabled` from `true` to `false` in your [configuration YAML file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/?tab=agentv6v7#agent-main-configuration-file):

```yaml
remote_configuration:
  enabled: false
```

{% /tab %}

{% tab title="Environment variable" %}
Add the following to your Datadog Agent manifest:

```yaml
DD_REMOTE_CONFIGURATION_ENABLED=false
```

{% /tab %}

{% tab title="Helm" %}
Add the following to your Helm chart:

```yaml
datadog:
  remoteConfiguration:
    enabled: false
```

{% /tab %}

### At the organization level{% #at-the-organization-level %}

{% alert level="warning" %}
**Datadog does not recommend disabling Remote Configuration at the organization level. Disabling Remote Configuration at the organization level prevents Datadog components in several products across your organization from receiving configurations from Datadog.**
{% /alert %}

To disable Remote Configuration at the organization level:

1. Ensure you have the required `org_management` permission.
1. Go to the [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config) settings page.
1. Click **Disable**.
1. When the warning message appears, click **Disable** again.

## Troubleshooting{% #troubleshooting %}

If you experience issues using Remote Configuration with your Agents, use the following troubleshooting guidelines. If you need further assistance, contact [Datadog support](https://docs.datadoghq.com/help/).

### Restart the Agent{% #restart-the-agent %}

After the Agent configuration is updated in the [`datadog.yaml`][16] file, restart the Agent for the change to take effect.

### Ensure Datadog Remote Configuration endpoints are reachable from your environment{% #ensure-datadog-remote-configuration-endpoints-are-reachable-from-your-environment %}

To use Remote Configuration, the Agent deployed in your environment needs access to the Datadog Remote Configuration [endpoints](https://docs.datadoghq.com/agent/configuration/network). For a private network connection between your environment and Datadog, you can also connect to Remote Configuration Virtual Private Cloud [endpoints](https://docs.datadoghq.com/agent/guide#cloud-infrastructure-guides). Ensure that outbound HTTPS has access to Remote Configuration endpoints from your environment. If you also have a proxy in between Datadog and your environment, update your [proxy settings](https://docs.datadoghq.com/agent/configuration/proxy/) to incorporate Remote Configuration endpoints.

### Enable Remote Configuration on the API key{% #enable-remote-configuration-on-the-api-key %}

To authenticate and authorize the Agent to receive configuration, enable Remote Configuration on the relevant API Key. Only users who have the [`api_keys_write`](https://docs.datadoghq.com/account_management/rbac/permissions#api-and-application-keys) RBAC permission can enable Remote Configuration on the API Key.

**Note:** If you have [`api_keys_write`](https://docs.datadoghq.com/account_management/rbac/permissions#api-and-application-keys) RBAC permission, but are missing Remote Configuration [Organization](https://app.datadoghq.com/organization-settings/remote-config) level permissions, you cannot enable Remote Configuration on a new or an existing API Key. You only have permission to disable Remote Configuration on an existing API Key.

## Further reading{% #further-reading %}

- [Find out more about Remote Configuration](https://docs.datadoghq.com/remote_configuration)
- [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation)
- [Learn about the Agent configuration view](https://docs.datadoghq.com/infrastructure/list/#agent-configuration)
- [Centrally govern and remotely manage Datadog Agents at scale with Fleet Automation](https://www.datadoghq.com/blog/fleet-automation/)
