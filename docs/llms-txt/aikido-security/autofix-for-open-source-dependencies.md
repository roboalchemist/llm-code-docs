# Source: https://help.aikido.dev/aikido-autofix/autofix-for-open-source-dependencies.md

# AutoFix for Open Source Dependencies

> Aikido Local Scan accounts DO NOT have access to AutoFix within the UI. In the future, it will be available within our IDE plugins.

Aikido Autofix is a tool you can use to **automatically fix vulnerabilities in open source dependencies** in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue..

### Autofix Overview Page <a href="#autofix-overview-page" id="autofix-overview-page"></a>

Aikido allows you to easily create PRs for multiple version upgrades and fixes at the same time. By grouping per repo and lockfile, we ensure that PRs never get to large and are able to be merged without breaking certain parts of the app.

**Important.** By default, Aikido will always give you the minimum version required to do the fix, never a higher one. This means we prioritise minor version bumps always over the major ones, ensuring there are not too many breaking changes on your side. If a major upgrade is proposed, it is because a minor version upgrade would not fix the issue at hand.

![Dependency vulnerability dashboard showing severity, CVEs, version upgrades, and update statuses.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-257aba122ae5497e21440e6759611f140460b13f%2Fautofix-for-open-source-dependencies_6b1cd879-9709-4df0-8f9f-23855e0f9d38.png?alt=media)

### Autofix options <a href="#autofix-options" id="autofix-options"></a>

When creating an autofix, multiple options will be presented to you.

* **Upgrade all packages**: upgrades all packages and will contain major, minor and patch upgrades.
* **Minor and Patch Versions Only:** upgrades minor and patch versions only
* **Critical Issues only:** these are the critical issues as defined by Aikido. These can contain major, minor and patch upgrades.

![Options for creating an AutoFix PR to upgrade Python packages in cdk-goat.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d47e9205db2acc2609c65aca1a93fd095cc12ab1%2Fautofix-for-open-source-dependencies_3c94580b-c7a2-48cd-a31c-c45b72dcea99.png?alt=media)

After you will be shown with a progress window (bottom right) on the state of the PR creation. You will receive an update once the PR is ready.

![Aikido initiates an AutoFix pull request to apply code patches.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5451889ccc0b6ad69f33c58288949262f6a77938%2Fautofix-for-open-source-dependencies_16361918-0a43-4db3-b7ff-f250361d5fae.png?alt=media)

### Example of setting up autofix and creating your first PR <a href="#example-of-setting-up-autofix-and-creating-your-first-pr" id="example-of-setting-up-autofix-and-creating-your-first-pr"></a>

[Video](https://ucarecdn.com/4d1a26c8-3ccf-4762-818c-e3430058f9a9/)
