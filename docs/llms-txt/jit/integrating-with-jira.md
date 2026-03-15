# Source: https://docs.jit.io/docs/integrating-with-jira.md

# Jira Integration

Integrating with Jira

Integrating **Jira** with Jit streamlines the process of assigning security-related tickets directly to Engineering and Security teams from the Jit platform. Learn more about this [here](https://docs.jit.io/docs/integrating-with-tms).

Jit supports 2 methods of Jira integration. One is straight through the web app (recommended), and the other is through as-code configuration (old version).

# Web app integration (recommended)

## Quickstart

1. In Jit's webapp, go to the **Integrations page**:

   ![](https://files.readme.io/4a1e24a-image.png)
2. Find the "Jira" card and click "Connect".
3. You should now see a Jira integration window. Click on "Connect" at the top right corner.

   * You should now be prompted to install Jit's jira app to your Atlassian account.

   * After installing the app, you'll be prompted to select your desired project, as well as any relevant custom fields.

   * If your Jira configuration requires any custom fields, please set them now.

[block:image]{"images":[{"image":["https://files.readme.io/36311a2-image.png",null,""],"align":"center"}]}[/block]

   <br />
4. You can now add multiple Jira configurations, each linked to a specific Jira project.

* During setup, select your desired project and any required custom fields.

* You can add, manage, or delete multiple Jira configurations from the Integrations page.

[block:image]{"images":[{"image":["https://files.readme.io/8a2788e20a2e842a4387d39434456177bae80d88938a807c3071802509c06517-image.png",null,""],"align":"left"}]}[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f3775ef0aa0ae8cbbd9f01de66f2d2c60675cc0a9536d57bfdd43cd8e92c2505-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "750px"
    }
  ]
}
[/block]

5. After configuring your projects, you can create Jira tickets for findings and actions across the Jit platform.
6. Further configurations:\
   The Jira integration supports bi-directional connection, you can enable two options in the project configuration section:

   1. Close ticket From Fixed finding - this option will change the status of the ticket and will move it to the "completed lane" that you choose once the finding that is connected to the ticket is marked as fixed by the Jit platform.
   2. Update Jira Issue Status - this option will let you see the status of the ticket inside the Jit platform under the finding details.

   ![](https://files.readme.io/641a31e847d1c750faa8ceb9227a5e43793c41cbdfd24b2b7883819e57a31e10-image.png)

**Important note:** Custom **labels** are not supported and will be overridden if set. Jira tickets will always be created with the `Opened-by-Jit` label.

***

# As-code integration (old)

> ❗️ Important – New users
>
> The As-code Jira integration is **deprecated** and should not be used by new customers.\
> New users should use the current Jira integration via the Jit platform UI, which replaces this flow and is actively maintained.
>
> This page is kept for existing customers only.

> 📘 Prerequisites
>
> * Ensure that you have Jira **permissions** and you are familiar with the Jira **configurations** in your organization.
> * Jit supports **software development** project types in Jira only.

**Note**: It is recommended to set up a new user in Jira for this integration and not to link this to a specific individual's personal account.

# Integration steps

* Step 1: Create an API token in your Atlassian account.
* Step 2: Assign a secret to the API token in Jit.
* Step 3: Configure the integration in Jit.

## Step 1: Create an API Token in Your Atlassian Account

1. Log in to your Atlassian account.

2. Navigate to **[API token](https://id.atlassian.com/manage-profile/security/api-tokens)**.
   1. Click **Create API Token**.
   2. Assign a **Label** for easy identification, like `jit_token`.
   3. Click **Create**, then **Copy** to clipboard the generated token.

Learn more in [Atlassian documentation](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

## Step 2: Assign a Secret to the API Token in Jit

1. In the **Jit platform**, go to **Settings > Secrets**.

   ![](https://files.readme.io/956db39-image.png)

2. Click **Create new secret** and add the **API token** you created. It's recommended to name the secret something recognizable, like `jira_token`.

Learn more about managing Jit [Secrets](https://docs.jit.io/docs/secrets).

## Step 3: Configure the Integration in Jit

1. In the **Jit platform**, go to **Integrations** and locate the **Jira** tile.

   ![](https://files.readme.io/0d7130d-image.png)

2. Click **Integrate as-code** to open the **jit-integration.yml** file in your centralized Jit repository.

3. Copy and paste the **Jira integration-structure** at the end of the file.

```Text Jira integration-structure
jira:
  `jira_integration_name`:
    auth:
      api_token: ${{ jit_secrets.`secret_name` }}
      email: `email_address`
      domain: `jira_domain_name`
    preferences:
      project_id: `jira_project_id`
      issue_type_id: `jira_issue_type_id`
      fields:
        `customfield_XXXXX`:
          - value: "`customfield_XXXXX_value`"
        components:
          - name: "`component_YYY`"
```

4. Replace the placeholders with your specific information as outlined in the table below:

Your Jira organization domain **name** can be extracted from your Atlassian URL.\
![](https://files.readme.io/191fe1c-image.png)

[block:parameters]
{
  "data": {
    "h-0": "Key",
    "h-1": "Value",
    "0-0": "jira_integration_name",
    "0-1": "Name this integration, possibly after your Jira project, e.g., `Engineering`.",
    "1-0": "secret_name",
    "1-1": "The name you assigned to the secret in Step 2, e.g., `jira_token`.",
    "2-0": "email_address",
    "2-1": "The security champion's email (listed in the Atlassian account).",
    "3-0": "jira_domain_name",
    "3-1": "Your Jira organization domain **name** can be extracted from your Atlassian URL (described above). See [Verify a domain to manage accounts](https://support.atlassian.com/user-management/docs/verify-a-domain-to-manage-accounts/).",
    "4-0": "jira_project_id",
    "4-1": "See [How to get Jira Project **ID**](https://confluence.atlassian.com/jirakb/how-to-get-project-id-from-the-jira-user-interface-827341414.html).",
    "5-0": "issue_type_id",
    "5-1": "See [Finding the **ID** for Jira issue types](https://confluence.atlassian.com/jirakb/finding-the-id-for-issue-types-646186508.html). Choose the default issue type ID (e.g., the ID of `Story` or `Incident` types).",
    "6-0": "customfield_XXXXX, customfield_XXXXX_value",
    "6-1": "If applicable, add any custom fields with default values. Remove if not used.  \nRead more on Jira custom fields [here](https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/#setting-custom-field-data-for-other-field-types) or by trying to [edit them](https://support.atlassian.com/jira-cloud-administration/docs/edit-or-delete-a-custom-field/).",
    "7-0": "component_YYY",
    "7-1": "Include relevant [components](https://support.atlassian.com/jira-software-cloud/docs/what-are-jira-components/) here if used in your project. Remove if not used."
  },
  "cols": 2,
  "rows": 8,
  "align": [
    "left",
    "left"
  ]
}
[/block]

Adjust or remove the `fields` key as needed for your Jira setup. For more options, see the Jira `Create Issue` POST API [here](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post).

For example:

```Text Jira integration-structure example
jira:
  Engineering:
    auth:
      api_token: ${{ jit_secrets.jira_token }}
      email: ran@jit.io
      domain: Jit
    preferences:
      project_id: 10200
      issue_type_id: 10001
      fields:
        customfield_10007:
          - value: "security"
        assignee:
          id: "9990a2b5896d10ebd47114df"
        components:
          - name: "Development"
```