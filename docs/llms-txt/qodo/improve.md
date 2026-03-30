# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/improve.md

# Improve

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

The `improve` tool scans the PR code changes, and automatically generates meaningful suggestions for improving the PR code.&#x20;

***

## Example usage <a href="#example-usage" id="example-usage"></a>

{% tabs %}
{% tab title="Suggestions Overview" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FFwz0xBfjWZS73vC7mN1k%2Fimage.png?alt=media&#x26;token=9026fce2-d470-485f-ac2e-e17469f2356e" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Selecting a Specific Suggestion" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FyXGcrhfV6qn1ir12PvgQ%2Fimage.png?alt=media&#x26;token=da9970d4-427b-4ecf-a1cf-51973441045f" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Committable Code Comments" %}

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FWTTVMV20Y8pmRQdHipFH%2Fimage.png?alt=media&#x26;token=13ab3cb1-c2d8-4f39-8c6d-0aafabd97f4a" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

***

## How to use the `improve` tool

**Manual usage**

Comment on the PR:

```bash
/improve
```

You can also add configuration flags to the command to customize behavior:

```bash
/improve --pr_code_suggestions.some_config1=... --pr_code_suggestions.some_config2=...
```

**Automatic usage**

To run the tool automatically when a PR is opened, add it to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[github_app]
pr_commands = [
    "/improve",
    ...
]

[pr_code_suggestions]
num_code_suggestions_per_chunk = ...
...
```

[Learn more about automatic usage of tools.](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide)

When you first install Qodo app, the [default mode](https://qodo-merge-docs.qodo.ai/usage-guide/automations_and_usage/#github-app-automatic-tools-when-a-new-pr-is-opened) for the `improve` tool is:

```
pr_commands = ["/improve", ...]
```

Meaning the `review` tool will run automatically on every PR, without any additional configurations. Edit this field to enable/disable the tool, or to change the configurations used.

### Code suggestions elements <a href="#implementing-the-proposed-code-suggestions" id="implementing-the-proposed-code-suggestions"></a>

Each generated suggestion consists of three key elements:

1. A single-line summary of the proposed change.
2. An expandable section containing a description of the suggestion.
3. A diff snippet showing the recommended code modification (before and after).

### Interactive options

After using the `improve` tool, you can immediately trigger actions and apply changes with simple checkbox clicks:

* ***Apply this suggestion*****&#x20;button**: Clicking this checkbox instantly converts a suggestion into a committable code change. When committed to the PR, changes made to code that was flagged for improvement will be marked with a check mark, allowing developers to easily track and review implemented recommendations.
* ***More button***: Triggers additional suggestions generation while keeping each suggestion focused and relevant as the original set
* ***Update*****&#x20;button**: Triggers a re-analysis of the code, providing updated suggestions based on the latest changes
* ***Author self-review*****&#x20;button**: Interactive acknowledgment that developers have opened and reviewed collapsed suggestions

***

## Configuration Options

### Configuration Options Table

Configure the `improve` tool by setting configurations under the `pr_code_suggestions` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

#### General options

<table><thead><tr><th width="239.23828125">Possible configurations</th><th width="157.6953125">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>extra_instructions</code></td><td>none</td><td>Optional extra instructions for the tool. For example: "focus on the changes in the file X", "Ignore changes in ..."</td></tr><tr><td><code>commitable_code_suggestions</code></td><td><code>false</code></td><td>If set to true, the tool will display the suggestions as committable code comments.</td></tr><tr><td><code>enable_chat_in_code_suggestions</code></td><td><code>true</code></td><td>If set to true, Qodo will interact with comments made on code changes it has proposed.</td></tr><tr><td><code>dual_publishing_score_threshold</code></td><td><code>-1</code> (disabled)</td><td>Minimum score threshold for suggestions to be presented as committable PR comments.</td></tr><tr><td><code>focus_only_on_problems</code></td><td><code>true</code></td><td>If set to true, suggestions will focus primarily on identifying and fixing code problems, and less on style considerations like best practices, maintainability, or readability.</td></tr><tr><td><code>persistent_comment</code></td><td><code>true</code></td><td>If set to true, the improve comment will be persistent, meaning that every new improve request will edit the previous one.</td></tr><tr><td><code>suggestions_score_threshold</code></td><td><code>0</code></td><td>Any suggestion with importance score less than this threshold will be removed.</td></tr><tr><td><code>apply_suggestions_checkbox</code></td><td><code>true</code></td><td>Enable a checkbox to create a committable suggestion.</td></tr><tr><td><code>enable_more_suggestions_checkbox</code></td><td><code>true</code></td><td>Enable a checkbox to generate more suggestions.</td></tr><tr><td><code>enable_help_text</code></td><td><code>true</code></td><td>If set to true, Qodo will display a help text in the comment.</td></tr><tr><td><code>enable_chat_text</code></td><td><code>true</code></td><td>If set to true, Qodo will display a reference to the PR chat in the comment.</td></tr><tr><td><code>publish_output_no_suggestions</code></td><td><code>true</code></td><td>If set to true, Qodo will publish a comment even if no suggestions were found.</td></tr><tr><td><code>wiki_page_accepted_suggestions</code></td><td><code>true</code></td><td>If set to true, Qodo will automatically track accepted suggestions in a dedicated wiki page called <code>.pr_agent_accepted_suggestions</code>.</td></tr><tr><td><code>allow_thumbs_up_down</code></td><td><code>false</code></td><td><p>If set to true, all code suggestions will have thumbs up and thumbs down buttons.</p><p>Note that this feature is for statistics tracking. It will not affect future feedback from the AI model.</p></td></tr></tbody></table>

#### Params for number of suggestions and AI calls

<table><thead><tr><th width="252.2109375">Possible configurations</th><th width="150.54296875">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>auto_extended_mode</code></td><td><code>true</code></td><td>Enable chunking the PR code and running the tool on each chunk.</td></tr><tr><td><code>num_code_suggestions_per_chunk</code></td><td><code>3</code></td><td>Number of code suggestions provided by the 'improve' tool, per chunk.</td></tr><tr><td><code>max_number_of_calls</code></td><td><code>3</code></td><td>Maximum number of chunks.</td></tr></tbody></table>

***

## Other features of the `improve` tool

### Best Practices

Another option to give additional guidance to the AI model is by creating a [best\_practices.md file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/best-practices) in your repository's root directory.

You can also setup [a wiki page](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/enabling-a-wiki) in GitHub.

***

### Extra instructions

Extra instructions are important. The `imrpove` tool can be configured with extra instructions, which can be used to guide Qodo to a feedback tailored to the needs of your project.

Be specific, clear, and concise in the instructions. With extra instructions, you are the prompter. Specify the relevant sub-tool, and the relevant aspects of the PR that you want to emphasize.

Examples of extra instructions:

```toml
[pr_code_suggestions]
extra_instructions="""\
(1) Answer in Japanese
(2) Don't suggest to add try-except block
(3) Ignore changes in toml files
...
"""
```

Use **triple quotes** to write multi-line instructions.

***

### Dual publishing mode <a href="#dual-publishing-mode" id="dual-publishing-mode"></a>

Dual publishing mode allows code suggestions to appear as commit-ready comments in the PR.

This mode helps highlight suggestions that are more critical.

To activate dual publishing mode, use the following setting:

```toml
[pr_code_suggestions]
dual_publishing_score_threshold = x # The minimum score threshold >=
```

Where x represents the minimum score threshold (>=) for suggestions to be presented as commitable PR comments in addition to the table. The default value is -1 (disabled).

***

### Self-review <a href="#self-review" id="self-review"></a>

{% hint style="info" %}

### Platforms supported: GitHub, GitLab <a href="#self-review" id="self-review"></a>

{% endhint %}

You can set the `improve` tool to add a checkbox below the suggestions, prompting users to acknowledge that they have reviewed them.

In your configuration file, set:

```toml
[pr_code_suggestions]
demand_code_suggestions_self_review = true 
```

You can set the content of the checkbox text via:

```toml
[pr_code_suggestions]
code_suggestions_self_review_text = "... (your text here) ..."
```

<figure><img src="https://codium.ai/images/pr_agent/self_review_1.png" alt="" width="375"><figcaption></figcaption></figure>

### Make self-review mandatory

To enforce self-review before merging, add the following to your configuration file:

```toml
[pr_code_suggestions]
approve_pr_on_self_review = true
```

This allows Qodo to automatically approve the PR when the author checks the self-review box.

When used together with a minimum of 2 as the required number of approvals, this ensures the PR author must complete a self-review for the PR to be mergeable.

<figure><img src="https://codium.ai/images/pr_agent/self_review_2.png" alt="" width="563"><figcaption></figcaption></figure>

***

### Auto-approval <a href="#auto-approval" id="auto-approval"></a>

{% hint style="info" %}

### Platforms supported: GitHub, GitLab, Bitbucket <a href="#self-review" id="self-review"></a>

{% endhint %}

Qodo can auto-approve a PR when a specific comment is invoked, or when the PR meets certain criteria.

To ensure safety, the auto-approval feature is disabled by default.

{% hint style="warning" %}
N**ote**: the approval flags cannot be set as command line arguments, only in the configuration file.
{% endhint %}

To enable auto-approval features, you need to set one or both of the following options in your configuration file:

1. **Auto-approval by commenting**

To enable auto-approval by commenting, set in the configuration file:

```toml
[config]
enable_comment_approval = true
```

After setting, comment on a PR:

```bash
/review auto_approve
```

Qodo will automatically approve the PR, and add a comment with the approval.

2\. **Auto-approval when the PR meets a condition**

To enable auto-approval based on specific criteria, set in the configuration file:

```toml
[config]
enable_auto_approval = true
```

You can configure auto-approval to trigger based on either of these two conditions:

1. **Review effort score**

```toml
[config]
enable_auto_approval = true
auto_approve_for_low_review_effort = X # X is a number between 1 to 5
```

When the review effort score is lower or equal to X, the PR will be auto-approved.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FcFmp7yAtTW7teOXPwET3%2Fimage.png?alt=media&#x26;token=3569d72e-27fc-4dcc-b0d0-5103a617d3de" alt="" width="563"><figcaption></figcaption></figure>

2. **No code suggestions**

```toml
[config]
enable_auto_approval = true
auto_approve_for_no_suggestions = true
```

When no code suggestion were found for the PR, the PR will be auto-approved.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FpHAcfY2qpcF3XM77sTRY%2Fimage.png?alt=media&#x26;token=a9efbb17-20ad-46b4-a339-a71ce71046d6" alt="" width="563"><figcaption></figcaption></figure>

***

### Automatic updates on new commits - the Update button <a href="#example-usage" id="example-usage"></a>

When new commits are pushed after a recent code suggestions report on a pull request, an **Update** button appears (as shown below).

Clicking this button triggers the `/improve` tool, which:

1. Detects what's changed since the last report
2. Generates suggestions based on those new changes
3. Merges these suggestions with the overall PR feedback, highlighting recent updates
4. Marks change-related comments with a note and an asterisk (\*), including a link to this page for easy reference

**Benefits for Developers**

* **Stay focused:** Get feedback on the most recent changes first
* **Stay organized:** Comments related to new commits are clearly marked
* **Stay efficient:** Tackle feedback in order, starting with what's new

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FYFAqvm6FJk2Z0SWiw6BI%2Fimage.png?alt=media&#x26;token=59a1b27d-2607-497f-9511-9f4af67a060f" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FopAF8Q2SyKO2qASOcxM5%2Fimage.png?alt=media&#x26;token=1fd330cb-e504-42ac-8fd3-45bcbc9cdebb" alt="" width="563"><figcaption></figcaption></figure>
