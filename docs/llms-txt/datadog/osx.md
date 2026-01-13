# Source: https://docs.datadoghq.com/agent/supported_platforms/osx.md

---
title: macOS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Agent > Supported Platforms > macOS
source_url: https://docs.datadoghq.com/supported_platforms/osx/index.html
---

# macOS

## Overview{% #overview %}

This page outlines the basic features of the Datadog Agent for macOS. See the [Supported Platforms](https://docs.datadoghq.com/agent/supported_platforms/?tab=macos) documentation for the complete list of supported macOS distributions and versions.

## Install the Agent{% #install-the-agent %}

To install the Agent on macOS, follow the [in-app instructions in Fleet Automation](https://app.datadoghq.com/fleet/install-agent/latest?platform=macos), and run the generated script on your hosts.

{% image
   source="https://datadog-docs.imgix.net/images/agent/basic_agent_usage/macos_img_installation.64dbfa0e404712b75d1ea27d8cf6d559.png?auto=format"
   alt="In-app installation steps for the Datadog Agent on a MacOS host." /%}

{% alert level="info" %}
By default, the Agent is installed in a sandbox located at `/opt/datadog-agent`. You can move this folder anywhere; however, this documentation assumes a default installation location.
{% /alert %}

## Commands{% #commands %}

The `launchctl` service manager controls the Agent lifecycle, while other commands can be executed through the Agent binary, systray app, or web GUI.

| Description                        | Command                                                                                                                            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Start Agent as a service           | `launchctl start com.datadoghq.agent` or systray app                                                                               |
| Stop Agent running as a service    | `launchctl stop com.datadoghq.agent` or systray app                                                                                |
| Restart Agent running as a service | Stop and then start the Agent with:`launchctl stop com.datadoghq.agent``launchctl start com.datadoghq.agent`Or use the systray app |
| Status of Agent service            | `launchctl list com.datadoghq.agent` or systray app                                                                                |
| Status page of running Agent       | `datadog-agent status` or web GUI                                                                                                  |
| Send flare                         | `datadog-agent flare` or web GUI                                                                                                   |
| Display command usage              | `datadog-agent --help`                                                                                                             |
| Run a check                        | `datadog-agent check <CHECK_NAME>`                                                                                                 |

## Configuration{% #configuration %}

The [Datadog Agent configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/#agent-main-configuration-file) is located in `/opt/datadog-agent`. This YAML file holds the host-wide connection details used to send data to Datadog including:

- `api_key`: your organization's [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys)
- `site`: target Datadog region (for example `datadoghq.com`, `datadoghq.eu`, `ddog-gov.com`)
- `proxy`: HTTP/HTTPS proxy endpoints for outbound traffic (see [Datadog Agent Proxy Configuration](https://docs.datadoghq.com/agent/configuration/proxy/))
- Default tags, log levels, and Datadog configurations.

A fully commented reference file, located in `/etc/datadog-agent/datadog.yaml.example`, lists every available option for comparison or copy-paste. Alternatively, see the [sample config_template.yaml file](https://github.com/DataDog/datadog-agent/blob/master/pkg/config/config_template.yaml) for all available configuration options.

### Integration files{% #integration-files %}

Configuration files for integrations are found in `/etc/datadog-agent/conf.d/`. Each integration has its own sub-directory, `<INTEGRATION>.d/`, which contains:

- `conf.yaml`: the active configuration controlling how the integration gathers metrics and logs
- `conf.yaml.example`: a sample illustrating supported keys and defaults

## Uninstall the Agent{% #uninstall-the-agent %}

To uninstall the Agent, run the following command:

### Single user installation{% #single-user-installation %}

To remove the Agent and all Agent configuration files:

1. Stop and close the Datadog Agent with the bone icon in the tray.
1. Drag the Datadog application from the application folder to the trash bin.
1. Run the following commands:
   ```shell
   sudo rm -rf /opt/datadog-agent
   sudo rm -rf /usr/local/bin/datadog-agent
   sudo rm -rf ~/.datadog-agent/** # to remove broken symlinks
   launchctl remove com.datadoghq.agent
   sudo rm -rf /var/log/datadog
   ```
1. Reboot your machine for the changes to take effect.

## Uninstall the Agent{% #uninstall-the-agent-1 %}

To remove the Agent and all Agent configuration files:

1. Drag the Datadog application from the application folder to the trash bin.
1. To remove remaining files, run the following:
   ```shell
   sudo rm -rf /opt/datadog-agent
   sudo rm -rf /usr/local/bin/datadog-agent
   sudo rm -rf ~/.datadog-agent/** # to remove broken symlinks
   sudo launchctl disable system/com.datadoghq.agent && sudo launchctl bootout system/com.datadoghq.agent
   sudo launchctl unload /Library/LaunchDaemons/com.datadoghq.agent.plist
   sudo rm /Library/LaunchDaemons/com.datadoghq.agent.plist
   sudo rm -rf /var/log/datadog
   ```
1. Reboot your machine for the changes to take effect.

## Troubleshooting{% #troubleshooting %}

See the [Agent Troubleshooting documentation](https://docs.datadoghq.com/agent/troubleshooting/) for troubleshooting steps.

## Working with the embedded Agent{% #working-with-the-embedded-agent %}

The Agent contains an embedded Python environment at `/opt/datadog-agent/embedded/`. Common binaries such as `python` and `pip` are contained within `/opt/datadog-agent/embedded/bin/`.

See the instructions on how to [add packages to the embedded Agent](https://docs.datadoghq.com/developers/guide/custom-python-package/) for more information.

## Further Reading{% #further-reading %}

- [Collect your logs](https://docs.datadoghq.com/logs/)
- [Collect your processes](https://docs.datadoghq.com/infrastructure/process/)
- [Collect your traces](https://docs.datadoghq.com/tracing/)
- [Find out more about the Agent's architecture](https://docs.datadoghq.com/agent/architecture/#agent-architecture)
- [Configure inbound ports](https://docs.datadoghq.com/agent/configuration/network#configure-ports)
