# Giselles Documentation

Source: https://docs.giselles.ai/llms-full.txt

---

# Account FAQ
Source: https://docs.giselles.ai/en/faq/account-billing/accounts

Frequently asked questions about Giselle accounts

TBD


# Billing FAQ
Source: https://docs.giselles.ai/en/faq/account-billing/billing

Frequently asked questions about billing and payments for Giselle

TBD


# Plan FAQ
Source: https://docs.giselles.ai/en/faq/account-billing/plan

Frequently asked questions about Giselle plans and features

TBD


# AI Models FAQ
Source: https://docs.giselles.ai/en/faq/application/ai-models

Frequently asked questions about AI models and their usage in Giselle

TBD


# Workspace FAQ
Source: https://docs.giselles.ai/en/faq/application/workspaces

Frequently asked questions about Giselle workspaces

TBD


# Privacy & Security FAQ
Source: https://docs.giselles.ai/en/faq/security-support/privacy-security

Frequently asked questions about Giselle7s privacy and security measures

TBD


# Support FAQ
Source: https://docs.giselles.ai/en/faq/security-support/support

Frequently asked questions about Giselle support services

TBD


# Action Node
Source: https://docs.giselles.ai/en/glossary/action-node

Learn how Action Nodes in Giselle enable your workflows to interact with external services like GitHub, performing tasks such as creating issues, comments, or retrieving discussions in your repositories.

## Action Node in Giselle

**Action Node** empowers your Giselle workflows to connect with and control external services. It acts as a bridge, allowing you to automate tasks beyond the Giselle environment. Currently, the primary integration is with **GitHub**, enabling a variety of repository operations. We are continuously working to expand support for more external services.

### GitHub Action

The GitHub Action capability within the Action Node allows your workflows to perform specific operations in your GitHub repositories. This is useful for automating tasks like issue creation, commenting, retrieving data, and more, based on the logic and data processed within your Giselle flow.

#### Setting up a GitHub Action:

1. **Select GitHub Account/Organization**:
   * Upon adding an Action Node and choosing GitHub as the service, you'll first need to select the GitHub account or organization where your target repository resides (e.g., `giselles-ai`, `liam-hq`).

2. **Choose a Repository**:
   * Next, a list of repositories accessible under the selected account/organization will appear (e.g., `docs`, `giselle`).
   * Click the **Set up** button next to the repository you want the action to target (e.g., `giselle`).

3. **Choose the GitHub Action to Perform**:
   * Once a repository is selected (e.g., `giselles-ai/giselle`), you'll need to specify what action the Giselle's app should execute.
   * Click on the dropdown menu, which might be labeled "Choose what action you want to perform."
   * Select the desired action from the list. Examples include:
     * **Create Issue**
     * **Create Issue Comment**
     * **Create Pull Request Comment**
     * **Reply Pull Request Review Comment**
     * **Get Discussion**
   * After selecting an action, click the **Setup Action** button to proceed to parameter configuration.

4. **Configure Action Parameters**:
   * Each GitHub action requires specific parameters to execute correctly. For instance, the "Create Issue Comment" action requires an `issueNumber` and a `body` for the comment, as indicated by "Required" fields.
   * The configuration panel will display the selected repository and the chosen action (e.g., "Create Issue Comment"). Below this, the necessary parameters will be listed.
   * For each parameter, you'll need to provide a value. This can often be done by:
     * Entering a static value directly.
     * **Selecting a Source**: This allows you to map data dynamically from the outputs of previous nodes in your flow or from the Giselle's app flow's initial trigger inputs. The "Select Source" option next to each parameter field facilitates this.
   * Ensure all parameters marked as "Required" are filled in.
   * Once all parameters are configured, the changes are typically saved by an "Action" button or similar confirmation in the UI. The node on the canvas will update to reflect the configured action (e.g., showing "Create Issue Comment" with inputs for `issueNumber` and `body`).

#### Output of the Action Node:

After successfully performing its task, an Action Node will typically produce an **output**. This output can contain information relevant to the action performed, such as the ID or URL of a created issue or comment, or the data retrieved from a service (like discussion content). This output can then be used as input by subsequent nodes in your workflow, enabling complex chains of operations. The node preview often indicates the availability of an "output".

#### Example: Creating an Issue Comment

Imagine you've configured an Action Node to "Create Issue Comment" for the `giselles-ai/giselle` repository:

* **Repository**: `giselles-ai/giselle`
* **Action**: Create Issue Comment
* **Required Parameters (Inputs)**:
  * `issueNumber`: Sourced from a workflow trigger or a previous node (e.g., an issue number identified earlier in the flow).
  * `body`: Sourced from another node (e.g., a text summary generated by an AI model in a preceding step).
* **Execution**: When this node runs, it will post a new comment using the provided `body` to the issue specified by `issueNumber` within the `giselles-ai/giselle` repository.
* **Potential Output**: The node might output details like the URL or ID of the newly created comment, which can be used in further steps.

#### Example: Replying to a Pull Request Review Comment

Here's how you might configure an Action Node to "Reply Pull Request Review Comment" in the `giselles-ai/giselle` repository, as shown in the provided image:

* **Repository**: `giselles-ai/giselle`
* **Action**: Reply Pull Request Review Comment
* **Required Parameters (Inputs)**:
  * `pullNumber`: The number of the pull request containing the review comment. This would typically be sourced from a trigger event (e.g., a GitHub Trigger for "Pull Request Review Comment Created") or a previous node that identified the pull request.
  * `commentId`: The ID of the specific review comment to which you are replying. This also would likely come from the trigger data or a preceding node that fetched comment details.
  * `body`: The content of your reply. This could be static text, or more powerfully, dynamically generated text from an AI node in your workflow (e.g., an automated acknowledgment, a question, or a summary).
* **Execution**: When this Action Node executes, it will post the content from the `body` parameter as a reply to the specified `commentId` on the given `pullNumber` within the `giselles-ai/giselle` repository.
* **Potential Output**: The node may output information about the reply that was posted, such as its own ID or URL, which could be useful for further conditional workflow logic.

#### Example: Getting a GitHub Discussion

This action allows your workflow to retrieve the content and details of a specific GitHub Discussion from your repository.

* **Repository**: `giselles-ai/giselle` (or any other configured repository)
* **Action**: Get Discussion
* **Required Parameters (Inputs)**:
  * `discussionNumber`: The number of the GitHub Discussion to retrieve. This can be a static value or sourced dynamically from a previous node's output or a trigger input.
* **Execution**: When this node runs, it connects to GitHub and fetches the details of the discussion specified by `discussionNumber` from the selected repository.
* **Potential Output**: The node will output an object containing the discussion data. This typically includes details such as the discussion's `id`, `title`, `bodyHTML` (the content of the discussion in HTML format), `createdAt`, `updatedAt`, `author` information, and an array of `comments` associated with the discussion (each comment also having details like `bodyHTML`, `author`, etc.). This structured data can then be used by subsequent nodes in your workflow, for example, to summarize the discussion, extract key points, perform analysis on the comments, or trigger other actions based on its content.

The Action Node, particularly with its GitHub integration, is a versatile tool for extending Giselle's automation capabilities into your software development and project management lifecycles. Stay tuned for more actions and integrations with other external services!


# AI Parameters
Source: https://docs.giselles.ai/en/glossary/ai-parameters

Dictionary of Generation Parameters Used Across AI Models in Giselle.

This document provides a detailed overview of common generation parameters ("Generation Parameters") that can be configured within Giselle's Generator Nodes to fine-tune outputs from various multimodal AI models such as Claude, Gemini, GPT-4o, Sonar, and Fal AI.

Please note that definitions and availability of generation parameters may vary depending on the AI provider and specific models. Additionally, Giselle does not currently implement all parameters supported by each provider's API. This document primarily covers general definitions and typical usages of the parameters that are available. If you have suggestions for parameters you would like Giselle to support, please feel free to contact us.

## Common AI Parameters

### Temperature

* **Definition:** Controls randomness in text or image generation.
* **Range:** 0 (less random, deterministic) to 1 (highly random, creative).
* **Recommended use:**
  * Lower values (0–0.3) for precise, factual outputs.
  * Higher values (0.7–1.0) for creative or exploratory outputs.

### Top-p (Nucleus Sampling)

* **Definition:** Limits token selection to the smallest set whose cumulative probability exceeds a threshold (p).
* **Range:** Typically 0.0 to 1.0.
* **Recommended use:**
  * Lower values (0.7–0.9) for focused, consistent outputs.
  * Higher values (\~1.0) for broader, diverse content generation.

### Max Tokens

* **Definition:** Maximum number of tokens generated in a response.
* **Recommended use:**
  * Adjust based on desired response length and API/model token limits.
  * Essential for cost management and resource optimization.

## Text-Specific Parameters

### Frequency Penalty

* **Definition:** Reduces repetition by penalizing repeated tokens.
* **Range:** Typically 0.0 (no penalty) to 1.0 (strong penalty).
* **Recommended use:**
  * Increase when repetitive outputs are undesirable.

### Presence Penalty

* **Definition:** Encourages new content by penalizing tokens previously used.
* **Range:** Typically 0.0 (no penalty) to 1.0 (strong penalty).
* **Recommended use:**
  * Helpful for generating more diverse text outputs.

### Stop Sequences

* **Definition:** Tokens or phrases indicating where the model should stop generating.
* **Recommended use:**
  * Define clearly when structured or partial outputs are required.

## Image Generation Parameters

### Guidance Scale

* **Definition:** Influences how closely the generated image follows the provided prompt.
* **Range:** Typically 1 (less strict adherence) to 20 (highly strict adherence).
* **Recommended use:**
  * Lower values for exploratory, abstract outputs.
  * Higher values for precise, detailed adherence to prompts.

### Inference Steps

* **Definition:** Number of steps in the diffusion process.
* **Recommended use:**
  * Lower values (1–4 steps with flux/schnell) for rapid prototyping.
  * Higher values (\~28 steps with stable-diffusion) for detailed, high-quality images.

## Multimodal Parameters

### Context Window

* **Definition:** Maximum tokens/models can "remember" or process at once.
* **Typical values:**
  * Gemini: up to 1M tokens.
  * GPT-4o: 128k tokens.
  * Claude: up to 200k tokens.
* **Recommended use:**
  * Use larger context windows for extensive documents, multimodal data analysis, and tasks requiring detailed understanding.

### Input Modalities

* **Definition:** Types of inputs supported by the model (text, images, audio, video).
* **Models:**
  * Gemini 2.5 Pro and GPT-4o support extensive multimodal inputs.
  * Choose models based on required input modalities.

## Web-Search Parameters

### Grounding

* **Definition:** Enables the model to incorporate real-time web-search results into generated responses.
* **Recommended use:**
  * Enable for up-to-date, fact-based research tasks or informational queries.

## Practical Recommendations for Giselle

* **Experimentation and Adjustment:** Regularly adjust parameters based on task-specific results.
* **Node Integration:** Use parameters strategically across chained nodes to maximize workflow effectiveness.
* **Document Settings Clearly:** Clearly document chosen parameter settings within your Giselle workflow for team clarity and reproducibility.


# Document Vector Store Node
Source: https://docs.giselles.ai/en/glossary/document-vector-store-node

Learn how the Document Vector Store Node enables you to upload and search documents using vector embeddings for AI-powered retrieval in your Giselle workflows.

## Document Vector Store Node in Giselle

The **Document Vector Store Node** is a specialized "Variable" node that creates a powerful, searchable knowledge base from uploaded documents. It works by processing your documents (PDFs, text files, and markdown) into vector embeddings, allowing AI models to perform semantic searches and retrieve relevant context for answering questions and generating responses.

This process uses advanced embedding models to convert your document content into vector embeddings. You can select from multiple embedding models, including OpenAI's [`text-embedding-3-small`](https://platform.openai.com/docs/models/text-embedding-3-small) (1536 dimensions) and [`text-embedding-3-large`](https://platform.openai.com/docs/models/text-embedding-3-large) (3072 dimensions). These vectorized data are then stored securely in Giselle's dedicated Vector Store.

### Setting up a Document Vector Store:

Before using the Document Vector Store Node in your workflow, you need to create and configure a vector store through your team settings:

1. **Navigate to Vector Store Settings**:
   * Go to **Settings > Team > Vector Stores** in your Giselle account.
   * You can access this page here: [https://studio.giselles.ai/settings/team/vector-stores/document](https://studio.giselles.ai/settings/team/vector-stores/document).

2. **Create a New Document Vector Store**:
   * Click the button to create a new document vector store.
   * Enter a descriptive name for your vector store (e.g., "Company Documentation" or "Product Manuals").

3. **Upload Documents**:
   * After creating the vector store, you can upload documents by clicking the upload area or dragging and dropping files.
   * **Supported File Types**: PDF (`.pdf`), Text (`.txt`), Markdown (`.md`)
   * **Maximum File Size**: 4.5 MB per file
   * You can upload multiple documents to build a comprehensive knowledge base.

4. **Document Processing**:
   * Once uploaded, documents are automatically processed through several stages:
   * **Text Extraction**: Text is extracted from PDFs and decoded from text files.
   * **Chunking**: Content is divided into manageable chunks (max 150 lines or 6000 characters per chunk, with 30-line overlap).
   * **Embedding Generation**: Each chunk is converted into vector embeddings using the selected embedding model.
   * **Storage**: Embeddings are stored with HNSW (Hierarchical Navigable Small World) indexes for fast similarity search.

5. **Monitor Processing Status**:
   * Each document shows its status: **Pending**, **Processing**, **Ready**, or **Failed**.
   * Wait for documents to reach the "Ready" status before using the vector store in your workflows.

### Adding a Document Vector Store Node to Your Workflow:

1. **Add the Node**:
   * From the toolbar at the bottom of the canvas, click the **Variable** icon.
   * Select **Document Vector Store** from the pop-up menu to add the node to your workspace.

2. **Configure the Vector Store**:
   * When first added, the node will display a "REQUIRES SETUP" status.
   * Select the node to open its configuration panel on the right.
   * Click the **Select a vector store** dropdown menu and choose the document vector store you created earlier.

3. **Select the Embedding Profile**:
   * After selecting a vector store, choose which embedding model to use for queries.
   * This must match one of the embedding profiles used when the documents were processed.
   * Available options typically include:
   * **text-embedding-3-small**: 1536 dimensions - Efficient and suitable for most use cases.
   * **text-embedding-3-large**: 3072 dimensions - Higher precision for complex semantic understanding.

4. **Finalize Setup**:
   * Once configured, the node on the canvas will update to show the name of the selected vector store.
   * The node is now ready to be connected to other nodes in your workflow.

### Supported File Types

The Document Vector Store supports multiple file types, each with specific size limits:

| File Type    | Supported Formats | Maximum Size | Common Use Cases                             |
| :----------- | :---------------- | :----------- | :------------------------------------------- |
| **PDF**      | `.pdf`            | 4.5MB        | Documentation, reports, manuals, articles    |
| **Text**     | `.txt`            | 4.5MB        | Plain text documents, logs, transcripts      |
| **Markdown** | `.md`             | 4.5MB        | Technical documentation, README files, notes |

### Usage in Workflows

The Document Vector Store Node is designed to be used in combination with a **Query Node**. It acts as the knowledge base that the Query Node searches through.

* **Connect the Output**: The "Output" of the Document Vector Store Node should be connected to the input of a Query Node.
* **Perform a Search**: The Query Node takes a user's question or dynamic input, searches the vectorized document content for the most relevant information, and passes that information to subsequent nodes (like a Generator Node) for processing, analysis, or summarization.

#### Example Workflow:

```
[Text Node: "What are the safety guidelines?"]
         ↓
[Query Node] ←── [Document Vector Store Node]
         ↓
[Generator Node: Summarizes safety guidelines based on search results]
```

### Query Parameters

When using a Query Node with the Document Vector Store, you can configure:

* **Max Results**: The maximum number of document chunks to return (default: 20, maximum: 100).
* **Similarity Threshold**: The minimum cosine similarity score for results (default: 0.3, range: 0-1). Higher values return only more relevant results.

### Output of the Node

The Document Vector Store Node's **output** is a reference to the vectorized data of your uploaded documents. This output provides the necessary connection for other nodes, like the Query Node, to access and search the document content.

### Managing Your Document Vector Stores

You can manage all your document vector stores from the team settings page:

* **Add Documents**: Upload additional documents to existing vector stores.
* **Monitor Status**: View the processing status of each document.
* **Remove Documents**: Delete documents that are no longer needed.
* **Delete Vector Stores**: Remove entire vector stores when they're no longer in use.

### Technical Considerations

* **File Size Limit**: The maximum file size per document is **4.5 MB** due to platform constraints.
* **Processing Time**: Larger documents or multiple simultaneous uploads may take longer to process.
* **Embedding Consistency**: Ensure you use the same embedding profile when querying that was used during document ingestion for optimal search results.
* **Concurrent Processing**: The system prevents duplicate processing through atomic claim mechanisms, ensuring each document is processed only once.

### Error Handling

If a document fails to process, possible reasons include:

* **Unsupported File Type**: Ensure your file is PDF, TXT, or MD format.
* **File Too Large**: Files exceeding 4.5 MB will fail to upload.
* **Extraction Failed**: PDFs with non-standard encoding or corruption may fail during text extraction.
* **Processing Errors**: Network issues or system errors during embedding generation.

When errors occur, you can re-upload the document or contact support if the issue persists.


# File Node
Source: https://docs.giselles.ai/en/glossary/file-node

Learn how the File Node in Giselle allows you to upload and use files like PDFs, images, and text as inputs for your AI workflows.

## File Node in Giselle

The **File Node** is a specialized type of "Variable Node" that allows you to handle file uploads and processing directly within your Giselle workflows. It acts as an input source, enabling you to incorporate documents, images, and text files for AI models to analyze, summarize, or transform.

### How to Use a File Node

1. **Add the Node**: Drag and drop a "File" node from the toolbar at the bottom of the canvas onto your workspace.
2. **Upload a File**: Select the node to open its configuration panel. You can upload a file by dragging and dropping it onto the designated area or by clicking to open a file selector.
3. **Monitor Status**: The node will display the status of the upload. Files can be in one of three states: "uploading," "uploaded," or "failed." Once successfully uploaded, the file is securely stored in your workspace and ready to be used in your workflow.

### Supported File Types

The File Node supports several types of files, each with specific use cases and limitations.

| File Type | Accepted Formats                                    | Max Size | Common Use Cases                               |
| :-------- | :-------------------------------------------------- | :------- | :--------------------------------------------- |
| **PDF**   | `application/pdf`                                   | 4.5MB    | Document processing, text extraction, analysis |
| **Image** | `image/png`, `image/jpeg`, `image/gif`, `image/svg` | 4.5MB    | Visual content analysis and generation         |
| **Text**  | `text/plain`, `text/markdown`                       | 4.5MB    | Text content processing and generation         |

### Workflow Integration

The primary purpose of a File Node is to provide data to other nodes, most commonly a [Generator Node](/glossary/generator-node).

* **Connect the Output**: The "Output" of a File Node can be connected to the input of a Generator Node.
* **Process the Content**: In the Generator Node, you can then prompt an AI model to perform a task on the file's content. For example, you can connect a PDF file and instruct the AI to "Summarize the key findings from the attached document."

#### Model Compatibility

The type of file you can connect depends on the capabilities of the target AI model. For example:

* **PDF and Text files** can be connected to text-based or multimodal models for tasks like analysis, summarization, or Q\&A.
* **Image files** can be connected to multimodal models that accept image inputs for analysis, or to image generation models for transformation tasks.

### Technical Limitations

Please be aware of the following limitations when using File Nodes:

* **Maximum File Size**: Due to platform constraints (Vercel Serverless Function limits), the maximum size for any single file upload is **4.5MB**.
* **Image Size Limit**: Image files have a maximum size of **4.5MB**.
* **Connection Restrictions**: You cannot connect a file to a node that does not support its type. For instance, a PDF file cannot be connected to a node that only generates images, and an image file may not be compatible with older text-only generation models.


# Generator Node
Source: https://docs.giselles.ai/en/glossary/generator-node

Learn how the Generator Node in Giselle uses AI models to generate text, images, and more, forming the core of your AI flows.

## Generator Node in Giselle

The **Generator Node** is the central component for AI-driven content creation in Giselle. It allows you to harness the power of various advanced AI models to generate text and images based on your instructions. By configuring prompts, selecting models, and providing tools, you can create highly customized outputs for any flow.

The Generator Node is configured through three main tabs in its settings panel: **Prompt**, **Model**, and **Tools**.

### Prompt Tab

This is where you provide the instructions for the AI model. Write a clear and detailed prompt describing the task you want the AI to perform. The output generated by the model will appear at the bottom of this panel, allowing you to quickly see the results.

You can also test the node individually by clicking the **Generate** button, which runs only this node without executing the entire flow.

### Model Tab

In the Model tab, you can select the specific AI model you want to use for the generation task. Giselle provides access to a wide range of models from leading providers.

* **Select a Model**: Choose from a list of available models, such as OpenAI's `gpt-4o`, Anthropic's `claude-4-opus`, or Google's `gemini-2.5-pro`.
* **Configure Parameters**: Depending on the selected model, you can adjust various [AI Parameters](ai-parameters) like `Temperature` or `Max Tokens` to fine-tune the output.

For more details on the available models from each provider, see our documentation:

* [Anthropic](https://docs.giselles.ai/models/providers/anthropic)
* [fal.ai](https://docs.giselles.ai/models/providers/fal)
* [Google](https://docs.giselles.ai/models/providers/google)
* [OpenAI](https://docs.giselles.ai/models/providers/openai)

### Tools Tab

The Tools tab allows you to grant the AI model access to external services, enabling it to perform actions or retrieve data from outside Giselle. This is useful for creating more dynamic and powerful flows.

Currently, the following tools are supported:

* [GitHub](/glossary/github-tools)
* [PostgreSQL](/glossary/postgresql-tools)

We are continuously working to add support for more tools in the future.

## Output of the Generator Node

The primary output of a Generator Node is the content it creates (e.g., a block of text or an image). This output can be connected to the input of other nodes, allowing you to chain AI tasks together. For example, the text generated by one node can be used as the input for another node that summarizes or translates it.


# GitHub Tools
Source: https://docs.giselles.ai/en/glossary/github-tools

Learn how to configure and use GitHub Tools within a Generator Node, empowering your AI models to interact directly with your GitHub repositories.

**GitHub Tools** enable AI models inside a Generator Node to perform a wide range of actions on GitHub by giving them access to a curated set of functions. This feature, often referred to as "tool use" or "function calling," allows you to build powerful AI agents that can automate development workflows, such as creating issues, managing pull requests, searching for code, and more, all based on natural language instructions in your prompt.

## Configuring GitHub Tools

Follow these steps to connect your GitHub account and enable specific tools for a Generator Node.

### 1. Navigate to the Tools Tab

In any Generator Node (e.g., `gemini-2.5-pro`), select the **Tools** tab. You will see a list of available integrations that can be connected.

### 2. Connect to GitHub

Click the **+ Connect** button next to the GitHub integration. This will open a configuration modal to add your credentials.

### 3. Add Your Personal Access Token (PAT)

To authenticate with GitHub, you need to provide a Personal Access Token (PAT).

<Info>
  You can create a new PAT from your GitHub account settings: [https://github.com/settings/personal-access-tokens](https://github.com/settings/personal-access-tokens). Ensure your token has the necessary permissions (scopes) for the actions you want to perform.
</Info>

In the "Connect to GitHub" window:

1. **Token Name**: Give your token a descriptive name for easy identification later (e.g., "Create Issue" or "Update Docs").
2. **Personal Access Token (PAT)**: Paste your token into this field. Giselle encrypts the token with authenticated encryption before saving it.
3. Click **Save & Connect**.

### 4. Select the Tools to Enable

After your token is validated, you'll be presented with a list of available GitHub tools, grouped by category. For security and control, you must explicitly select which actions the AI model is allowed to perform.

Check the boxes next to the tools you want to enable for this node (e.g., `createIssue`, `getPullRequest`, `createOrUpdateFile`).

### 5. Save the Configuration

Once you've selected the desired tools, click **Save & Connect** at the bottom of the modal. The Generator Node will now show that GitHub is connected, displaying the enabled tools and a **Configuration** button to make future changes.

## Available GitHub Tools

The following is a list of tools you can enable for your AI model, categorized as they appear in the configuration screen.

**Note**: GitHub tools conform to the definitions at [https://github.com/github/github-mcp-server](https://github.com/github/github-mcp-server)

### Repository

#### `getFileContents`

Retrieves file or directory contents from a repository

* **Required**:
  * `owner` (Repository owner)
  * `path` (Path to file/directory)
  * `repo` (Repository name)
* **Optional**: `branch` (Branch to get contents from)

#### `listBranches`

Lists all branches in a repository with pagination support

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
* **Optional**:
  * `page` (Page number for pagination, min 1)
  * `perPage` (Results per page, min 1, max 100)

### Issues

#### `createIssue`

Opens a new issue with required title and optional body, assignees, labels, and milestone number

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `title` (Issue title)
* **Optional**:
  * `body` (Issue body content)
  * `assignees` (Array of usernames to assign)
  * `labels` (Array of labels to apply)
  * `milestone` (Milestone number)

#### `getIssue`

Retrieves detailed information about a specific issue by its number

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `issueNumber` (Issue number)

#### `listIssues`

Lists repository issues with filters for state, labels, date, sort order, and direction with pagination

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
* **Optional**:
  * `state` (open/closed/all)
  * `labels` (Array of labels to filter by)
  * `sort` (created/updated/comments)
  * `direction` (asc/desc)
  * `since` (ISO 8601 timestamp)
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

#### `updateIssue`

Updates an existing issue's properties

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `issueNumber` (Issue number to update)
* **Optional**:
  * `title` (New title)
  * `body` (New description)
  * `state` (open/closed)
  * `assignees` (New assignees array)
  * `labels` (New labels array)
  * `milestone` (New milestone number)

#### `addIssueComment`

Adds a comment to an existing issue with required body content

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `issueNumber` (Issue number)
  * `body` (Comment content)

#### `getIssueComments`

Retrieves all comments on a specific issue with pagination support

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `issueNumber` (Issue number)
* **Optional**:
  * `page` (Page number)
  * `perPage` (Number of records per page)

### Pull Requests

#### `createPullRequest`

Opens a new PR from head branch to base branch with title, optional body, draft status

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `title` (PR title)
  * `head` (Branch containing changes)
  * `base` (Branch to merge into)
* **Optional**:
  * `body` (PR description)
  * `draft` (Create as draft PR)
  * `maintainerCanModify` (Allow maintainer edits)

#### `getPullRequest`

Fetches detailed information about a specific pull request by number

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)

#### `updatePullRequest`

Edits PR properties including title, body, base branch, state, and maintainer permissions

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)
* **Optional**:
  * `title` (New title)
  * `body` (New description)
  * `state` (open/closed)
  * `base` (New base branch name)
  * `maintainerCanModify` (Allow maintainer edits)

#### `listPullRequests`

Lists PRs with filters for state, base/head branches, sort order, and direction with pagination

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
* **Optional**:
  * `state` (open/closed/all)
  * `head` (Filter by head user/org and branch)
  * `base` (Filter by base branch)
  * `sort` (created/updated/popularity/long-running)
  * `direction` (asc/desc)
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

#### `getPullRequestComments`

Retrieves review comments on a pull request

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)

#### `getPullRequestFiles`

Lists all files changed in a pull request with pagination

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)

#### `getPullRequestReviews`

Gets all reviews submitted for a PR

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)

#### `getPullRequestStatus`

Checks CI/CD status checks for a pull request

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)

#### `createPullRequestReview`

Creates a pending review that can be submitted later

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)
  * `event` (APPROVE/REQUEST\_CHANGES/COMMENT)
* **Optional**:
  * `body` (Review comment text)
  * `commitId` (SHA of commit to review)
  * `comments` (Array of line-specific comment objects)

#### `addPullRequestReviewComment`

Adds inline comments to specific lines/files during review with support for multi-line comments

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)
  * `body` (Review comment text)
* **Optional** (one of these patterns required):
  * **Pattern 1 (reply)**: `inReplyTo` (ID of comment to reply to)
  * **Pattern 2 (new comment)**:
    * `commitId` (SHA of commit to comment on)
    * `path` (Relative path to file)
    * `line` (Line number in the diff)
    * `side` (LEFT/RIGHT)
    * `startLine` (For multi-line comments)
    * `startSide` (LEFT/RIGHT for multi-line)
    * `subjectType` (line/file)

#### `mergePullRequest`

Merges a PR with options for merge method, commit title, and commit message

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)
* **Optional**:
  * `mergeMethod` (merge/squash/rebase)
  * `commitTitle` (Title for merge commit)
  * `commitMessage` (Extra detail for merge commit)

#### `updatePullRequestBranch`

Updates PR branch with latest changes from base branch

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `pullNumber` (Pull request number)
* **Optional**:
  * `expectedHeadSha` (Expected SHA of the PR's HEAD ref)

### Code Management

#### `createBranch`

Creates a new branch from an existing branch or repository's default branch

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `branch` (Name for new branch)
* **Optional**:
  * `fromBranch` (Source branch, defaults to repo default)

#### `createOrUpdateFile`

Creates new files or updates existing ones with content, commit message, and branch. Requires SHA for updates

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `path` (Path where to create/update the file)
  * `content` (Content of the file)
  * `message` (Commit message)
  * `branch` (Branch to create/update the file in)
* **Optional**:
  * `sha` (SHA of file being replaced, required for updates)

#### `getCommit`

Retrieves detailed information about a specific commit by SHA, branch name, or tag name

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
  * `sha` (Commit SHA, branch name, or tag name)
* **Optional**:
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

#### `listCommits`

Lists commit history with optional filtering by author and SHA/branch/tag reference

* **Required**:
  * `owner` (Repository owner)
  * `repo` (Repository name)
* **Optional**:
  * `sha` (SHA or branch name)
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

### Search

#### `searchCode`

Searches for code using GitHub's code search syntax

* **Required**:
  * `q` (Search query using GitHub code search syntax)
* **Optional**:
  * `sort` (indexed)
  * `order` (asc/desc)
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

#### `searchIssues`

Searches issues and pull requests using GitHub search syntax, can be scoped to specific owner/repo

* **Required**:
  * `q` (Search query using GitHub issues search syntax)
* **Optional**:
  * `sort` (comments/reactions/reactions-+1/reactions--1/reactions-smile/reactions-thinking\_face/reactions-heart/reactions-tada/interactions/created/updated)
  * `order` (asc/desc)
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

#### `searchPullRequests`

Specifically searches pull requests with advanced filtering and GitHub search syntax

* **Required**:
  * `q` (Search query using GitHub issues search syntax, automatically adds type:pr)
* **Optional**:
  * `sort` (comments/reactions/reactions-+1/reactions--1/reactions-smile/reactions-thinking\_face/reactions-heart/reactions-tada/interactions/created/updated)
  * `order` (asc/desc)
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

#### `searchRepositories`

Finds repositories matching search query with pagination support

* **Required**:
  * `query` (Search query)
* **Optional**:
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

#### `searchUsers`

Searches for GitHub users using search syntax

* **Required**:
  * `q` (Search query using GitHub users search syntax)
* **Optional**:
  * `sort` (followers/repositories/joined)
  * `order` (asc/desc)
  * `page` (Page number, min 1)
  * `perPage` (Results per page, min 1, max 100)

## How to Use GitHub Tools

Once configured, you can instruct the AI model to use the enabled tools directly in your prompt. The model will understand your request and call the appropriate function with the necessary parameters to complete the task.

### Example Prompt: Create a pull request to add a new documentation page

Imagine you have enabled the `getFileContents`, `createPullRequest`, `createBranch` and `createOrUpdateFile` tools for a node.

```markdown  theme={null}
Please complete the last step without checking with me.

Creating the pull request, please follow these steps:

1. Create a new branch in your GitHub repository https://github.com/giselles-ai/docs
  - Use GitHub tool createBranch
  - fromBranch: main
  - newBranchName: prefix giselle/create-docs-xxx

2. Please create a new file based on the contents of followings
  - Use GitHub tool createOrUpdateFile
  - Contents: @generate-contents-node-output
  - Latest SHA: @getSHA-node-output

3. Create pull request to https://github.com/giselles-ai/docs
  - Use GitHub tool createPullRequest
```

When this prompt is run, the Giselle will:

1. Create a new branch in your GitHub repository.
2. Create a new file based on the contents.
3. Create pull request.


# GitHub Vector Store Node
Source: https://docs.giselles.ai/en/glossary/github-vector-store-node

Learn how the GitHub Vector Store Node vectorizes your GitHub repositories, creating a searchable knowledge base for your AI workflows in Giselle.

Learn how the GitHub Vector Store Node in Giselle vectorizes your GitHub repositories, creating a searchable knowledge base that can be queried within your AI workflows.

## GitHub Vector Store Node in Giselle

The **GitHub Vector Store Node** is a specialized "Source" node that creates a powerful, searchable database from the contents of a GitHub repository. It works by vectorizing the code and documents within the repository, allowing AI models to perform semantic searches and retrieve relevant context.

This process uses advanced embedding models to convert your repository's content into vector embeddings. You can select from multiple embedding models, including OpenAI's [`text-embedding-3-small`](https://platform.openai.com/docs/models/text-embedding-3-small) and [`text-embedding-3-large`](https://platform.openai.com/docs/models/text-embedding-3-large), as well as Google's [`gemini-embedding-001`](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemini-embedding-001?hl=en). These vectorized data are then stored securely in Giselle's dedicated Vector Store.

To use this feature, the [Giselle GitHub App](https://github.com/apps/giselles-ai) must be installed on the target GitHub repository.

### Setting up a GitHub Vector Store Node:

1. **Add the Node**:
   * From the toolbar at the bottom of the canvas, click the **Source** icon (a folder with a link symbol).
   * Select **GitHub Vector Store** from the pop-up menu to add the node to your workspace.

2. **Configure the Repository**:
   * When first added, the node will display a "REQUIRES SETUP" status.
   * Select the node to open its configuration panel on the right.
   * Click the **Select a repository** dropdown menu. This list will only show repositories that have the Giselle GitHub App installed. Choose the repository you want to use as a knowledge source (e.g., `giselles-ai/docs`).

3. **Choose the Content Type**:
   * After selecting a repository, you will need to specify which type of content to vectorize. The available options are:
   * **Code**: Vectorizes the source code and documents from the repository's default branch. This is useful for creating a knowledge base from your codebase.
   * **Issues**: Vectorizes the content from issues, including descriptions, comments, and discussions. This is ideal for analyzing problem patterns or summarizing bug tracking.
   * **Pull Requests**: Vectorizes the content from pull requests, including descriptions, comments, and discussions. This is ideal for analyzing development patterns or summarizing changes.
   * Select the radio button corresponding to the content you wish to use.

4. **Finalize Setup**:
   * Once the repository and content type are selected, the node on the canvas will update to show the name of the configured repository. The vectorization process for this repository will be initiated or updated in the background.

### Managing Your Vector Stores

You can add, configure, and remove the GitHub repositories that are processed by the GitHub Vector Store Node from your team's settings page.

* Navigate to **Settings > Team > Vector Stores** in your Giselle account.
* Alternatively, you can click the **Set Up GitHub Vector Store** link directly from the node's configuration panel.
* This page allows you to manage which repositories are indexed and available for your workflows. You can access it here: [https://studio.giselles.ai/settings/team/vector-stores](https://studio.giselles.ai/settings/team/vector-stores).

#### Sources to Ingest

When registering a new repository, you can select which types of content to ingest. Giselle currently supports three sources:

* **Code**: Ingests the source code files from the repository. This source is required and cannot be disabled.
* **Issues**: Ingests the descriptions, comments, and discussions from issues. This is an optional source that can be enabled to provide additional context to your AI workflows.
* **Pull Requests**: Ingests the content and discussions from merged pull requests. This is an optional source that can be enabled to provide additional context to your AI workflows.

#### Embedding Models

When setting up a GitHub Vector Store, you can select from multiple embedding models for indexing your repository content. You must select at least one embedding model. Available options include:

* **OpenAI text-embedding-3-small**: Provider: OpenAI • Dimensions: 1536 - A powerful and efficient model suitable for most use cases.
* **OpenAI text-embedding-3-large**: Provider: OpenAI • Dimensions: 3072 - A larger model with higher precision for complex semantic understanding.
* **Google gemini-embedding-001**: Provider: Google • Dimensions: 3072 - Google's embedding model offering alternative semantic representation capabilities.

The choice of embedding model affects how your content is vectorized and can impact search quality and performance. You can select multiple models to leverage different semantic representation capabilities for your vector store.

### Rate Limits and Considerations

When using the GitHub Vector Store Node, please be aware of GitHub API rate limits. Giselle's GitHub Vector Store uses [GitHub App Installation](https://docs.github.com/ja/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28#primary-rate-limit-for-github-app-installations) for GitHub API access, which has a rate limit of approximately 5,000 requests per hour. You may encounter errors when working with large-scale projects. If this occurs, please wait some time before trying again.

For large repositories or frequent updates, you may experience rate limiting during the vectorization process. If you encounter errors, simply wait and retry after the rate limit window resets.

### Usage in Workflows

The GitHub Vector Store Node is designed to be used in combination with a **Query Node**. It acts as the knowledge base that the Query Node searches through.

* **Connect the Output**: The "Output" of the GitHub Vector Store Node should be connected to the input of a Query Node.
* **Perform a Search**: The Query Node can then take a user's question or a dynamic input, search the vectorized repository content for the most relevant information, and pass that information to subsequent nodes (like a Generator Node) for processing, analysis, or summarization.

### Output of the Node

The GitHub Vector Store Node's **output** is a reference to the vectorized data of the selected repository. This output provides the necessary connection for other nodes, like the Query Node, to access and search the repository's content.


# Nodes in Giselle
Source: https://docs.giselles.ai/en/glossary/node

Learn about nodes, the building blocks of AI apps on Giselle. Connect nodes with various functions to visually design powerful AI workflows.

## Giselle's AI Agents Can Be Built by Combining "Nodes"

Giselle is a platform that allows you to build powerful AI agents through an intuitive node-based interface. By connecting "nodes" with various functions, like assembling building blocks, you can visually design complex AI workflows. This makes it easy for anyone, even without specialized knowledge, to achieve automation with AI agents.

## Introducing Giselle's Key Nodes

Here are some of the fundamental nodes available in Giselle. By combining these nodes, you can build various AI workflows.

### Generator Node

The Generator node can create both text and images using advanced AI models. By configuring prompts and conditions, you can generate content tailored to your needs. For text, this includes applications such as document creation, blog writing, and research report generation, leveraging Giselle's LLM API for high-quality, natural-sounding text. For images, you can generate visuals from text prompts, enabling creative content creation and workflows that utilize visual data. The Generator node empowers you to flexibly produce a wide range of AI-generated outputs within your workflows.

**Web Search Capability**: When using models that support web search functionality, the Generator node can access real-time information from the internet. This enables the creation of content based on the latest data and current events, making your AI workflows more dynamic and up-to-date.

### Text Node

Text node is used to hold text data. It can be used to record prompts, instructions, annotations, and more. It helps manage and organize text data within the workflow, streamlining input to text generation nodes and data usage in other nodes.

### File Node

File node is used to handle file data. You can read files, use them as input for AI models, and save output results to files. It is useful for various tasks that involve utilizing file data, such as data-based analysis and report generation.

### Web Page Node

The Web Page node is used to fetch and hold content from web pages. You can input one or more URLs, and Giselle will attempt to retrieve the content from these pages. Currently, the fetched content is processed and made available primarily in Markdown format. This allows you to use web content as a dynamic input source for AI models or other processing nodes within your workflow, enabling tasks like summarization, analysis, or content generation based on information from the web.

### Trigger Node

Trigger Node is the starting point for running the workflow built in the Giselle App. It initiates the execution of the connected nodes in a sequence. Currently, two types of Trigger Nodes are supported:

* **Manual Trigger Node**: This node allows you to manually initiate the workflow directly within the Giselle App Workspace. It's useful for testing, on-demand executions, or when you want direct control over when a workflow runs.
* **GitHub Trigger Node**: This node enables workflows to be automatically triggered by GitHub webhooks. When the Giselle GitHub App is installed in a repository, this node can listen for specific events (like issue comments or pull requests) and start the Giselle App's workflow in response.

### Action Node

Action Node is a node that can call external services. Currently, it primarily supports integrations with GitHub, allowing workflows to perform actions within your repositories. We plan to expand its capabilities to enable interactions with a variety of other external services in the future.

### GitHub Vector Store Node & Query Node

Giselle supports advanced data retrieval and search capabilities through the **GitHub Vector Store Node** and the **Query Node**.

* **GitHub Vector Store Node**: This specialized Source node allows you to vectorize the contents of a GitHub repository, creating a searchable knowledge base. You can select from multiple advanced embedding models, including OpenAI's text-embedding models and Google's gemini-embedding-001, to convert your repository's code and documents into vector representations, enabling semantic search within your workflows. This is especially useful for building Retrieval-Augmented Generation (RAG) applications. For setup and details, see the [GitHub Vector Store Node documentation](github-vector-store-node).

* **Query Node**: The Query Node is designed to execute search queries against connected data sources, such as the GitHub Vector Store Node. It retrieves the most relevant information (text chunks) from your vectorized repositories, which can then be used as dynamic context for AI generation or further processing. For more information, see the [Query Node documentation](query-node).

**Typical Usage:**

1. Add a GitHub Vector Store Node and configure it with your repository.
2. Connect its output to a Query Node.
3. Use the Query Node to search your repository's content and pass the results to other nodes, such as a Generator Node, for context-aware AI workflows.

These nodes enable powerful, up-to-date, and context-rich AI applications by leveraging your own data sources within Giselle.

## Tips for using Node

Here are some helpful tips to enhance your experience with nodes in Giselle.

### Node Duplication

To enhance workflow efficiency, Giselle supports node duplication. This feature allows you to quickly create a copy of an existing node within the workflow designer.

**How to Duplicate a Node:**

* **Right-Click Context Menu:** Right-click on any node in the workflow designer to open the context menu, then select "Duplicate Node."
* **Keyboard Shortcut:** Select the node you wish to duplicate and use the keyboard shortcut `Cmd + D` (on macOS) or `Ctrl + D` (on Windows/Linux).

**Duplication Behavior:**

* The duplicated node will appear at an offset position from the original node.
* Connections from the original node are preserved in the duplicate where applicable.
* For File nodes, the duplicated node will correctly reference newly copied files.
* Cloned nodes will start in an "unconfigured" state, allowing you to customize their settings independently from the original node.
* If the duplication process encounters an issue, an error message will be displayed.

This feature streamlines the process of building complex workflows by allowing for easy replication of configured or template nodes.

## Future Node Expansion Plans

We plan to expand node functionality to further empower our users to build AI workflows. Here's a look at what our team is currently considering:

### Expansion of the File Node

We plan to expand the file formats supported by the File node, adding support for:

* **Tabular Files** (CSV, Excel, etc.)
* **Audio Files**

Stay tuned for Giselle's product updates!


# PostgreSQL Tools
Source: https://docs.giselles.ai/en/glossary/postgresql-tools

Learn how to use PostgreSQL Tools in a Generator Node to connect your AI models to a PostgreSQL database, enabling them to query and retrieve data.

**PostgreSQL Tools** empower AI models within a Generator Node to connect directly to your PostgreSQL databases. This feature, a form of "tool use" or "function calling," allows you to build AI agents that can query tables, retrieve data, and understand your database schema, all based on natural language instructions in your prompt.

This enables powerful workflows, such as generating business reports, answering data-driven questions, or performing automated data analysis.

## Configuring PostgreSQL Tools

Follow these steps to connect your PostgreSQL database and enable specific tools for a Generator Node.

### 1. Navigate to the Tools Tab

In any Generator Node (e.g., `gemini-2.5-pro`), select the **Tools** tab. You will see a list of available integrations that can be connected.

### 2. Connect to PostgreSQL

Click the **+ Connect** button next to the PostgreSQL integration. This will open a configuration modal to add your database credentials.

### 3. Add Your Connection String

To authenticate with your PostgreSQL database, you need to provide a connection string.

<Info>
  The connection string typically follows the format: `postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]`. For detailed information, refer to the [official PostgreSQL documentation](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING).
</Info>

In the "Connect to PostgreSQL" window:

1. **Connection Name**: Give your connection a short, descriptive name for easy identification (e.g., "giselle-db-preview"). You'll use this to link other nodes.
2. **Connection String**: Paste your full PostgreSQL connection string into this field. Giselle encrypts the connection string with authenticated encryption before saving it.
3. Click **Save & Connect**.

### 4. Select the Tools to Enable

After your connection is validated, you'll be presented with a list of available PostgreSQL tools. For security and control, you must explicitly select which actions the AI model is allowed to perform.

Check the boxes next to the tools you want to enable for this node:

* `getTableStructure`
* `query`

### 5. Save the Configuration

Once you've selected the desired tools, click **Save & Connect**. The Generator Node will now show that PostgreSQL is connected, displaying the enabled tools and a **Configuration** button to make future changes.

## Available PostgreSQL Tools

The following is a list of tools you can enable for your AI model.

### Schema

* `getTableStructure`: Allows the AI model to retrieve the schema of your database. This includes table names, column names, and data types. This is crucial for the AI to understand how to construct valid queries.

### Query

* `query`: Allows the AI model to execute a standard SQL query against the connected database and retrieve the results.

## How to Use PostgreSQL Tools

Once configured, you can instruct the AI model to use the enabled tools directly in your prompt. The model will understand your request, call the appropriate function, and use the results to complete the task.

### Example Prompt: Calculate the number of users

Imagine you have enabled the `getTableStructure` and `query` tools for a node.

```markdown  theme={null}
Please find out the total number of users from the database.
```

When this prompt is run, the Giselle agent will:

1. Call the `getTableStructure` function to understand the database layout.
2. Identify the relevant table (e.g., `users`).
3. Formulate a SQL query like `SELECT COUNT(*) FROM users;`.
4. Execute the query using the `query` tool.
5. Return a final answer based on the query result, such as: "The total number of users is 1,234."


# Query Node
Source: https://docs.giselles.ai/en/glossary/query-node

Learn how the Query Node in Giselle executes queries against data sources like the GitHub Vector Store to enable Retrieval-Augmented Generation (RAG).

## Query Node in Giselle

The **Query Node** is a powerful component in Giselle designed to search and retrieve information from connected data sources. Its primary function is to execute a query (such as a question or a search term) against a dataset and return the most relevant results.

Currently, the Query Node is optimized to work with the **GitHub Vector Store Node**, making it a crucial building block for creating Retrieval-Augmented Generation (RAG) applications directly within your Giselle workflows.

### How to Use the Query Node

Setting up a Query Node involves adding it to your canvas, connecting a data source, and running a query.

#### 1. Add a Query Node

From the node toolbar at the bottom of the canvas, select the **Query Node**, which is identifiable by its magnifying glass icon, and place it in your workspace.

#### 2. Connect a Data Source

The Query Node requires an input from a data source to function. You must connect the `Output` of a data source node (like the GitHub Vector Store Node) to the `Input` of the Query Node. Until a data source is connected, the node will indicate that it is waiting for a connection.

#### 3. Write and Run a Query

Once a data source is connected, you can configure the Query Node:

* **Enter a Query**: In the configuration panel, type your question or search term into the "Query" input field.
* **Run the Query**: Click the **Run Query** button to execute the search against the connected data source.

#### 4. Review the Results

After the query runs, the results will be displayed directly in the node's panel. The results typically include:

* A summary of the number of results found.
* A list of relevant "chunks" of text retrieved from the source documents.
* A similarity score (e.g., 58%) for each chunk, indicating its relevance to your query.

You can expand each chunk to view its content and metadata.

### Core Use Case: Retrieval-Augmented Generation (RAG)

The primary purpose of the Query Node is to enable **Retrieval-Augmented Generation (RAG)** workflows. RAG enhances the capabilities of Large Language Models (LLMs) by providing them with relevant, up-to-date information from your own data sources before they generate a response.

A typical RAG workflow in Giselle looks like this:

1. **Data Source (GitHub Vector Store Node)**: Ingests and vectorizes your documentation from a GitHub repository, making it searchable.
2. **Query Node**: Takes a user's question (the query) and retrieves the most relevant text chunks from the vector store.
3. **Generator Node**: Receives the original question *and* the retrieved information from the Query Node's output. It uses this combined context to generate a more accurate, detailed, and factually grounded answer.

### Output of the Query Node

The `Result` output of the Query Node contains the collection of retrieved data chunks. This structured data can be passed to subsequent nodes—most commonly a **Generator Node**—to serve as dynamic context for text generation.

<Note>
  For more information on how to set up a data source for querying, see our documentation on the [GitHub Vector Store Node](github-vector-store-node).
</Note>


# Text Node
Source: https://docs.giselles.ai/en/glossary/text-node

Learn how the Text Node in Giselle allows you to store and manage plain text, such as prompts, instructions, or data, directly within your workflows.

## Text Node in Giselle

The **Text Node** is one of the simplest yet most versatile "Source" nodes in Giselle. It is designed to hold and manage plain text content directly within your workflow, making it an essential tool for a wide range of applications. Unlike the File Node, which handles uploaded files, the Text Node stores its content inline, ensuring it is always immediately available without any loading or processing time.

### Key Features

* **Direct Text Input**: You can write or paste any text directly into the node's built-in editor.
* **Inline Storage**: The content is stored as a simple string within the node itself, making your workflow self-contained and portable.
* **Instant Availability**: Since there are no file uploads or external storage, the text is instantly available as an output for other nodes.

### How to Use a Text Node

1. **Add the Node**: From the toolbar at the bottom of the canvas, click the **Source** icon and select **Plain Text** to add the node to your workspace.
2. **Configure the Content**: Select the node to open its configuration panel on the right.
3. **Enter Text**: Type or paste your content directly into the text editor, which displays the placeholder "Write or paste text here...". The content is saved automatically as you type.

### Common Use Cases

The Text Node is ideal for:

* **Storing Prompts**: Write and store reusable prompts for Generator Nodes.
* **Creating Templates**: Keep text templates for various content generation tasks.
* **Writing Instructions**: Document workflow-specific instructions or guidelines for your team.
* **Holding Data**: Store small, structured datasets like JSON or CSV content for processing.
* **Quick Notes**: Use it for temporary text storage or as a scratchpad during workflow development.

### Text Node vs. File Node

While a **File Node** can also handle text files (like `.txt` or `.md`), the **Text Node** is fundamentally different and often more convenient:

* **Storage**: The Text Node stores content *directly* in the workflow. The File Node requires you to *upload* a file, which is stored separately.
* **Editing**: Content in a Text Node can be edited instantly within the Giselle interface. To change the content of a File Node, you would need to upload a new file.
* **Overhead**: The Text Node has no file management overhead (no size tracking, upload states, or potential upload failures).
* **Best For**: The Text Node is better suited for dynamic or frequently edited content, while the File Node is ideal for using large, static text files as a data source.

### Output of the Node

The **output** of a Text Node is the raw text content you have entered into its editor. This output can be connected to the input of any compatible node. For example, you can connect it to a Generator Node to use the text as a prompt, or to an Action Node to pass the text as a parameter to an external service.


# Trigger Node
Source: https://docs.giselles.ai/en/glossary/trigger-node

Learn about Trigger Nodes, the starting points for workflows in Giselle. Configure Manual Triggers with parameters or use GitHub Triggers to initiate your AI workflow sequences.

## Trigger Node in Giselle

The **Trigger Node** is the starting point for running the workflow built in the Giselle App. It initiates the execution of the connected nodes in a sequence.

Currently, two types of Trigger Nodes are supported.

### Manual Trigger Node

The **Manual Trigger Node** allows you to start your workflow with the click of a button. You can also configure it to request specific parameters each time it's run. This is useful for providing dynamic inputs to your workflow at the moment of execution.

**Configuring Manual Trigger Parameters:**

When you add a Manual Trigger Node to your workflow, you can define parameters that will be requested when the flow is manually triggered. If no parameters are configured, the flow will simply start when triggered.

To add and configure parameters:

1. In the "Add New Parameter" section:
   * **Parameter Name**: Enter a descriptive name for the parameter (e.g., "Title", "Message", "Priority"). This name will be used to identify the input field when the trigger is run.
   * **Type**: Select the type of data this parameter will accept. The available options are:
     * **Text**: For single-line text input.
     * **Text(multi-line)**: For longer text input that may span multiple lines.
     * **Number**: For numerical input.
   * **Required**: Check this box if the parameter must be filled in before the workflow can be triggered. An error will occur if a required parameter is left empty.
2. Click the **plus icon (+)** to add the configured parameter to the list.
3. You can add multiple parameters by repeating the steps above.
4. Once all desired parameters are added and configured, click **Save Configuration**.

When you manually run this workflow, a form will appear prompting you to enter values for the parameters you've defined. These values can then be used by subsequent nodes in your workflow.

### GitHub Trigger Node

The **GitHub Trigger Node** enables you to automatically start your Giselle workflows based on specific events occurring in your GitHub repositories. This allows for seamless integration between your code management and AI-powered tasks.

**Setting up a GitHub Trigger:**

1. **Select GitHub Account/Organization**:
   * When you add a GitHub Trigger node, you'll first need to choose the GitHub account or organization where your target repository resides (e.g., `giselles-ai`, `liam-hq`).
   * If you're missing a GitHub account connection or need to adjust permissions, click on "Adjust GitHub App Permissions".

2. **Choose a Repository**:
   * A list of repositories available under the selected account/organization will be displayed (e.g., `docs`, `giselle`).
   * Click the **Set up** button next to the desired repository (e.g., `giselle`).
   * If your repository isn't listed, you might need to "Adjust GitHub App Permissions" to grant Giselle access to it.

3. **Configure the Trigger Event**:
   * Once a repository is selected (e.g., `giselles-ai/giselle`), you need to specify which GitHub event will trigger the workflow.
   * Click on the dropdown menu labeled "Choose when you want to trigger the flow."
   * Select an event from the list, such as:
     * **Issue Created**: Triggers the flow when a new issue is created in the repository.
     * **Issue Closed**: Triggers when an issue is closed.
     * **Issue Labeled**: Triggers when a specific label is added to an issue.
     * **Issue Comment Created**: Triggers when a new comment is made on an issue.
     * **Pull Request Comment Created**: Triggers on a new pull request comment.
     * **Pull Request Opened**: Triggers when a new pull request is opened.
     * **Pull Request Ready for Review**: Triggers when a pull request is marked as ready for review.
     * **Pull Request Closed**: Triggers when a pull request is closed.
     * **Pull Request Labeled**: Triggers when a specific label is added to a pull request.

4. **Configure Callsign (for specific events)**:
   * For some events, like "Issue Comment Created" or "Pull Request Comment Created," you can specify a **Callsign**.
   * A Callsign is a specific string or command (e.g., `/code-review`, `/deep-research`) that must be present in the comment for the trigger to activate. This prevents the flow from running on every single comment.
   * Enter your desired Callsign in the provided field. The example shows `/code-review`.
   * Click **Set up** after configuring the Callsign.

4a. **Configure Labels (for specific events)**:

* For some events, like "Issue Labeled" or "Pull Request Labeled," you can specify one or more **Labels**.
* When multiple labels are added, the workflow will trigger if *any* of the specified labels are added to the issue or pull request (OR condition). This allows for flexible triggering based on labeling conventions.
* Enter your desired labels in the provided input fields. You can add multiple labels using the "Add label" button.
* Click **Set up** after configuring the Labels.

5. **Enable the Trigger**:
   * After configuring the event and any associated options (like Callsign or Labels), the trigger will initially be in a "Disabled" state. The node on the canvas will show "Requires Setup" or display the repository and event type with a "Disabled" status.
   * On the configuration panel for the trigger (e.g., "On Issue Created" or "On Issue Comment Created"), you will see the current **State** as "Disable".
   * Click on **Enable** to activate the trigger.
   * Once enabled, the **State** will change to "Enable", and you will see an option to **Disable Trigger**. The node on the canvas will also reflect its "Enabled" status.

6. **Run in the workspace**:
   * For GitHub Trigger Nodes, clicking the "Run" button allows you to test your workflow without waiting for an actual GitHub webhook. You can enter values in a form that simulates the GitHub event, enabling you to verify that your workflow functions correctly before enabling it for real GitHub events.

**Example Workflow after Setup:**

On Issue Created:

* **Trigger**: "On Issue Created" for repository `giselles-ai/giselle`.
* **State**: Enabled.
* **Action**: When a new issue is created in the `giselles-ai/giselle` repository, this Giselle workflow will automatically start.

On Pull Request Comment Created:

* **Trigger**: "On Pull Request Comment Created" for repository `giselles-ai/giselle` with Callsign `/code-review`.
* **State**: Enabled.
* **Action**: When a comment containing `/code-review [enter your request...]` is posted on a pull request in `giselles-ai/giselle`, this workflow will start. The subsequent nodes can then access information like the comment body, pull request number, the pull request's diff content, etc.

On Issue Labeled:

* **Trigger**: "On Issue Labeled" for repository `giselles-ai/giselle` with label `bug`.
* **State**: Enabled.
* **Action**: When the label `bug` is added to an issue in `giselles-ai/giselle`, this Giselle workflow will automatically start. The subsequent nodes can access information like the issue number, title, body, and the name of the label that triggered the event.

On Pull Request Labeled:

* **Trigger**: "On Pull Request Labeled" for repository `giselles-ai/giselle` with labels `feature` or `enhancement`.
* **State**: Enabled.
* **Action**: When either the `feature` or `enhancement` label is added to a pull request in `giselles-ai/giselle`, this workflow will start. The subsequent nodes can access information like the pull request number, title, body, and the name of the label that triggered the event.

Stay tuned for more updates and functionalities for Giselle's nodes!


# Web Page Node
Source: https://docs.giselles.ai/en/glossary/webpage-node

Learn how the Web Page Node in Giselle allows you to fetch and use content from web pages as static inputs in your AI workflows.

## Web Page Node in Giselle

The **Web Page Node** is used to fetch and hold content from web pages. You can input one or more URLs, and Giselle will attempt to retrieve the content from these pages. Currently, the fetched content is processed and made available primarily in **Markdown format**. This allows you to use web content as a static input source for AI models or other processing nodes within your workflow, enabling tasks like summarization, analysis, or content generation based on information from the web.

The Web Page Node functions as an independent variable node, providing a streamlined way to integrate web-based information into your Giselle applications.

### Setting up a Web Page Node:

1. **Add a Web Page Node**:
   * Drag and drop a "Web Page" node from the toolbar at the bottom of the canvas onto your workspace.

2. **Configure URLs**:
   * Select the Web Page node on the canvas to open its configuration panel on the right.
   * In the text area labeled "URLs (one per line)", enter the full web addresses (URLs) of the pages from which you want to fetch content. If you have multiple URLs, enter each one on a new line.
     ```
     https://example.com/
     https://docs.giselles.ai/glossary/node
     ```

3. **Add URLs**:
   * After entering the desired URLs, click the blue **Add** button.
   * Giselle will then attempt to fetch the content from the specified URLs.
   * Once the URLs are processed, the configuration panel will update to list the added pages, often displaying their titles or a reference to the URL. The "URLs (one per line)" input area and the **Add** button will remain, allowing you to add more URLs if needed.

### Output of the Web Page Node:

* **Content**: After successfully fetching data from the provided URLs, the Web Page Node makes this content available as its **output**.
* **Format**: The fetched content is primarily delivered in **Markdown format**. This standardized format makes it easy to use in subsequent text-processing nodes.
* **Connectivity**: The output of the Web Page Node can be connected to other nodes in your workflow. For instance, you can feed the Markdown content into a **Generator Node** to summarize an article, extract specific information, or use it as context for generating new content.

The Web Page node on the canvas will have an "Output" port, which you can drag to connect to an input port of another node.

### Example: Summarizing a Web Article

1. **Configure Web Page Node**:
   * Add a Web Page Node.
   * Input the URL of an online blog article (e.g., `https://giselles.ai/blog/transforming-product-development-human-ai-collaboration`).
   * Click **Add**.

2. **Connect to Generator Node**:
   * Add a Generator Node.
   * Connect the "Output" of the Web Page Node to an input (e.g., a context or document input) of the Generator Node.

3. **Configure Generator Node**:
   * Instruct the Generator Node to summarize the provided text. For example, use a prompt like: "Please summarize the following article concisely:"

4. **Run Workflow**:
   * When the workflow runs, the Web Page Node fetches the article content as Markdown, and the Generator Node produces a summary.

### Future Updates

The Web Page Node's user interface and functionality, including supported output formats, may be updated incrementally in future Giselle releases.


# My Apps
Source: https://docs.giselles.ai/en/guides/apps/myapp

Create and manage your personal AI applications

My Apps are personal AI applications that you can create and manage on the Giselle App Builder platform. You can build powerful AI applications by combining multiple AI models and data sources, and run them as many times as needed.

## Key Features

### Application Building

* **AI Model Integration**: Combine various AI models to create custom applications
* **Data Source Connectivity**: Leverage information from multiple data sources to enhance AI capabilities
* **Repeated Execution**: Run your built applications as many times as necessary

### Team Utilization through GitHub Integration

While My App is primarily intended for personal use, you can utilize it with teams through GitHub integration:

* **Repository Integration**: Connect with repositories such as GitHub
* **Automatic Execution Triggers**: Set up automatic application execution triggered by issue creation or pull request submission
* **Output Sharing**: Functions as a GitHub App, allowing all team members with access to the connected repository to share output results

This enables you to incorporate functions from your personally created My App into your entire team's workflow.

## Differences Between My App and Team App

My App has the following limitations:

* **Editing Permissions**: Only the creator of the app can edit the application itself
* **Viewing Restrictions**: Viewing the application settings and configuration is also limited to the creator

To remove these restrictions and enable collaborative editing and viewing of applications with multiple members, you need to become a Pro user and create a team. After creating a team, collaborative management becomes possible as a Team App.

## Use Cases for My App

* **Personal Productivity Enhancement**: Create AI applications that assist with daily work and research
* **Project Automation**: Automate development processes through GitHub integration
* **Code Review Support**: Automatically run code analysis when pull requests are created

## Getting Started

1. Create a [Giselle account](https://studio.giselles.ai/signup)
2. Create a new My App from "New App+"
3. Select and configure the necessary AI models and data sources
4. [Build](workspaces/build) your application
5. Run your application as needed


# Team Apps
Source: https://docs.giselles.ai/en/guides/apps/teamapp

Collaborate and manage AI applications with your team

Team Apps are collaborative AI applications that enable multiple team members to create, edit, and manage applications together on the Giselle App Builder platform. With Team Apps, you can leverage the collective expertise of your team to build more sophisticated AI solutions by combining multiple AI models and data sources.

## Key Features

### Collaborative Application Building

* **Shared Editing Access**: Multiple team members can edit and refine the same application
* **Collaborative Configuration**: Team members can jointly configure AI models and data sources
* **Version History**: Track changes and contributions from different team members

### Team Management

* **Permission Controls**: Assign different roles and access levels to team members
* **Shared Visibility**: All team members can view application settings and configurations
* **Collective Ownership**: Applications belong to the team rather than a single creator

### Enhanced Integration Capabilities

Team Apps include all the GitHub integration features available in My Apps:

* **Repository Integration**: Connect with repositories such as GitHub
* **Automatic Execution Triggers**: Set up automatic application execution triggered by issue creation or pull request submission
* **Output Sharing**: Functions as a GitHub App, allowing all team members with access to the connected repository to share output results

## Differences Between My Apps and Team Apps

Team Apps offer several advantages over My Apps:

* **Collaborative Editing**: Multiple team members can edit the application, unlike My Apps where only the creator has edit access
* **Shared Viewing**: All team members can view application settings and configurations
* **Seamless Handoffs**: Team members can continue work started by colleagues

## Requirements for Team Apps

* **Pro Subscription**: Team Apps are only available to Pro users
* **Team Creation**: You must create a team before you can start using Team Apps
* **Team Members**: Invite colleagues to join your team through the team management interface

## Getting Started

1. Upgrade to a [Pro subscription](https://studio.giselles.ai/pricing)
2. Create a team from the "Teams" section in your account
3. Invite team members to join
4. Create a new Team App from "New App+" within your team workspace
5. Collaborate with your team to build, preview, and integrate your application


# Quickstart
Source: https://docs.giselles.ai/en/guides/get-started/quickstart

Build your first AI workflow with Giselle in minutes! This quick start guide covers signup to running a workflow.

## Build Your First AI Workflow with Giselle

Get up and running with Giselle in minutes! This quick start guide walks you through creating your first Workspace, step by step, from signup to running a complete workflow. Learn to build and test workflows with our user-friendly interface.

<Steps>
  <Step title="Sign Up">
    Unlock the power of Giselle! If you're joining us for the first time, create your account on the [sign up](https://studio.giselles.ai/signup) page. If
    you're already part of the Giselle community, [log in](https://studio.giselles.ai/login) to jump right in.
  </Step>

  <Step title="Build a Workspace">
    <AccordionGroup>
      <Accordion title="Create a Workspace" defaultOpen={true}>
        Go to the [Workspaces](https://studio.giselles.ai/workspaces) page and click the "New Workspace" button in the top right to start creating your first Workspace.
      </Accordion>

      <Accordion title="Place a Node" defaultOpen={true}>
        From the toolbar at the bottom, drag and drop a "Generator" node onto the canvas to place it. This will be the first node in your workflow.
      </Accordion>

      <Accordion title="Set the Prompt" defaultOpen={true}>
        In the right panel, open the "Prompt" tab and enter your prompt in the text area. This text will guide how the node works.

        ```markdown  theme={null}
        Suggest one interesting topic related to animals.
        ```
      </Accordion>

      <Accordion title="Select a Model" defaultOpen={true}>
        In the "Model" tab, select the AI model provider (OpenAI, Anthropic, Google, etc.) and the specific model you want to use.
      </Accordion>

      <Accordion title="Test the Node" defaultOpen={true}>
        Click the "Generate" button (or press Cmd+Enter) at the top of the right panel. This will execute only this node, allowing you to test your prompt and see the output.
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Run as a Workflow">
    <AccordionGroup>
      <Accordion title="Add Another Node" defaultOpen={true}>
        To build a workflow, let's add another node. Drag the "Generator" node from the bottom toolbar and place it on the canvas.
      </Accordion>

      <Accordion title="Connect the Nodes" defaultOpen={true}>
        To connect the two nodes, drag from the Output port of the first node to the Input port of the second node.
      </Accordion>

      <Accordion title="Set the Second Node's Prompt" defaultOpen={true}>
        Enter the following into the "Prompt" tab of the second node. By feeding the output of the first node into the second node, a continuous workflow is built.

        ```markdown  theme={null}
        Please research on the following topics:
        ```
      </Accordion>

      <Accordion title="Run the Workflow" defaultOpen={true}>
        Finally, click the "Run" button in the upper right corner to execute the workflow. This will run both nodes in sequence and generate the final output. Congratulations, you've run your first workflow in Giselle!
      </Accordion>
    </AccordionGroup>
  </Step>
</Steps>


# About Giselle
Source: https://docs.giselles.ai/en/guides/introduction

Welcome to the home of Giselle documentation!

Giselle is your intuitive, no-code AI application builder designed to unlock the full potential of generative AI. Whether you're automating research, streamlining team workflows, or building custom AI agents, Giselle helps you go from idea to production—fast.

Built with a powerful visual editor and seamless integrations, Giselle empowers individuals and teams to collaborate with AI like never before.

<Frame>
  <img src="https://mintcdn.com/giselle/vlnHNRyXbutP6jGh/en/images/introduction/screen.png?fit=max&auto=format&n=vlnHNRyXbutP6jGh&q=85&s=2e7039d81de62279697bfaa1f3da5284" data-og-width="2348" width="2348" data-og-height="1318" height="1318" data-path="en/images/introduction/screen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/giselle/vlnHNRyXbutP6jGh/en/images/introduction/screen.png?w=280&fit=max&auto=format&n=vlnHNRyXbutP6jGh&q=85&s=853b67d9d8e13481ab4bc95d4de717c4 280w, https://mintcdn.com/giselle/vlnHNRyXbutP6jGh/en/images/introduction/screen.png?w=560&fit=max&auto=format&n=vlnHNRyXbutP6jGh&q=85&s=a24ee30b30603f366d68b715f3c50184 560w, https://mintcdn.com/giselle/vlnHNRyXbutP6jGh/en/images/introduction/screen.png?w=840&fit=max&auto=format&n=vlnHNRyXbutP6jGh&q=85&s=26a312fbbb7d0ee18c3d8df35e178aa6 840w, https://mintcdn.com/giselle/vlnHNRyXbutP6jGh/en/images/introduction/screen.png?w=1100&fit=max&auto=format&n=vlnHNRyXbutP6jGh&q=85&s=7d0a5017091cb80864c054e96cf7c6f4 1100w, https://mintcdn.com/giselle/vlnHNRyXbutP6jGh/en/images/introduction/screen.png?w=1650&fit=max&auto=format&n=vlnHNRyXbutP6jGh&q=85&s=1a16b640fcb0d2a6dec92f5376abdc05 1650w, https://mintcdn.com/giselle/vlnHNRyXbutP6jGh/en/images/introduction/screen.png?w=2500&fit=max&auto=format&n=vlnHNRyXbutP6jGh&q=85&s=bea5f4939f5d42ef153ca32c39fbb32b 2500w" />
</Frame>

***

## Core Features

Giselle helps you create, deploy, and manage AI apps in minutes with no code. Here's how it fits into your workflow:

### Visual Node Editor

Design your AI applications using our drag-and-drop system. Automate complex tasks with clear, modular logic.

### Multi-Model AI Collaboration

Use OpenAI, Anthropic, Google Gemini, and more—together in a single app. Create powerful workflows by combining the best of each model.

### GitHub Integration

Trigger your AI apps with GitHub events—automate code reviews, documentation, or issue triaging.

### Team Knowledge Sharing

Build and refine AI agents collaboratively. Share your apps and agents with your team to scale your expertise.

***


# Billing
Source: https://docs.giselles.ai/en/guides/learn-about/billing

Manage your personal account billing and payments

## Payment Guide

This guide explains how Giselle's pricing system works, including subscription management, billing cycles, and secure payments. Giselle uses [Stripe](https://stripe.com) for simplified billing to ensure safe and reliable transactions.

***

## How to Access Billing Settings

After logging in, you can access　[Settings > Team > Billing](https://studio.giselles.ai/settings/team/billing) by selecting "Billing" from the sidebar menu.

From this page, you can access the dedicated billing portal provided by Stripe.
In the Stripe billing portal, you can:

View your current subscription details
Update your payment method
View invoice history
Cancel your subscription

Subscription cancellation is possible through the Stripe management screen. You cannot cancel directly from the Giselle management interface.

***

## About the Billing Cycle

* Subscriptions are billed on a monthly recurring basis, starting from your subscription date
* Your subscription automatically renews on the same day each month (e.g., May 5)
* Payments are processed automatically through your registered payment method

***

## Current Plans and Pricing

For detailed information about our current plans and pricing options, please visit [Our Pricing page](https://giselles.ai/pricing)

Alternatively, you can refer to our documentation at [Plan](plan) for comprehensive plan details and feature comparisons.

For any specific pricing questions not covered on these pages, please contact our support team.

***

## How AI Model Usage is Billed

* The Free Plan includes 30 minutes of AI usage per month (limited-time offer)
* The Pro Plan includes unlimited AI model usage during the promotional period
* Users will be notified one month before the promotion ends

***

## How to View and Download Invoices

You can view and download your invoice history in the Stripe billing portal. Each invoice shows:

* Date of payment
* Amount charged
* Payment status
* Description of services

From the Stripe portal, you can download both invoices and receipts for your records or accounting purposes. Simply locate the invoice you need and use the download options provided.

***

## How to Update Payment Method

To update your payment information:

1. Go to the [Billing section](https://studio.giselles.ai/settings/team/billing) in Settings
2. Access the Stripe billing portal
3. Look for the "Payment Method" section
4. Modify your payment details, where you can:
   * Update your credit card information
   * Change to a different payment method

All changes to your payment information will be securely processed and stored by Stripe.

***

## How to Cancel a Subscription

To cancel your subscription:

1. Go to [Billing settings](https://studio.giselles.ai/settings/team/billing)
2. Click "Cancel subscription"
3. Review the cancellation information
4. Click the "Cancel subscription" button to confirm

Your subscription will remain active until the end of your current billing period. If you change your mind before the end date, you can renew your subscription.

***

## Payment Processing

* All payments are processed securely through Stripe
* Supported payment methods include major credit cards
* Payment information is stored securely by Stripe, not by Giselle

If you have questions not covered in this guide or encounter any billing-related issues, please contact: **[support@giselles.ai](mailto:support@giselles.ai)**

Include your account information and a description of your issue for prompt assistance.


# Open Source License
Source: https://docs.giselles.ai/en/guides/learn-about/open-source-license

Learn about Giselle's open-source license and how it applies to your usage

Giselle Community Edition is open-source and released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). This allows you to freely use, modify, and distribute the software, with certain conditions. For complete terms, please refer to the [`LICENSE`](https://github.com/giselles-ai/giselle/blob/main/LICENSE) file in the GitHub repository.

This license grants you:

* Commercial and non-commercial usage
* Modification and redistribution
* Use in proprietary products (with attribution)

However, it **does not** grant use of Giselle's **name, logo, or trademarks** without explicit permission, as outlined in section 6 of the license.

If you have any questions or concerns regarding licensing or usage rights, please contact: **[support@giselles.ai](mailto:support@giselles.ai)**

We appreciate contributions from the community. For details on how to contribute, please refer to our [Contributing Guide](https://github.com/giselles-ai/giselle/blob/main/CONTRIBUTING.md).


# Plans
Source: https://docs.giselles.ai/en/guides/learn-about/plans

Understand your Giselle subscription.

## Available Plans

For the latest information about our plans and pricing options,please visit [Our Pricing page](https://giselles.ai/pricing)

### Free Plan

Ideal for solo developers exploring AI agents.

* **30 minutes** of AI model usage per month (\$3 monthly credit)
* Access to basic AI models
* Create and deploy agents with no-code builder
* Single-user account
* Managed cloud deployment

### Pro Plan

Built for individual power users.

* **\$20/month**
* **Unlimited** AI model usage (limited-time promotional offer)
* Access to all premium AI models
* All Free plan features included
* Single-user account
* Managed cloud deployment
* Email support

### Team Plan

Designed for teams collaborating on AI agents. (Coming soon)

* Contact sales for pricing
* All Pro plan features included
* Team collaboration with multiple users
* Member invitation and role management
* Advanced team administration
* Priority email support

## Monthly AI Model Usage Details

Each Giselle subscription includes monthly AI model usage credits:

* **Free Plan:** Monthly limit of 30 minutes of AI usage. Once the monthly limit is reached, AI usage pauses until the next billing cycle.
* **Pro Plan:** Includes \$20 worth of monthly AI usage credits. During the current limited-time promotion, all usage beyond the standard monthly credits is unlimited at no additional cost.

AI model usage credits are refreshed monthly and unused credits do not roll over.

## Plan Changes & Billing Information

### Upgrading from Free to Pro

* When upgrading, Free plan unused credits are discarded.
* Pro plan benefits, including unlimited promotional usage, become immediately available upon upgrade.

### Downgrading from Pro to Free

* Downgrades take effect at the end of the current billing cycle.
* Pro benefits remain available until the downgrade takes effect.

### Team Membership

* **Free Plan:** Limited to a single user, with membership to only one Free team.
* **Pro Plan:** Single-user account. Allows multiple team memberships but each team is limited to one user.
* **Team Plan:** Allows multiple team memberships with unlimited team size. Contact sales for pricing details.

### Additional Usage Costs (Pro Plan)

* During standard (non-promotional) periods, Pro plan users exceeding the \$20 monthly usage credit incur reasonable additional charges (10% fee), billed automatically at the next subscription payment cycle.

### Promotional Period

* Current unlimited usage offer for the Pro plan is temporary. Users will be notified one month before this promotion ends.

***

For detailed pricing and further information, visit the [Giselle Pricing page](https://giselles.ai/pricing) or contact [support@giselles.ai](mailto:support@giselles.ai).


# Privacy & Security
Source: https://docs.giselles.ai/en/guides/learn-about/privacy-security

Manage your account security and privacy settings

A guide to Giselle’s privacy settings, data handling, security practices, and our commitment to information protection.

Giselle is developed and operated by [ROUTE06, Inc.](https://route06.com), a company that has obtained **ISO/IEC 27001:2013 (JIS Q 27001:2014)** [certification(IS 779274)](https://www.bsigroup.com/en-US/products-and-services/assessment-and-certification/validation-and-verification/client-directory-profile/ROUTE0-0047877345-000) for its **Information Security Management System (ISMS)**. This means your data is protected not only by modern infrastructure and encryption standards but also by strict organizational policies that meet global compliance benchmarks.

***

## Quick Links

* [Privacy Policy](https://giselles.ai/legal/privacy)
* [Terms of Service](https://giselles.ai/legal/terms)
* [Billing Portal](https://studio.giselles.ai/settings/team/billing)
* [ROUTE06 ISMS Certification Announcement](https://route06.com/news/isms)

***

## ISMS Certification

ROUTE06 is officially certified under the **ISO/IEC 27001** standard by **BSI Group Japan K.K.**

* **Certification ID**: IS 779274
* **Scope**: Enterprise software provision, digital product design and development, DX consulting, and more
* **Date of Initial Certification**: February 12, 2023

> This certification demonstrates ROUTE06’s commitment to **confidentiality, integrity, and availability** of data. We continually monitor and improve our systems to maintain high standards of information security.

***

## Security Overview

Giselle benefits from ROUTE06’s ISMS-backed security infrastructure, including:

### Organizational Security

* ISMS certification under **ISO/IEC 27001:2013**
* Role-based access control for internal staff
* Regular audits, internal self-assessments, and third-party penetration tests

### Administrative Measures

* Confidentiality agreements and security training for employees
* Defined procedures for incident reporting and escalation
* Data protection roles clearly defined

### Technical Safeguards

* TLS encryption in transit
* Strict access controls and API rate limiting
* Secure cloud infrastructure (AWS, Supabase, Vercel)

### Physical Safeguards

* Secure facilities via our cloud providers
* Hardware and device-level protection policies for remote-first teams

***

Submit requests via your account or by emailing [support@giselles.ai](mailto:support@giselles.ai).


# Usage
Source: https://docs.giselles.ai/en/guides/learn-about/usage

Monitor and manage your team's resource usage

## Usage Overview

Giselle monitors and manages your team's use of its features and resources to ensure optimal performance and availability.

### Resource Metrics

Giselle internally tracks detailed metrics related to AI model utilization, distinguishing between Free and Pro plan allocations.

## Usage Limits

Each subscription plan has defined usage limits to maintain consistent service levels.

### Current Plan Limits

Subscription plans include:

* **Free plan**: Limited-time offer of 30 minutes of AI model usage (normally \$3 worth of credits per month)
* **Pro plan**: \$20 per month with limited-time unlimited AI model usage during the promotional period
* **Team plan**: Contact sales for pricing. All Pro plan features plus team collaboration capabilities
* **Team member seats**: 1 user for Free and Pro plans; multiple users available with Team plans (contact sales for pricing)

## Usage Reports

Giselle generates detailed internal reports on resource usage for analysis and planning.

## Usage Monitoring

Giselle regularly reviews usage data to ensure accuracy. The usage information displayed in the system is updated throughout the day, but discrepancies may occur due to API issues or other technical factors affecting the AI model.

If Giselle detects significant inconsistencies or unusual patterns in your usage data, the support team may contact you directly. Likewise, if you notice any discrepancies or have questions about your reported usage, please don't hesitate to reach out to the support team at [support@giselles.ai](mailto:support@giselles.ai).

Giselle is continuously improving its monitoring systems to provide you with the most accurate and up-to-date information possible.


# Authentication
Source: https://docs.giselles.ai/en/guides/settings/account/authentication

Connect your Giselle account with third-party services to simplify login.

<Info>
  You can access the Authentication settings page by navigating to [Settings > Account > Authentication](https://studio.giselles.ai/settings/account/authentication).
</Info>

### Connecting External Services

You can connect your Giselle account with external services such as Google and GitHub to streamline the login process. You can easily manage these connections:

* **Google**\
  Connect or reconnect your Giselle account with your Google account.

* **GitHub**\
  Connect or disconnect your Giselle account with your GitHub account.

You can manage your connections directly from the Authentication settings page.


# General
Source: https://docs.giselles.ai/en/guides/settings/account/general

Configure your account basic settings and preferences

<Info>
  You can access the General settings page by navigating to [Settings > Account > General](https://studio.giselles.ai/settings/account/general).
</Info>

### Display Name

You can edit your display name by clicking the "Edit" button on the General Settings page, entering your preferred name, and clicking "Save".

### Email Address

Your email address is displayed here and is used for account-related notifications. This email address cannot be edited directly in this view.

### Session Management

You can securely log out of all active sessions by clicking the "Log Out" button in the Session section.

Our team is actively working to bring additional configuration options to you soon. Stay tuned for updates!


# Account Overview
Source: https://docs.giselles.ai/en/guides/settings/account/overview

View and manage your teams.

<Info>
  You can access the Account Overview page by navigating to [Settings > Account > Overview](https://studio.giselles.ai/settings/account).
</Info>

## Account Overview Page Summary

The Account Overview page displays all teams you belong to and allows you to switch between teams and manage team settings. You can create new teams or leave existing teams.

## Team List

### Team Information Display

Each team card displays the following information:

* **Team Avatar**: Team profile image (or random image if not set)
* **Team Name**: Display name of the team
* **Plan Badge**: Pro Plan or Free Plan indicator
* **Role**: Admin or Member designation
* **Action Menu**: Dropdown menu for team operations (...)

### Team Search and Filter

A search field is available at the top of the team list to filter teams by name:

* Real-time search (filters instantly as you type)
* Case-insensitive search
* Shows only teams matching the search criteria

### Team Actions

Click the menu icon (...) in the top-right corner of each team card to access the following actions:

#### Apps

* Navigate to the team's apps page
* Switches to that team's context and redirects to `/workspaces` page

#### Settings

* Navigate to team settings page
* Switches to that team's context and redirects to `/settings/team` page

#### Leave team

* Leave the team
* Requires confirmation before execution
* Cannot leave if:
  * It's your only team
  * You are the last admin of the team

<Warning>
  Leaving a team will remove your access to all apps, workflows, and data in that team. This action cannot be undone.
</Warning>

## Creating a New Team

### Create New Team Button

You can create a new team using the **Create New Team** button at the top of the team list.

#### Creation Restrictions

* **Free Plan Users**: Can create only 1 team
* **Pro Plan Users**: Can create multiple teams (single-user per team)
* **Team Plan Users**: Can create multiple teams with multiple members

<Note>
  Upgrading to Pro Plan is required to create multiple teams. For team collaboration features, contact sales about Team Plan. See the [pricing page](https://giselles.ai/pricing) for details.
</Note>

#### Creation Steps

1. Click the **Create New Team** button
2. A team creation dialog will appear
3. Enter a team name (1-256 characters)
4. Optionally select a team avatar image
5. Click **Create** to complete creation

The created team will be automatically selected as your current team and added to the team list.

## Plans and Roles

### Plan Types

**Free Plan**:

* Can create only 1 team
* Basic features available

**Pro Plan**:

* Can create multiple teams
* Single-user account per team
* Advanced features and integrations
* See the [Plans page](/en/guides/learn-about/plans) for details

**Team Plan**:

* Can create multiple teams
* Invite and manage team members
* All Pro plan features plus team collaboration
* Contact sales for more information

### Role Types

**Admin (Administrator)**:

* Invite and remove team members
* Manage team settings
* Delete teams
* Access to all apps and workflows

**Member**:

* Access to apps and workflows
* Can only leave teams themselves
* No team management permissions

For detailed permissions, see the [Members documentation](/en/guides/settings/team/members).

## Related Pages

From Account Settings, you can also access the following settings pages:

* [General](/en/guides/settings/account/general) - Display name, email address, session management
* [Authentication](/en/guides/settings/account/authentication) - Google and GitHub authentication integration

These pages can be accessed from the sidebar menu on the left side of the page.

## Support

If you have questions or encounter issues with team management, please contact our support team at [support@giselles.ai](mailto:support@giselles.ai).


# Team Settings
Source: https://docs.giselles.ai/en/guides/settings/team/general

Manage your team's profile, plan, and other settings.

<Info>
  You can access the Team Settings page by navigating to [Settings > Team Settings](https://studio.giselles.ai/settings/team).
</Info>

## Team Settings Page Overview

The Team Settings page provides centralized management of key team settings. You can edit your team profile, manage your plan, delete your team, and access detailed configuration pages.

From this page, you can also access the following detailed settings pages:

* **Members**: Invite and manage team members
* **Integrations**: Configure external service connections
* **Vector Stores**: Manage document and code vector stores
* **Usage**: Track agent usage and activity

## Team Profile

The Team Profile section allows you to manage your team's display name and profile image.

### Viewing Team Information

The Team Profile card displays:

* **Team Avatar**: 48x48 pixel circular image
* **Team Name**: Click to edit
* **Edit Button**: Opens the profile editing dialog

### Editing Team Profile

Click the **Edit** button to open the "Edit Team Profile" dialog.

#### Editable Fields

**Team Name**:

* Must be between 1 and 256 characters
* Required field
* Cannot be blank or whitespace only

**Profile Image**:

* Supported formats: JPG, PNG, GIF, WebP
* Maximum file size: 1MB
* Image preview available
* If not set, displays team name initials

#### Editing Steps

1. Click the **Edit** button
2. Enter team name (1-256 characters)
3. Optionally select a profile image
4. Review the preview
5. Click **Save** to save changes

<Note>
  Image uploads are limited to 1MB. Supported formats are JPEG, PNG, GIF, and WebP.
</Note>

### Validation

The following validations are performed when editing:

* **Team Name**: Must be 1-256 characters
* **Image Format**: JPG, PNG, GIF, or WebP only
* **Image Size**: 1MB or less

If validation errors occur, error messages will be displayed and saving will be prevented.

## Plan Management

Different information and actions are displayed based on your team's current plan.

### Free Plan

For teams on the Free Plan, the following is displayed:

#### Display Content

* **Heading**: "Free Plan"
* **Description**: "Have questions about your plan?"
* **Pricing Link**: "Learn about plans and pricing" (links to [https://giselles.ai/pricing](https://giselles.ai/pricing))

#### Actions

**Upgrade to Pro Button**:

* Initiates upgrade to Pro Plan
* Clicking starts the upgrade process
* Redirects to Stripe checkout

### Pro Plan

For teams on the Pro Plan, the following is displayed:

#### Display Content

* **Heading**: "Pro Plan" (displayed in primary color)
* **Description**: "Have questions about your plan?"
* **Pricing Link**: "Learn about plans and pricing" (links to [https://giselles.ai/pricing](https://giselles.ai/pricing))
* **Cancellation Notice** (if applicable): "Subscription will end on \[date]" (displayed in warning color)

#### Actions

**Manage Subscription Button**:

* Opens subscription management interface
* Redirects to Stripe customer portal
* Available operations:
  * Change payment method
  * Cancel subscription
  * View invoices and receipts

<Info>
  Subscription management is handled through the Stripe customer portal. You can update payment information, cancel your plan, and view billing history.
</Info>

### Cancellation Schedule

If you cancel your Pro Plan subscription, the following is displayed:

* Cancellation notice: "Subscription will end on \[end date]"
* You can continue using Pro Plan features until the end date
* Automatically switches to Free Plan after the end date

<Warning>
  Canceling your subscription will prevent access to Pro Plan features after the end date.
</Warning>

## Danger Zone

The Danger Zone section allows you to completely delete your team. This action is irreversible and requires caution.

### Deleting a Team

#### Deletion Requirements

To delete a team, all of the following conditions must be met:

1. **Admin Permission**: You must be a team administrator
2. **Free Plan**: Pro Plan teams cannot be deleted (you must cancel the plan first)
3. **Multiple Team Membership**: You must belong to at least one other team (your only team cannot be deleted)

#### Deletion Steps

1. Click the **Delete Team** button
2. A confirmation dialog is displayed
   * Title: "Delete Team"
   * Description: "This action cannot be undone. This will permanently delete the team and remove all members."
3. Confirm deletion by clicking **Delete Team**
4. Team is deleted and you are automatically switched to another team

<Warning>
  Deleting a team will permanently delete all of the following data:

  * Team profile
  * All team members
  * Team apps and workflows
  * Vector Stores and documents
  * Integration settings
  * Usage history

  This action cannot be undone. We strongly recommend backing up important data before deletion.
</Warning>

#### Deletion Restrictions

You cannot delete a team in the following cases:

* **Active Pro Plan**: You must first cancel the subscription and wait until the plan ends
* **Only Team**: Your last team cannot be deleted. At least one team is required
* **Member Permission**: You cannot delete without Admin permission

If deletion is not possible, the delete button will not be displayed or an error message will be shown when clicked.

## Related Pages

From Team Settings, you can access the following detailed settings pages:

* [Members](/en/guides/settings/team/members) - Invite and manage team members
* [Integrations](/en/guides/settings/team/integrations) - Connect external services like GitHub
* [Vector Stores](/en/guides/settings/team/vector-stores) - Document and code vector stores
* [Usage](/en/guides/settings/team/usage) - Agent usage and activity

These pages can be accessed from the navigation menu at the top of the page.

## Support

If you have questions or encounter issues with Team Settings, please contact our support team at [support@giselles.ai](mailto:support@giselles.ai).

For information about plans and pricing, visit the [pricing page](https://giselles.ai/pricing).


# Integrations
Source: https://docs.giselles.ai/en/guides/settings/team/integrations

Configure and manage integrations with external services for your team.

<Info>
  You can access the Integrations page by navigating to [Settings > Team > Integrations](https://studio.giselles.ai/settings/team/integrations).
</Info>

## Integrations Page Overview

The Integrations page allows you to connect and manage external services with Giselle. Currently, GitHub integration is supported, enabling access to GitHub repositories and management of GitHub App installations.

## GitHub Integration

### Connecting Your GitHub Account

To set up GitHub integration for the first time:

1. Click the **Configure GitHub App** button on the Integrations page
2. Navigate to the [account authentication page](/en/guides/settings/account/authentication)
3. Follow the on-screen instructions to authenticate your GitHub account

<Note>
  When your GitHub account is not connected, you'll see "Not connected" displayed with a "Configure GitHub App" button.
</Note>

### GitHub App Installation

The GitHub App is required for Giselle to access your GitHub repositories.

#### New Installation

1. Click **Add Giselle's GitHub App** or **Configure Giselle's GitHub App** button on the Integrations page
2. A popup window will open with the GitHub installation page
3. Select where to install (personal account or organization)
4. Choose which repositories to grant access to:
   * All repositories
   * Only select repositories
5. Click **Install** to complete the installation
6. The popup window will close automatically and the page will refresh

#### Managing Installations

The Integrations page displays installed GitHub Apps in the following format:

* **Login status**: Displayed as "Logged in as (@username)"
* **Installation cards**: A card is displayed for each installation
  * Account/organization name where installed
  * Avatar image
  * List of accessible repositories
  * Repository visibility status (Private/Public badge)
  * Links to repositories (opens in GitHub)

<Warning>
  Each installation can retrieve up to 100 repositories. A warning will be displayed if the limit is exceeded.
</Warning>

### Authentication Status and Troubleshooting

#### Authentication Error

When your GitHub authentication token is expired or invalid, an "Authentication Error" will be displayed. In this case:

1. Review the displayed error message
2. Re-authenticate via the [account authentication page](/en/guides/settings/account/authentication)

#### Automatic Token Refresh

Giselle automatically refreshes your GitHub access tokens:

* Automatically checks token expiration
* Uses refresh tokens to auto-renew before expiration
* Displays an error if refresh fails

### Uninstalling GitHub App

To uninstall the GitHub App, use the GitHub settings:

1. Open your GitHub account settings
2. Navigate to **Settings > Applications > Installed GitHub Apps**
3. Find "Giselle"
4. Click **Uninstall** in the Danger Zone section

<Warning>
  Uninstalling the GitHub App will immediately revoke all access permissions from Giselle to those repositories. Related workflows and triggers may stop functioning.
</Warning>

### Disconnecting GitHub Account

To disconnect your GitHub account itself:

1. Navigate to the [account authentication page](/en/guides/settings/account/authentication)
2. Follow the disconnection steps

<Note>
  You can only disconnect your GitHub account if you have multiple authentication methods configured. The last authentication method cannot be removed.
</Note>

## Permissions and Access Control

### Team Member Access

* The Integrations page is accessible to all team members
* GitHub App installations are shared across the entire team
* Team members can access repositories selected in each installation

### GitHub App Permissions

The GitHub App has the following permissions configured:

* Read access to repository metadata
* Read access to repository contents
* Other permissions necessary for Giselle functionality

<Info>
  Specific permission details can be reviewed on the GitHub App installation page.
</Info>

## Leveraging Integrations

### Using Repository Information

Connected GitHub repositories can be utilized in the following features:

* **Vector Stores**: Ingest repository contents as a knowledge base
* **Workflow Triggers**: Execute workflows triggered by repository events

<Note>
  For vector store configuration, refer to the [Vector Stores documentation](/en/guides/settings/team/vector-stores).
</Note>

## Future Support

While currently only GitHub integration is supported, we plan to add more external service integrations in the future.

## Support

If you encounter issues with integration setup or have questions, please contact our support team at [support@giselles.ai](mailto:support@giselles.ai).


# Members
Source: https://docs.giselles.ai/en/guides/settings/team/members

Invite, manage, and oversee team members' access to your Giselle apps.

<Info>
  You can access the Members page by navigating to [Settings > Team > Members](https://studio.giselles.ai/settings/team/members).
</Info>

## Members Overview

The Members page allows administrators to comprehensively manage member access within your team. You can invite new members, modify roles, remove members, and manage invitations.

<Note>
  Member invitations and role management are available to administrators on **Team Plan** only. This feature is not available on Free or Pro plans.
</Note>

## Member Roles & Permissions

There are two roles available in a team:

### Admin

* Invite and remove members
* Change member roles
* Manage team settings (integrations, billing, etc.)
* Access to all AI apps

### Member

* Access to AI apps
* Can only leave the team themselves
* No member management permissions

| Action                    | Admin              | Member |
| ------------------------- | ------------------ | ------ |
| Invite members            | ✓ (Team Plan only) | ✗      |
| Change other member roles | ✓ (Team Plan only) | ✗      |
| Change own role           | ✗                  | ✗      |
| Remove other members      | ✓                  | ✗      |
| Leave team                | ✓                  | ✓      |

## Inviting Members

### How to Invite New Members

<Steps>
  <Step title="Open the invite dialog">
    Click the **Invite Member** button (visible only to Team Plan admins).
  </Step>

  <Step title="Enter email addresses">
    Enter the email addresses of the members you want to invite in the email input field.

    * You can enter multiple email addresses (separated by commas, semicolons, or spaces)
    * Press Enter or click outside the field to add email tags
    * Added email addresses appear as removable tags
  </Step>

  <Step title="Select a role">
    Choose the role for the invited members:

    * **Member**: Standard user access
    * **Admin**: Full administrative privileges
  </Step>

  <Step title="Send invitations">
    Click the **Invite** button to send invitation emails.
  </Step>
</Steps>

### Email Validation

The following validations are automatically performed when inviting:

* **Email format validation**: Ensures valid email address format
* **Duplicate check**: Detects duplicate email addresses
* **Existing member check**: Detects email addresses already in the team
* **Already invited check**: Detects email addresses with active invitations

Email addresses that fail validation will be displayed with error messages.

### Pricing Information

<Warning>
  Each member added to your team will be charged as an additional seat on your Team Plan subscription. Please contact sales for Team Plan pricing details.
</Warning>

## Managing Invitations

### Invitation Status

Sent invitations appear at the bottom of the member list with an **"(Invitation pending)"** label.

* Invitations are valid for **24 hours**
* Expired invitations appear in red with "Expired" status
* Users who receive invitations can join the team via the link in the email

### Invitation Actions (Admins Only)

The following actions are available for each invitation:

#### Copy Invite Link

1. Click the options icon (**...**) next to the invitation
2. Select **Copy invite link**
3. The link is copied to your clipboard (format: `/join/{token}`)

#### Resend Invitation

Use this when an invitation has expired or the email wasn't received:

1. Click the options icon (**...**)
2. Select **Resend invitation**
3. The old invitation is revoked and a new 24-hour invitation is created
4. The invitation email is resent with the same email address and role

#### Revoke Invitation

1. Click the options icon (**...**)
2. Select **Revoke invitation**
3. Confirm in the confirmation dialog
4. The invitation is permanently revoked (the invite link becomes invalid)

## Changing Member Roles

<Note>
  Role changes can only be performed by **Team Plan** administrators.
</Note>

### How to Change a Role

1. Click the role dropdown for the member you want to change
2. Select the new role (**Admin** or **Member**)
3. The role is updated immediately

### Restrictions

You cannot change roles in the following cases:

* **Last admin**: If there is only one admin in the team, you cannot downgrade that admin to Member
* **Own role**: You cannot change your own role

<Warning>
  A team must always have at least one administrator.
</Warning>

## Removing Members

### How to Remove a Member

1. Click the options icon (**...**) next to the member's name
2. Select **Remove from Team**
3. Confirm the removal in the confirmation dialog
4. The member is immediately removed from the team

### Removal Restrictions

You cannot remove members in the following cases:

* **Last member**: If there is only one member in the team, you cannot remove that member
* **Last admin**: If the member you're trying to remove is the last admin, you cannot remove them
* **Only team**: If you're trying to remove yourself and it's your only team, you cannot leave

<Warning>
  Removing a member will immediately revoke all their access to Giselle apps. This action cannot be undone.
</Warning>

### Leaving a Team

Both regular members and admins can remove themselves from a team (unless restricted by the above conditions):

* You must belong to other teams
* If you're the last admin, you need to promote another member to admin first

## Member Details Display

Each member entry displays the following information:

* **Avatar image**: User's profile image (36×36 pixels)
* **Display name**: User's name (shows "**No display name**" if not set)
* **Email address**: User's email address
* **Role**: Current role (Admin or Member)

## Notifications & Feedback

Operation results are displayed as toast notifications at the top of the screen:

* **Success**: "Role updated: Admin", "Member removed", "Invitation resent!", etc.
* **Error**: Specific error messages (e.g., "Cannot remove the last admin from the team")
* **Info**: "Invite link copied!", etc.

When errors occur, detailed error messages may also appear below the member row.

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Can I invite multiple members at once?">
    Yes, you can enter multiple email addresses in the invite dialog. Separate them with commas, semicolons, or spaces. All invitations will be sent with the same role.
  </Accordion>

  <Accordion title="What should I do if an invitation expires?">
    Admins can resend invitations. Resending creates a new 24-hour invitation and sends it to the same email address.
  </Accordion>

  <Accordion title="What happens if the last admin leaves?">
    The system prevents the removal of the last admin. Before leaving, you need to promote another member to admin.
  </Accordion>

  <Accordion title="Can I re-invite a member after removing them?">
    Yes, removed members can be re-invited as new members. However, their previous access rights and settings will not be restored.
  </Accordion>

  <Accordion title="Can I invite members on the Free or Pro Plan?">
    No, member invitations and role management are Team Plan features only. Free and Pro plans are designed for individual users. Please contact sales to learn more about Team Plan.
  </Accordion>
</AccordionGroup>

## Support

For assistance or if you encounter issues managing team members, please contact our support team at [support@giselles.ai](mailto:support@giselles.ai).


# Usage
Source: https://docs.giselles.ai/en/guides/settings/team/usage

Monitor and manage your team's AI app usage

<Info>
  You can access the Usage page by navigating to [Settings > Team > Usage](https://studio.giselles.ai/settings/team/usage).
</Info>

## Usage Overview

Monitor your team's AI app usage clearly and efficiently. Recently, we've transitioned from calculating usage based on minutes to a credit-based system.

### Resource Metrics

Giselle tracks your team's AI app runtime in minutes for informational purposes only. This monitoring currently does not directly relate to your billing, as billing is now calculated through credits.

## Usage Limits

Your subscription plan includes AI model usage credits each month:

* **Free Plan**: 30 minutes per month (limited-time promotion)
* **Pro Plan**: Unlimited usage during the promotional period

Note: App runtime displayed in minutes is separate from your actual billed credits.

## Usage Reports

Detailed logs of recent app activities, including start time, end time, and total duration, are provided for easy tracking.

## Usage Monitoring

<Warning>
  Giselle continuously updates app usage throughout the day. We are currently transitioning from time-based to credit-based monitoring. Parts of the previous UI remain and might cause confusion.
</Warning>

If you find anything unclear or have concerns regarding your usage, please contact our support team at [support@giselles.ai](mailto:support@giselles.ai).


# Vector Stores
Source: https://docs.giselles.ai/en/guides/settings/team/vector-stores

Ingest and manage GitHub repositories and documents as knowledge bases.

<Info>
  You can access the Vector Stores page by navigating to [Settings > Team > Vector Stores](https://studio.giselles.ai/settings/team/vector-stores).
</Info>

## Vector Stores Page Overview

The Vector Stores page allows you to ingest and manage your project's code and documents into Vector Stores. The ingested data can be utilized in GitHub Vector Store Nodes and Document Vector Store Nodes.

Currently, two types of Vector Stores are supported:

* **Document Vector Stores**: Ingest PDF, TXT, and Markdown files
* **GitHub Repositories**: Ingest code, Issues, and Pull Requests from GitHub repositories

## Document Vector Stores

<Note>
  A sidebar navigation with "Document" and "GitHub" options will appear on the left side of the page.
</Note>

Document Vector Stores allows you to upload PDF, TXT, and Markdown files to ingest into Vector Stores.

### Creating a Document Vector Store

1. Click the **New Vector Store** button
2. The "Create Vector Store" dialog opens
3. Configure the following items:

#### Name

Enter a name for the Vector Store (e.g., "Product Docs")

#### Embedding Models

Select at least one embedding model to use

Each model displays:

* Model name
* Provider
* Dimensions

4. Click **Create** to complete creation

### Managing Document Vector Stores

Created Document Vector Stores are displayed in the "Document Vector Stores" section.

Each Vector Store card displays:

* Store name
* Store ID
* Action menu (three-dot icon)

#### Action Menu

* **Configure Sources**: Update name, embedding models, and source files
* **Delete**: Delete the Document Vector Store

### Uploading and Managing Files

To upload files to a Document Vector Store:

1. Select **Configure Sources** from the action menu
2. The "Configure Sources" dialog opens

#### Name Section

You can update the Vector Store name.

#### Embedding Models Section

Select embedding models to use (at least one required)

#### Source Files Section

**Supported file formats**: PDF, TXT, Markdown (.md)
**Maximum file size**: 4.5MB

File upload methods:

* Drag and drop to add files
* Click the **Select files** button to choose files

#### Uploaded Files List

Uploaded files are displayed with the following information:

* **File name**: Truncated if long
* **Status badge**:
  * **Pending** (yellow, clock icon): Waiting for ingestion
  * **Processing** (blue, loading icon): Processing
  * **Ready** (green, check icon): Ingestion complete
  * **Failed** (red, alert icon): Ingestion failed
* **Delete button**: Can delete each file (trash icon)

<Note>
  Hover over a failed file to see the error code in a tooltip.
</Note>

3. Click **Save** to save changes

After uploading files, the ingestion process starts automatically.

### Deleting a Document Vector Store

To delete a Document Vector Store:

1. Select **Delete** from the action menu
2. Confirm in the "Delete Document Vector Store" dialog
3. Execute deletion

<Warning>
  Deletion cannot be undone. The Document Vector Store and its embedding profiles and source files will be permanently deleted.
</Warning>

## GitHub Repositories

To use GitHub Vector Stores:

1. **GitHub Account Authentication**: Connect your GitHub account on the [account authentication page](/en/guides/settings/account/authentication)
2. **GitHub App Installation**: Install Giselle's GitHub App from [Integrations settings](/en/guides/settings/team/integrations)

If these conditions are not met, a guidance message will be displayed on the Vector Stores page.

### Registering a Repository

Steps to register a GitHub repository to Vector Store:

1. Click the **Register Repository** button
2. The "Register GitHub Repository" dialog opens
3. Configure the following items:

#### Owner / Organization

Select from installed GitHub Apps. You can choose a personal account or organization.

#### Repository Name

Select from repositories under the selected Owner.

#### Sources to Ingest

Select content types to ingest:

* **Code**: Ingest source code files (required, cannot be disabled)
* **Issues**: Ingest Issue descriptions, comments, and discussions (optional)
* **Pull Requests**: Ingest merged Pull Request content and discussions (optional)

<Note>
  Code is a required content type and is always enabled.
</Note>

#### Embedding Models

Select embedding models to use for indexing. At least one model must be selected.

Available models:

* OpenAI (various sizes)
* Google (various sizes)

Each model displays provider name and dimensions.

4. Click **Register** to complete registration

### Managing Repositories

Registered repositories are displayed in the "GitHub Repositories" section.

Each repository card displays:

#### Repository Information

* Repository name (`owner/repo` format, click to go to GitHub)
* Action menu (three-dot icon)

#### Action Menu

* **Ingest Now**: Manually trigger ingestion
* **Configure Sources**: Modify content types and embedding models
* **Delete**: Remove repository from Vector Store

#### Embedding Model Status

A status card is displayed for each embedding model:

**Code Section**:

* Status badge:
  * **Enabled** (green): Enabled
  * **Running** (blue, animated): Ingestion in progress
  * **Idle** (gray): Idle state
  * **Error** (red): Error occurred
  * **Disabled** (gray): Disabled
* Last sync: Last sync time (relative time format)
* Latest ingested commit SHA (first 7 characters)
* Error message and retry time (when failed)

**Issues Section**:

* Similar status display as Code
* Latest ingested Issue number (if ingested)

**Pull Requests Section**:

* Similar status display as Code
* Latest ingested PR number (if ingested)

<Warning>
  If repository access fails, a "Check" link will appear on the Error status. Click it to open a diagnostic modal and attempt to restore the connection.
</Warning>

### Manual Ingestion

You can manually trigger ingestion with the **Ingest Now** button.

Conditions for ingestion:

* Status is "Idle", "Completed", or "Failed" (if retry time has passed)
* At least one content type is enabled

During ingestion, the status changes to "Running" and updates to "Completed" or "Error" upon completion.

### Configure Sources

To modify repository settings:

1. Select **Configure Sources** from the action menu
2. The "Configure Vector Stores" dialog opens

#### Sources Section

Select content types to ingest:

* **Code**: Always enabled (toggle disabled)
* **Issues**: Optional (toggle to enable/disable)
* **Pull Requests**: Optional (toggle to enable/disable)

#### Embedding Models Section

Select embedding models to use (at least one required)

3. Click **Save Changes** to save modifications

### Deleting a Repository

To delete a repository from Vector Store:

1. Select **Delete** from the action menu
2. Confirm in the "Delete Repository" dialog
3. Execute deletion

<Warning>
  Deletion cannot be undone. The repository `{owner}/{repo}` and its embedding profiles will be permanently deleted.
</Warning>

### Diagnosing and Restoring Connection

If an error occurs accessing the repository:

1. Click the **Check** link on the Error status
2. The "Checking Repository Access" modal opens and performs diagnostics
3. Actions are displayed based on diagnostic results:

#### If Restorable

* Title: "Connection can be restored"
* Message: "Click Restore Connection to reconnect and continue ingesting data from this repository."
* Button: **Restore Connection** - Click to restore connection

#### If Not Restorable

* Title: "Repository no longer accessible"
* Custom error message is displayed
* Button: **Delete Repository** - Delete the repository

Issues detected by diagnostics:

* GitHub App installation cannot access the repository
* Repository not found
* Other diagnostic errors

## Empty State

### Document Vector Stores

When no Document Vector Store is created:

* "No document vector stores yet."
* 'Use the "New Vector Store" button to create one.'

### GitHub Repositories

When no repository is registered:

* "No repositories are registered."
* 'Please register a repository using the "Register Repository" button.'

## Error Messages

The following errors may occur:

* **Repository not found.**: Repository not found
* **Rate limited.**: Rate limit reached
* **Repository too large.**: Repository is too large
* **Repository error.**: Repository error
* **Failed to upload files**: File upload failed
* **Failed to delete file**: File deletion failed

## Leveraging Vector Stores

Ingested data can be utilized in the following Nodes:

* **Document Vector Store Node**: Search and use uploaded documents
* **GitHub Vector Store Node**: Search and use code, Issues, and Pull Requests ingested from GitHub repositories

By using these Nodes, you can integrate your project's knowledge base into AI workflows.

## Support

If you encounter issues with Vector Stores configuration or have questions, please contact our support team at [support@giselles.ai](mailto:support@giselles.ai).

For more details, please refer to the [Vector Stores documentation](https://docs.giselles.ai/en/guides/settings/team/vector-stores).


# Build
Source: https://docs.giselles.ai/en/guides/workspaces/build

Learn how to build and configure workspaces in Giselle

TBD


# Anthropic
Source: https://docs.giselles.ai/en/models/providers/anthropic

Available Anthropic AI Models Overview.

## Claude Models

The following Claude models are available in the Anthropic workspace. Each model offers specific capabilities and features tailored to match your use case requirements. The "Reasoning" (Extended Thinking) capability is supported in Giselle for applicable models.

| Models                         | Generate Text | Web Search | Reasoning | Input PDF | Input Image | Context Window | Max Output | Plan\@Giselle |
| :----------------------------- | :------------ | :--------- | :-------- | :-------- | :---------- | :------------- | :--------- | :------------ |
| **claude-opus-4-1-20250805**   | ✅             | ✅          | ✅         | ✅         | ✅           | 200k tokens    | 32k tokens | Pro           |
| **claude-sonnet-4-5-20250929** | ✅             | ✅          | ✅         | ✅         | ✅           | 200k tokens    | 64k tokens | Pro           |
| **claude-haiku-4-5-20251001**  | ✅             | ✅          | ✅         | ✅         | ✅           | 200k tokens    | 64k tokens | Free          |

Please note that some features may not be available within Giselle even if they are offered in the official API. Extended thinking mode and other Anthropic API features will be gradually implemented within Giselle.

### claude-opus-4-1-20250805

Claude Opus 4.1 is Anthropic's most powerful model, designed as the ultimate coding powerhouse. It excels at complex multi-step coding, sustained long-running tasks, and advanced reasoning. With a 200k token context window and the ability to output up to 32k tokens, Opus 4.1 delivers sustained performance for several hours and is ideal for projects requiring deep understanding and persistence, such as complex refactoring or multi-repository analysis. It supports text and image inputs.

### claude-sonnet-4-5-20250929

Claude Sonnet 4.5 is one of Anthropic's latest and most powerful models, offering balanced high performance. It excels at complex coding tasks, advanced reasoning, and content generation, delivering frontier-level performance with an optimal cost-performance balance. It features a 200k token context window, can output up to 64k tokens, and supports text, PDF, and image inputs. The reasoning capability makes it particularly powerful for tasks requiring multi-step thought processes.

### claude-haiku-4-5-20251001

Claude Haiku 4.5 is optimized for speed and cost-efficiency while also supporting reasoning capabilities. It handles rapid text generation, PDF and image inputs, making it ideal for scenarios requiring real-time responsiveness. With a 200k token context window and the ability to output up to 64k tokens, it balances fast interactions with detailed responses. The extended thinking capability enables it to handle complex tasks as well.

## Model Selection Guide

Guidelines for selecting the optimal Claude model:

* **For the ultimate coding powerhouse and most complex reasoning**: `claude-opus-4-1-20250805`
* **For balanced high-performance, everyday coding, and cost-effective workflows**: `claude-sonnet-4-5-20250929`
* **For speed, cost-efficiency, with reasoning capabilities**: `claude-haiku-4-5-20251001`

## Practices for Giselle

We recommend `claude-opus-4-1-20250805` or `claude-sonnet-4-5-20250929` as your primary models in Giselle, especially for tasks involving advanced coding, complex problem-solving, and in-depth analysis. These models feature hybrid reasoning modes, automatically switching between instant responses and extended thinking based on task complexity.

`claude-haiku-4-5-20251001` excels at speed and cost-efficiency while also supporting reasoning capabilities, making it capable of handling complex thought processes even when fast responses are needed. These models excel not only at code generation, architectural design, and technical reviews but also produce remarkably natural text. Their "Reasoning" (Extended Thinking) capability, supported in Giselle, makes them particularly powerful for tasks requiring multi-step thought processes. These versatile models can be effectively utilized across a broad spectrum of tasks, from creating engaging blog articles to writing complex code implementations and performing detailed analytical work.

### Anthropic Web Search Tool

For supported Claude models, Giselle integrates the Anthropic Web Search tool, which can be configured directly from a Generator Node's **Tools** tab. This feature allows Claude to access real-time information from the web, enabling it to answer questions and generate content based on the most up-to-date data, complete with source citations.

#### Configuration

In the Generator Node, navigate to the **Tools** tab and click **Configure** next to "Anthropic Web Search." You can then:

* **Enable Tool**: Toggle the web search functionality on or off.
* **Set Maximum Uses**: Limit the number of web searches the model can perform in a single run (from 1 to 10).
* **Filter Domains**: Control the search scope by either:
  * **Allowing Specific Domains**: Restricting searches to a whitelist of trusted sources.
  * **Blocking Specific Domains**: Excluding certain websites from the search results.

For detailed specifications, performance benchmarks, or additional assistance, please refer to the [Anthropic API Documentation](https://docs.anthropic.com/en/docs/about-claude/models/all-models) and the [Claude 4 announcement](https://www.anthropic.com/news/claude-4).


# fal.ai
Source: https://docs.giselles.ai/en/models/providers/fal

Overview of Available fal.ai Image Generation Models.

## fal.ai Image Generation Models

> **Note:** fal.ai models are currently only available in the Open Source version of Giselle.

The following image generation models are available in the fal.ai workspace. Each model provides distinct features suited to different use cases, balancing speed, detail, and artistic fidelity.

| Models                     | Text-to-Image | Speed      | Detail & Fidelity | Typography   | Inference Steps  | Safety Checker           | Plan\@Giselle |
| -------------------------- | ------------- | ---------- | ----------------- | ------------ | ---------------- | ------------------------ | ------------- |
| flux-pro/v1.1              | ✅             | ⚡️ High    | ⭐️⭐️⭐️⭐️⭐️        | ✅            | Optimized        | ✅ (Tolerance levels 1-6) | Free          |
| flux/schnell               | ✅             | ⚡️⚡️ Turbo | ⭐️⭐️⭐️⭐️          | ✅            | 1-4 steps        | ✅                        | Pro           |
| stable-diffusion-v3-medium | ✅             | Moderate   | ⭐️⭐️⭐️⭐️⭐️        | ✅ (Enhanced) | Default 28 steps | ✅                        | Pro           |

Please note that some features may not be available within Giselle even if they are offered in the official API.

### flux-pro/v1.1

Enhanced version of FLUX.1, offering superior composition, detail, and artistic fidelity. With significantly accelerated speeds (up to 10x), it provides excellent results for professional-grade visual content. Includes adjustable safety tolerance levels, detailed typography support, and optimized inference steps for efficiency.

### flux/schnell

A highly efficient 12-billion-parameter model, optimized for extremely fast image generation (1-4 steps). Ideal for use-cases requiring rapid image production without significant compromise on quality. Suitable for both personal and commercial purposes, with built-in safety checking.

### stable-diffusion-v3-medium

An advanced Multimodal Diffusion Transformer (MMDiT) model that significantly improves image quality, typography handling, prompt comprehension, and overall efficiency. Provides excellent balance between quality and speed with enhanced typography capabilities and standard inference steps.

## Model Selection Guide

Guidelines for selecting the optimal fal.ai model:

* **For highest artistic fidelity and professional results**: flux-pro/v1.1
* **For fastest image generation**: flux/schnell
* **For balanced image quality, typography, and efficiency**: stable-diffusion-v3-medium

## Practices for Giselle

We recommend flux-pro/v1.1 as your primary choice when exceptional detail, artistic accuracy, and overall superior image quality are essential. For real-time applications or projects requiring quick visual feedback, flux/schnell provides the necessary speed. When needing a versatile balance of quality, efficiency, and typographic precision, stable-diffusion-v3-medium is highly recommended.

For detailed specifications, integration guides, and further assistance, please refer to the [fal.ai API Documentation](https://fal.ai/models).


# Google
Source: https://docs.giselles.ai/en/models/providers/google

Available Google AI Models Overview.

## Gemini

The following Gemini models are available in the Giselle workspace. Each model offers specific capabilities and features to match your use case requirements.

| Models                | Generate Text | Web Search | Reasoning | Input PDF | Input Image | Input Audio | Input Video | Context Window      | Plan\@Giselle |
| --------------------- | ------------- | ---------- | --------- | --------- | ----------- | ----------- | ----------- | ------------------- | ------------- |
| gemini-2.5-pro        | ✅             | ✅          | ✅         | ✅         | ✅           | ✅           | ✅           | 1M tokens (2M soon) | Pro           |
| gemini-2.5-flash      | ✅             | ✅          | ✅         | ✅         | ✅           | ✅           | ✅           | 1M tokens           | Pro           |
| gemini-2.5-flash-lite | ✅             | ✅          | ✅         | ✅         | ✅           | ✅           | ✅           | 1M tokens           | Free          |

*Note: Some features may not be available within Giselle even if they are offered in the Google official API. Features marked 'Free' or 'Pro' refer to the Giselle subscription plan required to access them.*

### gemini-2.5-pro

The next-generation comprehensive model. It provides state-of-the-art capabilities, including text generation, web search, advanced reasoning, and robust coding features. It supports a wide range of input formats (PDF, images, audio, video) and has a 1 million token context window (expansion to 2 million tokens planned). Ideal for users wanting to experiment with the latest advancements for complex problems and deep multimodal understanding. Requires a Pro plan.

### gemini-2.5-flash

The next-generation Flash model, optimized for speed *and* reasoning. It offers fast text generation, web search, reasoning capabilities, and supports various inputs (PDF, images, audio, video). With a 1 million token context window, it's ideal for tasks requiring quick responses combined with analytical depth and multimodal understanding. Requires a Pro plan.

### gemini-2.5-flash-lite

The next-generation Flash Lite model, `gemini-2.5-flash-lite` is designed for maximum efficiency and the quickest possible responses. It supports text generation, web search, and multimodal inputs (PDF, image, audio, video). With a 1M token context window, it's ideal for high-throughput tasks and applications where immediate feedback is paramount. Available on the Free plan.

## Model Selection Guide

Guidelines for selecting the optimal model based on your needs and plan:

**Free Plan Models:**

* **For extremely fast responses and efficiency**: `gemini-2.5-flash-lite` (Maximum speed)

**Pro Plan Models:**

* **For best overall performance and complex tasks**: `gemini-2.5-pro` (Most powerful, all features)
* **For fast responses with reasoning**: `gemini-2.5-flash` (Speed + Reasoning balance)

## Practices for Giselle

We recommend `gemini-2.5-pro` (Pro plan) as your primary model in Giselle due to its proven power and stability for complex tasks. It is capable of processing large volumes of data, executing complex code reviews, and handling a wide variety of business tasks.

For users prioritizing speed on the Free plan, `gemini-2.5-flash-lite` is an excellent option. Pro users seeking a balance of speed and reasoning might consider the `gemini-2.5-flash`.

By enabling the **Search grounding** feature with these models (where applicable), you can access web search functionality, allowing you to supplement your workflows with the most current information available.

For detailed specifications, performance benchmarks, or additional assistance, please check [Google AI for Developers](https://ai.google.dev/gemini-api/docs/models).


# OpenAI
Source: https://docs.giselles.ai/en/models/providers/openai

Overview of available OpenAI Models within the Giselle workspace.

Explore the OpenAI models available in the Giselle workspace. These models are categorized based on their primary strengths and use cases, reflecting OpenAI's platform structure.

## Quick Comparison

The following table summarizes the key features of the OpenAI models available in Giselle.

| Models      | Generate Text | Input Image | Web Search | Reasoning   | Context Window | Max Output Tokens | Pricing (Input/Output per 1M tokens) | Availability |
| ----------- | ------------- | ----------- | ---------- | ----------- | -------------- | ----------------- | ------------------------------------ | ------------ |
| gpt-5       | ✅             | ✅           | ✅          | ✅ (Highest) | 400k tokens    | 128k tokens       | $1.25 / $10.00                       | Pro          |
| gpt-5-mini  | ✅             | ✅           | ✅          | ✅ (High)    | 400k tokens    | 128k tokens       | $0.25 / $2.00                        | Pro          |
| gpt-5-nano  | ✅             | ✅           | ❌          | ✅ (Medium)  | 400k tokens    | 128k tokens       | $0.05 / $0.40                        | Free         |
| gpt-image-1 | ❌             | ✅           | ❌          | ❌           | Unknown        | N/A               | $5.00 / $40.00                       | Open Source  |

*Please note that some features listed (like specific API functionalities e.g., fine-tuning, batch processing, specific tool use like audio or transcription) may not be directly exposed or available within the Giselle interface even if supported by the underlying OpenAI model.*

## GPT-5 Series Models

Introducing the GPT-5 series, OpenAI's latest and most advanced family of models. These models set new benchmarks for performance across a wide range of tasks, featuring enhanced reasoning capabilities, faster speeds, and improved efficiency.

### gpt-5

GPT-5 is OpenAI's flagship model, setting a new standard for coding, complex reasoning, and agentic tasks across various domains. It features built-in expert-level intelligence and a deeper reasoning engine, making it exceptionally capable for multi-step problems, technical writing, and analyzing text, code, and images. It supports web search functionality.

* **Context Window:** 400,000 tokens
* **Max Output Tokens:** 128,000 tokens
* **Knowledge Cutoff:** October 1, 2024
* **Inputs:** Text, Image
* **Availability:** Pro Plan

### gpt-5-mini

GPT-5 mini is a faster, more cost-efficient version of GPT-5, optimized for well-defined tasks. It balances intelligence, speed, and affordability while maintaining strong reasoning capabilities. It supports image inputs and web search, making it a versatile choice for many common use cases.

* **Context Window:** 400,000 tokens
* **Max Output Tokens:** 128,000 tokens
* **Knowledge Cutoff:** May 31, 2024
* **Inputs:** Text, Image
* **Availability:** Pro Plan

### gpt-5-nano

GPT-5 nano is the fastest and most cost-effective model in the GPT-5 series. It is designed for high-throughput tasks like summarization and classification, providing quick and efficient performance. It supports text and image inputs but does not include web search functionality.

* **Context Window:** 400,000 tokens
* **Max Output Tokens:** 128,000 tokens
* **Knowledge Cutoff:** May 31, 2024
* **Inputs:** Text, Image
* **Availability:** Free Plan

## Image Generation Models

These models are specialized in generating high-quality images from text and image inputs.

### gpt-image-1

OpenAI's state-of-the-art image generation model. It is a natively multimodal language model that accepts both text and image inputs and produces image outputs. The model offers different quality levels (Low, Medium, High) and supports various image dimensions, allowing for flexible generation based on use case requirements.

> **Note**: This model is currently available only on the Open Source plan.

* **Pricing:** Input text: $5.00 per 1M tokens, Input images: $10.00 per 1M tokens, Output images: \$40.00 per 1M tokens
* **Quality Options:** Low, Medium, High
* **Supported Dimensions:** 1024x1024, 1024x1536, 1536x1024
* **Knowledge Cutoff:** April 2025 (estimate based on release date)
* **Inputs:** Text, Image
* **Outputs:** Image
* **Availability:** Open Source

## Model Selection Guide

Guidelines for selecting the optimal OpenAI model within Giselle:

* **For the best overall performance, coding, agentic tasks, and highest reasoning**: `gpt-5` (Pro)
* **For a faster, cost-efficient version of GPT-5 for well-defined tasks**: `gpt-5-mini` (Pro)
* **For the fastest, most cost-effective version of GPT-5 for summarization and classification**: `gpt-5-nano` (Free)
* **For high-quality image generation from text or image inputs**: `gpt-image-1` (Pro)

## Practices for Giselle

We recommend **gpt-5** as the versatile primary model in Giselle for Pro users. It offers an unparalleled balance of capability, intelligence, and features (including web search via tool) across various tasks like complex coding, business document creation, in-depth analysis, and advanced research. GPT-5 is designed to be highly reliable and accurate, significantly reducing hallucinations and improving instruction following.

For Pro users requiring a balance of speed and cost-efficiency for well-defined tasks, **gpt-5-mini** is an excellent choice, maintaining strong reasoning and multimodal capabilities.

For Free plan users or those prioritizing the fastest and most cost-effective solution for high-throughput tasks like summarization and classification, **gpt-5-nano** is the recommended model.

**Automatic Fallback for Deprecated Models:**
Giselle now automatically maps previously available OpenAI models to the new GPT-5 series to ensure a seamless transition for existing workflows.

* **Models now mapping to `gpt-5` (Pro)**: `gpt-4o`, `o3`, `gpt-4.1`, `o1`, `gpt-4-turbo`, `gpt-4`, `gpt-3.5-turbo`
* **Models now mapping to `gpt-5-mini` (Pro)**: `o4-mini`, `gpt-4.1-mini`, `o3-mini`, `o1-mini`, `gpt-4o-mini`
* **Models now mapping to `gpt-5-nano` (Free)**: `gpt-4.1-nano`

For image generation needs, **gpt-image-1** provides high-quality results and supports both text and image inputs. The model offers different quality tiers to balance cost and detail based on specific requirements.

By combining these models in workflows, you can leverage their specific strengths. For example, use `gpt-5` for its advanced reasoning and coding, `gpt-5-mini` for cost-efficient tasks, or `gpt-5-nano` for rapid, high-volume operations.

For detailed specifications and the full range of models offered directly by OpenAI, please check the [Official OpenAI Documentation](https://platform.openai.com/docs/models).


# Overview
Source: https://docs.giselles.ai/en/models/providers/overview

AI Model Providers.

This document provides an overview of the AI providers available through Giselle's Generator Nodes. Giselle integrates with multiple AI providers' APIs to offer you a diverse range of capabilities for your workflows.

## Provider Overview

### Anthropic

Anthropic focuses on developing AI systems that are reliable, interpretable, and steerable. Their Claude models are designed with an emphasis on helpfulness, harmlessness, and honesty, making them excellent for applications requiring nuanced understanding and safe outputs.

**Key models:**

* Claude Opus 4.1 - Ultimate coding powerhouse with most complex reasoning capabilities
* Claude Sonnet 4.5 - Balanced high-performance model with latest reasoning features
* Claude Haiku 4.5 - Cost-efficient model with speed and reasoning capabilities

### Google AI

Google's Gemini models represent their most capable and versatile AI systems. These models excel at multimodal tasks and offer extensive context windows, making them suitable for complex, context-rich applications and varied input types.

**Key models:**

* Gemini 2.5 Pro - Comprehensive model with multimodal capabilities and web search
* Gemini 2.0 Flash - Speed-optimized model for quick responses
* Gemini 2.0 Flash Thinking - Reasoning-focused rapid response model

### OpenAI

OpenAI provides a range of powerful models with particular strengths in code generation, creative content, and structured outputs. Their models feature robust function calling capabilities and strong performance across diverse domains.

**Key models:**

* GPT-4o - Flagship multimodal model with comprehensive capabilities
* GPT-4o-mini - Fast, affordable small model for focused tasks
* o3-mini - Reasoning-optimized small model with large token limits

### Fal AI

Fal AI focuses on image generation models that balance quality, speed, and versatility. Their models are designed for various creative and commercial applications, offering different optimization profiles to suit diverse needs.

> **Note:** Fal AI models are currently only available in the Open Source version of Giselle.

**Key models:**

* flux-pro/v1.1 - High-quality image generation with superior composition and detail
* flux/schnell - Ultra-fast image generation for time-sensitive applications
* stable-diffusion-v3-medium - Balanced model with enhanced typography capabilities

## Use Cases in Giselle

### Content Creation Workflows

* **Anthropic (Claude)**: Ideal for drafting nuanced business documents, creating policy content, and generating well-reasoned explanations in Giselle workflows. Claude models are particularly effective when handling sensitive subject matter or when ethical considerations are paramount.

* **Google (Gemini)**: Perfect for Giselle workflows involving mixed media inputs. Use Gemini models when your workflow processes documents containing text, images, and other media formats simultaneously. Their large context window makes them excellent for analyzing extensive documentation or research materials.

* **OpenAI (GPT)**: Excellent choice in Giselle for technical documentation workflows, code generation pipelines, and creative content production. The structured output capabilities make GPT models particularly useful when your Giselle workflow needs to generate content in specific formats or extract structured data.

### Visual Content Workflows

* **Fal AI**: Essential for Giselle workflows involving image generation tasks. Use flux-pro for high-quality marketing visuals, flux/schnell for rapid prototyping and iterative design processes, and stable-diffusion for balanced results with typography requirements.

### Multi-Provider Workflows

One of Giselle's strengths is the ability to combine different providers in a single workflow:

* Use different models to gather information, analyze implications, and format the findings into structured documentation
* Combine Gemini's multimodal analysis with Fal AI's image generation to create visual content based on document analysis
* Leverage different models' strengths in sequential nodes to optimize cost/performance at each workflow stage

## Future Roadmap

At Giselle, we're committed to continuously expanding our provider integrations and updating our supported models as the AI landscape evolves. We regularly assess new models and capabilities to ensure you have access to cutting-edge AI technology that best serves your needs.

We value your input on which models and providers you'd like to see added to our platform. If you have specific requests or feedback about our current offerings, please don't hesitate to contact us.

## Additional Resources

For detailed specifications and documentation on each provider's models:

* [Anthropic Documentation](https://docs.anthropic.com/)
* [Google AI for Developers](https://ai.google.dev/)
* [OpenAI Documentation](https://platform.openai.com/docs)
* [Fal.ai Models](https://fal.ai/models)


# Examples
Source: https://docs.giselles.ai/en/prompts/examples

Effective Prompt Examples in Giselle’s Generator Nodes.

This document provides effective and concrete prompt examples tailored specifically for Giselle's Generator Nodes, leveraging various multimodal AI models including Anthropic's Claude, Google's Gemini, OpenAI's GPT-4o, and Fal AI for image generation.

## Basic Examples

### 1. Technical Query using GPT-4o

```plaintext  theme={null}
Role: Experienced programmer

Task:
Explain the most efficient way to extract unique elements from a Python list.

Output Format:
- Brief explanation
- Python code example demonstrating the method clearly
```

**Why this prompt is effective:**

* Clear role definition aligns the AI’s perspective.
* Explicit instruction and clear output expectations.
* Specifies programming language explicitly.

### 2. Image Generation with Fal AI

```plaintext  theme={null}
Role: Graphic designer

Task:
Generate a high-quality, minimalist logo for a technology startup named "QuantumLeap."

Constraints:
- Model: flux-pro/v1.1
- Color scheme: Blue and white
- Style: Modern, minimalistic

Output Format:
- PNG image (1024x1024)
```

**Why this prompt is effective:**

* Clearly defines role and creative constraints.
* Utilizes specific Fal AI model for high-quality outputs.
* Precise output format suitable for immediate use.

## Advanced Examples

### 1. Multimodal Analysis with Gemini

```plaintext  theme={null}
Role: Industry analyst

Task:
Analyze the attached PDF industry report and the accompanying infographic image.

Steps:
1. Summarize key findings from the PDF.
2. Identify and explain trends visible in the infographic.
3. Recommend strategic actions based on combined insights.

Constraints:
- Model: Gemini 2.5 Pro

Output Format:
- Concise summary
- Clearly explained visual trends
- Strategic recommendations as bullet points
```

**Why this prompt is effective:**

* Clearly utilizes Gemini’s multimodal capabilities.
* Sequential and structured instructions.
* Explicitly states the model to ensure precise capability usage.

### 2. Ethical Analysis and Content Structuring with Claude

```plaintext  theme={null}
Role: Ethics consultant

Task:
Review the provided research paper on AI surveillance technologies.

Steps:
1. Identify ethical implications.
2. Suggest practical ethical guidelines for deployment.

Constraints:
- Model: Claude 3.7 Sonnet

Output Format:
- Ethical implications listed clearly
- Practical guidelines structured as actionable points
```

**Why this prompt is effective:**

* Aligns task specifically with Claude's strengths in nuanced understanding.
* Structured clearly to maximize Claude's reasoning and analytical capabilities.

## Integrated Workflow Examples

### 1. Comprehensive Market Research Workflow

```plaintext  theme={null}
Step 1 (Claude 3.7 Sonnet):
Role: Market researcher and sustainability analyst
Task: Research sustainable food packaging trends and analyze their ethical and sustainability implications.
Output Format: Analysis summary and recommendations.

Step 2 (GPT-4o):
Role: Technical writer
Task: Format the insights and recommendations into a structured industry report.
Output Format: Professional document in markdown format.

Step 3 (Fal AI flux-pro/v1.1):
Role: Graphic designer
Task: Generate a compelling visual cover image for the final report.
Constraints: Sustainability theme, professional style
Output Format: High-quality cover image (PNG, 1200x800)
```

**Why this prompt is effective:**

* Clearly leverages strengths of multiple AI models sequentially.
* Structured, integrated steps with explicit model assignments.
* Produces comprehensive, ready-to-use workflow outputs.

## Key Effective Elements in Giselle Prompts

Effective Giselle Generator Node prompts typically include:

* **Explicit Role Definitions**
* **Clear Constraints and Context**
* **Structured Output Formats**
* **Sequential or Stepwise Instructions**
* **Specific Model Selections for Capabilities**

For additional guidance and practical tips on creating impactful prompts, refer to [tips.mdx](./tips).


# Overview
Source: https://docs.giselles.ai/en/prompts/overview

Prompt Engineering in Giselle’s Node-Based UI.

Prompt engineering involves crafting and refining prompts—structured instructions designed to guide AI models toward precise and high-quality outputs. Giselle enhances this practice through a rich node-based UI called Generator Nodes, enabling intuitive, visual, and efficient prompt construction.

## What is a Prompt in Giselle?

In Giselle, prompts are carefully structured instructions provided individually within each Generator Node through a rich text editor. Unlike conversational interfaces, Giselle primarily uses one-shot prompting, allowing each node to independently deliver precise instructions and receive AI-generated outputs tailored to specific tasks.

Each prompt typically includes:

* **Role Definition**: Specifies the AI model’s intended expertise or persona.
* **Task Instructions**: Clearly states the task the model needs to perform.
* **Context**: Provides relevant background information and supporting data.
* **Input Data**: Delivers specific information or data sources for processing.
* **Output Format**: Defines the required format and structure of the AI’s response.

## Why Effective Prompts Matter

Creating effective prompts in Giselle's Generator Nodes significantly enhances AI-driven workflows by:

* **Improving Output Quality**: Clearly articulated prompts result in accurate and relevant responses.
* **Minimizing Errors**: Reduces the likelihood of misunderstandings or incorrect outputs.
* **Ensuring Consistency**: Promotes uniformity and reliability in outputs, crucial for downstream tasks.
* **Optimizing Resources**: Well-crafted prompts reduce token consumption and processing time, enhancing cost efficiency.

## Leveraging Giselle’s Generator Nodes

Giselle’s Generator Nodes provide a robust platform for prompt engineering, allowing teams to:

* **Adjust Model Parameters**: Fine-tune various LLM settings to suit specific task requirements.
* **Integrate Diverse Data Sources**: Incorporate multiple data inputs and seamlessly manage them across nodes.
* **Share Data Between Nodes**: Reuse outputs generated in one node as inputs for subsequent nodes, enabling sophisticated workflow automation.
* **Visualize Workflows**: Clearly map out intellectual production processes for improved transparency, collaboration, and understanding within teams.

## Recommended Practices

To maximize the effectiveness of Giselle’s Generator Nodes, adhere to the following practices:

* **Clearly Define Roles**: Explicitly establish the AI’s expected perspective or expertise.
* **Write Precise Instructions**: Avoid ambiguity by providing clear, concise task descriptions.
* **Provide Relevant Context**: Supply comprehensive background information to enhance understanding.
* **Specify Structured Outputs**: Always include detailed output formatting to maintain consistency.
* **Iteratively Refine Prompts**: Regularly test and refine prompts within the node-based UI to continuously improve outputs.

Understanding the fundamentals of prompt engineering is crucial, as effectively designed prompts significantly influence the quality and reliability of AI-generated outputs.

For detailed prompt examples, see [examples.mdx](./examples). For additional practical tips, refer to [tips.mdx](./tips).


# Tips
Source: https://docs.giselles.ai/en/prompts/tips

Practical Tips for Effective Prompt Creation in Giselle’s Generator Nodes.

This document provides concrete, actionable tips tailored specifically for creating effective prompts within Giselle’s Generator Nodes. Unlike conversational UIs, Giselle uses a single-shot prompting model, meaning each prompt must be precise and complete on its own. While direct iterative refinement through conversation within a single node isn't possible, strategically chaining multiple nodes can significantly elevate the output quality through careful node integration and diverse data sourcing.

## Essential Principles

### 1. Ensure Clarity and Precision

* Clearly define the AI model’s role.
* Provide explicit, focused instructions without ambiguity.

```plaintext  theme={null}
❌ Poor example:
"Describe a useful invention."

✅ Good example:
"Role: Technology historian

Task: Provide a concise summary (100 words max) of the invention of the telephone, highlighting its historical significance and modern impact.

Output Format:
- Summary paragraph
- Clearly stated historical context and modern relevance"
```

### 2. Include Comprehensive Context

* Provide necessary background and purpose clearly in your prompt.
* Explicitly state constraints or expectations relevant to the task.

### 3. Specify Structured Outputs

* Clearly outline the desired response structure, length, and style.
* Define formats explicitly (e.g., bullet points, structured paragraphs, JSON, image dimensions).

## Advanced Node Integration Techniques

### 1. Effective Role Definition

Defining roles guides the AI to produce contextually accurate outputs:

```plaintext  theme={null}
✅ Example:
"Role: UX Designer

Task: Evaluate the provided web interface design for usability issues.

Output Format:
- List identified issues clearly
- Provide specific recommendations for improvements"
```

### 2. Sequential Node Chaining

Although Giselle nodes are single-shot, you can achieve iterative refinement by chaining multiple nodes:

1. **Ideation Node**: Generate initial ideas or concepts.
2. **Drafting Node**: Develop detailed drafts from initial concepts.
3. **Review Node**: Critically evaluate drafts and suggest improvements.

### 3. Leveraging Multi-Node Workflows

Combine diverse AI models across nodes to maximize output quality:

* **Claude** for nuanced analysis and ethical considerations.
* **GPT-4o** for structured and creative content creation.
* **Fal AI** for high-quality image and visual content generation.

## Common Pitfalls to Avoid

### 1. Overly Restrictive Instructions

Avoid excessively rigid constraints:

```plaintext  theme={null}
❌ Avoid:
"Create a detailed report exactly 200 words, including exactly four examples."
```

### 2. Contradictory or Confusing Instructions

Ensure instructions remain logically consistent:

```plaintext  theme={null}
❌ Avoid:
"Provide a highly detailed yet simple explanation using advanced terminology."
```

### 3. Ambiguous or Incomplete Prompts

Avoid vague instructions that lead to unclear outputs:

```plaintext  theme={null}
❌ Avoid:
"Explain something useful."
```

## Optimizing Giselle Workflows

### 1. Iterative Node Refinement

* Regularly review outputs from each node to optimize subsequent prompts.
* Use multiple nodes strategically to iteratively refine concepts, drafts, and final outputs.

### 2. Strategic Use of Templates

Leverage prompt templates for consistent, effective outputs:

```plaintext  theme={null}
✅ Giselle Template:

Role: [Defined AI role]

Task: [Explicit, precise task description]

Constraints:
- [Specific constraint or limitation]
- [Additional constraints as necessary]

Input Data:
- [Clearly referenced or provided data]

Output Format:
- [Detailed expected structure of response]
```

## Giselle-Specific Recommendations

### 1. Select Appropriate AI Models

Choose AI models carefully according to task requirements and capabilities:

* **Claude**: nuanced, ethical analyses.
* **Gemini**: complex multimodal inputs.
* **GPT-4o**: structured outputs and creative content.
* **Fal AI**: image generation tasks.

### 2. Visualize and Collaborate

* Clearly map your workflows visually within Giselle’s UI.
* Share your workflows with teams to enhance collaboration and clarity.
* Experiment with node combinations to achieve advanced, high-quality results beyond standard conversational interfaces.

## Key Points for Effective Giselle Prompts

* **Role Definition**: Clearly articulate the AI model’s role.
* **Precision**: Provide exact, detailed instructions.
* **Contextual Completeness**: Include essential context and constraints.
* **Output Structure**: Clearly define response formats.
* **Workflow Optimization**: Strategically chain multiple nodes to enhance output quality.


# Product Notes
Source: https://docs.giselles.ai/en/releases/product-notes

This document outlines key updates, improvements, and future prospects of our product.

## Latest Product Updates

### Public Beta

Giselle is currently available as a public beta, allowing users to test and provide feedback on our AI app building platform.
We're excited to announce that we will be officially launching on Product Hunt soon at [https://www.producthunt.com/products/giselle](https://www.producthunt.com/products/giselle).
This launch will introduce our open-source visual editor for building custom AI applications to a wider audience.
Stay tuned for the official launch date and be among the first to explore the full capabilities of Giselle.


# Release Notes
Source: https://docs.giselles.ai/en/releases/release-notes

This page provides chronological information about the latest releases and updates of our product.

TBD

## Community-Driven

We believe in building with our community. Your feedback and suggestions are essential to shaping our product direction. We actively welcome feature requests, improvement suggestions, bug reports, and use case scenarios. Please share your thoughts through [GitHub Issues](https://github.com/giselles-ai/giselle) or [GitHub Discussions](https://github.com/giselles-ai/giselle/discussions).


# Roadmap
Source: https://docs.giselles.ai/en/releases/roadmap

Discover our product development plans and upcoming milestones.

Our roadmap is currently under active development. We are working to provide a clear vision of our future plans and milestones.

## Community-Driven

We believe in building with our community. Your feedback and suggestions are essential to shaping our product direction.

We actively welcome:

* Feature requests
* Improvement suggestions
* Bug reports
* Use case scenarios

Please share your thoughts through:

* [GitHub Issues](https://github.com/giselles-ai/giselle)
* [GitHub Discussions](https://github.com/giselles-ai/giselle/discussions)

## What's Next

Stay tuned as we formalize our roadmap with specific timelines and feature sets. We'll be updating this page regularly as our plans evolve.

<Info>
  Note: This roadmap is subject to change without notice based on user feedback and development priorities.
</Info>


