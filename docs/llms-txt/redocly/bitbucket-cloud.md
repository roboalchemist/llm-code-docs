# Source: https://redocly.com/docs/realm/reunite/project/connect-git/bitbucket-cloud.md

# Connect a Bitbucket Cloud repo

If your project files are stored in a remote repository on Bitbucket Cloud, you can connect that repository, so you can access, edit, and publish those files in Reunite.

To connect a Bitbucket Cloud repository, you must first create a new access token in Bitbucket Cloud, then enter the connection details in Reunite.

## Create a new repository access token in Bitbucket Cloud

Before entering the connection details in Reunite, you need to create and copy a new repository access token for your account in Bitbucket Cloud.
Redocly uses this access token to establish a connection to your repository.
The access token you use needs to have `repository:write`, `pullrequest:write` and `webhook` scopes.

See the Bitbucket Cloud documentation for creating the following access token types with appropriate permissions and scopes:

- [Create a repository access token](https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-access-token/)
- [Repository Access Token permissions](https://support.atlassian.com/bitbucket-cloud/docs/repository-access-token-permissions/)


## Enter the connection details in Redocly

1. From your project, select **Settings > Git hosting**.
2. From the list of Git providers, select **Bitbucket Cloud**.
3. Enter a **Credential name** for the new Bitbucket Cloud credential.
4. Enter the **Workspace name** of the Bitbucket Cloud Workspace and select **Next**.
5. Enter the **Access token** you saved from the [Create a new repository access token in Bitbucket Cloud](#create-a-new-repository-access-token-in-bitbucket-cloud) step and select **Next**.
6. Select the **Namespace > Project > Branch**.
7. (Optional) Select the **Monorepo folder**, if your project files are part of a monorepo, and you want to include only a specific folder from the repository.
If you select to only include a specific folder from a monorepo:
  - Only files listed in file tree are cloned, no other files are included
  - Project builds are started only when branch contains changes to connected folder
  - Remote content can only be added to the connected folder.
8. Select **Next > Connect**.
**This step deletes the files currently in the Redocly project and replaces them with the files in Bitbucket Cloud.**


## Resources

- **[Include remote content](/docs/realm/reunite/project/remote-content)** - Integrate content from external Bitbucket repositories into your Reunite projects for streamlined documentation workflows
- **[Use the Editor](/docs/realm/reunite/project/use-editor)** - Leverage Reunite's collaborative editing tools for content creation with Bitbucket integration and team collaboration features
- **[Projects overview](/docs/realm/reunite/project/projects)** - Manage feedback, deployment details, and project settings for Bitbucket-connected documentation projects
- **[Configuration reference](/docs/realm/config)** - Complete redocly.yaml configuration options for Bitbucket integration, automated deployment, and project customization