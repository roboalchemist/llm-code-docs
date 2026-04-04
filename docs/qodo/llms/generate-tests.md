# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/generate-tests.md

# Generate Tests

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

The `test` tool generate tests for a selected component, based on the PR code changes.

The `test` tool supports the programming languages: Python, Java, C++, JavaScript, TypeScript, C#.

***

## How to use the `test` tool

This tool can also be triggered interactively by using the [`analyze`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/analyze) tool.

**Manual usage**

Comment on the PR:

```
/test component_name
```

The tool will generate tests for the selected component.

&#x20;If no component is selected, `test` will generate tests for largest component.

### Choosing components

You can set the component name as the name of a specific component in the PR.

To get a list of the components that changed in the PR and choose the relevant component interactively, use the [`analyze`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/analyze) tool.

***

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `test` tool by setting configurations under the `pr_test` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="257.36328125">Possible configurations</th><th width="222.34765625">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>num_tests</code></td><td><code>3</code></td><td>Number of tests to generate.</td></tr><tr><td><code>testing_framework</code></td><td><p>For Python: <code>pytest</code></p><p>For Java: <code>JUnit</code></p><p>For C++: <code>Catch2</code></p><p>For JavaScript &#x26; TypeScript: <code>jest</code></p></td><td>The testing framework to use.</td></tr><tr><td><code>avoid_mocks</code></td><td><code>true</code></td><td>if set to true, the tool will try to avoid using mocks in the generated tests. Note that even if this option is set to true, the tool might still use mocks if it cannot generate a test without them.</td></tr><tr><td><code>extra_instructions</code></td><td>none</td><td>Optional extra instructions for the tool. For example: "focus on the changes in the file X", "Ignore changes in ..."</td></tr><tr><td><code>file</code></td><td>none</td><td>Lets you specify a relevant file in case there are several components with the same name.</td></tr><tr><td><code>class_name</code></td><td>nona</td><td>Lets you specify a relevant class name in case there are several methods with the same name in the same file.</td></tr><tr><td><code>enable_help_text</code></td><td><code>true</code></td><td>If set to true, the tool will add a help text to the PR comment.</td></tr></tbody></table>

***

## Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://codium.ai/images/pr_agent/test1.png" alt="" width="563"><figcaption></figcaption></figure>
