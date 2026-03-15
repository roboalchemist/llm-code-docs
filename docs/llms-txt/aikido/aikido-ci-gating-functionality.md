# Source: https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality.md

# PR Gating Overview

Aikido CI gating allows you to scan feature branches for issues before they reach production. It covers open-source dependencies (SCA), IaC, Secrets, SAST, malware, license risks and code quality issues.

## Overview

Aikido offers two gating modes:

* **PR Gating:** Primarily handled via native integrations (GitHub, GitLab, Bitbucket, Azure). It scans the diff of your branch.
* **Release Gating:** Handled via the Aikido CLI. It ensures your final build is clean before deployment.

## Setup Options

You can configure gating in two ways:

1. **Aikido Interface:** Use our 1-click configuration for [GitHub](https://help.aikido.dev/pr-and-release-gating/github-ci-pr-gating-via-aikido-dashboard), [GitLab](https://help.aikido.dev/pr-and-release-gating/gitlab-mr-gating), [Bitbucket](https://help.aikido.dev/pr-and-release-gating/bitbucket-pr-gating), and [Azure](https://help.aikido.dev/pr-and-release-gating/azure-pr-gating). This setup is managed entirely within the Aikido interface, provides a better overview, and **doesn’t consume your CI minutes.**
2. **CI Pipeline:** For teams that prefer managing configuration in their own environment. You can use [Bitbucket Pipes](https://help.aikido.dev/pr-and-release-gating/bitbucket-pr-gating/bitbucket-pipes-setting-up-gating-for-pull-requests-via-code) natively, or integrate with any other runner (Jenkins, CircleCI, etc.) using the [Aikido CLI](https://help.aikido.dev/~/revisions/SGhJfnCIOpxRjx1gC1k5/pr-and-release-gating/cli-for-pr-and-release-gating) or our [Public CI API](https://help.aikido.dev/en/articles/8711075-aikido-ci-api).

## Configuring Your CI Gate

When you set up gating in Aikido, you have granular control over what triggers a failure. These settings are found by going to **Integrations > PR Quality Gating > \[Your Setup]**.

From here, you can:

* **Set Defaults:** Define the default gating configuration for all new repositories added to your workspace. See [Automatic Configuration for Newly Added Repos](https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/default-pr-mr-gating-configuration-for-new-repositories).
* **Bulk Edit:** Select multiple repositories to apply configuration changes across your entire project.
* **Granular Control:** Adjust settings for a single repository to handle specific project needs.
* **Advanced Settings:** Fine-tune how Aikido interacts with your workflow.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FUGDgcTISElHLXi7ECqzh%2FScreenshot%202025-12-17%20at%2016.04.20.png?alt=media&#x26;token=5682d601-59be-48c7-8bb2-3477141f139e" alt=""><figcaption></figcaption></figure></div>

### Severity Threshold

Select the minimum severity level that will cause the CI gate to fail (e.g., **Critical** or **High**).

* Any new issue detected at or above this level will break the build.
* Issues below this threshold will still be reported but won't block the merge.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZ9ULJIAYmqUSLP3tagCA%2FScreenshot%202025-12-17%20at%2016.01.28.png?alt=media&#x26;token=3bd91258-787b-4d9c-999d-7d10603980bb" alt=""><figcaption></figcaption></figure></div>

### Scans to Execute

Toggle specific scan types on or off for the CI gate. This allows you to focus on the security categories that are most relevant to your workflow.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FjOIdamcKnJDcEwOutDWO%2FScreenshot%202025-12-17%20at%2016.01.28.png?alt=media&#x26;token=66911b85-e193-44b8-9c14-4c6ffe6ccd56" alt=""><figcaption></figcaption></figure></div>

### Advanced Configuration

Fine-tune how Aikido interacts with your workflow to maintain developer velocity:

* **Always make the PR check green:** Use this to get security visibility without physically blocking merges. Aikido runs full scans but always reports a "Success" status to your git provider. Perfect for teams in the initial "visibility phase."
* **Disable checks on draft Pull Requests:** Avoid generating noise on work-in-progress code. Scans only trigger once the PR is moved to "Ready for Review."

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FL55UAiF9ZMPN4hIArHF0%2FScreenshot%202025-12-17%20at%2016.18.51.png?alt=media&#x26;token=1ec55b61-8097-40eb-bda1-a6fca076319f" alt=""><figcaption></figcaption></figure></div>

## **Checking results**

After a CI run, Aikido provides a direct link to the scan results for that specific branch. Because Aikido scans the branch diff rather than the entire repo, it clearly distinguishes between **fixed issues** and **newly introduced risks**.

* **Fixed in branch:** If a PR resolves an existing vulnerability, Aikido marks it as "PR open" in your feed, allowing you to verify the fix before merging.
* **New issues:** Anything introduced in the branch that exceeds your severity threshold will trigger a failure (unless "Always Green" is enabled).

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FJ4OsaC46WPzzQmg2nVE1%2FScreenshot%202025-12-17%20at%2016.27.20.png?alt=media&#x26;token=9f58c76b-8059-47a4-a1ea-db291fb283f5" alt=""><figcaption></figcaption></figure></div>

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e4ecd31199baf3a34e9d4b38474cff1772622b50%2Faikido-ci-gating-functionality_8e9a6629-93f8-4f78-a264-732e5ff5351f.png?alt=media" alt="Table listing unresolved critical security issues in software projects with open tasks."></div>

### Bypassing a failed state <a href="#bypassing-a-failed-state" id="bypassing-a-failed-state"></a>

In case you would like to bypass a failed state, this is possible by ignoring the issues that caused the CI gate to fail. You can do this by clicking the issue and in the top right **Actions menu** select Ignore or Snooze. This issue will then be ignored/snoozed in any future branches in your CI.

{% hint style="info" %}
Only users that have the permission to snooze or ignore issues can bypass the CI gate.
{% endhint %}
