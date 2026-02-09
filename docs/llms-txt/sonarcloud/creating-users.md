# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/user-management/creating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/creating-users.md

# Creating users manually

You can create a user account manually in SonarQube Server. Manually created users are authenticated against SonarQube Server’s own user/group database. In contrast, users can be provisioned and authenticated through an external tool such as GitHub, GitLab, SAML Identity Provider, LDAP service, etc. (For more information, see [overview](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/overview "mention").).

You need the global Administer System permission to create user accounts.

{% hint style="info" %}
If you enable the automatic provision mode in SonarQube with an identity provider, you cannot manually create users and the existing manually created users become *local users*. For more information, see [#local-user-concept](https://docs.sonarsource.com/sonarqube-server/authentication/overview#local-user-concept "mention").
{% endhint %}

To create a user account:

1. In the top navigation bar, go to **Administration > Security > Users**.
2. Select the **Create User** button. The **Create User** dialog opens.
3. In the dialog, enter the **Login** (user identifier), **Name** (account’s screen name), **Email** (optional), and **Password**.
4. If the entered login or email address does not match the user’s SCM account login, you can explicitly associate the SCM account with the manual account: see [updating-scm-details](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/updating-scm-details "mention").
5. Select **Create**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [changing-user-password](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/changing-user-password "mention")
* [deactivating-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/deactivating-users "mention")
