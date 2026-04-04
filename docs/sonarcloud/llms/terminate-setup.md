# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/terminate-setup.md

# Step 4: Terminate SSO setup

To terminate the transition of your enterprise to SSO:

1. Sign up with SonarQube Cloud by using the enterprise’s SSO log in URL. Your SSO account is created.
2. Sign in to SonarQube Cloud with your DOP account and grant your SSO account the Administer Enterprise permissions. See [..](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more details.
3. Once the enterprise users have successfully transitioned to SSO you can remove their DOP accounts from the organizations and the users can delete their DOP account. If you use Bitbucket Cloud, we recommend that you don’t remove the *admin* DOP accounts since, with an SSO account, you currently cannot bind a SonarQube Cloud organization with a Bitbucket Cloud workspace.

### Related pages <a href="#related-pages" id="related-pages"></a>

[verify-user-groups](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/verify-user-groups "mention")\
[configure-sso](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/configure-sso "mention")\
[inviting-users-to-sign-in](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/setup/inviting-users-to-sign-in "mention")\
[editing-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-sso-configuration "mention")\
[deleting-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration "mention")
