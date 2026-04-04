# Source: https://docs.datadoghq.com/agent/guide/integration-management.md

---
title: Integration Management
description: >-
  Guide to managing official Datadog integrations using the datadog-agent
  integration command, including install, remove, show, and freeze operations.
breadcrumbs: Docs > Agent > Agent Guides > Integration Management
---

# Integration Management

## Overview{% #overview %}

The Agent comes with a set of bundled official Datadog integrations to allow users to start monitoring their applications quickly. These integrations are available as single Python packages, and you can upgrade them separately.

**Note**: Starting with Agent version 7.69, Community, Partner, and Marketplace integrations are automatically retained during upgrades. To opt out of this functionality, create an empty file named `.skip_install_python_third_party_deps` in the `/etc/datadog-agent/` directory prior to upgrading. If this file is present, integrations are not retained and must be manually reinstalled after the upgrade.

For Agent v6.8+, the `datadog-agent integration` command allows users to manage the official Datadog integrations that are available for the Agent. It has the following subcommands:

- install
- remove
- show
- freeze

Print the usage and documentation of these commands with `datadog-agent integration --help`. For Linux, execute the command as the `dd-agent` user. For Windows, execute the command as an `administrator`.

## Integration commands{% #integration-commands %}

### Workflow{% #workflow %}

1. Check the version of the integration installed in your Agent with the `show` command.
1. Review the changelog of the specific integration on the [integrations-core](https://github.com/DataDog/integrations-core) repository to identify the version you want.
1. Install the integration with the `install` command.
1. Restart your Agent.

**Note**: When using a configuration management tool, it is recommended to pin the integration to the desired version. When you're ready to upgrade the Agent, remove the pin. Upgrading the Agent without removing the integration pin can cause the configuration management tool to fail if the version of the integration is not compatible with the new version of the Agent.

### Install{% #install %}

Use the `datadog-agent integration install` command to install a specific version of an official Datadog integration (available on the [integrations-core repository](https://github.com/DataDog/integrations-core)), provided that it is compatible with the version of the Agent. The command does this verification and exits with a failure in case of incompatibilities.

An integration is compatible and installable if both conditions are met:

1. The version is newer than the one [shipped with the Agent](https://github.com/DataDog/integrations-core/blob/master/AGENT_INTEGRATIONS.md).
1. It is compatible with the version of the [datadog_checks_base](https://github.com/DataDog/integrations-core/tree/master/datadog_checks_base) in the installed Agent.

**Note**: `datadog_checks_base` cannot be manually installed. The base check can only be upgraded by upgrading the Agent.

The syntax for this command is `datadog-agent integration install <INTEGRATION_PACKAGE_NAME>==<VERSION>` where `<INTEGRATION_PACKAGE_NAME>` is the name of the integration prefixed with `datadog-`.

For example, to install version 3.6.0 of the vSphere integration, run:

{% tab title="Linux" %}

```shell
sudo -u dd-agent -- datadog-agent integration install datadog-vsphere==3.6.0
```

{% /tab %}

{% tab title="Windows PowerShell" %}
Run `powershell.exe` as **elevated** (run as admin).

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" integration install datadog-vsphere==3.6.0
```

{% /tab %}

The command installs the Python package of the integration and copies the configuration files (`conf.yaml.example`, `conf.yaml.default`, `auto_conf.yaml`) to the `conf.d` directory, overwriting the existing ones. The same thing is done during a full Agent upgrade. If a failure occurs while copying of the files, the command exits with a failure, but the version of the integration you specified still gets installed.

After upgrading, restart your Agent to begin using the newly installed integration.

This command is designed specifically to allow users to upgrade an individual integration to get a new feature or bugfix as soon as it is available, without needing to wait for the next release of the Agent. **Note**: It is still recommended to upgrade the Agent when possible, as it always ships the latest version of every integration at the time of the release.

Upon Agent upgrade, every integration that you individually upgraded using the command gets overwritten by the integration shipped within the Agent.

#### Configuration management tools{% #configuration-management-tools %}

Configuration management tools can leverage this command to deploy the version of an integration across your entire infrastructure.

### Remove{% #remove %}

To remove an integration, use the `datadog-agent integration remove` command. The syntax for this command is `datadog-agent integration remove <INTEGRATION_PACKAGE_NAME>` where `<INTEGRATION_PACKAGE_NAME>` is the name of the integration prefixed with `datadog-`.

For example, to remove the vSphere integration, run:

{% tab title="Linux" %}

```shell
sudo -u dd-agent -- datadog-agent integration remove datadog-vsphere
```

{% /tab %}

{% tab title="Windows PowerShell" %}
Run `powershell.exe` as **elevated** (run as admin).

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" integration remove datadog-vsphere
```

{% /tab %}

Removing an integration does not remove the corresponding configuration folder in the `conf.d` directory.

### Show{% #show %}

To get information, such as the version, about an installed integration, use the `datadog-agent integration show` command. The syntax for this command is `datadog-agent integration show <INTEGRATION_PACKAGE_NAME>` where `<INTEGRATION_PACKAGE_NAME>` is the name of the integration prefixed with `datadog-`.

For example, to show information on the vSphere integration, run:

{% tab title="Linux" %}

```shell
sudo -u dd-agent -- datadog-agent integration show datadog-vsphere
```

{% /tab %}

{% tab title="Windows PowerShell" %}
Run `powershell.exe` as **elevated** (run as admin).

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" integration show datadog-vsphere
```

{% /tab %}

### Freeze{% #freeze %}

To list all the Python packages installed in the Agent's Python environment, use the `datadog-agent integration freeze` command. This lists all the Datadog integrations (packages starting with `datadog-`) and the Python dependencies required to run the integrations.

{% tab title="Linux" %}

```text
sudo -u dd-agent -- datadog-agent integration freeze
```

{% /tab %}

{% tab title="Windows PowerShell" %}
Run `powershell.exe` as **elevated** (run as admin).

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" integration freeze
```

{% /tab %}
