# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/without_infrastructure_monitoring.md

---
title: Setting Up Cloud Security without Infrastructure Monitoring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security > Setting
  Up Cloud Security without Infrastructure Monitoring
---

# Setting Up Cloud Security without Infrastructure Monitoring

## Set up Cloud Security with your cloud provider{% #set-up-cloud-security-with-your-cloud-provider %}

In addition to setting up Cloud Security with or without an Agent, you can also set it up without Infrastructure Monitoring. Doing so disables metric data submission (including Custom Metrics) so that hosts stop showing up in Datadog.

### AWS{% #aws %}

1. Navigate to the [AWS Integration configuration page](https://app.datadoghq.com/integrations/amazon-web-services) in Datadog.
1. On the **Configuration** tab, select the account you want to enable Cloud Security on.If you don't see the required account, add it by clicking **Add AWS Account(s)** and following the onscreen prompts.
1. To turn off infrastructure monitoring on the selected account, under the account number, navigate to the **Metric Collection** tab, then click the **disable metric collection** link. Then, click **Disable Metric Collection** to confirm.
1. On the **Resource Collection** tab, click **Enable** next to Cloud Security. You are redirected to the Cloud Security Setup page, and a setup dialog automatically opens for the selected account.
1. On the setup dialog, switch the **Enable Resource Scanning** toggle to the on position.
1. Click **Done** to complete the setup.

**Note**: In your Cloud Security settings, set up [resource evaluation filters](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters/) to limit the number of hosts you need security on.

### Azure{% #azure %}

1. Navigate to the [Azure Integration configuration page](https://app.datadoghq.com/integrations/azure) in Datadog.
1. Select the client ID or subscription you want to enable Cloud Security on.If you don't see the required client ID, add it by clicking **Add New App Registration** and following the onscreen prompts.
1. To turn off infrastructure monitoring on the selected account, under the client ID, navigate to the **Metric Collection** tab, then turn off the **Enable Metric Collection** toggle.
1. On the **Resource Collection** tab, click **Enable** next to Cloud Security. You are redirected to the Cloud Security Setup page, which automatically scrolls to the selected Azure subscription in the Cloud Integrations section.
1. Switch the **Resource Scanning** toggle to the on position.
1. Click **Done** to complete the setup.

**Note**: In your Cloud Security settings, set up [resource evaluation filters](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters/) to limit the number of hosts you need security on.

### Google Cloud Platform{% #google-cloud-platform %}

1. Navigate to the [Google Cloud Platform configuration page](https://app.datadoghq.com/integrations/google-cloud-platform) in Datadog.
1. Select the service account you want to enable Cloud Security on.If you don't see the required account, add it by clicking **Add GCP Account** and following the onscreen prompts.
1. To turn off infrastructure monitoring on the selected account, under the account name, navigate to the **Metric Collection** tab. Then, above the Metric Collection table, click **Disable All**.
1. On the **Resource Collection** tab, click **Enable** next to Cloud Security. You are redirected to the Cloud Security Setup page, which automatically scrolls to the selected Google Cloud Platform project in the Cloud Integrations section.
1. Switch the **Resource Scanning** toggle to the on position.
1. Click **Done** to complete the setup.

**Note**: In your Cloud Security settings, set up [resource evaluation filters](https://docs.datadoghq.com/security/cloud_security_management/guide/resource_evaluation_filters/) to limit the number of hosts you need security on.

## Set up the Datadog Agent{% #set-up-the-datadog-agent %}

If you're using the Datadog Agent, you must run Agent v6.4+.

{% tab title="Host " %}

1. Open the [datadog.yaml configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/).

1. Add `enable_payloads` as a top-level attribute anywhere in the configuration file with the following settings:

   ```yaml
   enable_payloads:
       series: false
       events: false
       service_checks: false
       sketches: false
   ```

1. [Configure the Agent with Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup/agent).

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).

{% /tab %}

{% tab title="Docker" %}
If you're using the Docker containerized Agent, add and set the following environment variables to `false` to the [Cloud Security configuration for Agent](https://docs.datadoghq.com/security/cloud_security_management/setup/agent/docker/):

```shell
-e DD_ENABLE_PAYLOADS_EVENTS=false \
-e DD_ENABLE_PAYLOADS_SERIES=false \
-e DD_ENABLE_PAYLOADS_SERVICE_CHECKS=false \
-e DD_ENABLE_PAYLOADS_SKETCHES=false \
```

{% /tab %}

{% tab title="Kubernetes" %}
If you're deploying the Agent in Kubernetes, make the following changes in your Helm chart in addition to the [Cloud Security configuration for Agent](https://docs.datadoghq.com/security/cloud_security_management/setup/agent/kubernetes?tab=helm):

```yaml
clusterAgent:
  enabled: false
datadog:
[...]
  processAgent:
    enabled: false
    containerCollection: false
[...]
  env:
    - name: DD_ENABLE_PAYLOADS_EVENTS
      value: "false"
    - name: DD_ENABLE_PAYLOADS_SERIES
      value: "false"
    - name: DD_ENABLE_PAYLOADS_SERVICE_CHECKS
      value: "false"
    - name: DD_ENABLE_PAYLOADS_SKETCHES
      value: "false"
```

{% /tab %}
