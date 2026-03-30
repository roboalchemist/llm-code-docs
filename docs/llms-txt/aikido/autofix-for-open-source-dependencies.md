# Source: https://help.aikido.dev/aikido-autofix/autofix-for-open-source-dependencies.md

# AutoFix for Open Source Dependencies

{% hint style="info" %}
Aikido Local Scan accounts DO NOT have access to AutoFix within the UI. If you want to use AutoFix locally, we suggest using our IDE plugins.
{% endhint %}

Aikido AutoFix creates pull requests that fix vulnerabilities in your open source dependencies by upgrading affected packages. Upgrades always target the minimum version needed to resolve the issue. Minor and patch bumps are preferred over major ones, keeping breaking changes to a minimum. AutoFix groups fixes per repo and lockfile, so each PR stays focused and mergeable. In some cases, a single upgrade removes an entire class of vulnerabilities rather than just one.

If a major version upgrade is proposed, no minor or patch version exists that resolves the vulnerability.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FkvZ2kWWdHhZqAxcIDpZ6%2Fimage.png?alt=media&#x26;token=92afb621-0847-47b8-b028-6008bf18a972" alt=""><figcaption></figcaption></figure>

### Autofix options <a href="#autofix-options" id="autofix-options"></a>

AutoFix can fix vulnerabilities in two ways:

* **Update Top-Level Dependencies** identifies and upgrades the top-level dependencies responsible for introducing the vulnerability. The package manager resolves the correct version of the vulnerable sub-dependency automatically. This is the default and recommended strategy, supported for JavaScript, .NET, Java, Kotlin, and Python.
* **Add Overrides for Dependencies** pins the vulnerable sub-dependency to a specific patched version. This is useful when the top-level dependency can't be upgraded yet, for example because a major version bump would be breaking.&#x20;

{% hint style="info" %}
There is actually a third option, by using hardened libraries. [More info here](https://help.aikido.dev/aikido-autofix/autofix-for-open-source-deps-extended-lifecycle-support).
{% endhint %}

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FAlAc7vrQtSGVqes3iCuo%2Fimage.png?alt=media&#x26;token=c6cd63d1-688e-4cf7-8923-c95115f4b53a" alt=""><figcaption></figcaption></figure>

When using **Add Overrides for Dependencies** to fix multiple vulnerabilities at once, the **All available fixes** dropdown lets you control which packages are included:

1. **All available fixes** — fixes everything, including major version bumps
2. **Minor and patch versions only** — skips any fix that requires a major version bump
3. **Critical issues only** — only fixes issues with a Critical Aikido priority

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FDznGTYoHctRdf0UPNNcO%2Fimage.png?alt=media&#x26;token=c1aae813-59a9-4a6a-ad95-170e2bcfb0cc" alt=""><figcaption></figcaption></figure>

After you will be shown with a progress window (bottom right) on the state of the PR creation. You will receive an update once the PR is ready.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5451889ccc0b6ad69f33c58288949262f6a77938%2Fautofix-for-open-source-dependencies_16361918-0a43-4db3-b7ff-f250361d5fae.png?alt=media)

### Example video of setting up AutoFix and creating your first PR <a href="#example-of-setting-up-autofix-and-creating-your-first-pr" id="example-of-setting-up-autofix-and-creating-your-first-pr"></a>

[Video](https://ucarecdn.com/4d1a26c8-3ccf-4762-818c-e3430058f9a9/)
