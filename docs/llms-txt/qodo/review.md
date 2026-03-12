# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/review.md

# Review

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

The `review` tool scans the PR code changes, and generates a list of feedbacks about the PR, aiming to aid the reviewing process.

Note that the main purpose of the `review` tool is to provide the **PR reviewer** with useful feedbacks and insights. The **PR author** may prefer to focus on the output of the [`improve` tool](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/improve), which provides actionable code suggestions.

***

## Example usage <a href="#example-usage" id="example-usage"></a>

#### Manual triggering <a href="#manual-triggering" id="manual-triggering"></a>

Run the tool manually by commenting `/review` on any PR:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2Fe72ulLqdIO5Ta6hc1FV8%2Fimage.png?alt=media&#x26;token=880b885a-2b63-4b6c-8fa5-e1c0a50d759e" alt="" width="563"><figcaption></figcaption></figure>

The tool will generate a review for the PR:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FdUHachP3SgQWHiyeeQ7R%2Fimage.png?alt=media&#x26;token=6b45b078-9e8b-44d2-9a92-0630e8cb870f" alt="" width="563"><figcaption></figcaption></figure>

***

## How to use the `review` tool

**Manual usage**

Comment on the PR:

```bash
/review
```

You can also add configuration flags to the command to customize behavior:

```bash
/review --pr_reviewer.some_config1=... --pr_reviewer.some_config2=...
```

**Automatic usage**

To run the tool automatically when a PR is opened, add it to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[github_app]
pr_commands = [
    "/review",
    ...
]

[pr_reviewer] # Edit this field to enable/disable the tool, or to change the configurations used.
extra_instructions = "..."
...
```

[Learn more about automatic usage of tools.](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide)

When you first install Qodo app, the [default mode](https://qodo-merge-docs.qodo.ai/usage-guide/automations_and_usage/#github-app-automatic-tools-when-a-new-pr-is-opened) for the `review` tool is:

```
pr_commands = ["/review", ...]
```

Meaning the `review` tool will run automatically on every PR, without any additional configurations. Edit this field to enable/disable the tool, or to change the configurations used.

***

## Configuration Options

### Configuration Options Table

Configure the `review` tool by setting configurations under the `pr_reviewer` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

#### General options

<table><thead><tr><th width="259.81640625">Possible configurations</th><th width="140.7265625">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>persistent_comment</code></td><td><code>true</code></td><td>If set to true, the review comment will be persistent, meaning that every new review request will edit the previous one.</td></tr><tr><td><code>final_update_message</code></td><td><code>true</code></td><td>If set to true, updating a persistent review comment will automatically add a short comment to the PR with a link to the updated review.</td></tr><tr><td><code>extra_instructions</code></td><td>none</td><td>Optional extra instructions for the tool. For example: "focus on the changes in the file X", "Ignore changes in ..."</td></tr><tr><td><code>enable_help_text</code></td><td><code>true</code></td><td>If set to true, Qodo will display a help text in the comment.</td></tr></tbody></table>

#### Enable\disable specific sub-sections

<table><thead><tr><th width="261.7578125">Possible configurations</th><th width="141.65625">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>require_score_review</code></td><td><code>false</code></td><td>If set to true, Qodo will add a section that scores the PR.</td></tr><tr><td><code>require_tests_review</code></td><td><code>true</code></td><td>If set to true, Qodo will add a section that checks if the PR contains tests.</td></tr><tr><td><code>require_estimate_effort_to_review</code></td><td><code>true</code></td><td>If set to true, Qodo will add a section that estimates the effort needed to review the PR.</td></tr><tr><td><code>require_can_be_split_review</code></td><td><code>false</code></td><td>If set to true, Qodo will add a section that checks if the PR contains several themes, and can be split into smaller PRs.</td></tr><tr><td><code>require_security_review</code></td><td><code>true</code></td><td>If set to true, Qodo will add a section that checks if the PR contains a possible security or vulnerability issue.</td></tr><tr><td><code>require_ticket_analysis_review</code></td><td><code>true</code></td><td>If set to true, and the PR contains a GitHub or Jira ticket link, Qodo will add a section that checks if the PR fulfilled the ticket requirements.</td></tr></tbody></table>

#### Adding PR labels

You can enable the `review` tool to add specific labels to the PR:

<table><thead><tr><th width="262.1015625">Possible configurations</th><th width="147.40234375">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>enable_review_labels_security</code></td><td><code>true</code></td><td>If set to true, Qodo will publish a <code>possible security issue</code> label if it detects a security issue.</td></tr><tr><td><code>enable_review_labels_effort</code></td><td><code>true</code></td><td>If set to true, Qodo will publish a <code>Review effort</code> label, with a score from 1 to 5.</td></tr></tbody></table>

***

### Extra instructions

Extra instructions are important. The `review` tool can be configured with extra instructions, which can be used to guide Qodo to a feedback tailored to the needs of your project.

Be specific, clear, and concise in the instructions. With extra instructions, you are the prompter. Specify the relevant sub-tool, and the relevant aspects of the PR that you want to emphasize.

Examples of extra instructions:

```toml
[pr_reviewer]
extra_instructions="""\
In the code feedback section, emphasize the following:
- Does the code logic cover relevant edge cases?
- Is the code logic clear and easy to understand?
- Is the code logic efficient?
...
"""
```

Use **triple quotes** to write multi-line instructions.

***

### Labels

The `review` tool can auto-generate two specific types of labels for a PR:

* A `possible security issue` label that detects if a possible [security issue](https://github.com/Codium-ai/pr-agent/blob/tr/user_description/pr_agent/settings/pr_reviewer_prompts.toml#L136) exists in the PR code (`enable_review_labels_security` flag)
* A `Review effort [1-5]: x` label, where x is the estimated effort to review the PR (`enable_review_labels_effort` flag)

Both modes are useful, and we recommended to enable them.
