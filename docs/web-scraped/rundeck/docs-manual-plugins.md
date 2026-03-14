# Source: https://docs.rundeck.com/docs/manual/plugins/

Title: Plugins

URL Source: https://docs.rundeck.com/docs/manual/plugins/

Markdown Content:
1.   [Rundeck | Runbook Automation Documentation](https://docs.rundeck.com/docs/)
2.   [User Guide Overview](https://docs.rundeck.com/docs/manual/)
3.   [Plugins](https://docs.rundeck.com/docs/manual/plugins/)

[Plugins](https://docs.rundeck.com/docs/manual/plugins/#plugins)
----------------------------------------------------------------

[Overview](https://docs.rundeck.com/docs/manual/plugins/#overview)
------------------------------------------------------------------

Runbook Automation is a sophisticated orchestration platform with numerous types of integrations called _plugins_.

The functionality of plugins ranges from executing commands on nodes, performing steps in a workflow, sending notifications about job status, gathering information about the hosts on a network, copying a file to a remote server, storing and streaming logs, and much more.

This section is a guide for the basic configuration of plugins. For a detailed list of the various types of plugins, click [here](https://docs.rundeck.com/docs/administration/configuration/plugins/plugin-types.html#types-of-plugins).

For administrators and advanced-users, here is additional documentation on Installing Plugins and [advanced configuration settings](https://docs.rundeck.com/docs/administration/configuration/plugins/configuring.html).

For developers interested in developing new plugins or contributing to open-source plugins, click [here](https://docs.rundeck.com/developer/).

[Plugins Configuration](https://docs.rundeck.com/docs/manual/plugins/#plugins-configuration)
--------------------------------------------------------------------------------------------

All plugins are configured by defining plugin properties - such as credentials and endpoints. These properties can be defined on a per-plugin, project, or system basis.

Plugin properties are prioritized for usage in the following order:

1.   **Individual Plugin**
2.   **Project**
3.   **System**

For example, if credentials for integrating with Jira are defined both in the _**Project**_ configuration _and_ in a specific Jira Job Step plugin, then the credentials defined in the Job Step will be used.

A plugin _suite_ is a group of plugins that share a set of the same properties. Most often, this is a group of plugins that are built to integrate with the same third-party product - such as the [PagerDuty Plugins](https://docs.rundeck.com/docs/manual/jobs/job-plugins/workflow-steps/pagerduty.html).

### [Project Level Plugin Configuration](https://docs.rundeck.com/docs/manual/plugins/#project-level-plugin-configuration)

To configure a plugin-suite for a project, navigate to **Project Settings** ->**Edit Configuration** ->**Plugins**:

![Image 1: Plugin Suite Project Settings](https://docs.rundeck.com/docs/assets/img/plugin-groups-project-settings.png)

Click on **PluginGroup+** and select the desired Plugin Suite from the list.

The properties for the chosen plugin-suite will now be available to configure. Once the properties are filled in, click **Save** for that plugin-suite. Then click **Save** at the bottom of the page:

![Image 2: Saving pluing suite settings](https://docs.rundeck.com/docs/assets/img/saving-plugin-suite-settings.png)

When the configuration is saved, all plugins for the given suite in that project will default to these properties.

### [System Level Plugin Configuration](https://docs.rundeck.com/docs/manual/plugins/#system-level-plugin-configuration)

To configure a plugin-suite for the system - thereby spanning all projects - click on the **Gear Icon** (upper right) ->**System Configuration**.

Navigate to the plugin-suite name - such as PagerDuty - and click the **Pencil Icon** in the upper right:

![Image 3: Edit Plugin Suite Sysytem Level](https://docs.rundeck.com/docs/assets/img/edit-plugin-suite-system-level.png)

Place the properties into their associated fields and then click **Save**.

When the configuration is saved, all plugins for the specified suite across all projects will default to the defined properties.
