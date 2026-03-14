# Source: https://docs.envzero.com/changelogs/2022/12/log-forwarding-to-google-cloud-logging.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🪵 Log Forwarding to Google Cloud Logging

> env0 now supports Google Cloud Logging as a target for Infrastructure as Code deployment logs. By adding Google Cloud Logging alongside other currently supported centralized logging and observability platforms, users can see their IaC data right alongside their other logging data.

Centralized log systems have been around for a long time, and in today's world, they are more than just log aggregators. Metrics, traces, analytics, and other valuable tools are all rolled up into logging systems. Today we've added integration between env0 and Google Cloud Logging. env0 can now forward your infrastructure deployment logs, giving you the ability to monitor, track and analyze logs.

This integration is an addition to the [existing integrations](changelog:logs-forwarding-to-datadog-splunk-and-logzio)l.

## ✨ Google Cloud Logging setup ✨

Follow Setting up Google Cloud Logging is simple - just follow [This guide](/guides/integrations/logs-forwarding/gcp-logging)

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/12/5d62842-google-logs.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=4bfffdcc020efef4529957b6b02c5922" alt="Feature demonstration screenshot showing new functionality" width="1766" height="481" data-path="images/changelogs/2022/12/5d62842-google-logs.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
