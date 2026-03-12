# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/custom-prompt.md

# Custom Prompt

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

The `custom_prompt` tool scans the PR code changes, and automatically generates suggestions for improving the PR code.

It shares similarities with the `improve` tool, but with one main difference: the `custom_prompt` tool will **only propose suggestions that follow specific guidelines defined by the prompt** in the `pr_custom_prompt.prompt` configuration.

With this tool, you are the prompter. Be specific, clear, and concise in the instructions. Specify relevant aspects that you want the model to focus on.

## How to use the `custom_prompt` tool

**Manual usage**

Comment on the PR:

```bash
/custom_prompt --pr_custom_prompt.prompt="
The code suggestions should focus only on the following:
- ...
- ...
"
```

**Automatic usage**

To run the tool automatically when a new issue is opened, add it to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[pr_custom_prompt]
prompt="""\
The suggestions should focus only on the following:
-...
-...

"""
```

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `custom_prompt` tool by setting configurations under the `pr_custom_prompt` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="257.36328125">Possible configurations</th><th width="222.34765625">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>prompt</code></td><td>none</td><td><p></p><p>The prompt for the tool. It should be a multi-line string.</p></td></tr><tr><td><code>num_code_suggestions_per_chunk</code></td><td><code>3</code></td><td>Number of code suggestions provided by the <code>custom_prompt</code> tool, per chunk.</td></tr><tr><td><code>enable_help_text</code></td><td><code>true</code></td><td>If set to true, the tool will display a help text in the comment</td></tr></tbody></table>

## Example usage <a href="#example-usage" id="example-usage"></a>

An example of a possible prompt defined in the configuration file:

```toml
[pr_custom_prompt]
prompt="""\
The code suggestions should focus only on the following:
- look for edge cases when implementing a new function
- make sure every variable has a meaningful name
- make sure the code is efficient
"""
```

The prompt should be specific and clear, and be tailored to the needs of your project.

Results obtained with the prompt above:

<figure><img src="https://codium.ai/images/pr_agent/custom_suggestions_result.png" alt="" width="563"><figcaption></figcaption></figure>
