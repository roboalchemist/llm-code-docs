# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration.md

# Deleting SSO configuration

{% hint style="warning" %}
The SSO users will no longer be able to login after the deletion. Before proceeding with the deletion, ensure the following:

* For each organization in the enterprise, there is at least one organization admin account that doesn’t use the SSO authentication.
* There is at least one enterprise admin account that doesn’t use the SSO authentication.
  {% endhint %}

### In the UI <a href="#in-the-ui" id="in-the-ui"></a>

To delete your SSO configuration in the UI:

1. Retrieve your enterprise. See [..](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention") for more details.
2. Select **Administration** > **Single Sign-On**. The **Single Sign-On** page opens.
3. Select **Delete**. The **Delete SSO configuration** dialog opens.
4. In the dialog, confirm the deletion.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-c6afa6771121abf6fde7ffdc8f54a843373401ab%2Fe79146d5dda9e68579fdbf4bb56ac7b999b6ee72.png?alt=media" alt="Confirm the deletion of your SSO configuration in the UI by selecting Delete, in the upper right corner." width="563"><figcaption></figcaption></figure></div>

### Via the Web API <a href="#via-web-api" id="via-web-api"></a>

To delete your SSO configuration via the [web-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api "mention"):

* Use the `api/authentication/connections/delete` endpoint.

### Related pages <a href="#related-pages" id="related-pages"></a>

[about](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about "mention")\
[setting-up-sso](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-sso "mention")\
[editing-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-sso-configuration "mention")\
[troubleshooting](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/troubleshooting "mention")\
[#deleting-sso-account](https://docs.sonarsource.com/sonarqube-cloud/managing-organization/users-and-permissions/user-on-and-offboarding#deleting-sso-account "mention")
