# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/security/user-accounts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/security/user-accounts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/security/user-accounts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/security/user-accounts.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/security/user-accounts.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/security/user-accounts.md

# User accounts

By default, authentication is forced.

Authentication can be managed:

* Via the SonarQube Server built-in users/groups database. See [creating-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/creating-users "mention")
* Via several delegated authentication methods, see [authentication](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication "mention") for more information.

To change the password of a manually created account, see [changing-user-password](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/changing-user-password "mention").

To deactivate a user account, see [deactivating-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/deactivating-users "mention").

To manage the user account permissions, see:

* [user-permissions](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions "mention")
* [setting-project-permissions](https://docs.sonarsource.com/sonarqube-server/project-administration/setting-project-permissions "mention")

### Disabling forced user authentication <a href="#disabling-forced-authentication" id="disabling-forced-authentication"></a>

You can disable forced user authentication, and allow anonymous users to browse projects and run analyses in your instance. To do so, you need the Administer System permission.

{% hint style="warning" %}
Disabling forced authentication can expose your SonarQube Server instance to security risks. We strongly recommend forcing user authentication on production instances or carefully configuring the security (user permissions, project visibility, etc.) on your instance. See also [#accessible-api-endpoints-if-forced-authentication-disabled](#accessible-api-endpoints-if-forced-authentication-disabled "mention") below.

We advise keeping forced authentication if you have your SonarQube Server instance publicly accessible.
{% endhint %}

<details>

<summary>Accessible API endpoints if forced authentication disabled</summary>

If forced authentication is disabled, the following API endpoints are accessible **without authentication**:

* api/components/search
* api/issues/tags
* api/languages/list
* api/metrics/domains
* api/metrics/search
* api/metrics/types
* api/plugins/installed
* api/project\_tags/search
* api/qualitygates/list
* api/qualitygates/search
* api/qualitygates/show
* api/qualityprofiles/backup
* api/qualityprofiles/changelog
* api/qualityprofiles/export
* api/qualityprofiles/exporters
* api/qualityprofiles/importers
* api/qualityprofiles/inheritance
* api/qualityprofiles/projects
* api/qualityprofiles/search
* api/rules/repositories
* api/rules/search
* api/rules/show
* api/rules/tags
* api/server/version
* api/settings/login\_message
* api/sources/scm (for public repositories)
* api/sources/show (for public repositories)
* api/system/db*migration*status
* api/system/migrate\_db
* api/system/ping
* api/system/status
* api/system/upgrades
* api/users/search
* api/webservices/list
* api/webservices/response\_example

</details>

To disable forced authentication:

1. Go to **Administration** > **Configuration** > **General Settings** > **Security.**
2. Disable **Force user authentication**.
