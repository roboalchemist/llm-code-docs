# Source: https://docs.snyk.io/snyk-platform-administration/snyk-projects/view-project-issues-fixes-and-dependencies.md

# View Project issues, fixes, and dependencies

The following Project information is available on the Snyk Web UI:

* [Issues](#view-issues): the number of vulnerabilities and Open Source license issues
* [Fixes](#view-fixes): fix advice
* [Dependencies](#view-dependencies): for Open Source, the total number of direct and transitive (nested) dependencies

## View issues

The Project details page displays Issue cards on the **Issues** tab. The information provided includes vulnerabilities and Open Source license issues.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b63d66462392da34ad06752f3b2c7ae8971a83b1%2FOS-fix-vulns-issues-in-project.png?alt=media" alt="Project details Issues tab and filters"><figcaption><p>Project details Issues tab and filters in environments with Fix advice available</p></figcaption></figure>

Use the filters in the panel to the left to narrow the search for issues. Select the checkboxes to filter issues by **Issue type**, **Severity**, **Fixability**, **Exploit Maturity**, and **Status**. You can also edit the **Priority Score** slider to change the range displayed; the default is 0 to 1000.

Issue details are shown on issue cards in the main area, sorted by priority score. See [Issue card information](https://docs.snyk.io/snyk-platform-administration/snyk-projects/issue-card-information) for more details.

{% hint style="info" %}
Snyk provides features to fix issues identified during scanning. See [Fix your vulnerabilities](https://docs.snyk.io/scan-with-snyk/snyk-open-source/manage-vulnerabilities/fix-your-vulnerabilities) for more details.
{% endhint %}

## View dependency details

Scroll to a dependency and the listed issues to view details, including the max and individual [risk scores](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/risk-score) (or [priority score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/priority-score)).

The Severity icon in front of the dependency title shows the maximum severity associated with the dependency. In this example, there are listed issues with medium or high severity, so the maximum severity for the dependency is high.

The score associated with the dependency title is the maximum of all listed issues under that dependency. This will show as either [Risk Score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/risk-score) if you are opted-in to the Early Access feature, or [Priority Score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/priority-score).

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0260b936fc04edc0b3bba8fffb215fc43f953a29%2FPR-checks-fix-dependencies-issue.png?alt=media" alt="View issue details"><figcaption><p>View dependency details</p></figcaption></figure></div>

* Click **Learn about this type of vulnerability** for [Snyk Learn](https://docs.snyk.io/discover-snyk/snyk-learn) training.
* Click **Show more detail** to view detailed information about the vulnerability from the [Snyk Vulnerability database](https://snyk.io/product/vulnerability-database/):

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f49afea06c8ac0a2b01027ea3018d6daa46b7648%2FProjects-vuln-db-info.png?alt=media" alt=""><figcaption><p>More information from the Snyk Vulnerability Database</p></figcaption></figure></div>

## View fixes

Snyk knowledge of the transitive dependencies in your Project makes it possible for Snyk to provide additional fix advice on the **Fixes** tab:

<div align="center"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-142fbc0d4a69423ed2f4bfe69aac12109bbb5089%2FScreenshot%202021-10-19%20at%2011.57.07.png?alt=media&#x26;token=6094978a-11e0-40fd-9ad0-c0956f382e91" alt="Issue details Fixes tab"><figcaption><p>Project details Fixes tab</p></figcaption></figure></div>

See [Fix your vulnerabilities](https://docs.snyk.io/scan-with-snyk/snyk-open-source/manage-vulnerabilities/fix-your-vulnerabilities) for details.

## View dependencies in Snyk Open Source

Snyk uses the package manager for your application to build the dependency tree and display it in the **Dependencies** tab of the Project issues detail page for Open Source. This tab shows which components introduce a vulnerability, indicating how the dependency was introduced to the application.

An example follows:

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e18abf288822b51d128e7f3743254bd5219bfc0f%2FScreenshot%202023-06-13%20at%2008.57.23.png?alt=media" alt="Issues detail page dependencies tab"><figcaption><p>Issues detail page dependencies tab</p></figcaption></figure></div>
