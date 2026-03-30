# Source: https://northflank.com/docs/v1/application/observe/observability-on-northflank.md

# Observability on Northflank

Northflank provides observability tooling to monitor and ensure your applications and microservices are available.

## Logs and metrics

You can view live and historical logs and metrics for builds, deployments, jobs, and addons.

You can configure health checks for deployments and jobs to ensure your applications are available to serve traffic, and that containers can be automatically replaced if they are in an unhealthy state.

You can also integrate external log aggregators to analyze and retain logs from your Northflank workloads.

Organisations can use audit logs to track actions taken on Northflank and ensure compliance.

- [See previous builds: See previous builds, their status, and view detailed logs and metrics for each build.](/v1/application/observe/see-builds)
- [Monitor containers: Monitor the health and resource usage of deployments, and view detailed logs and metrics for individual container.](/v1/application/observe/monitor-containers)
- [View logs: View detailed, real-time logs from builds, deployments, and more.](/v1/application/observe/view-logs)
- [View metrics: View detailed, real-time metrics from builds, deployments, and more.](/v1/application/observe/view-metrics)
- [Configure health checks: Monitor the uptime and success of your deployed services and builds to ensure your code runs correctly and is always available.](/v1/application/observe/configure-health-checks)
- [Configure log sinks: Integrate third-party logging and observability services with Northflank.](/v1/application/observe/configure-log-sinks)
- [Audit logs: Monitor and review events affecting your organisation, teams, projects, and resources.](/v1/application/observe/audit-logs)

## Alerts and notifications

You can configure infrastructure alerts to monitor usage and be informed of any issues with your resources. These are delivered via a notification integration with other service providers, or via custom webhooks.

- [Infrastructure alerts: Set infrastructure alerts to let you and your team know when there is an issue with your applications or addons.](/v1/application/observe/set-infrastructure-alerts)
- [Discord notifications: Send notifications to Discord channels with Discord webhook integrations.](/v1/application/observe/configure-notification-integrations#discord-notifications)
- [Slack notifications: Send notifications to Slack channels, groups, or users.](/v1/application/observe/configure-notification-integrations#slack-notifications)
- [Teams notifications: Send notifications to Microsoft Teams channels.](/v1/application/observe/configure-notification-integrations#teams-notifications)
- [Webhook notifications: Build your own integrations with custom Northflank webhooks.](/v1/application/observe/configure-notification-integrations#webhook-notifications)
- [Monitor spending: Monitor your current resource usage across services.](/v1/application/billing/monitor-spending)
- [Configure billing alerts: Set up alerts to notify you if your spend exceeds a specified amount.](/v1/application/billing/monitor-spending#set-up-billing-alerts)
