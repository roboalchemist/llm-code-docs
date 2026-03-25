# Source: https://docs.qodo.ai/qodo-documentation/code-review/concepts/enable-ci-failure-feedback.md

# Enable Automatic CI Failure Feedback

{% hint style="success" %}
**Platform supported:** GitHub
{% endhint %}

Qodo provides **automatic CI feedback** when a pull request contains failed checks.

When a CI failure is detected, Qodo analyzes the results and surfaces structured, actionable information directly in the pull request to help developers quickly understand and resolve the issue.

The CI feedback includes:

* **Failed stage** – the pipeline stage where the failure occurred
* **Failed test name** – the specific test or job that failed
* **Failure summary** – a concise explanation of what went wrong
* **Relevant error logs** – extracted log output to aid debugging

This feedback helps reduce context switching by keeping CI failure analysis inside the pull request, where developers are already working.

### Using CI feedback in pull requests

#### **Manual usage**

Comment on the PR:

```
/checks "https://github.com/{repo_name}/actions/runs/{run_number}/job/{job_number}"
```

Where:

* `{repo_name}` is the name of the repository.
* `{run_number}` is the run number of the failed check.
* `{job_number}` is the job number of the failed check.

### Disabling the tool from running automatically <a href="#disabling-the-tool-from-running-automatically" id="disabling-the-tool-from-running-automatically"></a>

If you wish to disable the tool from running automatically, add the following add to the [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/configuration-file):

```
[checks]
enable_auto_checks_feedback = false 
```

### Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `checks` tool by setting configurations under the `checks` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/get-started/configuration-overview/configuration-file).

<table><thead><tr><th>Configuration key</th><th>Default value</th><th width="356.541748046875">Description</th></tr></thead><tbody><tr><td><code>enable_auto_checks_feedback</code></td><td><code>true</code></td><td>Automatically provides feedback when a CI check fails on a pull request.</td></tr><tr><td><code>excluded_checks_list</code></td><td><code>[]</code></td><td>A list of CI checks to exclude from feedback (for example: <code>["check1", "check2"]</code>).</td></tr><tr><td><code>persistent_comment</code></td><td><code>true</code></td><td>Updates an existing CI feedback comment instead of posting a new one for each run.</td></tr><tr><td><code>enable_help_text</code></td><td><code>true</code></td><td>Displays a help message when a user comments <code>/checks</code> on a pull request.</td></tr><tr><td><code>final_update_message</code></td><td><code>true</code></td><td>When <code>persistent_comment</code> is enabled, posts an additional message indicating that the CI feedback was updated to the latest commit.</td></tr></tbody></table>

Example:&#x20;

![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2Fwww.codium.ai%2Fimages%2Fpr_agent%2Ffailed_check1.png\&width=768\&dpr=3\&quality=100\&sign=5c1019fb\&sv=2)![](https://docs.qodo.ai/qodo-documentation/~gitbook/image?url=https%3A%2F%2Fwww.codium.ai%2Fimages%2Fpr_agent%2Ffailed_check2.png\&width=768\&dpr=3\&quality=100\&sign=f6c3df9a\&sv=2)

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FdIWxdN698SnEvIc0mOik%2Fimage.png?alt=media&#x26;token=72b6a6fe-afa9-4309-89e7-4547a6a366ae" alt=""><figcaption></figcaption></figure>
