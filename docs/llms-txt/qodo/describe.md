# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/describe.md

# Describe

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

The `describe` tool scans the PR code changes, and generates a full PR description: title, type, summary, a walkthrough of the changes made in the PR, and suggested labels.

***

## Example Usage

#### Manual triggering <a href="#manual-triggering" id="manual-triggering"></a>

Comment `/describe` on any PR:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2F81sq0EvYfk6NY1eRqSgf%2Fimage.png?alt=media&#x26;token=abd2bd20-0d11-4c15-8f84-12e1bc3d1039" alt="" width="563"><figcaption></figcaption></figure>

Qodo Git plugin will generate a description for the PR:

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FyI4KQO2VyXl8UxKRtv8n%2Fimage.png?alt=media&#x26;token=4c950d5e-16a3-4350-a007-3d8e38db2499" alt="" width="563"><figcaption></figcaption></figure>

***

## How to use the `describe` tool

**Manual usage**

Comment on the PR:

```bash
/describe
```

You can also add configuration flags to the command to customize behavior:

<pre class="language-bash"><code class="lang-bash"><strong>/describe --pr_description.publish_labels=true
</strong></code></pre>

**Automatic usage**

To run the tool automatically when a PR is opened, add it to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[github_app]
pr_commands = [
    "/describe",
    ...
]

[pr_description]
publish_labels = true
...
```

[Learn more about automatic usage of tools.](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/getting-started/usage-guide)

***

## Configuration Options

### Configuration Options Table

Configure the `describe` tool by setting configurations under the `pr_description` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="279.92578125">Possible configurations</th><th width="152.99609375">Default value</th><th>What do they do</th></tr></thead><tbody><tr><td><code>publish_labels</code></td><td><code>false</code></td><td>If set to true, Qodo will publish labels to the PR.</td></tr><tr><td><code>publish_description_as_comment</code></td><td><code>false</code></td><td>If set to true, Qodo will publish the description as a comment to the PR.<br>If false, it will overwrite the original description.</td></tr><tr><td><code>publish_description_as_comment_persistent</code></td><td><code>true</code></td><td>If set to true and <code>publish_description_as_comment</code> is true, Qodo will publish the description as a persistent comment to the PR.</td></tr><tr><td><code>add_original_user_description</code></td><td><code>true</code></td><td>If set to true, Qodo will add the original user description to the generated description.</td></tr><tr><td><code>generate_ai_title</code></td><td><code>false</code></td><td>If set to true, Qodo will generate an AI title for the PR.</td></tr><tr><td><code>extra_instructions</code></td><td>none</td><td>Optional extra instructions for the tool. For example: "focus on the changes in the file X", "Ignore changes in ..."</td></tr><tr><td><code>enable_pr_type</code></td><td><code>true</code></td><td>If set to false, Qodo will not show the <code>PR type</code> as a text value in the description content.</td></tr><tr><td><code>final_update_message</code></td><td><code>false</code></td><td>If set to true, Qodo will add a comment message <a href="https://github.com/Codium-ai/pr-agent/pull/499#issuecomment-1837412176"><code>PR Description updated to latest commit...</code></a> after finishing calling <code>/describe</code>.</td></tr><tr><td><code>enable_semantic_files_types</code></td><td><code>true</code></td><td>If set to true, "Changes walkthrough" section will be generated.</td></tr><tr><td><code>collapsible_file_list</code></td><td><code>adaptive</code></td><td>If set to true, the file list in the "Changes walkthrough" section will be collapsible. If set to "adaptive", the file list will be collapsible only if there are more than 8 files.</td></tr><tr><td><code>enable_large_pr_handling</code></td><td><code>true</code></td><td>If set to true, in case of a large PR Qodo will make several calls to the AI models and combine them to be able to cover more files.</td></tr><tr><td><code>enable_help_text</code></td><td><code>false</code></td><td>If set to true, Qodo will display a help text in the comment.</td></tr></tbody></table>

### **Preserve your own PR description**

By default, Qodo keeps your original PR description at the top and adds the generated description below it.\
Just make sure to add your description during the initial PR creation. Editing the description while Qodo is running might cause issues.

Any text above the `PR Type` header is considered as user-written content and will be preserved. Any text below it is auto-generated and will be replaced.

<figure><img src="https://codium.ai/images/pr_agent/pr_description_user_description.png" alt=""><figcaption></figcaption></figure>

***

### **Show file summaries in "Files changed"**

You can choose to show a summary of code changes for each file inside the “Files changed” tab (GitHub only).

Click on the checkbox that appears in the PR Description status message, below the main PR Description.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FO3Hssjw2tNSfz0MqS5LA%2FScreenshot%202025-05-13%20at%2012.10.18.png?alt=media&#x26;token=ac212ccc-06cf-4497-aba5-4c732e6007ff" alt=""><figcaption></figcaption></figure>

**To enable the summary for every PR:** make the following change in your configuration file:&#x20;

```toml
[pr_description]
inline_file_summary = "table"  # or "true" or "false"
```

* `table`: A summary table will be displayed at the top of "Files changed" tab.
* `true`: Adds a comment to each file with a short summary.
* `false` (default): File changes walkthrough will appear only in the main PR description (the "Conversations" tab).

***

### **Use markers to control placement of generated content**

You can define exactly where each part of the generated description should appear using markers.

For example, if the PR's original description was:

```md
## PR Type:
pr_agent:type

## PR Description:
pr_agent:summary

## PR Walkthrough:
pr_agent:walkthrough
```

The description will replace the `pr_agent:` placeholders with the relevant content.

To enable this, make the following change in your configuration file:&#x20;

```toml
[pr_description]
use_description_markers = true
include_generated_by_header = false
```

**Configuration params**:

* `use_description_markers`: if set to true, the tool will use markers template. Default is false.
* `include_generated_by_header`: if set to true, the tool will add a dedicated header: **Generated by PR Agent at...** to any automatic content. Default is true.

***

### Custom labels

The default labels of the describe tool are generic: `Bug fix`, `Tests`, `Enhancement`, `Documentation`, `Other`.

You can add your own custom labels that fit your repository better.

There are two ways to define them:

#### **1. From a configuration file**

```toml
[config]
enable_custom_labels=true


[custom_labels."sql_changes"]
description = "Use when a PR contains changes to SQL queries"

[custom_labels."test"]
description = "use when a PR primarily contains new tests"

...
```

**Follow these guidelines for setting custom labels in your configuration file:**

* Use a clear name.
* Add a detailed description for each label so that Qodo knows when to suggest it.
  * A good description should be a conditional statement that indicates whether the label should be added to the PR or not, based on the PR's content. For example: `Use when a PR contains changes to SQL queries`.

#### **2. From your repository’s labels page**

* **GitHub:** Go to `https://github.com/{owner}/{repo}/labels`
* **GitLab:** Go to `https://gitlab.com/{owner}/{repo}/-/labels`

**Follow these guidelines for setting custom labels in your repository’s labels page:**

* Use a clear name.
* Add a detailed description for each label so that Qodo knows when to suggest it.
  * Start the description of with prefix `pr_agent:`, for example: `pr_agent: Description of when AI should suggest this label`.

<figure><img src="https://codium.ai/images/pr_agent/add_native_custom_labels.png" alt=""><figcaption></figcaption></figure>

For example:&#x20;

```
Name: Main topic:performance
Description: pr_agent:The main topic of this PR is performance

Name: New endpoint
Description: pr_agent:A new endpoint was added in this PR

Name: SQL query
Description: pr_agent:A new SQL query was added in this PR

Name: Dockerfile changes
Description: pr_agent:The PR contains changes in the Dockerfile
```
