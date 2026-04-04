# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/viewing-reports/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/pdf-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/pdf-reports.md

# PDF reports

*PDF reports are available as part of* [*Enterprise Edition*](https://www.sonarsource.com/plans-and-pricing/enterprise/) *and above.*

{% hint style="info" %}
The content on this page is aimed at developers who want to get PDF reports and subscribe to updates. If you're an admin, see [pdf-reports](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/pdf-reports "mention") in the instance administration section.
{% endhint %}

The PDF reports focus mainly on new code and quality gate conditions. This means that, if there are failing conditions on the overall code, they will appear in the report as well.

Depending on the configuration of your SonarQube Server instance, the PDF reports are generated with metrics either from [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention") or [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention").

### Project and application PDF reports <a href="#project-and-application-pdf-reports" id="project-and-application-pdf-reports"></a>

You can download PDF reports for a permanent branch of a project or application and subscribe to regular updates. The frequency with which you receive reports is set by a project or system administrator. See [maintaining-the-branches-of-your-project](https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/maintaining-the-branches-of-your-project "mention") for more information.

To download a PDF report for a project or application:

1. Retrieve the project or application. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information.
2. In the upper right corner of the project or application’s Overview page, click **Project PDF report** or **Application PDF report** and select **Download** or **Subscribe to report** from the drop-down menu.

{% hint style="info" %}
You cannot download or subscribe to a PDF report for a temporary branch. If you are unable to download or subscribe to a PDF report for a branch, go to **Project Settings** > **Branches and Pull Requests** and make sure that the **Keep when inactive** toggle is on for that branch (you must be a project admin).
{% endhint %}

### Portfolio PDF reports <a href="#portfolio-pdf-reports" id="portfolio-pdf-reports"></a>

You can download a PDF report for a portfolio from the portfolio’s Overview page by selecting **Portfolio PDF report** from the upper-right corner and clicking **Download**. This is really convenient, for example, if you’re going into a meeting where you may not have access to your SonarQube Server instance.

You can subscribe to receive a PDF by email by selecting **Subscribe to report** from the **Portfolio PDF report** drop-down menu. The default subscription frequency is monthly, but a portfolio administrator can change it. See [managing-portfolios](https://docs.sonarsource.com/sonarqube-server/project-administration/managing-portfolios "mention") for more information.

{% hint style="info" %}
You will only receive the PDF when the portfolio is computed.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [security-reports](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/security-reports "mention")
* [regulatory-reports](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/regulatory-reports "mention")
* [portfolios](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/portfolios "mention")
* [pdf-reports](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/pdf-reports "mention")
