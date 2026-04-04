# Source: https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github

Title: Connect an Azure Boards or Azure DevOps project to a GitHub repository - Azure Boards

URL Source: https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github

Markdown Content:
**Azure DevOps Services**

Use GitHub.com repositories for your software development and your Azure Boards project to plan and track your work. Connect your project and repo so your GitHub commits and pull requests get linked to your work items in Azure Boards.

| Category | Requirements |
| --- | --- |
| Permissions | - Member of the [**Project Collection Administrators** group](https://learn.microsoft.com/en-us/azure/devops/organizations/security/change-organization-collection-level-permissions?view=azure-devops) If you created the project, you have permissions. - **Administrator** or **owner** of the GitHub repository to connect to. You can connect to multiple GitHub repositories as long as you're an administrator for those repositories. |
| **Project membership** | [Project member](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops). |

The following authentication options are supported based on the GitHub platform you want to connect to.

**GitHub.com**

**GitHub Enterprise Server**

*   [GitHub.com user account (Recommended)](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#add-a-github-connection-with-github-credentials)
*   [Personal access token (PAT)](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#github-pat)

*   [OAuth (preferred, registration required)](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#server-github-ent-oauth-register)
*   [PAT](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#server-github-ent-pat)
*   [GitHub credentials](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#server-github-ent-credentials)

Note

If you choose to connect GitHub with a PAT, configure single sign-on (SSO) for the PAT on your GitHub account. This configuration is necessary to retrieve a list of repositories from an organization with Security Assertion Markup Language (SAML) SSO authentication enabled.

1.   Sign in to your project (`https://dev.azure.com/{Your_Organization/Your_Project}`).

2.   Select **Project settings**>**GitHub connections**.

![Image 1: Screenshot of open Project Settings>GitHub connections.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/open-project-settings-github-connections.png?view=azure-devops)

3.   If it's your first time connecting from the project, select **Connect your GitHub account** to use your GitHub account credentials.

![Image 2: Screenshot of first time connecting with GitHub credentials.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/connect-github-account-first-time.png?view=azure-devops)

Otherwise, choose ![Image 3](https://learn.microsoft.com/en-us/azure/devops/media/icons/add-light-icon.png?view=azure-devops)**New connection**, and select your authentication method from the **New Connection** dialog.

When you connect with your GitHub account, use your GitHub credentials to authenticate. To use a PAT, see [Add a GitHub connection using PAT](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#github-pat). For connecting to a GitHub Enterprise Server, see [Register Azure DevOps in GitHub as an OAuth App](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#server-github-ent-oauth-register).

You can connect up to 1,000 GitHub repositories to an Azure Boards project.

1.   If it's your first time connecting to GitHub from Azure Boards, sign in using your GitHub credentials. Choose an account for which you're a repository administrator.

2.   Select the GitHub account or organization you want to connect. Only organizations that you own or are an administrator for are listed.

If all repositories for an organization are already connected to Azure Boards, the following message shows:

![Image 4: Screenshot of message where no more repositories exist to connect.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/message-all-repositories-already-connected.png?view=azure-devops)

3.   Enter your GitHub credentials. If you have two-factor authentication enabled, enter the authentication code sent by GitHub and select **Verify**. If not, the system automatically recognizes your GitHub organization as your GitHub account is associated with your Azure DevOps Services account.

Once authenticated, you can select the repositories you want to connect.

1.   The **Add GitHub Repositories** dialog automatically displays and selects all GitHub.com repositories for which you're an administrator in the selected organization. Deselect any repositories that you don't want to include in the integration.

![Image 5: Screenshot showing GitHub repos.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github/add-github-repos.png?view=azure-devops)

Tip

To avoid unexpected **AB#** mention linking, we recommend connecting a GitHub repo to projects within a single Azure DevOps organization. Connecting the same GitHub repo to projects in multiple Azure DevOps organizations can cause issues. For more information, see [Troubleshoot GitHub & Azure Boards integration](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops#resolve-connection-issues). 
If all repositories are already connected to the current or another organization, the following message displays:

![Image 6: Screenshot of message where no more repositories exist to connect.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/message-all-repositories-already-connected.png?view=azure-devops)

2.   After making your selections, select **Save**.

1.   Review the GitHub page that displays and then choose **Approve, Install, & Authorize**.

![Image 7: Screenshot showing confirming GitHub repositories.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github/approve-install-auth-azure-boards-from-github.png?view=azure-devops)

2.   Provide your GitHub credentials to confirm.

3.   When you're done, you should see the new connection with the selected repositories listed.

![Image 8: Screenshot of list of connected repositories.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github/repos-list-s154.png?view=azure-devops)

To change the configuration or manage the Azure Boards app for GitHub, see [Change repository access to Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/github/change-azure-boards-app-github-repository-access?view=azure-devops).

We recommend using your GitHub account credentials to connect to your GitHub repository.

Tip

When you create your GitHub PAT, make sure that you include these scopes: `repo, read:user, user:email, admin:repo_hook`.

1.   Choose **Personal Access Token**.

![Image 9: Screenshot of New GitHub connection dialog, choosing Personal Access Token.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/connect-with-pat.png?view=azure-devops)

To create a GitHub PAT, go to [GitHub Developer Settings > Personal access tokens](https://github.com/settings/tokens).

2.   Enter the PAT and select **Connect**.

![Image 10: Screenshot showing entered PAT.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github/add-github-connection-dialog-pat.png?view=azure-devops)

3.   Select the repositories you want to connect to the project by following the procedures outlined in [Choose the repositories](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#choose-repositories) earlier in this article.

4.   If it's the first time connecting to a GitHub account or organization from Azure Boards, install the Azure Boards app for GitHub. [Confirm the connection](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#confirm-connection) earlier in this article.

To use OAuth to connect Azure DevOps with your GitHub Enterprise Server, first register the application as an OAuth App. For more information, see [Create an OAuth App](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/).

1.   Sign into the web portal for your GitHub Enterprise server.

![Image 11: Screenshot of sign in for GitHub Enterprise server.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github-ent/sign-in-to-ghe.png?view=azure-devops)

2.   Open **Settings**>**Developer settings**>**Oauth Apps**>**New OAuth App**.

![Image 12: Screenshot showing sequence for New OAuth App.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github-ent/ghe-settings-dev-oauth.png?view=azure-devops)

3.   Enter registration information.

For the **Homepage URL**, specify the **Organization URL** of your organization.

 For the **Authorization callback URL**, use the following pattern to construct the URL.

`{Azure DevOps Services Organization URL}/_admin/oauth2/callback`

For example:

`https://dev.azure.com/fabrikam/_admin/oauth2/callback`

![Image 13: Screenshot showing app to register.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github-ent/ghe-register-app-services.png?view=azure-devops)

4.   Select **Register application**.

5.   The **Client ID** and **Client Secret** for your registered OAuth application appear.

![Image 14: Screenshot of Client ID and Client Secret for the registered OAuth application.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github-ent/ghe-register-app-success.png?view=azure-devops)

1.   Sign into the web portal for Azure DevOps Services.

2.   Add the GitHub Enterprise Oauth configuration to your organization.

3.   In **Organization settings**, select **Oauth configurations**>**Add Oauth configuration**.

![Image 15: Screenshot of Open Organization Settings, OAuth configurations.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/open-oauth-configuration.png?view=azure-devops)

4.   Enter your information, and then select **Create**.

![Image 16: OAuth configurations dialog.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/register-oauth-azure-devops.png?view=azure-devops)

Important

To connect Azure DevOps Services to your GitHub Enterprise Server, ensure your GitHub Enterprise Server is accessible from the Internet. Verify that Azure DNS can resolve your GitHub Enterprise Server name and that your firewall allows access from Azure Data Center IP addresses. To determine the IP address range, see [Microsoft Azure Data Center IP Ranges](https://www.microsoft.com/download/details.aspx?id=41653). A common error message for connectivity issues is:

_The remote name could not be resolved: 'github-enterprise-server.contoso.com'_

If you encounter this error, check your server's accessibility. For more information, see [Azure DNS FAQ](https://learn.microsoft.com/en-us/azure/dns/dns-faq).

1.   Select **Project settings**>**GitHub connections**>**GitHub Enterprise Server** for a first-time connection.

![Image 17: First connection, choose GitHub Enterprise Server.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/first-connection-enterprise.png?view=azure-devops)

Or, from the **New GitHub connection** dialog, select **GitHub Enterprise Server**.

![Image 18: Screenshot of New GitHub connection dialog, choose GitHub Enterprise Server.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/connect-to-enterprise.png?view=azure-devops)

2.   Select the authentication method.

![Image 19: Screenshot showing authentication method dialog.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/enterprise-select-authentication-method.png?view=azure-devops)

**Connect with OAuth**

Choose the configuration that you set up in [Step 4 of Register your OAuth configuration in Azure DevOps Services](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#register-services-github-ent-oauth), and then choose **Connect**.

![Image 20: Screenshot of New GitHub Enterprise connection, OAuth connection dialog.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/new-github-enterprise-server-dialog-oauth.png?view=azure-devops)

**Connect with a Personal Access Token**

Enter the URL for your GitHub Enterprise server and the Personal access token credentials recognized by that server. And then choose **Connect**.

![Image 21: Screenshot of New GitHub Enterprise connection, Personal access token connection dialog.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/new-github-enterprise-server-dialog-pat.png?view=azure-devops)

**Connect with GitHub credentials**

Enter the URL for your GitHub Enterprise server and the administrator account credentials recognized by that server, and then select **Connect**.

![Image 22: Screenshot of New GitHub Enterprise connection screen, User Name connection dialog.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/connect-cloud/new-github-enterprise-server-dialog-user-name.png?view=azure-devops)

3.   The dialog lists all repositories for which you have GitHub administration rights. You can toggle between **Mine** and **All** to determine if others appear, and then check the ones that you want to add. Select **Save** when you're done.

![Image 23: Screenshot of repositories listed.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/github-ent/ads-add-ghe-repositories.png?view=azure-devops)

Tip

You can only make a connection to repositories defined under one GitHub organization. To connect a project to other repositories defined in another GitHub organization, you must add another connection. 
4.   If it's your first time connecting to a GitHub account or organization from Azure Boards, you also install the Azure Boards app for GitHub. [Confirm the connection](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github#confirm-connection) earlier in this article.

The Azure Boards-GitHub integration uses various authentication protocols to maintain the connection. Changes to a user's permission scope or authentication credentials can revoke the GitHub repositories connected to Azure Boards.

For an overview of the integration supported by the Azure Boards app for GitHub, see [Azure Boards-GitHub integration](https://learn.microsoft.com/en-us/azure/devops/boards/github/?view=azure-devops).

The following supported authentication options depend on the GitHub platform you are connecting to:

**Platform**

**GitHub.com**

**GitHub Enterprise Server**

**Azure DevOps Services**

*   GitHub.com user account
*   Personal access token (PAT)

*   OAuth
*   PAT
*   GitHub credentials

**Azure DevOps Server 2020**

Not applicable

*   PAT
*   GitHub credentials

Note

**GitHub integration support:**

*   **Azure DevOps Services**: Integrates with both GitHub.com and GitHub Enterprise Server repositories through the Azure Boards app for GitHub.
*   **Azure DevOps Server 2020 and later**: Supports integration with GitHub Enterprise Server repositories only.
*   **Other Git repositories**: Integration is not supported.

If the integration between Azure Boards and GitHub isn't working as expected, verify that you granted organization access.

1.   From GitHub web portal, open **Settings** from your profile menu.

![Image 24: Screenshot of open profile, choose Settings.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/troubleshoot/choose-settings.png?view=azure-devops)

2.   Select **Applications** under **Integrations**>**Authorized OAuth Apps**>**Azure Boards**.

3.   Under **Organization access**, resolve any issues that might appear. Select **Grant** to grant access to any organizations that show as having an **Access request pending**.

![Image 25: Screenshot of Organization access with organizations without access.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/troubleshoot/organization-access-issues.png?view=azure-devops)

When the Azure Boards connection to GitHub loses access, an alert status with a red-X appears in the user interface. Hover over the alert to see that the credentials are no longer valid. To fix the issue, remove the connection and create a new one.

![Image 26: Screenshot of failed connection.](https://learn.microsoft.com/en-us/azure/devops/boards/github/media/troubleshoot/failed-connection.png?view=azure-devops)

To resolve this issue, consider the following items:

*   **If the connection is using OAuth**:

    *   The Azure Boards application had its access denied for one of the repositories.

    *   GitHub might be unavailable/unreachable. This unavailability could be because of an outage in either service or an infrastructure/network issue on-premises. You can check service status from the following links:

        *   [GitHub](https://status.github.com/)
        *   [Azure DevOps](https://status.dev.azure.com/)

Delete and recreate the connection to the GitHub repository. This recreated connection causes GitHub to prompt to reauthorize Azure Boards.

*   **If the connection is using a PAT:**

    *   The PAT was revoked or the required permission scopes changed and are insufficient.

    *   The user might not have admin permissions on the GitHub repo.

Recreate the PAT and ensure the scope for the token includes the required permissions: `repo, read:user, user:email, admin:repo_hook`. For more information, see [Best practices for using PATs](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops#best-practices-for-using-pats).

If you migrated from Azure DevOps Server to Azure DevOps Services with an existing GitHub Enterprise Server connection, your existing connection might not work as expected. Work item mentions within GitHub might be delayed or never appear in Azure DevOps Services because the callback URL associated with GitHub is no longer valid. Consider the following resolutions:

*   **Remove and re-create the connection**: Remove and re-create the connection to the GitHub Enterprise Server repository. Follow the sequence of steps provided in [Connect from Azure Boards](https://learn.microsoft.com/en-us/azure/devops/boards/github/connect-to-github?view=azure-devops#github-ent-oauth-services) documentation.

*   **Fix the webhook URL**: Go to GitHub's repository settings page and edit the webhook URL, pointing to the migrated Azure DevOps organization URL: `https://dev.azure.com/{OrganizationName}/_apis/work/events?api-version=5.2-preview`

When you connect your GitHub repository to projects in multiple Azure DevOps organizations, such as dev.azure.com/Contoso and dev.azure.com/Fabrikam, can cause unexpected results with **AB#** mentions. Work item IDs aren't unique across Azure DevOps organizations, so **AB#12** could refer to a work item in either Contoso or Fabrikam. When a work item is mentioned in a commit message or pull request, both organizations might attempt to link to a work item with the matching ID, causing confusion.

To avoid this issue, connect a single GitHub repository to only one Azure DevOps organization.

Note

When you connect using the Azure Boards app for GitHub, the app prevents connections to multiple organizations. If a GitHub repository is connected to the wrong Azure DevOps organization, contact the owner of that organization to remove the connection before adding the repository to the correct Azure DevOps organization.

Update the XML definitions for the work item types if your organization uses the Hosted XML or on-premises XML process model to customize the work tracking experience and link to and view the GitHub link types from the Development section in the work item forms.

For example, to link user stories and bugs to GitHub commits and pull requests from the **Development** section, update the XML definitions for user stories and bugs.

Follow the sequence of tasks provided in [Hosted XML process model](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/work/hosted-xml-process-model?view=azure-devops) to update the XML definitions. For each work item type, find the `Group Label="Development"` section, and add the following two lines in the code syntax to support the external link types: **GitHub Commit** and **GitHub Pull Request**.

```
<ExternalLinkFilter Type="GitHub Pull Request" />  
             <ExternalLinkFilter Type="GitHub Commit" />
```

After you update, the section should appear as follows.

```
<Group Label="Development">  
   <Control Type="LinksControl" Name="Development">  
      <LinksControlOptions ViewMode="Dynamic" ZeroDataExperience="Development" ShowCallToAction="true">  
         <ListViewOptions GroupLinks="false">   
         </ListViewOptions>  
         <LinkFilters>  
             <ExternalLinkFilter Type="Build" />  
             <ExternalLinkFilter Type="Integrated in build" />  
             <ExternalLinkFilter Type="Pull Request" />  
             <ExternalLinkFilter Type="Branch" />  
             <ExternalLinkFilter Type="Fixed in Commit" />  
             <ExternalLinkFilter Type="Fixed in Changeset" />  
             <ExternalLinkFilter Type="Source Code File" />  
             <ExternalLinkFilter Type="Found in build" />  
             <ExternalLinkFilter Type="GitHub Pull Request" />  
             <ExternalLinkFilter Type="GitHub Commit" />  
         </LinkFilters>  
      </LinksControlOptions>  
   </Control>  
</Group>
```

A: No. Ask your users to sign out and then sign back in to the organization with their GitHub credentials from a fresh browser session. This action establishes their GitHub identities.

A: After changing the setting, sign out of Azure DevOps and then sign back in to the organization (`dev.azure.com/{organizationName}` or `organizationName.visualstudio.com`) with your GitHub credentials from a fresh browser session.

A: Only organization or project Administrators can invite new users to join the organization. You might not have the required permissions to add new users. Work with your administrator to get the necessary permissions or ask them to add the user for you.

A: For more information, see [User and permissions management FAQs/GitHub Enterprise](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/faq-user-and-permissions-management?view=azure-devops#github-enterprise).

*   [Install and configure the Azure Boards app for GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/install-github-app?view=azure-devops)
*   [Configure status badges to add to GitHub README files](https://learn.microsoft.com/en-us/azure/devops/boards/github/configure-status-badges?view=azure-devops)
*   [Troubleshoot GitHub & Azure Boards integration](https://learn.microsoft.com/en-us/azure/devops/boards/github/troubleshoot-github-connection?view=azure-devops)
*   [Build GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops)
*   [Change GitHub repository access](https://learn.microsoft.com/en-us/azure/devops/boards/github/install-github-app?view=azure-devops#change-repository-access)

Once connected, you can:

*   **Use GitHub Copilot**: [Use GitHub Copilot with work items](https://learn.microsoft.com/en-us/azure/devops/boards/github/work-item-integration-github-copilot?view=azure-devops) for automated code generation
*   **Link work items**: Automatically link commits, branches, and pull requests to work items
*   **Track development**: Monitor progress directly from Azure Boards
