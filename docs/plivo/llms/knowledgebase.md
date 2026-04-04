# Source: https://plivo.com/docs/aiagent/aistudio/agentconfiguration/knowledgebase.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Knowledge Base

> A Knowledge Base in Plivo is a structured repository of information that your AI Agent can access

## Overview

A **Knowledge Base**  is an essential resource that stores and organizes information your AI Agent needs to provide contextually relevant answers during conversations. It allows the agent to access and reference structured data, documents, and information sources without overwhelming the prompts with excessive detail.

The ability to link a Knowledge Base to an AI Agent enables dynamic, real-time responses, boosting both efficiency and accuracy during customer interactions.

## Creating and Linking a Knowledge Base

### Steps to Create and Link a Knowledge Base:

1. **Navigate to the Knowledge Base Section**: In the **AI Studio**, go to the **Knowledge** section.
2. **Click “Create Knowledge Base”**: Assign a **name** to the Knowledge Base and select your source(s).
3. **Link to Agent**: You can link the Knowledge Base to an agent at the time of its creation or later through the **Agent Builder** interface.
4. **Multiple Agent Link**: A single Knowledge Base can be linked to multiple agents. Once the Knowledge Base is created, you can update it at any time by adding or removing sources.

   **Note**: You can update the Knowledge Base later by adding or removing sources.

## Supported Data Sources

You can feed the Knowledge Base with various types of content. The following data sources are supported:

### 1. **Files**

Upload documents in various formats to build your Knowledge Base.

* **Supported Formats**:
  * CSV
  * PDF
  * DOCX
  * TXT
  * JSON
  * XML
* **Max File Size**: 64 MB per file
* **Recommended Formatting**: Use **structured, markdown-style** formatting for optimal performance and easier retrieval.

### 2. **Website URLs**

Sync content from your website to populate the Knowledge Base.

* **Sync Options**:

  * **Entire Website** or configure custom sync settings:
    * Number of subpages
    * Crawl depth
    * Include/exclude specific paths
  * Sync up to **10,000 URLs** per Knowledge Base.
  * **Auto-Crawling**: Enable periodic updates (minimum interval: 1 week).

  **Note**: Once the Knowledge Base is created, sync settings cannot be modified.

### 3. **Apps**

Sync content from tools and apps like:

* **Notion**
* **Confluence**
* **Freshdesk**
* **Zendesk**
* **Intercom**

To sync content, you’ll need to configure the integration first. You can do this by going to **Settings** → **Integrations**, authenticate the app, and then pull the data.

**Important**: App integrations must be set up before syncing content from apps. Learn more about [Integrations](#).

## Configure

* **Multiple Data Sources**: You can combine multiple data sources (files, websites, apps) within a single Knowledge Base.
* **Auto-Refresh**: Enable auto-refresh for website and app sources to keep your Knowledge Base up-to-date. (Auto-refresh minimum interval: 1 week).
* **Variables**: You can use variables extracted from **API-triggered requests** to query and dynamically filter knowledge base content.
* **Manual Updates**: You can manually add or remove files, URLs, or app sources after the Knowledge Base is created.

## How the Agent Uses the Knowledge Base

Once a **Knowledge Base** is linked to an agent, the agent automatically searches the knowledge base to provide relevant responses. Here’s how it works:

* **Automatic Search**: During a conversation, the agent searches the Knowledge Base at each response step.
* **Semantic Search**: The agent retrieves the most relevant chunks of data using semantic search, ensuring the responses are contextually appropriate.
* **Contextual Responses**: The retrieved information is passed to the **Large Language Model (LLM)** during generation. No need to modify the prompt or provide additional context.
* **Real-Time Retrieval**: The knowledge base is accessed in real-time based on the conversation's history. If no relevant matches are found, the agent will not pull content from the Knowledge Base.

## Best Practices for Using Knowledge Bases

To get the best performance from your Knowledge Base and ensure optimal retrieval of information, follow these best practices:

1. **Use Clear Formatting**: For best retrieval performance, ensure content is clearly formatted. Prefer **markdown** or structured text.
2. **Group Related Content**: Organize related information in sections. This makes it easier to retrieve relevant data when the agent queries the Knowledge Base.
3. **Avoid Vague Language**: Always use explicit references in content. Avoid using vague terms like “this” or “it.” Be specific.
4. **Sync Specific Subpaths**: When syncing websites, prefer syncing specific subpaths (URLs) instead of entire domains. This minimizes irrelevant data retrieval.
5. **Use Knowledge Bases for Facts**: Knowledge Bases are great for providing factual support. Avoid using them for task instructions—that’s better suited for system prompts.

## Linking Knowledge Base(s) to an Agent Flow

You can link one or more Knowledge Bases to an agent flow for dynamic content retrieval during conversations.

### Steps to Link Knowledge Base(s):

<Frame>
  <video controls className="w-full aspect-video" src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/images/Knowledge-Base-Video.mp4?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=c00582093f9684fb28c89c665f965072" data-path="images/Knowledge-Base-Video.mp4" />
</Frame>

1. **Go to Agent Settings**: In the **Flow Builder**, click on **Agent Settings** from the top-right navigation bar.
2. **Link Knowledge Base(s)**: From the available dropdown, select the **Knowledge Base(s)** you want to link to your agent.
3. **Create a Knowledge Base**: If you haven’t created a Knowledge Base yet, you can navigate to **AI Studio** → **Knowledge** to create one.

**Note**: If your use case does not require external content or documents, you can leave this field blank.

### Example Use Case:

**Customer Support**:

* A customer asks for information about a product's return policy.
* The agent is linked to a Knowledge Base containing FAQs and policy documents.
* The agent automatically retrieves the relevant information from the Knowledge Base using semantic search.
* The response is delivered in real-time, providing accurate policy details without needing manual input.
