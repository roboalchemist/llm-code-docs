# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/features/qodo-aware-rag.md

# Qodo Context Engine

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
This feature is available for [Enterprise users](https://www.qodo.ai/pricing/) only.

**Platforms supported:** GitHub, GitLab, Bitbucket Data Center
{% endhint %}

## What is Qodo Context Engine?

Qodo Context Engine is the code intelligence engine behind the Qodo platform. It connects to all your repos, analyzes architecture and patterns, and powers AI agents that help you search, understand, and solve technical problems.

Think of it as an AI-powered Principal Engineer, that understands your entire system and helps you move faster with confidence.

### Why should I use it?

When used with Qodo Git interface, Qodo Context Engine brings deep, architecture-level understanding directly into your review workflow.

You ask the questions, and Qodo Context Engine finds the answers from across your entire codebase.

### How does it work?

Qodo Context Engine uses Retrieval-Augmented Generation (RAG) and agentic reasoning to understand your codebase:

* **Indexing** – Builds a deep internal map of your code
* **Retrieval** – Pulls relevant code, docs, and patterns
* **Reasoning** – AI agents analyze dependencies and logic
* **Generation** – Produces grounded, accurate responses

***

## Using Qodo Context Engine <a href="#applications" id="applications"></a>

In order to enable the RAG feature, add the following lines to your [configuration file](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/configuration/configuration-file):

```toml
[rag_arguments]
enable_rag=true
```

{% tabs %}
{% tab title="/ask" %}
The [`/ask`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/ask) tool can access broader repository context through the RAG feature when answering questions that go beyond the PR scope alone.

The **References** section displays the additional repository content consulted to formulate the answer.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FzHTtmmsKmAiYM6bvjLJ7%2Fimage.png?alt=media&#x26;token=3deaa122-0127-4702-83ae-8aa8e1be7b1f" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="/compliance" %}
The [`/compliance`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/compliance) tool offers the *Codebase Code Duplication Compliance* section which contains feedback based on the RAG references. This section highlights possible code duplication issues in the PR, providing developers with insights into potential code quality concerns.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FSwjrP9CSUj26GL3kQYcR%2Fimage.png?alt=media&#x26;token=7e997284-4cc1-4c17-828b-28ef00b680b2" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="/implement" %}
The [`/implement`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/implement) tool utilizes the RAG feature to provide comprehensive context of the repository codebase, allowing it to generate more refined code output.

The **References** section contains links to the content used to support the code generation.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FEz5FU3ADkLKjrZtQiHUM%2Fimage.png?alt=media&#x26;token=f2c2002e-a7d2-4e2b-8d1f-46743b2863b2" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="/review" %}
The [`/review`](https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/tools/tools-list/review) tool offers the **Focus area** which contains feedback based on the RAG output.

The complete list of references found relevant to the PR will be shown in the **References** section, helping developers understand the broader context by exploring the provided references.

<figure><img src="https://4090466057-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzLhdlSjTSQhS3ANJsKST%2Fuploads%2FBqeIoCSiMLrLSKGQHgfh%2Fimage.png?alt=media&#x26;token=34801f15-ebfc-41c4-9391-101481024234" alt="" width="375"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

***

## Configuration options <a href="#configuration-options" id="configuration-options"></a>

| Possible configurations | Default value                                | What does it do                                                                                                                                                                                                                              |
| ----------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enable_rag`            | `false`                                      | If set to true, repository enrichment using RAG will be enabled.                                                                                                                                                                             |
| `rag_repo_list`         | The repository from which the PR was opened. | <p>A list of repositories that will be used by the semantic search for RAG.</p><p>Use <code>\['all']</code> to consider the entire codebase, or a select list of repositories.</p><p>For example: <code>\['my-org/my-repo', ...]</code>.</p> |
