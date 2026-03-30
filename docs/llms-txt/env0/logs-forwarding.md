# Source: https://docs.envzero.com/guides/integrations/logs-forwarding.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Logs Forwarding Overview

> Forward deployment and audit logs from env zero to external observability and log aggregation platforms

env zero supports forwarding both deployment logs and audit logs to your preferred external observability or log aggregation platform - such as Datadog, New Relic, Amazon CloudWatch, and more.

You can setup log forwarding in the organization settings integrations page:

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/integrations/6d9aee4518e69356cb14e9fe49ce1c1407b6b5bec79f7d5e8a7125ede7771f86-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=04e8a968c1eab5cbb33c6e1dcf620eba" alt="" width="2352" height="956" data-path="images/guides/integrations/6d9aee4518e69356cb14e9fe49ce1c1407b6b5bec79f7d5e8a7125ede7771f86-image.png" />

This allows teams to:

* Monitor deployments in real time
* Integrate infrastructure activity into existing dashboards
* Maintain audit trails for compliance or security
* Trigger alerts or automations based on activity

## What Can Be Forwarded

env zero supports forwarding the following types of logs:

### Deployment Logs

All standard output and error logs generated during deployments - including plan, apply, and destroy steps.

These logs are streamed live during deployments, and can be forwarded to external tools for real-time visibility or long-term storage.

### Audit Logs

env zero keeps track of actions performed across your organization - such as changes to projects, environment settings, variable updates, or user actions.

These logs are collected and forwarded in near-real time. Audit logging is triggered for any non-GET HTTP request, meaning any change, update, or destructive action performed via the UI or API is tracked.

Once collected, audit events are sent to your configured log platform.

## How Log Forwarding Works

* You configure your preferred log destination from within the env zero UI or using environment variables.
* env zero formats and sends logs directly to your configured provider in near-real time.
* Deployment logs are streamed as deployments occur.
* Audit logs are captured on all mutating operations and sent as they’re stored.

## Allow env zero's IP addresses

env zero will use the IP addresses listed [here](/guides/overview/security-overview/ip-addresses) when sending an Audit Log to any of your destinations. You can add these to your server IP allow list to block spoofed requests.

## Supported Platforms

We support forwarding to a variety of platforms, each platform has its own configuration steps. Please refer to the individual setup guides:

* [AWS CloudWatch](/guides/integrations/logs-forwarding/cloudwatch)
* [AWS S3](/guides/integrations/logs-forwarding/s3)
* [Coralogix](/guides/integrations/logs-forwarding/coralogix)
* [Datadog](/guides/integrations/logs-forwarding/datadog)
* [Dynatrace](/guides/integrations/logs-forwarding/dynatrace)
* [Google Cloud Logging](/guides/integrations/logs-forwarding/gcp-logging)
* [Grafana Loki](/guides/integrations/logs-forwarding/grafana-loki)
* [Logz.io](/guides/integrations/logs-forwarding/logzio)
* [New Relic](/guides/integrations/logs-forwarding/new-relic)
* [Splunk](/guides/integrations/logs-forwarding/splunk)
* [Sumo Logic](/guides/integrations/logs-forwarding/sumologic)

Built with [Mintlify](https://mintlify.com).
