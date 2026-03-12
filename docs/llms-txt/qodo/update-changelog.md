# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/update-changelog.md

# Update Changelog

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, Bitbucket & Gitlab (partial)
{% endhint %}

The `update_changelog` tool automatically updates the `CHANGELOG.md` file with the PR changes.

## How to use the `update_changelog` tool

**Manual usage**

Comment on the PR:

```
/update_changelog
```

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `update_changelog` tool by setting configurations under the `pr_update_changelog` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="237.734375">Possible configurations</th><th width="169.38671875">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>push_changelog_changes</code></td><td><code>false</code> (publish as a comment)</td><td>Choose whether to push the changes to <code>CHANGELOG.md</code>, or publish them as a comment.<br><br><strong>Not supported on Gitlab</strong></td></tr><tr><td><code>extra_instructions</code></td><td>none</td><td>Optional extra instructions for the tool. For example: "focus on the changes in the file X", "Ignore changes in ..."</td></tr><tr><td><code>add_pr_link</code></td><td><code>true</code></td><td>Choose whether to add a link to the PR in the changelog.</td></tr><tr><td><code>skip_ci_on_push</code></td><td><code>true</code></td><td>Choose whether the commit message will include the term <code>[skip ci]</code>, preventing CI tests to be triggered on the changelog commit.</td></tr></tbody></table>

## Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://codium.ai/images/pr_agent/update_changelog_comment.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/update_changelog.png" alt="" width="563"><figcaption></figcaption></figure>
