# Source: https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/ci-scan-history-overview.md

# CI Scan History Overview

The CI Scan History feature in Aikido provides a detailed overview of all past CI scans, offering insights into their status, newly introduced issues, and resolved issues. This is important to keep an overview of all executed scans and allow you to quickly check the diff page from previous executed scans.

### How to check your CI Scan History <a href="#how-to-check-your-ci-scan-history" id="how-to-check-your-ci-scan-history"></a>

**Step 1.** Go to the CI section on the [Integrations page](https://app.aikido.dev/settings/integrations) and enter the [GitHub](https://app.aikido.dev/settings/integrations/github/checks)/[Azure](https://app.aikido.dev/settings/integrations/azure-devops/checks) CI dashboard **OR** - if you are running your CI via code - go to the [CI Settings Page](https://app.aikido.dev/settings/integrations/continuous-integration).

**Step 2.** Click on "CI Scan History" located at the top right of the page.

![GitHub CI dashboard showing repository count and a button for CI scan history.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e10971ac2e09a467643a6bb131a46b040a0198cd%2Fci-scan-history-overview_65a20f5b-7a38-455b-b76c-6b4b34b37c04.png?alt=media)

**Step 3.** Review the overview page to see all previous CI scans, including their status, newly introduced issues, and resolved issues.

![CI scan history table showing pull requests, issue counts, scan dates, and gate statuses.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-77f761884223d1dc28db03dea2bdded5795ca7f8%2Fci-scan-history-overview_8753a53f-765d-4154-a02d-67cdd9eaaa12.png?alt=media)

**Step 4.** Click one of the PRs to get a full overview of the executed scan.

![CI check failed: 2 secrets exposed, 1 vulnerability solved in code review.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cc1fd8be1d60a625611c8aff62ecad705e3888b3%2Fci-scan-history-overview_85f48f63-1982-45f4-90ce-d74c5b1d88d1.png?alt=media)
