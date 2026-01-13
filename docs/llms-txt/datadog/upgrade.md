# Source: https://docs.datadoghq.com/agent/guide/upgrade.md

---
title: Upgrade to Datadog Agent 7
description: >-
  Instructions for upgrading from Datadog Agent 5 or 6 to Agent 7 across Linux,
  Windows, and macOS platforms with Python 3 compatibility notes.
breadcrumbs: Docs > Agent > Agent Guides > Upgrade to Datadog Agent 7
source_url: https://docs.datadoghq.com/guide/upgrade/index.html
---

# Upgrade to Datadog Agent 7

{% alert level="info" %}
Agent 7 only supports Python 3 custom checks. [Check if your custom checks are Python 3 compatible](https://docs.datadoghq.com/agent/guide/python-3) before upgrading to Agent 7.
{% /alert %}

## From Agent 6{% #from-agent-6 %}

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

## From Agent 5{% #from-agent-5 %}

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

**Note:** The upgrade process won't automatically move **custom** Agent checks. This is by design as Datadog cannot guarantee full backwards compatibility out of the box. See the [Python 3 Custom Check Migration](https://docs.datadoghq.com/agent/guide/python-3/) guide to discover how to migrate your custom check from Python 2 to Python 3.

## Further Reading{% #further-reading %}

- [Migrate your Custom Checks from python 2 to python 3](https://docs.datadoghq.com/agent/guide/python-3/)
