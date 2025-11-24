# Source: https://dev.writer.com/home/knowledge-graph-concepts.md

# Connect your data to AI with Knowledge Graph

> Understand graph-based RAG with Knowledge Graph. Learn how content ingestion, graph construction, and query processing deliver accurate AI responses.

Knowledge Graph is Writer's retrieval-augmented generation (RAG) system that uses graph-based relationships that can improve accuracy compared to vector-only approaches ([reference](https://arxiv.org/abs/2405.02048)). Connect your data sources to enable LLMs to access, understand, and reason about your specific information when generating responses. Get inline citations to ensure every answer pulls from your actual data.

## Knowledge Graph concepts

Knowledge Graph is a structured way to store and retrieve information from your documents, websites, and data sources. Unlike traditional search systems that rely on keyword matching or vector similarity, Knowledge Graph creates a network of interconnected information that captures relationships between concepts, entities, and ideas.

### How Knowledge Graph works

Knowledge Graph processes your data through several stages:

1. **Content ingestion**: upload files, connect data sources, or add website URLs
2. **Graph construction**: analyze content to identify entities, concepts, and relationships
3. **Indexing**: create a searchable graph structure that captures semantic connections
4. **Query processing**: when you ask questions, the system traverses the graph to find relevant information
5. **Response generation**: combine retrieved information with AI to generate accurate, contextual answers

<img src="https://mintcdn.com/writer/9kv7QIFPQINxtMk7/images/home/kg-overview.excalidraw.png?fit=max&auto=format&n=9kv7QIFPQINxtMk7&q=85&s=9a2934f60712ebf1ef24753f53705d9a" alt="Knowledge Graph flow from ingestion to graph construction, indexing, query processing, and response generation." data-og-width="1416" width="1416" data-og-height="1039" height="1039" data-path="images/home/kg-overview.excalidraw.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9kv7QIFPQINxtMk7/images/home/kg-overview.excalidraw.png?w=280&fit=max&auto=format&n=9kv7QIFPQINxtMk7&q=85&s=9f3015ffcc8b52cdcf4e82fd25b24feb 280w, https://mintcdn.com/writer/9kv7QIFPQINxtMk7/images/home/kg-overview.excalidraw.png?w=560&fit=max&auto=format&n=9kv7QIFPQINxtMk7&q=85&s=2c7d31f1cb143122305df212d3644141 560w, https://mintcdn.com/writer/9kv7QIFPQINxtMk7/images/home/kg-overview.excalidraw.png?w=840&fit=max&auto=format&n=9kv7QIFPQINxtMk7&q=85&s=a54e4f488fe58e521147e82f707aebaa 840w, https://mintcdn.com/writer/9kv7QIFPQINxtMk7/images/home/kg-overview.excalidraw.png?w=1100&fit=max&auto=format&n=9kv7QIFPQINxtMk7&q=85&s=ad879c0f2c9bf340fc99f270586fed1c 1100w, https://mintcdn.com/writer/9kv7QIFPQINxtMk7/images/home/kg-overview.excalidraw.png?w=1650&fit=max&auto=format&n=9kv7QIFPQINxtMk7&q=85&s=0b9934ff0e6d5e80a2a8e59ebf153bfc 1650w, https://mintcdn.com/writer/9kv7QIFPQINxtMk7/images/home/kg-overview.excalidraw.png?w=2500&fit=max&auto=format&n=9kv7QIFPQINxtMk7&q=85&s=9d412f2a6296ad7cd67a8cdd4b4df4ed 2500w" />

## Data sources and formats

Knowledge Graph supports multiple ways to add data:

| Source type             | Description                   | Supported formats/features                                                                                                                                                                                   | Learn more                                                                                                    |
| ----------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **File uploads**        | Upload documents directly     | - PDF, TXT, DOC/DOCX, PPT/PPTX<br />- CSV, XLS/XLSX<br />- EML, HTML, SRT                                                                                                                                    | [Manage Knowledge Graph data](/home/knowledge-graph)                                                          |
| **Data connectors**     | Connect to external platforms | - Confluence: Access team documentation and wikis<br />- Notion: Import workspaces and databases<br />- Google Drive: Connect to shared drives and documents<br />- SharePoint: Access Microsoft 365 content | [Data connectors guide](https://support.writer.com/article/251-setting-up-knowledge-graph-data-connectorss)   |
| **Website integration** | Add web content               | - Add specific URLs or entire domains<br />- Configure page inclusion/exclusion<br />- Automatic content updates                                                                                             | [Website integration guide](https://support.writer.com/article/272-setting-up-knowledge-graph-web-connectors) |

Learn more about [data sources and formats](https://support.writer.com/article/242-how-to-create-and-manage-a-knowledge-graph).

## Query capabilities

Knowledge Graph supports natural language questions and querying across multiple graphs. You can configure the retrieval to break it down into subqueries, support streaming, get inline citations, and fine-tune the search parameters.

**Core features:**

* **Natural language questions**: ask questions in plain, conversational language without needing special syntax or query formats. For example, "What is our refund policy?" or "Tell me about our enterprise pricing tiers" will work naturally.
* **Multi-graph queries**: search across multiple Knowledge Graphs simultaneously. For example, you can compare data across departments or time periods.

**Configurable options:**

* **Subqueries**: break down complex questions into smaller parts automatically
* **Streaming responses**: get answers as they're generated for real-time applications
* **Inline citations**: get answers with embedded source references to verify information
* **Query configuration**: fine-tune search parameters including search weight, grounding level, maximum snippets and tokens, and semantic thresholds

## Add Knowledge Graph to your Writer applications

Add Knowledge Graph to your Writer applications to create conversational AI, generate content, and enable tool calling in complex workflows. Get started with these guides:

* [Create and manage Knowledge Graphs](/home/knowledge-graph): set up your first Knowledge Graph via the Writer API and SDKs
* [Ask questions to Knowledge Graphs](/home/kg-query): query your data directly via the Writer API and SDKs
* [Build chat applications with Knowledge Graph](/no-code/chat-kg): create conversational AI that can reference your specific data
* [Use Knowledge Graph with tool calling](/agent-builder/tool-calling-intro): integrate Knowledge Graph with Agent Builder
* [Enable inline citations](/home/inline-citations): get source references in responses from Knowledge Graph queries
* [Knowledge Graph query configuration](/home/knowledge-graph-query-config): fine-tune search parameters

## Best practices

### Organize your data

* Create separate Knowledge Graphs for different topics or departments
* Use descriptive names and descriptions to help the AI understand context
* Regularly update content to ensure accuracy

### Optimize queries

* Ask specific, well-formed questions for better results
* Use the query configuration parameters to fine-tune responses
* Enable subqueries for complex multi-part questions

### Monitor and improve

* Review source citations to understand how information is being retrieved
* Update Knowledge Graphs with new information as it becomes available
* Test different query approaches to find what works best for your use case

## Next steps

* Learn how to [create and manage Knowledge Graphs](/home/knowledge-graph)
* Explore the [Knowledge Graph API reference](/api-reference/kg-api)
* See how to [ask questions to Knowledge Graphs](/home/kg-query)
* Understand [Knowledge Graph query configuration](/home/knowledge-graph-query-config)
* For additional help, visit the [Writer Help Center](https://support.writer.com) for detailed guides and troubleshooting
