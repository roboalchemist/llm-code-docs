# Source: https://docs.datadoghq.com/agent/troubleshooting/send_a_flare.md

---
title: Agent Flare
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Agent > Agent Troubleshooting > Agent Flare
source_url: https://docs.datadoghq.com/troubleshooting/send_a_flare/index.html
---

# Agent Flare

A flare allows you to send necessary troubleshooting information to the Datadog support team.

This page covers:

- Sending a flare using the `flare` command.
- Sending a flare from the Datadog site using Remote Configuration.
- Manual submission.

A flare gathers all of the Agent's configuration files and logs into an archive file. It removes sensitive information, including passwords, API keys, Proxy credentials, and SNMP community strings. If APM is enabled, the flare includes [tracer debug logs](https://docs.datadoghq.com/tracing/troubleshooting/tracer_debug_logs/?code-lang=dotnet#data-collected) when available.

The Datadog Agent is completely open source, which allows you to [verify the code's behavior](https://github.com/DataDog/datadog-agent/tree/main/pkg/flare). If needed, the flare can be reviewed prior to sending since the flare prompts a confirmation before uploading it.

When contacting Datadog Support with Remote Configuration enabled for an Agent, the Support team may initiate a flare from your environment in order to better assist you in a timely manner. Flares provide troubleshooting information to Datadog Support to help you resolve your issue.

## Send a flare from the Datadog site{% #send-a-flare-from-the-datadog-site %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
Sending an Agent Flare from Fleet Automation is not supported for this site.
{% /alert %}

{% /callout %}

To send a flare from the Datadog site, make sure you've enabled [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/) and [Remote configuration](https://docs.datadoghq.com/agent/guide/setup_remote_config) on the Agent.

To send a remote flare:

1. From the [Fleet Automation](https://app.datadoghq.com/fleet) page, select an Agent that requires support.
1. Click **Support**.
1. Click **Send Support Ticket**.
1. Provide an existing Zendesk support ticket number. If you don't provide a ticket number, one is created on your behalf.
1. Enable **Debug mode** to allow Datadog support staff to troubleshoot your issue faster. The log level is reset to its previous configuration after you send the flare.
1. If you are troubleshooting your application, enable application tracer level logs to be included in the flare.
1. Click **Send Ticket**.

{% image
   source="https://datadog-docs.imgix.net/images/agent/fleet_automation/fleet_automation_remote_flare.eddc4a71c702b7900e16f7116bee56e5.png?auto=format"
   alt="The Send Ticket button launches a form to send a flare for an existing or new support ticket" /%}

## Send a flare using the `flare` command{% #send-a-flare-using-the-flare-command %}

Use the `flare` subcommand to send a flare. In the commands below, replace `<CASE_ID>` with your Datadog support case ID if you have one, then enter the email address associated with it.

If you don't have a case ID, enter your email address used to log in to Datadog to create a new support case.

**Confirm the upload of the archive to immediately send it to Datadog support**.

{% tab title="Agent" %}

| Platform   | Command                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------- |
| AIX        | `datadog-agent flare <CASE_ID>`                                                                                           |
| Docker     | `docker exec -it dd-agent agent flare <CASE_ID>`                                                                          |
| macOS      | `datadog-agent flare <CASE_ID>` or via the [web GUI](https://docs.datadoghq.com/agent/basic_agent_usage/#gui)             |
| CentOS     | `sudo datadog-agent flare <CASE_ID>`                                                                                      |
| Debian     | `sudo datadog-agent flare <CASE_ID>`                                                                                      |
| Kubernetes | `kubectl exec -it <AGENT_POD_NAME> -- agent flare <CASE_ID>`                                                              |
| Fedora     | `sudo datadog-agent flare <CASE_ID>`                                                                                      |
| Redhat     | `sudo datadog-agent flare <CASE_ID>`                                                                                      |
| Suse       | `sudo datadog-agent flare <CASE_ID>`                                                                                      |
| Source     | `sudo datadog-agent flare <CASE_ID>`                                                                                      |
| Windows    | `& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" flare <CASE_ID>`                                               |
| Heroku     | Consult the dedicated [Heroku documentation](https://docs.datadoghq.com/agent/guide/heroku-troubleshooting/#send-a-flare) |
| PCF        | `sudo /var/vcap/jobs/dd-agent/packages/dd-agent/bin/agent/agent flare <CASE_ID>`                                          |

## Dedicated containers{% #dedicated-containers %}

When using Agent v7.19+ and using the Datadog Helm Chart with the [latest version](https://github.com/DataDog/helm-charts/blob/master/charts/datadog/CHANGELOG.md) or a DaemonSet where the Datadog Agent and Trace Agent are in separate containers, you deploy an Agent Pod containing:

- One container with the Agent process (Agent + Log Agent)
- One container with the process-agent process
- One container with the trace-agent process
- One container with the system-probe process

To get a flare from each container, run the following commands:

### Agent{% #agent %}

```bash
kubectl exec -it <AGENT_POD_NAME> -c agent -- agent flare <CASE_ID>
```

### Process Agent{% #process-agent %}

```bash
kubectl exec -it <AGENT_POD_NAME> -c process-agent -- agent flare <CASE_ID> --local
```

### Trace Agent{% #trace-agent %}

```bash
kubectl exec -it <AGENT_POD_NAME> -c trace-agent -- agent flare <CASE_ID> --local
```

### Security Agent{% #security-agent %}

```bash
kubectl exec -it <AGENT_POD_NAME> -c security-agent -- security-agent flare <CASE_ID>
```

### System probe{% #system-probe %}

The system-probe container cannot send a flare so get container logs instead:

```bash
kubectl logs <AGENT_POD_NAME> -c system-probe > system-probe.log
```

## ECS Fargate{% #ecs-fargate %}

When using ECS Fargate platform v1.4.0, ECS tasks and services can be configured to allow access to running Linux containers by enabling [Amazon ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html). After enabling Amazon ECS exec, run the following command to send a flare:

```bash
aws ecs execute-command --cluster <CLUSTER_NAME> \
    --task <TASK_ID> \
    --container datadog-agent \
    --interactive \
    --command "agent flare <CASE_ID>"
```

**Note:** ECS Exec can only be enabled for new tasks. You must recreate existing tasks to use ECS Exec.
{% /tab %}

{% tab title="Cluster Agent" %}

| Platform      | Command                                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes    | `kubectl exec -n <NAMESPACE> -it <CLUSTER_POD_NAME> -- datadog-cluster-agent flare <CASE_ID>`                                                |
| Cloud Foundry | `/var/vcap/packages/datadog-cluster-agent/datadog-cluster-agent-cloudfoundry flare -c /var/vcap/jobs/datadog-cluster-agent/config <CASE_ID>` |

{% /tab %}

## Manual submission{% #manual-submission %}

The Agent flare protocol collects configurations and logs into an archive file first located in the local `/tmp` directory. Manually obtain this file and provide it to support if there are any issues with Agent connectivity.

### Kubernetes{% #kubernetes %}

To obtain the archive file in Kubernetes, use the kubectl command:

```
kubectl cp datadog-<pod-name>:tmp/datadog-agent-<date-of-the-flare>.zip flare.zip -c agent
```

## Further Reading{% #further-reading %}

- [Agent Debug Mode](https://docs.datadoghq.com/agent/troubleshooting/debug_mode/)
- [Get the Status of an Agent Check](https://docs.datadoghq.com/agent/troubleshooting/agent_check_status/)
