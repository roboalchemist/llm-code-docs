# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-on-and-offboarding.md

# User onboarding and offboarding

### User onboarding <a href="#onboarding-users" id="onboarding-users"></a>

Whether through a DevOps platform or an SSO identity provider, when users first sign up with SonarQube Cloud, their account is automatically created in SonarQube Cloud.

At login time, users are automatically added to organizations in the following cases:

* With a DevOps platform (DOP) service, through the GitHub member synchronization. In this case, you cannot add DOP users manually.
* In an SSO-enabled enterprise, through group synchronization wiht the identity provider. You cannot add SSO users manually.

Otherwise, you must manually add the DOP users to their organization, see [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention") for more information.

{% hint style="info" %}
In an SSO-enabled enterprise, DOP users can be added manually to organizations.
{% endhint %}

### Deleting a DOP account <a href="#deleting-dop-account" id="deleting-dop-account"></a>

You can only delete your own account, see [deleting](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/deleting "mention"). If you want to delete another user’s DevOps platform (DOP) account:

* If the GitHub member synchronization is used, remove the user from the GitHub organization.
* Otherwise, remove the user’s DOP account from the SonarQube Cloud organizations they are a member of, see [organization-members](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/organization-members "mention").

### Deleting an SSO account <a href="#deleting-sso-account" id="deleting-sso-account"></a>

You can only delete your own account, see [deleting](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/deleting "mention")for more details.

To prevent an SSO user from logging in to your SonarQube Cloud organizations, remove their access rights from the identity provider.
