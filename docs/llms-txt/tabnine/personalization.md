# Source: https://docs.tabnine.com/main/welcome/readme/personalization.md

# Personalization

## What is personalization and why does it matter?

Tabnine’s AI code assistant — including its code completions and chat — is backed by Tabnine’s Universal AI models, which were trained on permissively licensed open source code. Like other LLMs, the Universal models were **not** **exposed to the specific data and distinctive patterns** of an organization. Consequently, they lack the context and domain knowledge that an experienced developer at an organization has, resulting in recommendations that often aren’t tailored to the developers.

Personalization is an added layer of Tabnine’s AI coding assistant that closes this gap and aims to solve the problem by increasing Tabnine's contextual awareness in three ways:

1. **Context** through local code awareness
2. **Connection** to software repository for global code awareness
3. **Customization** of an AI model

The different layers of personalization enable Tabnine’s AI coding assistant to return code suggestions, including tests, explanations, documentation, and more that are more accurate and relevant to your needs.

{% embed url="<https://youtu.be/nWXRaozjHnM>" %}

## How does Tabnine solve the personalization problem?

Tabnine uses several components to make its AI coding assistant aware of your environment. Different techniques are applied for code completions and chat; some are only available for Tabnine Enterprise plans.

* **Context through local code awareness (General availability):** Tabnine accesses information available in a developer’s local IDE workspace, applying different methods to do so: context from the open file and related files, information on types in the current scope, and **retrieval-augmented generation (RAG)**. [RAG](https://docs.tabnine.com/main/welcome/readme/tabnines-personalization-in-depth#rag-in-tabnine) is the most effective component for all Pro and Enterprise customers. Context through local code awareness is beneficial for any individual developer and for those within a team or a big organization.
* **Connection for global code awareness (Private Preview):** Tabnine leverages the information available in the organization's code repositories, including relevant code that isn't accessible in the local IDE. [RAG](https://docs.tabnine.com/main/welcome/readme/tabnines-personalization-in-depth#rag-in-tabnine) is the main method used to achieve this. This feature is available in Private Preview as an option for Enterprise Customers. The team admin needs to explicitly enable this feature by connecting Tabnine to the desired repos in the organization codebase. This is beneficial mainly for developers in organizations.
* **Customization (AI models fine-tuned with private code):** Tabnine leverages the information available in the whole codebase of the organization (with the admin controlling which repos will be included) through a private customized model that was retrained on the organization’s private code, making the core AI model aware of the organizational code pattern and reflecting the specific languages and frameworks used in the organization. This option is for Enterprise customers with private installation and is beneficial for larger organizations with a bespoke codebase.

These techniques and mechanisms can be applied individually or together for code completions and chat to achieve the optimal solution for each end user or organization.

## Personalization and code privacy

Code privacy is our utmost priority. The personalization layer maintains all of Tabnine’s code privacy principles:

* Your code remains private
* Tabnine does not share any of your code with third parties.
* Tabnine does not train on your code.

There are two cases when your code is sent to the Tabnine server (in Tabnine’s secure SaaS or the customer's private installation):

* **AI model inference:** When the user queries Tabnine (explicitly or implicitly), a prompt is sent to the AI model in the Tabnine server with a context window that includes some elements from your code. The sole purpose of the context window is to facilitate the most accurate answers possible.
* **Creating the chat RAG index:** The computation for vector embeddings for the chat [RAG index](https://docs.tabnine.com/main/welcome/readme/tabnines-personalization-in-depth#the-rag-index) requires a lot of resources, and cannot be done locally without stressing the user’s machine. Tabnine performs this computation on the server GPU.

In both cases, the data is sent encrypted over SSL and is deleted immediately after returning the answer.

For global RAG, the index is retained on Tabnin servers.

Clarification about customization (an option for Tabnine Enterprise customers): Training and hosting the private customized model is done in the customer’s isolated private installation, which ensures no data is shared outside the organization.

## Personalization in Tabnine's UI

Most of the personalization impact is in the quality of the code suggestions. However, there are some UI-related ways that personalization shows up.

#### Mentions

Mentions (using the @ symbol) are a way that the user can specifically ask the Tabnine Chat to use a specific code element (type, method, or class) from the workspace in the query context. Mentions allow users to leverage their domain knowledge and help the AI by explicitly focusing it on relevant context from the workspace.

Note:

1. Mentions work for each language with a Language Server Protocol (LSP) support in the IDE.
2. Type 2-3 characters after the “@” to view the available code elements.

<figure><img src="https://lh7-us.googleusercontent.com/GGPIQKx9s7OsJxM_EbVoT1J3hRxOIm-MEJSi2NS9g92P9tpFdvPJv3qDWciBvXzNXqi6lazY15dkjyts80qP8VZRCKVl49NwroZjuPkn9r-TWydTX_ekIu25gJVMKetBlnQq3l9X2x2AlzMG05KGbW4" alt="" width="563"><figcaption></figcaption></figure>

#### References

If the context for local code awareness is enabled, by default Tabnine Chat tries to answer the user questions with context from the local workspace. When returning the answer to the user, Tabnine Chat is explicit about the context used to answer the question by including a list of references:

<figure><img src="https://lh7-us.googleusercontent.com/y-xyv2jZeBa-OTtLRiGAuhsu47FbsA288s8kLnMdoZbIbA2-Oq87dYIMRdyZuNmHTKsD83enhmcgXkTeqVfcYpBBLY4vPTTcoDiu3gLawUJJGgzuuCpoatu2hEdFtBcDlwrpAg6fChrydUTrURB7ons" alt="" width="563"><figcaption></figcaption></figure>

You can click each reference and get to the full code that was induced in the chat context.

#### Workspace selector

Tabnine Chat includes a **Workspace** toggle button that indicates to the user whether or not context is being used for the workspace (i.e., in the folders that are open in the IDE). If the context for local code awareness is enabled, the Workspace toggle is on by default.

If you’re not interested in an answer that relies on your workspace, you can simply toggle it off.

<figure><img src="https://lh7-us.googleusercontent.com/-9iF4iVwFN2ialWmEsKxjNpgKAvAFcc-xqqb8cPPTRxe1nI6iTdhWqTi7U2yQKy9lUVpB3yfpwgTcJm5CtiN5Ubc3Jft_nce0fkDW9RyMewtEzqLUSS_oeYzhF58F6tjV2_gd5d7VfjgvCSJOA__id8" alt="" width="563"><figcaption></figcaption></figure>

## Personalization availability matrix

<table data-full-width="true"><thead><tr><th width="176"></th><th>Context through local code awareness</th><th>Connection for global code awareness</th><th>Customization for AI models</th></tr></thead><tbody><tr><td>Product milestone</td><td>General availability</td><td><p>Private preview</p><p>(<a href="https://www.tabnine.com/contact-us/?utm_source=docs&#x26;utm_medium=organic&#x26;utm_campaign=docs">Contact your Sales</a> rep to learn more)</p></td><td>General availability</td></tr><tr><td>Tabnine Pro</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Tabnine Enterprise</td><td>Yes</td><td>Yes*</td><td>Yes (Private installation only)</td></tr><tr><td>Scope</td><td>Local IDE workspace</td><td>Selected repos from the organization's codebase*</td><td>Selected repos from the organization's codebase**</td></tr><tr><td>Code completions</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td>Chat</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>IDEs</td><td>VS Code, JetBrains, Visual Studio, Eclipse**<br></td><td>VS Code, JetBrains, Visual Studio, Eclipse**<br></td><td>VS Code, JetBrains, Visual Studio, Eclipse<br></td></tr><tr><td>Languages</td><td>All supported languages</td><td>All supported languages</td><td>All supported languages</td></tr></tbody></table>

\* For connection and customization, the team admin explicitly selects the specific repos.

\*\* For private installation, Visual Studio and Eclipse are supported from release 5.2.

### Do I need to enable the feature? Can I disable the feature?

**Context for code completions:**

* **All plans:** Enabled by default and cannot be switched off

**Context for Chat:**

* **Pro:** Enabled by default and cannot be switched off
* **Enterprise:** Enabled by default; the team admin can switch it off

**Note:** Users can use the [Workspace selector](#workspace-selector) to disable the context and connection for a specific query.

**Connection and customization**

* These options for Enterprise customers are off by default and the team admin needs to explicitly connect to each repo in the organization codebase.

### Enabling context through local code awareness in Tabnine Enterprise

Context through local code awareness using RAG **for code completions** is enabled for all Enterprise users, and cannot be turned off.

However, context through local code awareness using RAG **for Tabnine Chat** for all users is controlled by the team admin:

**Enterprise (SaaS)**

Enabled by default; the team admin can switch it off for the whole team.\\

To enable/switch it off, the Enterprise team admin should go to the [Personalization screen](https://app.tabnine.com/profile/personalization) on the Tabnine app and enable **Workspace indexing**.

Note: It can take up to one hour to populate the end users’ IDEs.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b3817330a6c9973294a874f947e3e3a4400d56b0%2Fsaas%20ent%20admin%20personalization.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

**Enterprise (private installation)**

Enabled by default; the team admin can switch it off for the whole team using the admin console
