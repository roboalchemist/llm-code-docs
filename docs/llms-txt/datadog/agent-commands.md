# Source: https://docs.datadoghq.com/agent/configuration/agent-commands.md

---
title: Agent Commands
description: >-
  Complete reference of Datadog Agent commands for starting, stopping,
  troubleshooting, and managing the Agent.
breadcrumbs: Docs > Agent > Agent Configuration > Agent Commands
---

# Agent Commands

{% alert level="danger" %}
For Linux based systems where the `service` wrapper command is not available, [consult the list of alternatives](https://docs.datadoghq.com/agent/faq/agent-v6-changes/?tab=linux#service-lifecycle-commands).
{% /alert %}

## Start, stop, and restart the Agent{% #start-stop-and-restart-the-agent %}

### Start the Agent{% #start-the-agent %}

List of commands to start the Datadog Agent:

| Platform   | Command                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------- |
| AIX        | `startsrc -s datadog-agent`                                                                         |
| Linux      | See the [Agent documentation](https://docs.datadoghq.com/agent/) for your OS.                       |
| Docker     | Use the [installation command](https://docs.datadoghq.com/agent/docker/).                           |
| Kubernetes | `kubectl create -f datadog-agent.yaml`                                                              |
| macOS      | `launchctl start com.datadoghq.agent` *or* through the systray app                                  |
| Source     | `sudo service datadog-agent start`                                                                  |
| Windows    | See the [Windows Agent documentation](https://docs.datadoghq.com/agent/basic_agent_usage/windows/). |

### Stop the Agent{% #stop-the-agent %}

List of commands to stop the Datadog Agent:

| Platform   | Command                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------- |
| AIX        | `stopsrc -s datadog-agent`                                                                          |
| Linux      | See the [Agent documentation](https://docs.datadoghq.com/agent/) for your OS.                       |
| Docker     | `docker exec -it <CONTAINER_NAME> agent stop`                                                       |
| Kubernetes | `kubectl delete pod <AGENT POD NAME>`ânote: the pod is automatically rescheduled                    |
| macOS      | `launchctl stop com.datadoghq.agent` *or* through the systray app                                   |
| Source     | `sudo service datadog-agent stop`                                                                   |
| Windows    | See the [Windows Agent documentation](https://docs.datadoghq.com/agent/basic_agent_usage/windows/). |

### Restart the Agent{% #restart-the-agent %}

List of commands to restart the Datadog Agent:

| Platform   | Command                                                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Linux      | See the [Agent documentation](https://docs.datadoghq.com/agent/) for your OS.                                                      |
| Docker     | Use the [installation command](https://docs.datadoghq.com/agent/docker/).                                                          |
| Kubernetes | `kubectl delete pod <AGENT POD NAME>`ânote: the pod is automatically rescheduled                                                   |
| macOS      | Stop and then start the Agent with:`launchctl stop com.datadoghq.agent``launchctl start com.datadoghq.agent`Or use the systray app |
| Source     | *unsupported Platform*                                                                                                             |
| Windows    | See the [Windows Agent documentation](https://docs.datadoghq.com/agent/basic_agent_usage/windows/).                                |

## Agent status and information{% #agent-status-and-information %}

### Service status{% #service-status %}

List of commands to display the status of the Datadog Agent:

| Platform                                                                           | Command                                                                                                                    |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| AIX                                                                                | `lssrc -s datadog-agent`                                                                                                   |
| Linux                                                                              | See the [Agent documentation](https://docs.datadoghq.com/agent/) for your OS.                                              |
| Docker (Debian)                                                                    | `sudo docker exec -it <CONTAINER_NAME> s6-svstat /var/run/s6/services/agent/`                                              |
| Kubernetes                                                                         | `kubectl exec -it <POD_NAME> -- s6-svstat /var/run/s6/services/agent/`                                                     |
| macOS                                                                              | `launchctl list com.datadoghq.agent` *or* through the systray app                                                          |
| Source                                                                             | `sudo service datadog-agent status`                                                                                        |
| Windows                                                                            | See the [Windows Agent documentation](https://docs.datadoghq.com/agent/basic_agent_usage/windows/#status-and-information). |
| [Cluster Agent (Kubernetes)](https://docs.datadoghq.com/containers/cluster_agent/) | `datadog-cluster-agent status`                                                                                             |

### Agent information{% #agent-information %}

List of commands to display the status of your Datadog Agent and enabled integrations.

| Platform                                                                           | Command                                                                                                                    |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| AIX                                                                                | `datadog-agent status`                                                                                                     |
| Linux                                                                              | `sudo datadog-agent status`                                                                                                |
| Docker                                                                             | `sudo docker exec -it <CONTAINER_NAME> agent status`                                                                       |
| Kubernetes                                                                         | `kubectl exec -it <POD_NAME> -- agent status`                                                                              |
| macOS                                                                              | `datadog-agent status` or through the [web GUI](https://docs.datadoghq.com/agent/basic_agent_usage/#gui)                   |
| Source                                                                             | `sudo datadog-agent status`                                                                                                |
| Windows                                                                            | See the [Windows Agent documentation](https://docs.datadoghq.com/agent/basic_agent_usage/windows/#status-and-information). |
| [Cluster Agent (Kubernetes)](https://docs.datadoghq.com/containers/cluster_agent/) | `datadog-cluster-agent status`                                                                                             |

A properly configured integration is displayed under **Running Checks** with no warnings or errors, as seen below:

```text
Running Checks
==============
  network (1.6.0)
  ---------------
    Total Runs: 5
    Metric Samples: 26, Total: 130
    Events: 0, Total: 0
    Service Checks: 0, Total: 0
    Average Execution Time : 0ms
```

## Other commands{% #other-commands %}

The Agent command-line interface is sub-command based. To see the list of available sub-commands, run:

```shell
<AGENT_BINARY> --help
```

To run a sub-command, the Agent binary must be invoked:

```shell
<AGENT_BINARY> <SUB_COMMAND> <OPTIONS>
```

Some options have flags and options detailed under `--help`. For example, use help with the `check` sub-command:

```shell
<AGENT_BINARY> check --help
```

| Subcommand        | Notes                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| `check`           | Run the specified check.                                                                                  |
| `config`          | [Runtime configuration management](https://docs.datadoghq.com/agent/troubleshooting/config/).             |
| `configcheck`     | Print all configurations loaded & resolved of a running Agent.                                            |
| `diagnose`        | Execute connectivity diagnosis on your system.                                                            |
| `flare`           | [Collect a flare and send it to Datadog](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/). |
| `health`          | Print the current Agent health.                                                                           |
| `help`            | Help about any command.                                                                                   |
| `hostname`        | Print the hostname used by the Agent.                                                                     |
| `import`          | Import and convert configuration files from previous versions of the Agent.                               |
| `jmx`             | JMX troubleshooting.                                                                                      |
| `launch-gui`      | Start the Datadog Agent GUI.                                                                              |
| `restart-service` | Restart the Agent within the service control manager. Windows only.                                       |
| `start-service`   | Start the Agent within the service control manager. Windows only.                                         |
| `stream-logs`     | Stream the logs being processed by a running agent.                                                       |
| `stopservice`     | Stop the Agent within the service control manager. Windows only.                                          |
| `version`         | Print version info.                                                                                       |

## Further Reading{% #further-reading %}

- [Agent Troubleshooting](https://docs.datadoghq.com/agent/troubleshooting/)
