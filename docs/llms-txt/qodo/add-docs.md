# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/add-docs.md

# Add Docs

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

The `add_docs` tool scans the PR code changes, and automatically suggests documentation for any code components that changed in the PR.

The `add_docs` tool supports the programming languages: Python, Java, C++, JavaScript, TypeScript, C#.

## How to use the `add_docs` tool

**Manual usage**

Comment on the PR:

```
/add_docs
```

You can also state a name of a specific component in the PR to get documentation only for that component:

```
/add_docs component_name
```

This tool can also be triggered interactively by using the [`analyze`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/analyze) tool.

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `add_docs` tool by setting configurations under the `pr_add_docs` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="237.734375">Possible configurations</th><th width="169.38671875">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>docs_style</code></td><td><code>sphinx</code></td><td>The exact style of the documentation (for python docstring). You can choose from: <code>google</code>, <code>numpy</code>, <code>sphinx</code>, <code>restructuredtext</code>, <code>plain</code>. </td></tr><tr><td><code>extra_instructions</code></td><td>none</td><td>Optional extra instructions for the tool. For example: "focus on the changes in the file X", "Ignore changes in ..."</td></tr></tbody></table>

## Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://codium.ai/images/pr_agent/docs_command.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/docs_components.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://codium.ai/images/pr_agent/docs_single_component.png" alt="" width="563"><figcaption></figcaption></figure>
