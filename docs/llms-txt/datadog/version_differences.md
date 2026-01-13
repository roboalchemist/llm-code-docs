# Source: https://docs.datadoghq.com/agent/guide/version_differences.md

---
title: Agent Version differences
description: >-
  Overview of key differences between major Datadog Agent versions, including
  performance improvements, new functionalities, and upgrade recommendations.
breadcrumbs: Docs > Agent > Agent Guides > Agent Version differences
source_url: https://docs.datadoghq.com/guide/version_differences/index.html
---

# Agent Version differences

{% alert level="info" %}
Datadog recommends you update Datadog Agent with every minor and patch release, or, at a minimum, monthly.

Upgrading to the latest major Datadog Agent version and keeping it updated is the only supported way to get the latest Agent functionality and fixes. The Agent has frequent update releases, though, and managing updates at enterprise scale can be challenging. That doesn't mean you should wait for major releases before updating. The right update cadence for your organization will depend on your infrastructure and your configuration management practices, but aim for monthly.

To update the Datadog Agent core between two minor versions on a given host, run [the corresponding install command for your platform](https://docs.datadoghq.com/agent/versions/upgrade_between_agent_minor_versions).

Datadog Agent release numbering follows [SemVer](https://semver.org/) rules.
{% /alert %}

## Changes between major Agent versions{% #changes-between-major-agent-versions %}

{% tab title="Agent v7 vs v6" %}
Agent v7 is the latest major version of the Datadog Agent. The main difference from Agent v6 is that **this version only includes support for Python 3 for integrations and custom checks**.

See the [Upgrade to Agent v7 documentation](https://docs.datadoghq.com/agent/versions/upgrade_to_agent_v7/) to learn how to upgrade your Agent to version 7. All official integrations support Python 3 out-of-the-box. Follow the [Python 3 Custom Check Migration guide](https://docs.datadoghq.com/agent/guide/python-3/) to migrate your custom checks to Python 3.

**Note**: You can test this migration with Agent v6, by [Using Python 3 with Datadog Agent v6](https://docs.datadoghq.com/agent/guide/agent-v6-python-3/).
{% /tab %}

{% tab title="Agent v6 vs v5" %}
**Agent version 6 main changes**:

The big difference between Agent 5 and Agent 6 is that Agent 6 is a complete rewrite of the core Agent in Golang. Golang has allowed the Agent to take advantage of concurrency. In place of the three processes the Agent v5 used to runâ*the Forwarder*, *the Collector*, and *DogStatsD*âthere is now only one process: *the Agent*. It also comes with a number of other core improvements:

- Agent v6 has significantly improved resource usage over Agent v5:

  - Decreased CPU usage
  - Decreased memory usage
  - Fewer file descriptors
  - All around decreased footprint

- Agent 6 uses [two additional ports](https://docs.datadoghq.com/agent/#agent-architecture):

  - `5000` to expose its runtime metrics.

  - `5001` for the [Agent CLI/GUI commands](https://docs.datadoghq.com/agent/configuration/agent-commands/).

**Note**: You can specify different ports for `expvar_port` and `cmd_port` in the `datadog.yaml` file.

- Custom build your Agent v6 and [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/unix_socket/) much easier and with many more configuration options, to include or exclude almost anything.

**Agent v6 new functionalities**:

To see all changes between Agent v5 and v6, consult the [Datadog Agent dedicated changes](https://github.com/DataDog/datadog-agent/blob/master/docs/agent/changes.md) documentation. The following are key differentiators:

- [Distributions metrics](https://docs.datadoghq.com/metrics/types/?tab=distribution#metric-types) can be performed on the server directly to calculate real, effective global percentiles.
- [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/unix_socket/) can be used over a Unix socket instead of over UDP.
- [Live Process monitoring is available for Windows](https://docs.datadoghq.com/infrastructure/process/).
- [Prometheus OpenMetrics is supported natively](https://www.datadoghq.com/blog/monitor-prometheus-metrics).
- [All your logs can be sent to Datadog for alerting, analysis, and correlation with metrics](https://docs.datadoghq.com/logs/).

{% /tab %}

## Further Reading{% #further-reading %}

- [Upgrade to Agent v7](https://docs.datadoghq.com/agent/versions/upgrade_to_agent_v7)
- [Upgrade to Agent v6](https://docs.datadoghq.com/agent/versions/upgrade_to_agent_v6)
- [Upgrade Between Agent Minor Versions](https://docs.datadoghq.com/agent/versions/upgrade_between_agent_minor_versions)
- [Agent v6 Changes](https://docs.datadoghq.com/agent/faq/agent_v6_changes)
