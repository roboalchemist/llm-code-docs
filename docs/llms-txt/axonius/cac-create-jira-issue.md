# Source: https://docs.axonius.com/docs/cac-create-jira-issue.md

# Create Jira Issue

The **Create Jira Issue** action creates a Jira issue including a CSV file with the filtered compliance results attached to the issue.

To configure the **Create Jira Issue** action, in the **Cloud Asset Compliance** page, click the **Enforce** menu, and select **Create Jira Issue**.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1094\).png)

## Connection Settings

To use this action, you must enable the **Use Jira** setting and configure your Jira server. For more details, see [Configuring Jira Settings](/docs/configuring-jira-settings).

## Action Settings

1. **Project Key** *(required)* - Specify or select the desired project in Jira where the issue will be created.
2. **Issue Key** *(required)* - Specify or select the issue type for the created issue.
3. **Summary** *(required)* - Specify a summary for the created issue.
4. **Description** *(required)* - Specify a description for the created issue.
5. Multiple optional fields for the created issue *(optional, default: empty)* :
   * **Assignee** - A single user to assign the tickets to.
   * **Labels** - Comma separated labels that will be added to the tickets.
   * **Components** - Comma separated components that will be added to the tickets.