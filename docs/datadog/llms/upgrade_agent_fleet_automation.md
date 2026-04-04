# Source: https://docs.datadoghq.com/agent/guide/upgrade_agent_fleet_automation.md

---
title: Upgrade your Datadog Agent
description: >-
  Guide for upgrading Datadog Agent versions using Fleet Automation remote
  management, installation scripts, and configuration management tools.
breadcrumbs: Docs > Agent > Agent Guides > Upgrade your Datadog Agent
---

# Upgrade your Datadog Agent

## Overview{% #overview %}

Datadog recommends you update your Datadog Agent with every [minor and patch](https://github.com/DataDog/datadog-agent/releases?page=1) release. This guide walks you through how to roll out a new Agent version across your hosts in a few clicks.

## Upgrade between minor versions of the Agent{% #upgrade-between-minor-versions-of-the-agent %}

### Upgrade remotely with Fleet Automation{% #upgrade-remotely-with-fleet-automation %}

[Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/) enables you to centrally manage your fleet of Datadog Agents. Fleet Automation includes [Remote Agent Management](https://docs.datadoghq.com/agent/fleet_automation/remote_management), which allows you to remotely upgrade Agents across non-containerized Linux and Windows environments. See [Remote Agent Management: Upgrade your Datadog Agents](https://docs.datadoghq.com/agent/fleet_automation/remote_management/#upgrade-your-agents).

### Upgrade with script or configuration management tooling{% #upgrade-with-script-or-configuration-management-tooling %}

Follow the [in-app instructions](https://app.datadoghq.com/fleet/install-agent/latest?platform=overview) to upgrade Datadog Agents across container, host-based, and Infrastructure as Code (IaC) tool-managed environments. The guided flow generates an Agent installation command tailored to your platform for upgrading the Agent. By default, the command installs the latest version of the Agent. To upgrade to a specific minor version, set `DD_AGENT_MINOR_VERSION=<TARGET_MINOR>` before running the script.

## Upgrade between major versions of the Agent{% #upgrade-between-major-versions-of-the-agent %}

{% alert level="info" %}
Agent 7 only supports Python 3 custom checks. [Verify if your custom checks are Python 3 compatible](https://docs.datadoghq.com/agent/guide/python-3) before upgrading to Agent 7.
{% /alert %}

### Upgrade from Agent 6 to Agent 7{% #upgrade-from-agent-6-to-agent-7 %}

{% tab title="Linux" %}
Run the following Agent installation command to upgrade your Agent from version 6 to version 7:

{% dl %}

{% dt %}
The following command works on Amazon Linux, CentOS, Debian, Fedora, Red Hat, Ubuntu, and SUSE:
{% /dt %}

{% dd %}
`DD_API_KEY="<DATADOG_API_KEY>" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"`
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Windows" %}

1. [Download the Datadog Agent installer](https://ddagent-windows-stable.s3.amazonaws.com/datadog-agent-7-latest.amd64.msi).
1. Run the installer (as **Administrator**) by opening `datadog-agent-7-latest.amd64.msi`.
1. Follow the prompts, accept the license agreement, and enter your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
1. When the install finishes, you are given the option to launch the Datadog Agent Manager.

**Note**: Links to all available versions of the Windows Installer are [provided in JSON format](https://ddagent-windows-stable.s3.amazonaws.com/installers_v2.json).
{% /tab %}

{% tab title="MacOS" %}
Run the Agent installation command with the environment variable `DD_AGENT_MAJOR_VERSION=7` to upgrade your Agent from version 6 to version 7:

```shell
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY="<DATADOG_API_KEY>" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_mac_os.sh)"
```

{% /tab %}

### Upgrade from Agent 5 to Agent 7{% #upgrade-from-agent-5-to-agent-7 %}

{% tab title="Linux" %}
Run the Agent installation command with the environment variable `DD_UPGRADE="true"` to upgrade your Agent from version 5 to version 7. The Agent v7 installer can automatically convert v5 configurations during the upgrade:

{% dl %}

{% dt %}
The following command works on Amazon Linux, CentOS, Debian, Fedora, Red Hat, Ubuntu, and SUSE:
{% /dt %}

{% dd %}
`DD_UPGRADE="true" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"`
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Windows" %}

1. Upgrade your Agent to version 6 following the [manual upgrade process](https://docs.datadoghq.com/agent/versions/upgrade_to_agent_v6/?tab=windows#manual-upgrade).
1. Follow the From Agent v6 to Agent v7 upgrade instructions.

{% /tab %}

{% tab title="MacOS" %}
Run the Agent installation command with the environment variable `DD_AGENT_MAJOR_VERSION=7` and `DD_UPGRADE="true"` to upgrade your Agent from version 5 to version 7. The Agent v7 installer can automatically convert v5 configurations during the upgrade:

```shell
DD_UPGRADE="true" DD_AGENT_MAJOR_VERSION=7 bash -c "$(curl -L https://install.datadoghq.com/scripts/install_mac_os.sh)"
```

{% /tab %}

**Note:** The upgrade process does not automatically move **custom** Agent checks. This is by design as Datadog cannot guarantee full backwards compatibility out of the box. See the [Python 3 Custom Check Migration](https://docs.datadoghq.com/agent/guide/python-3/) guide to discover how to migrate your custom check from Python 2 to Python 3.

## Further reading{% #further-reading %}

- [Agent Troubleshooting](https://docs.datadoghq.com/agent/troubleshooting/)
- [The Datadog Agent](https://docs.datadoghq.com/agent/)
