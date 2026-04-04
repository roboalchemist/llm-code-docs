# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/maintenance/deprecations/api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/monitoring/api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/monitoring/api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/monitoring/api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/monitoring/api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/monitoring/api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/api-deprecation.md

# API deprecation

If you use custom plugins based on the plugin API or consume SonarQube Server services through the [web-api](https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/web-api "mention") then you will have to manage the possible API deprecations. See also the [web-api](https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/web-api "mention") and the [plugin-basics](https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/plugin-basics "mention") pages.

### Monitoring the deprecated Web API components <a href="#web-api" id="web-api"></a>

After an upgrade, you can check if an authenticated client of your SonarQube Server instance uses deprecated Web API endpoints and parameters in order to anticipate their drop. To do so, browse the deprecation log as illustrated below.

<figure><img src="https://3560343708-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4FzELVjsPO4ijRo3jtBV%2Fuploads%2Fgit-blob-4b53c5d66dfe84d90dc406247b5c00adf19b9329%2Fsonarqube-deprecation-log.png?alt=media" alt="Deprecation logs"><figcaption></figcaption></figure>

To download the deprecation log from the UI (with the **Administer System** permission):

1. In the top navigation bar of the SonarQube Server UI, select **Administration > System**.
2. In the top right corner of the **System Info** page, click **Download Logs > Deprecation Logs**.

{% hint style="info" %}
You can automate the retrieval of the deprecation log information by calling the Web API endpoint [`api/system/logs`](https://next.sonarqube.com/sonarqube/web_api/api/system/logs) with `deprecation` as the value of the `name` parameter.
{% endhint %}

### Monitoring the deprecated Plugin API components <a href="#plugin-api" id="plugin-api"></a>

Check the [Plugin API release notes](https://github.com/SonarSource/sonar-plugin-api/releases) for deprecation notes.
