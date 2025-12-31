# Source: https://planetscale.com/docs/vitess/tutorials/prometheus-metrics-datadog.md

# Source: https://planetscale.com/docs/vitess/monitoring/prometheus-metrics-datadog.md

# Source: https://planetscale.com/docs/vitess/guides/prometheus-metrics-datadog.md

# Sending Prometheus Metrics to Datadog

> If you're looking for more metrics than PlanetScale's native Datadog integration provides, this tutorial will show how to configure your [Datadog agent](https://docs.datadoghq.com/agent/) to scrape PlanetScale's [Prometheus infrastructure](/docs/vitess/integrations/prometheus) automatically, allowing you to collect detailed metrics for all of your PlanetScale branches.

## Overview

In this tutorial, we'll assume that you have a Datadog Agent Version 7 running. For more information on what the Datadog Agent is and how to install it, start with the [Datadog Agent documentation](https://docs.datadoghq.com/getting_started/agent/).

For the purposes of this guide, we'll be using a Datadog agent running with the recommended installation steps on a Linux system.

## Prerequisites

You'll need a working Datadog agent and access to add a [Custom Agent Check](https://docs.datadoghq.com/developers/custom_checks/) to that instance. This may require `root` or `sudo` access on the machine running the Datadog agent.

You'll also need a [Service token](/docs/api/reference/service-tokens) in your Organization, with the `read_metrics_endpoints` permission granted.

## Adding the Plugin to the Datadog Agent

Go to [https://github.com/planetscale/planetscale-datadog](https://github.com/planetscale/planetscale-datadog), which is the repository that has our custom OpenMetrics Check.

Place the unedited `planetscale.py` in the `checks.d` directory of your Datadog Agent.

* On Linux, that is `/etc/datadog-agent/checks.d/`
* On macOS, that is `/opt/datadog-agent/etc/checks.d/`

Make sure that it belongs to the appropriate user. If you're using the recommended Linux installation steps, it will have created a `dd-agent` user:

```
$ pwd
/etc/datadog-agent/checks.d
$ ls -al planetscale.py
-rw-r--r-- 1 dd-agent dd-agent 9261 Apr  2 22:54 planetscale.py
```

This file is owned by the `dd-agent` user and group in the `/etc/datadog-agent/checks.d` directory.

If you're on macOS, it will depend on whether you installed the agent as a 'Single User Agent' or a 'Systemwide Agent'. If you picked Single User, there should be no additional permission changes needed. If you installed it as a Systemwide agent, make sure the user and group you installed the agent with as ownership of the file.

## Configuring the Datadog Agent

Now that we have the plugin installed, we need to configure it. In the `conf.d` directory of the Datadog agent take the `conf.d/planetscale.yaml.example` file and edit it with your organization name and Service Token information. It should look like this:

```bash expandable theme={null}
instances:
  - planetscale_organization: 'nick' # Required: Your PlanetScale organization ID
    ps_service_token_id: '${TOKEN_ID}' # Required: Your PlanetScale Service Token ID
    ps_service_token_secret: '${TOKEN}' # Required: Your PlanetScale Service Token Secret. Consider using Datadog secrets management: https://docs.datadoghq.com/agent/guide/secrets-management/

    namespace: 'planetscale' # Required: Namespace for the metrics
    metrics: # Required: List of metrics to collect. Use mapping for renaming/type overrides.
      - planetscale_vtgate_queries_duration: vtgate_query_duration

    min_collection_interval: 60
    send_distribution_buckets: true
    collect_counters_with_distributions: true
```

This configures the integration to look for all of the branches in the `"nick"` PlanetScale organization, only collect the `planetscale_vtgate_queries_duration` metric, which it will rename `vtgate_query_duration` and put it inside of the `planetscale` namespace.

Save the file at `planetscale.yaml`, making sure to double check permissions:

```
$ pwd
/etc/datadog-agent/conf.d
$ ls -al planetscale.yaml
-rw-r--r-- 1 root root 1518 Apr  2 22:57 planetscale.yaml
```

## Restart the Datadog Agent

Now that this is configured and installed, restart the Agent:

```
$ sudo systemctl restart datadog-agent
```

## Validating the PlanetScale Plugin

Now that the Datadog Agent is running the PlanetScale plugin, metrics should start flowing into Datadog within a couple of minutes. To validate, we can ask the Datadog Agent:

```
sudo -u dd-agent -- datadog-agent check planetscale
```

If the plugin is installed successfuly, this should output the scrape targets for your branches, as well as metadata about when it was last run and how many metrics were emitted:

```bash expandable theme={null}
$ sudo -u dd-agent -- datadog-agent check planetscale
=== Service Checks ===
[
  {
    "check": "planetscale.api.can_connect",
    "host_name": "ubuntu",
    "timestamp": 1743638192,
    "status": 0,
    "message": "",
    "tags": [
      "planetscale_org:nick"
    ]
  },
  {
    "check": "planetscale.prometheus.health",
    "host_name": "ubuntu",
    "timestamp": 1743638192,
    "status": 0,
    "message": "",
    "tags": [
      "endpoint:https://metrics.psdb.cloud/metrics/branch/7wxuxewx4l0p?..."
    ]
  },
  {
    "check": "planetscale.prometheus.health",
    "host_name": "ubuntu",
    "timestamp": 1743638192,
    "status": 0,
    "message": "",
    "tags": [
      "endpoint:https://metrics.psdb.cloud/metrics/branch/6o0rr27785fl?..."
    ]
  }
]


  Running Checks
  ==============

    planetscale (unversioned)
    -------------------------
      Instance ID: planetscale:planetscale:8d4d64f696d967be [OK]
      Configuration Source: file:/etc/datadog-agent/conf.d/planetscale.yaml
      Total Runs: 1
      Metric Samples: Last Run: 0, Total: 0
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 3, Total: 3
      Histogram Buckets: Last Run: 77, Total: 77
      Average Execution Time : 809ms
      Last Execution Date : 2025-04-02 23:56:32 UTC (1743638192000)
      Last Successful Execution Date : 2025-04-02 23:56:32 UTC (1743638192000)


  Metadata
  ========
    config.hash: planetscale:planetscale:8d4d64f696d967be
    config.provider: file
```

The Service Checks show that it has successfully connected to the PlanetScale API to request information about how to scrape for the branches in my organization, and it has successfully scraped both of what it discovered.

We can also see that it successfully executed at `2025-04-02 23:56:32 UTC` and produced 77 Histogram Buckets.

## Adding Metrics

In our earlier configuration, we only added one metric. For a complete list of what PlanetScale exposes, please take a look at our [Metrics Reference Documentation](/docs/vitess/integrations/prometheus-metrics).

Note that the Datadog agent [normalizes metrics with certain suffixes starting in v7.32.0](https://github.com/DataDog/integrations-core/blob/master/openmetrics/README.md):

> Starting in Datadog Agent v7.32.0, in adherence to the OpenMetrics specification standard, counter names ending in \_total must be specified without the \_total suffix. For example, to collect promhttp\_metric\_handler\_requests\_total, specify the metric name promhttp\_metric\_handler\_requests. This submits to Datadog the metric name appended with .count, promhttp\_metric\_handler\_requests.count.

This means that to scrape a metric such as `planetscale_mysql_bytes_received_total`, you would configure the Datadog agent for `planetscale_mysql_bytes_received`.

If I want to collect additional metrics, I can add them to the list:

```
    metrics: # Required: List of metrics to collect. Use mapping for renaming/type overrides.
      - planetscale_vtgate_queries_duration: vtgate_query_duration
      - planetscale_edge_active_connections: active_connections
```

Then, restart the Datadog Agent:

```
$ sudo systemctl restart datadog-agent
```

If I check the status of the PlanetScale Plugin, I can see our last run added a Metric Sample:

```bash  theme={null}
  Running Checks
  ==============

    planetscale (unversioned)
    -------------------------
      Instance ID: planetscale:planetscale:fde586b60a54a38f [OK]
      Configuration Source: file:/etc/datadog-agent/conf.d/planetscale.yaml
      Total Runs: 1
      Metric Samples: Last Run: 1, Total: 1
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 3, Total: 3
      Histogram Buckets: Last Run: 77, Total: 77
      Average Execution Time : 826ms
      Last Execution Date : 2025-04-03 00:01:45 UTC (1743638505000)
      Last Successful Execution Date : 2025-04-03 00:01:45 UTC (1743638505000)
```

In the Datadog UI, I can see data for the `planetscale.active_connections` metric:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/prometheus-datadog-graph.png?fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=af198d4ffbb6a7ca9bd821afd5d79d83" alt="Datadog Connections Metric" data-og-width="2770" width="2770" data-og-height="1206" height="1206" data-path="docs/vitess/tutorials/prometheus-datadog-graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/prometheus-datadog-graph.png?w=280&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=ba4fabc1030fe00f62d363eb04438b17 280w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/prometheus-datadog-graph.png?w=560&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=5d9107c8dc8cf34d267a57fc59179006 560w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/prometheus-datadog-graph.png?w=840&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=80385f6b51c3a50fcc2c507d8317a061 840w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/prometheus-datadog-graph.png?w=1100&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=1dd84603686131e0547c6931a5e68045 1100w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/prometheus-datadog-graph.png?w=1650&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=7bd1a120cff8194ad5069748dd7b5ef5 1650w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/prometheus-datadog-graph.png?w=2500&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=8b08666bcb27fcc7d57ec5c0aca1b2ba 2500w" />
</Frame>

## What's Next?

Now that you're sending a couple of metrics from PlanetScale to Datadog, take a look at our [full list](/docs/vitess/integrations/prometheus-metrics) and start building dashboards!

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt