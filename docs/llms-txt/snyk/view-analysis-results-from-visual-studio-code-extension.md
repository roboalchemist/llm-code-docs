# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension.md

# View analysis results from Visual Studio Code extension

## Overview of results

Snyk analysis shows a list of security vulnerabilities and code issues in the application code. Select a security vulnerability or a code security issue to view more details and examples of how others fixed the issue. The **Issue details panel** appears in a tab on the right side of the screen, as shown in following screen image.

The **Snyk analysis panel** on the left shows the time the analysis took and a list of issues with the suggestions found for those issues.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-07a74f25e035478cfad7b673c3af38be7e6cfcce%2FSCR-20241024-rqfj.png?alt=media" alt="Snyk Security extension with Snyk Code issue"><figcaption><p>Snyk Security extension with Snyk Code issue</p></figcaption></figure>

Each issue contains a severity icon that has the following meaning:

| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-0964f55a564a59f90e3dafb653d5cd0bff7be603%2Fimage%20\(50\).png?alt=media) Critical severity | May allow attackers access to sensitive data and to run code on your application.                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-35db9c5b28b416932407dcc20cb40cf0d4b1a9ed%2Fimage%20\(29\).png?alt=media) High severity     | May allow attackers access to sensitive data on your application.                                                                            |
| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f313e50f5a233da9896f390a4db0483d5186b6a0%2Fimage%20\(62\).png?alt=media) Medium severity   | May allow attackers under some conditions to have access to sensitive data on your application.                                              |
| ![](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-680033c036e72c136475928f88590f463bbaa52a%2Fimage%20\(37\).png?alt=media) Low severity      | The application may expose some data allowing vulnerability mapping, which can be used with other vulnerabilities to attack the application. |

## Scan configuration

You can customize your scan behavior to reflect your company's security policy or to focus on certain areas.

### Severity filter

Snyk reports critical, high, medium, and low severities. This can be adjusted in the [scan configuration settings](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/visual-studio-code-extension-configuration-environment-variables-and-proxy).

By default, all levels are selected. You must select at least one.

### Filter by issue type

Snyk reports the following types of issues:

* Open Source issues: Found in open-source dependencies; for more details, see [Analysis results: Snyk Open Source](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension/analysis-results-snyk-open-source).
* Code Security issues: Found in your application’s source code; for more details, see [Analysis results: Snyk Code](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension/analysis-results-snyk-code).
* Infrastructure as Code issues: Found in infrastructure as code files; For more details, see [Snyk IaC Analysis results: Snyk IaC Configuration](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension/analysis-results-snyk-iac-configuration).

{% hint style="info" %}
The exact capabilities and available scanners depend on your Snyk plan. Be sure your Organization's admin enabled all Snyk products prior to configuring any of them in the IDE plugin.
{% endhint %}

You can set the issue types to be shown in the Scan configuration settings. By default, all issue types shown are selected.

### Net new issues versus all issues

Starting with Visual Studio Code extension version 2.19.0, it is possible to see only newly introduced issues.

This functionality reduces noise and allows you to focus only on current changes. This helps prevent issues early, thus unblocking your CI/CD pipeline and speeding up your deliveries.

The logic uses your local Git repository or any folder to compare the current findings with those in a base branch or reference folder. Net new issues scanning (delta scanning) shows you the difference between the two branches or folders, highlighting only the new issues.

In Visual Studio Code version 2.21.0 and later, you can choose any folder as your base for scanning.

To apply the filter and see only the new issues, use the **total** or **new** toggle in the summary panel.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1bd38bc13bb3c46b7ea2cc7c17fb41ac7460d661%2Fimage.png?alt=media" alt=""><figcaption><p>Summary panel with a toggle that shows the total number of issues, and the number of issues in the checked out branch or current folder</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-05473a50643403cdcf028447558755297ca4726d%2Fimage.png?alt=media" alt=""><figcaption><p>Net new issues filter enabled after the user clicks on the total/new issues toggle</p></figcaption></figure>

You can also enable the net new issues feature in the [scan configuration](#scan-configuration) settings for the extension.

For newly created feature branches, there will be no reported issues. That is an intended state that developers would aim for, as shown in the screen image that follows:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-9e0b241dafc2f9ff88c16259c38ca28e46072f42%2FSCR-20241024-ruvq.png?alt=media" alt="Successful state. No Net New issues found." width="304"><figcaption><p>Successful state. No net new issues found.</p></figcaption></figure>

### Changing the base branch

The base branch is usually determined automatically for each Git repository.

You can change the base branch or base folder by following these steps:

1. Select the Snyk plugin.
2. Toggle the `total/new` filter in the summary panel.
3. Click on the top-level node in the issues tree to change the branch or directory.
4. Use text input to specify any branch name or reference directory.
