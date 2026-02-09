# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/deprecations/monitoring-api-deprecation.md

# Monitoring API deprecation

If you use custom plugins based on the plugin API or consume SonarQube Server services through the [web-api](https://docs.sonarsource.com/sonarqube-server/extension-guide/web-api "mention") then you will have to manage the possible API deprecations. See also the [deprecation-policy](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/deprecations/deprecation-policy "mention").

### Monitoring the deprecated Web API components <a href="#web-api" id="web-api"></a>

After an update, you can check if an authenticated client of your SonarQube Server instance uses deprecated Web API endpoints and parameters in order to anticipate their drop. To do so, browse the deprecation log as illustrated below.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/HVGuhsOIleL1us7wqiwZ/sonarqube-deprecation-log.png" alt="The screenshot highlights the line-by-line information available in the SonarQube deprecation logs." width="563"><figcaption></figcaption></figure></div>

To download the deprecation log from the UI (with the **Administer System** permission):

1. In the top navigation bar of the SonarQube Server UI, select **Administration** > **System**.
2. In the top right corner of the **System Info** page, click **Download Logs** > **Deprecation Logs**.

{% hint style="info" %}
You can automate the retrieval of the deprecation log information by calling the Web API endpoint [`api/system/logs`](https://next.sonarqube.com/sonarqube/web_api/api/system/logs) with `deprecation` as the value of the `name` parameter.
{% endhint %}

### Monitoring the deprecated Plugin API components <a href="#plugin-api" id="plugin-api"></a>

Check the [Plugin API release notes](https://github.com/SonarSource/sonar-plugin-api/releases) for deprecation notes.
