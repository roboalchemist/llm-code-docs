# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-sso.md

# Setting up SSO

With the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features), you can transition from the DevOps platform authentication mode to Single Sign On (SSO) with any identity provider (IdP) that supports SAML. SonarQube Cloud uses the Service Provider (SP) initiated SSO.

With SSO you benefit from:

* Increased security and a single source of truth for user authentication.
* [automatic-group-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about/automatic-group-synchronization "mention").
* Just-in-Time user provisioning. When a user signs up with SonarQube Cloud with SSO for the first time, their SSO user account is automatically created in SonarQube Cloud.

SSO is set up for a given enterprise, see [setting-up-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-your-enterprise "mention") for more information. At SSO login time, users select the enterprise they want to access.

For more information, see [about](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about "mention").

To set up SSO in your enterprise:

1. Verify the user groups of the enterprise’s organizations to ensure proper user onboarding through automatic group synchronization. For more information, see [automatic-group-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about/automatic-group-synchronization "mention") for more details.

To do so, verify that:

* The user groups defined in your IdP service exist in the relevant organizations of your SonarQube Cloud enterprise (i.e. a group with the same (context-sensitive) name exists in the relevant organization(s)).
* The user groups in SonarQube Cloud have the correct permissions.

To manage the user groups in SonarQube Cloud, see [user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-groups "mention").

For more information, see [verify-user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups "mention").

2. Transition your enterprise to SSO [setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup "mention") to Setting up Single Sign-On
3. Send the SSO login URL to [inviting-users-to-sign-in](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in "mention") to sign in to SonarQube Cloud with SSO. Once they have signed in, their SSO account is created in SonarQube Cloud and they have access to their organization(s) through the automatic group synchronization with the identity provider. They should:

* Check that they have access to their organization(s) and can perform their tasks as before.
* Generate their analysis tokens with their SSO account. (They can still use their DevOps platform service (DOP) account tokens to execute analysis as long as their DOP account still exists).

4\. Sign up with SonarQube Cloud by using the enterprise’s SSO log in URL. Your SSO account has been created.

5\. Sign in to SonarQube Cloud with your DOP account and grant your SSO account the Administer Enterprise permission. See [#manage-permissions](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise#manage-permissions "mention") for more information.

6\. Once the enterprise users have successfully transitioned to SSO, you can remove their DOP accounts from the organizations and the users can delete their DOP account. See [user-on-and-offboarding](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-on-and-offboarding "mention") for more details. We recommend that you don’t remove the admin DOP accounts since, with a SSO account, you cannot bind a SonarQube Cloud organization with the corresponding DOP organization. See [onboarding-new-org](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/onboarding-new-org "mention") for more information.

{% hint style="warning" %}
When created, SSO accounts will have no history. That means that comments on issues, favorite projects, etc., will not be transferred from the corresponding DOP account’s history.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-up-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-your-enterprise "mention")\
  View the different steps necessary to create and configure an enterprise.
* [viewing-billing-usage-info](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-billing-usage-info "mention")
* [onboarding-new-org](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/onboarding-new-org "mention")
