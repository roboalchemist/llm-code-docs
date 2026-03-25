# Source: https://redocly.com/docs/realm/reunite/project/remote-content/from-gitlab.md

# Add remote files from GitLab

If your project files are stored in a remote repository on GitLab, you can connect that repository, so you can access and publish those files in Redocly.

To connect a GitLab repository, you must first create a new access token in GitLab.
Afterward, you must create a new branch, enter the connection details, and merge the open pull request in Reunite.

## Create a new access token in GitLab

Before entering the connection details in Reunite, you need to create and copy a new access token for your account in GitLab.
Redocly uses this access token to establish a connection to your repository.
GitLab offers multiple types of access tokens.
The access token you use needs to have `api` scope and at least `Maintainer` role.

See the GitLab documentation for creating the following access token types with the API scope option:

- [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)
- [Create a project access token](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html#create-a-project-access-token)


## Create a new branch in Reunite

Before you make any changes to your project, create a new branch.
This new branch is a place where you can make changes without affecting the published site until you are ready.
After you have iterated on your changes based on reviews by your team and the updates have been approved, you can merge your changes into the published site.

To create a new branch:

1. From the Reunite editor, click the name of the current branch at the top of the page.

2. Enter the name for your new branch, for example `new-dev-branch`, and select **Create branch**.
Reunite automatically replaces spaces with hyphens `-`because spaces are not allowed in branch names.


## Enter the connection details in Reunite

After you have created a new branch in Reunite, you can add remote content to your project in Reunite using the connection details you have collected from GitLab.

To enter the connection details in Reunite:

1. In the file tree, select the folder (or click on the empty space to select the root directory) where you want to add the remote content.
2. Select **+ > New remote folder > Add Git repository** to add a remote content folder, or **+ > New remote file > Add Git repository** to add a remote content file.
3. Enter a name for the new remote content (folder or file) and press the Enter or Return key.
4. From the list of Git providers, select **GitLab** or a self-managed GitLab instance.
5. Enter a **Credential name** for the new GitLab credential.
6. Enter the **Access token** you saved from the [Create a new access token in GitLab](#create-a-new-access-token-in-gitlab) step and select **Next**.
7. Select the **Namespace > Project > Branch**.
8. (Optional) Select the [**Folder**](/docs/realm/reunite/project/remote-content/remote-content#remote-contents-repository-folder) or [**File**](/docs/realm/reunite/project/remote-content/remote-content#remote-contents-repository-file), depending on whether you are adding a remote folder or a remote file.
9. (Optional) Select the [**Auto-sync**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) or [**Auto-merge**](/docs/realm/reunite/project/remote-content/remote-content#auto-sync-and-auto-merge) toggles to turn off either option.
10. Select **Add remote**.
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

- **[Connect a Git provider](/docs/realm/reunite/project/connect-git/connect-git-provider)** - Connect entire GitLab repositories to your project for comprehensive version control and automated documentation workflows
- **[Use the Editor](/docs/realm/reunite/project/use-editor)** - Leverage Reunite's collaborative editing environment for creating content with GitLab remote content integration and team collaboration
- **[Projects overview](/docs/realm/reunite/project/projects)** - Manage feedback, deployment details, and project settings for GitLab remote content-enabled documentation projects
- **[Configuration reference](/docs/realm/config)** - Complete redocly.yaml configuration options for GitLab remote content integration and project customization