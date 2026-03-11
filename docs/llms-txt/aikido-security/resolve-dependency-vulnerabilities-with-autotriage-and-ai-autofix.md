# Source: https://help.aikido.dev/workflows-and-guides/resolve-dependency-vulnerabilities-with-autotriage-and-ai-autofix.md

# Fix Dependency Issues with AutoTriage and AutoFix

### Prerequisites

You'll need:

* An [Aikido account](https://app.aikido.dev/login)
* A personal [GitHub account](https://github.com/login) (to fork the sample project)

## Connect sample repo to Aikido

This tutorial will make use of a public repository called [Damn Vulnerable Python Web App](https://github.com/anxolerd/dvpwa), a variant of the popular [Damn Vulnerable Web Application](https://github.com/digininja/DVWA) used for demoing security tools.&#x20;

First, [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the [DVPWA](https://github.com/anxolerd/dvpwa) repository to your GitHub namespace so you have a personal copy to work with. Then log into an Aikido workspace and navigate to **Repositories > Manage Repos**. Click **Add Repo**. If prompted, grant GitHub permission to select repositories and choose your forked repo of DVPWA.&#x20;

If redirected to Aikido and asked which repos to scan, select your DVPWA repo. Then click **Next, Details**. You will then be brought to into the feed for your workspace.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FeVqRhFHA8FiW5a8Pt0In%2FScreenshot%202025-10-21%20at%203.01.26%E2%80%AFPM.png?alt=media&#x26;token=d8db7f4f-a19e-4c62-85dd-074ca263b324" alt=""><figcaption></figcaption></figure>

## Analyze initial findings and false positives&#x20;

In your feed, you'll see a summary of the scan results against the repository. Take note of the default filter being **Aikido refined** findings. Hover your cursor over the filter selection to view a funnel chart showing how Aikido has reduced false positives. Since this is a demo app with with deliberately highly exploitable vulnerabilities, most of them remain after triage. However, Aikido will commonly reduce false positive noise by upwards of 90% in your typical codebase.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FlJLERJb9jFEjUjiCnZ6k%2FScreenshot%202025-10-21%20at%205.20.04%E2%80%AFPM.png?alt=media&#x26;token=4b5543f1-31df-4112-858f-15bfc1503e63" alt=""><figcaption></figcaption></figure>

In the upper right corner, select the tile that reads **1 Auto Ignored**. That will take you to the **Ignored** section of your feed.

Note the issue name (`pyyaml`), type (Python package), severity (Critical) and reason for ignoring. Even though this is a critical vulnerability for a severely outdated package, Aikido suggests that the function is not used anywhere in the codebase (aside from being declared).&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FifJSOPEN2kGXr7OpwR6V%2FScreenshot%202025-10-21%20at%205.39.55%E2%80%AFPM.png?alt=media&#x26;token=5f6ca16f-8114-4576-b498-c2f52d7d9260" alt=""><figcaption></figcaption></figure>

Click into the issue to open a drawer showing more details. The declared version of the package, 3.13, is affected by two critical CVE's marked as subissues.&#x20;

While the the official fix is to upgrade to version 5.4, Aikido has marked the issue as safe to ignore. Click the **Affected function not in use** downgrade message beneath one of the subissues. This confirms Aikido has performed a [reachability analysis](https://help.aikido.dev/getting-started/reachability-analysis/reachability-engine-to-remove-false-positives) and determined the package is not used anywhere in the code.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FsYSL88xVaRWbMTV9zBmF%2FScreenshot%202025-10-21%20at%205.48.58%E2%80%AFPM.png?alt=media&#x26;token=a6a08a67-b09c-4eda-9381-92e6106d970e" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
Reachability is core to how Aikido assesses the relevance and impact of security issues. [Read more](https://help.aikido.dev/getting-started/reachability-analysis/reachability-engine-to-remove-false-positives) about Aikido's reachability engine.
{% endhint %}

Return to the issue details and click **View reachability analysis**. The flowchart shows that the affected version of **pyyaml,** while declared in requirements.txt, is not used anywhere in the code nor are any functions that depend on it.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FOAjiaLKgL3BWHJ0JbJRe%2FScreenshot%202025-10-21%20at%205.51.59%E2%80%AFPM.png?alt=media&#x26;token=65bdcadd-8098-417a-b622-dbecd789a021" alt="" width="375"><figcaption></figcaption></figure>

As a counter-example, return to the main Aikido refined issue feed. Click into the criticaly vulnerable `aiohttp` package. The issue details show a multitude of CVE's. For CVE-2024-23334, click **View reachability analysis**. Here we see that two different package depending on aiohttp are used by two different files in the codebase.&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fy7ny66C5wijaQwjHRB7Q%2FScreenshot%202025-10-21%20at%205.58.46%E2%80%AFPM.png?alt=media&#x26;token=403ad915-d4ba-4cdb-867e-377893ac0837" alt="" width="375"><figcaption></figcaption></figure>

Back in the issue details, click the **Upgraded** mesage for CVE-2024-23334. Aikido provides two reasons for the upgraded severity: (1) exploitation code exists on GitHub and is therefore highly discoverable, and (2) the vulnerability is actively being exploited in the real world.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FQUxPjtxMYblB3hOP79gn%2FScreenshot%202025-10-21%20at%206.30.21%E2%80%AFPM.png?alt=media&#x26;token=dd2b5fc9-8705-45ef-a74b-7ef3eaf27a16" alt=""><figcaption></figcaption></figure>

## Use AutoFix to resolve security issues

{% hint style="info" %}
Aikido AutoFix is an agent that leverages best-in-class LLMs to offer one-click fixes to security issues, either inline or via pull request. [Learn more](https://help.aikido.dev/aikido-autofix/overview-aikido-autofix) about AutoFix.
{% endhint %}

Still in the details drawer for the aiohttp issue, next to **How do I fix it?**, click **AutoFix**.  This will take you to the AutoFix page. Here Aikido will propose bumping the version of aiohttp in requirements.txt from 3.5.3 to  3.12.14.&#x20;

To apply the fix via a new pull request, open the kebab menu next to the status column and click **Create PR.** (Note: you may be prompted to grant Aikido write access to you repository. This is necessary for Aikido to open pull requests on your behalf).

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FdCKqGxXS6ish3lI41RVc%2FScreenshot%202025-10-21%20at%206.14.36%E2%80%AFPM.png?alt=media&#x26;token=277be4ef-023a-43af-bf59-e7d63d11aae5" alt=""><figcaption></figcaption></figure>

If prompted to apply a fix to either all packages or specific packages, select **all packages**. Aikido will open a dialog window as the PR creation processes. When it is finished, click **View PR**.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FiS1xw6SUw4a5Ws2t4AW9%2FScreenshot%202025-10-21%20at%206.17.54%E2%80%AFPM.png?alt=media&#x26;token=e949f7c9-126a-4d01-91ee-0d02371228ca" alt=""><figcaption></figcaption></figure>

You will then be taken to an open PR in your GitHub repository (your dvpwa fork). Aikido has filled out a detailed description as to the vulnerabilities resolved by the change. You can also click the **Files changed** tab to see the bumped package version in requirements.txt&#x20;

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnuLTXERE8TrUJrwfDSsr%2FScreenshot%202025-10-21%20at%206.22.20%E2%80%AFPM.png?alt=media&#x26;token=b7a50449-eaa4-4b2d-88d9-51e6f033907a" alt=""><figcaption></figcaption></figure>

At this point you can choose to either close the pull request or abandon in (if you'd like to preserve the vulnerability for future testing).&#x20;

You did it! In this tutorial, you:

* Connected a repository to Aikido and ran your first security scan
* Auto-triaged vulnerabilities based on their severity and exposure in the codebase
* Used AutoFix to propose and apply a fix to a vulnerable dependency
