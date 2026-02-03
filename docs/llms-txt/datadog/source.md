# Source: https://docs.datadoghq.com/agent/supported_platforms/source.md

---
title: Source Installation
description: >-
  Learn how to install, configure, and manage the Datadog Agent when building
  from source code.
breadcrumbs: Docs > Agent > Supported Platforms > Source Installation
---

# Source Installation

## Overview{% #overview %}

This page outlines the basic features of the Datadog Agent. If you haven't installed the Agent yet, instructions can be found [in the Datadog Agent Integration page](https://app.datadoghq.com/account/settings/agent/latest?platform=source).

By default, your Agent is installed in its own sandbox at `~/.datadog-agent`. You're free to move this folder anywhere. However, this article assumes that the Agent is installed in its default location, so be sure to modify the instructions accordingly if you decide to move them.

## Commands{% #commands %}

Datadog Agent has some commands and only the *lifecycle commands*, such as `start`/`stop`/`restart`/`status`, should be run with `sudo`.

| Description                  | Command                        |
| ---------------------------- | ------------------------------ |
| Start Agent                  | `sudo ./bin/agent/agent start` |
| Stop Agent                   | `sudo ./bin/agent/agent stop`  |
| Status page of running Agent | `sudo ./bin/agent/agent info`  |
| Send flare                   | `sudo ./bin/agent/agent flare` |
| Display command usage        | `sudo ./bin/agent/agent help`  |

## Configuration{% #configuration %}

The configuration files and folders for the Agent are located in:

- `/etc/datadog-agent/datadog.yaml`

Configuration files for [Integrations](https://docs.datadoghq.com/integrations/):

- `/etc/datadog-agent/conf.d/`

## Troubleshooting{% #troubleshooting %}

See the [Agent Troubleshooting documentation](https://docs.datadoghq.com/agent/troubleshooting/).

## Further Reading{% #further-reading %}

- [Collect your logs](https://docs.datadoghq.com/logs/)
- [Collect your processes](https://docs.datadoghq.com/infrastructure/process/)
- [Collect your traces](https://docs.datadoghq.com/tracing/)
- [Find out more about the Agent's architecture](https://docs.datadoghq.com/agent/architecture/#agent-architecture)
- [Configure inbound ports](https://docs.datadoghq.com/agent/configuration/network#configure-ports)
