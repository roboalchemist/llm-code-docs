# Source: https://render.com/docs/datadog.md

# Integrating Render with Datadog

[Datadog](https://www.datadoghq.com/) is an observability platform for cloud-scale applications. You can integrate your Render services and databases with Datadog to enable fine-tuned metrics, monitoring, and automated alerting.

Although [core Postgres metrics](postgresql-creating-connecting#dashboard) are available in the Render Dashboard, integrating with Datadog can provide more detailed metrics about the Postgres instance host environment. You can also use Datadog as a centralized location for dashboards and automated alerts.

## Getting started

[Sign up for a Datadog account](https://app.datadoghq.com/signup) if you don't already have one. Then, create or retrieve an API key from your [Datadog organization settings page](https://app.datadoghq.com/organization-settings/api-keys):

[image: Datadog API settings]

> *Make sure to create an _API key_ for your organization.* The Datadog integration doesn't support using an _application key_ or a user-scoped API key.

You can confirm that you've correctly generated an API key by calling Datadog's [validate endpoint](https://docs.datadoghq.com/api/latest/authentication/) with your key.

## Setting up Postgres monitoring

Adding an API key enables a Datadog agent to run alongside your [Render Postgres](postgresql) instance and report metrics to your Datadog account. All metrics reported by the agent are native to the Datadog platform, so you aren't [billed for custom metrics](https://docs.datadoghq.com/account_management/billing/custom_metrics).

> Render currently supports only the [Datadog sites](https://docs.datadoghq.com/getting_started/site/) US1, US3, US5, and EU1. Postgres monitoring is not supported with other Datadog sites (such as AP1, AP2, and US1-FED).

### For new databases

While creating a Postgres database, provide your Datadog API key in the corresponding field:

[image: Add Datadog for new databases]

### For existing databases

Add your Datadog API key from the *Info* tab of your database's page on the [Render Dashboard](https://dashboard.render.com) (in the General section, click *Add Datadog API Key*).

> This requires a restart of your Postgres instance, which causes brief downtime.

[image: Add Datadog for existing databases]

### Available metrics

Render fully supports all of the following Datadog integrations (see the linked documentation for metrics details):

| Integration                                                  | Description                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------- |
| [Postgres](https://docs.datadoghq.com/integrations/postgres) | Metrics related to your PostgreSQL instance                   |
| [Disk](https://docs.datadoghq.com/integrations/disk)         | Metrics related to disk usage and IO for your Postgres volume |
| [Network](https://docs.datadoghq.com/integrations/network)   | Metrics related to TCP/IP network stats of instance           |

In addition, Render reports the following metrics:

| Metric                 | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| `system.cpu.num_cores` | The number of CPUs, as chosen by your database instance type               |
| `system.cpu.system`    | The percentage of time the CPU spent running the kernel                    |
| `system.cpu.user`      | The percentage of time the CPU spent running user space processes          |
| `system.mem.free`      | The amount of free RAM                                                     |
| `system.mem.total`     | The total amount of physical RAM, as chosen by your database instance type |
| `system.mem.used`      | The amount of RAM in use                                                   |

### Viewing metrics in Datadog

You can view reported metrics from any Datadog dashboard or metrics explorer page. You can filter metrics by the `database-id` tag equal to your Render Postgres database ID.

[image: Datadog Postgres metrics]

## Streaming service logs and metrics

You can use Datadog as your observability provider for Render [log streams](log-streams) and [metrics streams](metrics-streams). This enables you to inspect logs and metrics from your Render services directly in your Datadog dashboard.

> *Currently, Render only supports TCP log forwarding with TLS.*
>
> Check the [Datadog docs](https://docs.datadoghq.com/logs/log_collection/?tab=host) to confirm whether TCP log forwarding is supported for your site.

To set these up, follow the general setup instructions in the [log stream docs](log-streams#setup) and [metrics stream docs](metrics-streams#general-setup).

In both cases, you specify your Datadog API key and [Datadog site](https://docs.datadoghq.com/getting_started/site/) in the Render Dashboard. Note that both integrations require an organization-level API key, not an application key or user-scoped API key.

For log streams, you specify the endpoint corresponding to your Datadog site:

| Datadog Site | Endpoint                           |
| ------------ | ---------------------------------- |
| US1          | `intake.logs.datadoghq.com:10516`  |
| EU           | `tcp-intake.logs.datadoghq.eu:443` |