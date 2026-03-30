# Source: https://northflank.com/docs/v1/application/build/build-code-from-a-self-hosted-vcs.md

# Build code from a self-hosted VCS

Teams can add their own self-hosted version control systems (VCS) to Northflank and build from repositories as with any other Git provider linked to the account.

Northflank currently supports GitLab Enterprise/Community Edition.

> [!note] 
> [Click here](https://app.northflank.com/s/account/integrations/vcs) to link a git service.

## Add a self-hosted VCS

To add a self-hosted VCS navigate to the Git section, underneath integrations on the team settings page, click 'add a self-hosted VCS' and select the type of VCS you would like to integrate. Follow the application specific instructions to integrate your self-hosted VCS. You can choose how team members can access the repositories on the self-hosted VCS after adding it to Northflank.

### Add a self-hosted GitLab instance

Navigate to your GitLab service and create a new OAuth application at `[YOUR URL]/profile/applications` or `[YOUR URL]/admin/applications` if you are an administrator. Give the application the `api` scope and set the `Redirect URI` as specified on Northflank.

On Northflank enter the root domain of your self-hosted GitLab, e.g. `gitlab.yourdomain.com`, the `application ID` and the `secret` from the OAuth application.

## Learn more

Read more about [managing self-hosted VCS services](https://northflank.com/docs/v1/application/collaborate/manage-git-integrations#self-hosted-vcs-settings).

- [Add a self-hosted VCS: Add your own self-hosted Git provider and build from its repositories.](/v1/application/collaborate/manage-git-integrations#add-a-self-hosted-vcs)
- [Build from a Git repository: Start building from your linked Git repositories in minutes.](/v1/application/build/build-code-from-a-git-repository)
