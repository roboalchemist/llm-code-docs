# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/notifications/slack/about.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack/about.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about.md

# About SSO authentication solution

The SonarQube Cloud Enterprise plan supports a transition from the DevOps platform authentication mode to Single Sign On (SSO) with any identity provider (IdP) that supports SAML. SonarQube Cloud uses the Service Provider (SP) initiated SSO. See the [introduction](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/introduction "mention") to Enterprise plans for more information about these and other supported features.

With SSO you benefit from:

* Increased security and a single source of truth for user authentication.
* [automatic-group-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about/automatic-group-synchronization "mention").
* Just-in-Time user provisioning; when a users sign up with SonarQube Cloud with SSO for the first time, their SSO user account is automatically created in SonarQube Cloud.

SSO is set up for a given enterprise, see [setting-up-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-your-enterprise "mention") for more details. At SSO login time, users select the enterprise they want to access.

### SAML SSO authentication flow

Users log directly into SonarQube Cloud with their SAML SSO credentials which are transmitted to an Auth0 server for authentication. Auth0 functions as the SAML service provider, bridging SonarQube Cloud and the identity provider.

The authentication flow is as follows:

1. The user enters their login for SAML SSO via SonarQube Cloud.
2. SonarQube Cloud redirects the authentication request to Auth0.
3. Auth0 forwards the SAML request to the SAML identity provider.
4. The SAML identity provider authenticates the user and generates a signed token containing the user’s information and privileges (SAML assertion). It sends the SAML assertion to Auth0. Optionally, the identity provider can encrypt this assertion with SonarQube Server’s certificate. Note that in that case, the SAML response, which contains the encrypted assertion, must be signed.
5. Auth0 sends the token to SonarQube Cloud.
6. SonarQube Cloud receives the token, verifies its signature and performs extra-authentication checks. If successful, the user is authenticated in SonarQube Cloud.

<figure><img src="broken-reference" alt="Users access SonarQube Cloud using their SAML SSO credentials, which are sent to an Auth0 server for authentication. Auth0 functions as the SAML service provider, bridging SonarQube and the identity provider."><figcaption></figcaption></figure>

{% hint style="info" %}
Auth0 may connect to the identity provider from one of the IP addresses listed [here](https://auth0.com/docs/secure/security-guidance/data-security/allowlist).
{% endhint %}

### User login format <a href="#user-login-format" id="user-login-format"></a>

When creating a new user login, SonarQube Cloud systematically adds a random suffix to the login name to manage user misidentification risk.

{% hint style="info" %}
When setting up API-based automations related to users, don’t use the `login` field to retrieve a user. Use the `email` field instead.
{% endhint %}

### Limitations <a href="#limitations" id="limitations"></a>

In an SSO-enabled enterprise:

* SSO users cannot be added to organizations outside of their enterprise.
* The GitHub member synchronization is disabled on any organization of the enterprise.
* Currently, an SSO user cannot bind a SonarQube Cloud organization to its corresponding Bitbucket Cloud workspace. They must use their DevOps platform (DOP) account to perform the binding.
* Both DevOps platform and SSO authentications are supported but only one SSO configuration can be managed.

### Related pages <a href="#related-pages" id="related-pages"></a>

[automatic-group-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/about/automatic-group-synchronization "mention")\
[setting-up-sso](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/setting-up-sso "mention")\
[editing-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/editing-sso-configuration "mention")\
[deleting-sso-configuration](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/deleting-sso-configuration "mention")\
[troubleshooting](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso/troubleshooting "mention")\
[#deleting-sso-account](https://docs.sonarsource.com/sonarqube-cloud/managing-organization/users-and-permissions/user-on-and-offboarding#deleting-sso-account "mention")
