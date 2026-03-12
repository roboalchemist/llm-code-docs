# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/checks-ci-feedback.md

# Checks (CI Feedback)

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub
{% endhint %}

The CI feedback tool `/checks` automatically triggers when a PR has a failed check.

The tool analyzes the failed checks and provides several feedbacks:

* Failed stage
* Failed test name
* Failure summary
* Relevant error logs

***

## How to use the `/checks` tool

**Manual usage**

Comment on the PR:

```
/checks "https://github.com/{repo_name}/actions/runs/{run_number}/job/{job_number}"
```

Where:

* `{repo_name}` is the name of the repository.
* `{run_number}` is the run number of the failed check.
* `{job_number}` is the job number of the failed check.

### Disabling the tool from running automatically <a href="#disabling-the-tool-from-running-automatically" id="disabling-the-tool-from-running-automatically"></a>

If you wish to disable the tool from running automatically, a the following add to the [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[checks]
enable_auto_checks_feedback = false 
```

***

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `checks` tool by setting configurations under the `checks` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="259.98046875">Possible configurations</th><th width="222.34765625">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>enable_auto_checks_feedback</code></td><td><code>true</code></td><td>If set to true, the tool will automatically provide feedback when a check is failed.</td></tr><tr><td><code>excluded_checks_list</code></td><td><code>[]</code></td><td><p>A list of checks to exclude from the feedback.</p><p>For example: <code>["check1", "check2"]</code>.</p></td></tr><tr><td><code>persistent_comment</code></td><td><code>true</code></td><td>If set to true, the tool will overwrite a previous checks comment with new feedback.</td></tr><tr><td><code>enable_help_text</code></td><td><code>true</code></td><td>If set to true, the tool will provide a help message when a user comments <code>/checks</code> on a PR.</td></tr><tr><td><code>final_update_message</code></td><td><code>true</code></td><td>If <code>persistent_comment</code> is true and updating a previous checks message, the tool will also create a new message: <code>"Persistent checks updated to latest commit"</code>.</td></tr></tbody></table>

***

## Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://www.codium.ai/images/pr_agent/failed_check1.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://www.codium.ai/images/pr_agent/failed_check2.png" alt="" width="563"><figcaption></figcaption></figure>
