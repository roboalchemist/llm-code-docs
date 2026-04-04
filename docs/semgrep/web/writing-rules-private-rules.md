# Private rules

Source: https://semgrep.dev/docs/writing-rules/private-rules

- [](/docs/)- [Write rules](/docs/writing-rules/overview)- Write rules for Semgrep Code- Private rules**On this page- [Rule writing](/docs/tags/rule-writing)Private rules
Users with Semgrep Code&#x27;s [Team or Enterprise tier](https://semgrep.dev/pricing) can publish rules to the [Semgrep Registry](https://semgrep.dev/explore) as private rules that are not visible to those outside their organization. Maintaining the rules&#x27; privacy allows you the benefits of using the Semgrep Registry while keeping sensitive code or information internal.

## Creating private rules[​](#creating-private-rules)
You can create private rules the same way you create other custom rules. The subsequent sections can help you create and save your private rules.

### Create private rules through Semgrep AppSec Platform[​](#create-private-rules-through-semgrep-appsec-platform)
To create and publish private rules through the Semgrep AppSec Platform:

- Go to [Semgrep Editor](https://semgrep.dev/orgs/-/editor).
- Click ** **Create New Rule**.
- Choose one of the following options to create your rule:

Click the ** **plus** icon, select **New rule**, provide the YAML file for your rule, and then click ** **Save**.
- In the ** **Library** panel, select a rule from a category in **Semgrep Registry**. Click ** **Fork**, modify the rule or test code, and then click ** **Save**.

- Click ** **Share**.
- Click ** **Private**.

Your private rule has been created and added to the Registry. It is visible only to logged in users of your organization, and its private status is reflected by the **Share** button displaying a ** icon.

Private rules are stored in the folder with the same name as your Semgrep AppSec Platform organization.

### Create private rules through the Semgrep command-line interface[​](#create-private-rules-through-the-semgrep-command-line-interface)
To create private rules through the [Semgrep CLI](/docs/getting-started/quickstart), :

- Log in to Semgrep. Running this command launches a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed:

`semgrep login`

- 
In the **Semgrep CLI login**, click **Activate** to proceed.

- 
Create your rule. For more information, see [Contributing rules](/docs/contributing/contributing-to-semgrep-rules-repository).

- 
Publish your rule from the command line using `semgrep publish` command followed by the path to your private rules:

`semgrep publish myrules/`
If the rules are in the directory you publish from, you can use `semgrep publish .` to refer to the current directory. You must provide the directory specification.

If the directory contains test cases for the rules, Semgrep uploads them as well (see [testing Semgrep rules](/docs/writing-rules/testing-rules)).

You can change the visibility of the rules. For instance, to publish the rules as unlisted (which does not require authentication but results in the rules hidden from users of the public registry):

`semgrep publish --visibility=unlisted myrules/`
For more details, run `semgrep publish --help`.

## View and use private rules[​](#view-and-use-private-rules)
View your rules in [Semgrep Editor](https://semgrep.dev/orgs/-/editor) under the folder corresponding to your organization name.

You can also find it in the [Semgrep Registry](https://semgrep.dev/explore) by searching for `[organization-id].[rule-id]`. For example: `r2c.test-rule-id`.

To use the rule with subsequent scans, add the rule in the [Registry](https://semgrep.dev/explore) to an existing policy.

## Automatically publish rules[​](#automatically-publish-rules)
This section provides examples of how to automatically publish your private rules so they are accessible within your private organization. Publishing your private rules in this manner does not make them public. In the following examples, the private rules are stored in `private_rule_dir`, which is a subdirectory of the repository root. If your rules are in the root of your repository, you can replace the command with `semgrep publish --visibility=org_private .` to refer to the repository root. You must provide the directory specification.

The following sample of the GitHub Actions workflow publishes rules from a private Git repository after a merge to the `main`, `master`, or `develop` branches.

- 
Ensure that `SEMGREP_APP_TOKEN` is defined in your GitHub project or organization&#x27;s secrets.

- 
Create the following file at `.github/workflows/semgrep-publish.yml`:

`name: semgrep-publishon:  push:    branches:    - main    - master    - developjobs:  publish:    name: publish-private-semgrep-rules    runs-on: ubuntu-latest    container:      image: semgrep/semgrep    steps:    - uses: actions/checkout@v4    - name: publish private semgrep rules      run: semgrep publish --visibility=org_private ./private_rule_dir      env:        SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}`
Alternatively, if you use GitLab, you can use the subsequent sample after ensuring that `SEMGREP_APP_TOKEN` is defined in your GitLab project&#x27;s CI/CD variables:

`semgrep-publish:  image: semgrep/semgrep  script: semgrep publish --visibility=org_private ./private_rule_dirrules:  - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCHvariables:  SEMGREP_APP_TOKEN: $SEMGREP_APP_TOKEN`

## Delete private rules[​](#delete-private-rules)
To remove a private rule, follow these steps:

- In the [Semgrep Editor](https://semgrep.dev/orgs/-/editor), find the private rule to delete under the ** **Library** tab. Private rules are usually stored in the folder with the same name as your Semgrep AppSec Platform organization.
- Click the rule you want to delete, and then click the ** three vertical dots.
- Click ** **Delete**.

Deleting a rule is permanent. If the rule was previously added to the **Policies** page, it is removed upon deletion.

## Appendix[​](#appendix)
### Visibility of private rules[​](#visibility-of-private-rules)
Private rules are only visible to logged-in members of your organization.

### Publish a rule with the same rule ID[​](#publish-a-rule-with-the-same-rule-id)
Rules have unique IDs. If you publish a rule with the same ID as an existing rule, the new rule overwrites the previous one.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Rule writing](/docs/tags/rule-writing)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/writing-rules/private-rules.md)Last updated on **Oct 15, 2025**