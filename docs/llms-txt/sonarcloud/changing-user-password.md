# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/user-management/changing-user-password.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/changing-user-password.md

# Changing user password

### Changing the password in the UI <a href="#ui" id="ui"></a>

1. In **Administration > Security > Users**, retrieve the user (see [viewing-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/viewing-users "mention")).
2. In the user’s **Actions** column, select the three-dot menu.
3. Select **Enter a new password**.

{% hint style="info" %}
You cannot change any user password in the UI (even of user accounts not tied to a third-party provider) if your system has enabled automatic provisioning mode.
{% endhint %}

### Changing the password through the API <a href="#api" id="api"></a>

Use the web service [`api/users/change_password`](https://next.sonarqube.com/sonarqube/web_api/api/users/change_password).

### Related pages <a href="#related-pages" id="related-pages"></a>

* [creating-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/creating-users "mention")
* [deactivating-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/deactivating-users "mention")
* [changing-password](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-your-account/changing-password "mention")
