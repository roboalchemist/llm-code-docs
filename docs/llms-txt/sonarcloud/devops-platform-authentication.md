# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/devops-platform-authentication.md

# Default authentication through DevOps platform

With the DevOps platform service authentication:

* Just-in-Time user provisioning is used. When a user signs up with SonarQube Cloud for the first time through their DevOps platform (DOP), their DOP user account is automatically created in SonarQube Cloud.
* The automatic member synchronization is supported with GitHub. See [github-member-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/github-member-synchronization "mention") for more information.

### Authentication flow

Users log directly into SonarQube Cloud with their DevOps platform (DOP) credentials which are transmitted to an Auth0 server for authentication. Auth0 bridges SonarQube Cloud and the DOP service.

The authentication flow is as follows:

1. The user enters their login for their DOP via SonarQube Cloud.
2. SonarQube Cloud redirects the authentication request to Auth0.
3. Auth0 forwards the request to the DOP service.
4. The DOP authenticates the user and sends the authentication response to Auth0.
5. Auth0 forwards the authentication response to SonarQube Cloud.
6. SonarQube Cloud performs extra-authentication checks. If successful, the user is authenticated in SonarQube Cloud.

<figure><img src="broken-reference" alt="Users log directly into SonarQube Cloud with their DevOps platform (DOP) credentials which are transmitted to an Auth0 server for authentication. Auth0 bridges SonarQube Cloud and the DOP service."><figcaption></figcaption></figure>

{% hint style="info" %}
Auth0 may connect to the DOP service from one of the IP addresses listed [here](https://auth0.com/docs/secure/security-guidance/data-security/allowlist).
{% endhint %}

### User login format <a href="#user-login-format" id="user-login-format"></a>

When creating a new user login, SonarQube Cloud systematically adds a random suffix to the login name to manage user misidentification risk.

{% hint style="info" %}
When setting up API-based automations related to users, don’t use the `login` field to retrieve a user. Use the `email` field instead.
{% endhint %}

### Azure DevOps service authentication <a href="#azure-devops-service-authentication" id="azure-devops-service-authentication"></a>

The following applies for Azure DevOps service authentication in SonarQube Cloud:

* ID tokens are used.
* Both personal and organizations accounts are supported (the multi-tenant endpoint is used).
* The following scopes are required: `User.Read`, `openid`, `profile`, and `email`.

### Related page <a href="#related-pages" id="related-pages"></a>

[user-on-and-offboarding](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/users-and-permissions/user-on-and-offboarding "mention")\
[github-member-synchronization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/about-sonarqube-cloud-solution/user-management/github-member-synchronization "mention")\
[sso](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/enterprise-security/sso "mention")
