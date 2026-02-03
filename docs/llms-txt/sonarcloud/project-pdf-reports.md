# Source: https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/project-pdf-reports.md

# Viewing project PDF reports

This feature is only available in the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

PDF reports give a view of a project’s state through a number of lenses, including releasability, security, reliability, and maintainability. They focus mainly on new code and quality gate conditions. You can subscribe to receive a monthly report by email. A project PDF report is available for the main or other long-lived branches.

{% hint style="info" %}
Before you can view the Enterprise-level reports, your organization must be added to an enterprise. For more information, see [managing-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise "mention").
{% endhint %}

### Viewing the PDF report of a project branch <a href="#viewing-report" id="viewing-report"></a>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Select the project branch you want to view:
   * For the main branch: In the left-side panel, select **Main Branch**.
   * For another branch: In the left-side panel, select **Branches** and choose a long-lived branch from the list.
3. In the top right corner of the **Summary** page, select **Project PDF > Download**. The PDF report is downloaded.

### Subscribing to the monthly PDF report <a href="#monthly-report" id="monthly-report"></a>

If you subscribe to the monthly PDF report of a project branch, you’ll receive a report by email during the first portfolio calculation of the month (if any), starting from the first day of the current month.

To subscribe or unsubscribe to the monthly PDF report for a project:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Select the project branch you want to view:
   * For the main branch: In the left-side panel, select **Main Branch**.
   * For another branch: In the left-side panel, select **Branches**, and choose a long-lived branch from the list.
3. In the top right corner of the **Summary** page, select **Project PDF > Subscribe** ***(or*** *Unsubscribe)*\*\* **to monthly report**.

### Related pages

* [project-security-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/project-security-reports "mention")
* [viewing-project-regulatory-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-project-regulatory-reports "mention")
