# Source: https://docs.datadoghq.com/cloudprem/introduction/network.md

# Source: https://docs.datadoghq.com/agent/configuration/network.md

---
title: Network Traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Agent > Agent Configuration > Network Traffic
---

# Network Traffic

## Overview{% #overview %}

{% alert level="danger" %}
Traffic is always initiated by the Agent to Datadog. No sessions are ever initiated from Datadog back to the Agent.
{% /alert %}

All Agent traffic is sent over SSL. The destination is dependent on the Datadog service and site. To see destinations based on your [Datadog site](https://docs.datadoghq.com/getting_started/site/), click the `DATADOG SITE` selector on the right.

## Installation{% #installation %}

Add the following domains to your inclusion list to allow for Agent installation:

- `install.datadoghq.com`
- `yum.datadoghq.com`
- `keys.datadoghq.com`
- `apt.datadoghq.com`
- `windows-agent.datadoghq.com`

## Destinations{% #destinations %}

{% alert level="warning" %}
Starting with version 7.67.0, the Agent converts Datadog sites to fully qualified domain names (by adding a dot at the end of the domain) to reduce the number of DNS queries. For example, it sends APM payloads to `trace.agent.datadoghq.com.`.This behavior can be disabled in version 7.72.0 and later by setting `convert_dd_site_fqdn.enabled` to `false` in the configuration, or with the environment variable `DD_CONVERT_DD_SITE_FQDN_ENABLED=false`.
{% /alert %}

{% dl %}

{% dt %}
[APM](https://docs.datadoghq.com/tracing/)
{% /dt %}

{% dd %}
`trace.agent.``instrumentation-telemetry-intake.`
{% /dd %}

{% dt %}
[LLM Observabilty](https://docs.datadoghq.com/llm_observability/)
{% /dt %}

{% dd %}
`llmobs-intake.`
{% /dd %}

{% dt %}
[Container Images](https://docs.datadoghq.com/infrastructure/containers/container_images)
{% /dt %}

{% dd %}
`contimage-intake.`
{% /dd %}

{% dt %}
[Live Containers](https://docs.datadoghq.com/infrastructure/livecontainers/), [Live Process](https://docs.datadoghq.com/infrastructure/process/), [Cloud Network Monitoring](https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/), [Universal Service Monitoring](https://docs.datadoghq.com/universal_service_monitoring/)
{% /dt %}

{% dd %}
`process.`
{% /dd %}

{% dt %}
[Network Device Monitoring](https://docs.datadoghq.com/network_monitoring/devices)
{% /dt %}

{% dd %}
`ndm-intake.``snmp-traps-intake.``ndmflow-intake.`
{% /dd %}

{% dt %}
[Network Path](https://docs.datadoghq.com/network_monitoring/network_path/)
{% /dt %}

{% dd %}
`netpath-intake.`
{% /dd %}

{% dt %}
[Orchestrator](https://docs.datadoghq.com/infrastructure/containers/#kubernetes-orchestrator-explorer)
{% /dt %}

{% dd %}
`orchestrator.``contlcycle-intake.`
{% /dd %}

{% dt %}
[Profiling](https://docs.datadoghq.com/profiler/)
{% /dt %}

{% dd %}
`intake.profile.`
{% /dd %}

{% dt %}
[Real User Monitoring (RUM)](https://docs.datadoghq.com/real_user_monitoring/)
{% /dt %}


{% dt %}
[Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/)
{% /dt %}

{% dd %}
`sbom-intake.`
{% /dd %}

{% dt %}
[Synthetic Monitoring Private Locations](https://docs.datadoghq.com/synthetics/private_locations)
{% /dt %}

{% dd %}
Synthetics Worker v1.5.0 or later: `intake.synthetics.` is the only endpoint you need to configure.API test results for the Synthetics Worker > v0.1.6: `intake.synthetics.`Browser test results for the Synthetics Worker > v0.2.0: `intake-v2.synthetics.`API test results for the Synthetics Worker < v0.1.5: `api.`
{% /dd %}

{% /dl %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, app.datadoghq.eu, us3.datadoghq.com, us5.datadoghq.com, ap1.datadoghq.com, ap2.datadoghq.com

{% dl %}

{% dt %}
[Remote Configuration](https://docs.datadoghq.com/remote_configuration)
{% /dt %}

{% dd %}
`config.`
{% /dd %}

{% dt %}
[Database Monitoring](https://docs.datadoghq.com/database_monitoring/)
{% /dt %}

{% dd %}
`dbm-metrics-intake.``dbquery-intake.`
{% /dd %}

{% /dl %}

{% /callout %}

{% alert level="warning" %}
TCP log collection is **not supported**. Datadog provides **no delivery or reliability guarantees** when using TCP, and log data may be lost without notice. For reliable ingestion, use the HTTP intake endpoint, an official Datadog Agent, or forwarder integration instead. For more information, see [Log Collection](https://docs.datadoghq.com/logs/log_collection/?tab=host).
{% /alert %}

{% dl %}

{% dt %}
[Logs](https://docs.datadoghq.com/logs/) & [HIPAA logs](https://docs.datadoghq.com/data_security/logs/#hipaa-enabled-customers)
{% /dt %}

{% dd %}
(Deprecated) TCP: HTTP: Other: See [logs endpoints](https://docs.datadoghq.com/logs/log_collection/#logging-endpoints)
{% /dd %}

{% dt %}
[HIPAA logs legacy](https://docs.datadoghq.com/data_security/logs/#hipaa-enabled-customers) (Deprecated, TCP not supported)
{% /dt %}


{% dt %}
[Metrics](https://docs.datadoghq.com/metrics/), [Service Checks](https://docs.datadoghq.com/developers/service_checks/), [Events](https://docs.datadoghq.com/events/), and other Agent metadata
{% /dt %}

{% dd %}
`<VERSION>-app.agent.`For example, Agent v7.31.0 reports to `7-31-0-app.agent.`. You must add `*.agent.` to your inclusion list in your firewall(s).Since v6.1.0, the Agent also queries Datadog's API to provide non-critical functionality (For example, display validity of configured API key):Agent v7.18.0 or 6.18.0 and later: `api.`Agent < v7.18.0 or 6.18.0: `app.`
{% /dd %}

{% dt %}
[Agent flare](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare)
{% /dt %}

{% dd %}
`<VERSION>-flare.agent.`For example, Agent v7.31.0 sends flare data to `7-31-0-flare.agent.`. You must add `*.agent.` to your inclusion list in your firewall(s).
{% /dd %}

{% /dl %}

### Static IP addresses{% #static-ip-addresses %}

All of these domains are **CNAME** records pointing to a set of static IP addresses. These addresses can be found at `https://ip-ranges.`.

The information is structured as JSON following this schema:

```text
{
    "version": 1,                          // <-- incremented every time this information is changed
    "modified": "YYYY-MM-DD-HH-MM-SS",     // <-- timestamp of the last modification
    "agents": {                            // <-- the IPs used by the Agent to submit metrics to Datadog
        "prefixes_ipv4": [                 // <-- list of IPv4 CIDR blocks
            "a.b.c.d/x",
            ...
        ],
        "prefixes_ipv6": [                 // <-- list of IPv6 CIDR blocks
            ...
        ]
    },
    "api": {...},                          // <-- the IPs used by the Agent for non-critical functionality (querying information from API)
    "apm": {...},                          // <-- the IPs used by the Agent to submit APM data to Datadog
    "logs": {...},                         // <-- the IPs used by the Agent to submit logs to Datadog
    "process": {...},                      // <-- the IPs used by the Agent to submit process data to Datadog
    "orchestrator": {...},                 // <-- the IPs used by the Agent to submit container data to Datadog
    "remote-configuration": {...},         // <-- the IPs used by the Agent to retrieve its dynamic configuration
    "synthetics": {...},                   // <-- the source IPs used by Synthetic workers (not used by the Agent)
    "synthetics-private-locations": {...}, // <-- the IPs used by Synthetics Private Locations workers to submit data to Datadog (not used by the Agent)
    "webhooks": {...}                      // <-- the source IPs used by Datadog to connect to 3rd party infrastructure over HTTP (not used by the Agent)
}
```

Each section has a dedicated endpoint, for example:

- `https://ip-ranges.  /logs.json` for the IPs used to receive logs data over TCP.
- `https://ip-ranges.  /apm.json` for the IPs used to receive APM data.

### Inclusion{% #inclusion %}

Add all of the `ip-ranges` to your inclusion list. While only a subset are active at any given moment, there are variations over time within the entire set due to regular network operation and maintenance.

## Open ports{% #open-ports %}

{% alert level="danger" %}
All outbound traffic is sent over SSL through TCP or UDP.Ensure the Agent is only accessible by your applications or trusted network sources using a firewall rule or similar network restriction. Untrusted access can allow malicious actors to perform several invasive actions, including but not limited to writing traces and metrics to your Datadog account, or obtaining information about your configuration and services.
{% /alert %}

Open the following ports to benefit from all the **Agent** functionalities:

#### Outbound{% #outbound %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, app.datadoghq.eu

| Product/Functionality                                                                                                                                                                                                                   | Port | Protocol         | Description                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AgentAPMContainersLive ProcessesMetricsCloud Network MonitoringUniversal Service Monitoring                                                                                                                                             | 443  | TCP              | Most Agent data uses port 443.                                                                                                                                                                                                                         |
| [Custom Agent Autoscaling](https://docs.datadoghq.com/containers/guide/cluster_agent_autoscaling_metrics)                                                                                                                               | 8443 | TCP              |
| Log collection                                                                                                                                                                                                                          |      | (Deprecated) TCP | Logging over TCP.**Note**:TCP log collection is **not supported**. Datadog provides **no delivery or reliability guarantees** when using TCP, and log data may be lost without notice.                                                                 |
| For reliable ingestion, use the HTTP intake endpoint, an official Datadog Agent, or forwarder integration instead. For other connection types, see [logs endpoints](https://docs.datadoghq.com/logs/log_collection/#logging-endpoints). |
| NTP                                                                                                                                                                                                                                     | 123  | UDP              | Network Time Protocol (NTP). See [default NTP targets](https://docs.datadoghq.com/integrations/ntp/#overview).For information on troubleshooting NTP, see [NTP issues](https://docs.datadoghq.com/agent/faq/network-time-protocol-ntp-offset-issues/). |

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com, us5.datadoghq.com, app.ddog-gov.com, ap1.datadoghq.com, ap2.datadoghq.com

| Product/Functionality                                                                       | Port | Protocol | Description                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------- | ---- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AgentAPMContainersLive ProcessesMetricsCloud Network MonitoringUniversal Service Monitoring | 443  | TCP      | Most Agent data uses port 443.                                                                                                                                                                                                                         |
| NTP                                                                                         | 123  | UDP      | Network Time Protocol (NTP). See [default NTP targets](https://docs.datadoghq.com/integrations/ntp/#overview).For information on troubleshooting NTP, see [NTP issues](https://docs.datadoghq.com/agent/faq/network-time-protocol-ntp-offset-issues/). |

{% /callout %}

#### Inbound{% #inbound %}

Used for Agent services communicating with each other locally within the host only.

| Product/Functionality                                                        | Port | Protocol | Description                                                                                                                    |
| ---------------------------------------------------------------------------- | ---- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [Agent browser GUI](https://docs.datadoghq.com/agent/basic_agent_usage/#gui) | 5002 | TCP      |
| APM receiver                                                                 | 8126 | TCP      | Includes Tracing and the Profiler.                                                                                             |
| [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/)                | 8125 | UDP      | Port for DogStatsD unless `dogstatsd_non_local_traffic` is set to true. This port is available on IPv4 localhost: `127.0.0.1`. |
| go_expvar server (APM)                                                       | 5012 | TCP      | For more information, see [the go_expar integration documentation](https://docs.datadoghq.com/integrations/go_expvar/).        |
| go_expvar integration server                                                 | 5000 | TCP      | For more information, see [the go_expar integration documentation](https://docs.datadoghq.com/integrations/go_expvar/).        |
| IPC API                                                                      | 5001 | TCP      | Port used for Inter Process Communication (IPC).                                                                               |
| Process Agent debug                                                          | 6062 | TCP      | Debug endpoints for the Process Agent.                                                                                         |
| Process Agent runtime                                                        | 6162 | TCP      | Runtime configuration settings for the Process Agent.                                                                          |

## Configure ports{% #configure-ports %}

If you need to change an inbound port because the default port is already in use by an existing service on your network, edit the `datadog.yaml` configuration file. You can find most of the ports in the **Advanced Configuration** section of the file:

In the `datadog.yaml` file:

```yaml
## @param expvar_port - integer - optional - default: 5000
## @env DD_EXPVAR_PORT - integer - optional - default: 5000
## The port for the go_expvar server.
#
# expvar_port: 5000

## @param cmd_port - integer - optional - default: 5001
## @env DD_CMD_PORT - integer - optional - default: 5001
## The port on which the IPC api listens.
#
# cmd_port: 5001

## @param GUI_port - integer - optional
## @env DD_GUI_PORT - integer - optional
## The port for the browser GUI to be served.
## Setting 'GUI_port: -1' turns off the GUI completely
## Default is:
##  * Windows & macOS : `5002`
##  * Linux: `-1`
##
#
# GUI_port: <GUI_PORT>
```

The APM receiver and the DogStatsD ports are located in the **Trace Collection Configuration** and **DogStatsD Configuration** sections of the `datadog.yaml` configuration file, respectively:

In the `datadog.yaml` file:

```yaml
## @param dogstatsd_port - integer - optional - default: 8125
## @env DD_DOGSTATSD_PORT - integer - optional - default: 8125
## Override the Agent DogStatsD port.
## Note: Make sure your client is sending to the same UDP port.
#
# dogstatsd_port: 8125

[...]

## @param receiver_port - integer - optional - default: 8126
## @env DD_APM_RECEIVER_PORT - integer - optional - default: 8126
## The port that the trace receiver should listen on.
## Set to 0 to disable the HTTP receiver.
#
# receiver_port: 8126
```

{% alert level="danger" %}
If you change the DogStatsD port or APM receiver port value here, you must also change the APM tracing library configuration for the corresponding port. See the information about configuring ports in the [Library Configuration docs for your language](https://docs.datadoghq.com/tracing/trace_collection/library_config/).
{% /alert %}

## Using proxies{% #using-proxies %}

For a detailed configuration guide on proxy setup, see [Agent Proxy Configuration](https://docs.datadoghq.com/agent/configuration/proxy/).

## Data buffering{% #data-buffering %}

If the network becomes unavailable, the Agent stores the metrics in memory. The maximum memory usage for storing the metrics is defined by the `forwarder_retry_queue_payloads_max_size` configuration setting. When this limit is reached, the metrics are dropped.

Agent v7.27.0 or later stores the metrics on disk when the memory limit is reached. Enable this capability by setting `forwarder_storage_max_size_in_bytes` to a positive value indicating the maximum amount of storage space, in bytes, that the Agent can use to store the metrics on disk.

The metrics are stored in the folder defined by the `forwarder_storage_path` setting, which is by default `/opt/datadog-agent/run/transactions_to_retry` on Unix systems, and `C:\ProgramData\Datadog\run\transactions_to_retry` on Windows.

To avoid running out of storage space, the Agent stores the metrics on disk only if the total storage space used is less than 80 percent. This limit is defined by `forwarder_storage_max_disk_ratio` setting.

## Installing the Datadog Operator{% #installing-the-datadog-operator %}

If you are installing the Datadog Operator in a Kubernetes environment with limited connectivity, you need to allowlist the following endpoints for TCP port 443, based on your location:

- `gcr.io/datadoghq` (GCR US)
- `eu.gcr.io/datadoghq` (GCR Europe)
- `asia.gcr.io/datadoghq` (GCR Asia)
- `datadoghq.azurecr.io` (Azure)
- `public.ecr.aws/datadog` (AWS)
- `docker.io/datadog` (DockerHub)

## Further Reading{% #further-reading %}

- [Learn about the Datadog site](https://docs.datadoghq.com/getting_started/site)
- [Collect your logs](https://docs.datadoghq.com/logs/)
- [Collect your processes](https://docs.datadoghq.com/infrastructure/process)
- [Collect your traces](https://docs.datadoghq.com/tracing)
