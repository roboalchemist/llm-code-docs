# Source: https://docs.aws.amazon.com/codecatalyst/latest/userguide/llms.txt

# Amazon CodeCatalyst User Guide

> Amazon CodeCatalyst is a cloud-based collaboration space for software development teams which provides one place where you can plan work, collaborate on code, and build, test, and deploy applications with continuous integration/continuous delivery (CI/CD) tools.

- [What is Amazon CodeCatalyst?](https://docs.aws.amazon.com/codecatalyst/latest/userguide/welcome.html)
- [How to migrate from CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html)
- [Concepts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/concepts.html)
- [Search for code, issues, projects, and users](https://docs.aws.amazon.com/codecatalyst/latest/userguide/search.html)
- [Understanding current service status with the CodeCatalyst health report](https://docs.aws.amazon.com/codecatalyst/latest/userguide/health-dashboard.html)
- [Quotas](https://docs.aws.amazon.com/codecatalyst/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/codecatalyst/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/codecatalyst/latest/userguide/glossary.html)

## [Set up and sign in to CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/setting-up-topnode.html)

- [Creating a new space and development role (starting without an invitation)](https://docs.aws.amazon.com/codecatalyst/latest/userguide/sign-up-create-resources.html): Learn how to sign up for Amazon CodeCatalyst and create your first space and your development role.
- [Accepting an invitation and creating an AWS Builder ID](https://docs.aws.amazon.com/codecatalyst/latest/userguide/sign-up-sign-in.html): Learn how to sign in to Amazon CodeCatalyst for the first time as part of accepting an invitation to a project or space.
- [Signing in with an AWS Builder ID](https://docs.aws.amazon.com/codecatalyst/latest/userguide/id-how-to-sign-in.html): Learn how to sign in to the CodeCatalyst console as a returning user.
- [Signing in with SSO](https://docs.aws.amazon.com/codecatalyst/latest/userguide/sign-in-sso.html): Learn how to sign in to the CodeCatalyst console with SSO.
- [Viewing all spaces and projects for a user](https://docs.aws.amazon.com/codecatalyst/latest/userguide/home.html): You can view a listing of your spaces and projects on the user home page.

### [Viewing and managing CodeCatalyst profiles](https://docs.aws.amazon.com/codecatalyst/latest/userguide/view-profiles.html)

You can view user profiles in Amazon CodeCatalyst to get information such as email addresses and CodeCatalyst aliases.

- [Updating a profile](https://docs.aws.amazon.com/codecatalyst/latest/userguide/your-profile.html): Learn about profiles in Amazon CodeCatalyst.
- [Changing a CodeCatalyst password associated with an AWS Builder ID](https://docs.aws.amazon.com/codecatalyst/latest/userguide/id-change-password.html): Use the following instructions to change the Amazon CodeCatalyst password associated with your AWS Builder ID.
- [Setting up to use the AWS CLI with CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html): Learn how to configure the AWS CLI to use with CodeCatalyst commands.


## [Getting started tutorials](https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-topnode.html)

- [Tutorial: Creating a project with the Modern three-tier web application blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-template-project.html): Learn how to create a project using a blueprint in Amazon CodeCatalyst.
- [Tutorial: Starting with an empty project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-blank-template.html): Learn how to create an empty project and add resources to it.
- [Tutorial: Using generative AI features](https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-project-assistance.html): Learn how to use the generative AI features included in Amazon CodeCatalyst to help you make progress in your projects.


## [Organize resources with spaces](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces.html)

- [Creating a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-create.html): Learn how to create additional spaces in CodeCatalyst.
- [Editing a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-edit.html): Learn how to edit a space description in CodeCatalyst.
- [Deleting a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-delete.html): Learn how to delete a space in CodeCatalyst.
- [Monitoring activity for users and resources in a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-activity.html): To see recently created projects and status updates, you can use the CodeCatalyst console to view an activity feed that shows updates for space resources.

### [Allowing access to AWS resources with connected AWS accounts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account.html)

Learn how to connect AWS accounts to a space in CodeCatalyst.

- [Adding an AWS account to a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account-create.html): Learn how to add an AWS account to a space in CodeCatalyst.
- [Adding IAM roles to account connections](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account-addroles.html): Part of creating your account connection includes adding the IAM role or roles you want to use with projects in your CodeCatalyst space.
- [Adding the account connection and IAM roles to your deploy environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account-addroles-env.html): To access AWS resources, such as Amazon ECS or AWS Lambda resources for deployments, CodeCatalyst build and deploy actions require IAM roles with permissions to access those resources.
- [Viewing account connections](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account-list.html): You can view a list of your connections and view details about each connection.
- [Deleting account connections (in CodeCatalyst)](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-connect-account-delete.html): You can delete an account connection that you no longer need.
- [Configuring a billing account for a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/connect-account-billing-ref.html): A billing account must be designated for your CodeCatalyst space, even if usage for the space will not exceed the Free tier.
- [Configuring IAM roles for connected accounts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-manage-roles.html): You create roles in AWS Identity and Access Management (IAM) for the account that you want to add to CodeCatalyst.

### [Granting users space permissions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members.html)

Learn how to manage space users and their permissions in CodeCatalyst.

- [Viewing members in a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members-view.html): You can view the users in your space, including information about their display names, aliases, and the role they have for the space.
- [Inviting a user directly to a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members-add-admin.html): You can invite users directly to your CodeCatalyst space.
- [Canceling an invitation for a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members-cancel-invite.html): If you want to cancel an invitation to join a space that you sent recently, and it has not yet been accepted, you can cancel it.
- [Changing the role for a space member](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members-rolechange.html): You can change the assigned role for a member of your space.
- [Removing a space member](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members-remove-member.html): You can remove a member of your space when they do not need to access any of the space resources.
- [Removing or changing the role for a user with the Space administrator role](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-members-remove.html): You can remove or change the role for a user with the Space administrator role for your space.

### [Allowing space access using teams](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams.html)

Learn about the steps you must perform to manage teams for your CodeCatalyst space.

- [Creating a team](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-create.html): A team can have role permissions, such as Power user, in a space.
- [Viewing a team](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-view.html): In CodeCatalyst, you can view the projects and roles for your team.
- [Granting space roles for a team](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-space-roles.html): Teams are a way to group users so that you can grant and manage team access to projects in CodeCatalyst.
- [Granting project roles for a team at the space level](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-project-roles.html): A team in CodeCatalyst is similar to a user in that the team members can have role permissions, such as Project administrator, in a project.
- [Adding a user to a team directly](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-add-users.html): You can add team members to your team.
- [Removing a user from a team directly](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-remove-users.html): You can remove team members from your team.
- [Adding an SSO group to a team](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-add-sso.html): If your space is configured as a space with SSO users and groups managed in IAM Identity Center, you can add an SSO group that will join the space as a separate team.
- [Deleting a team](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-teams-delete.html): You can delete a team that you no longer need.

### [Allowing space access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-machine-resources.html)

Learn about the steps you must perform to manage machine resources for a CodeCatalyst space.

- [Viewing space access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-machine-resources-view.html): You can view a listing of the machine resources that are in use in your space.
- [Disabling space access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-machine-resources-disable.html): You can choose to disable machine resources that are in use in your space.
- [Enabling space access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/managing-machine-resources-enable.html): You can choose to enable machine resources that are in use in your space and that have been disabled.

### [Administering Dev Environments for a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-devenv.html)

All Dev Environments are created as part of a project within a space.

- [Viewing Dev Environments for your space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-devenv-view.html): You can view the type, status, and details for all Dev Environments in your space.
- [Editing a Dev Environment for your space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-devenv-edit.html): You can edit the configuration for a Dev Environment, such as the configured length of timeout, if any, for an idle Dev Environment to stop running.
- [Stopping a Dev Environment for your space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-devenv-stop.html): You can stop a running Dev Environment before it becomes idle if the Dev Environment is configured to have a timeout.
- [Deleting a Dev Environment for your space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-devenv-delete.html): You can delete a Dev Environment that is no longer needed or that no longer has an owner.
- [Quotas for spaces](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-quotas-limits.html): Learn about the quotas and limits for spaces in CodeCatalyst.


## [Organize work with projects](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects.html)

- [Creating a project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-create.html): Learn how to create a project in CodeCatalyst.

### [Getting a list of projects](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-view.html)

Learn about viewing a project in CodeCatalyst.

- [Viewing all projects in a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-view-overview.html): In the Projects list for your space, you can view all projects where you have permissions.
- [Deleting a project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-delete.html): You can delete a project to remove all access to the project's resources.
- [Granting users project permissions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-members.html): Learn about how to add and remove members to and from projects in Amazon CodeCatalyst, and how to use invitations.

### [Allowing project access using teams](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-teams.html)

Learn about the steps you must perform to manage teams for your CodeCatalyst project.

- [Adding a team to a project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-teams-add.html): You can manage teams where the team members can access resources in your project.
- [Granting project roles for a team](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-teams-project-roles.html): A team can have role permissions, such as Power user, in a space.
- [Removing a project role for a team](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-teams-remove.html): In CodeCatalyst, you can view the project roles for your team.

### [Allowing project access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-machine-resources.html)

Learn about the steps you must perform to manage machine resources for your CodeCatalyst project.

- [Viewing project access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-machine-resources-view.html): You can view a listing of the machine resources that are in use in your project.
- [Disabling project access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-machine-resources-disable.html): You can choose to disable machine resources that are in use in your project.
- [Enabling project access for machine resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-machine-resources-enable.html): You can choose to enable machine resources that are in use in your project and that have been disabled.
- [Quotas for projects](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-quotas.html): Learn about the quotas and limits for projects in CodeCatalyst.

### [Sending notifications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications.html)

Learn about using notifications to monitor your projects and resources in Amazon CodeCatalyst.

- [How do notifications work?](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications-concepts.html): Learn how notifications work in CodeCatalyst.
- [Getting started with Slack notifications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-notifications.html): Learn how to use Slack to get notified of changes to your CodeCatalyst projects.

### [Sending Slack and email notifications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications-manage.html)

Learn how to manage, configure, and customize notifications in Amazon CodeCatalyst.

- [Configuring email notifications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications-personal.html): Learn how to manage, configure, and customize email notifications from Amazon CodeCatalyst.
- [Sending notifications to Slack channels](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications-projects.html): Learn how to add, edit, and remove Slack channels in Amazon CodeCatalyst.
- [Configuring Slack direct messages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications-personal-slack.html): Learn how to manage, configure, and customize direct messages from Amazon CodeCatalyst.
- [Editing notifications for a notification channel](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications-edit.html): You can change which channels notifications go to, and you can turn off specific notifications altogether.
- [Removing a channel](https://docs.aws.amazon.com/codecatalyst/latest/userguide/notifications-remove-channel.html): You can remove a Slack channel from Amazon CodeCatalyst.


## [Set up projects with blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/blueprints.html)

- [Creating a project with a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/create-project-with-bp.html): Learn how to create a project with a blueprint from the Amazon CodeCatalyst catalog or your space's blueprints catalog.
- [Adding a blueprint in a project to integrate resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/apply-bp.html): Learn how to add a blueprint to a CodeCatalyst project.
- [Disassociating a blueprint from a project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/disassociate-bp.html): If you don't want new updates from a blueprint, you can disassociate the blueprint from your project.
- [Changing blueprint versions in a project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/update-bp.html): Learn how to change a blueprint's version in your Amazon CodeCatalyst project.
- [Editing a desciption for a blueprint in a project](https://docs.aws.amazon.com/codecatalyst/latest/userguide/update-settings-bp.html): Learn how to edit a blueprint's alias after it's applied to your Amazon CodeCatalyst project.
- [Working with lifecycle management as a blueprint user](https://docs.aws.amazon.com/codecatalyst/latest/userguide/lifecycle-management-user.html): Learn about the lifecycle management for projects using blueprints in your Amazon CodeCatalyst space.
- [Creating a comprehensive project with blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/project-blueprints.html): Learn about the project blueprints available in Amazon CodeCatalyst.

### [Standardizing projects with custom blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/custom-blueprints.html)

Learn how to develop custom blueprints for your Amazon CodeCatalyst space and manage the lifecycle of those blueprints.

- [Custom blueprints concepts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/custom-bp-concepts.html): Learn about custom blueprint concepts required for blueprint authors.
- [Getting started with custom blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-bp.html): Learn how to develop and publish custom blueprints for your Amazon CodeCatalyst space.
- [Tutorial: Creating and updating a React application](https://docs.aws.amazon.com/codecatalyst/latest/userguide/blueprint-getting-started-tutorial.html): Get started with custom blueprints.
- [Converting source repositories to custom blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/convert-bp.html): Learn how to convert source repositories and CodeCatalyst projects to blueprints for your space.

### [Working with lifecycle management as a blueprint author](https://docs.aws.amazon.com/codecatalyst/latest/userguide/lifecycle-management-dev.html)

Learn about the lifecycle management for projects using blueprints in your Amazon CodeCatalyst space.

- [Testing lifecycle management for bundle outputs and merge conflicts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-lm.html): You can locally test your blueprintâs lifecycle management and merge conflict resolution.
- [Using merge strategies to generate bundles and specifying files](https://docs.aws.amazon.com/codecatalyst/latest/userguide/merge-strategies-lm.html): You can use merge strategies to generate bundles with resynthesis and specify files for lifecycle management updates of custom blueprints.
- [Accessing context objects for project details](https://docs.aws.amazon.com/codecatalyst/latest/userguide/context-objects-lm.html): As a blueprint author, you can access context from the blueprintâs project during synthesis to get information like space and project names, or existing files in a projectâs source repository.

### [Developing a custom blueprint to meet project requirements](https://docs.aws.amazon.com/codecatalyst/latest/userguide/develop-bp.html)

Learn how to develop a custom blueprint for your Amazon CodeCatalyst space.

- [Modifying blueprint features with a front-end wizard](https://docs.aws.amazon.com/codecatalyst/latest/userguide/wizard-bp.html): Learn about working with the front-end wizard of your custom blueprints in your Amazon CodeCatalyst space.
- [Generating inputs and rerendering front-end wizard elements](https://docs.aws.amazon.com/codecatalyst/latest/userguide/comp-dynamic-input-bp.html): Learn how to generate wizard inputs and dynamically rerendering the front-end wizard from your custom blueprint.
- [Adding environment components to a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/comp-env-bp.html): Learn how to work with environment components for custom blueprints.
- [Adding secrets components to a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/secrets-comp-bp.html): Learn how to work with secrets components for your custom blueprints.
- [Adding region components to a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/region-comp-bp.html): Learn how to work with region components for your custom blueprints.
- [Adding repository and source code components to a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/comp-repo-source-bp.html): Learn how to work with repository and source code components for your custom blueprints.
- [Adding workflow components to a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/comp-workflow-bp.html): Learn how to work with workflow components for custom blueprints.
- [Adding Dev Environments components to a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/comp-dev-env-bp.html): Learn how to work with Dev Environments components for custom blueprints.
- [Adding issues components to a blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/comp-issues-bp.html): Learn how to work with issues components for custom blueprints.
- [Working with blueprint tooling and CLI](https://docs.aws.amazon.com/codecatalyst/latest/userguide/bp-cli.html): Learn about how to use the blueprint CLI to manage and work with custom blueprint.
- [Assessing interface changes with snapshot testing](https://docs.aws.amazon.com/codecatalyst/latest/userguide/testing-bp.html): Learn about how custom blueprints support snapshot testing.
- [Publishing a custom blueprint to a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/publish-bp.html): Learn how to publish a preview version of a custom blueprint to test before publishing a normal version to a CodeCatalyst space.
- [Setting publishing permissions for a custom blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/manage-permissions-bp.html): Learn how to enable and disable publishing permissions for custom blueprints in your Amazon CodeCatalyst space.
- [Adding a custom blueprint to a space blueprints catalog](https://docs.aws.amazon.com/codecatalyst/latest/userguide/add-bp.html): Learn how to add a custom blueprint to your Amazon CodeCatalyst space's blueprints catalog.
- [Changing catalog versions for a custom blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/mange-version-bp.html): Learn how to change the version of your custom blueprints for your Amazon CodeCatalyst space's blueprints catalog.
- [Viewing details, versions, and projects of a custom blueprint](https://docs.aws.amazon.com/codecatalyst/latest/userguide/view-bp.html): Learn how to view a custom blueprint in your space.
- [Removing a custom blueprint from a space blueprints catalog](https://docs.aws.amazon.com/codecatalyst/latest/userguide/remove-bp.html): Learn how to remove a custom blueprint from your Amazon CodeCatalyst space's blueprints catalog.
- [Deleting a published custom blueprint or version](https://docs.aws.amazon.com/codecatalyst/latest/userguide/delete-bp.html): Learn how to delete a custom blueprint or custom blueprint's version from your Amazon CodeCatalyst space.
- [Adding dependencies, handling mismatches, and upgrading tooling and components](https://docs.aws.amazon.com/codecatalyst/latest/userguide/dependencies-tooling-bp.html): Learn how to work with dependencies and tooling for custom blueprints.
- [Contribute](https://docs.aws.amazon.com/codecatalyst/latest/userguide/contribute-bp.html): Learn how to contribute to the open-source blueprints GitHub repository.
- [Quotas for blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/blueprints-quotas.html): Learn about the quotas and limits for blueprints in CodeCatalyst.


## [Store and collaborate on code with source repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source.html)

- [Source repository concepts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-concepts.html): Learn about the concepts that can help you work with source repositories in CodeCatalyst.
- [Setting up](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-setting-up.html): Learn how to set up for working with source repositories in CodeCatalyst.
- [Getting started with source repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-getting-started.html): Learn how to get started with source repositories in CodeCatalyst.

### [Storing source code in repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories.html)

Learn how to work with source repositories in CodeCatalyst.

- [Creating a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-create.html): Learn how to create a source repository in CodeCatalyst.
- [Cloning an existing Git repository into a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-add-existing.html): Learn how to clone the contents of an existing Git repository into a source repository in CodeCatalyst.
- [Linking a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-link.html): Learn how to link a source repository in CodeCatalyst.
- [Viewing a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-view.html): Learn how to view a source repository in CodeCatalyst.
- [Editing the settings for a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-edit.html): Learn how to edit the settings for a source repository in CodeCatalyst.
- [Cloning a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-clone.html): Learn how to clone a source repository in CodeCatalyst.
- [Deleting a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-delete.html): Learn how to delete a source repository in CodeCatalyst.

### [Organizing your source code work with branches](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-branches.html)

Learn how to work with branches in CodeCatalyst.

- [Creating a branch](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-create-delete-branch.html): Learn how to create a branch in the CodeCatalyst console.
- [Managing the default branch](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-branches-default-branch.html): Learn about default branches, how to know which is the default branch, and how to specify a different branch as the default.
- [Manage allowed actions with branch rules](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-branches-branch-rules.html): Learn about branch rules, which help you determine what actions a user can take in a branch depending on their role in a project.
- [Git commands for branches](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-branches-git.html): Learn how to use Git to manage branches in Amazon CodeCatalyst, including creating and deleting branches.
- [Viewing branches and details](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-branches-view.html): Learn how to view details about a branch in Amazon CodeCatalyst, including its contents and the latest commit.
- [Deleting a branch](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-branches-delete.html): Learn how to delete unneeded branches in Amazon CodeCatalyst

### [Managing source code files](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-files.html)

Learn how to work with files in CodeCatalyst.

- [Creating or adding a file](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-files-create.html): Learn how to create and add files to your Amazon CodeCatalyst source repository.
- [Viewing a file](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-files-view.html): Learn how to view files in a source repository in Amazon CodeCatalyst.
- [Viewing the history of changes to a file](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-files-view-history.html): Learn how to view the history of changes to a file in Amazon CodeCatalyst.
- [Editing a file](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-files-edit.html): Learn how to edit a file in Amazon CodeCatalyst.
- [Renaming or deleting a file](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-files-delete.html): Learn how to rename and delete files in Amazon CodeCatalyst.

### [Reviewing code with pull requests](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-pull-requests.html)

Learn how to work with pull requests in CodeCatalyst.

- [Creating a pull request](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-create.html): Learn how to create a pull request in Amazon CodeCatalyst.
- [Viewing pull requests](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-view.html): Learn how to view pull requests in Amazon CodeCatalyst.
- [Managing requirements for merging with approval rules](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-pull-requests-approval-rules.html): Learn about approval rules, which help you meet quality standards for merging pull requests by setting requirements that must be met before merging a pull request to a destination branch.
- [Reviewing a pull request](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-review.html): Learn how to review a pull request in Amazon CodeCatalyst.
- [Updating a pull request](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-update.html): Learn how to update a pull request in Amazon CodeCatalyst.
- [Merging a pull request](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-merge.html): Learn how to merge a pull request in Amazon CodeCatalyst.
- [Closing a pull request](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-close.html): Learn how to close a pull request in Amazon CodeCatalyst.
- [Understanding changes in source code with commits](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-commits.html): Learn how to work with commits in CodeCatalyst.
- [Quotas for source repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-quotas.html): Learn about the quotas and limits for source repositories in CodeCatalyst.


## [Write and modify code with Dev Environments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html)

- [Creating a Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-create.html): Learn how to create a Dev Environment in Amazon CodeCatalyst.
- [Stopping a Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-stop.html): Learn how to stop use of a Dev Environment in Amazon CodeCatalyst.
- [Resuming a Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-resume.html): Learn how to resume use of a Dev Environment in Amazon CodeCatalyst.
- [Editing a Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-edit.html): Learn how to edit a Dev Environment in Amazon CodeCatalyst.
- [Deleting a Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-delete.html): Learn how to delete a Dev Environment in Amazon CodeCatalyst.
- [Connecting to a Dev Environment using SSH](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-connect-ssh.html): Learn how to connect to a Dev Environment using SSH in Amazon CodeCatalyst.

### [Configuring and using a devfile](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile.html)

Learn how to configure your CodeCatalyst Dev Environment by editing the devfile for a Dev Environment.

- [Editing a devfile](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile-moving.html): Learn how to edit a devfile for a Dev Environment.
- [Specifying universal devfile images](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-universal-image.html): The default universal image includes the most commonly used programming languages and related tools that can be used for your IDE.
- [Devfile commands](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile-commands.html): Currently, CodeCatalyst only supports exec commands in your devfile.
- [Devfile events](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile-events.html): Currently, CodeCatalyst only supports postStart events in your devfile.
- [Devfile components](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile-components.html): Currently, CodeCatalyst only supports container components in your devfile.
- [Associating a VPC connection to a Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-using-vpc.html): Learn how to work with VPC-connected Dev Environment.
- [Quotas for Dev Environments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-limits.html): Learn about the quotas and limits for Dev Environments in CodeCatalyst.


## [Publish and share software packages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages.html)

- [Packages concepts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-concepts.html): Learn about the concepts and terms that you'll need to know as you work with packages in Amazon CodeCatalyst.

### [Configuring and using package repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-repositories.html)

Learn about working with packages in CodeCatalyst.

- [Creating a package repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-repositories-create.html): Perform the following steps to create a package repository in CodeCatalyst.
- [Connecting to a package repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-repositories-connect.html): To publish to, or consume packages from CodeCatalyst, you must configure your package manager with your package repository endpoint information and CodeCatalyst credentials.
- [Deleting a package repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-repositories-delete.html): Perform the following steps to delete a package repository in CodeCatalyst.

### [Configuring and using upstream repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-upstream-repositories.html)

Learn about working with upstream repositories in CodeCatalyst.

- [Adding an upstream repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-upstream-repositories-add.html): Adding a public package repository or another CodeCatalyst package repository as an upstream repository to your downstream repository makes all of the packages in the upstream repository available to package managers that are connected to the downstream repository.
- [Editing the search order of upstream repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-upstream-repositories-search-order.html): CodeCatalyst searches upstream repositories in their configured search order.
- [Requesting a package version with upstream repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-upstream-repositories-request.html): Learn what happens when a package manager requests a package version from a package repository in CodeCatalyst that contains upstream repositories.
- [Removing an upstream repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-upstream-repositories-remove.html): If you no longer want to access the packages within an upstream repository, you can remove the upstream repository from a package repository.
- [Connecting to public external repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-connect-external.html): You can connect CodeCatalyst package repositories to supported public, external repositories by adding the corresponding gateway repository as an upstream repository.

### [Publishing and modifying packages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/working-with-packages.html)

Learn about working with package repositories in CodeCatalyst.

- [Publishing packages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/package-publishing.html): You can publish versions of any supported package type to a CodeCatalyst package repository by using package manager tools.
- [Viewing package version details](https://docs.aws.amazon.com/codecatalyst/latest/userguide/working-with-packages-view.html): You can use the CodeCatalyst console to view details about a specific package version.
- [Deleting a package version](https://docs.aws.amazon.com/codecatalyst/latest/userguide/working-with-packages-delete.html): You can delete a package version from the Package version details page in the CodeCatalyst console.
- [Updating a package version's status](https://docs.aws.amazon.com/codecatalyst/latest/userguide/working-with-packages-update-version-status.html): Every package version in CodeCatalyst has a status that describes the current state and availability of the package version.
- [Editing package origin controls](https://docs.aws.amazon.com/codecatalyst/latest/userguide/package-origin-controls.html): In Amazon CodeCatalyst, package versions can be added to a package repository by directly publishing them, pulling them down from an upstream repository, or ingesting them from an external, public repository through a gateway.

### [Using npm](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-npm.html)

Learn about using npm with Amazon CodeCatalyst.

- [Configuring and using npm](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-npm-use.html): To use npm with CodeCatalyst, you must connect npm to your package repository and provide a personal access token (PAT) for authentication.
- [npm tag handling](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-npm-tags.html): npm registries support tags, which are string aliases for package versions.

### [Using Maven](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-maven.html)

Learn about using Maven with Amazon CodeCatalyst.

- [Configuring and using Gradle Groovy](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-maven-gradle.html): To use Gradle Groovy with CodeCatalyst, you must connect Gradle Groovy to your package repository and provide a personal access token (PAT) for authentication.
- [Configuring and using mvn](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-maven-mvn.html): You use the mvn command to run Maven builds.
- [Publishing packages with curl](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-maven-curl.html): This section shows how to use the HTTP client curl to publish Maven packages to a CodeCatalyst package repository.
- [Using Maven checksums and snapshots](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-maven-checksums-snapshots.html): The following sections describe how to use Maven checksums and Maven snapshots in CodeCatalyst.

### [Using NuGet](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-nuget.html)

Learn about using NuGet with Amazon CodeCatalyst.

- [Using CodeCatalyst with Visual Studio](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-nuget-visual-studio.html): Configure Visual Studio to consume packages with CodeCatalyst.
- [Configuring and using nuget or dotnet](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-nuget-cli.html): Configure the NuGet package manager to consume and publish packages with CodeCatalyst.
- [NuGet package name, version, and asset name normalization](https://docs.aws.amazon.com/codecatalyst/latest/userguide/nuget-name-normalization.html): CodeCatalyst normalizes package and asset names and package versions before storing them, which means the names or versions in CodeCatalyst may be different than the ones provided when the package or asset was published.
- [NuGet compatibility](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-nuget-compatibility.html): NuGet versions and compatibility in CodeCatalyst.

### [Using Python](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-python.html)

Learn about using Python with Amazon CodeCatalyst.

- [Configuring pip and installing Python packages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-python-pip.html): To use pip with CodeCatalyst, you must connect pip to your package repository and provide a personal access token for authentication.
- [Configuring Twine and publishing Python packages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-python-twine.html): To use twine with CodeCatalyst, you must connect twine to your package repository and provide a personal access token for authentication.
- [Python package name normalization](https://docs.aws.amazon.com/codecatalyst/latest/userguide/python-name-normalization.html): CodeCatalyst normalizes package names before storing them, which means the package names in CodeCatalyst may be different than the name provided when the package was published.
- [Python compatibility](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-python-compatibility.html): While CodeCatalyst does not support the /simple/ API, it does support the Legacy API operations.
- [Quotas for packages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-quotas.html): Learn about packages quotas in Amazon CodeCatalyst.


## [Build, test, and deploy with workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflow.html)

- [Workflows concepts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-concepts.html): Learn the terminology and concepts associated with workflows in Amazon CodeCatalyst.
- [Getting started with workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-getting-started.html): Learn how to create your first workflow in Amazon CodeCatalyst.

### [Building with workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/build-workflow-actions.html)

Learn how to build applications and other resources using a build action in an Amazon CodeCatalyst workflow.

- [Adding the build action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/build-add-action.html): Learn how to add a build action to an Amazon CodeCatalyst workflow.
- [Viewing build action results](https://docs.aws.amazon.com/codecatalyst/latest/userguide/build-view-results.html): Learn how to view the results of an Amazon CodeCatalyst build action, including the generated logs, reports, and variables.
- [Tutorial: Upload artifacts to Amazon S3](https://docs.aws.amazon.com/codecatalyst/latest/userguide/build-deploy.html): Learn how to upload build artifacts to an Amazon S3 bucket using a build action in an Amazon CodeCatalyst workflow.
- [YAML - build and test actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/build-action-ref.html): Describes the build and test actions' YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Testing with workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-workflow-actions.html)

Learn how to configure a Amazon CodeCatalyst workflow to run tests and generate quality reports.

- [Adding the test action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-add-action.html): Learn how to add an Amazon CodeCatalyst test action to a CodeCatalyst workflow.
- [Viewing test action results](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-view-results.html): Learn how to view the results of a test action in Amazon CodeCatalyst.
- [Skipping failed tests](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test.error-handling.html): Learn how to skip a failed test in Amazon CodeCatalyst.
- [Integrating with universal-test-runner](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test.universal-test-runner.html): Learn how to use universal-test-runner to test your code in Amazon CodeCatalyst.
- [Configuring quality reports](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-config-action.html): Learn how to configure quality reports in Amazon CodeCatalyst.
- [Best practices for testing](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-best-practices.html): Learn about the best practices for testing in Amazon CodeCatalyst.
- [SARIF properties](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test.sarif.html): Learn about the SARIF properties that are supported in Amazon CodeCatalyst.

### [Deploying with workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy.html)

Learn how to deploy applications and other resources to various targets such as Amazon ECS, AWS Lambda, and more, using Amazon CodeCatalyst workflows.

### [Deploying to Amazon ECS](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-ecs.html)

Learn how to deploy a containerized application to an Amazon Elastic Container Service cluster by adding the 'Deploy to Amazon ECS' action to an Amazon CodeCatalyst workflow.

- [Tutorial: Deploy to Amazon ECS](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-tut-ecs.html): Learn how to build, test, and deploy an application to Amazon Elastic Container Service (Amazon ECS) using an Amazon CodeCatalyst workflow.
- [Adding the 'Deploy to Amazon ECS' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-ecs-adding.html): Learn how to add the 'Deploy to Amazon ECS' action to an Amazon CodeCatalyst workflow.
- [Variables - 'Deploy to Amazon ECS'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-ecs-variables.html): Learn about the variables that are output by the 'Deploy to Amazon ECS' action in an Amazon CodeCatalyst workflow.
- [YAML - 'Deploy to Amazon ECS'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-ref-ecs.html): Describes the 'Deploy to Amazon ECS' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Deploying to Amazon EKS](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-eks.html)

Learn how to deploy a containerized application into an Amazon Elastic Kubernetes Service cluster by adding the 'Deploy to Kubernetes cluster' action to an Amazon CodeCatalyst workflow.

- [Tutorial: Deploy to Amazon EKS](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-tut-eks.html): Learn how to build and deploy a containerized application into an Amazon EKS cluster using an Amazon CodeCatalyst workflow.
- [Adding the 'Deploy to Kubernetes cluster' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-eks-adding.html): Learn how to add the 'Deploy to Kubernetes cluster' action to an Amazon CodeCatalyst workflow.
- [Variables - 'Deploy to Kubernetes cluster'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-eks-variables.html): Learn about the variables that are output by the 'Deploy to Kubernetes cluster' action in an Amazon CodeCatalyst workflow.
- [YAML - 'Deploy to Kubernetes cluster'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-ref-eks.html): Describes the 'Deploy to Kubernetes cluster' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Deploying a CloudFormation stack](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-cfn.html)

Learn how to deploy an AWS CloudFormation stack using an Amazon CodeCatalyst workflow.

- [Tutorial: Deploy a CloudFormation stack](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-tut-lambda.html): Learn how to build, test, and deploy a serverless application using an Amazon CodeCatalyst workflow and a CloudFormation stack.
- [Adding the 'Deploy CloudFormation stack' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-cfn-adding.html): Learn how to add the 'Deploy CloudFormation stack' action to an Amazon CodeCatalyst workflow.
- [Configuring rollbacks](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-consumption-enable-alarms.html): Learn how to turn off rollbacks in Amazon CodeCatalyst, and how to enable rollbacks when an alarm occurs.
- [Variables - 'Deploy CloudFormation stack'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-cfn-variables.html): Learn about the variables that are output by the 'Deploy CloudFormation stack' action in an Amazon CodeCatalyst workflow.
- [YAML - 'Deploy CloudFormation stack'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-action-ref-cfn.html): Describes the 'Deploy CloudFormation stack' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Deploying an AWS CDK app](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-dep-action.html)

Learn how to deploy an AWS CDK app using the 'AWS CDK deploy' action in an Amazon CodeCatalyst workflow.

- [Example: Deploying an AWS CDK app](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-dep-action-example-workflow.html): See an example Amazon CodeCatalyst workflow that includes the 'AWS CDK deploy' and 'AWS CDK bootstrap' actions.
- [Adding the 'AWS CDK deploy' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-dep-action-add.html): Learn how to add the 'AWS CDK deploy' action to an Amazon CodeCatalyst workflow.
- [Variables - 'AWS CDK deploy'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-dep-action-variables.html): Learn about the variables generated by the 'AWS CDK deploy' action in Amazon CodeCatalyst.
- [YAML - 'AWS CDK deploy'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-dep-action-ref.html): Describes the 'AWS CDK deploy' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Bootstrapping an AWS CDK app](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-boot-action.html)

Learn about configuring the 'AWS CDK bootstrap' action in Amazon CodeCatalyst workflows.

- [Example: Bootstrapping an AWS CDK app](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-boot-action-example-workflow.html): Provides an example workflow that includes the 'AWS CDK bootstrap' action and a Deploy an AWS CDK app action.
- [Adding the 'AWS CDK bootstrap' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-boot-action-add.html): Learn how to add the 'AWS CDK bootstrap' to an Amazon CodeCatalyst workflow.
- [Variables - 'AWS CDK bootstrap' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-boot-action-variables.html): Learn about the variables generated by the "Deploy AWS CDK bootstrap" action in a Amazon CodeCatalyst workflow.
- [YAML - 'AWS CDK bootstrap'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-boot-action-ref.html): Describes the 'AWS CDK bootstrap' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Publishing to Amazon S3](https://docs.aws.amazon.com/codecatalyst/latest/userguide/s3-pub-action.html)

Learn how to publish files to an Amazon S3 bucket using the 'Amazon S3 publish' action and an Amazon CodeCatalyst workflow.

- [Example: Publish files to Amazon S3](https://docs.aws.amazon.com/codecatalyst/latest/userguide/s3-pub-action-example-workflow.html): See an example Amazon CodeCatalyst workflow that includes an 'Amazon S3 publish' action, a build action, and a 'Deploy to Amazon ECS' action.
- [Adding the 'Amazon S3 publish' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/s3-pub-action-add.html): Learn how to add the 'Amazon S3 publish' to an Amazon CodeCatalyst workflow.
- [YAML - 'Amazon S3 publish' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/s3-pub-action-ref.html): Describes the 'Amazon S3 publish' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Deploying into AWS accounts and VPCs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments.html)

Learn how to deploy your applications into your AWS accounts and Amazon Virtual Private Clouds using Amazon CodeCatalyst environments.

- [Creating an environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments-creating-environment.html): Learn how to create an Amazon CodeCatalyst environment that you can later associate with a CodeCatalyst workflow action.
- [Associating an environment with an action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments-add-app-to-environment.html): Learn how to associate an environment with a workflow action in Amazon CodeCatalyst.
- [Associating a VPC with an environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments-associate-vpc.html): Learn how to associate an Amazon VPC connection with an Amazon CodeCatalyst environment.
- [Associating an AWS account with an environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments-associate-account.html): Learn how to associate an AWS account with an Amazon CodeCatalyst environment.
- [Changing the IAM role of an action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-environments-switch-role.html): Learn how to change the IAM role associated with an Amazon CodeCatalyst workflow action.
- [Displaying the app URL](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-app-url.html): Learn how to make the app URL appear in the workflow diagram so that it's easier to find.
- [Removing a deployment target](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-remove-target.html): Learn about removing clusters, stacks, and other deployment targets from the environments page in the Amazon CodeCatalyst console.
- [Tracking deployment status by commit](https://docs.aws.amazon.com/codecatalyst/latest/userguide/track-changes.html): Learn how to track commits in Amazon CodeCatalyst and see which ones have been deployed to which environments.
- [Viewing deployment logs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-deployment-logs.html): View and search for deployment logs in Amazon CodeCatalyst.
- [Viewing deployment information](https://docs.aws.amazon.com/codecatalyst/latest/userguide/deploy-view-deployment-info.html): View deployment status, start time, end time, duration of events, commits, pull requests (PRs), related issues, and metrics in Amazon CodeCatalyst.
- [Creating a workflow](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-create-workflow.html): Learn how to create a workflow in Amazon CodeCatalyst.

### [Running a workflow](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-runs.html)

Learn how to start, stop, and configure workflow runs in Amazon CodeCatalyst.

- [Starting runs manually](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-manually-start.html): Learn how to start a workflow run manually starting from the Amazon CodeCatalyst console.

### [Starting runs automatically using triggers](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-add-trigger.html)

Learn how to start an Amazon CodeCatalyst workflow run automatically using triggers.

- [Examples: Triggers in workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-add-trigger-examples.html): Learn how to set up triggers in a Amazon CodeCatalyst workflow through the use of examples.
- [Usage guidelines for triggers and branches](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-add-trigger-considerations.html): Learn how to set up triggers and workflows in a setup that works with typical Git braching and software release strategies.
- [Adding triggers to workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-add-trigger-add.html): Learn how to add triggers to an Amazon CodeCatalyst workflow.
- [Configuring manual-only triggers](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-manual-only.html): Learn how to set up manual workflow triggers in Amazon CodeCatalyst.
- [Stopping a workflow run](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-stop.html): Learn how to stop an Amazon CodeCatalyst workflow run midway through its processing.

### [Gating a workflow run](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-gates.html)

Learn how to prevent an Amazon CodeCatalyst workflow run from continuing using gates.

- [Adding a gate to a workflow](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-gates-add.html): Learn how to add a gate to an Amazon CodeCatalyst workflow to prevent it from continuing unless certain conditions are met.
- [Sequencing gates and actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-gates-depends-on.html): Learn how to set up gates to run before or after actions in a workflow using the 'Depends on' feature.
- [Specifying the version of a gate](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-gates-version.html): Learn how to configure an Amazon CodeCatalyst workflow to use a specific version of a gate, or to use the latest version of a gate.

### [Requiring approvals on workflow runs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-approval.html)

Learn how to configure an Amazon CodeCatalyst workflow so that it requires an approval.

- [Example: An 'Approval' gate](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-approval-example.html): Learn how to add an 'Approval' gate to an Amazon CodeCatalyst workflow using example code.
- [Adding an 'Approval' gate](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-approval-add.html): Learn how to add an 'Approval' gate to a CodeCatalyst workflow.
- [Configuring approval notifications](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-approval-notify.html): Learn how to set up Slack so that users are notified when an approval is required on an Amazon CodeCatalyst workflow run.
- [Approving or rejecting a workflow run](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-approval-approve.html): Learn how to approve or reject a workflow run in Amazon CodeCatalyst.
- [YAML - 'Approval' gate](https://docs.aws.amazon.com/codecatalyst/latest/userguide/approval-ref.html): Describes the 'Approval' gate's YAML properties in the Amazon CodeCatalyst workflow definition file.
- [Configuring the queuing behavior of runs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-configure-runs.html): Learn how to configure the queuing behavior of Amazon CodeCatalyst workflow runs.
- [Caching files between runs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-caching.html): Amazon CodeCatalyst allows you to save on-disk files to a cache and restore them from that cache in subsequent workflow runs.
- [Viewing workflow run status and details](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-view-run.html): Learn how to view the status and details of an Amazon CodeCatalyst workflow run.

### [Configuring workflow actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-actions.html)

Learn how to add different types of actions, or tasks, to an Amazon CodeCatalyst workflow.

- [Adding an action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-add-action.html): Learn how to add actions, or tasks, to an Amazon CodeCatalyst workflow.
- [Removing an action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-delete-action.html): Learn how to remove an action, or task, from an Amazon CodeCatalyst workflow.
- [Developing a custom action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-custom-action.html): Learn how to develop your own custom actions using the Amazon CodeCatalyst Action Development Kit.

### [Grouping actions into action groups](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-group-actions.html)

Learn how to organize your actions into action groups in Amazon CodeCatalyst.

- [Example: Defining two action groups](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-group-actions-example.html): The following example shows how to define two Amazon CodeCatalyst action groups: BuildAndTest and Deploy.

### [Sequencing actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-depends-on.html)

Learn how to set up your actions to run in sequence (or in parallel) within an Amazon CodeCatalyst workflow.

- [Examples of how to configure dependencies between actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-depends-on-examples.html): Learn how to configure dependencies between workflow actions using the DependsOn property.
- [Setting up dependencies between actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-depends-on-set-up.html): Learn how to set up dependencies between workflow actions and action groups.

### [Sharing artifacts and files between actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-artifacts.html)

Learn about how you can use Amazon CodeCatalyst workflow artifacts to share data between actions in a workflow.

- [Examples of artifacts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-artifacts-ex.html): Learn about how to output and reference artifacts through a series of examples.
- [Defining an output artifact](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-artifacts-output.html): Learn how to output a workflow artifact
- [Defining an input artifact](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-artifacts-refer.html): Learn how to reference an artifact generated by a previous workflow action.
- [Referencing files in an artifact](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-artifacts-refer-files.html): Learn how to reference files inside an artifact.
- [Downloading artifacts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-download-workflow-outputs.html): Learn about workflow artifacts, how to download them, and how to inspect them
- [Specifying the action version to use](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-action-versions.html): Learn how actions are versioned, and how to configure which version an Amazon CodeCatalyst workflow uses.
- [Listing the available action versions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-action-versions-determine.html): Learn how to determine which versions of an action are available in Amazon CodeCatalyst.
- [Viewing an action's source code](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-view-source.html): Learn how to inspect an Amazon CodeCatalyst action's source code to make sure it doesn't contain risky code or security vulnerabilities.

### [Integrating with GitHub Actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/integrations-github-actions.html)

Learn how to integrate GitHub Actions with Amazon CodeCatalyst workflows.

- [Tutorial: Lint code using a GitHub Action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/integrations-github-action-tutorial.html): Learn how to add the Super-Linter GitHub Action to an Amazon CodeCatalyst workflow.
- [Adding the 'GitHub Actions' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/integrations-github-action-add.html): Learn how to add a 'GitHub Actions' action to an Amazon CodeCatalyst workflow.
- [Adding a curated GitHub Action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/integrations-github-action-add-curated.html): Learn what a curated GitHub Action is and how to add one to an Amazon CodeCatalyst workflow.
- [Exporting GitHub output parameters](https://docs.aws.amazon.com/codecatalyst/latest/userguide/integrations-github-action-export.html): Learn how to export GitHub output parameters from a GitHub Action so that they can be used in subsequent actions in an Amazon CodeCatalyst workflow.
- [Referencing GitHub output parameters](https://docs.aws.amazon.com/codecatalyst/latest/userguide/integrations-github-action-referencing.html): GitHub Actions can generate output parameters.
- [YAML - 'GitHub Actions' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/github-action-ref.html): Describes the 'GitHub Actions' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Configuring compute and runtime images](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-compute.html)

Learn how to configure the compute engine and runtime image that Amazon CodeCatalyst uses to run workflows.

- [Creating a provisioned fleet](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-create-compute-resource.html): Learn how to create a provisioned fleet in Amazon CodeCatalyst.
- [Editing a provisioned fleet](https://docs.aws.amazon.com/codecatalyst/latest/userguide/edit-compute-resource.html): Learn how to change the capacity and scaling mode of a provisioned fleet in Amazon CodeCatalyst.
- [Deleting a provisioned fleet](https://docs.aws.amazon.com/codecatalyst/latest/userguide/delete-compute-resource.html): Learn how to delete a provisioned fleet in Amazon CodeCatalyst.
- [Assigning a fleet or compute to an action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-assign-compute-resource.html): Learn how to assign a provisioned fleet or a different on-demand compute type to an Amazon CodeCatalyst action.
- [Sharing compute across actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/compute-sharing.html): Learn about compute sharing, the capabilities of compute sharing, and how to turn on compute sharing in Amazon CodeCatalyst.
- [Specifying runtime environment images](https://docs.aws.amazon.com/codecatalyst/latest/userguide/build-images.html): Learn how to specify the runtime environment Docker image on which worflow actions will run in Amazon CodeCatalyst.

### [Connecting source repositories to workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-sources.html)

Learn how to connect a source repository to an Amazon CodeCatalyst workflow so that the workflow can interact with files in the repository.

- [Specifying a workflow file's source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-sources-specify-workflow-def.html): Learn how to specify the Amazon CodeCatalyst source repository that will contain your workflow definition file.
- [Specifying a workflow action's source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-sources-specify-action.html): Learn how to specify the source source repository to which an Amazon CodeCatalyst workflow action will connect to obtain files.
- [Referencing source repository files](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-sources-reference-files.html): You might have files stored in a source repository connected to Amazon CodeCatalyst.
- [Variables - 'BranchName' and 'CommitId'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-sources-variables.html): Learn about the 'BranchName' and 'CommitId' variables that are output by the CodeCatalyst workflow source.

### [Connecting package repositories to workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-packages.html)

Learn how to connect an Amazon CodeCatalyst package repository to a workflow so that the workflow's actions can push and pull dependencies to and from the configured repository.

- [Tutorial: Pull from a package repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-tutorial.html): Learn how create an Amazon CodeCatalyst workflow that runs an application that pulls its dependencies from a CodeCatalyst package repository.
- [Specifying CodeCatalyst package repositories in workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-package-specify-action.html): Learn how to specify a package configuration to use with an action in your Amazon CodeCatalyst workflow.
- [Using authorization tokens in workflow actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-package-export-token.html): Learn how to use an exported authorization token with an action in your workflow.
- [Examples: Package repositories in workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-packages-ex.html): Learn about how to reference packages through a series of examples.

### [Invoking a Lambda function](https://docs.aws.amazon.com/codecatalyst/latest/userguide/lam-invoke-action.html)

Learn how to configure the 'AWS Lambda invoke' action in Amazon CodeCatalyst workflows.

- [Example: Invoke a Lambda function](https://docs.aws.amazon.com/codecatalyst/latest/userguide/lam-invoke-action-example-workflow.html): Describes an example workflow that includes the 'AWS Lambda invoke' action and a deploy action in Amazon CodeCatalyst.
- [Adding the 'AWS Lambda invoke' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/lam-invoke-action-add.html): Learn how to add the 'AWS Lambda invoke' to your workflow in Amazon CodeCatalyst.
- [Variables - 'AWS Lambda invoke'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/lam-invoke-action-variables.html): Learn about the variables that are generated by the 'AWS Lambda invoke' action in an Amazon CodeCatalyst workflow.
- [YAML - 'AWS Lambda invoke' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/lam-invoke-action-ref.html): Describes the 'AWS Lambda invoke' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Modifying an Amazon ECS task definition](https://docs.aws.amazon.com/codecatalyst/latest/userguide/render-ecs-action.html)

Learn how to configure the 'Render Amazon ECS task definition' action in Amazon CodeCatalyst workflows.

- [Example: Modify an Amazon ECS taskdef](https://docs.aws.amazon.com/codecatalyst/latest/userguide/render-ecs-action-example-workflow.html): Describes an example workflow that includes the Render Amazon ECS task definition action, a build action, and a Deploy to Amazon ECS action so that you can see how they interact.
- [Adding the 'Render Amazon ECS task definition' action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/render-ecs-action-add.html): Describes how to add the 'Render Amazon ECS task definition' to a Amazon CodeCatalyst workflow.
- [Viewing the updated task definition file](https://docs.aws.amazon.com/codecatalyst/latest/userguide/render-ecs-action-view.html): Describes how to view the name and contents of the task definition file that is updated by the 'Render Amazon ECS task definition' action.
- [Variables - 'Render Amazon ECS task definition'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/render-ecs-action-variables.html): Learn about the variables that are output by the 'Render Amazon ECS task definition' action.
- [YAML - 'Render Amazon ECS task definition'](https://docs.aws.amazon.com/codecatalyst/latest/userguide/render-ecs-action-ref.html): Describes the 'Render Amazon ECS task definition' action's YAML properties in the Amazon CodeCatalyst workflow definition file.

### [Using variables in workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables.html)

Learn what variables are and how to use them in an Amazon CodeCatalyst workflow.

### [Using user-defined variables](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-using-variables.html)

Learn what user-defined variables are and how to define, export, and reference them in an Amazon CodeCatalyst workflow.

- [Examples of variables](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-ex.html): The following examples show how to define and reference variables in the workflow definition file.
- [Defining a variable](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-define-input.html): You can define variables in two ways:
- [Defining a secret](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-define-secret.html): You define a secret on the Secrets page of the CodeCatalyst console.
- [Exporting a variable so that other actions can use it](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-export-input.html): Use the following instructions to export a variable from an action so that you can reference it in other actions.
- [Referencing a variable in the action that defines it](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-reference-input.html): Use the following instructions to reference a variable in the action that defines it.
- [Referencing a variable output by another action](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-reference-action.html): Use the following instructions to reference variables output by other actions.
- [Referencing a secret](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-reference-secret.html): For instructions on referencing a secret in the workflow definition file, see .

### [Using predefined variables](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-using-predefined-variables.html)

Learn what predefined variables are and how to reference them in an Amazon CodeCatalyst workflow.

- [Examples of referencing predefined variables](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-predefined-examples.html): Learn how to reference predefined variables in a workflow.
- [Referencing a predefined variable](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-reference-output-vars.html): You can reference predefined variables in any action within an Amazon CodeCatalyst workflow.
- [Determining which predefined variables your workflow emits](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-determine-output-vars.html): Use the following procedure to determine which predefined variables a workflow emits when it runs.
- [List of predefined variables](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflow-ref-action-variables.html): Provides reference information for predefined variables generated by Amazon CodeCatalyst actions or sources.

### [Masking data using secrets](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-secrets.html)

Learn how to use secrets to mask data in the Amazon CodeCatalyst workflow definition file.

- [Creating a secret](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-secrets.creating.html): Learn how to create a secret in Amazon CodeCatalyst to mask passwords and other sensitive information in the workflow definition file.
- [Editing a secret](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-secrets.editing.html): Learn how to edit a secret's value and description in Amazon CodeCatalyst.
- [Using a secret](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-secrets.using.html): Learn how to reference a secret in an Amazon CodeCatalyst workflow definition file.
- [Deleting a secret](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-secrets.deleting.html): Learn how to delete a secret from the Amazon CodeCatalyst console and workflow definition file.
- [Viewing a workflow's status](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-view-status.html): Learn about the different Amazon CodeCatalyst workflow states and how to view them.
- [Workflow quotas](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-quotas.html): Learn about the quotas and limits for workflows in Amazon CodeCatalyst.
- [Workflow run states](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-view-run-status.html): Learn about the states of a workflow run in Amazon CodeCatalyst.
- [Workflow states](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-workflow-status.html): Learn about the different workflow states and how to view them in Amazon CodeCatalyst.
- [Workflow YAML definition](https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflow-reference.html): CodeCatalyst workflows are defined in a YAML file called the 'workflow definition file'.


## [Track and organize work with issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues.html)

- [Issues concepts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-concepts.html): Describes issues terminology and concepts.

### [Tracking work with issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-tracking-work.html)

Learn about the different ways to track work with issues in CodeCatalyst.

- [Creating an issue](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-create-issue.html): Describes how to create an issue.

### [Editing and collaborating on issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-edit-collaborate-issue.html)

Describes how to edit an issue

- [Editing an issue](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-edit-issue.html): Follow these steps to edit the title, description, status, assignee, priority, estimate, or labels of an issue.

### [Working with attachments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-attachments.html)

Information about attachments for issues in CodeCatalyst.

- [Viewing and managing attachments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-settings-attachments.html): Describes how to manage attachments in CodeCatalyst issues.
- [Managing tasks on issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-tasks.html): Tasks can be added to issues to further break down, organize, and track the work of that issue.
- [Link an issue to another issue](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-link-issue.html): Describes how to link an issue to another issue.
- [Marking an issue as blocked or unblocked](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-mark-as-blocked.html): Describes how to mark an issue as blocked or unblocked.

### [Adding, editing, or deleting comments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-comment.html)

Describes how to comment on an issue

- [Using mentions in a comment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-mentions-comment.html): You can mention space members, other projects in the space, related issues, and code in comments.

### [Finding and viewing issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-view.html)

Describes the various ways to view an issue

- [Sorting issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-sorting.html): By default, issues in CodeCatalyst are sorted by Manual order.
- [Grouping issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-grouping.html): Grouping is used to organize issues on the board by multiple parameters, such as assignee, labels, and priority.
- [Filtering issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-filter.html): Use filtering to find issues that contain a specified name, priority, label, custom fields, or assignee.

### [Progressing an issue](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-move-issue.html)

Describes how to move an issue

- [Moving an issue beetween the backlog and board](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-move-backlog-board.html): You can move an issue from the backlog to the board once you begin to work on the issue.
- [Progress an issue through lifecycle stages on the board](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-move-within-board.html): You can move an issue within a board through different statuses until completion.
- [Moving issues between groups](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-move-groups.html): You can group issues in the All issues and Board views by various parameters.
- [Archiving an issue](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-archive-issues.html): Describes how to archive an issue
- [Exporting issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-export-active-issues.html): Describes how to configure the settings for issues.

### [Organizing work with backlogs, labels, and boards](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-organizing-work.html)

Learn about the different ways to organize work with issues in CodeCatalyst.

### [Categorizing work with labels](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-labels.html)

Describes how to customize labels.

- [Editing a label](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-edit-label.html): Use the following procedure to change the name or color of an existing label.
- [Deleting a label](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-delete-label.html): You cannot currently delete an issues label in CodeCatalyst.
- [Organizing work with custom fields](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-custom-fields.html): Describes how to customize fields in CodeCatalyst issues.

### [Tracking work with custom statuses](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-customize-statuses.html)

Describes how to customize statuses.

- [To create a status](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-create-status.html)
- [To edit a status](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-edit-status.html)
- [To move a status](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-move-status.html)
- [To deactivate a status](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-deactivate-status.html)
- [Configuring issue effort estimation](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-settings-estimation.html): Describes how to configure effort estimation for issues.
- [Enabling or disabling multiple assignees](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-settings-multiple-assignees.html): Describes how to configure multiple assignees for issues.
- [Creating an issues view](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-creating-view.html): You can create views to quickly view issues that match a particular set of filters.
- [Quotas for issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-quotas.html): Learn about the quotas and limits for issues in CodeCatalyst.


## [Configure identity, permissions, and access in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa.html)

### [Granting access with user roles](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-roles.html)

Learn about the roles in CodeCatalyst, including the permissions associated with each role.

- [Understanding user roles for spaces and projects](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-role-types.html): Learn about the types of role available in CodeCatalyst.
- [Viewing the permissions available for each role](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-permissions.html): Learn which CodeCatalyst permissions are available for each CodeCatalyst role.
- [Viewing and changing user roles](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-roles-manage.html): Learn how to view and change the roles assigned to users in a project and in a space in CodeCatalyst.
- [Grant users repository access with personal access tokens](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-tokens-keys.html): Learn how to manage personal access tokens in CodeCatalyst.
- [](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-settings-connections.html): Learn how to access GitHub resources with personal connections in CodeCatalyst.
- [Configure your AWS Builder ID to sign in with multi-factor authentication (MFA)](https://docs.aws.amazon.com/codecatalyst/latest/userguide/mfa.html): Learn about multi-factor authentication in Amazon CodeCatalyst.

### [Security](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security.html)

Configure Amazon CodeCatalyst to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your CodeCatalyst resources.

- [Data privacy](https://docs.aws.amazon.com/codecatalyst/latest/userguide/data-privacy.html): CodeCatalyst collects aggregate information in IAM Identity Center.
- [Data protection](https://docs.aws.amazon.com/codecatalyst/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in CodeCatalyst.

### [CodeCatalyst and Identity and Access Management](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam.html)

Learn how to manage access to CodeCatalyst resources in connected AWS accounts.

- [Using tags to control access to account connection resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/id-based-policy-examples-tags.html): Lists example tag-based access control policies for account connections.
- [Using service-linked roles](https://docs.aws.amazon.com/codecatalyst/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give CodeCatalyst access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for CodeCatalyst and recent changes to those policies.
- [Grant access to project AWS resources with IAM roles](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-iam-roles.html): Learn how to create and manage roles and policies you need to perform Amazon CodeCatalyst actions in an AWS account.
- [Compliance validation](https://docs.aws.amazon.com/codecatalyst/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/codecatalyst/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific CodeCatalyst features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/codecatalyst/latest/userguide/infrastructure-security.html): Learn how Amazon CodeCatalyst isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/codecatalyst/latest/userguide/vulnerability-analysis-and-management.html): Learn about configuration and vulnerability analysis in Amazon CodeCatalyst.
- [Your data and privacy in Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/your-data-privacy.html): Learn about data and privacy in Amazon CodeCatalyst.
- [Best practices for workflow actions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/security-best-practices-for-actions.html): Description of best practices when using security for actions in workflows.
- [Understanding the CodeCatalyst trust model](https://docs.aws.amazon.com/codecatalyst/latest/userguide/trust-model.html): Learn about the trust model in Amazon CodeCatalyst.

### [Monitoring events and API calls using logging](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-monitoring.html)

Learn about monitoring and logging in CodeCatalyst.

- [Monitoring API calls by AWS accounts using AWS CloudTrail logging](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-logging-connections.html): Learn about logging Amazon CodeCatalyst with AWS CloudTrail.
- [Accessing logged events using event logging](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-logs.html): Learn about downloading, viewing, and understanding logs of Amazon CodeCatalyst events.
- [Quotas for identity, permission, and access](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-quotas.html): Learn about the quotas and limits for identity, permission, and access in CodeCatalyst.
- [Troubleshooting](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-troubleshooting.html): Learn how to troubleshoot problems related to signing up and account verification in Amazon CodeCatalyst.


## [Add functionality to projects with extensions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions.html)

- [Extensions concepts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-concepts.html): Insert abstract text
- [Quickstart: Installing extensions, connecting provideres, and linking resources](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-quickstart.html): Learn how to quickly set up to use GitHub, Bitbucket, GitLab, or Jira with CodeCatalyst.
- [Installing an extension in a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/install-extension.html): You can install extensions for your CodeCatalyst space that add functionality to projects in that space.
- [Uninstalling an extension in a space](https://docs.aws.amazon.com/codecatalyst/latest/userguide/uninstall-extension.html): You can uninstall extensions that were previously installed in your CodeCatalyst space.
- [Connecting GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-connect.html): Learn how to connect GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites in CodeCatalyst.
- [Disconnecting GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-disconnect.html): Learn how to disconnect GitHub accounts, Bitbucket workspaces, GitLab users, and Jira sites in CodeCatalyst.
- [Linking GitHub repositories, Bitbucket repositories, GitLab project reposotories, and Jira projects](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-link.html): Learn how to link Linking GitHub repositories, Bitbucket repositories, GitLab project repositories, and Jira projects in CodeCatalyst.
- [Unlinking GitHub repositories, Bitbucket repositories, GitLab project repositories, and Jira projects](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-unlink.html): Learn how to unlink Linking GitHub repositories, Bitbucket repositories, GitLab project repositories, and Jira projects in CodeCatalyst.
- [Viewing third-party repositories and searching Jira issues in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-view-search.html): Learn how to view linked GitHub repositories, Bitbucket repositories, and GitLab project repositories, as well as search for Jira issues in CodeCatalyst.
- [Automatically starting a workflow run after third-party repository events](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-workflow-repositories.html): Learn about CodeCatalyst workflows and third-party events in GitHub repositories, Bitbucket repositories, or GitLab project repositories.
- [Restricting IP access with third-party repository providers](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-restrict-ip-access.html): Learn about CodeCatalyst's compatibility with GitHub Enterprise Cloud, Bitbucket Cloud Premium, and GitLab, including IP address access restrictions.
- [Blocking third-party merges when workflows fail](https://docs.aws.amazon.com/codecatalyst/latest/userguide/extensions-block-merges.html): Learn about blocking pull request merges in GitHub and Bitbucket, as well as merge requests in GitLab, when CodeCatalyst workflows fail.
- [Linking Jira issues to pull requests](https://docs.aws.amazon.com/codecatalyst/latest/userguide/link-jira-issues-pull-requests.html): Learn about linking Jira issues to a CodeCatalyst pull request.
- [Viewing CodeCatalyst events in Jira issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/view-codecatalyst-events-jira.html): Learn how to view CodeCatalyst events in Jira issues.


## [Troubleshooting](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting.html)

- [Troubleshooting source repositories](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-source.html): Learn how to troubleshoot problems with source repositories in Amazon CodeCatalyst.

### [Troubleshooting projects and blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-troubleshooting.html)

Learn how to troubleshoot problems related to projects and blueprints in Amazon CodeCatalyst.

- [Java API with AWS Fargate blueprint missing dependencies for apache-maven-3.8.6](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-troubleshooting-error-maven.html): Issue: For a project created from the Java API with AWS Fargate blueprint, the workflow fails with an error for missing apache-maven-3.8.6 dependencies.
- [Modern three-tier web application blueprint workflow OnPullRequest fails with permissions error for Amazon CodeGuru](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects-troubleshooting-onpullrequest.html): Issue: When I try to run a workflow for my project, the workflow fails to run with the following message:

### [Troubleshooting Dev Environments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironments-troubleshooting.html)

Learn how to troubleshoot problems with Dev Environments in Amazon CodeCatalyst.

- [Troubleshooting IDEs](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironments-troubleshooting-ides.html): Learn how to troubleshoot problems with IDEs in Amazon CodeCatalyst.
- [Troubleshooting devfiles](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironments-devenvironments-devfile.html): Learn how to troubleshoot problems with devfiles in Amazon CodeCatalyst.
- [Troubleshooting workflows](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-workflows.html): Learn how to troubleshoot problems with workflows in Amazon CodeCatalyst.
- [Troubleshooting issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-issues.html): Learn how to troubleshoot problems with issues in Amazon CodeCatalyst.
- [Troubleshooting search](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-search.html): Learn how to troubleshoot problems with search in Amazon CodeCatalyst.
- [Troubleshooting extensions](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-extensions.html): Learn how to troubleshoot problems with extensions in Amazon CodeCatalyst.
- [Troubleshooting associated accounts](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-connections.html): Learn how to troubleshoot problems with associated accounts in Amazon CodeCatalyst.
- [Troubleshooting AWS CLI and SDK issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/troubleshooting-cli-sdk.html): Learn how to troubleshoot problems between the AWS SDKs or the AWS CLI and Amazon CodeCatalyst.


## [Support for Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/support.html)

- [Billing for Support for Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/support-and-billing.html): When you create a space in CodeCatalyst, users in the space can create and manage support cases from Support for Amazon CodeCatalyst.
- [Setting up your space for Support for Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/support-setting-up.html): Support for Amazon CodeCatalyst manages support cases as part of Support API integration with CodeCatalyst.
- [Accessing support for CodeCatalyst in the AWS Management Console](https://docs.aws.amazon.com/codecatalyst/latest/userguide/support-for-disconnected-account.html): If the support enabled billing account for a space is disconnected, Support cases associated with the previous space billing account and associated support plan will no longer be visible in Support for Amazon CodeCatalyst.
- [Creating a CodeCatalyst support case in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/creating-a-support-case.html): You can create a support case in the Support for Amazon CodeCatalyst page.
- [Resolving a support case in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/resolving-a-support-case.html): You can resolve open support cases from the Support for Amazon CodeCatalyst page.
- [Reopening a support case in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/reopening-a-support-case.html): You can use the reopen a resolved support case from the Support for Amazon CodeCatalyst page.
