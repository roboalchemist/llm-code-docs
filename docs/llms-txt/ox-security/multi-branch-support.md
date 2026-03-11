# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/multi-branch-support.md

# Scanning Multiple Branches

You can streamline your security management across multiple branches ensuring comprehensive visibility into potential vulnerabilities with multi-branch scanning that allows scanning multiple branches within a repository.

This capability enables you to go beyond scanning just the default branch and extend your security coverage to branches representing specific versions of your software, OR various development stages, such as:

* specific versions of your software, OR
* various development stages, such as: development, staging, production.

## Working in the Multi-Branch mode

With multi-branch support, every branch is treated as a separate application in the OX platform, allowing you to track and resolve issues independently for each branch.

The branches that you select are scanned in addition to the default branch, which is scanned alongside the multi-branch selection.

Enabling the capability can change how the system operates, and it may affect existing data or issue handling. You can expect potential delays or changes in the data and issue resolution process, as the scan process becomes more complex.

You can define which branches to scan in the following ways:

* [for all repos](#securing-branches-in-all-repos)
* [for an individual repo](#securing-branches-of-an-individual-repo)

## Enabling the capability and securing branches in all repos

Initially the capability is disabled and only the branch that defined as default is scanned.

> **Note:** **To enable the Multi-Branch capability, contact OX Security Technical Support at <support@ox.security>, or contact your regional customer success manager.**

**To define branches for scanning:**

1. Go to **Settings** > **Applications** and scroll down to the **Branch Scanning** section.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-519aeae140727133b72a2d6bc20f0a9618b47c48%2Fenable%20multi-branch.png?alt=media" alt="" width="352"><figcaption></figcaption></figure>

1. Enable **Multi-branch scan**.
2. To set specific branch names for scanning in all repos, add branch name(s) in the **Branches for scanning** box.

> **Note:** If you request a branch that does not exist, the system creates an irrelevant application for this branch. For example you request to scan the branch named `version-1-3-front-end`. OX platform searches all the repos for this branch name and creates irrelevant apps each time it was not found.

1. Select **UPDATE**.

## Securing branches of an individual repo

When Multiple-branch scan is [enabled](#enabling-the-capability-and-securing-branches-in-all-repos), you can specify which branches to scan in each repo. You can scan up to 4 branches in each repo, the default branch and 3 other branches that you select.

When multiple branches are selected for scanning from a specific repo, OX designates one branch as the primary application. It’s marked with a unique icon and you can filter the Applications table using the Primary Application tag.

The primary application performs several roles, including receiving issues from third-party integrations, artifact scanners, Git posture, and cloud checks and so on.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-37dd826e16ae1c2a36faca355f06610e5d97e1dd%2FApps_primary_branch.png?alt=media" alt="" width="563"><figcaption><p>Primary Application</p></figcaption></figure>

**To set branches for scanning in a specific repo:**

1. In the **Connectors** page, select the source control system that you use to integrate with the OX platform.
2. In the **Configure \[source control name] Credentials** dialog, select the gear icon next to **DELETE** .

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07f73b8b0e9278c5539a519850d40be46afae27e%2Fgear_icon%20(1).png?alt=media" alt="" width="321"><figcaption></figcaption></figure>

1. In the **Configure your** \[**source control name] Connector** dialog, select the repos that you want to scan.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1c5aef154f13badd37b9095f85209c5c49a34272%2Fselecting%20repos_no_title.png?alt=media" alt="" width="266"><figcaption></figcaption></figure>

1. To specify which branches to scan in selected repo, click the gear icon next to the repo and select up to 4 branches, including the default one, in the **Select Branches to Scan** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-642eca5a87e1b1140de406bd9aa31af5c7b9a470%2Fselect%20branches.png?alt=media" alt="" width="360"><figcaption></figcaption></figure>

1. Click **SELECT**. The in the **Select Branches to Scan** dialog closes.

> **Note:** Selecting specific branches for scanning overrides the global branch-scanning settings.

1. In the **Configure your** \[**source control name] Connector** dialog, select **SAVE**.
