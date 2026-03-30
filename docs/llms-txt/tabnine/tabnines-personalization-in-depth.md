# Source: https://docs.tabnine.com/main/welcome/readme/personalization/tabnines-personalization-in-depth.md

# Tabnine’s Personalization in Depth

## **Background**

The main approach Tabnine uses to return code suggestions that are more accurate and relevant for your code is to enrich the context sent to the AI with additional relevant information from the user’s code.

The additional information comes from several sources, including code from the currently open file, related or recently viewed files, chat conversion history, and more, but the most important method is **retrieval-augmented generation (RAG)**.

RAG is used both for **context** through local code awareness and **connection** to your organization's codebase.

## **RAG in Tabnine**

RAG is a common AI framework for improving the accuracy of LLM-generated answers by adding an information retrieval component that adds data and context to each query of the model.

RAG's implementation has two components:

1. **Indexing —** Tabnine builds RAG indices that enable fast and effective retrieval of relevant data. These indices are for code completions and chat, based on local code or global code, and are based on all the code in the IDE workspace or the organization’s global codebase.
2. **Querying —** With each user query to Tabnine (explicit or implicit), Tabnine retrieves relevant code context from the RAG index and adds it as a context to the prompt to the AI model. The result is a more accurate code suggestion from Tabnine, which is more relevant to the user codebase.

The following illustrates the process of a user query to Tabnine, with the personalization layer of querying from the RAG indices, in **context** through local code awareness and **connection** to your organization codebase.

<figure><img src="https://lh7-us.googleusercontent.com/v_8AG30VcLDGzkZw4tj825lr00qLwsSp0N8vtuFuYK0po19hOkHYVX3QxsuxVSAeglxt7ojL4WRD1dyaR-TfK0Eps1lKfUWB3sbqcv3fGnTSkLnHEOdUFUG1Mv5BJuBXpdIrY7Vc5HAXtENWfZjUSeQ" alt=""><figcaption><p>Context through local code awareness</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/m4_ysoivQET4Ux31SYFNebc6X2QGXyH0vvUjRpJzn2ocY8EbOAkFKN_JuaEVzvFy1Vv6nWXaXcrF23KbeI_K2Vq5VkdfdgHttXQE-h0mI-Y1UGTwrj6y153U5Shjn0-Q6J0g7f237hjHsjLYBpg1gKw" alt=""><figcaption><p>Connection for <em>global</em> code awareness</p></figcaption></figure>

### **The RAG Index**

#### Types and Scope of Indices

Tabnine uses RAG for both 1) **context** through local code awareness and 2) **connection** to your organization's codebase. There are different RAG indices for code completions and chat. The code representation in each index is different and fits its relevant AI model.

Additionally, the scope of the indices can be either local or global:

1. **Local** means that Tabnine builds the index based on the IDE workspace of each developer.
2. **Global** means that Tabnine builds the index based on the whole codebase of the organization.

Tabnine’s RAG indices provide:

* **Context** through local code awareness for code completions
* **Context** through local code awareness for chat
* [**Connection**](https://docs.tabnine.com/main/welcome/readme/personalization/connection-global-codebase-awareness) to your organization codebase for chat

#### What files are being indexed?

{% hint style="warning" %}
Everything said here about `.tabnineignore` and `.gitignore` files is relevant ***only*** to local indexing, ***not*** remote indexing.
{% endhint %}

Tabnine’s RAG indices include all files in the scope that meet these criteria:

* File extensions from this [table](https://github.com/codota/TabNine/blob/master/languages.yml) (there are *1,233 different extensions* listed here)
* Files with extensions other than: "`md`", "`yaml`", "`yml`", "`json`", "`lock`", "`xml`", "`gradle`", "`bash`", "`sh`", "`txt`", "`csv`".

{% hint style="info" %}
As of 5.23.0, all these filetypes with these extensions can be incorporated as remote files referenced by [Context Scoping](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping): `.md, .mkd, .mdwn, .mdown, .mdtxt, .mdtext, .markdown, .yaml, .yml, .json, .xml, .gradle, bash, .sh, .txt, .ini, .properties, .prefs, .cfg, .cmake`
{% endhint %}

#### Controlling Local Workspace Indexing

Additionally, Tabnine's RAG includes files not listed in any files with the extensions `.tabnineignore`, `.ignore`, and`.gitignore.`

{% hint style="info" %}
The `.tabnineignore` file supports all the same patterns and expressions that a `.gitignore` file supports. See [documentation](http://git-scm.com/) on `.gitignore` syntax.
{% endhint %}

#### Index Life Cycle

The **context** through local code awareness indices (Completions and Chat) are created from scratch upon the first time Tabnine runs on the workspace.

After the index is built, changes are monitored and the indices are incrementally updated.

The **connection** to your organization codebase index is created after the team admin connects the repos from the customer codebase to Tabnine; it is updated regularly.

#### Indexing Process

The RAG indexing applies vector embeddings for each chunk of code in the scope (local or global).

For Code Completions, the RAG index computation runs locally on the developers’ machines.

For Chat, the RAG index computation requires *a lot* of resources. As such, it requires a GPU, which means it cannot be done locally without stressing the end user’s machine. Tabnine performs just this computation on the Tabnine server GPU (SaaS or the customer's private installation).

Your code remains private. Chunks of code are sent in an encrypted format, and Tabnine does not share your data with any third parties. The sole purpose of sending these code chunks is to compute the vector representation for indexing.

#### Index Location and Persistence

* **Local RAG (Context)**
  * The indices for Code Completions and Chat suggestions are saved on the end user’s local machine.
  * The vector database used locally is **Quadrant**.
* **Global RAG (Connection)**
  * The indices are retained on Tabnine servers.

#### Integrations for connection to your organization's codebase

Tabnine can integrate with the leading git-hosting platforms such as GitHub, GitLab, or Bitbucket. The integration keeps the existing permission models or the organization so that each user can only retrieve code from repositories that they have access to.

### VDB on Docker

Tabnine indexes the user’s codebase into a VDB embedding store (vector database) locally in memory.

Docker containerization for VDB: Achieve better resource allocation and system stability when processing your codebase. Activate by setting the `TABNINE_DOCKER_ENABLED` environment variable.

#### VDB Logs

If you have any indexing issues, please send us all the VDB logs in the relevant log folder. The logs are located in:

<table data-header-hidden><thead><tr><th width="119.68011474609375"></th><th></th></tr></thead><tbody><tr><td><strong>Platform</strong></td><td><strong>Path</strong></td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-162ed82d77744806c2aba64ef9a70a80c3e66d56%2Fmacos.png?alt=media" alt="" data-size="line">MacOS</td><td>/Users/{UserName}/Library/Application Support/TabNine/servers/vdb/1.7.3-fix.1/logs</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-094a4a86d9eede964e0367ecc9372e77542ad5ea%2Flinux.png?alt=media" alt="" data-size="line">Linux</td><td>~/.local/share/TabNine/servers/vdb/1.7.3-fix.1/logs</td></tr><tr><td><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f7c9731c7a83ba2d75b0d17864d12091461bf38e%2FWindows_logo_-_2021.svg.png?alt=media" alt="" data-size="line"> Windows</td><td>C:\Users\{UserName}\AppData\Roaming\TabNine\servers\vdb\1.7.3-fix.1\logs</td></tr></tbody></table>

{% hint style="info" %}
**\* {UserName}** = current user name on your machine
{% endhint %}
