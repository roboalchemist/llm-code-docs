# Source: https://docs.datadoghq.com/getting_started/tagging.md

---
title: Getting Started with Tags
description: Learn how to assign and use tags in Datadog.
breadcrumbs: Docs > Getting Started > Getting Started with Tags
---

# Getting Started with Tags

## Overview{% #overview %}

Tags are a way of adding dimensions to Datadog telemetries so they can be filtered, aggregated, and compared in Datadog visualizations. [Using tags](https://docs.datadoghq.com/getting_started/tagging/using_tags/) enables you to observe aggregate performance across several hosts and (optionally) narrow the set further based on specific elements. In summary, tagging is a method to observe aggregate datapoints.

Tags are `key:value` pairs containing two parts:

- The tag **key** is the identifier. The tag key is case sensitive.
- The tag **value** is the specific data or information associated with the key. Tag values are not unique per resource and can be used across many resources in a `key:value` pair.

Tagging binds different data types in Datadog, allowing for correlation and calls to action between metrics, traces, and logs. This is accomplished with **reserved** tag keys:

| Tag key   | Allows for                                                             |
| --------- | ---------------------------------------------------------------------- |
| `host`    | Correlation between metrics, traces, processes, and logs.              |
| `device`  | Segregation of metrics, traces, processes, and logs by device or disk. |
| `source`  | Span filtering and automated pipeline creation for Log Management.     |
| `service` | Scoping of application-specific data across metrics, traces, and logs. |
| `env`     | Scoping of application-specific data across metrics, traces, and logs. |
| `version` | Scoping of application-specific data across metrics, traces, and logs. |
| `team`    | Assigning ownership to any resources.                                  |

Datadog recommends looking at containers, VMs, and cloud infrastructure at the `service` level in aggregate. For example, look at CPU usage across a collection of hosts that represents a service, rather than CPU usage for server A or server B separately.

Because containers and cloud environments regularly churn through hosts, using tags is important to aggregate your metrics.

## Define tags{% #define-tags %}

Below are Datadog's tagging requirements:

1. Tags must **start with a letter** and after that may contain the characters listed below:

   - Alphanumerics
   - Underscores
   - Minuses
   - Colons
   - Periods
   - Slashes

Other special characters are converted to underscores.

1. Tags can be **up to 200 characters** long and support Unicode letters (which includes most character sets, including languages such as Japanese).

1. Tags are converted to lowercase. Therefore, `CamelCase` tags are not recommended. Authentication (crawler) based integrations convert camel case tags to underscores, for example `TestTag` â> `test_tag`.

1. A tag can be in the format `value` or `<KEY>:<VALUE>`. Commonly used tag keys are `env`, `instance`, and `name`. The key always precedes the first colon of the global tag definition, for example:

| Tag                | Key           | Value          |
| ------------------ | ------------- | -------------- |
| `env:staging:east` | `env`         | `staging:east` |
| `env_staging:east` | `env_staging` | `east`         |

1. Tags should not originate from unbounded sources, such as epoch timestamps, user IDs, or request IDs. Doing so may infinitely [increase the number of metrics](https://docs.datadoghq.com/metrics/) for your organization and impact your billing.

1. Limitations (such as downcasing) only apply to metric tags, not log attributes or span tags.

## Assign tags{% #assign-tags %}

### Tagging methods{% #tagging-methods %}

Tags may be assigned using any (or all) of the following methods.

| Method                                                                                                        | Assign tags                                                     |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [Configuration Files](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/#configuration-files) | Manually in your main Agent or integration configuration files. |
| [UI](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/#ui)                                   | In the Datadog site.                                            |
| [API](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/#api)                                 | When using Datadog's API.                                       |
| [DogStatsD](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/#dogstatsd)                     | When submitting metrics with DogStatsD.                         |

For more information, see [Assigning Tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/).

#### Unified service tagging{% #unified-service-tagging %}

As a best practice, Datadog recommends using unified service tagging when assigning tags. Unified service tagging ties Datadog telemetry together through the use of three standard tags: `env`, `service`, and `version`. To learn how to configure your environment with unified tagging, see [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging).

### Tag inheritance{% #tag-inheritance %}

All metrics, logs, traces, and integrations go through a process of `host-tag` inheritance as data is ingested into Datadog. Since data is associated with a given hostname, those components inherit all the `host-level` tags associated with that host. These tags are visible in the [infrastructure list](https://docs.datadoghq.com/getting_started/tagging/using_tags/#infrastructure) for a given host, sourced from either the cloud provider or the Datadog Agent. See [missing `host-level` tags on new hosts or nodes](https://docs.datadoghq.com/containers/troubleshooting/log-collection?tab=datadogoperator#missing-host-level-tags-on-new-hosts-or-nodes) for more information.

Because tags can be inherited from multiple sources, choose unique and specific key names to avoid duplicating them across sources. For example, if you've set a `service` key on a host (`service:my-host`) and a `service` key on a pod running on that host (`service:my-service`), your data inherits both tags. Opt for more differentiated key names (such as `infra_service`) to avoid duplicate tag keys.

### Tag precedence{% #tag-precedence %}

The Datadog Agent does **not** enforce a precedence order for tags set from different sources. Instead, the Agent collects all tags from every available source, stores each unique value for a given tag key, and emits all of them with the telemetry.

This means a single tag key can have multiple values if it's configured differently across sources. For example, if the `service` tag is set to `payments` in an environment variable, `checkout` in the Agent YAML, and `orders` in a tracing client configuration, telemetry for that service could include:

```
service:payments
service:checkout
service:orders
```

Downstream filters or dashboards should explicitly filter on the desired value if you expect only one.

## Usage{% #usage %}

After you have [assigned tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/) at the host and [integration](https://docs.datadoghq.com/integrations/) level, start using them to filter and group your metrics, traces, and logs. Tags are used in the following areas of your Datadog platform.

| Area                                                                                                                  | Use Tags to                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [Events](https://docs.datadoghq.com/getting_started/tagging/using_tags/#events)                                       | Filter the Event Stream.                                                                                                    |
| [Dashboards](https://docs.datadoghq.com/getting_started/tagging/using_tags/#dashboards)                               | Filter and group metrics on graphs.                                                                                         |
| [Infrastructure](https://docs.datadoghq.com/getting_started/tagging/using_tags/#infrastructure)                       | Filter and group on the host map, infrastructure list, live containers, and live processes views.                           |
| [Monitors](https://docs.datadoghq.com/getting_started/tagging/using_tags/#monitors)                                   | Manage monitors, create monitors, or manage downtime.                                                                       |
| [Metrics](https://docs.datadoghq.com/getting_started/tagging/using_tags/#metrics)                                     | Filter and group with the Metric Explorer.                                                                                  |
| [Integrations](https://docs.datadoghq.com/getting_started/tagging/using_tags/#integrations)                           | Optionally limit metrics for AWS, Google Cloud, and Azure.                                                                  |
| [APM](https://docs.datadoghq.com/getting_started/tagging/using_tags/#apm)                                             | Filter services, traces, and profiles, or navigate to other areas with the Service Map.                                     |
| [RUM & Session Replay](https://docs.datadoghq.com/getting_started/tagging/using_tags/#rum--session-replay)            | Filter event search, analytics, patterns, replays, and issues with the RUM Explorer.                                        |
| [Synthetic Monitoring & Continuous Testing](https://docs.datadoghq.com/getting_started/tagging/using_tags/#synthtics) | Filter and group Synthetic tests or tests running in CI pipelines with the Synthetic Monitoring & Testing Results Explorer. |
| [Notebooks](https://docs.datadoghq.com/getting_started/tagging/using_tags/#notebooks)                                 | Filter and group metrics on graphs.                                                                                         |
| [Logs](https://docs.datadoghq.com/getting_started/tagging/using_tags/#logs)                                           | Filter logs search, analytics, patterns, live tail, and pipelines.                                                          |
| [SLOs](https://docs.datadoghq.com/getting_started/tagging/using_tags/?tab=manageslos#service-level-objectives)        | Search for SLOs, grouped metric-based SLOs, and grouped monitor-based SLOs.                                                 |
| [Developers](https://docs.datadoghq.com/getting_started/tagging/using_tags/#developers)                               | Pull information or set up different areas in the UI with the API.                                                          |
| [Billing](https://docs.datadoghq.com/account_management/billing/usage_attribution/)                                   | Report on Datadog usage by choosing up to three tags, for example: `env`, `team`, and `account_id`.                         |
| [CI Visibility](https://docs.datadoghq.com/getting_started/tagging/using_tags/#ci-visibility)                         | Filter and group test runs or pipeline executions with the CI Visibility Explorer.                                          |

For more information, see [Using Tags](https://docs.datadoghq.com/getting_started/tagging/using_tags/).

## Further Reading{% #further-reading %}

- [Learn how to assign tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/)
- [Learn how to configure unified service tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/)
- [Learn how to use tags](https://docs.datadoghq.com/getting_started/tagging/using_tags/)
- [Join an interactive session on effective tagging with Datadog](https://dtdg.co/fe)
- [Design effective executive dashboards with Datadog](https://www.datadoghq.com/blog/datadog-executive-dashboards)
