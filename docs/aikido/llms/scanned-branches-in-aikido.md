# Source: https://help.aikido.dev/code-scanning/miscellaneous/scanned-branches-in-aikido.md

# Scanned Branches in Aikido

### Single-Branch Scanning <a href="#single-branch-scanning" id="single-branch-scanning"></a>

By default, Aikido will scan the default branch in your repository for dependency and code issues. The default branch is usually main/master. **Aikido runs a full scan of all repos, clouds, containers and domains every night**.

If you update the default branch, Aikido will pick up this change during its nightly sync, so no changes are needed on Aikido's end.

In some cases, it might be interesting to scan another branch instead of the default branch. This could be the case if you are developing on another branch for an extended period of time. You can overwrite the branch being scanned on the repository detail page in Aikido by clicking the branch button at the top.

![GitHub admin-panel repository showing master branch and issue status.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d75548d237b04712da7bccdbefc12a6422ffe451%2Fscanned-branches-in-aikido_769bdbd4-5ab6-4248-a382-b6e56af0438e.png?alt=media)

A modal will appear that will allow you to change the branch being scanned every night.

![Dialog box to update and save the branch name for scanning.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-65a7b7ba025161bf76684dbdf15e285d78451311%2Fscanned-branches-in-aikido_b460fe90-cd2f-41b8-bb40-b54fb7f7aaa1.png?alt=media)

## Multi-Branch Scanning <a href="#multi-branch-scanning" id="multi-branch-scanning"></a>

If you are looking to scan multiple branches of the same repo on a regular basis, you can contact us to enable Multi-Branch Scanning for you. This is only available for Paid Plans. Please check whether multi-branch scanning is right for you [by checking the use cases in this article](https://help.aikido.dev/code-scanning/miscellaneous/support-for-multi-branch-scanning).
