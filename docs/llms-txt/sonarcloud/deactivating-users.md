# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/user-management/deactivating-users.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/deactivating-users.md

# Deactivating users

When you deactivate a user in SonarQube Server:

* Any SonarQube Server tokens associated with the user are revoked.
* You have the possibility to delete the user’s personal data at the same time.

{% hint style="warning" %}
When SonarQube Server authentication is delegated to an external identity provider, deactivating a user on the identity provider side does not remove any tokens associated with the user on the SonarQube Server side. To revoke a token, see [#revoking-token](https://docs.sonarsource.com/sonarqube-server/security/administering-tokens#revoking-token "mention").
{% endhint %}

### Introduction to personal data deletion <a href="#user-data-deletion" id="user-data-deletion"></a>

For legal compliance, you may want to ensure that the personal data of deactivated users is not retained.

SonarQube Server deletes a user’s personal data by anonymizing their data. This feature has the following limitations:

* The user login is changed, making it impossible to reactivate the user by recreating a user with the old login.
* The user’s login may still be stored in issue changelogs and the user’s login, name, and email address may still be stored in audit entries (Audit entries are purged by default after 30 days.).
* The user may still appear in the list of authors and other locations due to SCM (Source Control Management) data.
* Some columns in the database may contain parts of the user’s login if the user was created before the instance was upgraded to SonarQube Server 8.3.

### Deactivating a user in SonarQube Server <a href="#deactivating" id="deactivating"></a>

You need the global Administer System permission to be able to deactivate users in SonarQube Server.

To deactivate a user:

1. In **Administration > Security > Users**, retrieve the user (see[viewing-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/viewing-users "mention")).
2. In the user’s **Actions** column, select the three-dot menu.
3. Select **Deactivate**. The **Deactivate User** dialog opens.
4. Select the **Delete user’s personal information** option if you want to anonymize the user’s personal data.
5. Select **Deactivate**.

### Deleting users’ personal data using the API (deprecated) <a href="#deleting-personal-data-api" id="deleting-personal-data-api"></a>

This feature is deprecated.

You can delete personal data using the API. First, the user needs to be deactivated, then an admin can use the web service `/api/users/anonymize` and pass to it the login of a deactivated user to replace all personal data of the user with anonymized data. Note that the admin is able to retrieve the logins of deactivated users by using `/api/users/search` endpoint with the appropriate parameter.
