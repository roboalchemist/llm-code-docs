# Source: https://docs.lost-pixel.com/docs/recipes/lost-pixel-platform/automatic-baseline-updates-on-selected-branches.md

# Automatic baseline updates on selected branches

Sometimes your team uses Visual Regression Testing flow in a non-enforcement way, meaning that Lost Pixel checks don't need to pass for a PR to be qualified for a merge.

In this case, to speed up your review flow, you can set up the automatic approval of baselines in Lost Pixel Platform whenever PR is merged into a defined branch. In this case, the branch is defined as `main` but Lost Pixel Platform supports regex syntax, and you can easily use multiple branches here or even branches that follow some regex pattern, e.g.: `main|master|develop`\\

<figure><img src="https://354517992-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2tpFIKHmNw4YdppgU75t%2Fuploads%2Fgit-blob-c835b4681dc29793f312642e81f149bb57022389%2Fimage%20(5).png?alt=media" alt=""><figcaption><p>Lost Pixel Platform automatic baseline updates settings</p></figcaption></figure>

In this setup, whenever somebody merges a PR containing unapproved visual tests, they will be automatically approved on the main branch and will not appear in the next runs unless they have new changes.
