# Source: https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/severity-levels.md

# Severity levels

Use severity levels to help you with [vulnerability assessment](https://snyk.io/learn/vulnerability-assessment/) for your applications. Severity levels indicate the assessed level of risk, as **C**ritical, **H**igh, **M**edium, or **L**ow. Snyk reports the number of vulnerabilities at each level of severity in many places in the Snyk application. The display varies; a typical example follows.

<img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5c0c572108790ca4e26203520a33a600107a4b06%2FScreenshot%202022-08-16%20at%2009.52.22.png?alt=media" alt="Issues at each level of severity, C, H, M, and L" data-size="original">

{% hint style="info" %}
Severity levels also apply to license issues. See [Licenses](https://docs.snyk.io/scan-with-snyk/snyk-open-source/scan-open-source-libraries-and-licenses/open-source-license-compliance).
{% endhint %}

The severity levels are defined in the following table.

| Icon                                                                                                                                                                                                                                                                                                                                       | Level        | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| <img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1513e24c07c9bae9b86a7ae66295b84f09794e07%2Fimage.png?alt=media" alt="C" data-size="line">                                                                                                       | **C**ritical | May allow attackers to access sensitive data and run code on your application                                                              |
| <img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0d07ed1d261138fb70d49e1a2eb3303f9c69daae%2Fimage%20(103)%20(1)%20(1)%20(1)%20(1)%20(1)%20(1)%20(2).png?alt=media&#x26;token=f7589b87-e404-419b-be01-c57b5ac2508d" alt="H" data-size="original"> | **High**     | May allow attackers to access sensitive data in your application                                                                           |
| ![M](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-12406488dc8d63ee93363b62f220f10c5ccc666c%2Fimage.png?alt=media)                                                                                                                                      | **M**edium   | Under some conditions, may allow attackers to access sensitive data on your application                                                    |
| ![L](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-aa748f59862a13bc369e1d5b4fdb1ef7bd977501%2Fimage%20\(60\).png?alt=media)                                                                                                                             | **L**ow      | Application may expose some data that allows vulnerability mapping, which can be used with other vulnerabilities to attack the application |

## Severity levels and Priority Score

Severity levels are one factor used in determining the Snyk Priority Score for each vulnerability. Other factors include [Snyk Exploit Maturity](https://snyk.io/blog/whats-so-wild-about-exploits-in-the-wild-and-how-can-we-prioritize-accordingly/) and [Reachable Vulnerabilities](https://snyk.io/blog/optimizing-prioritization-with-deep-application-level-context/) information.

See [Snyk Priority Score](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/priority-score) for details.

## How to view severity levels

Severity levels are displayed throughout Snyk, to keep this information visible at all times.

For example, the severity levels appear in the **Pending tasks** section of the Dashboard:

<img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-2096af5c4461a40871a2cbd65ba1947211294d40%2Fimage.png?alt=media" alt="Severity levels with Pending tasks" data-size="original">

Severity levels are displayed in association with your [Snyk Projects](https://docs.snyk.io/snyk-platform-administration/snyk-projects):

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5690064863499e700834b60b4b8c9ff937b10f00%2Fimage.png?alt=media" alt="Severity levels assoicated with Projects"><figcaption><p>Severity levels associated with Projects</p></figcaption></figure>

The number of issues at each severity level is also displayed in the left sidebar of an issue card:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f08f7c56833013021bb53455daf12aafa9890042%2Fimage%20(39).png?alt=media&#x26;token=b3a83c57-bd5e-4e60-9982-02c2134c3d85" alt="Issue card; severity levels in sidebar"><figcaption><p>Issue card; severity levels in sidebar</p></figcaption></figure>

## How Snyk determines severity levels

### Severity levels and CVSS

The Common Vulnerability Scoring System (CVSS) determines the severity level of a vulnerability.

Snyk supports the [CVSS framework version 4.0](https://www.first.org/cvss/v4-0/), along with the previous version, [CVSS framework version 3.1](https://www.first.org/cvss/v3-1/), to designate the characteristics and severity of vulnerabilities.

Vulnerabilities published prior to the support of CVSS v4.0, are based on the 3.1 version of CVSS to define severities.

| **Level** | **CVSS score** |
| --------- | -------------- |
| Critical  | 9.0 - 10.0     |
| High      | 7.0 - 8.9      |
| Medium    | 4.0 - 6.9      |
| Low       | 0.0 - 3.9      |

The severity level and score are determined based on the CVSS Base Score calculations using the [Base Metrics](https://www.first.org/cvss/v4.0/specification-document#Base-Metrics). The Temporal Score, based on the Temporal Metrics, affects the Priority Score.

See [Scoring security vulnerabilities 101: Introducing CVSS for CVEs](https://snyk.io/blog/scoring-security-vulnerabilities-101-introducing-cvss-for-cve/).

{% hint style="info" %}
Severity levels may not always align with CVSS scores. For example, Snyk Container severity scores for Linux vulnerabilities may vary depending on NVD severity rankings; see [Understanding Linux vulnerability severity](https://docs.snyk.io/scan-with-snyk/snyk-container/how-snyk-container-works/severity-levels-of-detected-linux-vulnerabilities) for details.
{% endhint %}

### Why are there multiple CVSS Scores for the same vulnerability?

There are multiple CVSS Scores for the same vulnerability for several reasons:

* ​When evaluating the severity of a vulnerability, it is important to note that there is no single CVSS vector. There are multiple CVSS vectors defined by multiple vendors; the [National Vulnerability Database](https://nvd.nist.gov/) (NVD) is one.
* The majority of vulnerabilities published by Snyk originate from [proprietary research](https://security.snyk.io/disclosed-vulnerabilities), public information sources, or through third-party disclosures.
* For example, when Snyk discovered the Critical Severity [Spring4Shell vulnerability](https://security.snyk.io/vuln/SNYK-JAVA-ORGSPRINGFRAMEWORK-2436751), the advisory was published on March 30, 2022, with the CVSS vector analysis. This was before an official CVE was assigned and before NVD conducted its analysis, which was published nine days later on April 8, 2022.
* Having some differences in CVSS vectors is normal and expected. The likelihood of certain attack vectors will involve discrepancies and judgments made about them that make sense for the application and use cases of open source software users.
* The severity of a vulnerability is influenced by a variety of factors, including whether it comes from a "red team" angle or a "blue team" angle. To arrive at an objective and actionable rating, Snyk analysts examine the full range of data, from vendors to reporters to attackers.
* There are times when a vendor discovers additional information about a vulnerability that can affect its severity. Users can find all the relevant information used to determine the severity that Snyk curated in the description and references of the advisory.
* Different vendors may use different versions of CVSS, resulting in differing scores and severity levels. For instance, Snyk adopted CVSS version 4.0 as its primary framework in 2024. When comparing a vulnerability published by Snyk using [CVSS v4.0 ](https://www.first.org/cvss/v4-0/)with one published by the NVD using CVSS v3.1, the scores and severity ratings may differ significantly. In addition, CVSS score calculation can be done based on different vectors:

  * Base (CVSS-B),
  * Base + Threat (CVSS-BT),
  * Base + Environmental (CVSS-BE),
  * Base + Threat + Environmental (CVSS-BTE).

  Snyk performs the calculation of the score and the severity based on the Base metrics (as advised in compliance frameworks like FedRAMP and PCI-DSS) and provides the Threat Metric (also known as Exploit Maturity) as a separate data point.

### Severity levels and CCSS

The Common Configuration Scoring System (CCSS), developed by the National Institute of Standards and Technology (NIST) and derived from CVSS, measures the severity of software security configuration issues.

Snyk uses the [CCSS](https://www.nist.gov/publications/common-configuration-scoring-system-ccss-metrics-software-security-configuration) to designate the characteristics and severity of IaC+ vulnerabilities and misconfigurations.

| **Level** | **CCSS score** |
| --------- | -------------- |
| Critical  | 9.0 - 10.0     |
| High      | 7.0 - 8.9      |
| Medium    | 4.0 - 6.9      |
| Low       | 0.0 - 3.9      |

The severity level and score are determined based on the CCSS Base Score calculations using the Base Metrics.
