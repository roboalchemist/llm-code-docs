# Source: https://docs.snyk.io/snyk-platform-administration/snyk-projects/issue-card-information.md

# Issue card information

Issue cards appear on the details page for a Project. You can use available options to do the following:

* [View dependency card information](#view-dependency-card-information).
* [Expand an issue card to show more details](#expanded-vulnerability-section).
* [Filter and sort issue cards](#filter-and-sort-issue-cards).
* [Perform additional card actions](#perform-additional-card-actions).

## View dependency card information

Dependency cards show details for a specific dependency, its associated vulnerabilities or license issues, and actions you can take.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0260b936fc04edc0b3bba8fffb215fc43f953a29%2FPR-checks-fix-dependencies-issue.png?alt=media" alt=""><figcaption><p>Issue card for the npmconf vulnerability</p></figcaption></figure>

The dependency card provides a [Header section](#header-section) and [Body section](#expanded-vulnerability-section) with information as explained in the next sections of this documentation.

### Header section

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-21245eddd40179b83982074d20d4fc9ee3c6543a%2FProjects-issue-card-header.png?alt=media" alt=""><figcaption><p>jsonwebtoken issue card header</p></figcaption></figure>

* [Severity level](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/severity-levels): for example, **High**. For dependencies with multiple severity levels, the severity shown in the header is the maximum of all listed issues under that dependency.
* Dependency name: for example, **jsonwebtoken** or **libxmljs2**.
* **Score**: [Risk Score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/risk-score) or [Priority score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/priority-score): 0 to 1,000. For dependencies with multiple scores, the score shown in the header is the maximum of all listed issues under that dependency. This will show as Priority score unless you are opted-in to the Early Access for Risk score.
* Tabs separating out the fixable issues, issues with no supported fix, and vulnerable dependencies.

### Expanded vulnerability section

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-3e86cafe7b539078ec65695289df5d2b9d1d40b0%2FProject-issues-expanded-vuln-section.png?alt=media" alt=""><figcaption><p>jsonwebtoken issue card body details</p></figcaption></figure>

* **Issue Name**: the vulnerability name, in this case "Authentication bypass".
* Type: **VULNERABILITY** or LICENSE ISSUE
* Links to [CWE](https://cwe.mitre.org/index.html) (Common Weakness Enumeration), [CVSS](https://www.first.org/cvss/calculator/3.1) (Common Vulnerability Scoring System), and [Snyk Vulnerability Database](https://snyk.io/vuln) information for the issue. You can use these links to view more information about the CWE, CVE, and CVSS scores or navigate to the Snyk Vulnerability Database information for a specific vulnerability from its issue card.
* [**Exploit maturity**](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/view-exploits): for example, **Mature** or **Proof Of Concept**, which indicates how well known the implementation of this exploit is.
* The exploit's **reachability**, for example, **Reachable**. This indicates whether a path from your first party code to the vulnerable code element exists, For information and an example, see [Reachable vulnerabilities](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/reachability-analysis).
* **Fixed in:** The file the vulnerability is fixed in
* **Social Trends**: Snyk occasionally shows a [Trending](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/vulnerabilities-with-social-trends) banner for issues that are being actively discussed on X (formerly known as Twitter).

## Filter and sort issue cards

You can apply multiple filters to a Project to show a set of issues based on specific criteria:

* Vulnerability or license issue
* Issues with a specific severity
* Issues within a range of the priority score
* Issues that have an exploit and how mature the exploit is
* Issues that are open or have been patched or ignored

You can sort the issue cards in a Project based on their priority score or severity.

## Perform additional card actions

You can perform the following actions on the issue card by clicking the tri-dot menu associated with each vulnerability:

* [Ignore the issue](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/ignore-issues): if you do not need to take action on an issue, or it does not need to appear on your reports, you can ignore it.
* [Create a Jira ticket](https://docs.snyk.io/integrations/jira-and-slack-integrations/jira-integration): if you have the Jira integration, you can link your issue boards to Snyk and create Jira tickets directly from the Project details page to fix vulnerabilities.

You can also open a PR if a fix is available by clicking the "**Upgrade to X.X.X"** button at the bottom of the card.

* [Fix the vulnerability](https://docs.snyk.io/scan-with-snyk/snyk-open-source/manage-vulnerabilities/fix-your-vulnerabilities): if a fix is available, you can fix individual vulnerabilities.
