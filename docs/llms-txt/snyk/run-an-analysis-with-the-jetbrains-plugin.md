# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/jetbrains-plugin/run-an-analysis-with-the-jetbrains-plugin.md

# Run an analysis with the JetBrains plugin

{% hint style="info" %}
Ensure the Snyk extension is configured, authenticated, and trusted for your current Project, as described in the configuration and authentication pages.
{% endhint %}

You can trigger `snyk test` using one of these methods:

* automatic (default)
* manual

A Snyk scan is triggered automatically when you open your Project and when you save any supported files. This behavior can be turned off in [user experience configuration](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/configuration-for-the-snyk-jetbrains-plugin-and-ide-proxy#user-experience).

{% hint style="info" %}
Ensure your files are saved before manually running an analysis.
{% endhint %}

To manually trigger `snyk test` , as illustrated in the following screen image:

1. Click the Snyk icon in the sidebar to open the Snyk panel.
2. Click the **Run (play)** button at the top of the plugin sidebar.
3. If the play button is grayed out, there is a scan in progress. Wait for it to complete before starting another scan.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-be62a2c314315d595384ef622248b761ef33ccf5%2FrunAnalysis.png?alt=media" alt="How to manually trigger a Snyk analysis"><figcaption><p>Manually triggering a Snyk analysis</p></figcaption></figure>

## Scan configuration

You may customize your scan behavior to reflect the security policy of your company or to focus on certain areas.

### Severity filter

Snyk reports critical, high, medium, and low severities. There are two ways to control severity:

* Use the plugin settings for the [Scan configuration](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/configuration-for-the-snyk-jetbrains-plugin-and-ide-proxy#general-settings).
* Use the small buttons with the severity icons at the top of the issues in the Snyk panel.

By default, all levels are selected. You must select at least one.

Snyk severity icons have the following meaning:

| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0964f55a564a59f90e3dafb653d5cd0bff7be603%2Fimage%20\(50\).png?alt=media) Critical severity | May allow attackers to access sensitive data and run code on your application.                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-35db9c5b28b416932407dcc20cb40cf0d4b1a9ed%2Fimage%20\(29\).png?alt=media) High severity     | May allow attackers to access sensitive data on your application.                                                                            |
| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f313e50f5a233da9896f390a4db0483d5186b6a0%2Fimage%20\(62\).png?alt=media) Medium severity   | May allow attackers under some conditions to access sensitive data on your application.                                                      |
| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-680033c036e72c136475928f88590f463bbaa52a%2Fimage%20\(37\).png?alt=media) Low severity      | The application may expose some data allowing vulnerability mapping, which can be used with other vulnerabilities to attack the application. |

### Filter by issue type

Snyk reports the following types of issues:

* Open Source issues: found in open source dependencies. For details, see the section [Snyk Open Source issues](#snyk-open-source-issues).
* Code Security issues: found in your application’s source code. For details, see the section [Snyk Code security vulnerabilities and quality issues](#snyk-code-security-vulnerabilities-and-quality-issues).
* Code Quality issues: found in your application source code. For details, see the section [Snyk Code security vulnerabilities and quality issues](#snyk-code-security-vulnerabilities-and-quality-issues).
* Infrastructure as Code issues: found in infrastructure as code files. For details, see the section [Snyk Infrastructure as Code issues](#snyk-infrastructure-as-code-issues).
* Container issues: found in images sourced from Kubernetes workload files. For details, see the section [Snyk Container issues](#snyk-container-issues).

{% hint style="info" %}
The exact capabilities and available scanners depend on your plan. Be sure your Organization's admin has enabled all Snyk products prior to configuring any of them in the IDE plugin.
{% endhint %}

There are two ways to show or hide specific issue types:

* Use the plugin settings for the [Scan configuration](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/configuration-for-the-snyk-jetbrains-plugin-and-ide-proxy#general-settings).
* Use the filter button in the panel's sidebar, as illustrated in the screen image that follows

By default, all issue types shown are selected.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d146a70fc26befe2db1099a008453f97e44689e5%2FSCR-20241024-miah.png?alt=media" alt="Show or hide specific issue types"><figcaption><p>Filter to show or hide specific issue types</p></figcaption></figure>

### Net new issues versus all issues

Beginning with plugin version [2.10.0](https://plugins.jetbrains.com/plugin/10972-snyk-security/versions/stable/623034), it is possible to see only newly introduced issues.

This functionality reduces noise and allows you to focus only on current changes. This will prevent issues early, thus unblocking your CI/CD pipeline and speeding up your deliveries.

The logic uses your local Git repository or any folder to compare the current findings with those in a base branch or reference folder. Net new issues scanning (delta scanning) shows you the difference between the two branches or folders, highlighting only the new issues.

In plugin version 2.12.0 and later, you can choose any folder as your base for scanning.

To apply the filter and see only the new issues, use the toggle in the summary panel.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-47ec9bec4637d9071e2482fc597b0fa9e045e0fc%2Fimage.png?alt=media" alt=""><figcaption><p>Summary panel toggle showing the the total number of issues and the number of issues in the checked out branch or current folder or new issues only</p></figcaption></figure>

You can also enable the net new issues feature in the [scan configuration](#scan-configuration) settings.\
\
For newly created feature branches, there will be no reported issues. That is an intended state that developers would aim for, as illustrated in the screen image that follows:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5883f8d331c3803f01ae2340805d1ccc7989b025%2FSCR-20241024-ngbm.png?alt=media" alt="Successful state. No Net New issues found"><figcaption><p>Successful state, no net new issues found</p></figcaption></figure>

### Changing the base branch

The base branch is usually automatically determined for each Git repository.

You can change the base branch or base folder by following these steps, as illustrated in the screen image that follows:

1. Click on the top-level node in the issues tree.
2. Use the dropdown selection.
3. Choose any branch.
4. Click OK to save the selection.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f2b97850d916629ce8ec6107c6e42588f0b253ac%2FSCR-20241024-nfhj.png?alt=media" alt="Change base branch for calculation Net New issues"><figcaption><p>Choosing the base branch or folder</p></figcaption></figure>

## Available Snyk issue types

### Snyk Code security vulnerabilities and quality issues

Snyk Code analysis shows a list of security vulnerabilities and code quality issues found in your application code.

{% hint style="info" %}
Effective beginning on June 24, 2025, Snyk Code Quality issues will no longer be provided.
{% endhint %}

For more details and examples of fixes others used to fix the issue, select the security vulnerability or the code security issue.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8ccc089343ac9bf645e020e9f649bdbfe54d127f%2FSCR-20241024-npba.png?alt=media" alt=""><figcaption><p>Snyk Code issue details</p></figcaption></figure>

### Snyk Open Source issues

Snyk Open Source analysis shows a list of vulnerabilities and license issues found in all manifest files. To see more detailed information, select a vulnerability or license issue.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a4f1a31f34ae55b045eed7126954fac09e284b8e%2FSCR-20241024-nrsk.png?alt=media" alt="Snyk Open Source issue details"><figcaption><p>Snyk Open Source issue details</p></figcaption></figure>

### Snyk Infrastructure as Code issues

With every scan, Snyk IaC analysis shows issues in your Terraform, Kubernetes, AWS CloudFormation, and Azure Resource Manager (ARM) code. The scan is based on the Snyk CLI and is fast and friendly for local development. To see more detailed information, select an issue.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-aced2e57feaa52c94c1862e93945055c160f18f1%2FSCR-20241024-ntcr.png?alt=media" alt="Snyk IaC issue details"><figcaption><p>Snyk IaC issue details</p></figcaption></figure>

### Snyk Container issues

{% hint style="info" %}
The Snyk JetBrains IDE plugin will no longer detect container images specified in Kubernetes YAML files in versions released after June 24, 2025.
{% endhint %}

The JetBrains plugin scans Kubernetes configuration files and searches for container images. Vulnerabilities are found quickly using the extracted container images and comparative analysis against the latest information from the [Snyk Vulnerability Database](https://security.snyk.io).

Snyk Container analysis shows each of the security vulnerabilities that might affect your image. To see more detailed information, select a vulnerability.

A comparison table shows the severity levels, such as critical or high. This shows the difference in vulnerabilities between the current image and the image recommended by Snyk, with the same characteristics sorted by severity. This helps you decide if you want to upgrade your image to the recommended one and increase the level of confidence in the image you are running in production.
