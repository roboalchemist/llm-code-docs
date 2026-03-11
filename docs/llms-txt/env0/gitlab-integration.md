# Source: https://docs.envzero.com/guides/admin-guide/templates/gitlab-integration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Standard Gitlab Integration

> Connect GitLab repositories to env zero using OAuth or access tokens for template creation and deployments

<Info>
  **Note**

  In order to integrate with GitLab, you need to have a GitLab user with Maintainer/Owner permissions on the necessary GitLab Project. We highly recommend that the user be a designated shared bot user, as env zero would perform actions as this user on the project/repository.

  <Info>
    If you do not have those permissions, please ask an admin or a different user with those permissions to create the template.

    If you are using a Personal or a Group Access Tokens, you will need to have the permissions to create those in the relevant GitLab Project.
  </Info>
</Info>

## New Template

If you would like to create the first GitLab Integrated Template in this env zero organization, please see **[Create Your First Template](/guides/getting-started/getting-started/create-your-first-template)** instead.

1. Click **ADD A NEW TEMPLATE** on the top right in the *Templates* screen.
2. Pick your template type, enter a name for the template, and then click on **NEXT**
3. Click on the **GitLab.com** button. Since you have already created a GitLab template in this env zero organization, there is no need for further authentication with Gitlab.
4. Select one of the following authentication types:
   1. **OAuth**
      1. Pick which user you want to authenticate as, out of the users in your organization that have already authorized the env zero GitLab app.
      2. After picking the user, you'll be able to pick a project from the GitLab Projects accessible to that user.
   2. **Access Token**
      1. Click on Access Token and either select an existing token or create a new one.
      2. Creating a token:
         1. The token can be either a [Personal](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) or a [Group](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html) Access Token.
         2. The token must have access to each repository you would like to be able to use with env zero.
         3. For each project, the user should have at least Maintainer/Owner permissions.
         4. The token must have the `read_repository` and `api` scopes defined.
5. After picking the user/token, you'll be able to pick a project from the accessible GitLab Projects.
6. If you would like to pull the code from a specific revision or branch, enter that in the `Revision` field. Leaving this field empty will use your default branch, which is usually “master”/"main".
7. Enter the folder your Terraform files are located in under `Terraform Folder`. If your Terraform files are in the root of the repository, leave this empty.
8. Click on **NEXT** to proceed to the variables section
9. Add environment and terraform variables that you'd like to be used during deployment, and then click on **NEXT** to go to the final "Projects" section
10. Pick the projects that you'd like to have access to deploy this template, and then click on **DONE** to create the template.

<Warning>
  Troubleshoot

* Can't find your repository? Check if your Authorized User has access to the necessary GitLab project. In order to authorize as a new GitLab user, please log out of GitLab on your browser, and then click on "authorize another GitLab user"
</Warning>

## Existing Template

If you would like to integrate an existing template with GitLab:

1. Go to the **Templates** screen, and click on **Settings** for the template you would like to integrate with GitLab.
2. Click on the **VCS** step. From there you can click on the **GitLab.com** button, and integrate with GitLab as you would for a new template.

<Info>
  Additional Content

* [Managing Terraform variable hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)
* [Why env zero is a Terraform Cloud alternative?](https://www.env0.com/alternatives/terraform-cloud-alternative)
</Info>

Built with [Mintlify](https://mintlify.com).
