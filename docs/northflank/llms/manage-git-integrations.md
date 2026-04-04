# Source: https://northflank.com/docs/v1/application/collaborate/manage-git-integrations.md

# Manage Git integrations

Teams can link multiple accounts per Git service and self-hosted VCS.

> [!note] 
> [Click here](https://app.northflank.com/s/account/integrations/vcs) to view your Git namespaces.

![The Git integrations page on a team account in the Northflank application, showing a self-hosted VCS](https://assets.northflank.com/documentation/v1/application/collaborate/manage-git-integrations/team-git-page.png)

## Add a Git account

To add a Git account to your team account, navigate to the Git section under integrations in the team dashboard and click  link on the relevant service. For GitHub you will be asked which account to link, for all other services the currently-logged-in account will be added.
Team users must have the manage Git permission on one of their assigned roles to add or remove accounts.

## Add a self-hosted VCS

To add a self-hosted VCS navigate to the Git section, underneath integrations on the team settings page, click 'add a self-hosted VCS' and select the type of VCS you would like to integrate. Follow the application specific instructions to integrate your self-hosted VCS. You can choose how team members can access the repositories on the self-hosted VCS after adding it to Northflank.

### Add a self-hosted GitLab instance

Navigate to your GitLab service and create a new OAuth application at `[YOUR URL]/profile/applications` or `[YOUR URL]/admin/applications` if you are an administrator. Give the application the `api` scope and set the `Redirect URI` as specified on Northflank.

On Northflank enter the root domain of your self-hosted GitLab, e.g. `gitlab.yourdomain.com`, the `application ID` and the `secret` from the OAuth application.

## Self-hosted VCS settings

Settings for a self-hosted VCS can be configured by navigating to the team account's Git integrations page and clicking the options button  on the card for the self-hosted VCS.

#### Personal & team use

Select personal use to allow team members to use the self-hosted VCS to build and run from the repositories on this service in their user account's projects as well as in team projects. Team members will need to link their account on the VCS service to Northflank in their own user account settings.

Select team use only to only allow team members to build and run from the repositories on this service in team projects.

#### Application configuration

You can update the `VCS provider URL`, `application ID` and `secret` from the OAuth application.

## Restrict namespaces

On team accounts you may need to restrict access to certain namespaces on your linked Git accounts.

GitHub account restrictions are managed on GitHub by selecting which account/organisation to install the Northflank GitHub app on, and then granting access to specific repositories on that account.

Your linked GitLab and Bitbucket accounts can be restricted to certain namespaces by opening the settings on the respective entry. Select restricted and pick the contexts you want your team members to access. Remove a namespace from the list to revoke access. The namespaces available to your team will be displayed on the git integrations page in the section for the relevant service.
Remove a namespace from the list in the selected account to revoke access.

New namespaces can be created in your Gitlab and Bitbucket accounts by creating new projects.

### Restrict self-hosted VCS access

You can restrict access to the repositories in your self-hosted VCS by selecting specific owners within the self-hosted VCS's settings. Team members will be able to build and run from repositories belonging to the selected namespaces, if your account has access to them.

Unrestricted access means team members will be able to create services and jobs from every repository that the linked account can access.

## Next steps

- [Build from a Git repository: Start building from your linked Git repositories in minutes.](/v1/application/build/build-code-from-a-git-repository)
- [Run an image continuously: Deploy a built image as a continuously-running service.](/v1/application/run/run-an-image-continuously)
