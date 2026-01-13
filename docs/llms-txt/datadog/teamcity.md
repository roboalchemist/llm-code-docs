# Source: https://docs.datadoghq.com/continuous_integration/pipelines/teamcity.md

---
title: TeamCity Setup for CI Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  TeamCity Setup for CI Visibility
source_url: https://docs.datadoghq.com/pipelines/teamcity/index.html
---

# TeamCity Setup for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[TeamCity](https://www.jetbrains.com/teamcity/) is a continuous integration and delivery server that optimizes and automates software development processes.

Set up CI Visibility for TeamCity to collect data about your pipeline executions, debug performance bottlenecks, address operational issues, and optimize your development workflows.

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                              | Platform                            | Definition                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------- |
| [Partial retries](https://docs.datadoghq.com/glossary/#partial-retry)                                                                            | Retry build triggers                | View partially retried pipeline executions.                               |
| [Queue time](https://docs.datadoghq.com/glossary/#queue-time)                                                                                    | Queue time                          | View the amount of time pipeline jobs sit in the queue before processing. |
| [Pipeline failure reasons](https://docs.datadoghq.com/glossary/#pipeline-failure)                                                                | Pipeline failure reasons            | Identify pipeline failure reasons from error messages.                    |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/) | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                      |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                   | Execution time                      | View the amount of time pipelines have been running jobs.                 |

The following TeamCity versions are supported:

- TeamCity >= 2021.2 or later

### Terminology{% #terminology %}

This table shows the mapping of concepts between Datadog CI Visibility and TeamCity:

| Datadog                    | TeamCity    |
| -------------------------- | ----------- |
| Pipeline                   | Build Chain |
| Job                        | Build       |
| *Not available in Datadog* | Step        |

## Configure the Datadog integration{% #configure-the-datadog-integration %}

The integration between [TeamCity](https://www.jetbrains.com/teamcity/) and Datadog CI Visibility is provided through a TeamCity plugin. The [source code](https://github.com/DataDog/ci-teamcity-plugin) of the Datadog CI Integration plugin is open source under the Apache 2.0 license.

To set up the integration:

1. Download the [Datadog CI Integration plugin](https://plugins.jetbrains.com/plugin/20852-datadog-ci-integration) on the TeamCity server by going to **Administration** -> **Plugins** -> **Browse Plugin Repository**.

1. If you don't already have one, add a [TeamCity composite build](https://www.jetbrains.com/help/teamcity/composite-build-configuration.html) as the last build of the build chain. This build must have a dependency on the current last build of the chain and no other builds depending on it.

Build chains that do not end with a composite build are ignored by the plugin. For example, consider an expected build chain where `Aggregating Results` is the last composite build:

   {% image
      source="https://datadog-docs.imgix.net/images/ci/teamcity_build_chain.8180c9c4e5dd6acca740dad979dfdcb4.png?auto=format"
      alt="TeamCity build chain with composite build at the end" /%}

The final composite build must be properly configured in terms of version control settings, with the VCS Root attached and the [VCS Trigger](https://www.jetbrains.com/help/teamcity/configuring-vcs-triggers.html#Trigger+build+on+changes+in+snapshot+dependencies) configured.

1. The following configuration parameters need to be present for TeamCity projects:

   - **datadog.ci.api.key**: Your [Datadog API Key](https://app.datadoghq.com/organization-settings/api-keys). Supports type **Password** in plugin version 0.0.5 and later.
   - **datadog.ci.site**:
   - **datadog.ci.enabled**: `true` (`false` can be used to disable the plugin for a specific project).

You can add them to either TeamCity subprojects or the [TeamCity Root Project](https://www.jetbrains.com/help/teamcity/project-administrator-guide.html#Root+Project). When added to the Root project, they are propagated to all its subprojects. For example, to enable the plugin for all projects, add `datadog.ci.enabled` with the value `true` to the Root Project.

For more information on defining configuration parameters, see the [TeamCity Project Hierarchy documentation](https://www.jetbrains.com/help/teamcity/project-administrator-guide.html#Project+Hierarchy).

1. To enable the plugin, click on **Enable uploaded plugins** in the **Administration** -> **Plugins** page. Alternatively, restart the TeamCity server.

## Advanced configuration{% #advanced-configuration %}

### Configure Git user information{% #configure-git-user-information %}

The plugin retrieves the Git author name and email based on the [TeamCity username style](https://www.jetbrains.com/help/teamcity/git.html#General+Settings). Datadog recommends using either **Author Name and Email** or **Author Email** username styles, as they provide information about the user email.

When one of the other username styles is used (**UserId** or **Author Name**), the plugin automatically generates an email for the user by appending `@Teamcity` to the username. For example, if the **UserId** username style is used and the Git author username is `john.doe`, the plugin generates `john.doe@Teamcity` as the Git author email. The username style is defined for [VCS Roots](https://www.jetbrains.com/help/teamcity/configuring-vcs-roots.html), and can be modified in the VCS Root settings.

{% alert level="danger" %}
The Git author email is used for [billing purposes](https://www.datadoghq.com/pricing/?product=ci-visibility#ci-visibility), therefore there might be cost implications when username styles not providing email (**UserId** or **Author Name**) are used. [Reach out to the Datadog support team](https://docs.datadoghq.com/help/) if you have any questions about your use case.
{% /alert %}

## Visualize pipeline data in Datadog{% #visualize-pipeline-data-in-datadog %}

View your data on the [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages after the pipelines finish.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Troubleshooting{% #troubleshooting %}

All the logs generated by the Datadog CI Integration plugin are stored inside the `teamcity-server.log` file and can be accessed from the TeamCity Server by going to **Administration** -> **Diagnostic** -> **Server Logs**. Check these logs to get additional context on any issues with the plugin.

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
