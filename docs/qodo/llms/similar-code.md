# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/similar-code.md

# Similar Code

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub
{% endhint %}

The similar code tool retrieves the most similar code components from inside the organization's codebase, or from open-source code.

## How to use the `similar code` tool

**Manual usage**

Comment on the PR:

```bash
/find_similar_component COMPONENT_NAME
```

Where `COMPONENT_NAME` is the name of a code component in the PR (class, method, function).

You can set a specific class or file  where the component will be taken from:

```bash
/find_similar_component COMPONENT_NAME --pr_find_similar_component.file=FILE_NAME
```

**Automatic usage**

To run the tool automatically, use the [`analyze`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/analyze) tool. On a PR, comment:

```bash
/analyze
```

For the components you want to find similar code, click the `similar` checkbox.

<figure><img src="https://codium.ai/images/pr_agent/analyze_similar.png" alt="" width="563"><figcaption></figcaption></figure>

You can search for similar code within your organization’s codebase or globally, across open-source projects. Each result includes the matching code and its license information.

<figure><img src="https://codium.ai/images/pr_agent/similar_code_global.png" alt="" width="563"><figcaption></figcaption></figure>

### Search results

Each search result includes:

* `extracted keywords`: Keywords identified in your code. Clicking the link to view the keywords and adjust the search if needed.
* `search context`: The context in which the tool looks for similar code, either inside your organization’s repositories or across public open-source projects (Global).
* `similar code`: Matching code snippets found in the selected search context. Click the link to open the code component in the relevant file.
* `relevant repositories`: Open-source repos that contain code related to your component and its keywords.

***

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

Configure the `similar code` tool by setting configurations under the `pr_find_similar_component` part in your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file).

<table><thead><tr><th width="257.36328125">Possible configurations</th><th width="222.34765625">Default value</th><th>What they do</th></tr></thead><tbody><tr><td><code>search_from_org</code></td><td><code>false</code></td><td><p></p><p>if set to true, the tool will search for similar code in the organization's codebase</p></td></tr><tr><td><code>number_of_keywords</code></td><td><code>5</code></td><td>number of keywords to use for the search.</td></tr><tr><td><code>number_of_results</code></td><td><code>5</code></td><td>the maximum number of results to present</td></tr></tbody></table>

***

## Example usage

`Global Search` for a method called `chat_completion`:

<figure><img src="https://codium.ai/images/pr_agent/similar_code_global2.png" alt="" width="563"><figcaption></figcaption></figure>

Search result link example:

<figure><img src="https://codium.ai/images/pr_agent/code_search_result_single.png" alt="" width="563"><figcaption></figcaption></figure>

`Organization Search`:

<figure><img src="https://codium.ai/images/pr_agent/similar_code_org.png" alt="" width="563"><figcaption></figcaption></figure>
