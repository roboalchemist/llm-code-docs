# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/user-management/updating-scm-details.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/updating-scm-details.md

# Associating with SCM account

{% hint style="info" %}
SonarQube Server users can view the SCM accounts associated with their account: see [viewing-user-profile](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-your-account/viewing-user-profile "mention").
{% endhint %}

### About the SCM account association <a href="#about-associated-scm-accounts" id="about-associated-scm-accounts"></a>

SonarQube Server associates users with SCM (Source Control Management) accounts to automatically assign issues to users:

* If SonarQube Server delegates the authentication to a third-party identity provider, this association is done through the delegation. However, you can associate the user with additional SCM accounts.
* If no delegation is used, SonarQube Server recognizes the SCM account from the SonarQube Servers account’s Login and/or Email address. If it cannot perform the association (or if you want to associate other SCM accounts with the user account), you can do it explicitly.

To add an SCM account to a SonarQube Server user account, you associate the SCM account’s login name or email address with the SonarQube Server account.

{% hint style="warning" %}
You should not associate the same SCM account with several SonarQube Server accounts; otherwise, SonarQube Server may not be able to properly assign issues to SonarQube Server users. In particular, this means that you should not configure the same email address in several SonarQube Server user accounts (Note that the email address check is case-insensitive in SonarQube Server). To ensure a proper issue assignment, SonarQube Server may reject a user login attempt, for example, if a SAML user logs in with an email address that is associated with a local user (In this case, the error "This account is already associated with another authentication method" is raised).
{% endhint %}

### Adding an SCM account to a SonarQube Server user account <a href="#adding" id="adding"></a>

1. Got to **Administration** > **Security** > **Users** and retrieve the user (see [viewing-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/viewing-users "mention")).
2. In the user’s **Actions** column, select the three-dot menu.
3. Select **Update (SCM) details**.
4. Near **SCM Accounts**, select **Add**. A box is displayed.
5. In the box, enter the SCM account’s login or email address.
6. To add another account, re-select **Add**, etc.
7. Select **Update**. The added SCM accounts are displayed in the **SCM Accounts** column as illustrated below.

The figure below shows:

1. The user's login name and email address.
2. The login name or email address added to the user account as *SCM account*.

<figure><img src="broken-reference" alt="The Security > Users menu allows you to manage the SCM account association"><figcaption></figcaption></figure>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [viewing-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/viewing-users "mention")
* [solution-overview](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview "mention")
* [#local-user-concept](https://docs.sonarsource.com/sonarqube-server/authentication/overview#local-user-concept "mention")
