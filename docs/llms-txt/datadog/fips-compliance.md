# Source: https://docs.datadoghq.com/agent/configuration/fips-compliance.md

---
title: Datadog FIPS Compliance
description: >-
  Configure FIPS-compliant cryptographic modules for the Datadog Agent in highly
  regulated environments like FedRAMP.
breadcrumbs: Docs > Agent > Agent Configuration > Datadog FIPS Compliance
---

# Datadog FIPS Compliance

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com, us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

The FIPS Agent is a flavor of the Datadog Agent that natively supports Federal Information Processing Standards (FIPS) compliance. The FIPS Agent's compliance is based on its use of the FIPS 140-2 validated [Cryptographic Module - Certificate #4282](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282). See the related [security policy](https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp4282.pdf) for information about validated operating environments and restrictions.

The FIPS Agent also includes [limited support for integrations](https://docs.datadoghq.com/integrations/guide/fips-integrations) that need to collect observability data that is external to the host.

**It is your responsibility to ensure operating environment compliance with the security policy and wider FIPS guidance.**

## Supported platforms and limitations{% #supported-platforms-and-limitations %}

Supported platforms:

|  |
|  |
| Bare metal and VMs  | RHEL >= 7Debian >= 8Ubuntu >= 14.04SUSE >= 12Windows Server >= 2016Windows >= 10 |
| Cloud and container | Amazon ECSAWS EKS (Helm)Docker                                                   |

Supported products (Agent 7.65.0 and above):

- Metrics
- Logs
- APM traces
- APM profiles
- Processes
- Orchestrator Explorer
- Runtime Security
- Serverless Monitoring

The Datadog FIPS Agent does **not** support the following:

- Communication between Cluster Agent and Node Agents
- Outbound communication to anything other than GovCloud
- Datadog [DDOT Collector](https://docs.datadoghq.com/opentelemetry/setup/ddot_collector)

## Compliance guidelines{% #compliance-guidelines %}

{% alert level="danger" %}
This is not an exhaustive list. These requirements are a baseline only. You are responsible for evaluating your environment and implementing any additional controls needed to achieve full FIPS compliance.
{% /alert %}
The following baseline controls apply to each platform. Your system may require additional controls:
{% tab title="Linux" %}

- A non-containerized Linux host.
- Your Linux OS must be in FIPS-compliant mode. See your OS vendor's documentation on what steps are required to meet this requirement.
- FIPS-compliant storage backing the host file system.

{% /tab %}

{% tab title="Windows" %}

- A non-containerized Windows host.
- Windows must be in [FIPS-compliant mode](https://learn.microsoft.com/en-us/windows/security/security-foundations/certification/fips-140-validation).
- FIPS-compliant storage backing the host file system.

{% /tab %}

{% tab title="AWS Lambda" %}

- Use a FIPS-compliant region (for example, AWS GovCloud)

{% /tab %}

{% tab title="AWS ECS" %}

- Use a FIPS-compliant region (for example, AWS GovCloud)
- Configure AWS compute services (EC2 or Fargate) in FIPS mode
- Use FIPS-compliant storage for your ECS tasks

{% /tab %}

{% tab title="AWS EKS" %}

- Use a FIPS-compliant region (for example, AWS GovCloud)
- Configure EKS worker nodes in FIPS mode
- Use FIPS-compliant storage for your EKS worker nodes

{% /tab %}

In addition to the Operating System (OS) requirements above:

- You must have access to a FIPS-compliant Datadog environment (US1-FED).
- The Agent version must be 7.65.0 and above to access the FIPS Agent

## Installation{% #installation %}

{% tab title="Linux" %}

1. Install the Agent with FIPS support.

**Note:** FIPS support is only available on Agent versions 7.65.0 and above:

   1. If you're using the Agent install script, specify the `DD_AGENT_FLAVOR="datadog-fips-agent"` environment variable in your installation command. For example:

      ```sh
      DD_SITE="ddog-gov.com" DD_API_KEY="MY_API_KEY" DD_AGENT_FLAVOR="datadog-fips-agent" â¦ bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"
      ```

   1. If you're installing with a package, [follow the instructions](https://docs.datadoghq.com/agent/guide/installing-the-agent-on-a-server-with-limited-internet-connectivity/) to install the latest `datadog-fips-agent` package available for your platform.

   1. Add `GOFIPS=1` to your Datadog environment variables, reload all service units, and restart the Datadog Agent service (`datadog-agent.service`). For example, if your host is using systemd:

      ```sh
      echo "GOFIPS=1" | sudo tee -a /etc/datadog-agent/environment
      systemctl daemon-reload
      systemctl restart 'datadog-agent*'
      ```

1. Run the `datadog-agent status` command and make sure you see `FIPS Mode: enabled` in the status output.

{% image
   source="https://datadog-docs.imgix.net/images/agent/fips-linux.9b9ee1a25073301cb634384630327924.png?auto=format"
   alt="Agent status command output with FIPS Mode enabled - Linux" /%}

{% /tab %}

{% tab title="Windows" %}

1. Follow the [Windows instructions](https://docs.datadoghq.com/agent/basic_agent_usage/windows/#uninstall-the-agent) to uninstall any existing Datadog Agent on the machine.

1. Run the command below to install the FIPS Agent, replacing `DATADOG_API_KEY` with your API key:

**Note:** FIPS support is only available on Agent versions 7.65.0 and above:

```powershell
$p = Start-Process -Wait -PassThru msiexec -ArgumentList '/qn /i https://windows-agent.datadoghq.com/datadog-fips-agent-7-latest.amd64.msi /log C:\Windows\SystemTemp\install-datadog.log APIKEY="<DATADOG_API_KEY>" SITE="ddog-gov.com"'
if ($p.ExitCode -ne 0) {
   Write-Host "msiexec failed with exit code $($p.ExitCode) please check the logs at C:\Windows\SystemTemp\install-datadog.log" -ForegroundColor Red
}
```

Run the Agent `status` command and make sure you see `FIPS Mode: enabled` in the status output.

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\bin\agent.exe" status
```

{% image
   source="https://datadog-docs.imgix.net/images/agent/fips-powershell.57cac1da498d14945679f7d38cb6aa43.png?auto=format"
   alt="Agent status command output with FIPS Mode enabled - Windows" /%}

**Note**: The program name for the FIPS Agent in **Add or Remove Programs** is "Datadog FIPS Agent."
{% /tab %}

{% tab title="AWS Lambda" %}
For AWS Lambda FIPS compliance, follow the instructions in the [AWS Lambda FIPS Compliance](https://docs.datadoghq.com/serverless/aws_lambda/fips-compliance/) documentation.
{% /tab %}

{% tab title="AWS ECS" %}
When following the [ECS installation instructions](https://docs.datadoghq.com/containers/amazon_ecs/), make sure to use these FIPS-specific configuration values for your Task Definition:

- Set `image` in the `containerDefinitions` object to `public.ecr.aws/datadog/agent:7-fips`
- Set `DD_SITE` environment variable to `ddog-gov.com`

{% /tab %}

{% tab title="AWS EKS" %}
When following the [Datadog Agent installation on Kubernetes](https://docs.datadoghq.com/containers/kubernetes/installation/) instructions, make sure to include these FIPS-specific configuration values in the `datadog-agent.yaml` file depending on your chosen installation method:

For the Datadog Operator:

```yaml
spec:
   global:
      site: "ddog-gov.com"
      useFIPSAgent: true
```

For the Datadog Helm Chart:

```yaml
datadog:
   site: "ddog-gov.com"
useFIPSAgent: true
```

{% /tab %}

## Security and hardening{% #security-and-hardening %}

You, the Datadog customer, are responsible for **host** security and hardening.

**Security considerations:**

- While the Datadog images provided are constructed with security in mind, they have not been evaluated against CIS benchmark recommendations or DISA STIG standards.
- If you rebuild, reconfigure, or modify the Datadog FIPS Agent to fit your deployment or testing needs, you might end up with a technically working setup, but Datadog cannot guarantee FIPS compliance if the Datadog FIPS Agent is not used exactly as explained in the documentation.
- If you did not follow the installation steps listed above exactly as documented, Datadog cannot guarantee FIPS compliance.
- Some Linux distros with `urllib3 â¤ 1.26.20` may fail FIPS encryption due to non-compliant libraries. Check with your Linux vendor to ensure FIPS-compliant encryption support.

## Further reading{% #further-reading %}

- [Agent Proxy Configuration](https://docs.datadoghq.com/agent/configuration/proxy)
- [Monitor highly regulated workloads with Datadog's FIPS-enabled Agent](https://www.datadoghq.com/blog/datadog-fips-enabled-agent/)
