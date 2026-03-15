# Source: https://help.aikido.dev/code-scanning/miscellaneous/support-for-multi-branch-scanning.md

# Support for Multi-Branch Scanning

**Table of contents:**

* [Use Cases](#use-cases)
* [Prerequisites](#prerequisites)
* [Adding multiple branches](#adding-multiple-branches)

## Support for Multi-Branch Scanning

Multi-branch scanning in Aikido allows developers to scan multiple legacy branches at the same time or is useful when you want to scan both your staging and production environment at the same time. You can add as many branches as you want. This is typically used when branches exist for months and continuous scanning is needed.

#### Use Cases <a href="#use-cases" id="use-cases"></a>

* You have old legacy branches that needs nightly scanning (eg branch V3, branch V4), that live in parallel, and you want to scan both as separate projects, even though they are in the same repository.
* You want to continuously monitor your staging and production environments

> In case you are looking to scan feature branches that get merged within a couple of days or weeks, we suggest looking into our [CI gating functionality](https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality).

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Multi-branch scanning needs to be enabled for your account. Contact us.

### Adding multiple branches <a href="#adding-multiple-branches" id="adding-multiple-branches"></a>

**Step 1:** Navigate to your repository's detail page and click on the current branch name (often tagged master). This action will open a modal window.

![NodeGoat GitHub repository showing the master branch and total issues count.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d95dd485a0330643686d366d4ae5f001f54a8acf%2Fsupport-for-multi-branch-scanning_fa3fe901-f8fd-44ea-8489-e354dcebf016.png?alt=media)

**Step 2:** Click 'Scan multiple branches.’\
​

![Branch selection dialog with options to scan single or multiple branches.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-bcacbfc33ce1fb3873a839086da290a0d17c2539%2Fsupport-for-multi-branch-scanning_f32721ac-7cc7-469a-af70-1a47866fcd5a.png?alt=media)

**Step 3:** Enter the name of the branch you wish to add to the scanning process.\
​

![Form to select and update branches for scanning in a repository.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-76875b9b7af20a9b92da77166fc5e36e67f7654e%2Fsupport-for-multi-branch-scanning_15130a0a-8e38-41fd-b271-ac0803c98b65.png?alt=media)

**Result:** Aikido clones the specified repo and scans the repository nightly, or you can trigger a scan manually for instant results. A label will appear next to the cloned repo so you know which repo contains which branch that is being scanned.

**Looking to scan more than 2 branches?** You can go into any of the repositories and go through this process again.

![Repository list with configuration options and a master copy label for one repo.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-44979bb0bf40b162883d69bbab47210f6494a3f6%2Fsupport-for-multi-branch-scanning_3b2e2e4c-407b-46e4-b4f7-96ba226eb282.png?alt=media)

> Note: It's important to note that secret scanning is conducted only on the initial repository. This is because the secret scanning feature is designed to automatically cover all branches by default.

***
