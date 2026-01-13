# Source: https://docs.datadoghq.com/agent/supported_platforms/aix.md

---
title: AIX
description: >-
  Install and manage the Datadog UNIX Agent on IBM AIX systems for
  infrastructure monitoring and custom metrics collection.
breadcrumbs: Docs > Agent > Supported Platforms > AIX
source_url: https://docs.datadoghq.com/supported_platforms/aix/index.html
---

# AIX

## Overview{% #overview %}

The [Datadog UNIX Agent](https://github.com/DataDog/datadog-unix-agent/blob/master/README.md) brings host-level monitoring to IBM AIX (PowerPC 8+) so you can visualize system metrics, enable additional Datadog products, and troubleshoot services that still run on-prem.

The UNIX Agent supports Infrastructure Monitoring and Custom Metrics using [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/?tab=hostagent). Other products like APM, Live Process Monitoring, Cloud Network Monitoring, and Log Management are not supported on the UNIX Agent. See [Supported Platforms](https://docs.datadoghq.com/agent/supported_platforms/?tab=unix) for the complete list of supported AIX versions.

This page walks you through installing, operating, and removing the Datadog UNIX Agent on AIX.

## Installation{% #installation %}

### Prerequisites{% #prerequisites %}

- Root privileges (or sudo) on each host
- Outbound HTTPS (443) to `.datadoghq.com`
- curl or ksh (shipped on AIX by default)
- Verify your host is running a [Supported AIX version](https://docs.datadoghq.com/agent/supported_platforms/?tab=unix)

### Install the Agent{% #install-the-agent %}

To install the Agent on AIX, follow the [in-app instructions in Fleet Automation](https://app.datadoghq.com/fleet/install-agent/latest?platform=aix), and run the generated script on your hosts.

{% image
   source="https://datadog-docs.imgix.net/images/agent/basic_agent_usage/aix_img2_july_25.535469aa7cc24d3ec40e0a5a8223efd4.png?auto=format"
   alt="The Datadog Agent installation step for AIX hosts." /%}

### Installation log files{% #installation-log-files %}

You can find the Agent installation log in the `dd-aix-install.log` file. To disable this logging, remove the `-e dd-aix-install.log` parameter in the installation command.

## Commands{% #commands %}

| Description             | Command (as root)           |
| ----------------------- | --------------------------- |
| Start Agent             | `startsrc -s datadog-agent` |
| Stop Agent              | `stopsrc -s datadog-agent`  |
| Status of Agent service | `lssrc -s datadog-agent`    |
| Agent status page       | `datadog-agent status`      |
| Send flare              | `datadog-agent flare`       |
| Show all commands       | `datadog-agent --help`      |

## Configure the Agent{% #configure-the-agent %}

The [Datadog Agent configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file) is located in `/etc/datadog-agent/datadog.yaml`. This YAML file holds the host-wide connection details used to send data to Datadog including:

- `api_key`: Your organization's [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys)
- `site`: Target Datadog region (see [Datadog Sites](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site))
- `proxy`: HTTP/HTTPS proxy endpoints for outbound traffic (see [Datadog Agent Proxy Configuration](https://docs.datadoghq.com/agent/configuration/proxy/))
- Default tags, log level, and Datadog configurations

A fully commented reference file, located in `/etc/datadog-agent/datadog.yaml.example`, lists every available option for comparison or to copy and paste.

Alternatively, see the [datadog.yaml.example file](https://github.com/DataDog/datadog-unix-agent/blob/master/docs/datadog.yaml.example) for all available configuration options.

### Integration files{% #integration-files %}

Configuration files for integrations exist in `/etc/datadog-agent/conf.d/`. Each integration has its own subdirectory, `<INTEGRATION>.d/`, that contains:

- `conf.yaml`: The active configuration controlling how the integration gathers metrics and logs
- `conf.yaml.example`: A sample illustrating supported keys and defaults

## Available integrations{% #available-integrations %}

{% dl %}

{% dt %}
Out of the box integrations
{% /dt %}

{% dd %}
`cpu`
{% /dd %}

{% dd %}
`filesystem`
{% /dd %}

{% dd %}
`iostat`
{% /dd %}

{% dd %}
`load`
{% /dd %}

{% dd %}
`memory`
{% /dd %}

{% dd %}
`uptime`
{% /dd %}

{% dd %}
`disk`
{% /dd %}

{% dd %}
`network`
{% /dd %}

{% dt %}
Additional integrations
{% /dt %}

{% dd %}
`process`
{% /dd %}

{% dd %}
`lparstats`
{% /dd %}

{% dd %}
`ibm_was` (WebSphere Application Server)
{% /dd %}

{% /dl %}

**Note:** Metric coverage can differ from the UNIX, Linux, Windows, and macOS integrations.

## Monitor Agent uptime{% #monitor-agent-uptime %}

You can use the metric `datadog.agent.running` to monitor the uptime of an Agent. The metric emits a value of `1` if the Agent is reporting to Datadog.

## Uninstall the Agent{% #uninstall-the-agent %}

To remove an installed Agent, run the following `installp` command:

```shell
installp -e dd-aix-uninstall.log -uv datadog-unix-agent
```

**Note:** Agent uninstallation logs can be found in the `dd-aix-install.log` file. To disable this logging, remove the `-e` parameter in the uninstallation command.

## Further Reading{% #further-reading %}

- [Find out more about the Agent's architecture](https://docs.datadoghq.com/agent/architecture/#agent-architecture)
- [Configure inbound ports](https://docs.datadoghq.com/agent/configuration/network#configure-ports)
- [Monitor AIX with the Datadog UNIX Agent](https://www.datadoghq.com/blog/announcing-ibm-aix-agent/)
