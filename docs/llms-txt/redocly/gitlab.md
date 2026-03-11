# Source: https://redocly.com/docs/realm/reunite/project/connect-git/self-hosted/gitlab.md

# Source: https://redocly.com/docs/realm/reunite/project/connect-git/gitlab.md

# Connect a GitLab repo

If your project files are stored in a remote repository on GitLab, you can connect that repository, so you can access, edit, and publish those files in Reunite.

To connect a GitLab repository, you must first create a new access token in GitLab, then enter the connection details in Reunite.

## Create a new access token in GitLab

Before entering the connection details in Reunite, you need to create and copy a new access token for your account in GitLab.
Redocly uses this access token to establish a connection to your repository.
GitLab offers multiple types of access tokens.
The access token you use needs to have `api` scope and at least `Maintainer` role.

See the GitLab documentation for creating the following access token types with the API scope option:

- [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)
- [Create a project access token](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html#create-a-project-access-token)


## Enter the connection details in Redocly

1. From your project, select **Settings > Git hosting**.
2. From the list of Git providers, select **GitLab** or a self-managed GitLab instance.
For more information, see [Manage self-hosted Git providers in Reunite](/docs/realm/reunite/project/connect-git/self-hosted/gitlab)
3. Enter a **Credential name** for the new GitLab credential.
4. Enter the **Access token** you saved from the [Create new access token in GitLab](#create-a-new-access-token-in-gitlab) step and select **Next**.
5. Select the **Namespace > Project > Branch**.
6. (Optional) Select the **Monorepo folder**, if your project files are part of a monorepo, and you want to include only a specific folder from the repository.
If you select to only include a specific folder from a monorepo:
  - Only files listed in file tree are cloned, no other files are included
  - Project builds are started only when branch contains changes to connected folder
  - Remote content is allowed to add to connected folder only
7. Select **Next > Connect**.
**This step deletes the files currently in the Redocly project and replaces them with the files in GitLab.**


## Resources

- **[Include remote content](/docs/realm/reunite/project/remote-content)** - Integrate content from external GitLab repositories into your Reunite projects for streamlined documentation workflows
- **[Use the Editor](/docs/realm/reunite/project/use-editor)** - Leverage Reunite's collaborative editing tools for content creation with GitLab repository integration and version control
- **[Projects overview](/docs/realm/reunite/project/projects)** - Manage feedback, deployment details, and project settings for GitLab-connected documentation projects
- **[Configuration reference](/docs/realm/config)** - Complete redocly.yaml configuration options for GitLab integration, automated deployment, and project customization