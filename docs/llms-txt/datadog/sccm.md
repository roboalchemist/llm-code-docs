# Source: https://docs.datadoghq.com/agent/supported_platforms/sccm.md

---
title: SCCM
description: SCCM (Systems Center Configuration Manager)
breadcrumbs: Docs > Agent > Supported Platforms > SCCM
source_url: https://docs.datadoghq.com/supported_platforms/sccm/index.html
---

# SCCM

Microsoft SCCM (Systems Center Configuration Manager) is a configuration management solution that comes packaged with Microsoft's Systems Center suite of tools. This page covers installing and configuring the Datadog Agent using SCCM.

## Prerequisites{% #prerequisites %}

- The Agent supports SCCM version 2103 or greater.
- Before you install the Agent, make sure you've installed and configured [Distribution Points](https://learn.microsoft.com/en-us/mem/configmgr/core/servers/deploy/configure/manage-content-and-content-infrastructure) in Configuration Manager.

## Setup{% #setup %}

### Create a deployable Datadog Agent application{% #create-a-deployable-datadog-agent-application %}

1. Download the latest Windows Datadog Agent installer file (MSI) to the SCCM server from the [Agent page](https://app.datadoghq.com/account/settings/agent/latest?platform=windows).

1. In SCCM, create an application and use the location of the Datadog Agent MSI.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/basic_agent_usage/sccm/sccm-deployable-app.b9ad9c852927714ffba94d9233ef8bd4.png?auto=format"
      alt="Create a new application and use the Datadog Agent MSI as the target MSI." /%}



1. Click **Next** until you get to the **General Information** page.

1. Under **Installation program**, paste the following command, replacing `MY_API_KEY` with your API key:

   ```powershell
   start /wait msiexec /qn /i datadog-agent-7-latest.amd64.msi APIKEY="MY_API_KEY" SITE="datadoghq.com"
   ```

For more installation options, see full list of [installation variables](https://docs.datadoghq.com/agent/basic_agent_usage/windows/?tab=commandline#configuration).

1. Ensure that **Install behavior** is set to **Install for system**.

1. Click **Next** and follow the prompts to create the application.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/basic_agent_usage/sccm/sccm-install-command.02f0e493e9731cd29cd3c8cdae689dad.png?auto=format"
      alt="Enter an installation program command and ensure that the install behavior is set to install for system." /%}



1. To verify the application has been created, look for it in **Software Library** > **Overview** > **Application Management** > **Applications**.

### Deploy the Datadog Agent application{% #deploy-the-datadog-agent-application %}

{% alert level="danger" %}
Before deploying the Datadog Agent application, make sure you've installed and configured [Distribution Points](https://learn.microsoft.com/en-us/mem/configmgr/core/servers/deploy/configure/install-and-configure-distribution-points) in Configuration Manager
{% /alert %}

1. Go to **Software Library** > **Overview** > **Application Management** > **Applications** and select the Datadog Agent application you created earlier.
1. From the **Home** tab in the **Deployment** group, select **Deploy**.

### Agent configuration{% #agent-configuration %}

SCCM packages allow you to deploy configuration files to your Datadog Agents, overwriting their default settings. An Agent configuration consists of a `datadog.yaml` configuration file and optional `conf.yaml` files for each integration. You must create a package for each configuration file you want to deploy.

1. Collect your `datadog.yaml` and `conf.yaml` files in a local SCCM machine folder. See the [sample `config_template.yaml` file](https://github.com/DataDog/datadog-agent/blob/master/pkg/config/config_template.yaml) for all available configuration options.
1. Create an SCCM Package and select **Standard program**.
1. Select the location that contains the configuration file that you want to deploy to your Agents.
1. Select a [Device collection](https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/collections/create-collections#bkmk_create) to deploy the changes to.
1. Configure deployment settings to pre-install the package on the targets immediately.

{% image
   source="https://datadog-docs.imgix.net/images/agent/basic_agent_usage/sccm/sccm-select-program.2356dadd7f759999c88db02ef4e25a68.png?auto=format"
   alt="The program type screen. Select standard program" /%}

### Restart the Datadog Agent{% #restart-the-datadog-agent %}

Restart the Agent service to observe your configuration changes:

1. Create a PowerShell script to restart the Datadog Agent using [Agent commands](https://docs.datadoghq.com/agent/basic_agent_usage/windows/#agent-commands).
1. Run the script to restart the Datadog Agent.
1. Check for new data in the Datadog UI.

## Further reading{% #further-reading %}

- [Collect your logs](https://docs.datadoghq.com/logs/)
- [Collect your processes](https://docs.datadoghq.com/infrastructure/process/)
- [Collect your traces](https://docs.datadoghq.com/tracing/)
- [Find out more about the Agent's architecture](https://docs.datadoghq.com/agent/architecture)
- [Configure inbound ports](https://docs.datadoghq.com/agent/configuration/network#configure-ports)
