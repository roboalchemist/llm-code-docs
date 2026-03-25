# Source: https://docs.axonius.com/docs/configuring-jira-settings.md

# Configuring Jira Settings

<Callout icon="📘" theme="info">
  Note

  This configuration is only required if you have Cloud Asset Compliance and want to use the Create Jira Issue Enforcement Action that is part of Cloud Asset Compliance.
</Callout>

**To configure Jira settings:**

1. From the top right corner of any page, click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **External Integrations**, and select **Jira**.

![JiraSettingsNM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JiraSettingsNM.png)

3. Toggle on **Use Jira**.  This is a prerequisite if you have Cloud Asset Compliance and want to use the [ Create Jira Issue Enforcement Action](/docs/cac-create-jira-issue) that is part of that module.
4. Do one of the following
   * **For Jira Cloud Users**

     1. Log in to Jira  and use the following URL to generate an API token: [https://id.atlassian.com/manage/api-tokens#](https://id.atlassian.com/manage/api-tokens#)

     <Image alt="image.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(421).png" />

     2. Specify the **Jira domain**, **User name**, and **API Token**.
     3. Select **Verify SSL** to verify the SSL certificate of the server.
     4. Select **Use assignee name instead of ID** to use the assignee ID instead of the assignee name in **Assignee** fields.
   * **For Jira On-prem/Jira hosted users**
     1. Obtain the **Personal Access Token** from the account.  Refer to [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) for information about obtaining the **Personal Access Token**.
     2. Specify the **Jira domain** and **Personal Access Token**.
     3. Select **Verify SSL** to verify the SSL certificate of the server.
     4. Select **Use assignee name instead of ID** to use the assignee ID instead of the assignee name in **Assignee** fields.