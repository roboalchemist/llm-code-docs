# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/managing-jira-work-items.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/managing-jira-work-items.md

# Managing Jira work items

### Prerequisites

Before you can start pushing SonarQube issues to Jira Cloud, you need to connect your SonarQube instance with your Jira Cloud instance and bind your SonarQube project to a Jira Cloud project. See:

* [jira-integration](https://docs.sonarsource.com/sonarqube-server/instance-administration/jira-integration "mention") on an instance level.
* [jira-integration](https://docs.sonarsource.com/sonarqube-server/project-administration/jira-integration "mention") on a project level.

### Permissions

To create or disconnect Jira work items from Sonar issues, you must be a project administrator or have the **Administer Issues** permission.

Go to *Your Project* > **Project Settings** > **Permissions** and select the **Administer Issues** or **Administer** checkbox for specific users and groups.

### Creating a Jira work item from a single SonarQube issue

You can create a Jira work item from a SonarQube issue or from the Issues page:

1. Click the **Push to Jira** button and choose a Jira work type, if more than two work types are available. The list of Jira work types depends on your Jira Cloud integration configuration and is configured by the project administrator. See [jira-integration](https://docs.sonarsource.com/sonarqube-server/project-administration/jira-integration "mention") for more details.
2. When the process is complete the button displays a Jira work item ID along with the status label.
3. A new Jira work item will be created in your Jira Cloud project and it will open in a new tab.
4. Click on the Jira work item ID to open it on the Jira’s website.

{% hint style="info" %}
If you are not seeing the **Push to Jira** button after properly setting your Jira Cloud integration, it might be due to unsupported mandatory fields present on all of the Jira work types. See [#mandatory-fields-without-a-default-value](https://docs.sonarsource.com/sonarqube-server/project-administration/jira-integration#mandatory-fields-without-a-default-value "mention") for more information.
{% endhint %}

On rare occasions, two or more concurrent Jira creation events might be triggered by multiple users simultaneously, resulting in two or more Jira work items being created at the same time.

### Contents of a Jira work item

When you create a Jira work item, it includes the following information:

* Title of the SonarQube issues
* SonarQube issue link
* Location of the issues
  * File path
  * Code lines
  * Commit hash
  * Date the issue was introduced
* Information about why this is an issue and how to fix it with the rule name and link.
* Impact on software quality and severity
* The reporter for the Jira work item is the default reporter set in SonarQube instance’s Jira Cloud integration.

### Disconnecting a Jira work item

You cannot delete a Jira work item from within SonarQube Server, but you can disconnect it by clicking on the close icon of the Jira button either within the SonarQube issue or on the Issues page. The connection with the Jira work item will be removed but the item will still exist in Jira Cloud.

You cannot push a SonarQube issue to an existing Jira work item, which means you can only create new Jira work items from SonarQube issues.

### Troubleshooting

* The **Push to Jira** button is not visible on the SonarQube issue page.\
  **Solution**: After connecting your instance to a Jira instance you need to bind individual SonarQube projects to Jira Cloud projects. See project-level [jira-integration](https://docs.sonarsource.com/sonarqube-server/project-administration/jira-integration "mention") for more information.

### Related pages

* [jira-integration](https://docs.sonarsource.com/sonarqube-server/instance-administration/jira-integration "mention") on an instance level.
* [jira-integration](https://docs.sonarsource.com/sonarqube-server/project-administration/jira-integration "mention") on a project level.

<br>
