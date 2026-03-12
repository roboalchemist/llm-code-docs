# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file/configuration-options.md

# Configuration options

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

### Show possible configurations <a href="#show-possible-configurations" id="show-possible-configurations"></a>

To list all available configuration options as a PR comment, use:

<pre><code><strong>/config
</strong></code></pre>

<figure><img src="https://codium.ai/images/pr_agent/possible_config1.png" alt=""><figcaption></figcaption></figure>

To see which configuration settings were actually used by a specific tool (after user settings are applied), append the following flag to the tool command:

```
/improve --config.output_relevant_configurations=true
```

This will output an additional field showing the actual configurations used for the `improve` tool.

<figure><img src="https://codium.ai/images/pr_agent/possible_config2.png" alt=""><figcaption></figcaption></figure>

### Ignoring Files from Analysis

To skip specific files or folders, use `ignore.glob` or `ignore.regex` patterns. You can edit these to ignore files or folders based on glob or regex patterns.

**Examples:**

Ignore all Python files in a single PR:

```toml
/review --ignore.glob="['*.py']"
```

Ignore Python files for all PRs using glob pattern:

```toml
[ignore]
glob = ['*.py']
```

Ignore Python files for all PRs using regex:

```toml
[regex]
regex = ['.*\.py$']
```

### Extra Instructions

All tools accept an `extra_instructions` parameter that allows you to add free-text extra instructions.

For example:

```bash
/update_changelog --pr_update_changelog.extra_instructions="Update the version number according to these guidelines:..."
```

### Language Settings

Qodo's default response language is US English. You can set the response language  to a different one using the `response_language` parameter. The value should follow a locale code. See the[ list of available locale codes](https://simplelocalize.io/data/locales/).

**Example:**

```toml
[config]
response_language = "it-IT"
```

Only AI-generated text is translated. Static UI elements like labels and headers stay in English.

### Patch Extra Lines

By default, your PR displays three lines of unchanged code above and below each change, to provide context.

```
[ code line that already existed in the file ]
[ code line that already existed in the file ]
[ code line that already existed in the file ]
- code line that was removed in the PR
+ new code line added in the PR
[ code line that already existed in the file ]
[ code line that already existed in the file ]
[ code line that already existed in the file ]
```

Qodo can increase the context around code changes, using:

```toml
[config]
patch_extra_lines_before = 3
patch_extra_lines_after = 1
```

This helps the AI model behind Qodo Merge understand changes better. If the PR is too large, this setting may be automatically disabled.

### Log Level

Control log verbosity with the `log_level` parameter.

The default log level is `DEBUG`, which provides a detailed output of all operations.

If you prefer less verbose logs, you can set higher log levels like `INFO` or `WARNING`.

```toml
[config]
log_level = "DEBUG"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

### Logging with Observability Tools

You can hook into logging observability tools can be used tools like LangSmith using LiteLLM callbacks:

```toml
[litellm]
enable_callbacks = true
success_callback = ["langsmith"]
failure_callback = ["langsmith"]
service_callback = []
```

Then set these environment variables:

```toml
LANGSMITH_API_KEY=<api_key>
LANGSMITH_PROJECT=<project>
LANGSMITH_BASE_URL=<url>
```

### Ignoring PRs Automatically

You can filter out PRs from triggering Qodo Merge using these settings:

**Ignore by Title**

You can set the `ignore_pr_title` to a list of regex patterns to match the PR title you want to ignore:

```toml
[config]
ignore_pr_title = ["\\[Bump\\]"]
```

**Ignore by Branch**

To ignore PRs from specific source or target branches, you can add the following to your `configuration.toml` file:

```toml
[config]
ignore_pr_source_branches = ['develop', 'main']
ignore_pr_target_branches = ["qa"]
```

Where the `ignore_pr_source_branches` and `ignore_pr_target_branches` are lists of regex patterns to match the source and target branches you want to ignore.

**Allow Only Specific Folders**

You can set Qodo Merge to trigger automatically only when PR changes include files in specific folders:

```toml
[config]
allow_only_specific_folders = ['folder1', 'folder2']
```

**Ignore by Label**

To ignore PRs containing specific labels, you can add the following to your `configuration.toml` file:

```toml
[config]
ignore_pr_labels = ["do-not-merge"]
```

**Ignore by Author**

Add the following to your `configuration.toml` file to ignore PRs from specific users:

```toml
[config]
ignore_pr_authors = ["my-special-bot-user"]
```

Where the `ignore_pr_authors` is a list of usernames that you want to ignore.

Qodo Merge also auto-detects bots using GitHub’s bot detection system. However, you can override this by explicitly listing bot usernames to ignore.

{% hint style="info" %}
**Notice:** Bots may still receive responses if a PR they open fails tests and triggers the [`ci_feedback`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/checks-ci-feedback) tool.
{% endhint %}
