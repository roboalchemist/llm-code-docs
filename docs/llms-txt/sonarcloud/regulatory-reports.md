# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/viewing-reports/regulatory-reports.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/regulatory-reports.md

# Regulatory reports

Starting in [Enterprise](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can download a regulatory report for any permanent branch of a project. A permanent branch is one that has been set to **Keep when inactive**, see [maintaining-the-branches-of-your-project](https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/maintaining-the-branches-of-your-project "mention") for details.

### Downloading regulatory reports <a href="#downloading-regulatory-reports" id="downloading-regulatory-reports"></a>

To download a regulatory report:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information.
2. On the Overview page, click **Downloadable reports** and select **Download Regulatory report (.zip)** from the drop down menu.

Alternatively:

1. Select **Project Information** from the project’s navigation bar.
2. In the **Regulatory Report** section, choose a project branch from the drop down menu.
3. Click **Download report**.

SonarQube generates the report for download, which may take a few minutes depending on the size of the project.

### Contents of the regulator report’s ZIP file <a href="#contents-regulatory-reports-zip-file" id="contents-regulatory-reports-zip-file"></a>

The reports are in a ZIP file containing a snapshot of the latest analysis of the selected branch and include TXT, CSV, and PDF files.

The PDF file includes:

* **Project overview**:
  * Project details
  * Quality gates information and status
* **Project rating** **overview** for:
  * New code broken down by new issues, accepted issues, coverage, duplication, and security hotspots.
  * Overall code broken down by security, reliability, maintainability (in [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention")) or vulnerabilities, bugs, and code smells (in [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention")), accepted issues, coverage, duplication, and security hotspots.
* **Distribution of issues in new code** showing open issues and breakdown by severity, based on security, reliability, maintainability (in [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention")) or vulnerabilities, bugs, and code smells (in [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention")).
* **Distribution of issues in overall code** showing open issues and breakdown by severity, based on security, reliability, maintainability (in [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention")) or vulnerabilities, bugs, and code smells (in [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention")).
* **Quality gate and quality profiles** information.
* **Files** lists all relevant files included in the ZIP file.
* **Definitions** lists all the definitions of terms related to the report.

Depending on the configuration of your SonarQube Server instance, the regulatory report is generated with metrics either from [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention") or [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention"). Some CSV files may contain metrics from both modes and they are marked accordingly.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [security-reports](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/security-reports "mention")
* [pdf-reports](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/pdf-reports "mention")
* [portfolios](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/portfolios "mention")
* [other-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/other-issues "mention")
