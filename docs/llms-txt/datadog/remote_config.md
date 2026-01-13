# Source: https://docs.datadoghq.com/tracing/guide/remote_config.md

---
title: Setting up Remote Configuration for Tracing
description: >-
  Learn how to set up and use Remote Configuration to dynamically manage tracing
  library settings without restarting applications.
breadcrumbs: Docs > APM > Tracing Guides > Setting up Remote Configuration for Tracing
source_url: https://docs.datadoghq.com/guide/remote_config/index.html
---

# Setting up Remote Configuration for Tracing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

This guide covers setting up and using Remote Configuration with your tracing libraries. For more information on how Remote Configuration works, see [Remote Configuration](https://docs.datadoghq.com/remote_configuration).

## Prerequisites{% #prerequisites %}

- [Datadog Agent](https://docs.datadoghq.com/agent/) 7.47.0 or higher installed on your hosts or containers.
- Upgrade your tracing libraries to a Remote Configuration-compatible version. For more information, see the [Supported configuration options](https://docs.datadoghq.com/tracing/trace_collection/runtime_config/#supported-configuration-options) section.
- Ensure your RBAC permissions include [`org_management`](https://docs.datadoghq.com/account_management/rbac/permissions/), so you can enable Remote Configuration for your organization.
- Ensure your RBAC permissions include [`api_keys_write`](https://docs.datadoghq.com/account_management/rbac/permissions#api-and-application-keys), so you can create a new API key with the Remote Configuration capability, or add the capability to an existing API key. Contact your organization's Datadog administrator to update your permissions if you don't have it. A key with this capability allows you to authenticate and authorize your Agent to use Remote Configuration.
- Ensure you have the `APM Remote Configuration Read` and `APM Remote Configuration Write` [permissions](https://docs.datadoghq.com/account_management/rbac/permissions/). **Note**: If you don't have these permissions, ask your Datadog Admin to update your permissions from your Organization Settings.

## Set up Remote Configuration{% #set-up-remote-configuration %}

1. Ensure that [Remote Configuration is enabled for your organization](https://app.datadoghq.com/organization-settings/remote-config). This enables Datadog components across your organization to receive configurations from Datadog.

1. Select an existing API key or create a new API key, and enable the Remote Configuration capability on the key if it is not already enabled.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/remote_config/RC_Key_updated.b0e2299082792781d28ea9a3c1e88950.png?auto=format"
      alt="API Key properties with Remote Configuration capability Enable button." /%}

1. Restart your Agent.

## Review Remote Configuration status of tracing libraries{% #review-remote-configuration-status-of-tracing-libraries %}

You can gain visibility into the Remote Configuration status of your Tracer libraries through the [Remote Configuration UI](https://app.datadoghq.com/organization-settings/remote-config).

The following table describes the meaning of each tracing library status:

| Tracing library Status | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONNECTED              | The tracing library is successfully connected to the Remote Configuration service through the associated Agent. This is the optimal state you want your tracing library to be in for Remote Configuration.                                                                                                                                                                                                                                                                                                                             |
| UNAUTHORIZED           | The tracing library is associated with an Agent which doesn't have `APM Remote Configuration Read` permission on its API key. To fix the issue, you need to enable Remote Configuration capability on the API Key used by the Agent associated with the tracing library.                                                                                                                                                                                                                                                               |
| CONNECTION ERROR       | The tracing library deployed in your environment is associated with an Agent that has `remote_config.enabled` set to true in its `datadog.yaml` configuration file, however, the Agent cannot be found in the Remote Configuration service. The most likely cause of this is that the associated Agent is unable to reach Remote Configuration [endpoints](https://docs.datadoghq.com/agent/configuration/network). To fix the issue, you need to allow outbound HTTPS access to Remote Configuration endpoints from your environment. |
| DISABLED               | The tracing library deployed in your environment is associated with an Agent that has `remote_config.enabled` set to false in its `datadog.yaml` configuration file. This could be set deliberately or mistakenly. To enable Remote Configuration on the associated Agent, set `remote_config.enabled` to true.                                                                                                                                                                                                                        |
| NOT CONNECTED          | The tracing library cannot be found in the Remote Configuration service and is associated with an Agent that could have `remote_config.enabled` set to true or false in its `datadog.yaml` configuration file. Check your local Agent configuration or your proxy settings.                                                                                                                                                                                                                                                            |
| UNSUPPORTED AGENT      | The tracing library is associated with an Agent which is not Remote Configuration capable. To fix this issue, update the associated Agent software to the latest available version.                                                                                                                                                                                                                                                                                                                                                    |
| NOT DETECTED           | The tracing library does not support Remote Configuration. To fix this issue, update the tracing library software to the latest available version.                                                                                                                                                                                                                                                                                                                                                                                     |
| UNKNOWN                | The tracing library status is unknown, and it can't be determined if an Agent is associated with the tracing library. For example, this could be because the Agent is deployed on a fully managed serverless container service like AWS Fargate.                                                                                                                                                                                                                                                                                       |

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

## Further reading{% #further-reading %}

- [Remote Configuration](https://docs.datadoghq.com/remote_configuration)
