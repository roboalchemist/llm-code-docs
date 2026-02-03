# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/user-management/managing-user-authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/user-management/managing-user-authentication.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/managing-user-authentication.md

# Managing user authentication

By default, authentication is forced.

Authentication can be managed:

* Via the SonarQube Server built-in users/groups database. See [creating-users](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/user-management/creating-users "mention")
* Via several delegated authentication methods, see the [authentication](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication "mention") pages for more information.

### Disabling forced user authentication <a href="#disabling-forced-authentication" id="disabling-forced-authentication"></a>

You can disable forced user authentication, and allow anonymous users to browse projects and run analyses in your instance. To do so, you need the Administer System permission.

{% hint style="warning" %}
Disabling forced authentication can expose your SonarQube Server instance to security risks. We strongly recommend forcing user authentication on production instances or carefully configuring the security (user permissions, project visibility, etc.) on your instance. See also **Accessible API endpoints if forced authentication is disabled** below.

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
