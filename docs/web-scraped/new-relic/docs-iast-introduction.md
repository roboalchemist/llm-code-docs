# Source: https://docs.newrelic.com/docs/iast/introduction/

Title: Introduction to IAST

URL Source: https://docs.newrelic.com/docs/iast/introduction/

Markdown Content:
The security of your software applications is essential to protect sensitive data, maintain the trust of your users, and comply with regulatory requirements. New Relic Interactive Application Security Testing (IAST) can help you prevent cyberattacks and breaches on your applications by probing your running code for exploitable vulnerabilities.

New Relic IAST helps address some of the limitations of more traditional application security tools. SAST, DAST, and penetration testing can struggle to keep pace with modern application delivery, especially applications based on distributed microservices. IAST can help by providing fewer false positive findings, which increases developer confidence and drives efficiency. You get double duty from your QA tests to continuously detect and prioritize vulnerabilities that are exploitable, along with guidance on how to mitigate the risk.

IAST helps you:

*   **Find and fix exploitable vulnerabilities**: No need to wait for scan results.
*   **Ship code faster**: Unmatched detection accuracy and substantially fewer false positives.
*   **See and secure every application**: Full visibility into your code, web components, and configuration data.
*   **Reduce time and cost**: When you eliminate vulnerabilities.
*   **Cut down the noise**: Use of both static application security testing (SAST) and dynamic application security testing (DAST) analysis.

[![Image 1: IAST testing status page](https://docs.newrelic.com/images/iast_screenshot-full_testing-status.webp)](https://docs.newrelic.com/images/iast_screenshot-full_testing-status.webp)

Go to **[one.newrelic.com](https://one.newrelic.com/)> All capabilities > IAST** to open the IAST testing status page.

IAST is fully integrated with [New Relic Vulnerability Management](https://docs.newrelic.com/docs/vulnerability-management/overview/), allowing you to continuously and quickly find, fix, and verify high-risk vulnerabilities across the software development lifecycle. IAST's exclusive proof of exploits helps you use your time more efficiently by providing you with a high-priority vulnerability, the steps to reproduce it, and remediation guidante.

Our agents deliver New Relic IAST and you can enable it with a simple configuration setting change. IAST is available in these languages:

| [Go agent](https://github.com/newrelic/csec-go-agent/tree/main#support-matrix) | [Java agent](https://github.com/newrelic/csec-java-agent#support-matrix) | [Node.js agent](https://github.com/newrelic/csec-node-agent/#supported--modules) | [Ruby agent](https://github.com/newrelic/csec-ruby-agent/tree/main#support-matrix) |
| --- | --- | --- | --- |
| APM version 3.30.0 or higher | APM version 8.9.0 or higher | APM version 11.10.4 or higher | APM version 9.12.0 or higher |

Follow [these instructions](https://docs.newrelic.com/docs/iast/install/) to install New Relic IAST.

About vulnerability severity (CVSS score)
-----------------------------------------

Discovering a vulnerability is important, but can be of little use without the ability to estimate a severity to each vulnerability. IAST assigns a qualitative severity to each vulnerability found in the system and according to the severity score of the [Common Vulnerability Scoring System (CVSS)](https://nvd.nist.gov/vuln-metrics/cvss). IAST works on CVSS version 3 (CVSSv3) for scoring.

The following table shows the version 3 (CVSSv3) ratings.

| Severity | Base Score Range |
| --- | --- |
| Low | 0.1-3.9 |
| Medium | 4.0-6.9 |
| High | 7.0-8.9 |
| Critical | 9.0-10.0 |
