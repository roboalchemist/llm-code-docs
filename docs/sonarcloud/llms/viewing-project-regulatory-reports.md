# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-project-regulatory-reports.md

# Viewing project regulatory reports

Starting in [Enterprise](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can download a regulatory report for any long-lived branch of a project, typically the main branch. See [long-lived-branch-pattern](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/long-lived-branch-pattern "mention") if the long-lived branch is other than main.

{% hint style="info" %}
Before you can view the Enterprise-level reports, your organization must be added to an enterprise. For more information, see [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention").
{% endhint %}

### Downloading regulatory reports

To download a regulatory report:

1. Retrieve the project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. On the Branch Summary page, click **Downloadable reports** and select **Download Regulatory report (.zip)** from the drop down menu.

Alternatively:

1. Click **Information** in the left side navigation bar.
2. In the **Regulatory Report** section, choose a project branch from the drop down men&#x75;**.**
3. Click **Download report**.

SonarQube generates the report for download, which may take a few minutes depending on the size of the project.

### Contents of the regulatory report’s ZIP file

The reports are in a ZIP file containing a snapshot of the latest analysis of the selected branch and include TXT, CSV, and PDF files.

The PDF file includes:

* **Project overview**:
  * Project details
  * Quality gates information and status
* **Project rating** **overview** for:
  * New code broken down by new issues, accepted issues, coverage, duplication, and security hotspots.
  * Overall code broken down by security, reliability, maintainability, accepted issues, coverage, duplication, and security hotspots.
* **Distribution of issues in new code** showing open issues and breakdown by severity, based on security, reliability, maintainability.
* **Distribution of issues in overall code** showing open issues and breakdown by severity, based on security, reliability, maintainability.
* **Quality gate and quality profiles** information.
* **Files** lists all relevant files included in the ZIP file.
* **Definitions** lists all the definitions of terms related to the report.

The PDF regulatory report is generated with metrics from software qualities (security, reliability, maintainability). Some CSV files may contain metrics from both software qualities and rule types (vulnerabilities, bugs and code smells) and they are marked accordingly.

### Related pages

* [project-security-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/project-security-reports "mention")
* [project-pdf-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/project-pdf-reports "mention")
