# Source: https://docs.augmentcode.com/codereview/admin-guide.md

# Augment Code Review

> Use Augment Code Review to automatically review PRs faster while catching more critical bugs.

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

## About Augment Code Review

Augment Code Review helps professional software teams complete code-reviews faster inside GitHub while also catching more critical bugs before they hit production. Backed by Augment's industry-leading Context Engine, the agent understands your codebase at a deep level, providing reviews that are more meaningful and account for codebase-wide effects. Augment prioritizes high signal-to-noise ratio by focusing on high-impact issues like bugs, security concerns, correctness, and cross-system problems while avoiding low-value style nags.

<Note>
  Augment Code Review relies on the Augment GitHub App which is only compatible with GitHub Enterprise Cloud and github.com. GitHub Enterprise Server is not currently supported.
</Note>

## Getting Started

Visit [app.augmentcode.com/settings/code-review](https://app.augmentcode.com/settings/code-review) and log in. Augment Code Review is only available as an add-on to [Enterprise plan](https://augmentcode.com/pricing) customers. Settings are accessible to all members of the Enterprise plan, but only configurable for Administrators of the Enterprise plan. If you aren't sure if you are an Administrator, please contact your solutions team.

### Configure Repo Access inside of the Augment GitHub App

Before you can configure repositories, click on "Install" to install the Augment GitHub App. This will redirect you to GitHub to provide permissions for all the repos you grant Augment Code Review to engage.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=fc3c7ac1bde5635d1cfef9cd96a88529" alt="Code Review Settings install button" className="rounded-xl" data-og-width="1307" width="1307" data-og-height="672" height="672" data-path="images/code-review-settings-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=31d46773f0cb7183c9ce124d29f560a7 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=bc0122ce8f4db9239dd4b3852a9c24e7 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=402c05c90721f936a6eb7799a09dc0f5 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=cb2b4114383e36a3857effe12f8eec58 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=1e8419133d036a6b6a05fb41d1a141da 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-install.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=d8af4c4cb27c4d36a0b437f62f345e2c 2500w" />

If your firewall configuration, allowlist or network policy requires a static IP for this integration, please refer to our [static IP address](https://docs.augmentcode.com/setup-augment/static-ip-support#allow-augment-traffic-from-static-ips) documentation.

<AccordionGroup>
  <Accordion title="Who can install the Augment GitHub App?">
    To install the Augment GitHub App, you will need to be an Administrator of your GitHub organization. To find who the Administrators are, visit your GitHub organization settings page and click on "People." Administrators are listed under "Owners."

    <img src="https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=0f6779df0d8a446bacbb4df0575c7cd0" alt="GitHub Admins" className="rounded-xl" data-og-width="2010" width="2010" data-og-height="1284" height="1284" data-path="images/code-review-owners.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=280&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=2654775b944c43922376d86b98e22175 280w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=560&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=63d0c59812fb1d4f0e747d67e65efa46 560w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=840&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=ae3ce426fada48f9464c54981e1a93e7 840w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=1100&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=cc6ca0802f7d540c107b4e414b8f96a3 1100w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=1650&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=96124ffa1c0c7689a4b2b485189ac871 1650w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=2500&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=1f74e1e9fb88262a6a1399af1db2e06c 2500w" />
  </Accordion>
</AccordionGroup>

Once you finish installing the GitHub app, you should see a green checkmark with the text "All set!". Then, back in the Augment Code Review Settings, the "Install" button should now show a green "Installed" badge. If you do not see either of these, you may need to uninstall the app through GitHub and reinstall it. See [Troubleshooting](/codereview/admin-guide#stuck-on-install-button) for more help.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=f4a0990fb97f3348aa6479f7227ea882" alt="GitHub App Installed" className="rounded-xl" data-og-width="813" width="813" data-og-height="627" height="627" data-path="images/code-review-github-integration-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=099cafaf756d8b53438815d57695a266 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=67f73fe4016247bb8f4c331cf77a1b81 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=83b3050a8120ec5ed27f63bc48dd311f 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=873defdc8762e23920704f7c618ee1e6 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=c296b2b5bbfae6af4caf0e8f6c71323b 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=7cccceea467427c5b923c4730f406b4e 2500w" />

### Permissions requested by the Augment GitHub App:

* Contents, read-only: Clone repositories

* Pull Requests, read and write: Read pull requests and post comments to pull requests

* Issues, read-only: Read top-level PRs / Issues

* Organization Members, read-only: Read members of an organization, to distinguish internal and external users and their access levels to Augment features

Organization owners and repository admins can install the app directly; others will need owner approval. See [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for details. If your organization uses [Augment for Slack,](https://docs.augmentcode.com/setup-augment/install-slack-app) the same selections will apply to both Augment for Slack and Augment Code Review.

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5e4084c99c0295b0f64244970b63b7c1" alt="Installing the GitHub app on a single repository" data-og-width="1372" width="1372" data-og-height="1387" height="1387" data-path="images/install-github-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=74db4d5e2ebb869baec7fa8a5542fe1e 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=124a9fff587698addbf6521b889b5c28 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3141ed13276ff2da9a123ad94d1d98b9 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa841e9121554b8c1a75c35097e0d84b 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7abe3b886150b097a11ae90b41cae3f1 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=333c129e393ab4b32f04c3940492cf1c 2500w" />

You can modify repository access anytime in the Augment GitHub App settings.

### Configuring Triggers Per Repository

As the Administrator, you control when Augment Code Review triggers via [Settings](https://app.augmentcode.com/settings/code-review):

* **Automatic**: Augment Code Review will automatically review and post a comment as soon as the PR is opened for review in GitHub. Use it when your teams want immediate feedback on all pull requests.

* **Manual Command**: Augment Code Review is only triggered when someone comments on the PR with any of the following:  `auggie review`, `augment review`, or `augmentcode review` on GitHub. Use it when you want full control over when a review happens.

* **Disabled**: Augment Code Review will not run on the repository.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=96c0f0dfc2186287a71bba713f7c31a6" alt="Trigger Types" className="rounded-xl" data-og-width="685" width="685" data-og-height="403" height="403" data-path="images/code-review-settings-triggers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=ec552a7eb0b39e85a412d191bf3c9c19 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=1cf11f2ee10f617961a22c17f36a6366 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=61f0470d5754359fa3a4375cc3112b46 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=b2199c1921299daf014149220d31c120 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=fc80b5456761c3cf534b3db831fb52af 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=83c4d15d7a40b8253a01803de97354b8 2500w" />

If the repo is set to "Automatic" or "Manual Command", to run additional rounds of reviews on a subsequent commit of any PR, you can use the same manual trigger keywords (`auggie review`, `augment review`, or `augmentcode review`).

On public repositories, reviews are only triggered for PRs whose authors are members of the GitHub organization, outside collaborators to the organization or repository, or contributors to that repository.

## Change the GitHub Organization using Augment Code Review

Today, Code Review is limited to one GitHub organization per Enterprise account. Augment will address this limitation in an upcoming release. You can change the organization by reinstalling the Augment GitHub App.

* To get started you need to review the GitHub Apps installed on an organization:
  * In the top right corner of GitHub, click your profile picture, then click Your organizations.
  * Next to your organization name, click Settings.
  * In the side bar, under "Third-party Access," click GitHub Apps. A list of the GitHub Apps installed on your organization will be displayed.
  * Next to the GitHub App you want to review or modify, click Configure.
* To uninstall the Augment GitHub App, click Uninstall.
* To reinstall, visit: [https://github.com/apps/augmentcode/installations/new](https://github.com/apps/augmentcode/installations/new). Select your organization.

## Providing feedback

You can provide in product feedback directly in GitHub by reacting with a thumbs up or thumbs down emoji to the inline comment left by Augment Code Review.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=4b5230f9a1ea82235d8275689aec130f" alt="Code Review Feedback using GitHub Reactions" className="rounded-xl place-self-center" data-og-width="524" width="524" data-og-height="163" height="163" data-path="images/code-review-github-feedback.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=462ec74def0372cb32ecc0d952a67878 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=8073845e10e05f4099306c21b441628f 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=27dbf7cfebe0d0d5745741af62cf8c58 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=bf7c7d0b8fe09bc130c976ae43b3ba88 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=5c24ee5cbd38d0b1a8143bc6acf0479c 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-feedback.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=dd387ce425da7df2d6a42667b683e03e 2500w" />

## Tell Augment Code Review to check specific areas with guidelines

Domain knowledge that isn't always evident in the code. Tell Augment Code Review to check specific areas like security vulnerabilities or inside particular directories when relevant. Augment Code Review allows you to outline these special guidelines per repository. Describe any areas of focus using a yaml file entitled code\_review\_guidelines.yaml inside the .augment folder at the repository root:

`<repo-root>/.augment/code_review_guidelines.yaml`

Scope guidelines to the appropriate sub-directories and focus on objective issues that can cause bugs, expose vulnerabilities, etc. and less on stylistic or subjective things.

### Example Augment Code Review Guidelines

```yaml  theme={null}
# Guidelines exclusive to augmentcode/auggie

areas:
  databases:
    description: "Data and Database related rules"
    globs:
      - "**"
    rules:
      - id: "no_pii_in_bigquery"
        description: "Never store PII data in BigQuery tables."
        severity: "high"
      - id: "no_guid_keys"
        description: "GUID foreign keys can slow lookups"
        severity: "medium"

  memory_safety:
    description: "Ensure Memory Safety"
    globs:
      - "kernel/**"
    rules:
      - id: "avoid_unsafe_rust"
        description: "Avoid unsafe Rust operations."
        severity: "high"
```

### Explanation of the Guideline Format

**Areas:** Focus domain. Example: focus is “databases”

**Area Name**: Double quoted string written in snake case (ex: memory\_safety)

* **Description:** Double quoted message summarizing intent of the area
* **Globs** (short for global): Double quoted pattern-matching notation. Used to specify sets of filenames or paths using wildcard characters

<Note>
  Common **globs** or pattern matching syntax:

  * `**` - Matches any number of directories (recursive wildcard)
    * Example: `**/test.py` matches `test.py`, `src/test.py`, `src/utils/test.py`, etc.
  * `*` - Matches any sequence of characters within a single directory level
    * Example: `*.py` matches `file.py`, `main.py` but not `src/main.py`
  * `?` - Matches exactly one character
    * Example: `test?.py` matches `test1.py`, `testA.py` but not `test10.py`
</Note>

* **Rules:** Areas can contain more than one rule. Each rule contains:
  * **ID**: Double quoted title written in snake case (ex: avoid\_unsafe\_rust)
  * **Description**: Double quoted message summarizing intent of the rule
  * **Severity**: Expects double quoted “high”, “medium” or “low”. Sets the priority of review by Augment Code Review

## User Access

Administrators can specify a list of GitHub users who can trigger Augment Code Review by turning on **Allowlist Mode**.

When Allowlist Mode is active, only users in the allowlist will be able to trigger Augment Code Review. Automatic and manual reviews will be disabled for all other users. This is useful for organizations that want to limit access to the feature to a select group of users.

To manage permissions, visit [User Access for Code Review](https://app.augmentcode.com/settings/code-review/user-access).

## Model Context Protocol (MCP)

Administrators can connect Augment Code Review to external context sources through Model Context Protocol (MCP). Augment Code Review supports both local and remote MCP servers.

* Remote MCP servers run remotely and are hosted by providers. Once you add a remote MCP server, you may need to complete an OAuth flow to sign in to the server before it can be used by the code review agent.
* Local MCP servers run in their own environment within the code review agent's workspace. You can specify environment variables for local servers by clicking + MCP and then clicking + Environment Variable. Once set,
  environment variables are write-only and can only be overwritten or removed (not viewed) after the server has been added.

To configure MCP servers, visit [MCP for Code Review](https://app.augmentcode.com/settings/code-review/mcp).

## Code Review Analytics

Use the Code Review Analytics dashboard to track the review load automated by Augment, along with the comments made by Code Review that developers ultimately addressed.

1. **Navigate to Code Review** - In your browser, visit [Code Review Analytics](https://app.augmentcode.com/code-review/analytics).
2. **Filter by Date** - Refine your Analytics using the tabs for Last 7 Days, Last 30 Days, or Last 60 Days.

### Metric Definitions

* **Total PRs Reviewed**: The number of PRs that have been reviewed by Augment Code Review.
* **Total Reviews Performed**: The number of reviews that have been run by Augment Code Review. One PR can have multiple reviews if people manually trigger more reviews.
* **Total Comments**: The total number of inline comments left by Augment Code Review.
* **Percentage of Comments Addressed**: A comment is addressed if the developer resolved the concerns raised by the Augment Code Review comment. The percentage is calculated by dividing the number of addressed comments by the total number of comments left by Augment Code Review.
* **Percentage of Thumbs Up Reactions**: A thumbs up reaction is counted if a user reacts with the Thumbs Up emoji on GitHub on an inline comment left by Augment Code Review. The percentage is calculated by dividing the number of thumbs up reactions by the total number of thumbs up and thumbs down emoji reactions.
* **Estimated Dev Hours Saved**: Number of PRs multiplied by 10 minutes

### Reading the Charts

* **Addressed Comments**: A chart detailing total number of comments per day broken down by unaddressed (gray) vs addressed (green). You can interpret the green bar to mean Augment Code Review caught issues that developers fixed and may not have without the comment.
* **Reviewed PRs**: A chart detailing the total number of reviewed PRs per day (blue).

## Troubleshooting

### Stuck on Install button

If you still see the “Install” button on the Augment Code Review Settings page, then the Augment GitHub App installation failed. You will need to uninstall the Augment GitHub App from your organization and then reinstall it. Make sure the person installing the GitHub app has an Augment account and they see the "All set!" text after installing the app.

<Steps>
  <Step title="Navigate to the Augment GitHub App settings page on GitHub">
    Follow the steps on [GitHub Docs](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify) to modify the Augment GitHub App installation.
  </Step>

  <Step title="Uninstall the Augment GitHub App from your organization">
    In the Danger zone section, click on "Uninstall"
  </Step>

  <Step title="Reinstall the Augment GitHub App">
    Follow the steps in [Getting Started](/codereview/admin-guide#getting-started) again to install the app
  </Step>
</Steps>
