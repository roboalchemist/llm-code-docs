# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file/additional-context.md

# Additional Context

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

## Custom Context Files

### Overview

Modern AI coding assistants work best when they understand the specific context of your project. By adding custom context files to your repository, you can provide the AI agent with essential information about your codebase, development practices, and project-specific requirements.

{% hint style="info" %}
Context files help the agent generate more accurate, relevant, and high-quality suggestions tailored to your team's needs.
{% endhint %}

### Supported File Formats

The AI agent automatically recognizes and processes several standard context file formats when they're placed in the root directory of your main branch:

| File Name   | Purpose                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `agents.md` | General-purpose context file for AI coding assistants ([learn more about the agents.md standard](https://agents.md/?utm_source=chatgpt.com)) |
| `qodo.md`   | Context specific to Qodo-based AI tools                                                                                                      |
| `claude.md` | Context optimized for Claude AI integration                                                                                                  |

> **Warning:** Context files must be placed in the **root directory** of your **main branch** to be detected by the AI agent.

### What to Include

Context files can contain various types of information to guide the AI agent:

#### Architecture and Design Patterns

* Overview of your system architecture
* Design patterns and principles your team follows
* Key technical decisions and their rationale

#### Coding Standards

* Language-specific style guidelines
* Naming conventions for variables, functions, and classes
* Code organization preferences

#### Development Workflow

* Testing requirements and strategies
* Code review expectations
* Deployment considerations

#### Project-Specific Information

* Domain knowledge and business logic
* Common patterns used across the codebase
* Dependencies and their purposes
* Known limitations or technical debt

### Best Practices

{% tabs %}
{% tab title="Keep It Concise" %}
Focus on key information impacting code suggestions. Avoid redundant details.
{% endtab %}

{% tab title="Update Regularly" %}
Regularly review and update context files for current information.
{% endtab %}

{% tab title="Use Clear Language" %}
Write clear, direct instructions for specific, actionable guidance.
{% endtab %}

{% tab title="Prioritize Impact" %}
Prioritize context that significantly affects code quality and productivity.
{% endtab %}
{% endtabs %}

### Getting Started

#### Enable the Feature

Before adding context files, you need to enable this feature in your Qodo configuration file:

```toml
[config]
add_repo_metadata = true
```

#### Custom File Names

You can also specify custom file names for your context files using the configuration:

```toml
[config]
add_repo_metadata_file_list = ["file1.md", "file2.md", ...]
```

This allows you to use your own naming convention or include multiple context files tailored for different purposes.

{% hint style="info" %}
**Info:** Learn more about the Qodo Merge configuration file in the [configuration Documentation](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).
{% endhint %}

#### Add Your Context File

Follow these steps to add a context file to your repository:

1. Enable `add_repo_metadata` in your Qodo Merge configuration file
2. Create one of the supported context files (`agents.md`, `qodo.md`, or `claude.md`) in your repository's root directory
3. Add relevant context about your project, starting with your most important guidelines
4. Commit the file to your main branch
5. The AI agent will automatically detect and use this context in future interactions

{% hint style="success" %}
By investing time in creating comprehensive context files, you'll see immediate improvements in the quality and relevance of AI-generated code suggestions.&#x20;
{% endhint %}
