# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/generate-labels.md

# Generate Labels

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab
{% endhint %}

The `generate_labels` tool analyzes the PR code changes and automatically suggests relevant labels, based on a list of predefined labels and their descriptions.

## How to use the `generate_labels` tool

**Manual usage**

Comment on the PR:

```
/generate_labels
```

### **Enabling custom labels**

There are 3 ways to enable custom labels:

#### **1. CLI (local configuration file)**

When working from CLI, you need to apply the [configuration changes ](#configuration-options)to the [custom\_labels file](https://github.com/Codium-ai/pr-agent/blob/main/pr_agent/settings/custom_labels.toml).

#### **2. Repository configuration file**

To enable custom labels, you need to apply the [configuration changes](#configuration-options) to the local `.pr_agent.toml` file in your repository.

#### **3. Handle custom labels from the repo's labels page**&#x20;

{% hint style="info" %}

### Platforms supported: GitHub, GitLab <a href="#self-review" id="self-review"></a>

{% endhint %}

* **GitHub:** `https://github.com/{owner}/{repo}/labels`, or click the **Labels** tab in the issues or PR's page.
* **GitLab:** `https://gitlab.com/{owner}/{repo}/-/labels`, or click **Manage** and then **Labels** from the left menu.

### Adding custom labels

Custom labels should be formatted as:

* **Label name**: The name of the custom label.
* **Description**: Start the description with prefix `pr_agent:`, for example: `pr_agent: Description of when AI should suggest this label`.\
  The description should be comprehensive and detailed, indicating when to add the desired label.

<figure><img src="https://codium.ai/images/pr_agent/add_native_custom_labels.png" alt="" width="563"><figcaption></figcaption></figure>

### Using `generate_labels`

After adding labels, they will be available for generation in `generate_labels`.

* Set `enable_custom_labels` to `True`: This will turn off the default labels and enable the custom labels provided in the `custom_labels.toml` file.
* Add the custom labels. It should be formatted as follows:

```
[config]
enable_custom_labels=true

[custom_labels."Custom Label Name"]
description = "Description of when AI should suggest this label"

[custom_labels."Custom Label 2"]
description = "Description of when AI should suggest this label 2"
```

## Example usage <a href="#example-usage" id="example-usage"></a>

If we wish to add detect changes to SQL queries in a given PR, we can add the following custom label along with its description:

<figure><img src="https://codium.ai/images/pr_agent/custom_labels_list.png" alt="" width="563"><figcaption></figcaption></figure>

When running the `generate_labels` tool on a PR that includes changes in SQL queries, it will automatically suggest the custom label:

<figure><img src="https://codium.ai/images/pr_agent/custom_label_published.png" alt="" width="563"><figcaption></figcaption></figure>

Note that in addition to the dedicated tool `generate_labels`, the custom labels will also be used by the `describe` tool.
