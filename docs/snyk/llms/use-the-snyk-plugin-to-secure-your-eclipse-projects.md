# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/eclipse-plugin/use-the-snyk-plugin-to-secure-your-eclipse-projects.md

# Use the Snyk plugin to secure your Eclipse projects

After the Eclipse plugin is downloaded and authentication is complete, the plugin starts the workspace scan. You may notice a confirmation that a workspace scan is starting. Alternatively, you can trigger a workspace scan from the context menu of your Project, or from the Snyk View.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-05cf6a8a67b66fbb7d751689345878ddc4cb91c6%2FScreenshot%202022-10-19%20at%2009.02.25.png?alt=media" alt=""><figcaption><p>Starting workspace scan</p></figcaption></figure>

## Issues are displayed in the Eclipse plugin

All of the issues found by Snyk are now integrated natively with Eclipse flows. Issues are shown in the **Problems** tab, as illustrated in the following screen image. There is a squiggly line indicating the issue while you code, along with gutter icons to indicate where the issue is.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c5c844ce96a72c9bf9acb5351d627fd7f8485be3%2FScreenshot%202022-05-13%20at%2012.20.26.png?alt=media" alt=""><figcaption><p>Eclipse Problems tab</p></figcaption></figure>

In addition, starting with version 3+, Snyk provides a custom UI in the Snyk Tab, that displays issue details:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-74dee5188d51d58d48623fe7c543105cff3d356e%2Fimage.png?alt=media" alt=""><figcaption><p>Issue details in Eclipse plugin</p></figcaption></figure>

## Severity filtering

Filter issues by severity level to reduce noise and focus on high-severity issues.

To hide low-severity issues, navigate to **View > Severity** and clear **Low Severity**. Select **Show All Severities** to enable or disable all severity filters.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FhQubadOKAVAISQvgHu4D%2FScreenshot%202025-12-22%20at%2015.55.35.png?alt=media&#x26;token=fa71c60e-0596-47aa-8dd1-07e3aab9b934" alt=""><figcaption><p>Severity filters in the View menu</p></figcaption></figure>

## Issue View Options

[Code Consistent Ignores](https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/ignore-issues/consistent-ignores-for-snyk-code) filters issues to help teams focus on critical tasks. After you create an ignore, Snyk applies it to all tests and branches.

{% hint style="info" %}
These filters do not apply if you disable **Code Consistent Ignores** for the Organization.
{% endhint %}

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fx3aMxtsGgPdsWbNeTGTB%2FScreenshot%202025-12-22%20at%2015.58.46.png?alt=media&#x26;token=853858c5-daf2-41fe-a1cf-74e05bcf7815" alt=""><figcaption><p>Issue View Options alongside the Net New filter in the View menu</p></figcaption></figure>

## Net new issues versus all issues

Starting with version 3.1.0, it is possible to see only newly introduced issues.

This functionality reduces noise and allows you to focus only on current changes. This helps prevent issues early, thus unblocking your CI/CD pipeline and speeding up your deliveries.

The logic uses your local Git repository or any folder to compare the current findings with those in a base branch or reference folder. Net new issues scanning (delta scanning) shows you the difference between the two branches or folders, highlighting only the new issues.

To apply the filter and see only the new issues, use the **total**/**new** toggle in the summary panel, or apply the **Show only Net New Issues filter** from the **View** menu (under **Issues Status**).

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-31331216844fcbd492919d76eb18b0ed275e7c22%2Fimage.png?alt=media" alt=""><figcaption><p>Net new issues filter enabled after clicking on the total/new issues toggle</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-02eb579647280c725cf540bcd7b8eaf7a6c8af08%2Fimage.png?alt=media" alt=""><figcaption><p>Activate Net new issues in the dot menu of the Snyk View</p></figcaption></figure>

For newly created feature branches, there will be no reported issues. That is an intended state that developers would aim for, as illustrated in the screen image that follows:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-f1ae79ad43d0be725641c289a246b277a9b0948a%2Fimage%20(269).png?alt=media" alt=""><figcaption><p>No new issues introduced in a newly created branch</p></figcaption></figure>

The base branch is usually automatically determined for each Git repository.

You may change the base branch or base folder by following these steps, as illustrated in the screen image that follows:

1. Toggle the **total**/**new** filter in the summary panel.
2. Click on the top-level node in the Issues tree to change the branch or directory.
3. Use the dropdown selection to choose any branch or reference folder.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-633aabba8f2fc7a4dabc6b635587b5e4a46522c2%2Fimage.png?alt=media" alt=""><figcaption><p>Changing reference branch or reference directory for calculation net new issues</p></figcaption></figure>

\
Continue by following the instructions on the page for the type of scan you are doing:

* [SAST scanning results (SAST, Snyk Code)](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/eclipse-plugin/sast-scanning-results-sast-snyk-code)
* [Misconfiguration scanning results (Snyk Infrastructure as Code)](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/eclipse-plugin/misconfiguration-scanning-results-snyk-infrastructure-as-code)
* [Third-party dependency scanning (SCA, Snyk Open Source)](https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/eclipse-plugin/third-party-dependency-scanning-sca-snyk-open-source)
