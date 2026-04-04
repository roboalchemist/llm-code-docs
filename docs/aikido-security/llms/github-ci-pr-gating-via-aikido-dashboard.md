# Source: https://help.aikido.dev/pr-and-release-gating/github-ci-pr-gating-via-aikido-dashboard.md

# GitHub PR Gating

You can easily configure GitHub PR Gating via the Aikido interface. This functionality allows you to block any **newly introduced** issues for a certain threshold that you decide. These checks run **everytime** changes are committed to the feature branch. This doc focusses on managing configurations in bulk - multiple repos at the same time - without code.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* **Bulk Repository Management**: Easily specify and manage configurations for multiple repositories at once through the Aikido interface.
* **Zero Code Integration**: Install the Aikido app on GitHub to manage checks without embedding any code, simplifying the setup process.
* **Cost Efficiency**: By managing GitHub Checks through Aikido, avoid using CI minutes on GitHub, leading to significant cost savings.

### Setting up GitHub CI <a href="#setting-up-github-ci" id="setting-up-github-ci"></a>

**Step 1.** Go to the [Integrations Page](https://app.aikido.dev/settings/integrations) and select GitHub in the CI gating section.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-be8f80aeb267d3030e72859823843eeef0fdf705%2Fgithub-ci-pr-gating-via-aikido-dashboard_43344e10-d830-4b16-9304-117e86c3a68e.png?alt=media" alt="Connect CI tools (GitHub, GitLab, Bitbucket, Azure) to block risky code merges." width="563"></div>

**Step 2 (optional).** Select **PR Gating Configuration Via Aikido Dashboard** in the modal that pops up. This will open up a new tab with GitHub to install the PR Checks App. **Note: this modal will only popup if you have already used GitHub Actions via code**.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e8e201d187852023ad274e36275b1848e77f2d79%2Fgithub-ci-pr-gating-via-aikido-dashboard_6dd239df-679e-47db-8da9-a2c507f22f1d.png?alt=media" alt="Select a PR gating method for GitHub: Aikido dashboard or GitHub Actions in code." width="563"></div>

**Step 3.** Install the **Aikido PR Checks app** in GitHub. Make sure that you select the GitHub organisation that is currently being used in your workspace. Choose which repos that Aikido is allowed to access. We recommend giving access to all repos so these can easily be managed from within Aikido.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7fedf034fba188ee993c9b04e84877b5ce086741%2Fgithub-ci-pr-gating-via-aikido-dashboard_b27aae05-4bb2-427a-86e3-358be281878b.png?alt=media" alt="Aikido PR Checks installation prompt with logo and installation location query." width="563"></div>

**Step 4.** Aikido redirects you to the [GitHub CI page](https://app.aikido.dev/settings/integrations/github/checks) with an overview of your repos. You can start configuring your repos. We recommend starting out with 1 repo to make sure everything works well.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FEGHgp6CLLoG40moYYE6c%2Fimage.png?alt=media&#x26;token=e4b10877-ad71-4972-ac25-331699181759" alt=""><figcaption></figcaption></figure></div>

**Step 5. Select repos in bulk** and click **Setup PR Scans** in the floating bar on the bottom

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fs5sswQWGpuJ2B29v0mX6%2Fimage.png?alt=media&#x26;token=be1d4f9b-5e8f-4c61-ad28-a95b4034bab6" alt=""><figcaption></figcaption></figure></div>

**Step 6**.This will trigger the modal to choose the severity level for failure and the scans you want to execute.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fd25eef886fd1d3a642fb33d22180411a0e89f63%2Fgithub-ci-pr-gating-via-aikido-dashboard_9bb2cc56-30d6-4da2-ace7-b89603d2bce8.png?alt=media" alt="Security scanning configuration settings for the &#x22;about-github&#x22; repository." width="563"></div>

{% hint style="info" %}
If you've added new repositories after the initial setup, you'll need to configure those repos as well.

To apply a default configuration automatically, see [Default PR/MR gating configuration for new repositories](https://help.aikido.dev/pr-and-release-gating/aikido-ci-gating-functionality/default-pr-mr-gating-configuration-for-new-repositories).
{% endhint %}

### Ignore issues directly from PR comments <a href="#ignore-issues-directly-from-pr-comments" id="ignore-issues-directly-from-pr-comments"></a>

When Aikido posts an inline PR comment for a finding, you can ignore that issue directly from GitHub by replying to the comment with:

`@AikidoSec ignore: [your reason to ignore]`

Example:

`@AikidoSec ignore: This secret is used for tests only.`

This performs the same action as manually ignoring the issue in the Aikido platform:

* The issue is marked as ignored in Aikido.
* The ignore reason is stored.
* PR gating can turn green once all blocking issues are resolved or ignored.

### Make failed PR checks block merges <a href="#make-failed-pr-checks-block-merges" id="make-failed-pr-checks-block-merges"></a>

Aikido can fail the PR check, but GitHub decides whether that failing check blocks a merge. Configure branch protection with required status checks:

* [GitHub Docs: About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging)
* [GitHub Docs: Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)

### Adding Exceptions for specific repos <a href="#adding-exceptions-for-specific-repos" id="adding-exceptions-for-specific-repos"></a>

You might want to have 1 specific repo where the configuration slightly differs. You can easily add exceptions by clicking the triple dots on a repo item or just select 1 or more items and go through the **Configure Scans** process again.

<div data-with-frame="true"><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d6534acd8fb274a990826d4ee2cb4ab40d51e887%2Fgithub-ci-pr-gating-via-aikido-dashboard_86da3769-0a5e-4012-ad5e-c1b6e53233f7.png?alt=media" alt="Critical vulnerability status dashboard with configuration management options for projects."></div>
