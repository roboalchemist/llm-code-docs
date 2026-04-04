# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/analyze.md

# Analyze

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

The `analyze` tool combines static code analysis with LLMs to identify the methods, functions, and classes changed in a PR.

The tool scans the PR code changes, identifies code components that changed, and for each component lets you interactively generate tests, documentation, code suggestions, and find similar code.

The `analyze` tool supports the programming languages: Python, Java, C++, JavaScript, TypeScript, C#.

## How to use the `analyze` tool

**Manual usage**

Comment on the PR:

```
/analyze
```

### Interactive options

After using the `analyze` tool, you can immediately trigger component-level actions and apply changes with a few interactive options:

* Interactive checkboxes to generate tests, documentation, and code suggestions for specific components
* On-demand similar code search that activates when a checkbox is clicked
* Component-specific actions that trigger only for the selected elements, providing focused assistance

## Example usage <a href="#example-usage" id="example-usage"></a>

<figure><img src="https://codium.ai/images/pr_agent/analyze_1.png" alt="" width="563"><figcaption></figcaption></figure>
