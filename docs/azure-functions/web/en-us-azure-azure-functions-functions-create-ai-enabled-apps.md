# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps

Title: Use AI tools and models in Azure Functions

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps

Published Time: Fri, 06 Mar 2026 18:05:10 GMT

Markdown Content:
Azure Functions provides serverless compute resources that integrate with AI and Azure services to streamline building cloud-hosted intelligent applications. This article provides a survey of the breadth of AI-related scenarios, integrations, and other AI resources that you can use in your function apps.

Consider using Azure Functions in your AI-enabled experiences for these scenarios:

| Scenario | Description |
| --- | --- |
| [Tools and MCP servers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#tools-and-mcp-servers) | Functions lets you create and host remote Model Content Protocol (MCP) servers and implement various AI tools. MCP servers are the industry standard for enabling function calling through remote tools. |
| [Agentic workflows](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#agentic-workflows) | Durable Functions helps you create multistep, long-running agent operations with built-in fault tolerance. |
| [Retrieval-augmented generation (RAG)](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#retrieval-augmented-generation) | RAG systems require fast data retrieval and processing. Functions can interact with multiple data sources simultaneously and provide the rapid scale required by RAG scenarios. |

Select one of these scenarios to learn more in this article.

This article is language-specific, so make sure you choose your programming language at the [top of the page](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#top).

AI models and agents use _function calling_ to request external resources known as _tools_. Function calling lets models and agents dynamically invoke specific functionality based on the context of a conversation or task.

Functions is particularly well-suited for implementing function calling in agentic workflows because it efficiently scales to handle demand and provides [binding extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings) that simplify connecting agents with remote Azure services. When you build or host AI tools in Functions, you also get serverless pricing models and platform security features.

The Model Context Protocol (MCP) is the industry standard for interacting with remote servers. It provides a standardized way for AI models and agents to communicate with external systems. An MCP server lets these AI clients efficiently determine the tools and capabilities of an external system.

Azure Functions currently supports exposing your function code by using these types of tools:

| Tool type | Description |
| --- | --- |
| [Remote MCP server](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#remote-mcp-servers) | Create custom MCP servers or host SDK-based MCP servers. |
| [Queue-based Azure Functions tool](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-ai-enabled-apps#queue-based-azure-functions-tools) | Microsoft Foundry provides a specific Azure Functions tool that enables asynchronous function calling by using message queues. |

Functions supports these options for creating and hosting remote MCP servers:

*   Use the [MCP binding extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) to create and host custom MCP servers as you would any other function app.
*   Self host MCP servers created by using the official MCP SDKs. _This hosting option is currently in preview._

Here's a comparison of the current MCP server hosting options provided by Functions:

| Feature | [MCP binding extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) | Self-hosted MCP servers |
| --- | --- | --- |
| Current support level | GA | Preview* |
| Programming model | [Functions triggers and bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings) | Standard MCP SDKs |
| Stateful execution | Supported | Not currently supported |
| Languages currently supported | C# (isolated process) Python TypeScript JavaScript Java | C# (isolated process) Python TypeScript Java |
| Other requirements | None | Streamable HTTP transport |
| How implemented | [MCP binding extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp) | [Custom handlers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-custom-handlers) |

*Configuration details for self-hosted MCP servers change during the preview.

Here are some options to help you get started hosting MCP servers in Functions:

| Options | MCP binding extensions | Self-hosted MCP servers |
| --- | --- | --- |
| Documentation | [MCP binding extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp?pivots=programming-language-csharp) | n/a |
| Samples | [Remote custom MCP server](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) | [Weather server](https://github.com/Azure-Samples/mcp-sdk-functions-hosting-dotnet) |
| Templates | [HelloTool](https://github.com/Azure/azure-functions-templates/tree/dev/Functions.Templates/Templates/McpToolTrigger-CSharp-Isolated) | n/a |

| Options | MCP binding extensions | Self-hosted MCP servers |
| --- | --- | --- |
| Documentation | [MCP binding extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp?pivots=programming-language-python) | n/a |
| Samples | [Remote custom MCP server](https://github.com/Azure-Samples/remote-mcp-functions-python) | [Weather server](https://github.com/Azure-Samples/mcp-sdk-functions-hosting-python) |

| Options | MCP binding extensions | Self-hosted MCP servers |
| --- | --- | --- |
| Documentation | [MCP binding extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp?pivots=programming-language-typescript) | n/a |
| Samples | [Remote custom MCP server](https://github.com/Azure-Samples/remote-mcp-functions-typescript) | [Weather server](https://github.com/Azure-Samples/mcp-sdk-functions-hosting-node) |

| Options | MCP binding extensions | Self-hosted MCP servers |
| --- | --- | --- |
| Documentation | [MCP binding extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp?pivots=programming-language-javascript) | n/a |
| Samples | Not yet available | n/a |

| Options | MCP binding extensions | Self-hosted MCP servers |
| --- | --- | --- |
| Documentation | [MCP binding extensions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp?pivots=programming-language-java) | n/a |
| Samples | Not yet available | Not yet available |

PowerShell isn't currently supported for either MCP server hosting option.

In addition to MCP servers, you can implement AI tools by using Azure Functions with queue-based communication. Foundry provides Azure Functions-specific tools that enable asynchronous function calling by using message queues. With these tools, AI agents interact with your code by using messaging patterns.

This tool approach is ideal for Foundry scenarios that require:

*   Reliable message delivery and processing
*   Decoupling between AI agents and function execution
*   Built-in retry and error handling capabilities
*   Integration with existing Azure messaging infrastructure

Here are some reference samples for function calling scenarios:

> Uses a [Foundry Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/) client to call a custom remote MCP server implemented by using Azure Functions.

> Uses function calling features for agents in Azure AI SDKs to implement custom function calling.

AI-driven processes often determine how to interact with models and other AI assets. However, some scenarios require a higher level of predictability or well-defined steps. These directed agentic workflows orchestrate separate tasks or interactions that agents must follow.

The [Durable Functions extension](https://learn.microsoft.com/en-us/azure/azure-functions/durable/what-is-durable-task) helps you take advantage of the strengths of Functions to create multistep, long-running operations with built-in fault tolerance. These workflows work well for your directed agentic workflows. For example, a trip planning solution might first gather requirements from the user, search for plan options, obtain user approval, and finally make required bookings. In this scenario, you can build an agent for each step and then coordinate their actions as a workflow using Durable Functions.

For more workflow scenario ideas, see [Application patterns](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-sequence) in Durable Functions.

Because Functions can handle multiple events from various data sources simultaneously, it's an effective solution for real-time AI scenarios, like RAG systems that require fast data retrieval and processing. Rapid event-driven scaling reduces the latency your customers experience, even in high-demand situations.

Here are some reference samples for RAG-based scenarios:

> For RAG, you can use SDKs, including Azure Open AI and Azure SDKs, to build your scenarios. ::: zone-end

> Shows you how to create a friendly chat bot that issues simple prompts, receives text completions, and sends messages, all in a stateful session using the [OpenAI binding extension](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-openai).

Functions lets you build apps in your preferred language and use your favorite libraries. Because of this flexibility, you can use a wide range of AI libraries and frameworks in your AI-enabled function apps.

Here are some key Microsoft AI frameworks you should be aware of:

| Framework/library | Description |
| --- | --- |
| [Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) | Easily build AI agents and agentic workflows. |
| [Agent Service](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview) | A fully managed service for building, deploying, and scaling AI agents with enterprise-grade security, built-in tools, and seamless integration with Azure Functions. |
| [Foundry Tools SDKs](https://learn.microsoft.com/en-us/azure/ai-foundry/) | By working directly with client SDKs, you can use the full breadth of Foundry Tools functionality directly in your function code. |

Functions also lets your apps reference third-party libraries and frameworks, so you can use all of your favorite AI tools and libraries in your AI-enabled functions.

*   [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios)
