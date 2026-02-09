# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in.md

# Step 3: Invite users to sign in

Once you have verified the user groups in your enterprise ([verify-user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups "mention")) and mapped properly the group attributes in your IdP ([configure-sso](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso "mention")), you can invite users to sign in to SonarQube Cloud with SSO. To do so, send them the login URL of your enterprise.

{% hint style="info" %}
SonarQube Cloud uses the Service Provider (SP) initiated SSO (Idp-initiated SSO is not supported). It means that SSO users must go to the login page of SonarQube Cloud.
{% endhint %}

When users sign in with SSO for the first time, their SSO account is created in SonarQube Cloud and they have access to their organization(s) through the automatic group synchronization with the identity provider. They should:

* Check that they have access to their organization(s) and can perform their tasks as before.
* If using Personal Access Tokens (PAT): generate their analysis tokens with their SSO account. (They can still use their DevOps platform service (DOP) account tokens to execute analysis as long as their DOP account still exists). Note that from the Team plan, it's highly recommended to use Scoped Organization Tokens (SOT) instead of PATs.

To retrieve the login URL of your enterprise:

1. Retrieve your enterprise. See [..](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more details.
2. Select **Administration** > **Single Sign-On**. The **Single Sign-On** page opens.
3. Select the copy tool at the right of the **Log in URL** field. You can now paste the copied URL to your invite message.

### Related pages <a href="#related-pages" id="related-pages"></a>

[verify-user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups "mention")\
[configure-sso](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso "mention")\
[terminate-setup](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/terminate-setup "mention")\
[editing-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-sso-configuration "mention")\
[deleting-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration "mention")
