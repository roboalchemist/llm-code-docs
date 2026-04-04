# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/improve-component.md

# Improve Component

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

The `improve_component` tool generates code suggestions for a specific code component that changed in the PR. The `improve_component` tool supports the programming languages: Python, Java, C++, JavaScript, TypeScript, C#.

***

### How to use the `improve_component` tool <a href="#how-to-use-the-improve_component-tool" id="how-to-use-the-improve_component-tool"></a>

This tool can also be triggered interactively by using the [`analyze`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/analyze) tool. \
**Manual usage**\
Comment on the PR: /improve\_component component\_name The tool will generate code suggestions for the selected component. If no component is stated, it will generate code suggestions for the largest component.

#### Choosing components <a href="#choosing-components" id="choosing-components"></a>

You can set the component name as the name of a specific component in the PR. To get a list of the components that changed in the PR and choose the relevant component interactively, use the [`analyze`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/analyze) tool.

***

### Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `improve_component` tool by setting configurations under the `pr_improve_component` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

| `num_code_suggestions` | `4`  | Number of code suggestions to provide.                                                                               |
| ---------------------- | ---- | -------------------------------------------------------------------------------------------------------------------- |
| `extra_instructions`   | none | Optional extra instructions for the tool. For example: "focus on the changes in the file X", "Ignore changes in ..." |
| `file`                 | none | Lets you specify a relevant file in case there are several components with the same name.                            |
| `class_name`           | none | Lets you specify a relevant class name in case there are several methods with the same name in the same file.        |

***

### Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://www.gitbook.com/cdn-cgi/image/dpr=2,width=760,onerror=redirect,format=auto/https%3A%2F%2Fcodium.ai%2Fimages%2Fpr_agent%2Fimprove_component1.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://www.gitbook.com/cdn-cgi/image/dpr=2,width=760,onerror=redirect,format=auto/https%3A%2F%2Fcodium.ai%2Fimages%2Fpr_agent%2Fimprove_component2.png" alt=""><figcaption></figcaption></figure>
