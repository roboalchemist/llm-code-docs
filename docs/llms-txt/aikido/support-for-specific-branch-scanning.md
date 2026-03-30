# Source: https://help.aikido.dev/code-scanning/miscellaneous/support-for-specific-branch-scanning.md

# Support for Specific Branch Scanning

### Introduction <a href="#introduction" id="introduction"></a>

Utilize Aikido's manual scanning feature to directly compare a branch with your current project state/main branch, ideal for situations where you have not integrated your CI with Aikido yet.

This functionality allows you compare a specific branch / pull request / tag with the current state in Aikido, highlighting the changes with the main branch. Scanning takes typically **1-2mins** so no need to leave the UI.

**Note.** In case you have old legacy branches that needs nightly scanning (eg branch V3, branch V4), check out our [Multi-Branch Scanning Feature](https://help.aikido.dev/en/articles/8979512-how-to-set-up-multi-branch-scanning).

### How to scan a specific branch <a href="#how-to-scan-a-specific-branch" id="how-to-scan-a-specific-branch"></a>

**Step 1**: Navigate to a specific repository detail page within Aikido

**Step 2**: Click on the Scan Branch button.\
​

![Repository dashboard showing critical security issues and scan options for the "terragoat" project.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d63121714879f7ecb114f0d4fa0329e74dd3539d%2Fsupport-for-specific-branch-scanning_ca647507-fde6-4251-b500-75c661626bff.png?alt=media)

**Step 3:** In the prompted field, enter the **name of the branch or tag** you wish to scan. Make sure to type the exact name of the branch / tag to avoid any errors. You can select which types of scans to execute.

![Initiate a security scan for a specified code branch with scan type options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-99b75f70fea472a175e285d470f76803b3aa828c%2Fsupport-for-specific-branch-scanning_0e7d4328-0929-42f6-ade1-92a9343d9cc0.png?alt=media)

**Step 4.** In the bottom right corner, you will be able to follow the progress of the scanning. Once the scanning is done, click 'View Diffs'\
​

![Scan completed notification with "View Diffs" button displayed for a demo application.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-87c142bfd9aaa1a3816fe0082751b10a6eaaeeee%2Fsupport-for-specific-branch-scanning_48a505a7-62a0-46fb-8a65-2f09bf3bbca8.png?alt=media)

**Step 5.** Check which new issues are introduced and resolved on the comparison page.\
​

![Branch security scan summary showing newly introduced critical and high severity vulnerabilities.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2651e8681165c657f6f2de87508d5b9d4546e9c6%2Fsupport-for-specific-branch-scanning_6c609701-289b-423a-92d7-49f4b8756e16.png?alt=media)

By following these steps, you can effectively conduct a manual scan of your branch/tag in Aikido, which will allow you to review changes, identify new or resolved issues, and make informed decisions about integrating the branch into your main codebase.

***
