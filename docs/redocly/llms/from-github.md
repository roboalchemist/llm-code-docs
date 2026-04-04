# Source: https://redocly.com/docs/realm/reunite/project/remote-content/from-github.md

# Add remote files from GitHub

If your content is stored in a repository on GitHub, you can connect that repository, so you can access and publish those files in Reunite.

To connect a GitHub repository, you must first install the Redocly app in GitHub.
Afterward, you must create a new branch, enter the connection details, and merge the open pull request in Reunite.

## Install the Redocly app in GitHub

Before you enter the GitHub repository connection details in Reunite, you must install the Redocly GitHub App on your organization in GitHub.

To install the Redocly GitHub App on your organization in GitHub:

1. Navigate to [Install Redocly](https://github.com/apps/redocly/installations/select_target), and select the organization on GitHub.
2. Enter your GitHub password to confirm access.
3. Grant the Redocly GitHub App access to your project's repository.


See [Installing a GitHub App from a third party](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) in the GitHub documentation for more information.

## Create a new branch in Reunite

Before you make any changes to your project, create a new branch.
This new branch is a place where you can make changes without affecting the published site until you are ready.
After you have iterated on your changes based on reviews by your team and the updates have been approved, you can merge your changes into the published site.

To create a new branch:

1. From the Reunite editor, click the name of the current branch at the top of the page.

2. Enter the name for your new branch, for example `new-dev-branch`, and select **Create branch**.
Reunite automatically replaces spaces with hyphens `-`because spaces are not allowed in branch names.


## Enter the connection details in Reunite

After you install the Redocly GitHub App on your organization in GitHub, and create a new branch, you can enter the connection details in Reunite.

To enter the connection details in Reunite:

1. In the file tree, select the folder (or click on the empty space to select the root directory) where you want to add the remote content.
2. Select **+ > New remote folder > Add Git repository** to add a remote content folder, or **+ > New remote file > Add Git repository** to add a remote content file.
3. Enter a name for the new remote content (folder or file) and press the Enter or Return key.
4. Select **GitHub > Next**.
5. Authorize your Redocly organization to verify your GitHub identity.
6. Select your GitHub **Organization > Repository > Branch**.
7. (Optional) Select the [**Folder**](/docs/realm/reunite/project/remote-content/remote-content#remote-contents-repository-folder) or [**File**](/docs/realm/reunite/project/remote-content/remote-content#remote-contents-repository-file), depending on whether you are adding a remote folder or a remote file.
8. (Optional) Select the [**Auto-sync**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) or [**Auto-merge**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) toggles to turn off either option.
9. Select **Add remote**.
This action opens a pull request in Reunite automatically.


You can click the **View Pull Request** button next to your new branch name to view the pull request.

## Merge the open pull request in Reunite

After you enter the connection details in Reunite, a pull request to merge your updates with the default branch opens.
When you merge the pull request your changes are added to your main branch and a production deployment is triggered.

To merge the open pull request in Reunite:

1. Select the **View Pull Request** button next to your branch name.
2. Review your updates in the **Review** tab.
3. After the tests have run and your pull request has been approved, click the **Merge** button to merge your updates with the default branch.


## Resources

- **[Connect a Git provider](/docs/realm/reunite/project/connect-git/connect-git-provider)** - Connect entire GitHub repositories to your project for comprehensive version control and automated workflows
- **[Use the Editor](/docs/realm/reunite/project/use-editor)** - Explore Reunite's collaborative editing tools for creating and managing content with GitHub remote content integration
- **[Projects overview](/docs/realm/reunite/project/projects)** - Access feedback, deployment details, and project settings for GitHub remote content-enabled documentation projects
- **[Configuration reference](/docs/realm/config)** - Complete redocly.yaml configuration options for GitHub remote content integration and project customization