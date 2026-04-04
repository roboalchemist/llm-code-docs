# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/onboarding-new-org.md

# Onboarding a new organization

To perform this procedure, you must be an admin of your enterprise. The procedure is different if the enterprise is SSO-enabled or not.

### Without SSO <a href="#without-sso" id="without-sso"></a>

1. Create your organization in SonarQube Cloud by importing the DevOps platform organization and select the Free plan. See:
   * [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
   * [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
   * [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
   * [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
2. Add the organization to the enterprise:
   * Retrieve your enterprise.
   * Go to **Administration** > **Organizations** and select **Add organization**.
3. Optionally, allocate an individual LOC limit to the organization. See [#allocating-loc-limit](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-lines-of-code-within-your-enterprise#allocating-loc-limit "mention").
4. Create the organization's user groups. See [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention") for more details.
5. Verify the groups' default permissions on new projects in the organization. See [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention") for more details.
6. Set project configurations at the organization level. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/introduction "mention") to Performing global analysis setup for more details.
7. Set the enterprise permissions for the new enterprise members. See [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more details.
8. Authorized organization members can now create projects or portfolios.

### With SSO <a href="#with-sso" id="with-sso"></a>

The procedure below explains how to onboard a new organization on an SSO-enabled enterprise.

1. Create your organization in SonarQube Cloud by importing the DevOps platform organization and select the Free plan. See:
   * [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
   * [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
   * [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
   * [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
2. Add the organization to the enterprise:
   * Retrieve your enterprise.
   * Go to **Administration** > **Organizations** and select **Add organization**.
3. Optionally, allocate an individual LOC limit to the organization. See [#allocating-loc-limit](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/managing-the-lines-of-code-within-your-enterprise#allocating-loc-limit "mention").
4. Create the organization's user groups in order to ensure that the automatic group synchronization can take place properly. See [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention") for more details. Make sure that:
   * The relevant user groups defined in your IdP service exist in your organization (i.e. a group with the same name exists in the organization).
   * The user groups in your organizations have the correct organization-related permissions. See [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention") for more information.
5. Verify the groups' default permissions on new projects in the organization. See [templates](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/manage-project-permissions/templates "mention") for more details.
6. Set the enterprise permissions at the organization level. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/introduction "mention") to Performing global analysis setup for more information.
7. Set the enterprise permissions of the new enterprise members. See [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more information.
8. Invite your DevOps platform organization users to sign up for SonarQube Cloud. See [inviting-users-to-sign-in](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in "mention") for more details. Their SonarQube Cloud SSO account will be automatically created.
9. Authorized organization members can now create projects or portfolios.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-up-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-your-enterprise "mention")\
  View the different steps necessary to create and configure an enterprise.
* [viewing-billing-usage-info](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-billing-usage-info "mention")
* [setting-up-sso](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-sso "mention")
* [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention")
