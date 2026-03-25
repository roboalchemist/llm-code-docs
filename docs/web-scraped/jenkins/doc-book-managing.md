# Source: https://www.jenkins.io/doc/book/managing/

Title: Managing Jenkins

URL Source: https://www.jenkins.io/doc/book/managing/

Markdown Content:
Managing Jenkins
===============

[> User Documentation Home](https://www.jenkins.io/doc/)

##### User Handbook

*   [User Handbook Overview](https://www.jenkins.io/doc/book/getting-started/)
*   [Installing Jenkins](https://www.jenkins.io/doc/book/installing/)
*   [Platform Information](https://www.jenkins.io/doc/book/platform-information/)
*   [Using Jenkins](https://www.jenkins.io/doc/book/using/)
*   [Pipeline](https://www.jenkins.io/doc/book/pipeline/)
*   [Blue Ocean](https://www.jenkins.io/doc/book/blueocean/)
*   [Managing Jenkins](https://www.jenkins.io/doc/book/managing/)
    *   [Configuring the System](https://www.jenkins.io/doc/book/managing/system-configuration/)
    *   [Configuration as Code](https://www.jenkins.io/doc/book/managing/casc/)
    *   [Managing Tools](https://www.jenkins.io/doc/book/managing/tools/)
    *   [Managing Plugins](https://www.jenkins.io/doc/book/managing/plugins/)
    *   [About Jenkins](https://www.jenkins.io/doc/book/managing/about-jenkins/)
    *   [System Information](https://www.jenkins.io/doc/book/managing/system-info/)
    *   [Jenkins Features Controlled with System Properties](https://www.jenkins.io/doc/book/managing/system-properties/)
    *   [Change System Time Zone](https://www.jenkins.io/doc/book/managing/change-system-timezone/)
    *   [Jenkins CLI](https://www.jenkins.io/doc/book/managing/cli/)
    *   [Script Console](https://www.jenkins.io/doc/book/managing/script-console/)
    *   [Groovy Hook Scripts](https://www.jenkins.io/doc/book/managing/groovy-hook-scripts/)
    *   [Managing Nodes](https://www.jenkins.io/doc/book/managing/nodes/)
    *   [In-process Script Approval](https://www.jenkins.io/doc/book/managing/script-approval/)
    *   [Users](https://www.jenkins.io/doc/book/managing/users/)
    *   [Themes for user interface](https://www.jenkins.io/doc/book/managing/ui-themes/)
    *   [User Content](https://www.jenkins.io/doc/book/managing/user-content/)
    *   [Spawning Processes From Build](https://www.jenkins.io/doc/book/managing/spawning-processes/)

*   [Securing Jenkins](https://www.jenkins.io/doc/book/security/)
*   [System Administration](https://www.jenkins.io/doc/book/system-administration/)
*   [Scaling Jenkins](https://www.jenkins.io/doc/book/scaling/)
*   [Troubleshooting Jenkins](https://www.jenkins.io/doc/book/troubleshooting/)
*   [Glossary](https://www.jenkins.io/doc/book/glossary/)

##### Tutorials

*   [Guided Tour](https://www.jenkins.io/doc/pipeline/tour/getting-started/)
*   [Jenkins Pipeline](https://www.jenkins.io/doc/tutorials#pipeline)
*   [Using Build Tools](https://www.jenkins.io/doc/tutorials#tools)

##### Resources

*   [Pipeline Syntax reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
*   [Pipeline Steps reference](https://www.jenkins.io/doc/pipeline/steps/)
*   [LTS Upgrade guides](https://www.jenkins.io/doc/upgrade-guide/)

[⇐ Blue Ocean](https://www.jenkins.io/doc/book/blueocean)

[Index](https://www.jenkins.io/doc/book/)

[Configuring the System ⇒](https://www.jenkins.io/doc/book/managing/system-configuration)

Managing Jenkins
================

 Chapter Sub-Sections 

*   [Configuring the System](https://www.jenkins.io/doc/book/managing/system-configuration)
*   [Configuration as Code](https://www.jenkins.io/doc/book/managing/casc)
*   [Managing Tools](https://www.jenkins.io/doc/book/managing/tools)
*   [Managing Plugins](https://www.jenkins.io/doc/book/managing/plugins)
*   [About Jenkins](https://www.jenkins.io/doc/book/managing/about-jenkins)
*   [System Information](https://www.jenkins.io/doc/book/managing/system-info)
*   [Jenkins Features Controlled with System Properties](https://www.jenkins.io/doc/book/managing/system-properties)
*   [Change System Time Zone](https://www.jenkins.io/doc/book/managing/change-system-timezone)
*   [Jenkins CLI](https://www.jenkins.io/doc/book/managing/cli)
*   [Script Console](https://www.jenkins.io/doc/book/managing/script-console)
*   [Groovy Hook Scripts](https://www.jenkins.io/doc/book/managing/groovy-hook-scripts)
*   [Managing Nodes](https://www.jenkins.io/doc/book/managing/nodes)
*   [In-process Script Approval](https://www.jenkins.io/doc/book/managing/script-approval)
*   [Users](https://www.jenkins.io/doc/book/managing/users)
*   [Themes for user interface](https://www.jenkins.io/doc/book/managing/ui-themes)
*   [User Content](https://www.jenkins.io/doc/book/managing/user-content)
*   [Spawning Processes From Build](https://www.jenkins.io/doc/book/managing/spawning-processes)

Table of Contents

*   [System Configuration group](https://www.jenkins.io/doc/book/managing/#system-configuration-group)
*   [Security group](https://www.jenkins.io/doc/book/managing/#security-group)
*   [Status Information group](https://www.jenkins.io/doc/book/managing/#status-information-group)
*   [Troubleshooting group](https://www.jenkins.io/doc/book/managing/#troubleshooting-group)
*   [Tools and Actions group](https://www.jenkins.io/doc/book/managing/#tools-and-actions-group)
*   [Uncategorized group](https://www.jenkins.io/doc/book/managing/#uncategorized-group)

Most standard administrative tasks can be performed from the screens in the **Manage Jenkins** section of the dashboard. In this chapter, we look at these screens and explain how to use them.

The tiles displayed on the **Manage Jenkins** page are grouped logically. Here we discuss the pages that are part of the standard installation. Plugins may add pages to this screen.

The top of the **Manage Jenkins** screen may contain "Monitors" that alert you when a new version of the Jenkins software or a security update is available. Each monitor includes a description of the issue it is reporting and links to additional information about the issue

Inline help is available on most **Manage Jenkins** pages:

*   To access the help, select the `?` icon to the right of each field.

*   Click the `?` icon again to hide the help text.

Other system administration topics are discussed in [Jenkins System Administration](https://www.jenkins.io/doc/book/system-administration/).

[](https://www.jenkins.io/doc/book/managing/#system-configuration-group)System Configuration group
--------------------------------------------------------------------------------------------------

Screens for configuring resources for your Jenkins controller.

[System](https://www.jenkins.io/doc/book/managing/system-configuration)
Configure global settings and paths for the Jenkins controller

[Tools](https://www.jenkins.io/doc/book/managing/tools)
Configure tools, their locations, and automatic installers

[Plugins](https://www.jenkins.io/doc/book/managing/plugins)
Add, update, remove, disable/enable plugins that extend the functionality of Jenkins.

[Nodes and Clouds](https://www.jenkins.io/doc/book/managing/nodes)
Add, remove, control, and monitor the nodes used for the agents on which build jobs run.

[Configuration as Code](https://www.jenkins.io/doc/book/managing/casc)
Configure your Jenkins controller using a human-readable YAML file rather than the UI. This is an optional feature that appears in this group only when the plugin is installed on your controller.

[](https://www.jenkins.io/doc/book/managing/#security-group)Security group
--------------------------------------------------------------------------

Screens for configuring security features for your Jenkins controller. See [Securing Jenkins](https://www.jenkins.io/doc/book/security/) for general information about managing Jenkins security.

[Security](https://www.jenkins.io/doc/book/managing/system-configuration)
Set configuration parameters that secure your Jenkins controller.

[Manage Credentials](https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials)
Configure the credentials that provide secure access to third-party sites and applications that interact with Jenkins.

**Credential Providers**
Configure credential providers and types

[Users](https://www.jenkins.io/doc/book/managing/users)
Manage users defined in the Jenkins user database. This is not used if you use a different security realm such as LDAP or AD.

[](https://www.jenkins.io/doc/book/managing/#status-information-group)Status Information group
----------------------------------------------------------------------------------------------

[System Information](https://www.jenkins.io/doc/book/managing/system-info)
Displays information about the Jenkins environment.

[System Log](https://www.jenkins.io/doc/book/system-administration/viewing-logs/)
Jenkins log that contains all `java.util.logging` output related to Jenkins.

**Load Statistics**
Displays information about resource utilization on you Jenkins controller.

[About Jenkins](https://www.jenkins.io/doc/book/managing/about-jenkins)
Provides version and license information for your Jenkins controller.

[](https://www.jenkins.io/doc/book/managing/#troubleshooting-group)Troubleshooting group
----------------------------------------------------------------------------------------

**Manage Old Data**
Remove configuration information related to plugins that have been removed from the controller.

[](https://www.jenkins.io/doc/book/managing/#tools-and-actions-group)Tools and Actions group
--------------------------------------------------------------------------------------------

Screens for common management tasks and management tools that enable you to do administrative tasks without using the UI.

**Reload Configuration from Disk**
Discard all data that is loaded in memory and reload everything from the file system. This is useful when you modify configuration files directly on disk.

[Jenkins CLI](https://www.jenkins.io/doc/book/managing/cli)
How to use the Jenkins CLI from a shell or script.

[Script Console](https://www.jenkins.io/doc/book/managing/script-console/)
Execute an Apache Groovy script for administration, troubleshooting, and diagnostics.

Prepare for Shutdown
Prevents new builds from starting so that the system can be shut down safely. Displays a red banner with a custom message so that users know what is about to happen.

![Image 1: Red headband with a custom message](https://www.jenkins.io/doc/book/resources/managing/prepare-for-shutdown.png)

This does not ask Jenkins to stop; this action will just prevent new builds from starting. If you need to stop or restart Jenkins, you should use the command line or the `/restart` and `/safeRestart` end points. There is also a plugin called [Safe Restart](https://plugins.jenkins.io/saferestart/) that will add a `Restart Safely` link in the UI.

[](https://www.jenkins.io/doc/book/managing/#uncategorized-group)Uncategorized group
------------------------------------------------------------------------------------

Screens for plugins that have not yet declared the category of their page.

* * *

[⇐ Blue Ocean](https://www.jenkins.io/doc/book/blueocean)

[Index](https://www.jenkins.io/doc/book/)

[Configuring the System ⇒](https://www.jenkins.io/doc/book/managing/system-configuration)

* * *

[Was this page helpful?](https://www.jenkins.io/doc/book/managing/#feedback)

Please submit your feedback about this page through this [quick form](https://www.jenkins.io/doc/feedback-form/).

Alternatively, if you don't wish to complete the quick form, you can simply indicate if you found this page helpful?

Yes No

Submit

See existing feedback [here](https://docs.google.com/spreadsheets/d/1IIdpVs39JDYKg0sLQIv-MNO928qcGApAIfdW5ohfD78).
