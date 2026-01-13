# Source: https://docs.datadoghq.com/agent.md

---
title: Agent
description: Install and configure the Agent to collect data
breadcrumbs: Docs > Agent
source_url: https://docs.datadoghq.com/index.html
---

# Agent

{% alert level="info" %}
Agent v7 is available. [Upgrade to the newest version](https://docs.datadoghq.com/agent/versions/upgrade_to_agent_v7) to benefit from all new functionality.
{% /alert %}

## Overview{% #overview %}

The Datadog Agent is software that runs on your hosts. It collects events and metrics from hosts and sends them to Datadog, where you can analyze your monitoring and performance data. The Datadog Agent is open source and its source code is available on GitHub at [DataDog/datadog-agent](https://github.com/DataDog/datadog-agent).
Choose A Platform[platform](https://docs.datadoghq.com/agent/basic_agent_usage/amazonlinux/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/aix/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/windows/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/osx/)[platform](https://docs.datadoghq.com/agent/docker/)[platform](https://docs.datadoghq.com/agent/kubernetes/)[platform](https://docs.datadoghq.com/serverless/google_cloud_run/containers/sidecar/)[platform](https://docs.datadoghq.com/containers/amazon_ecs/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/heroku/)[platform](https://docs.datadoghq.com/serverless/aws_lambda/instrumentation/)[platform](https://docs.datadoghq.com/integrations/guide/cloud-foundry-setup/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/ansible/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/chef/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/puppet/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/saltstack/)[platform](https://docs.datadoghq.com/agent/basic_agent_usage/sccm/)
### To get started using the Agent, select your platform.

{% tab title=" Host-based" %}
[integration](https://docs.datadoghq.com/agent/basic_agent_usage/amazonlinux/)[integration](https://docs.datadoghq.com/agent/basic_agent_usage/aix/)[integration](https://docs.datadoghq.com/agent/basic_agent_usage/windows/)[integration](https://docs.datadoghq.com/agent/basic_agent_usage/osx/)
{% /tab %}

{% tab title=" Container platforms" %}
[integration](https://docs.datadoghq.com/agent/docker/)[integration](https://docs.datadoghq.com/agent/kubernetes/)[integration](https://docs.datadoghq.com/serverless/google_cloud_run/containers/sidecar/)[integration](https://docs.datadoghq.com/containers/amazon_ecs/)
{% /tab %}

{% tab title=" Cloud platforms" %}
[integration](https://docs.datadoghq.com/agent/basic_agent_usage/heroku/)[integration](https://docs.datadoghq.com/serverless/aws_lambda/instrumentation/)[integration](https://docs.datadoghq.com/integrations/guide/cloud-foundry-setup/)
{% /tab %}

{% tab title=" Configuration management " %}
[integration](https://docs.datadoghq.com/agent/basic_agent_usage/ansible/)[integration](https://docs.datadoghq.com/agent/basic_agent_usage/chef/)[integration](https://docs.datadoghq.com/agent/basic_agent_usage/puppet/)[integration](https://docs.datadoghq.com/agent/basic_agent_usage/saltstack/)[integration](https://docs.datadoghq.com/agent/basic_agent_usage/sccm/)
{% /tab %}

{% alert level="info" %}
Datadog recommends you update Datadog Agent with every minor and patch release, or, at a minimum, monthly.

Upgrading to a major Datadog Agent version and keeping it updated is the only supported way to get the latest Agent functionality and fixes.

*It is recommended to fully install the Agent.* However, a standalone DogStatsD package is available for Amazon Linux, CentOS, Debian, Fedora, Red Hat, SUSE, and Ubuntu. This package is used in containerized environments where DogStatsD runs as a sidecar or environments running a DogStatsD server without full Agent functionality.
{% /alert %}

## Managing the Agent{% #managing-the-agent %}

### Managing the Agent with Fleet Automation (recommended){% #managing-the-agent-with-fleet-automation-recommended %}

[Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation) is the primary, in-app workflow for installing, upgrading, configuring, and troubleshooting the Datadog Agent at scale.

{% image
   source="https://datadog-docs.imgix.net/images/agent/basic_agent_usage/basic_agent_2_july_25.d2765e079fe75f83aed16c13aa5f3555.png?auto=format"
   alt="The Fleet Automation view that allows you to centrally manage your Datadog Agents in one place." /%}

- **View configuration & history**: View every Agent in your fleet, its version, enabled products, configuration files, and historical changes from a single page.
- **[Upgrade outdated Agents](https://docs.datadoghq.com/agent/fleet_automation/remote_management/#remotely-upgrade-your-agents)**: Trigger remote upgrades for your Agents to keep your fleet updated in a few clicks.
- **[Send a flare for support](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/?tab=agent#send-a-flare-from-the-datadog-site)**: From the Support tab of a host, generate a flare and attach it to an existing or new Support case without having to use the command line.
- **Audit API-key usage**: Identify which Agents are using a specific API key and rotate keys safely.

### Datadog Agent Manager GUI{% #datadog-agent-manager-gui %}

{% alert level="info" %}
The Agent GUI is not supported on 32-bit Windows platforms.
{% /alert %}

Use the Datadog Agent Manager GUI to:

- View the status information for your Agent
- View all running checks
- View the Agent log
- Edit the Agent configuration file (`datadog.yaml`)
- Add or edit Agent checks
- Send flares

The Datadog Agent Manager GUI is enabled by default on Windows and macOS, and runs on port `5002`. Use the `datadog-agent launch-gui` command to open the GUI in your default web browser.

You can change the GUI's default port in your `datadog.yaml` configuration file. To disable the GUI, set the port's value to `-1`. On Linux, the GUI is disabled by default.

GUI requirements:

- Cookies must be enabled in your browser. The GUI generates and saves a token in your browser, which is used for authenticating all communications with the GUI server.
- To start the GUI, the user must have the required permissions. If you are able to open `datadog.yaml`, you are able to use the GUI.
- For security reasons, the GUI can **only** be accessed from the local network interface (`localhost`/`127.0.0.1`), therefore you must be on the host where the Agent is running. You can't run the Agent on a VM or a container and access it from the host machine.

### Command-line interface{% #command-line-interface %}

From Agent 6 and later, the Agent command-line interface is based on subcommands. For a full list of Agent subcommands, see [Agent Commands](https://docs.datadoghq.com/agent/configuration/agent-commands/).

## Getting further with the Datadog Agent{% #getting-further-with-the-datadog-agent %}

### Update the Agent{% #update-the-agent %}

To manually update the Datadog Agent core between two minor versions on a given host, run the [corresponding installation command for your platform](https://app.datadoghq.com/account/settings/agent/latest).

**Note**: If you want to manually update one specific Agent integration, see the [Integration Management guide](https://docs.datadoghq.com/agent/guide/integration-management/).

### Configuration files{% #configuration-files %}

See the [Agent configuration files documentation](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/).

### Datadog site{% #datadog-site %}

Edit the [Agent's main configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file), `datadog.yaml`, to set the `site` parameter (defaults to `datadoghq.com`).

```yaml
site: 
```

**Note**: See the [Getting Started with Datadog Sites documentation](https://docs.datadoghq.com/getting_started/site/) for further details on the `site` parameter.

### Log location{% #log-location %}

See the [Agent log files documentation](https://docs.datadoghq.com/agent/configuration/agent-log-files/).

## Agent overhead{% #agent-overhead %}

An example of the Datadog Agent resource consumption is below. Tests were made on an Amazon EC2 machine `c5.xlarge` instance (4 VCPU/ 8GB RAM) and comparable performance was seen for ARM64-based instances with similar resourcing. The vanilla `datadog-agent` was running with a process check to monitor the Agent itself. Enabling more integrations may increase Agent resource consumption. Enabling JMX Checks forces the Agent to use more memory depending on the number of beans exposed by the monitored JVMs. Enabling the trace and process Agents increases the resource consumption as well.

- Agent Test version: 7.34.0
- CPU: ~ 0.08% of the CPU used on average
- Memory: ~ 130MB of RAM used (RSS memory)
- Network bandwidth: ~ 140 B/s â¼ | 800 B/s â²
- Disk:
  - Linux 830MB to 880MB depending on the distribution
  - Windows: 870MB

**Log Collection**:

The results below are obtained from a collection of *110KB of logs per seconds* from a file with the [HTTP forwarder](https://docs.datadoghq.com/agent/logs/log_transport/?tab=https#enforce-a-specific-transport) enabled. It shows the evolution of resource usage for the different compression levels available.

{% tab title="HTTP compression level 6" %}

- Agent Test version: 6.15.0
- CPU: ~ 1.5% of the CPU used on average
- Memory: ~ 95MB of RAM used.
- Network bandwidth: ~ 14 KB/s â²

{% /tab %}

{% tab title="HTTP compression level 1" %}

- Agent Test version: 6.15.0
- CPU: ~ 1% of the CPU used on average
- Memory: ~ 95MB of RAM used.
- Network bandwidth: ~ 20 KB/s â²

{% /tab %}

{% tab title="HTTP Uncompressed" %}

- Agent Test version: 6.15.0
- CPU: ~ 0.7% of the CPU used on average
- Memory: ~ 90MB of RAM used (RSS memory)
- Network bandwidth: ~ 200 KB/s â²

{% /tab %}

## Additional resources{% #additional-resources %}

- [Kubernetes: Install and configure the Datadog Agent on Kubernetes.](https://docs.datadoghq.com/agent/kubernetes)
- [Cluster Agent: Install and configure the Cluster Agent for Kubernetes, a version of the Datadog Agent built to efficiently gather monitoring data from across an orchestrated cluster.](https://docs.datadoghq.com/agent/cluster_agent)
- [Amazon ECS: Install and configure the Datadog Agent on Amazon ECS.](https://docs.datadoghq.com/agent/amazon_ecs)
- [AWS Fargate: Install and configure the Datadog Agent with Amazon ECS on AWS Fargate](https://docs.datadoghq.com/integrations/ecs_fargate/)
- [IoT: Install and configure the Datadog IoT Agent, a version of the Datadog Agent optimized for monitoring IoT devices and embedded applications.](https://docs.datadoghq.com/agent/iot)
- [Log Collection: Enable and configure log collection in the Datadog Agent.](https://docs.datadoghq.com/agent/logs)
- [Proxy: If your network configuration restricts outbound traffic, use a proxy for Agent traffic.](https://docs.datadoghq.com/agent/configuration/proxy)
- [Versions: Agent 7 is the latest major version of the Datadog Agent. Learn about changes between major Agent versions and how to upgrade.](https://docs.datadoghq.com/agent/versions/)
- [Troubleshooting: Find troubleshooting information for the Datadog Agent.](https://docs.datadoghq.com/agent/troubleshooting)
- [Guides: These are in-depth, step-by-step tutorials for using the Agent.](https://docs.datadoghq.com/agent/guide)
- [Security: Information on the main security capabilities and features available to customers to ensure their environment is secure.](https://docs.datadoghq.com/agent/security)
- [Configure Observability Pipelines and Datadog: Deploy the Observability Pipelines Worker as an aggregator to collect, transform, and route all of your logs and metrics to any destination.](https://docs.datadoghq.com/getting_started/observability_pipelines)

## Further Reading{% #further-reading %}

- [Collect your logs](https://docs.datadoghq.com/logs/)
- [Collect your processes](https://docs.datadoghq.com/infrastructure/process/)
- [Collect your traces](https://docs.datadoghq.com/tracing/)
- [Why install the Agent on cloud instances?](https://docs.datadoghq.com/agent/faq/why-should-i-install-the-agent-on-my-cloud-instances/)
- [Don't fear the Agent](https://www.datadoghq.com/blog/dont-fear-the-agent/)
