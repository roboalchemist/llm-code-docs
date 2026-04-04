# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/managing-tokens.md

# Managing Personal Access Tokens

Each user has the ability to generate tokens that can be used to run analyses or invoke web services without access to the user’s actual credentials. When a user is deleted, their user access tokens are also deleted.

{% hint style="warning" %}
From the Team plan, it's highly recommended to use Scoped Organization Tokens (SOT) instead of PATs. For more information, see [scoped-organization-tokens](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/scoped-organization-tokens "mention").
{% endhint %}

{% hint style="info" %}
For security reasons, tokens that have been inactive for 60 days will be automatically removed.
{% endhint %}

To generate a token, select your account menu in the top right corner of the SonarQube Cloud interface. In the menu, select **My Account** > **Security**. Your existing tokens are listed here, each with a **Revoke** button.

The form at the top of the page allows you to generate new tokens. Once you select **Generate**, you will see the token value. Copy it immediately; if your dismiss the notification or leave the page, you will not be able to retrieve the token's value.

Tokens are used as a replacement for your usual login:

* When running analyses on your code. Replace your login with the token in the `sonar.token` property. (Note that the property `sonar.password` is deprecated.)
* When invoking web services. See [web-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api "mention") for more details.

In either case, no password is needed.
