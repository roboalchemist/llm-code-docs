# Source: https://www.elastic.co/docs/explore-analyze/ai-features

﻿---
title: AI-powered features
description: AI is a core part of the Elastic platform. It augments features and helps you analyze your data more effectively. This page lists the AI-powered capabilities...
url: https://www.elastic.co/docs/explore-analyze/ai-features
products:
  - Elastic Cloud Serverless
  - Elastic Observability
  - Elastic Security
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# AI-powered features
AI is a core part of the Elastic platform. It augments features and helps you analyze your data more effectively. This page lists the AI-powered capabilities and features available to you in each solution, and provides links to more detailed information about each of them.
To learn about enabling and disabling these features in your deployment, refer to [Manage access to AI features](https://www.elastic.co/docs/explore-analyze/ai-features/manage-access-to-ai-assistant).
For pricing information, refer to [pricing](https://www.elastic.co/pricing).

## Requirements

- To use Elastic's AI-powered features, you need an appropriate subscription level or serverless feature tier. These vary by solution and feature. Refer to each feature's documentation to learn more.
- Most features require at least one working LLM connector. To learn about setting up large language model (LLM) connectors used by AI-powered features, refer to [Configure access to LLMs](https://www.elastic.co/docs/explore-analyze/ai-features/llm-guides/llm-connectors). Elastic Managed LLMs are available by default if your license supports it.


## AI-powered features on the Elastic platform

The following AI-powered features are available across the Elastic platform. These are core Elasticsearch capabilities that you can use regardless of your chosen solution or project type.

### Elastic Inference

[Elastic Inference](https://www.elastic.co/docs/explore-analyze/elastic-inference) enables you to use machine learning models to perform operations such as text embedding or reranking on your data.
To learn more, refer to:
- [Elastic Inference Service (EIS)](https://www.elastic.co/docs/explore-analyze/elastic-inference/eis):
  A managed service that runs inference without the need of deploying a model, or managing infrastructure and resources.
- [Elastic Managed LLMs](https://www.elastic.co/docs/reference/kibana/connectors-kibana/elastic-managed-llm):
  Built-in LLMs vetted for GenAI product features across the platform.
- [The inference API](https://www.elastic.co/docs/explore-analyze/elastic-inference/inference-api):
  This general-purpose API enables you to perform inference operations using EIS, your own models, or third-party services.


### Natural language processing models

Natural Language Processing (NLP) enables you to analyze natural language data and make predictions.  Elastic offers a range of [built-in NLP models](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-built-in-models) such as the Elastic-trained [ELSER](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-elser) or [Jina models](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-jina). You can also [deploy custom NLP models](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-overview).

### AI-powered search

[AI-powered search](https://www.elastic.co/docs/solutions/search/ai-search/ai-search) helps you find data based on intent and contextual meaning using vector search technology, which uses machine learning models to capture meaning in content.

#### Semantic and hybrid search

Depending on your team's technical expertise and requirements, you can choose from two broad paths for implementing semantic search:
- For a minimal configuration, managed workflow use [semantic_text](https://www.elastic.co/docs/solutions/search/semantic-search/semantic-search-semantic-text).
- For more control over the implementation details, implement dense or sparse [vector search](https://www.elastic.co/docs/solutions/search/vector) manually.

[Hybrid search](https://www.elastic.co/docs/solutions/search/hybrid-search) combines traditional full-text search with AI-powered search for more powerful search experiences that serve a wider range of user needs.

### Semantic re-ranking

[Semantic re-ranking](https://www.elastic.co/docs/solutions/search/ranking/semantic-reranking) involves using ML models to reorder search results based on semantic similarity to queries, using models hosted in Elasticsearch or using third-party inference endpoints.

### Learning to Rank (LTR)

[Learning To Rank](https://www.elastic.co/docs/solutions/search/ranking/learning-to-rank-ltr) is an advanced feature that involves using trained ML models to build custom ranking functions for search. Best suited for use cases with substantial training data and requirements for highly customized relevance tuning.

## AI-powered features in the Elasticsearch solution/project type

The [Elasticsearch](https://www.elastic.co/docs/solutions/search) solution view (or project type in Serverless) includes certain AI-powered features beyond the core Elasticsearch capabilities available on the Elastic platform.

### Agent Builder

[Agent Builder](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder) enables you to create AI agents that can interact with your Elasticsearch data, run queries, and provide intelligent responses. It provides a complete framework for building conversational AI experiences on top of your search infrastructure.

### AI assistant for Elasticsearch

[Elastic AI Assistant for Observability and Search](https://www.elastic.co/docs/solutions/observability/ai/observability-ai-assistant) helps you understand, analyze, and interact with your Elastic data throughout Kibana. It provides a chat interface where you can ask questions about the Elastic Stack and your data, and provides contextual insights throughout Kibana that explain errors and messages and suggest remediation steps.

### Playground

[Playground](https://www.elastic.co/docs/solutions/elasticsearch-solution-project/playground) enables you to use large language models (LLMs) to understand, explore, and analyze your Elasticsearch data using retrieval augmented generation (RAG), via a chat interface. Playground is also very useful for testing and debugging your Elasticsearch queries, using the [retrievers](https://www.elastic.co/docs/solutions/search/retrievers-overview) syntax with the `_search` endpoint.

### Model Context Protocol (MCP) servers

Elastic offers two MCP server options for connecting agents to your Elasticsearch data. The Agent Builder MCP server is the recommended approach for Elasticsearch 9.2+ deployments and Serverless projects, offering full access to built-in and custom tools. For older Elasticsearch versions without Agent Builder, you can use the `mcp-elasticsearch` server which has a limited tool set.

#### Elastic Agent Builder MCP server

<applies-to>
  - Serverless Elasticsearch projects: Preview
  - Elastic Stack: Preview since 9.2
</applies-to>

Elastic 9.2+ deployments and Serverless projects provide an [Agent Builder MCP server endpoint](https://www.elastic.co/docs/explore-analyze/ai-features/agent-builder/mcp-server) that exposes all built-in and custom [tools](https://www.elastic.co/docs/explore-analyze/ai-features/agent-builder/tools) you can use to power agentic workflows.

#### Elasticsearch MCP server

<applies-to>
  - Elastic Cloud Serverless: Deprecated
  - Elastic Stack: Deprecated since 9.2
</applies-to>

If you're running earlier versions of Elasticsearch without Agent Builder, you can use [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch?tab=readme-ov-file#elasticsearch-mcp-server). This MCP server enables connecting agents to your Elasticsearch data and allows you to interact with your Elasticsearch indices through natural language conversations, though with a more limited tool set compared to the Agent Builder MCP server.

## AI-powered features in Observability

Observability's AI-powered features all require an [LLM connector](https://www.elastic.co/docs/explore-analyze/ai-features/llm-guides/llm-connectors). When you use one of these features, you can select any LLM connector that's configured in your environment. The connector you select for one feature does not affect which connector any other feature uses. For specific configuration instructions, refer to each feature's documentation.

### AI assistant for Observability

[Elastic AI Assistant for Observability and Search](https://www.elastic.co/docs/solutions/observability/ai/observability-ai-assistant) helps you understand, analyze, and interact with your Elastic data throughout Kibana. It provides a chat interface where you can ask questions about the Elastic Stack and your data, and provides [contextual insights](/docs/solutions/observability/ai/observability-ai-assistant#obs-ai-prompts) throughout Kibana that explain errors and messages and suggest remediation steps.

### Streams

[Streams](https://www.elastic.co/docs/solutions/observability/streams/streams) is an AI-assisted centralized UI within Kibana that streamlines common tasks like extracting fields, setting data retention, and routing data. Streams leverages AI in the following features:
- [Grok processing](/docs/solutions/observability/streams/management/extract/grok#streams-grok-patterns): Use AI to generate grok patterns that extract meaningful fields from your data.
- [Partitioning](https://www.elastic.co/docs/solutions/observability/streams/management/partitioning): Use AI to suggest logical groupings and child streams based on your data when using wired streams.
- [Advanced settings](https://www.elastic.co/docs/solutions/observability/streams/management/advanced): Use AI to generate a [stream description](/docs/solutions/observability/streams/management/advanced#streams-advanced-description) and a [feature identification](/docs/solutions/observability/streams/management/advanced#streams-advanced-features) that other AI features use when generating suggestions.


## AI-powered features in Elastic Security

Elastic Security's AI-powered features all require an [LLM connector](https://www.elastic.co/docs/explore-analyze/ai-features/llm-guides/llm-connectors). When you use one of these features, you can select any LLM connector that's configured in your environment. The connector you select for one feature does not affect which connector any other feature uses. For specific configuration instructions, refer to each feature's documentation.

### AI Assistant for Security

[Elastic AI Assistant for Security](https://www.elastic.co/docs/solutions/security/ai/ai-assistant) helps you with tasks such as alert investigation, incident response, and query generation throughout Elastic Security. It provides a chat interface where you can ask questions about the Elastic Stack and your data, and provides contextual insights that explain errors and messages and suggest remediation steps.

### Attack Discovery

[Attack Discovery](https://www.elastic.co/docs/solutions/security/ai/attack-discovery) uses AI to triage your alerts and identify potential threats. Each "discovery" represents a potential attack and describes relationships among alerts to identify related users and hosts, map alerts to the MITRE ATT&CK matrix, and help identify threat actors.

### Automatic Migration

[Automatic Migration](https://www.elastic.co/docs/solutions/security/get-started/automatic-migration) uses AI to help you migrate Splunk assets to Elastic Security by translating them into the necessary format and adding them to your Elastic Security environment. It supports the following asset types:
- Splunk rules
- Splunk dashboards


### Automatic Import

[Automatic Import](https://www.elastic.co/docs/solutions/security/get-started/automatic-import) helps you ingest data from sources that do not have prebuilt Elastic integrations. It uses AI to parse a sample of the data you want to ingest, and creates a new integration specifically for that type of data.

### Automatic Troubleshooting

[Automatic troubleshooting](https://www.elastic.co/docs/solutions/security/manage-elastic-defend/automatic-troubleshooting) uses AI to help you identify and resolve issues that could prevent Elastic Defend from working as intended. It provides actionable insights into the following common problem areas:
- **Policy responses**: Detect warnings or failures in Elastic Defend’s integration policies.
- **Third-party antivirus (AV) software**: Identify installed third-party antivirus (AV) products that might conflict with Elastic Defend.


### Entity summary

<applies-to>
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available since 9.3
</applies-to>

[Entity summary](/docs/solutions/security/advanced-entity-analytics/view-entity-details#entity-summary), available in the entity details flyout, uses AI to generate a summary of a user's or host's security context. It aggregates information such as risk scores, asset criticality, vulnerabilities, and machine learning anomalies to provide a consolidated view of the entity's security posture. The summary helps you prioritize investigations and identify recommended next steps.