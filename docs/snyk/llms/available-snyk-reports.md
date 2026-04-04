# Source: https://docs.snyk.io/manage-risk/reporting/available-snyk-reports.md

# Available Snyk reports

The following reports are available:

* [Issues Detail report](#issues-detail-report)
* [Issues Summary report](#issues-summary-report)
* [Vulnerabilities Detail report](#vulnerabilities-detail-report)
* [Featured Zero-Day report](#featured-zero-day-report)
* [SLA Management report](#sla-management-report)
* [OWASP TOP 10 report](#owasp-top-10-report)
* [CWE TOP 25 report](#cwe-top-25-report)
* [CWE TOP 10 KEV report](#cwe-top-10-kev-report)
* [PCI-DSS v4.0.1 report](#pci-dss-v4.0.1-report)
* [Developer IDE and CLI usage report](#developer-ide-and-cli-usage)
* [Repositories Tested in CI/CD report](#repositories-tested-in-ci-cd-report)
* [Cloud Compliance Issues report](#cloud-compliance-issues-report)
* [Learn Engagement](#learn-engagement)
* [Learning Impact & Opportunities](#learning-impact-and-opportunities)
* [Snyk Generated Pull Requests](#snyk-generated-pull-requests)
* [Asset Dashboard](#asset-dashboard)
* [Risk exposure report](#risk-exposure-report)
* [Saved Views](#saved-views)
* [PR Check Report](#pr-check-report)

Select **Change Report** to change the report displayed:

<div align="left"><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-cf018b978165b3409bcd050f2e489d25a799ec87%2Fselect-report.png?alt=media" alt="Select Change Report to display different reports" width="563"><figcaption><p>Select Change Report to display different reports</p></figcaption></figure></div>

## Issues Detail report

The Issues Detail report displays all known issues in all of your Projects that are being monitored by Snyk. The report gives details about each issue and which of your Projects are affected and provides links to fix information.

The Issues Detail report displays the number of issues as well as the number of unique vulnerabilities that make up the issues.

Quick aggregations are available by categories including **Severity**, **Product Name**, and **Issue Type.**

Individual issues are displayed in a table according to the selected category. You can modify columns as needed.

For a table of only the unique vulnerabilities, use Change Report to switch to the Vulnerabilities Detail report.

## Issues Summary report

The Issues Summary report highlights the value that Snyk is providing by enabling both the identification and resolution of issues.

The report provides a glimpse into how well teams are optimizing the use of the Snyk platform for their workflow and provides a means to measure and improve security.

This report enables you to easily understand the current state and trends of the highest security risk items. This report also provides a quick view into where risk is coming from and where remediation efforts are most and least effective.

{% hint style="info" %}
Use the date filter in the upper right corner of the Issues Summary report to see key metrics and charts for a specified interval. The selected date range also impacts the compared period, which allows you to measure ‌progress across various key metrics.
{% endhint %}

At the top of the report, you can follow key metrics associated with security issues in the selected date range with a comparison to the previous sequential period's results. This allows you to get insights on trends. See the tooltips in Snyk Web UI for definitions of the metrics.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-ce1d3d27c9b494ac31b78a873cc0948923908f3f%2Fimage%20(293).png?alt=media" alt=""><figcaption></figcaption></figure>

The **Issues Identified and Resolved** trend captures the accumulated security issues that were identified and resolved during the selected date range. The gap between the two lines indicates the open issues backlog.

This visual trend allows you to identify if too many issues are being introduced, meaning that prevention should become a higher priority. Conversely, if not enough issues are being resolved, it means that you need to further analyze metrics such as MTTR and SLA.

{% hint style="info" %}
The Total Open issues metric at the top completes the picture for this trend, by showing the total open issues at the end of the selected period compared with the total open issues at the beginning of the selected date range.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-9259061e8cae34c0408553e2d4202f8f355c5ddc%2Fimage%20(294).png?alt=media" alt=""><figcaption></figcaption></figure>

Reviewing the **Exposure Window** trend allows you to identify the capacity of security issues that are open within predefined periods. This is a relevant metric to follow when filtering by attributes such as severity, exploit maturity, or asset class. and ensuring that the most critical issues for sensitive assets are being remediated on time.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-78c688d2ca8348b21064b91d3f74359a9b08d540%2Fimage%20(295).png?alt=media" alt=""><figcaption></figcaption></figure>

The **Time to Resolve by Week** trend provides visibility on the number of issues remediated within predefined periods, allowing you to measure remediation performance over time.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4d6da71b7b39ba29ac633cfc5ee729919f753fc0%2Fimage%20(297).png?alt=media" alt=""><figcaption></figcaption></figure>

The **Risk breakdown** table helps you make data-driven decisions about where you need to focus. The tables allow you to review ‌performance metrics from several angles.

Use the dimension picker to browse:

* **Projects** - Available at the Organization level. Allows you to pinpoint Projects that require your attention.
* **Organizations** - Available at the Group level. Surface Snyk Organizations based on their performance.
* **Asset Classes** - Ensure that efforts are prioritized to secure the most sensitive assets first.
* **Introduction Categories** - Allows to determine if preventable issues are handled properly by looking at the percentage change of new preventable issues, as well as assessing the impact of new monitored assets over your AppSec Program. You can view this under the **Baseline Issue** category.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b2da3d0b7334818d0065dfa7ccc5f5ff129f4bc1%2Fimage%20(296).png?alt=media" alt=""><figcaption></figcaption></figure>

## Vulnerabilities Detail report

The Vulnerabilities Detail report is similar to the Issues Detail report but shows issues grouped by Snyk Problem ID ([see Snyk Vulnerability DB](https://security.snyk.io/vuln)).

You can easily see how many instances of a vulnerability exist and how many Projects are affected. Use this report to understand which vulnerabilities are most prevalent for both resolution and prevention use cases.

For a table of Total Issues, use Change Reports to switch to the Issues Detail report.

{% hint style="info" %}
**Dependencies and license information**

To view Dependencies and license information, select the **Dependencies** menu option. See [Dependencies and licenses](https://docs.snyk.io/manage-risk/reporting/dependencies-and-licenses) for details.
{% endhint %}

## Featured Zero-Day report

This report addresses primary scenarios for managing and resolving emerging zero-day vulnerabilities, which carry significant consequences and attract substantial attention in the global AppSec community.

Use this report to discover your exposure to issues highlighted in a zero-day publication across various Targets and Projects. The report helps you prioritize zero-day issues and monitor the progress of remediation efforts against any remaining occurrences.

The [Security team at Snyk](https://snyk.io/platform/security-intelligence/) continuously updates the [Vulnerability Database](https://security.snyk.io/) with new vulnerabilities several times a day. When the team discovers a major new zero-day vulnerability—typically in a widely used package with high severity that affects many customers—it will be announced and addressed as a zero-day event.

Upon the announcement of a new zero-day event, begin by examining the **Impacted Targets** table to gain a deeper understanding of the exposure. Use filters such as Project Lifecycle, Environment, or Project Criticality to focus solely on Targets associated with Projects in production that are externally exposed or of high criticality. Gaining such insights depends on the [availability of Project attributes](https://docs.snyk.io/snyk-platform-administration/snyk-projects/project-attributes#available-attributes-and-their-values).

Next, proceed to the **All** **Issues** table and compile a prioritized list of issues requiring remediation. Typically, prioritization is determined by either the Snyk [Risk Score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/risk-score) or NVD CVSS Score, with emphasis placed on addressing vulnerabilities within sensitive targets. Apply filters based on Project Lifecycle, Environment, or Project Criticality to identify and address these targets promptly.

For continuous monitoring of remediation progress and efficacy, refer to the trend diagrams.\
The **Accumulative Issues Backlog Trend** diagram shows the weekly changes in the zero-day backlog by accumulating the weekly delta between identified and resolved issues. Use this diagram to ensure that your R\&D teams are reducing the zero-day backlog consistently, which will be indicated by a negative trend line.

In parallel, review the **Issues Identified versus Resolved over Time** diagram to conclude whether additional emphasis should be placed on preventing the introduction of new issues or on accelerating the remediation efforts.

## SLA Management report

The report presents a set of default SLA targets per severity based on common security standards, such as FedRAMP. These SLA targets can be modified to meet your own security requirements.

The SLA status of an issue can be:

* **Within SLA** - the age of the issue has not exceeded the SLA target, and it is expected to have sufficient lead time before breaching.
* **At Risk** - the issue is considered to be approaching an SLA breach and is flagged as “At Risk”.
* **Breached** - the age of the issue has exceeded the SLA target.

You can control the SLA targets and the transition of issues to the “At Risk” status by editing the **SLA target** and setting the **At risk duration before breach (days)** field.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e5f2d0cf6a7984061dcb4aaa2d39e095beee7cb6%2Fimage.png?alt=media" alt=""><figcaption><p>SLA Management Report - Edit SLA targets</p></figcaption></figure>

The SLA report includes additional filters under the SLA category, allowing for better identification of the age of issues in relation to the SLA target:

* **SLA status** - allows the filtering of the report according to a specific SLA status.
* **Issue age** - allows to discover issues within a range of age.
* **Time until breach** - identifies issues that will breach the SLA target within days.

{% hint style="info" %}
The report is, by default, showing only issues that are with high or critical severity. Update the severity filter if you want to view the SLA status for additional severities.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5c4ed62c75040a11a08cb87d573d16f0e9342700%2Fimage.png?alt=media" alt="" width="300"><figcaption><p>SLA Filters within the filters picker</p></figcaption></figure>

You can share the report with predefined SLA targets by sharing the report URL or return to a predefined SLA report by bookmarking the web page in your browser.

In the **Open issues** section, the **SLA severity breakdown** shows a distribution of severity levels by the SLA compliance status of the viewed Group or Organization.

The **SLA trend** shows the cumulative SLA status of issues over time.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-50194681e813cdfb37f38b15bca4762cb3f40301%2Fimage.png?alt=media" alt=""><figcaption><p>SLA Management Report - Open issues section</p></figcaption></figure>

The **SLA breakdown table** allows you to compare the SLA compliance results of Organizations in the Group view, or Targets in the Organization view. The table is sorted by default according to the quantity of breached issues.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d69632bb765a92f04104caf547e3aed33cd3d15e%2Fimage.png?alt=media" alt=""><figcaption><p>SLA Management Report - SLA Breakdown</p></figcaption></figure>

The **Breached and at-risk open issues** table helps you prioritize issues based on their aging and SLA compliance status. You can use the **Modify Column** picker to add additional columns and learn more about the specific issues.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a6f7d962d99a63d388f8014ca0b960d026563d68%2Fimage%20(227).png?alt=media" alt=""><figcaption><p>SLA Management Report - Breached and at risk open issues</p></figcaption></figure>

{% hint style="info" %}
You can download the **SLA Breakdown** and the **Breached and at risk open issues data** in a CSV format using the **Download CSV** option.
{% endhint %}

You can review the SLA results for resolved issues and perform a retrospective analysis by reviewing the **Resolved issues** section.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b07724e4ee9691eb4791ba0b44565c9b3170d785%2Fimage.png?alt=media" alt=""><figcaption><p>Resolved issues section</p></figcaption></figure>

## OWASP Top 10 report

The [OWASP Top 10](https://owasp.org/www-project-top-ten/) is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks for web applications and is globally recognized by developers as the first step towards more secure coding.

Each control in the list (A1, A2, and so on) is based on a list of Common Weakness Enumerations (CWEs). For example, [A01:2021 – Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) is based on a list of 34 CWEs.

The CWEs are mapped to Snyk-IDs (), which are mapped to issues.

For example, the critical vulnerability [SNYK-JAVA-ORGAPACHELOGGINGLOG4J-2314720](https://security.snyk.io/vuln/SNYK-JAVA-ORGAPACHELOGGINGLOG4J-2314720) is classified as [CWE-94](https://cwe.mitre.org/data/definitions/94.html), which is part of the OWASP TOP 10 [A03:2021 - Injection](https://owasp.org/Top10/A03_2021-Injection/). All the issues related to this vulnerability will be under the A03 category.

Learn more by using the [OWASP TOP 10 Learning path](https://learn.snyk.io/learning-paths/owasp-top-10/) on Snyk Learn.

The report is based on the latest mapping released in 2021. The supported products are Snyk Open Source, Snyk Container, and Snyk Code.

## CWE Top 25 report

The [CWE Top 25](https://cwe.mitre.org/top25/) Most Dangerous Software Weaknesses is a list that demonstrates the current most common and impactful software weaknesses based on Common Vulnerabilities and Exposures (CVEs) severity and their exploitation potential.

The report is based on the latest version released in 2023 by Mitre. The supported products are Snyk Open Source, Snyk Container, and Snyk Code.

## CWE Top 10 KEV report

The [CWE Top 10 KEV Weaknesses](https://cwe.mitre.org/top25/archive/2023/2023_kev_list.html) list identifies the top ten CWEs in the Cybersecurity and Infrastructure Security Agency’s (CISA) [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (KEV) Catalog, a database of security flaws in software applications and weaknesses that have been exposed and leveraged by attackers.

The report is based on the version released in 2023 by Mitre. The supported products are Snyk Open Source, Snyk Container, and Snyk Code.

## PCI-DSS v4.0.1 report

{% hint style="info" %}
**Release status**

The PCI-DSS v4.0.1 report is in Early Access and available only with Enterprise plans.
{% endhint %}

PCI Security Standards are technical and operational requirements created by the PCI Security Standards Council (PCI SSC) to safeguard cardholder data. These standards apply to all entities that store, process, or transmit this information and include requirements for software developers and manufacturers.\
\
The Council manages these standards, while compliance is enforced by founding members: American Express, Discover Financial Services, JCB, MasterCard, and Visa Inc.

Snyk PCI-DSS v4.0.1 Report is designed to help you:

* Estimate readiness for meeting the PCI-DSS AppSec requirements for SCA and SAST based on the Snyk scan results.
* Provide evidence that the Organization is meeting the PCI-DSS AppSec requirements for SCA and SAST vulnerabilities.
* Prioritize issues to improve PCI-DSS compliance readiness.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0214225dad814eaea39ee23796ab2d8d61f6328e%2Fimage%20(283).png?alt=media" alt=""><figcaption><p>Snyk PCI-DSS v4.0.1 Report</p></figcaption></figure>

The report identifies PCI-DSS risks and violations based on the following PCI-DSS v4.0.1 requirements:

1. **Requirement 6.2.4:** Engineers use various techniques to prevent or mitigate common software attacks and related vulnerabilities in bespoke and custom software. This includes but is not limited to the following methods:
   * Injection attacks, including SQL, LDAP, XPath, or other command, parameter, object, fault, or injection-type flaws.
   * Attacks on data and data structures, including attempts to manipulate buffers, pointers, input data, or shared data.
   * Attacks on cryptography usage, including attempts to exploit weak, insecure, or inappropriate cryptographic implementations, algorithms, cipher suites, or modes of operation.
   * Attacks on business logic, including attempts to abuse or bypass application features and functionalities through the manipulation of APIs, communication protocols and channels, client-side functionality, or other system or application functions and resources. This includes cross-site scripting (XSS) and cross-site request forgery (CSRF).
   * Attacks on access control mechanisms, including attempts to bypass or abuse identification, authentication, or authorization mechanisms or attempts to exploit weaknesses in the implementation of such mechanisms.
   * Attacks using any “high-risk” vulnerabilities identified in the vulnerability identification process, as defined in Requirement 6.3.1.
2. **Requirement 6.3.3:** All system components are protected from known vulnerabilities by installing applicable security patches and updates as follows:
   * Patches and updates for critical vulnerabilities, identified according to the risk ranking process at Requirement 6.3.1 are installed within one month of release.

### Snyk Violation Analysis based on PCI-DSS attack categories

As the standard does not explicitly define specific CWEs or CVEs, Snyk provides an analysis based on leading CWEs associated with the named attack categories. Below are the CWEs categorized by attack type:

#### Injection Attack Violations Summary

The following list provides an association between the identified attack categories and the CWEs associated with each category:

* SQL Injection: CWE-89
* LDAP Injection: CWE-90
* XML Injection (XPath Injection): CWE-91
* Command Injection: CWE-77
* Use of Unsafe Reflection: CWE-470

#### Attacks on Data and Data Structures Violations Summary

The following list provides an association between the identified attack categories and the CWEs associated with each category:

* Buffer Overflow: CWE-120
* NULL Pointer Dereference: CWE-476
* Double Free: CWE-415
* Concurrent Execution using Shared Resource with Improper Synchronization (‘Race Condition’): CWE-362

#### Attacks on Cryptography Usage Violations Summary

The following list provides an association between the identified attack categories and the CWEs associated with each category:

* Use of a Broken or Risky Cryptographic Algorithm: CWE-327
* Use of Insufficiently Random Values: CWE-330
* Improper Verification of Cryptographic Signature: CWE-347
* Cleartext Transmission of Sensitive Information: CWE-319
* Use of Hard-coded Cryptographic Key: CWE-321

#### Attacks on Business Logic Violations Summary

The following list provides an association between the identified attack categories and the CWEs associated with each category:

* Server-Side Request Forgery (SSRF): CWE-918
* Cross-Site Request Forgery (CSRF): CWE-352
* Cross-Site Scripting (XSS): CWE-79
* Origin Validation Error: CWE-346
* Improper Authorization: CWE-285
* Exposure of Sensitive Information to an Unauthorized Actor: CWE-200

#### Attacks on Access Control Mechanisms Violations Summary

The following list provides an association between the identified attack categories and the CWEs associated with each category:

* Improper Authentication: CWE-287
* Improper Access Control: CWE-284
* Incorrect Authorization: CWE-863
* Authorization Bypass Through User-Controlled Key: CWE-639
* Missing Authentication for Critical Function: CWE-306
* Incorrect Implementation of Authentication Algorithm: CWE-303

#### Attacks on Access Control Mechanisms Violations Summary

The Missing Authorization attack category is associated with CWE-862.

### PCI-DSS v4.0.1 Guidance

The report is filtered by default on open issues of critical severity. Those filters are also applicable when exporting the report to PDF.

#### PCI-DSS Readiness Trend

The PCI-DSS Readiness Trend is designed to help you track your progress toward eliminating PCI-DSS violations. A violation is defined as a critical vulnerability elected by the PCI-DSS attack categories (as explained in Requirement 6.2.4) that is more than 30 days old, as stated in Requirement 6.3.3.

The number on the left indicates the violation status and the progress made in the last seven days.

The trend shows all vulnerabilities per Requirement 6.2.4, categorized by age bucket. This allows for quick identification of potential violations and vulnerabilities that may soon become violations.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c94168d6124f3c48f39d9900a6ac5f4c0360ddb5%2Fimage.png?alt=media" alt=""><figcaption><p>PCI-DSS Readiness Trend</p></figcaption></figure>

#### Attack category breakdown

The breakdown table helps identify the number of vulnerabilities by attack category (as per requirement 6.2.4) or by Snyk Organization based on the relevant age bucket.

Use the table to pinpoint major attack categories or Snyk Organizations that lead to PCI-DSS violations. You can click on the figures to explore the specific issues in more detail.

{% hint style="info" %}
After you investigate and see the actual issues behind the figures, you may proceed by:

* Vulnerability triage and prioritization.
* Conclude the prevalent CWEs and CVEs by sorting on the CWE/CVE column and filtering those CWEs/CVEs in the [Vulnerabilities Detail Report](#vulnerabilities-detail-report) to surface all the vulnerability occurrences across targets and Projects.
* Run a vulnerability eradication campaign or assign Snyk Learn training to relevant engineering teams.
  {% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-51200c77e4a5f994c7421c2dd489a8110c203159%2Fimage%20(282).png?alt=media" alt=""><figcaption><p>Attack Category Breakdown</p></figcaption></figure>

## Developer IDE and CLI usage

To use this report, you must ensure you have installed the following prerequisites:

* Snyk CLI
  * version 1.1292.1 or newer (for CLI and IDE plugins usage)
  * version 1.1297.0 or newer for general Agentic scans (Snyk Studio using MCP)
  * version 1.1298.1 or newer for granular Agentic scans (such as MCP host)
* VS Code 1.86.0 or newer and Snyk Security plugin 2.3.3 or newer
* IntelliJ IDEs 2023.3 or newer and Snyk Security plugin 2.7.3 or newer
* Visual Studio 2019, 2022 and Snyk Security Plugin 1.1.47 or newer
* Eclipse 2023.12 or newer and Snyk Security plugin 2.1.0 or newer

This report shows the adoption of Snyk testing in local development through the IDE plugins, using the CLI locally or incorporating Snyk Studio into agentic workflows. The report is available under the Change Report dropdown at the Group and Organization levels.

{% hint style="info" %}
This report focuses on the local developer experience and does not include the use of CI/CD. In addition, it does not show Organizations or developers that have never used the CLI, IDE, or Snyk Studio (via MCP).
{% endhint %}

Security teams can use this report to demonstrate strong shift-left behavior as a model behavior to bring to other teams. This report also shows where teams or individual developers are not adopting Snyk locally. Companies can use this report to encourage more shift-left behavior.

This report shows the test usage in the IDE, CLI, and Snyk Studio by developers. Teams can filter by date and Organization. The report includes visibility into metrics such as:

#### Total number of developers running scans and the number of scans in IDE, CLI, and Agentic integrations (Snyk Studio)

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-082abdd4c2a0d31ebeec06e6660bb66d0ebc7b83%2FScreenshot%202025-07-22%20at%2010.16.07.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Charts and summary tables breaking down this data by the environment of the scan

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d9a2445ff939116f61fbe7d8f673aae85af1c265%2FScreenshot%202025-07-22%20at%2010.18.03.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Charts and summary tables breaking down this data by different dimensions, such as IDE plugins or Agentic integrations

<div><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5c5f7b2668659544ef844962e59660669b54d6fd%2FScreenshot%202025-07-22%20at%2010.19.11.png?alt=media" alt=""><figcaption></figcaption></figure> <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-54ea1c6a85e17d419e412f4d16571001648c3a9a%2FScreenshot%202025-07-22%20at%2010.19.17.png?alt=media" alt=""><figcaption></figcaption></figure></div>

#### Charts and summary tables breaking down this data by the Snyk scan type

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b272d8dfcd4a496045ced68524d57359424c3975%2FScreenshot%202025-07-22%20at%2010.20.04.png?alt=media" alt=""><figcaption></figcaption></figure>

#### List of organizations and developers adopting Snyk locally

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8f76c5a7220e3a5c2b05a0b9c4bf79b2273279c0%2Fide%20usage%20by%20developer.png?alt=media" alt=""><figcaption></figcaption></figure>

## Repositories tested in CI/CD report

To use this report, consider the following prerequisites:

* Snyk CLI version 1.1292.1 or newer.
* Viewing the last commit data requires SCM Group integration. For more details, navigate to [SCM integrations](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations).
* When testing containers, include the `.git` context as part of the `snyk container test` command.

This report analyzes Snyk tests performed as part of CI/CD pipelines executed using Snyk CLI. It will inform you about the usage of your company and adoption of testing in CI/CD, ensuring repositories are tested as expected and preventing critical vulnerabilities and misconfigurations from being deployed and reaching the production environment.

{% hint style="info" %}

* The report results are scoped by a date range filter that you can use to review specific periods. The filter is defaulted to the last 30 days.
* This report provides visibility into Snyk tests (`snyk test`, `snyk code test`, `snyk container test`, `snyk iac test`) executed within your CI pipeline (using CLI). Its primary goal is to help you evaluate test results and determine whether to pass or fail the build process based on these security checks.
* Please note that `snyk monitor` commands are **not** included in this report. While `snyk monitor` is crucial for ongoing security posture and identifying new vulnerabilities, this report specifically tracks tests that actively gate your CI/CD pipeline.
  {% endhint %}

The numbers displayed on the main view of the report represent the number of repositories tested in the selected date range per Snyk product.

In addition, you can learn about the change in the number of tested repositories compared to the previous sequential period, so you can conclude whether the adoption of CI/CD tests across repositories improved.

A green upward arrow indicates that more repositories were tested compared to the previous sequential period, while a red downward arrow indicates the opposite. The absolute change value appears next to the arrow, and the perception of change appears right underneath to measure the degree of change.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-770ee957ca935fdf6e12704481378231d0582766%2Fimage.png?alt=media" alt=""><figcaption><p>Repositories tested during date range</p></figcaption></figure>

{% hint style="info" %}
A sequential period refers to a date range covering the last seven days. In this case, the period starts seven days ago and ends today. The previous sequential period spans from 14 days ago to seven days ago. As a result, both sequential periods are of the same duration.
{% endhint %}

#### Repository Test Adoption <a href="#repository-test-adoption" id="repository-test-adoption"></a>

Review the Repository Test Adoption trend to learn more about ‌adoption over time.\
Represented by the green line, you can see the weekly number of repositories that have been tested compared to the repositories that had commits in the last 30 days, represented by the purple line.

This comparison helps determine whether Snyk tests in CI/CD are being increasingly adopted over time and highlights the number of repositories that have received commits but have not been tested in CI/CD.

{% hint style="info" %}
Viewing the last commit data requires SCM Group integration. For more details, navigate to the [SCM integrations](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations) page.
{% endhint %}

You can filter by specific products or by specific organizations or extend the viewed period using the date range filter.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-303c5b25eaf3b313184244994b52d6cc58c07689%2Fimage.png?alt=media" alt=""><figcaption><p>Repository Test Adoption</p></figcaption></figure>

#### Test Success Rate Trend <a href="#test-success-rate-trend" id="test-success-rate-trend"></a>

The test success rate serves as an indicator of how well the engineering department or specific Snyk Organizations can adopt a "shift left" approach, which aims to identify and resolve issues before the code reaches the build process. This success rate is calculated by dividing the number of tests that passed by the total number of relevant tests conducted.

{% hint style="info" %}
An applicable test is a test that did not fail due to technical issues or a non-supported Project.
{% endhint %}

Having a low success rate can indicate that:

* Snyk tests are failing due to security issues that can be prevented in local development or in the PR Check stages. Snyk recommends testing with the [Snyk IDE](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions) plugin, using [Snyk PR Checks](https://docs.snyk.io/scan-with-snyk/pull-requests/pull-request-checks) and enroll in a [Snyk Learn](https://docs.snyk.io/discover-snyk/snyk-learn) program.
* The test success criteria are too strict. To explore this option further, Snyk recommends reviewing the test definitions of the organizations with the lowest success rate, as shown by the Adoption by Organizations widget. For more details about defining test success criteria, navigate to the [Failing of builds in Snyk CLI](https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/failing-of-builds-in-snyk-cli) page.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b55f2c9e81e912d83063c88f21709b39e64fedac%2Fimage%20(277).png?alt=media" alt=""><figcaption><p>Test Success Rate Trend</p></figcaption></figure>

#### Adoption by Organizations <a href="#adoption-by-organizations" id="adoption-by-organizations"></a>

Launching an Application Security program to boost testing adoption in CI/CD pipelines can be challenging. This initiative requires collaboration between the AppSec and R\&D teams and will be implemented gradually, with regular progress monitoring.

The Adoption by Organization table facilitates tracking and comparing the adoption rates of Snyk Organizations, helping you identify the organizations that are struggling or lagging behind.

In addition, you can examine the success rate column to surface organizations that have lower success rates.

**Columns descriptions:**

* **Tested Repositories:** the number of repositories that were tested in the selected time range, with an indication of the percentage of change compared to the previous sequential period.
* **Committed Repositories:** the number of repositories that had any commits in the last 30 days at any given time within the selected time range, with an indication of the percentage of change compared to the previous sequential period.
* **Success Rate:** the portion of successful tests in CI/CD against all other tests that were executed.

#### Repository Test Summary <a href="#repository-test-summary" id="repository-test-summary"></a>

The repository test summary table shows the performed tests during the selected date range.

The default sorting in the table surfaces repositories according to their last commit, allowing you to identify repositories that were expected to be tested in CI/CD pipelines and verify they were tested. Clicking the column names to sort the table according to the selected column. You can sort the table by multiple columns at a time.

{% hint style="info" %}
Viewing the last commit data requires SCM Group integration. For more details, navigate to the [Group-level integrations](https://docs.snyk.io/developer-tools/scm-integrations/group-level-integrations) page.
{% endhint %}

You can execute the test on a specific repository branch in the table. The `tested` indicator means that any branch of this repository was tested during the selected date range.

{% hint style="info" %}
Hovering over the TESTED tag reveals the last test performed during the selected date range
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-9a114526a199cf043bdba141ea3b2be3676257cb%2Fimage%20(279).png?alt=media" alt=""><figcaption><p>Repository Test Summary</p></figcaption></figure>

## Cloud Compliance Issues report

{% hint style="info" %}
This report is available only if you have enabled legacy Snyk Cloud.
{% endhint %}

The Cloud Compliance Issues report shows cloud issues for an entire Organization, organized by [compliance standard](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/key-concepts-for-cloud-scans#docs-internal-guid-e2e38027-7fff-9271-f2c0-e23677542f6e).

You can view a report for a single version of a compliance standard at a time, for example, CIS AWS Foundations Benchmark v1.4.0, by selecting the desired standard from the dropdown menu. Each report includes a list of compliance controls organized by control category, with corresponding issue counts.

Selecting an issue count lets you view the list of issues associated with that control in the [Cloud Issues UI](https://docs.snyk.io/scan-with-snyk/snyk-iac/getting-started-with-cloud-scans/manage-cloud-issues/view-cloud-issues-in-the-snyk-web-ui), where you can view each issue in detail.

Use the information in the Cloud Compliance Issues report to investigate, triage, and fix cloud compliance issues.

## Learn Engagement

{% hint style="info" %}
Learn Engagement report is available only in the Learning Management add-on offering. For more information, contact your Snyk account team.
{% endhint %}

The goal of the engagement report is to provide insights into your security education and training programs overall progress, and give you insights into which parts of your Organization are engaging with Snyk Learn content. You can use the data and insights to better optimise your program, find security champions, generate reports for compliance and show progress to your executive sponsors.

### Access the report

The Learn Engagement report can be accessed at the Group level from the **Change Report** dropdown in the Reports menu.

### Report features

The report allows you to track:

* Learn engagement snapshot analytics
* Assignment Progress
* Adoption rankings
* Content usage breakdown
* Filtering: custom time periods, users, organizations, organization role, and Lesson titles.

### Learn engagement snapshot and assignment progress

The first section of the report focuses on showing key engagement statistics and the progress of any assignments. Tool tips provide more details on the definitions of the metrics.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-905142bac6c6313327f6faae7809e15011e874d3%2FScreenshot%202025-09-29%20at%2019.30.57.png?alt=media" alt=""><figcaption></figcaption></figure>

### Adoption rankings

The adoption ranking section shows your organization and individual user engagement with Snyk Learn. This is ranked by "Lessons complete" and also has the estimated duration the org/user has spent on Snyk Learn lessons. Estimated duration calculated using the estimated duration presented at the start of each lesson, and includes estimated time from any progress on "in-progress" lessons in the selected period.

{% hint style="info" %}
The user level adoption ranking is a great way to identify potential security champions who are proactively engaging in security education and training.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2d68d54286a26caaee49cfee54d405e8a75f44d0%2FScreenshot%202025-09-29%20at%2019.34.12.png?alt=media" alt=""><figcaption></figcaption></figure>

### Learning breakdown

The breakdown shows the different types of Learn content the users are engaging with, using lesson completions as the measure. You can see if users are engaging with product training or security education, along with the most popular lessons and insights into which CWE categories users are studying the most.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a42a5f0041d1dc010323d3f0338d6768c55d1702%2FScreenshot%202025-09-29%20at%2019.34.22.png?alt=media" alt=""><figcaption></figcaption></figure>

## Learning Impact & Opportunities

{% hint style="info" %}
Learning Impact & Opportunities report is in Early Access and available only in the Learning Management add-on offering. For more information, contact your Snyk account team.
{% endhint %}

The goal of the impact and opportunities report is to provide insights into the impact your security education and training programs are having on code issue remediation and code issue prevention. In addition, the report gives recommendations for future training based on your code issue backlog, and issues that were introduced during the selected time period of the report.

### Access the report

The Learning Impact & Opportunities report can be accessed at the Group level from the **Change Report** dropdown in the Reports menu.

### Report features

The report allows you to track:

* Impact of education and training on code issue remediation
* Impact of education and training on code issue prevention
* Recommendations for further training opportunities
* Coverage rates of users trained in identified training opportunities.
* Filtering: custom time periods, users, organizations, lesson title, CWE, issue severity.

### Learning impact snapshot

The first section of the report focuses on the impact education is having on your security program, focusing on code issue resolution and code issue prevention.

The "Learning Impact on Issue Resolution" chart measures the relationship between lesson completion and the resolution of detected code security issues. Resolved issues are counted when a related lesson was completed before the issue was fixed within the selected period. Lesson completions are counted when a related issue was fixed after the lesson was completed within the selected period. Use the filters to drill into specific lessons or CWE categories.

The "Learning Impact on Issue Prevention" chart measures the relationship between lesson completion and the prevention code security issues. Introduced issues are counted when a related lesson was completed within the selected period. Issues introduced on the day a Project was imported are not counted. Use the filters to drill into specific lessons or CWE categories.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-4698f8c243ade0dd8ba67127c411534411d89a9d%2FScreenshot%202025-10-23%20at%2015.00.57.png?alt=media" alt=""><figcaption></figcaption></figure>

### Top 10 CWEs - open issues / issues introduced in the period

This section of the report shows recommendation for training for your top open code issues, and most frequently introduced issues, by volume. Note issues are only included when Snyk Learn has a related lesson for the CWE category.

You will see coverage for all users within organisation scope of the report filters. This shows you how many people have ever completed a related Snyk Learn lesson on the topic.

<div><figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f95559cd58c09ff7cce0d1f3930401f9bbc6097c%2FScreenshot%202025-10-23%20at%2014.12.24.png?alt=media" alt=""><figcaption></figcaption></figure> <figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e6c2137c7877614b60560cb75cfa4e98556c42c7%2FScreenshot%202025-10-23%20at%2014.12.18.png?alt=media" alt=""><figcaption></figcaption></figure></div>

{% hint style="info" %}
The recommendations in this section allow you to focus on the most impactful training opportunities. Use the filters to further customise the recommendations based on issue severity or for specific Organizations.
{% endhint %}

## Snyk Generated Pull Requests

{% hint style="info" %}
**Feature availability**

Snyk Generated Pull Requests report is available only for Enterprise plan customers, for all SCM integrations. For more information, see [Plans and pricing](https://snyk.io/plans/).
{% endhint %}

### Access the report

The Generated Pull Requests report can be accessed at both Group and Organization level from the **Change Report** drop down in the Reports menu.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0ae3253f5c86fb06e85cee0ee75e3a2fa335c656%2F2025-03-05_11-19-35.png?alt=media" alt="Snyk generated pull requests report"><figcaption><p>Snyk generated pull requests report</p></figcaption></figure>

This report type provides an overview of how [Fix](https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests/create-automatic-prs-for-new-fixes-fix-prs), [Backlog](https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests/create-automatic-prs-for-backlog-issues-and-known-vulnerabilities-backlog-prs), and [Upgrade PRs](https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests/upgrade-dependencies-with-automatic-prs-upgrade-prs) are used and highlights the efficiency of PR merges.

The analytics report covers the following:

* Overview of PRs status by type and the PR merge ratio.
* Visibility of issues.
* Breakdown by repository for PR status.

The report summary enables you to check the total number of Snyk PRs created, the total pull requests merged, and the mean time to merge for those pull requests.

{% hint style="warning" %}
This report type does not include PR checks.
{% endhint %}

### Report features

Use the date filter in the upper right corner of the report to display data based on a specific interval.

Add various filters to narrow down results to specific configurations. The filter options are Organization, SCM, Project, and Repository.

#### Snyk Generated Pull Requests usage

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8afc6533efeaa842a092d656ea432eace85338bc%2F2025-03-05_11-20-10.png?alt=media" alt="Pull Request usage graph and table"><figcaption><p>Pull Request usage graph and table</p></figcaption></figure>

Pull Request usage is visualized in a **Pull requests by type** graph and a **Pull requests by status** table, displaying the same data in different formats. These distinguish the number of PRs into Fix, Backlog, and Dependency upgrade categories, segmented by Open, Merged, and Closed status types. Merge rate is presented as a percentage for each row.

#### Open vs Fixed issues

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a4bfbd7c36427d84f4370f0eb9a30d307c33579e%2Fopen-vs-fixed-issues-pr-report.png?alt=media" alt="Open vs Fixed issues graph and table"><figcaption><p>Open vs Fixed issues graph and table</p></figcaption></figure>

The Open vs Fixed issues in Snyk PRs graph and table displays the number of open and fixed issues based on severity.

#### Snyk Generated Pull Requests by repository

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6d8209a6db96c3f8533a7669eedfecf6dc6569ca%2F2025-03-05_10-02-13.png?alt=media" alt="Projects/Orgs/Repository table for PRs of different status"><figcaption><p>Projects/Orgs/Repository table for PRs of different status</p></figcaption></figure>

The **Projects/Org/Repository** table displays the number of Total, Open, Merged, and Closed PRs for each Organization and repository relationship. Merge rate is presented as a percentage for each row.

Select a repository name to open a modal containing additional metrics for that specific repository.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e304eb2aa5619661d810a26468209d8c29892faf%2Frepo-breakdown-report-blur.png?alt=media" alt="Repository breakdown by PR type and PR status"><figcaption><p>Repository breakdown by PR type and PR status</p></figcaption></figure>

The repository breakdown details the number of PRs segmented by PR type and PR status. Merge rate is presented as a percentage for each row. It also lists the Projects within that repository, with the number of issues categorised by severity.

## Asset Dashboard

The Asset Dashboard provides a comprehensive overview of your application and security controls. It displays essential data such as the status and trends of open issues, control coverage, and repository metadata.

The Asset Dashboard is a central hub for managing and reviewing assets, making tracking inventory size easier over time and understanding the interaction between different asset types.

While Snyk Inventory enables the discovery and management of your assets that should be secured, the Snyk Asset Dashboard allows you to go beyond the details and better understand the main building blocks of your inventory.\
\
The Asset Dashboard brings all the asset data that is available in your inventory and helps to answer various questions, such as:

* Does my AppSec program meet the coverage requirements for business-critical assets and strategic applications?
* Are the assets being classified properly according to their criticality?
* Do you know which repositories belong to which application or code owners? Are newly introduced repositories being updated with that data?
* What are the main programming languages and package managers that are used in repositories that have been worked on recently?

### Filters

The filters are located at the top left of the page, with the following filtering options: **Asset Class**, **Asset type,** **Add filter**. The filter selection applies to all available data widgets.

Here are the available filters:

| Filter               | Description                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asset Class          | The business criticality of an asset (A - most critical to D - least critical).                                                                                                                                                                                                                                                                                       |
| Asset type           | The type of an asset (Container image, Package, Repository). Most data widgets already present certain asset types by default.                                                                                                                                                                                                                                        |
| \*Application        | The list of the applications for which you have configured the application context catalog in Snyk Essentials.                                                                                                                                                                                                                                                        |
| \*Catalog name       | The name of your application context catalog.                                                                                                                                                                                                                                                                                                                         |
| \*Category           | The category of a repository asset. For example, `service` or `library`.                                                                                                                                                                                                                                                                                              |
| Discovered           | The period when the asset was discovered.                                                                                                                                                                                                                                                                                                                             |
| Last Seen            | The period when the asset was last imported from the integration.                                                                                                                                                                                                                                                                                                     |
| \*Lifecycle          | The lifecycle state of the application context catalog component. For example `production`, `experimental`, `deprecated`.                                                                                                                                                                                                                                             |
| \*Owner              | The team that owns the repository for which the application context catalog was configured.                                                                                                                                                                                                                                                                           |
| Repository Freshness | <p>The last commit date in the repository:</p><ul><li><strong>Active</strong>: Had commits in the last 3 months.</li><li><strong>Inactive</strong>: The last commits were made in the last 3 - 6 months.</li><li><strong>Dormant</strong>: No commits in the last 6 months.</li><li><strong>N/A</strong>: There are no commits detected by Snyk Essentials.</li></ul> |
| Source               | The integration that imported the asset.                                                                                                                                                                                                                                                                                                                              |
| Tags                 | The asset tags. For more details about tagging assets using a policy, see the [Tagging policy](https://docs.snyk.io/manage-risk/policies/assets-policies/use-cases-for-policies/tagging-policy) page.                                                                                                                                                                 |
| \*Title              | The name of the component for which the application context catalog was configured.                                                                                                                                                                                                                                                                                   |

**\***&#x41;ll filters marked with `*` are visible only if you configured the [application context](https://docs.snyk.io/developer-tools/scm-integrations/application-context-for-scm-integrations) catalog for your SCM integrations.

### Repository coverage widget

The repository coverage widget provides an overview of the percentage of scanned repositories compared to the total number of available repositories, using integrated Snyk or third-party security products.

Hover over any column to see how the coverage percentage is calculated.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-40663e6e1d6ce0ce8184c40e446261d68435b796%2Fimage.png?alt=media" alt=""><figcaption><p>Repository Coverage</p></figcaption></figure>

### Asset class breakdown

The asset class breakdown widget surfaces the distribution of repositories and container images by [asset class](https://docs.snyk.io/manage-assets/assets-inventory-components#class). Reviewing this widget allows you to determine the percentage of business-critical assets in your inventory and drill down to see the actual assets.

{% hint style="info" %}
**Tips**

* Having the context of the asset class is crucial for prioritizing assets. It is recommended to categorize your inventory by implementing [classification policies](https://docs.snyk.io/manage-risk/policies/assets-policies/use-cases-for-policies/classification-policy) to proactively classify existing and newly introduced assets.
* Using the filters enables narrowing down the asset class distribution within specific applications or code owners, as well as focusing on active repositories or a set of assets based on the asset tags.
  {% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-6714064155c3976953f4ca5c94a33c403a94de3f%2Fimage.png?alt=media" alt=""><figcaption><p>Asset Class Breakdown</p></figcaption></figure>

### Top 10 technologies breakdown

The top 10 technologies widget identifies the leading programming languages and frameworks used in repositories. Using the available filters enables you to determine the most commonly used technologies in active or business-critical repositories. Moreover, you can investigate specific applications or code owners.

{% hint style="info" %}
**Tips**

* The technology data is available in the [asset tags](https://docs.snyk.io/manage-assets/assets-inventory-components#tags).
* Click a presented technology to open the inventory page in a new browser tab. This will allow you to review the related repositories in detail.
  {% endhint %}

### Top 10 package managers breakdown

The top 10 package managers widget allows you to identify the leading package managers in your inventory. The quantities represent assets of package type. A [package asset](https://docs.snyk.io/manage-assets/assets-inventory-layouts#packages) is defined as software or library that is managed by package management systems.

### Repository freshness

The repository freshness widget displays the distribution of repositories according to the last commit date:

* **Active**: Had commits in the last 3 months.
* **Inactive**: The last commits were made in the last 3 - 6 months.
* **Dormant**: No commits in the last 6 months.
* **N/A**: Commits data is unavailable.

You can use this widget to surface the quantity of repositories that are more or less maintained in various contexts, such as specific applications.

{% hint style="info" %}
**Tips**

You can use the asset class filter to identify business-critical assets that are not being maintained. Click a specific slice to open the inventory page in a new browser tab where you can browse and learn more about those assets.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-85d662830fbd6d67eee9edd87b7af1054d7f24d7%2Fimage.png?alt=media" alt=""><figcaption><p>Repository freshness</p></figcaption></figure>

### Application context availability

The application context availability widget allows you to discover gaps in the context of assets. The available columns include:

* **Application Context** - displays the analyzed context attribute.
* **Unique Values** - shows how many unique instances exist for an attribute. For example, you can check how many unique applications or code owners are available for any of the listed attributes.
* **Availability in Repos** - indicates the completeness of a certain attribute across the repositories.

{% hint style="info" %}
**Tips**

* Before reviewing this widget, ensure that the results are cleaned up by filtering out the "dummy" attribute values, such as "unknown", "-", and so on.\
  You can clean up the values by selecting only the relevant values.
* Filtering by asset class allows you to identify business-critical repositories without a known code owner or associated application.
* Filtering by the "active" value of the repository freshness filter allows you to discover context gaps in repositories that are actively being developed.
* Reviewing the unique values allows you to spot gaps in context. For example, you may realize that the number of unique code owners does not match the number of teams.
  {% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-122bac325cf43afa7b94b83e4d66673efaa97b80%2Fimage.png?alt=media" alt=""><figcaption><p>Application Context Availability</p></figcaption></figure>

### Asset source breakdown

The asset source breakdown widget visualizes the quantities of detected assets from various sources. A source can be a platform where the asset is being managed directly (such as an SCM, container registry, and so on) or a platform that enriches the assets (such as security products and ASTs).

{% hint style="info" %}
**Tips**

* The widget displays the net quantities of detected assets for each source. If an asset is detected in more than one source, it will be counted once for each detected source.
* When asset inventory quantities seem incomplete or exceed expectations, this widget will help you discover which integrations should be examined and potentially configured differently.
  {% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-70677c5322e9cb5066bd68c3bc324152741659f0%2Fimage.png?alt=media" alt=""><figcaption><p>Asset source breakdown</p></figcaption></figure>

## Risk exposure report

This report gives you a single, consolidated view of your security risks. It allows you to quickly understand your risk exposure, track your progress in reducing it, and pinpoint high-risk areas.

The Risk Exposure Report helps AppSec teams make quicker, more informed decisions. Rather than reviewing multiple reports, it provides a clear overview of the security landscape, allowing you to:

* Make faster decisions by quickly identifying your biggest security challenges and where to focus your attention.
* Prioritize effectively by using data to guide your mitigation efforts toward the areas that contribute the most risk.
* Show progress by tracking the impact of your team on reducing risk over time with easy-to-understand visualizations.

### Severity source

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdufjGtE0kED7zHIl_L4jGrLbWkgeFfzbNwzEISsiINoEyWo2mQSnJxEBrzRca5bD1QCz-u60m-CQvDHVC-lx4gYd4LvsDrtTUkMcl6ff8V2q4uc5lUi1S8zAieM5s36JNVFbLU-Q?key=Dqdjzf6y3TJS6QA9IfBneg)

Choose your preferred severity source and automatically update selected severity throughout the report:

* **Snyk**: utilizing Snyk proprietary CVSS calculations and other factors, including the relative importance of the Linux distributor.
* **NVD CVSS**: leveraging severity scores from the National Vulnerability Database (NVD).
* **Non-SCA Severities:** For non-SCA issues (e.g., Code, IaC), Snyk's severity calculates High, Medium, and Low levels for specific code vulnerabilities and makes use of the Common Configuration Scoring System (CCSS) for IaC severity determinations

The report includes two main sections to provide a comprehensive view of your risk landscape:

### **Risk exposure Trends**

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd5HXXMoOzL2GsdBqF8tdO17PhaHx-1GdOdjVLAKpg46xqSMl1ooJB_KoaOkZb61O6Pu44KVI5hYkrn08aLiYfvKbIu0vZIraPlI1t44JcZP49KGbyYczwgn-jbXObBOmx-b_XF?key=Dqdjzf6y3TJS6QA9IfBneg" alt=""><figcaption></figcaption></figure>

This section provides a visual overview of your issues over time. You can view these trends by:

* **Severity**: See the distribution of issues across different severity levels.
* **Introduction Category**: Understand how issues are being introduced into your Projects.
* **Asset Class**: Group issues by the type of asset they affect.

### **Risk exposure Breakdown**

This detailed table breaks down issues and impacted assets. You can dynamically group the data to fit your needs by selecting from the following dimensions: group, organization, project, introduction category, and asset class.

The table is sorted by default to surface the total number of critical and high-severity issues, helping you focus on the most urgent risks first.

You can also export data to PDF or CSV and drill down into issues for more detail.

## Saved Views

The Saved Views feature enables collaboration based on shared, consistent, and customizable reports. This feature is available at Organization and Group level, in the **Reports** menu. It allows you to customize and save filter settings for your reports, which you can then reuse.

To make it easier to share the view outside of the Snyk platform, the URL of a saved view remains the same after it's created, regardless of any changes you make to it.

### Prerequisites

To create, edit, and remove a saved view, you must have **Edit reports** permission. Saved views are not private. After being created, Saved Views are visible to all users with **View reports** permission. Only Organization and Group Admins can assign these permissions. For more information, see [User role management](https://docs.snyk.io/snyk-platform-administration/user-roles/user-role-management).

To assign report permissions:

1. In the Snyk Web UI, navigate to your Group and Organization.
2. At the Group level, navigate to **Members** > **Manage Roles** > **Group Admin** and enable the following permissions:
   * **View reports:** to view Snyk Reports and to view the saved views that were created by others
   * **Edit reports:** to create saved views.
3. At the Organization level, enable the **View Organization reports** and **Edit Organization reports** permissions.

### Create a view

To create a new view:

1. In the Snyk Web UI, navigate to your Group or Organization.
2. Navigate to the **Reports** menu and select a report from the **Change Report** dropdown.
3. Select the **Standard view** filter and click **Create new view**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b33f4bea3f12f616e2873545a155b0724f0a70ad%2Freports_saved_views_standard_view.png?alt=media" alt=""><figcaption><p>Create new view button in the Standard view filter</p></figcaption></figure>

4. Fill in the name of the view and click **Create view**.

{% hint style="info" %}
The name of a saved view can contain a maximum of 60 characters and must be unique from other saved views for the same report.
{% endhint %}

### Update a view

To update a saved view:

1. In the Snyk Web UI, navigate to your Group and Organization.
2. Navigate to the **Reports** menu and select the report that contains the saved view you want to update.
3. From the **Standard view** filter, select and load the view you want to update.
4. Make any necessary changes to the report view.
5. Save the changes by clicking **Save** next to the Saved Views dropdown. This overwrites the existing view.

### Rename, delete, or copy the URL of a view

If you hover over the name of a saved view and click the three dots that appear, the following options are available:CommentShare feedback on the editor

* **Copy URL**: to copy the URL of the saved view
* **Set as Group default view:** to set a view as default for your Group. You can then remove it as the default by clicking **Remove as Group default view**.
* **Rename:** to rename the saved view
* **Delete**: to delete the saved view.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1a741534866b640908fa8640127f9bbf420617cb%2Freports_saved_views_view_options.png?alt=media" alt=""><figcaption><p>Options available for saved views</p></figcaption></figure>

### Example

Snyk offers built-in reports that you can customize based on associated report filters. A wide range of filters are available, some with multiple values. In such cases, you can save the state of the report using a saved view.

For example, your **Issues Detail** report shows a large number of issues and thus is difficult to manage.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-25a9100afe81449e62422e74562929ca97085060%2Freports_issue_detail.png?alt=media" alt=""><figcaption><p>An Issues Detail report</p></figcaption></figure>

You can add a **Computed Fixability** filter to your report to show only issues that are computed as **Fixable.**

Finally, you can add an **Exploit Maturity** filter to show only issues with a specific risk score.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7487e796d445caaab0a8e64402b6844f69cff1c1%2Freports_issue_detail_filtered_reports.png?alt=media" alt=""><figcaption><p>Filtered Issues Detail report</p></figcaption></figure>

You can then save this filtered view by clicking **Save**, adding a name to your view, and then clicking **Create view**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c502275eafdccb2dd12189a5c5f4416970423211%2Freports_saved_views_save_filtered_view.png?alt=media" alt=""><figcaption><p>Create view window</p></figcaption></figure>

You can then share the report with your development team by copying and sending the view URL.

## PR Check Report

{% hint style="info" %}
**Release status**

The PR Check report is in Early Access and available only with Enterprise plans.
{% endhint %}

This report combines adoption, performance, and reliability into a single view of PR scanning health, and it provides visibility into the adoption and performance of PR scanning across your different repositories.

You can use this report to determine where Snyk PR checks are implemented, where adoption could be increased, and which types of failures most frequently impact developer workflows. Together, these insights guide teams towards better PR scan coverage, more stable runs, and an improved developer experience across your whole Organization.

Filters and CSV downloads allow users to focus on specific groups or configurations for deeper analysis.

### PR check performance and status

You can visualize PR check performance through trend charts and summary tiles that display the successful, failed, and errored checks.

The charts break down performance across time and PR Check status. A secondary view distinguishes between Snyk Code and Snyk Open Source, allowing you to understand which product area contributes most to success or error patterns.

Use this report as an overview of platform reliability and scanning performance.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-295a1b074e79f1b98abf0660074f894a96fe934d%2Funknown.png?alt=media" alt=""><figcaption><p>PR check performance and status report</p></figcaption></figure>

### Error PR checks by error message

This view allows you to see the most common causes of PR check errors. This helps teams identify recurring issues and prioritize fixes that improve developer experience. The report highlights technical limitations or setup problems for quick resolution.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-71403b3ed227932b68234f5cf90e326c44d680cd%2Funknown.png?alt=media" alt=""><figcaption><p>Lst of error PR checks displayed by error message</p></figcaption></figure>

### PR scanning adoption

This view highlights PR scanning adoption across teams. You can view adoption by Group, Organization, or repository by using the dropdown controls.

Each view displays the following key indicators:

* SCM integrations with PR scanning
* Repositories using Snyk Code
* Repositories using Snyk Open Source

The layout displays where PR scanning is active and where further enablement could extend coverage across repositories. The long-term goal is to achieve full coverage, ensuring that 100% of repositories and integrations are included in PR scanning.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-76ad73f11253fdacebeaa7e4b1dacd9c3b07adaa%2Funknown.png?alt=media" alt=""><figcaption><p>PR scanning adoption view by Group</p></figcaption></figure>

### PR scanning performance

This view displays how PR activity across different Groups, Organizations, or repositories translates into scan coverage and failure rates.

You can go into detail by using the dropdown menu. The table summarizes total PRs and those with failed checks, and highlights where scanning activity is concentrated and where security risks can appear more frequently.

It is common that teams or repositories with higher PR volumes generate more checks. This view helps to surface patterns in failure distribution.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-991536d3bc49ca580ccdaa972f0b6c0a502f2214%2Funknown.png?alt=media" alt=""><figcaption><p>PR scanning performance view by Group</p></figcaption></figure>
