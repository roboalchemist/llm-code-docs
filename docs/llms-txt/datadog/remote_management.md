# Source: https://docs.datadoghq.com/agent/fleet_automation/remote_management.md

---
title: Remote Agent Management
description: Remotely upgrade and configure your Agents
breadcrumbs: Docs > Agent > Fleet Automation > Remote Agent Management
source_url: https://docs.datadoghq.com/fleet_automation/remote_management/index.html
---

# Remote Agent Management

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Remote Agent management with Fleet Automation simplifies how you deploy and upgrade your Datadog Agents. Instead of relying on external deployment or configuration tools, you can perform these actions directly from the Datadog platform. With Fleet Automation, you can:

1. Upgrade your Agent
1. Configure your Agent

## Getting started{% #getting-started %}

### Prerequisites{% #prerequisites %}

1. Verify that [Remote Configuration](https://docs.datadoghq.com/agent/guide/setup_remote_config) is enabled for your organization.
1. Confirm that your Agent version is 7.73 or later.

### Supported platforms{% #supported-platforms %}

- Linux VMs installed using the install script or Ansible Datadog Role
- Windows VMs

{% alert level="info" %}
Remotely upgrading Agents in containerized environments is not supported.
{% /alert %}

### Permissions{% #permissions %}

Users must have the [Agent Upgrade](https://docs.datadoghq.com/agent/fleet_automation/#control-access-to-fleet-automation) permission within Fleet Automation for upgrades. They must also have the [Agent Configuration Management](https://docs.datadoghq.com/agent/fleet_automation/#control-access-to-fleet-automation) permission to configure Agents remotely. These permissions are enabled by default on the Datadog Admin role.

## Upgrade Agents{% #upgrade-agents %}

### Disk space requirement{% #disk-space-requirement %}

Datadog suggests at least 2GB for the initial Agent install and an additional 2GB to use Fleet Automation to upgrade the Agent. Specifically, the upgrade requires 1.3GB in the `/opt/datadog-packages` directory on Linux, or `C:\ProgramData\Datadog\Installer\packages` on Windows. The extra space ensures that there is enough room to maintain two Agent installs temporarily during the upgrade process in case a rollback is needed.

### Upgrade steps{% #upgrade-steps %}

{% collapsible-section #id-for-anchoring %}
#### How to upgrade Agents remotely

1. From the **[Upgrade Agents](https://app.datadoghq.com/fleet/agent-upgrades)** tab, click **Upgrade Now**.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/upgrade-screen2.6ae4c20285dcf62bf47d7aa48d5990fc.png?auto=format"
      alt="UI showing the Upgrade Agents tab with the âUpgrade Nowâ button." /%}

1. **Select the Agents you want to upgrade**. You can target a group of Agents by filtering on host information or tags.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/start-agent-upgrade.951ffb8a482f1d30b6bca14665599896.png?auto=format"
      alt="Agent selection screen with filtering options to narrow the list of Agents to upgrade." /%}

1. **Review the deployment plan** and click **Upgrade Agents** to start the upgrade.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/agent-upgrades-staged.6c0e26083bd11aaf370603e9e5954afc.png?auto=format"
      alt="Deployment plan view showing the list of Agents staged for upgrade." /%}

1. **Use the [Deployments](https://app.datadoghq.com/fleet/deployments) dashboard** to track the upgrade process. Clicking on an Agent in the deployments table gives you more information about the upgrade, including the duration time, progress, and the user who started the upgrade.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/deployments.09f83298855bfed95752a07b4a0b8fa9.png?auto=format"
      alt="Deployments dashboard showing upgrade progress and details for each Agent." /%}

{% /collapsible-section %}

{% collapsible-section #id-for-anchoring %}
#### How to schedule Agent upgrades

1. From the [**Upgrade Agents** tab](https://app.datadoghq.com/fleet/agent-upgrades), click **+ Create Schedule**.

1. On the Upgrade Schedule page, add a **Schedule name**.

1. **Select the Agent version**. You have the option to upgrade the Agents to the latest version, to one version behind, or to two versions behind.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/agent_upgrade_select_version1.fd30cc8d8c0eab3112cec7481f09cc97.png?auto=format"
      alt="See a list of scheduled Agent upgrades." /%}

1. **Specify the Agents to be upgraded**. You can target a group of Agents by filtering on host information or tags.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/agent_upgrade_select_agents.3367dde143dbaaebff71f319ec945554.png?auto=format"
      alt="See a list of Agents to be upgraded." /%}

1. **Set the deployment window** for these upgrades. You can select the days, time frame, and timezone for the upgrade.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/agent_upgrade_set_window.78091ae7b77f6fc121a320d4332295fd.png?auto=format"
      alt="Select the time frame for your Agent upgrades." /%}

1. **Set up notifications** to receive updates on the status of the deployment. You can notify your team of the deployment status through the services you've already connected with Datadog, like Slack, Teams, or PagerDuty.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/agent_upgrade_set_notification.1bc802f564519756331c4a0540bbd0e1.png?auto=format"
      alt="Select people or channels to be notified about the progress of the upgrade." /%}

1. Click **Create Schedule** to save the schedule.

1. See a list of your scheduled upgrades under the [**Upgrade Agents** tab](https://app.datadoghq.com/fleet/agent-upgrades), in the **Upgrade Schedules** section.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/agent_upgrade_schedule_list3.09883c2cadcc374a42bc3cc25199e210.png?auto=format"
      alt="See a list of upgrades scheduled for your Agents." /%}

{% /collapsible-section %}

{% collapsible-section %}
#### Upgrade Agents using the API

Fleet Automation provides an API to trigger Agent upgrades programmatically or on a recurring schedule. Start upgrades for any set of hosts using filter queries, or create schedules that run during defined maintenance windows with a specified Agent version. For full details, see the [Fleet Automation API](https://docs.datadoghq.com/api/latest/fleet-automation/).
{% /collapsible-section %}

### Upgrade process{% #upgrade-process %}

Similar to a manual upgrade, expect a downtime of 5-30 seconds while the Agent restarts. The full upgrade process takes approximately 5 minutes. Around 2 minutes of this time is used for the upgrade process. The rest of the time is spent monitoring the upgrade to ensure stability and determining if a rollback is necessary. If the upgrade fails and a rollback is necessary, the Agent automatically reverts to the previously running Agent version.

The upgrade process primarily adds files to the following directories:

Linux:

- `/opt/datadog-packages`
- `/etc/datadog-agent`
- `/etc/systemd/system`

Windows:

- `C:\ProgramData\Datadog\Installer\packages`
- `C:\Program Files\Datadog\Datadog Agent`

The Agent ensures that the appropriate permissions are set for these files. No configuration files are altered during the installation process.

### Upgrade precedence{% #upgrade-precedence %}

For the most consistent upgrade experience, Datadog recommends managing upgrades from one source at a time. Use either Fleet Automation or a configuration management tool. If you run a configuration management tool on an Agent that has already been upgraded using Fleet Automation, the upgrade reverts the Agent to the [`DD_AGENT_MINOR_VERSION`](https://github.com/DataDog/agent-linux-install-script?tab=readme-ov-file#install-script-configuration-options) specified in your configuration. If no `DD_AGENT_MINOR_VERSION` is set, the Agent is upgraded to the latest available version.

## Configure Datadog Agents{% #configure-datadog-agents %}

Fleet Automation allows you to roll out and manage Datadog Agent configuration at scale. Configuration changes can be applied using guided workflows in the UI or by providing custom YAML files. Fleet Automation allows you to standardize Agent configuration across environments. With Fleet Automation, you can:

- Set up Datadog product telemetry such as APM, Logs, and NDM
- Enable or adjust Agent integrations
- Manage Agent tags
- Apply consistent configuration across environments

{% collapsible-section #id-for-anchoring %}
#### Configure multiple Agents

1. In Fleet Automation, open the [Configure Agents](https://app.datadoghq.com/fleet/agent-management) tab and click **Create Configuration**.

1. **Select and configure** the products (for example, APM, Logs, or NDM) that you want the target Agents to run.

   {% image
      source="https://datadog-docs.imgix.net/images/agent/fleet_automation/fa_create_agent_configuration2.fe42b34c65b9136089f7fb6b9bbf250e.png?auto=format"
      alt="Select which product to enable." /%}

1. **Review** your final configuration and begin scoping deployment to your Agents. Alternatively, you can save the configuration to edit or deploy to your Agents at a later time from the Configure Agents page.

1. **Scope Agents** to deploy configuration to (for example, through tags such as host names, site, or environment).

1. **Review the deployment plan** to confirm scoped Agents and deployment settings, such as rollout concurrency.

1. **Start deployment** and track progress from the Deployments page.

{% /collapsible-section %}

{% collapsible-section #id-for-anchoring %}
#### Edit configuration of a single Agent

1. In the Datadog UI, navigate to the [Fleet Automation](https://app.datadoghq.com/fleet) page and select **View Agents**.

1. (**Optional**) You can target a group of Agents by filtering on host information or tags.

1. **Select your host** to open a side panel. In the side panel, click on the **Configuration** tab to access your modifiable configurations.

1. Click the **Edit** button to edit your configuration.

1. **Submit** these changes by selecting **Deploy Changes**.

**Note**: Some configuration fields ( for example, `api_key`, `site`, and `notable_events`) cannot be modified.

In the following example, the `logs_enabled` field is changed from `false` to `true`. After the changes are deployed, log collection on this Agent is enabled.

{% image
   source="https://datadog-docs.imgix.net/images/agent/fleet_automation/agent_remote_management_single_agent_config2.a5ae38b1cf5ddc54eb4b1e5cffbc6511.png?auto=format"
   alt="Edit and deploy Agent configuration changes." /%}

{% /collapsible-section %}

{% collapsible-section %}
#### Configure Agents using the API

Fleet Automation provides an API to apply configuration updates to your Agents programmatically. Deploy changes to any group of hosts using filter queries, supplying either full configuration files or targeted patches. Fleet Automation does not support all Agent configuration fields, and settings related to Agent connection or secrets (site, API keys, and other authentication parameters) cannot be managed through the API. Push configuration on demand or integrate it into your existing automation workflows. For full details, see the [Fleet Automation API](https://docs.datadoghq.com/api/latest/fleet-automation/).
{% /collapsible-section %}

### Configuration precedence{% #configuration-precedence %}

Configuration changes deployed through Fleet Automation are appended to the Datadog Agent's local configuration. If a conflict occurs at the configuration-field level, Fleet Automation overrides the local value. In short, the most recent configuration change, whether applied by Fleet Automation, configuration management tools, or directly on the host, becomes the Agent's active configuration.

You can use [Fleet Automation Audit Trail](https://app.datadoghq.com/fleet) to gain visibility into recent configuration changes to your Agents and to set up alerts on those changes.

### Mirrors and proxies{% #mirrors-and-proxies %}

You can use Remote Agent Management along with a proxy or mirrored repositories.

For instructions on configuring your Agent to use a proxy, see [Agent Proxy Configuration](https://docs.datadoghq.com/agent/configuration/proxy/). After you've configured the proxy, restart the Agent to apply the settings.

For instructions on using mirrored or air-gapped repositories, see:

- [Synchronize Datadog's images with a private container registry](https://docs.datadoghq.com/containers/guide/sync_container_images/)
- [Installing the Agent on a server with limited internet connectivity](https://docs.datadoghq.com/agent/guide/installing-the-agent-on-a-server-with-limited-internet-connectivity/)

## Troubleshooting{% #troubleshooting %}

### Datadog Installer incompatible with Agent (pre-7.66){% #datadog-installer-incompatible-with-agent-pre-766 %}

If you were a Preview customer and set up remote Agent Management before Agent version 7.66, your Datadog Installer might be incompatible with the Agent.

To support general availability of remote Agent upgrades, the installer component was bundled with the Agent starting in version 7.66. This change ensures that both components stay up to date together, preventing version mismatches and related compatibility issues. Earlier versions of the Agent did not bundle these components, resulting in a possible version mismatch that could prevent automatic updates and remote Agent Management functionality.

To diagnose and fix the issue:

1. Use the following [query in Fleet Automation](https://app.datadoghq.com/fleet?query=support_remote_upgrade%3Adatadog-installer) to identify affected hosts:
   ```txt
   support_remote_upgrade:datadog-installer
   ```
1. If your setup is impacted, [re-run the install script](https://app.datadoghq.com/fleet/install-agent/latest?platform=overview) on each affected Agent to manually upgrade them to Agent version 7.66 or higher. This ensures full compatibility with Remote Agent Management features.

Manual Agent upgrades are not required after you've updated to 7.66 or higher. Future upgrades are handled automatically without requiring manual intervention.

If you don't upgrade an earlier Agent version to 7.66 or higher, there is no impact on your existing Agent. However, remote upgrades remain unavailable until you update the Agent.

## Further reading{% #further-reading %}

- [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Remote Configuration](https://docs.datadoghq.com/remote_configuration)
