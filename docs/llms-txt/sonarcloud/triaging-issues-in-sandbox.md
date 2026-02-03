# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/triaging-issues-in-sandbox.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/triaging-issues-in-sandbox.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/triaging-issues-in-sandbox.md

# Triaging issues in Sandbox

If the Sandbox feature is enabled for your project, issues coming from a SonarQube Server update and according to predefined conditions will be moved to the Sandbox. SonarQube ignores issues in sandbox in ratings/measure calculations and quality gate assessment but displays the number of sandboxed issues in the various analysis snapshots in the UI. The purpose is to prevent unexpected disruptions to your CI/CD pipelines after a SonarQube update by letting you triage the sandboxed issues at your convenience.

With the Administer Issue permission, you can perform the following actions on an issue stored in the Sandbox:

* You can open the issue if you want the issue to follow your standard fixing process.\
  The issue will impact the quality gate.
* You can accept the issue if you want to fix it later. The issue status is then marked as **Accepted**.\
  The issue will not impact the quality gate.
* You can mark the issue as **False positive** if you think the analysis is mistaken.

In addition, you can reassign an issue, tag an issue, and comment on an issue.

To triage your issues in Sandbox:

1. Retrieve your sandboxed issues. Do one of the following:

   * Retrieve your project and select **Issues** in the project navigation bar. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information.
   * Retrieve issues from an analysis report by selecting the reported number of issues in Sandbox.

   The **Issues** page opens with search filters in the left-side panel and issue results in the right section of the page. If not already done, select **In sandbox** in the search filters as illustrated below.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/kDytV6Db7DkNvdhnKQOs/sonarqube-server-triage-issues-in-sandbox_Qs0144.png" alt="Triaging issues in Sandbox"><figcaption></figcaption></figure>

2. In the issue results, in the card of the issue you want to triage, select the **In sandbox** status and select the action you want to perform on the issue.
3. To reassign an issue, tag an issue, or comment on an issue, see [managing](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/managing "mention").

### Related pages

* [#sandboxing-of-issues-coming-from-sonarqube-update](https://docs.sonarsource.com/sonarqube-server/user-guide/solution-overview#sandboxing-of-issues-coming-from-sonarqube-update "mention")
* [retrieving](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving "mention")
* [reviewing](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/reviewing "mention")
* [managing](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/managing "mention")
* [fixing](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/fixing "mention")
