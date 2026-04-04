# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/user-account/generating-and-using-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/user-account/generating-and-using-tokens.md

# Generating and using tokens

SonarQube users can generate tokens that can be used to run analyses or invoke web services without access to the user’s actual credentials. You can generate new tokens at **User** > **My Account** > **Security.**

### Types of tokens <a href="#types-of-tokens" id="types-of-tokens"></a>

#### User tokens <a href="#user-tokens" id="user-tokens"></a>

These tokens can be used to invoke web services, based on the token author’s permissions, and are the preferred authentication method used by SonarLint when setting up [SonarLint Connected Mode](https://app.gitbook.com/s/Bmptmznn7RpPe5u7vdup/user-guide/sonarlint-connected-mode "mention"). A user token gives you all the permissions of the user who issued it. For example, a global admin’s user token gives you full rights to the instance.

User tokens allow you to perform, via the [web-api](https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/web-api "mention"), any action the user can do via the UI.

{% hint style="info" %}
When using tokens to set up [sonarlint-connected-mode](https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/sonarlint-connected-mode "mention") in SonarLint, *user tokens are required*. Note that the binding will not function properly if *project tokens* or *global tokens* are used during the setup process. Check the SonarLint documentation for more details:

* [Connected mode](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/connected-mode)
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/connected-mode)
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode)
* [Connected mode](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connected-mode)
  {% endhint %}

#### Project analysis tokens <a href="#project-analysis-tokens" id="project-analysis-tokens"></a>

A project analysis token allows you to run analyses on the specific project it was generated for.

To create a project analysis token, the user should have Global Execute Analysis permission or Execute Analysis permission on the token’s associated project.

If the token’s author loses Execute Analysis permissions for the associated project, the token will no longer be valid for performing an analysis.

{% hint style="info" %}
The usage of project analysis tokens is encouraged for security reasons. If such a token were to leak, an attacker would only gain access to analyze a single project or to interact with the related web services requiring Execute Analysis permissions.
{% endhint %}

#### Global analysis tokens <a href="#global-analysis-tokens" id="global-analysis-tokens"></a>

These tokens can be used to run analyses on every project.

To create global analysis tokens, the user should have Global Execute Analysis Permission.

If the token’s author loses the Global Execute Analysis permission, the token will no longer be valid for performing an analysis.

### Generating a token <a href="#generating-a-token" id="generating-a-token"></a>

You can generate new tokens at **User** > **My Account** > **Security**.

The form at the top of the page allows you to generate new tokens, specifying their token type. You can select an expiration for your token or choose "no expiration". If you select an expiration date, and your system administrator has configured SonarQube to send email notifications, you will receive an email 7 days prior to your token’s expiry date to remind you to rotate your token. If the token is not revoked before expiring, you will receive another email once the token has expired to notify you the token is no longer usable.

If an Administrator has enforced a maximum lifetime for tokens, then the "no expiration" option will not be available and the maximum allowed expiration will correspond to the maximum token lifetime allowed by your organization. Enforcing a maximum lifetime for all newly generated tokens is available as part of the [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) and above; for more information, please see [security](https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/security "mention").

Once you select **Generate**, you will see the token value. Copy it immediately; when you dismiss the notification, you will not be able to retrieve it.

### Revoking a token <a href="#revoking-a-token" id="revoking-a-token"></a>

You can revoke an existing token at **User** > **My Account** > **Security** by selecting **Revoke** next to the token.

### Expired tokens <a href="#expired-tokens" id="expired-tokens"></a>

If a token has an expiration date and is past the expiration, it will no longer be usable. The token will still be visible under **User** > **My Account** > **Security**, where you can revoke it like any other token.

### Using a token <a href="#using-a-token" id="using-a-token"></a>

User tokens are used in the following scenarios:

* when running analyses on your code, use the token as value of the `sonar.token` property, or create the SONAR\_TOKEN environment variable and set the token as its value.
* when invoking web services, pass the token using the bearer or basic HTTP authentication scheme (see [web-api](https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/web-api "mention")).

In both cases, you don’t need to provide a password. Using a token is the preferred method over using a login and password.

#### Expiration date in HTTP response <a href="#expiration-date-in-http-response" id="expiration-date-in-http-response"></a>

When using a token to interact with web services, a `SonarQube-Authentication-Token-Expiration` HTTP header will be added to the response. This header contains the token expiration date and can help third-party tools track upcoming expirations; this method allows the token to be rotated in time.
