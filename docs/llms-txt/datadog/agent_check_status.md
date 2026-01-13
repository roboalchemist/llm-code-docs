# Source: https://docs.datadoghq.com/agent/troubleshooting/agent_check_status.md

---
title: Troubleshoot an Agent Check
description: >-
  Learn how to test and troubleshoot Datadog Agent checks using commands and
  systemd tools to diagnose integration issues.
breadcrumbs: Docs > Agent > Agent Troubleshooting > Troubleshoot an Agent Check
source_url: https://docs.datadoghq.com/troubleshooting/agent_check_status/index.html
---

# Troubleshoot an Agent Check

If you are experiencing issues with an Agent Check, use these commands to get more troubleshooting information.

**Note**: Replace `<CHECK_NAME>` in the examples below with any Agent check. For example: `activemq`, `ceph`, or `elastic`. Review an [integration's documentation](https://docs.datadoghq.com/integrations/) to confirm the Agent check name.

**Note**: To temporarily disable a service check while troubleshooting, rename `/conf.d/<CHECK_NAME>.d/conf.yaml` to something other than the `.yaml` or `.yml` file extension, such as `conf.yaml.disable`.

## Linux{% #linux %}

To test an Agent check, run:

```shell
sudo -u dd-agent datadog-agent check <CHECK_NAME>
```

If you want to include rate metrics, add `--check-rate` to your command, for instance for Agent v6.x run:

```shell
sudo -u dd-agent datadog-agent check <CHECK_NAME> --check-rate
```

If your issue continues, [reach out to the Datadog support team](https://docs.datadoghq.com/help) with a [flare](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/).

## Windows{% #windows %}

Run the following script from an **elevated** (run as admin) PowerShell command line, with the proper `<CHECK_NAME>`:

For Agent versions >= 6.12:

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" check <CHECK_NAME>
```

For Agent versions <= 6.11:

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\embedded\agent.exe" check <CHECK_NAME>
```

## Systemd{% #systemd %}

For systems using `systemd`, use `journalctl` to assist with debugging.

The following command shows the status of the Datadog Agent.

```shell
sudo systemctl status datadog-agent
```

If the Agent failed to start, and no further information is provided, use the following command to display all logs for the Datadog Agent service. If needed, use `-r` to print logs in reverse order.

```shell
sudo journalctl -u datadog-agent.service
```

## Further Reading{% #further-reading %}

- [Agent Debug Mode](https://docs.datadoghq.com/agent/troubleshooting/debug_mode/)
- [Send an Agent Flare](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/)
