# Source: https://redocly.com/docs/realm/reunite/project/remote-content/from-azure-devops.md

# Add remote files from Azure DevOps

If your content is stored in a repository on Azure DevOps Services, you can connect that repository, so you can access and publish those files in Reunite.

To connect an Azure DevOps repository, you must first create a new personal access token (PAT) token in Azure DevOps.
Afterward, you must create a new branch, enter the connection details, and merge the open pull request in Reunite.

## Create a new access token in Azure DevOps

### Permissions

Before creating Personal Access Token (PAT) for your user, make sure that they have a correct access right to the desired Azure projects.
Redocly recommends putting your user in the `Project Administrators` security group for your Azure DevOps project, since this security group has all the needed permissions by default.

*(For example, only the `Project Administrators` security group has the `View subscriptions` and the `Edit subscriptions` permissions enabled [by default](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops#q-what-permissions-do-i-need-to-set-up-a-subscription).
Redocly needs these permissions to be able to setup service hooks (webhooks) for the Azure project.)*

Screenshot with Azure user security group for project
Alternatively, you can put your user in the `Project Contributors` security group and add the `View subscriptions` and the `Edit subscriptions` permissions manually.
See [Manage permissions with command line tool](https://learn.microsoft.com/en-us/azure/devops/organizations/security/manage-tokens-namespaces?view=azure-devops)
or [Security REST API](https://learn.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-7.1) in Microsoft Azure DevOps documentation for detailed instructions.

### PAT scopes

Before you enter the connection details in Redocly, you need to create and copy a new PAT for your account in Azure DevOps.
Redocly uses this access token to establish a connection to your repository.

See [Create a PAT](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?#create-a-pat) in Microsoft Azure DevOps documentation for detailed instructions.

You must select an Organization for this PAT.
Do not select **All accessible organizations**.

Also, the PAT you use must have API scopes defined. You can choose the **Full access** option, or select **Custom defined** and enable the following specific scopes:

- Code: `Read, write, & manage` and `Status`


The following screenshot from Azure DevOps shows the required custom defined scopes:

Screenshot with Azure scopes
Reunite requires:

- **Code -> Read** (`vso.code`) scope for all read operations in Reunite *(list of repositories, branches, files, file contents, diffs, list of PRs, etc.)*.
- **Code -> Write** (`vso.code_write`) scope for all write operations in Reunite *(create/update Pull Requests, remove branches, synchronize remote content)*.
- **Code -> Manage** (`vso.code_manage`) scope for creating new code repositories from Reunite app.
- **Code -> Status** (`vso.code_status`) scope for setting commit and PR statuses *(Lint status, Build status, Link checker status, Visual review)*.


See [Scopes](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?#create-a-pat) in Microsoft Azure DevOps documentation for detailed information about scopes permissions.

details
summary
Detailed list of all resources that Reunite uses from Azure API and their required scopes:
| Resource | Auth Type | Scopes | Description |
|  --- | --- | --- | --- |
| [Repositories - List](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/list?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get repositories list |
| [Repositories - Get Repository](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/get-repository?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get repository metadata |
| [Stats - List](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/stats/list?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get branch list |
| [Refs - Update Refs](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/refs/update-refs?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To delete branches |
| [Items - List](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/items/list?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get folders list and PR templates list |
| [Items - Get](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/items/get?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get PR template content |
| [Commits - Get](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/commits/get?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get commit details |
| [Merge Bases - List](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/merge-bases/list?view=azure-devops-rest-7.1) | PAT | `vso.code` | To find the merge bases of two commits |
| [Diffs - Get](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/diffs/get?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get diff between commits |
| [Statuses - List](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/statuses/list?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code`, `vso.code_status` | To get existing commit statuses |
| [Statuses - Create](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/statuses/create?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code_write`, `vso.code_status` | To set commit statuses (for deployments and scorecards) |
| [Pull Requests - Get Pull Requests](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-requests/get-pull-requests?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get pull requests list |
| [Pull Requests - Get Pull Request](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-requests/get-pull-request?view=azure-devops-rest-7.1) | OAuth2 | `vso.code` | To get details about a specific pull request |
| [Pull Requests - Create](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-requests/create?view=azure-devops-rest-7.1&tabs=HTTP) | OAuth2 | `vso.code` | To create a new pull request |
| [Pull Requests - Update](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-requests/update?view=azure-devops-rest-7.1) | OAuth2 | `vso.code` | To manage existing pull requests (merge, close, reopen, etc.) |
| [Pull Request Statuses - Create](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-request-statuses/create?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code_write`, `vso.code_status` | To set pull request statuses |
| [Policy Configurations - Get](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/policy-configurations/get?view=azure-devops-rest-7.1) | OAuth2 | `vso.code` | To get configurations for merge strategies |
| [Subscriptions - List](https://learn.microsoft.com/en-us/rest/api/azure/devops/hooks/subscriptions/list?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To get a list of existing project subscriptions (webhooks) |
| [Subscriptions - Create](https://learn.microsoft.com/en-us/rest/api/azure/devops/hooks/subscriptions/create?view=azure-devops-rest-7.1&tabs=HTTP) | PAT | `vso.code` | To create a new project subscription (webhook) |
| [Profiles - Get](https://learn.microsoft.com/en-us/rest/api/azure/devops/profile/profiles/get?view=azure-devops-rest-7.1&tabs=HTTP) | OAuth2 | `vso.profile` | To get user display name |


> Note:


- Push and pull Git actions are performed using PAT.
- Redocly uses `https://dev.azure.com/{organization}/_apis/connectionData` endpoint to verify if the user is authorized.


## Create a new branch in Reunite

Before you make any changes to your project, create a new branch.
This new branch is a place where you can make changes without affecting the published site until you are ready.
After you have iterated on your changes based on reviews by your team and the updates have been approved, you can merge your changes into the published site.

To create a new branch:

1. From the Reunite editor, click the name of the current branch at the top of the page.

2. Enter the name for your new branch, for example `new-dev-branch`, and select **Create branch**.
Reunite automatically replaces spaces with hyphens `-`because spaces are not allowed in branch names.


## Enter the connection details in Reunite

After you have created a new branch in Reunite, you can add remote content to your project in Reunite using the connection details you have collected from Azure DevOps.

To enter the connection details in Reunite:

1. In the file tree, select the folder (or click on the empty space to select the root directory) where you want to add the remote content.
2. Select **+ > New remote folder > Add Git repository** to add a remote content folder, or **+ > New remote file > Add Git repository** to add a remote content file.
3. Enter a name for the new remote content (folder or file) and press the Enter or Return key.
4. Select **Azure DevOps Services**.
5. Enter a **Credential name** that identifies this Azure DevOps Services connection.
6. Enter the **Access token** you saved from the [Create a new access token in Azure DevOps](#create-a-new-access-token-in-azure-devops) step.
7. Enter the **Organization name** where you created the access token and select **Next**.
8. Select your **Organization > Repository > Branch**.
9. (Optional) Select the [**Folder**](/docs/realm/reunite/project/remote-content/remote-content#remote-contents-repository-folder) or [**File**](/docs/realm/reunite/project/remote-content/remote-content#remote-contents-repository-file), depending on whether you are adding a remote folder or a remote file.
10. (Optional) Click the [**Auto-sync**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) or [**Auto-merge**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) toggles to turn off either option.
11. (Optional) Select the [**Auto-sync**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) or [**Auto-merge**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) toggles to turn off either option.
12. Select **Add remote**.
This action opens a pull request in Reunite automatically.


You can click the **View Pull Request** button next to your new branch name to view the pull request.

## Merge the open pull request in Reunite

After you enter the connection details in Redocly, a pull request to merge your updates with the default branch opens.
When you merge the pull request your changes are added to your main branch and a production deployment is triggered.

To merge the open pull request in Reunite:

1. Select the **View Pull Request** button next to your branch name.
2. Review your updates in the **Review** tab.
3. After the tests have run and your pull request has been approved, click the **Merge** button to merge your updates with the default branch.


## Resources

- **[Connect a Git provider](/docs/realm/reunite/project/connect-git/connect-git-provider)** - Connect entire Azure DevOps repositories to your project for comprehensive version control and automated deployment pipelines
- **[Use the Editor](/docs/realm/reunite/project/use-editor)** - Explore Reunite's collaborative editing environment for creating content with Azure DevOps remote content integration and team workflows
- **[Projects overview](/docs/realm/reunite/project/projects)** - Access feedback, deployment details, and project settings for Azure DevOps remote content-enabled documentation projects
- **[Configuration reference](/docs/realm/config)** - Complete redocly.yaml configuration options for Azure DevOps remote content integration and project customization