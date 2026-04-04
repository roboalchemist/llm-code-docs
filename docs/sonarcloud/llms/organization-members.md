# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members.md

# Adding organization members

This page explains how to manually add users to your organization. Adding users manually is not necessary (and not possible) if:

* The GitHub member synchronization is activated. See [devops-platform-authentication](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/devops-platform-authentication "mention") for more details. If your users are onboarded through GitHub, the organization member synchronization between GitHub and SonarQube Cloud is enabled by default.
* Or the automatic group synchronization is activated. If your enterprise users are onboarded with your SSO identity provider, synchronized group members are automatically added to the respective organization.

{% hint style="warning" %}

* The Free plan limits the maximum authorized number of members. See [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") for more details.
* Be aware that, when you import an organization to SonarQube Cloud, the account you use for the import is added as a member of the organization (with the Administer Organization permission). If you want that your other SonarQube Cloud account(s) be also part of the organization, you must add them manually. For example, if you imported a GitHub organization by using your GitHub account and you are now logged in to SonarQube Cloud with your Azure DevOps account, then you will not view your GitHub organization if you haven’t added your Azure DevOps account as a member of this organization. For more information, see [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention").
  {% endhint %}

You must be an organization admin to be able to add or remove organization members. You can only add users to an organization who have already signed up with SonarQube Cloud.

To add or remove a member to/from your organization:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Members**.
3. To add a member:
   * Select the **Add a member** button. The **Add member** dialog opens.
   * Enter the exact email address of the member.
   * Select **Add member**.\
     If you cannot see the email address of a DevOps platform user account, it may be because the address has not been verified. See [signing-in](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/signing-in "mention") for more information
4. To remove a member, select the three-dot menu to the far right of the member’s name.
5. In the menu, select **Remove from organization’s members**. The **Remove user** dialog opens.
6. Confirm the deletion.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setup-overview](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setup-overview "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/introduction "mention") to Managing your subscription
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/introduction "mention") to Performing global analysis setup
* [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention")
* [organization-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-permissions "mention")
* [projects-management-page](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/manage-org-projects/projects-management-page "mention")
