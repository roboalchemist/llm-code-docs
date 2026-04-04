# Source: https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests/create-automatic-prs-for-new-fixes-fix-prs.md

# Create automatic PRs for new fixes (Fix PRs)

{% hint style="info" %}
**Feature availability**

* The Automatic Fix PRs feature is supported for the following SCM integrations: GitHub, GitHub Enterprise, GitHub Cloud App, Bitbucket Server, Bitbucket Cloud, Bitbucket Connect, GitLab, and Azure Repos.
* The Automatic Fix PR settings may vary depending on the integration.
  {% endhint %}

The following rules are applied to the creation of automatic PRs for vulnerabilities:

* Pull requests are created based on the **Test & Automated Pull Request Frequency** notification setting.
* If you select **Retest now** for the Project, a scan runs manually. The 24-hour window is marked as having had the scan run. and no automatic PR is created until the next automated scan runs.
* One pull request is created per Project.
* A **new vulnerability** is a vulnerability in the current recurring scan that was not present in the previous scan of the same project.
* If either the vulnerability is new and has a fix available **or** the fix is new and is not ignored, a Fix PR can be created.
* Fixing a vulnerability by upgrading a package may sometimes introduce a new vulnerability. Snyk will only automatically create such a pull request if the fixed vulnerabilities are a higher severity than any new ones introduced.
* For known vulnerabilities, see [Configure Automatic Backlog PRs.](https://docs.snyk.io/scan-with-snyk/pull-requests/snyk-pull-or-merge-requests/create-automatic-prs-for-backlog-issues-and-known-vulnerabilities-backlog-prs)

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-df1161dccb120e3c51b4688b23b8e1ec6676983d%2Fproject-settings-test-pull-request-frequency.png?alt=media" alt="Test &#x26; Automated Pull Request Frequency setting"><figcaption><p>Test &#x26; Automated Pull Request Frequency setting</p></figcaption></figure>

To determine when your last 24-hour window began, check the Project issue card for **Snapshot taken by recurring test** and check your email for **\[snyk] Vulnerability alert** for specific scan results:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-9754f10b5b77319d52ae7fdac14de5d6a79e71ef%2Fproject-snapshot-taken.png?alt=media" alt="Snapshot taken by recurring test 16 hours ago"><figcaption><p>Snapshot taken by recurring test 16 hours ago</p></figcaption></figure>

Pull requests for new vulnerabilities are enabled by default for new integrations.

See the [Git repository SCM integrations](https://docs.snyk.io/developer-tools/scm-integrations/organization-level-integrations) pages for details about supported integrations.

## Enable or disable pull requests for an integration

Follow these steps to enable pull requests at the global integration level:

1. Navigate to **Settings** > **Integrations**.
2. Select an SCM integration, for example, GitHub.
3. Enable **New vulnerabilities** and click **Save.**

**Apply changes to all overridden Projects** will update all of the individual Project settings for **Automatic fix PRs**. If a Project previously had its own settings for automatic fix pull requests, clicking the button will override the Project setting with the global setting.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-7f0c95f209e66a9553a316d04b5fd8375ffb6d50%2FScreenshot%202023-05-03%20at%2014.49.59.png?alt=media" alt=""><figcaption><p>Configure Automatic Fix PRs</p></figcaption></figure>

If you select **Fix all vulnerabilities for the same dependency in a single PR**, this will add any PR opened to address an issue with any potential PR for upgrades which also fix the same issue. So, fixing an instance of the vulnerability may imply that other vulnerabilities will also be fixed implicitly.

## Set creation thresholds for score and severity

For every new actionable vulnerability found on each recurring test, Snyk raises a Fix PR. This may not be ideal depending on the velocity you are looking for in your organization, so setting up specific criteria to match your needs can be achieved through setting thresholds.

To decide which automatic Fix PRs are visible to you, you can set a custom threshold for **Score** or **Severity.** You will have either Risk or Priority Score available in the dropdown depending on which is configured for your Organization.

### Score threshold

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-8ecf607c537dd42d4479cde15e9e89b0b566ffe6%2Ffix-pr-threshold-risk-score.png?alt=media" alt=""><figcaption><p>Fix PR Threshold by score</p></figcaption></figure>

Snyk will create Fix PRs only above the threshold you set in the **Score** field. The score type you use will display as the option for the dropdown. This threshold ranges from 0-1000.

The set defaults for score are as follows:

* Organizations created before December 5, 2024 have a default score of 0.
* Organizations created after December 5, 2024 have a default score of 700.
* After June 5, 2025, all Organizations will have a default score of 700 unless you have configured a score in the setting.

### Severity threshold

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-fc4e434bfc5e9b23ac8edcb297259abeb55a7427%2Ffix-pr-threshold-severity.png?alt=media" alt=""><figcaption><p>Fix PR Threshold by Severity</p></figcaption></figure>

Snyk will create Fix PRs for the severity levels selected, for example, Critical and High.

## Enable or disable pull requests for a single Project

Enabling or disabling at a Project level will override the pull request setting for this single Project, so it will not inherit from the global integration setting.

1. Under **Projects,** select a Project and select **Settings**.
2. Select an SCM integration, for example, GitHub.
3. In the **Automatic fix pull requests** section:
   * Select **Customize for only this project**
   * Enable **New vulnerabilities**
   * Select **Save changes**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-a6319a6eceb734d070c8ccb11ac4613a5581cb06%2Fproject-settings-github-integration-automatic-fix-pull-requests.png?alt=media" alt="Automatic Fix pull requests settings at the project level"><figcaption><p>Automatic Fix pull requests settings at the project level</p></figcaption></figure>
