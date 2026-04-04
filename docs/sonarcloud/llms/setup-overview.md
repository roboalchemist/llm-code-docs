# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview.md

# Organization setup overview

For the Single Sign-On (SSO) authentication, see [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention").

To set up a new organization in SonarQube Cloud:

1. Select the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") you want to assign to your new SonarQube Cloud organization.
2. Import your DevOps platform organization (or workspace, group, etc.). The corresponding SonarQube Cloud organization is automatically created and is bound to the DevOps platform organization, see [binding-with-dop](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/ressources-structure/binding-with-dop "mention"). You’re granted Administer permission on the new organization.\
   Refer to:
   * [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
   * [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
   * [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
   * [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
3. Set project configuration at the organization level. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/introduction "mention") to Performing global analysis setup.
4. Invite your DevOps platform organization users to sign up for SonarQube Cloud. Their SonarQube Cloud account will be automatically created.
5. If you use a GitHub platform with automatic member synchronization, the organization members are automatically synchronized in SonarQube Cloud. Otherwise, you must add the SonarQube Cloud users to your organization manually. See [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention") for more information.
6. Manage the permissions of the users and groups. In particular:
   * Create the user groups in your organization. See [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention") for more details.
   * Define the users and groups that can create projects in the organization. See [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention") for more information.
   * Verify the default permissions on new projects. See [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention") for more details.
7. Authorized organization members can now create projects. See [setting-up-project](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-up-project "mention") for more information.
8. Set up a dedicated [security-contact](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/security-contact "mention") for urgent, security-related communications.
