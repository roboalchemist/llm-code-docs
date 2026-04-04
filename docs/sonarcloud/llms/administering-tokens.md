# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/security/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/user-management/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/security/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/security/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/security/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/security/administering-tokens.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/security/administering-tokens.md

# Tokens

As a System Administrator, you can generate tokens of type **User** on behalf of another user and you can revoke any token. For more information about tokens and how to manage your own tokens, see [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention").

### Generating a token on behalf of another user <a href="#generating-user-token" id="generating-user-token"></a>

1. In **Administration** > **Security** > **Users**, retrieve the user (see [viewing-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/viewing-users "mention")).
2. In the user’s **Tokens** column, select the three-dot menu. The **Tokens** dialog opens.
3. Enter the token name, check the expiration date, and select **Generate**.

### Revoking a token <a href="#revoking-token" id="revoking-token"></a>

1. In **Administration** > **Security** > **Users**, retrieve the user (see [viewing-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/viewing-users "mention")).
2. In the user’s **Tokens** column, select the three-dot menu. The **Tokens** dialog opens with the list of tokens.
3. In the **Actions** column of the token, select **Revoke**.

### Enforcing a maximum lifetime for tokens (from Enterprise Edition) <a href="#enforcing-max-lifetime-for-tokens" id="enforcing-max-lifetime-for-tokens"></a>

The ability to configure a maximum lifetime for tokens is available starting in [Enterprise Edition](https://www.sonarsource.com/plans-and-pricing/enterprise/).

As a System Administrator, you can define a maximum lifetime for any *newly* generated token. Non-administrator users can also set a time-to-live as long as it is less than or equal to the maximum lifetime configured at the system level. Tokens generated after updating this setting will expire either at the configured maximum lifetime or at the time set by the user, whichever comes first.

{% hint style="info" %}
Updating this setting does *not* affect any existing tokens. It will only impact newly generated tokens.
{% endhint %}

To enforce a maximum lifetime for tokens at the system level:

1. Go to **Administration** > **Configuration** > **General Settings** > **Security**.
2. In **Maximum allowed lifetime for token**, select the lifetime you want to set.
