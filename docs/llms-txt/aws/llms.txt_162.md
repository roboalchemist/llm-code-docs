# Source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/llms.txt

# Amazon Bedrock AgentCore Developer Guide

- [Overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [Supported AWS Regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)
- [Get started with AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-toolkit.html)
- [Understand the available interfaces for using AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/develop-agents.html)
- [AgentCore MCP Server: Vibe coding with your coding assistant](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/mcp-getting-started.html)
- [Tagging resources](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tagging.html)
- [Quotas](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html)
- [Document history](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/doc-history.html)

## [AgentCore Runtime: Host agent or tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)

- [How it works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html): Learn how the AgentCore Runtime provides a fully managed, purpose-built environment for deploying and running AI agents or tools in the cloud.

### [Understand the AgentCore Runtime service contract](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-service-contract.html)

Learn about the Amazon Bedrock AgentCore service contract that defines the standardized communication protocol for your agent applications to integrate with the AgentCore Runtime hosting.

- [HTTP protocol contract](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-http-protocol-contract.html): Understand the requirements for implementing the HTTP protocol in your agent application.
- [MCP protocol contract](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp-protocol-contract.html): Understand the requirements for implementing the Model Context Protocol (MCP) in your agent application.
- [A2A protocol contract](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a-protocol-contract.html): Learn about the A2A protocol contract requirements for implementing agent-to-agent communication in Amazon Bedrock AgentCore.
- [IAM Permissions for AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html): The following are IAM permissions you need to create an agent in an AgentCore Runtime and the execution role permissions that an agent needs to run in an AgentCore Runtime.

### [Get started with AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-getting-started.html)

Learn how Amazon Bedrock AgentCore Runtime lets you use any agent framework

- [Get started with starter toolkit (Python)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-toolkit.html): This tutorial shows you how to use the Amazon Bedrock AgentCore starter toolkit to deploy a Python agent to an Amazon Bedrock AgentCore Runtime.
- [Get started with starter toolkit (TypeScript)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-toolkit-typescript.html): This tutorial shows you how to use the Amazon Bedrock AgentCore starter toolkit to deploy a TypeScript agent to an Amazon Bedrock AgentCore Runtime.
- [Get started without the starter toolkit](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-custom.html): Learn how to deploy a custom agent to AgentCore Runtime using FastAPI and Docker.
- [Get started with direct code deployment](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-code-deploy.html): Deploy Python agents to Amazon Bedrock AgentCore Runtime using ZIP file archives for faster development and simpler packaging.
- [Get started with bidirectional streaming using WebSocket](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-websocket.html): Learn how to deploy agents that support WebSocket streaming for real-time bidirectional communication with Amazon Bedrock AgentCore Runtime.
- [Use any agent framework](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-any-agent-framework.html): Learn how Amazon Bedrock AgentCore Runtime lets you use any agent framework
- [Use any foundation model](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-any-model.html): Learn how Amazon Bedrock AgentCore Runtime lets you use any foundation model
- [Deploy MCP servers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html): Learn how to create, test, and deploy your first Model Context Protocol (MCP) server using the AgentCore Runtime.
- [Stateful MCP features](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/mcp-stateful-features.html): Learn how to build stateful MCP servers that use features including resources, prompts, tools, elicitation, sampling, and progress notifications.
- [Deploy A2A servers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html): Amazon Bedrock AgentCore AgentCore Runtime lets you deploy and run Agent-to-Agent (A2A) servers in the AgentCore Runtime.

### [Use isolated sessions for agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html)

Learn how to use isolated sessions to maintain context across multiple invocations while ensuring complete security and data isolation between users.

- [Configure lifecycle settings](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-lifecycle-settings.html): The lifecycleConfiguration input parameter to CreateAgentRuntime lets you manage the lifecycle of runtime sessions and resources in Amazon Bedrock AgentCore Runtime.
- [Stop a running session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-stop-session.html): The StopRuntimeSession operation lets you immediately terminate active agent AgentCore Runtime sessions for proper resource cleanup and session lifecycle management.
- [Handle asynchronous and long running agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html): Learn how to implement asynchronous processing in the Amazon Bedrock AgentCore SDK to handle long-running operations without blocking responses.
- [Stream agent responses](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/response-streaming.html): The following Strands Agents example shows how an AgentCore Runtime agent can stream a response back to a client.
- [Pass custom headers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-header-allowlist.html): Learn how to pass headers from your request to your agent.
- [Authenticate and authorize with Inbound Auth and Outbound Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html): Learn how to set up authentication and authorization for your agent runtime using OAuth and JWT bearer tokens.
- [AgentCore Runtime versioning and endpoints](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-runtime-versioning.html): Learn how Amazon Bedrock AgentCore implements automatic versioning for AgentCore Runtimes and how to manage different configurations using endpoints.
- [Invoke an agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html): Learn how to use the InvokeAgentRuntime operation to send requests to agent runtime endpoints and receive streaming responses.
- [Observe agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-observability.html): Learn how to monitor, track, and understand the internal decision-making processes and behaviors of your agents.
- [Troubleshoot](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-troubleshooting.html): This guide provides solutions to common issues when working with AgentCore Runtime.


## [AgentCore Memory: Add memory to your agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)

### [How it works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/how-it-works.html)

AgentCore Memory provides a set of APIs that let your AI agents seamlessly store, retrieve, and utilize both short-term and long-term memory.

- [Memory terminology](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-terminology.html)
- [Memory types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html): AgentCore Memory offers two types of memory that work together to create intelligent, context-aware AI agents:

### [Memory strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html)

Memory strategies determine what types of information to extract from raw conversations and how to process them into meaningful long-term memories.

### [Built-in strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-strategies.html)

AgentCore Memory provides built-in strategies to create memories.

### [Semantic memory strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/semantic-memory-strategy.html)

The semantic memory strategy is designed to identify and extract key pieces of factual information and contextual knowledge from conversational data.

- [System prompt for semantic memory strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-system-prompt.html): A system prompt is a combination of instructions that guide the LLM's behavior and output schema that defines how the model should present the result.

### [User preference memory strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/user-preference-memory-strategy.html)

The UserPreferenceMemoryStrategy is designed to automatically identify and extract user preferences, choices, and styles from conversational data.

- [System prompt for user preference memory strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-user-prompt.html): A system prompt is a combination of instructions that guide the LLM's behavior and output schema that defines how the model should present the result.

### [Summary strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/summary-strategy.html)

The SummaryStrategy is responsible for generating condensed, real-time summaries of conversations within a single session.

- [System prompt for summary strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-summary-prompt.html): A system prompt is a combination of instructions that guide the LLM's behavior and output schema that defines how the model should present the result.

### [Episodic memory strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/episodic-memory-strategy.html)

Episodic memory captures meaningful slices of user and system interactions so applications can recall context in a way that feels focused and relevant.

- [System prompt for episodic memory strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-episodic-prompt.html): A system prompt is a combination of instructions that guide the LLM's behavior and output schema that defines how the model should present the result.
- [Customize a strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-custom-strategy.html): For advanced or domain-specific use cases, you can create a custom strategy to gain fine-grained control over the long-term memory process.
- [Self-managed strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-self-managed-strategies.html): Amazon Bedrock AgentCore Memory self-managed custom strategies provide you with complete control over your memory extraction and consolidation pipelines.
- [Memory organization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html): Understand how sessions, actors, and namespaces organize memory in AgentCore Memory.
- [Memory record streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-record-streaming.html): Stream memory record lifecycle events from Amazon Bedrock AgentCore Memory to a Kinesis Data Stream in your account.
- [Compare long-term memory with Retrieval-Augmented Generation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-ltm-rag.html): Long-term memory in Amazon Bedrock AgentCore Memory serves as persistent storage for session-specific context, enabling agents to maintain continuity and personalization across interactions.
- [Get started with AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-get-started.html): Amazon Bedrock Amazon Bedrock AgentCore Memory lets you create and manage memory resources that store conversation context for your AI agents.

### [Create an AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-create-a-memory-store.html)

Learn how to use create a memory store

- [Encrypt your Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/storage-encryption.html): Learn about encryption options and security best practices for AgentCore Memory.

### [Use short-term memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-memory-short-term.html)

Learn how to use short-term memory in your AI agent to store interactions and messages as events in AgentCore Memory.

- [Create an event](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/short-term-create-event.html): Store various types of data within AgentCore Memory as events, organized by actor and session.
- [Get an event](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/short-term-get-event.html): Retrieve a specific raw event by its identifier from short-term memory in AgentCore Memory.
- [List events](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/short-term-list-events.html): List events from a specified session with optional filtering and pagination support to reconstruct conversation histories and analyze interaction patterns.
- [Delete an event](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/short-term-delete-event.html): Remove individual events from AgentCore Memory to maintain data privacy and relevance while preserving broader context and relationship structure.

### [Use long-term memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-memory-long-term.html)

Long-term memory is enabled by adding one or more memory strategies to an AgentCore Memory.

- [Enable long-term memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-enabling-long-term-memory.html): You can enable long-term memory in two ways: by adding strategies when you first create an AgentCore Memory, or by updating an existing resource to include them.
- [Specify memory organization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/specify-long-term-memory-organization.html): Understand how sessions, actors, and namespaces organize memory in AgentCore Memory.
- [Configure built-in strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html): AgentCore Memory provides pre-configured, built-in memory strategies for common use cases.
- [Configure a custom strategy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-custom-strategies.html): For advanced use cases, built-in with overrides strategies give you fine-grained control over the memory extraction process.
- [Save and retrieve insights](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-saving-and-retrieving-insights.html): Once you have configured a AgentCore Memory with at least one long-term memory strategy and the strategy is ACTIVE, the service will automatically begin processing conversational data to extract and store insights.
- [Retrieve memory records](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-retrieve-records.html): You can retrieve extracted memories using the RetrieveMemoryRecords API.
- [List memory records](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-list-memory-records.html): The ListMemoryRecords operation lets you retrieve memory records from a namespace prefix without performing a semantic search.
- [Delete memory records](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-delete-memory-records.html): The DeleteMemoryRecord API removes individual memory records from your AgentCore Memory, giving you control over what information persists in your application's memory.
- [Redrive failed ingestions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-redrive.html): Extraction from short-term memory to long-term memory is usually automatic.

### [AgentCore Memory examples](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-examples.html)

Learn how to use AgentCore Memory with Amazon Bedrock AgentCore through different SDK options including AWS SDK, Amazon Bedrock AgentCore SDK, and Strands SDK.

- [Customer support AI agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-customer-scenario.html): Learn how to build a customer support AI agent that uses AgentCore Memory to provide personalized assistance by maintaining conversation history and extracting long-term insights about user preferences.
- [Integrate with LangChain or LangGraph](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-integrate-lang.html): Learn how to integrate Amazon Bedrock AgentCore AgentCore Memory with LangChain and LangGraph frameworks to build conversational AI applications with persistent memory capabilities.
- [AWS SDK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/aws-sdk-memory.html): Use the AWS SDK to directly interact with AgentCore Memory. clients for fine-grained control over memory operations.
- [Amazon Bedrock AgentCore SDK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-sdk-memory.html): Use the Amazon Bedrock AgentCore SDK for a higher-level abstraction that simplifies memory operations and provides convenient methods for common use cases.
- [Strands Agents SDK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/strands-sdk-memory.html): Use the Strands Agents SDK for seamless integration with agent frameworks, providing automatic memory management and retrieval within conversational agents.
- [Amazon Bedrock capacity for built-in with overrides strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-capacity.html): When configuring built-in with overrides strategies, you must provide a memoryExecutionRoleArn for Amazon Bedrock operations.
- [Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-observability.html): You can monitor usage metrics for your memory in CloudWatch metrics.
- [Best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html): Learn best practices for using AgentCore Memory effectively in your AI agent applications.


## [AgentCore Gateway: Securely connect to tools and resources](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

- [Get started with AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-quick-start.html): Learn how to set up a Gateway and integrate it into your agents using the AgentCore Starter Toolkit in just 5 minutes.
- [Core concepts](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-core-concepts.html): This chapter explains the core concepts of Amazon Bedrock AgentCore Gateway, including Gateway, Gateway Target, and Authorization.
- [AgentCore Gateway features](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-features.html): Learn about features that you can enable for your gateway

### [Supported gateway targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-supported-targets.html)

Targets define the tools that your gateway will host.

- [Lambda functions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-lambda.html): Lambda targets allow you to connect your gateway to AWS Lambda functions that implement your tools.
- [API Gateway stages](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-api-gateway.html): Learn how to make an Amazon API Gateway REST API a target
- [OpenAPI schemas](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-schema-openapi.html): OpenAPI (formerly known as Swagger) is a widely used standard for describing RESTful APIs.
- [Smithy models](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-smithy-targets.html): Smithy is a language for defining services and software development kits (SDKs).
- [MCP servers targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-MCPservers.html): MCP servers provide local tools, data access, or custom functions for your interactions with models and agents in Bedrock AgentCore.
- [Integration provider templates](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-integrations.html): Amazon Bedrock AgentCore lets you add open source templates from the following integration providers as targets in your gateway:
- [Understand gateway tool naming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-tool-naming.html): The name of a tool in your gateway is dependent on the name of the target through which the tool can be accessed.

### [Prerequisites](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-prerequisites.html)

Learn about the prerequisites that are required for trying out examples

- [Set up dependencies and credentials](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-setup-tools-credentials.html): The AgentCore Gateway service involves the following main processes:
- [Set up permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-prerequisites-permissions.html): To use Amazon Bedrock AgentCore Gateway and its capabilities, you'll need to consider the following permissions:
- [Set up inbound authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html): Before you create your gateway, you must set up inbound authorization.
- [Set up outbound authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html): Outbound authorization lets Amazon Bedrock AgentCore gateways securely access gateway targets on behalf of users that were authenticated and authorized during inbound authorization.

### [Set up a gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building.html)

This chapter provides detailed guidance on building with Amazon Bedrock AgentCore Gateway, including creating gateways, adding targets, and connecting agents.

### [Create a gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-create.html)

This guide walks you through the process of creating and configuring an Amazon Bedrock AgentCore Gateway.

- [Create a gateway (console)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-create-console.html): Learn how to create a gateway using the console
- [Create a gateway (CLI)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-create-cli.html): You can use the Amazon Bedrock AgentCore starter toolkit CLI to create gateways with simplified commands.
- [Create a gateway (API)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-create-api.html): To create a AgentCore gateway using the API, make a CreateGateway request with one of the AgentCore control plane endpoints.

### [Add targets to a gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets.html)

After creating a gateway, you can add targets, which define the tools that your gateway will host.

- [Add a target using the AWS Management Console](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-console.html): In the AWS Management Console, you can add gateway targets when you create the gateway.
- [Add a target using the CLI](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-cli.html): You can use the Amazon Bedrock AgentCore starter toolkit CLI to add targets to an existing gateway with simplified commands.

### [Add a target using the API](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-api.html)

To add a target using the API, make a CreateGatewayTarget request with one of the AgentCore control plane endpoints and define a target configuration that matches the target type.

- [Specify authorization type and credentials](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets-authorization.html): You provide the credential provider configuration as a member of the array that the credentialProviderConfigurations field in the CreateGatewayTarget request body maps to.
- [Define the target configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-api-target-config.html): The target configuration depends on the target type that you're adding to the gateway.

### [Use a gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using.html)

This chapter explains how to use a Amazon Bedrock AgentCore Gateway to connect agents with tools and resources.

### [Gateway authorization and authentication](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-auth.html)

Learn about authorizing to your gateway and gateway target

- [Example: Starter toolkit default gateway authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-auth-ex-starter.html): If you used the AgentCore starter toolkit to create a gateway and a Lambda target, you'll authorize with the following:
- [Example: Authorization code grant](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-auth-ex-3lo.html): If you set up your gateway target with an authorization code grant (for more information, see ), the defaultReturnUrl that you specified when creating the gateway will be the link that the user's browser redirects to after authentication.
- [List gateway tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-list.html): To list all available tools that an AgentCore gateway provides, make a POST request to the gateway's MCP endpoint and specify tools/list as the method in the request body:
- [Call a gateway tool](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-call.html): To call a specific tool, make a POST request to the gateway's MCP endpoint and specify tools/call as the method in the request body, name of the tool, and the arguments:
- [Search for a gateway tool](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-semantic-search.html): If you enabled semantic search for your gateway when you created it, you can call the x_amz_bedrock_agentcore_search tool to search for tools in your gateway with a natural language query.
- [Connect an agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-agent-integration.html): After creating and testing your gateway, you can create and connect AI agents to your gateway.
- [Fine-grained access control](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-fine-grained-access-control.html): This chapter explains how to implement fine-grained access control for Amazon Bedrock AgentCore Gateway using interceptors and authorization policies.

### [Debug and assess your gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-debug.html)

You can use different tools to help debug your gateway before putting it into a production environment, including built-in AWS and AgentCore Gateway tools, as well as external tools such as the MCP inspector.

- [Turn on debugging messages](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-debug-messages.html): While your gateway is in development, you can turn on debugging messages to return details on target configuration issues, including lambda function errors, egress authorizer errors, target specification parameter validation errors.
- [Use the MCP Inspector](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-inspector.html): The MCP Inspector, available through the Model Context Protocol (MCP), is a developer tool that helps you test and debug MCP servers by through an interactive interface.

### [Log AgentCore Gateway API calls with CloudTrail](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-cloudtrail.html)

Amazon Bedrock AgentCore Gateway is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Gateway.

- [Gateway event types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-event-types.html): This section provides information about the types of events that Amazon Bedrock AgentCore Gateway logs to CloudTrail.
- [Enable data event logging for gateway resources](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/enabling-cloudtrail-data-event-logging.html): You can use CloudTrail data events to get information about Amazon Bedrock AgentCore Gateway requests.
- [Understanding AgentCore Gateway CloudTrail events](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/understanding-gateway-cloudtrail-log-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.

### [Advanced topics](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced.html)

This chapter covers advanced features and best practices for Amazon Bedrock AgentCore Gateway, including observability, custom tool development, and performance optimization.

- [Customize your gateway's encryption](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-encryption.html): Learn how to encrypt your gateway with a customer managed KMS key so that you can customize the encryption properties.
- [Custom domain names](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-custom-domains.html): This section explains how to set up a custom domain name for your Amazon Bedrock AgentCore Gateway endpoint using Amazon CloudFront and AWS CDK.

### [Gateway interceptors](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors.html)

This section explains how to configure and use interceptors with your Amazon Bedrock AgentCore Gateway to modify requests and responses at runtime.

- [Permissions for interceptors](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors-permissions.html): When configuring interceptors, your gateway service role must have the lambda:InvokeFunction IAM permissions to invoke the Lambda functions that serve as interceptors.
- [Types of interceptors](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors-types.html): There are two types of interceptors that can be configured on your gateway:
- [Configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors-configuration.html): Interceptors can be configured with an input parameter called passRequestHeaders
- [Examples](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors-examples.html): The following example shows a Python Lambda function that can handle both REQUEST and RESPONSE interceptor types.
- [Header propagation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-headers.html): This section explains how to configure header and query parameter propagation with your Amazon Bedrock AgentCore Gateway to pass context and authentication information to downstream targets.
- [Performance optimization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html): To optimize the performance of your Gateway implementations, consider the following best practices:


## [AgentCore Identity: Provide identity management for agent applications](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html)

### [Overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-overview.html)

In the rapidly evolving landscape of AI agents, organizations need robust identity management solutions that can handle the unique challenges associated with non-human identities.

- [Features](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html): AgentCore Identity offers a set of features designed to address the unique challenges of workload identity management and credential security:
- [Terminology](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-terminology.html): AgentCore Identity uses specific terminology to describe the components, processes, and relationships involved in workload identity management and credential handling.
- [Example use cases](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-use-cases.html): Amazon Bedrock AgentCore Identity supports a wide range of use cases across different industries and application types.

### [Get started with AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-getting-started.html)

Learn how to set up your development environment and build authenticated agents that can access external resources securely using Amazon Bedrock AgentCore Identity.

- [Build your first agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-getting-started-cognito.html): Amazon Bedrock AgentCore Identity provides a secure way to manage identities for your AI agents and enable authenticated access to external services.
- [Google Drive integration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-getting-started-google.html): Learn how to set up your development environment, install the AgentCore SDK, configure your first workload identity, and build a simple authenticated agent that can access external resources securely.

### [Using the console](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-how-to.html)

Learn how to use the AgentCore Identity console to set up OAuth clients and API keys.

### [Configure an OAuth client](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-oauth-client.html)

An OAuth client enables your agent to securely access external services on behalf of users without requiring them to share their credentials directly.

- [Add OAuth client using included provider](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-add-oauth-client-included.html): Built-in providers offer streamlined setup for popular services including Google, GitHub, Slack, and Salesforce.
- [Add OAuth client using custom provider](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-add-oauth-client-custom.html): Custom providers enable you to connect to any OAuth2-compatible resource server beyond the built-in provider options.
- [Update OAuth client](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-update-oauth-client.html): You can modify the configuration settings for your existing OAuth client.
- [Delete OAuth client](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-delete-oauth-client.html): When you no longer need an OAuth client, you can delete it from your account.

### [Configure an API key](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-api-key.html)

API keys provide key-based authentication for services that require direct key access with secure storage capabilities.

- [Add API key](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-add-api-key.html): API keys provide key-based authentication for services that require direct key access with secure storage capabilities.
- [Update API key](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-update-api-key.html): You can update an existing API key to replace the key value when your external service provider rotates credentials.
- [Delete API key](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-delete-api-key.html): When you no longer need an API key, you can delete it from your account.

### [Manage agent identities](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-manage-agent-ids.html)

Agent identities are the foundation of secure authentication and authorization in AgentCore Identity.

- [Understanding identities](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/understanding-agent-identities.html): Workload identities represent the digital identity of your agents within the AWS environment.
- [Agent identity directory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-identity-directory.html): The agent identity directory is a centralized collection of all workload identities within your AWS account.
- [Create identities](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/creating-agent-identities.html): You can create agent identities using several methods, including the AWS CLI and the AgentCore SDK, depending on your workflow and integration requirements.
- [Inbound JWT authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/inbound-jwt-authorizer.html): Use JWTs to authenticate and authorize API requests against Amazon Bedrock AgentCore Runtime and Amazon Bedrock AgentCore Gateway.

### [Manage credential providers](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-outbound-credential-provider.html)

Learn how authentication and token exchange work in Amazon Bedrock AgentCore Identity.

- [Supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html): AgentCore Identity supports two primary authentication patterns that address different agent use cases.
- [Configure credential provider](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-providers.html): Resource credential providers in AgentCore Identity act as intelligent intermediaries that manage the complex relationships between agents, identity providers, and resource servers.

### [Obtain credentials](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/obtain-credentials.html)

AgentCore Identity uses a workload access token to authorize agent access to credentials stored in the vault, and this token contains both the identity of the agent and the identity of the end user on whose behalf the agent is working.

- [Get workload access token](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/get-workload-access-token.html): Understanding what workload access tokens are, how to obtain them, and the security aspects of working with them is essential for building secure agent applications.
- [Obtain access token](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html): Learn how authentication and token exchange work in Amazon Bedrock AgentCore Identity.
- [OAuth 2.0 authorization URL session binding](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/oauth2-authorization-url-session-binding.html): AgentCore Identity provides OAuth 2.0 access token retrievals for your agent applications to access third-party application vendors or resources protected by identity providers / authorization servers.
- [Scope credential access](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/scope-credential-provider-access.html): You can use IAM policies to control which workload identities have access to specific credential providers.
- [Obtain API key](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/obtain-api-key.html): Once you have stored your API keys in the AgentCore Identity vault, you can retrieve them directly in your agent using the AgentCore SDK and the @requires_api_key annotation.

### [Provider setup](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idps.html)

Amazon Bedrock AgentCore Identity provides managed OAuth 2.0 supported providers for both inbound and outbound authentication.

- [Amazon Cognito](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-cognito.html): Amazon Cognito can be configured as an identity provider for accessing AgentCore Gateway and Runtime, or an AgentCore Identity credential provider for outbound resource access.
- [Auth0 by Okta](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-auth0.html): Auth0 can be configured as an identity provider for accessing AgentCore Gateway and Runtime, or an AgentCore Identity credential provider for outbound resource access.
- [Atlassian](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-atlassian.html): Atlassian can be configured as an AgentCore Identity credential provider for outbound resource access.
- [CyberArk](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-cyberark.html): CyberArk can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Dropbox](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-dropbox.html): Dropbox can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Facebook](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-facebook.html): Facebook can be configured as an AgentCore Identity credential provider for outbound resource access.
- [FusionAuth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-fusionauth.html): FusionAuth can be configured as an outbound resource credential provider for AgentCore Identity.
- [GitHub](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-github.html): GitHub can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Google](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-google.html): Google can be configured as an AgentCore Identity credential provider for outbound resource access.
- [HubSpot](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-hubspot.html): HubSpot can be configured as an AgentCore Identity credential provider for outbound resource access.
- [LinkedIn](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-linkedin.html): LinkedIn can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Microsoft](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-microsoft.html): Microsoft Entra ID can be configured as an identity provider for accessing AgentCore Gateway and Runtime, or an AgentCore Identity credential provider for outbound resource access.
- [Notion](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-notion.html): Notion can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Okta](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-okta.html): Okta can be configured as an identity provider for accessing AgentCore Gateway and Runtime, or an AgentCore Identity credential provider for outbound resource access.
- [OneLogin](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-onelogin.html): OneLogin can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Ping Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-pingidentity.html): Ping Identity's PingOne platform can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Reddit](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-reddit.html): Reddit can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Salesforce](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-salesforce.html): Salesforce can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Slack](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-slack.html): Slack can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Spotify](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-spotify.html): Spotify can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Twitch](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-twitch.html): Twitch can be configured as an AgentCore Identity credential provider for outbound resource access.
- [X](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-x.html): X can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Yandex](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-yandex.html): Yandex can be configured as an AgentCore Identity credential provider for outbound resource access.
- [Zoom](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-zoom.html): Zoom can be configured as an AgentCore Identity credential provider for outbound resource access.

### [Data protection](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-protection.html)

Learn how Amazon Bedrock AgentCore Identity protects your data through encryption, access controls, and security best practices.

- [Data encryption](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-data-encryption.html): Data encryption typically falls into two categories: encryption at rest and encryption in transit.
- [Set customer managed key policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/kms-key-policy-configuration.html)
- [Configure with API operations or an AWS SDK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/api-configuration-encryption.html): Set your key configuration in a SetTokenVaultCMK API request.
- [Configure KMS key for Token Vault on Console](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/console-configuration-encryption.html): The KMS key configuration determines how your token vault encrypts data at rest.
- [Identity resource tagging](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-tagging.html): Use tags to organize and manage your AgentCore Identity resources for cost allocation, access control, and operational visibility.


## [AgentCore Built-in Tools: Interact with your applications using built-in tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-tools.html)

- [How it works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-tools-how-it-works.html): Amazon Bedrock AgentCore Tools provide Code Interpreter and Browser capabilities that enable AI agents to execute code and interact with web content in secure, isolated environments.

### [AgentCore Code Interpreter: Execute code and analyze data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html)

Learn how to use the code interpreter built-in tool in Amazon Bedrock AgentCore to execute code, analyze data.

- [Pre-installed libraries](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-preinstalled-libraries.html): The AgentCore Code Interpreter comes with a comprehensive set of pre-installed Python libraries to support various data analysis, machine learning, and development tasks.

### [Get started with AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-getting-started.html)

AgentCore Code Interpreter enables your agents to execute Python code in a secure, managed environment.

- [Using AgentCore Code Interpreter via AWS Strands](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-using-strands.html): The following sections show you how to use the Amazon Bedrock AgentCore Code Interpreter with the Strands SDK.
- [Using AgentCore Code Interpreter directly](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-using-directly.html): The following sections show you how to use the Amazon Bedrock AgentCore Code Interpreter directly without an agent framework.
- [Run code from agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-building-agents.html): You can build agents that use the Code Interpreter tool to execute code and analyze data.
- [Write files to a session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-file-operations.html): You can use the Code Interpreter to read and write files in the sandbox environment.
- [Using Terminal Commands with an execution role](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-s3-integration.html): You can create a custom Code Interpreter tool with an execution role to upload/download files from Amazon S3.

### [Resource and session management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-resource-session-management.html)

The following topics show how the Amazon Bedrock AgentCore Code Interpreter works and how you can create the resources and manage sessions.

### [Resource management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-resource-management.html)

The AgentCore Code Interpreter provides two types of resources:

- [Creating an AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-create.html): You can create a Code Interpreter using the Amazon Bedrock AgentCore console, AWS CLI, or AWS SDK.
- [Listing AgentCore Code Interpreter tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-list.html): You can view a list of all your Code Interpreter tools to manage and monitor them.
- [Deleting an AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-delete.html): When you no longer need a Code Interpreter, you can delete it to free up resources and avoid unnecessary charges.

### [Session management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-session-characteristics.html)

The AgentCore Code Interpreter sessions have the following characteristics:

- [Starting a AgentCore Code Interpreter session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-start-session.html): After creating a Code Interpreter, you can start a session to execute code.
- [Executing code](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-execute-code.html): Once you have started a Code Interpreter session, you can execute code in the session.
- [Stopping a AgentCore Code Interpreter session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-stop-session.html): When you are finished using a Code Interpreter session, you should stop it to release resources and avoid unnecessary charges.
- [API Reference Examples](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-api-reference-examples.html): This section provides reference examples for common Code Interpreter operations using different approaches.
- [Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-observability.html): The AgentCore Code Interpreter provides the following observability features:

### [AgentCore Browser: interact with web applications](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html)

Learn how to use the AgentCore Browser built-in tool in Amazon Bedrock AgentCore to interact with web applications in a secure environment.

- [Get started with AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-onboarding.html): AgentCore Browser enables your agents to interact with web pages through a managed Chrome browser.
- [Using AgentCore Browser with other libraries](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-building-agents.html): You can build browser agents using various frameworks and libraries to automate web interactions.

### [Resource and session management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-resource-session-management.html)

The following topics show how the Amazon Bedrock AgentCore Browser works and how you can create the resources and manage sessions.

### [Resource management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-resource-management.html)

The AgentCore Browser provides two types of resources:

- [Creating an AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-create.html): You can create a Browser Tool using the Amazon Bedrock AgentCore console, AWS CLI, or AWS SDK.
- [Get AgentCore Browser tool](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-get.html): You can get information about the Browser tool in your account and view their details, status, and configurations.
- [Listing AgentCore Browser tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-list.html): You can list all browser tools in your account to view their details, status, and configurations.
- [Deleting an AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-delete.html): When you no longer need a browser tool, you can delete it to free up resources.

### [Session management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-session-characteristics.html)

The AgentCore Browser sessions have the following characteristics:

- [Starting a browser session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-start-session.html): After creating a browser, you can start a session to interact with web applications.
- [Get Browser session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-session-get.html): You can get information about a browser session that you have created.
- [Interacting with a browser session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-interact.html): Once you have started a Browser session, you can interact with it using the WebSocket API.
- [Listing browser sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-list-sessions.html): You can list all active browser sessions to monitor and manage your resources.
- [Stopping a browser session](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-stop-session.html): When you are finished using a Browser session, you should stop it to release resources and avoid unnecessary charges.
- [Updating browser streams](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-update-stream.html): You can update browser streams to enable or disable automation.
- [Reducing CAPTCHAs with Web Bot Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-web-bot-auth.html)
- [Rendering live view using DCV client](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-dcv-integration.html): Amazon Bedrock AgentCore's live view is powered by AWS DCV.

### [Observability and session replay](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-observability.html)

The AgentCore Browser provides the following observability features:

- [CloudWatch Metrics for AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-metrics.html): You can view the following metrics in Amazon CloudWatch:

### [Browser session recording and replay](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-session-replay.html)

Browser session recording and replay provides comprehensive observability for debugging, auditing, or training purposes.

- [How to use session replay](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/session-replay-how-to-use.html): Session recording captures all browser interactions and allows you to replay sessions for debugging, analysis, and monitoring.
- [Session replay programmatic examples](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/session-replay-programmatic-usage.html): For advanced use cases, you can build custom session replay viewers and integrate recording data into your own analysis workflows.
- [Browser Extensions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-extensions.html): Learn how to install custom browser extensions into Amazon Bedrock AgentCore Browser sessions to customize browser behavior for automation tasks.
- [Browser Profiles](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-profiles.html): Learn how to use browser profiles to persist and reuse browser profile data across multiple browser sessions.
- [Browser Proxies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-proxies.html): Route browser traffic through external proxy servers for IP stability, corporate infrastructure integration, and ease of use.
- [Troubleshoot built-in tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-tools-troubleshooting.html): This section provides solutions to common issues you might encounter when using Amazon Bedrock AgentCore built-in tools.


## [AgentCore Observability: Observe your agents and resources](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

- [Get started with AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html): Amazon Bedrock Amazon Bedrock AgentCore Observability helps you trace, debug, and monitor agent performance in production environments.
- [Add observability to your agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html)
- [Observability concepts](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html): This section defines the concepts of sessions, traces and spans as they relate to monitoring and observability of agents.

### [AgentCore generated observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html)

- [Runtime observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-runtime-metrics.html): This section describes the key performance metrics displayed in the runtime overview dashboard
- [Memory observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-memory-metrics.html): This section describes the key performance metrics displayed in memory overview dashboard
- [Gateway observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-gateway-metrics.html)
- [Built-in tools observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-tool-metrics.html): This section describes the key performance metrics displayed in the runtime overview dashboard
- [Identity observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-identity-metrics.html): This section describes the key performance metrics displayed in the identity overview dashboard
- [Policy in AgentCore observability data](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-policy-metrics.html): Learn about the observability data that Amazon Bedrock AgentCore provides for policy and policy engine resources.
- [View metrics for your agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-view.html)


## [Policy in AgentCore: Control Agent-to-Tool Interactions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)

- [Getting started with Policy in AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-getting-started.html): Set up a policy engine, create policies, and test policy enforcement with your AgentCore Gateway.
- [Core concepts](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html): Understand the key concepts and components of Policy in Amazon Bedrock AgentCore.
- [AgentCore Gateway and Policy in AgentCore IAM Permissions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-permissions.html): Learn about the required IAM permissions for using Amazon Bedrock AgentCore Gateway with Policy in AgentCore for fine-grained authorization control using Cedar policies.
- [Create a policy engine](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-create-engine.html): Create and configure a policy engine to store and evaluate your Cedar policies.

### [Create a policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-create-policies.html)

Create and manage Cedar policies using direct Cedar syntax or natural language authoring.

- [Understanding Cedar policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-understanding-cedar.html): Policy in AgentCore uses Cedar policies to control access to AgentCore Gateway tools.
- [Policy scope](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-scope.html): The scope defines what the policy applies to.
- [Policy conditions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-conditions.html): Conditions add fine-grained logic to policies using when and unless clauses:
- [Authorization flow](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-authorization-flow.html): Amazon Bedrock AgentCore Gateway evaluates Cedar policies against incoming requests.
- [Schema constraints](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-schema-constraints.html): Policies for Amazon Bedrock AgentCore Gateway must validate against a specific Cedar schema that is automatically generated from the Gateway's MCP tool manifest.
- [Limitations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-limitations-section.html): Cedar policies and the current Amazon Bedrock AgentCore Gateway implementation have certain limitations that affect policy authoring and functionality.
- [Common policy patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-common-patterns.html): These examples demonstrate frequently used Cedar policy patterns for common authorization scenarios in Amazon Bedrock AgentCore Gateway.
- [Time-based policy support](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-time-based.html): Policy in AgentCore supports time-based restrictions in Cedar policies through the context.system.now datetime value.
- [Writing policies in natural language](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-natural-language.html): Write authorization policies in natural language that can be automatically converted to Cedar using the natural language-based policy authoring feature.

### [Validate and test policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-validate-policies.html)

Use validation and analysis capabilities to verify policy correctness and surface warnings about policies that may not match your intended behavior before deploying them to production.

- [Validation and analysis overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-validation-overview.html)
- [Policy generation: per-policy validation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-generation-validation.html): When using the policy authoring service to generate policies from natural language, validation and analysis occur per individual policy during generation.
- [Policy create and update: per-policy engine validation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-create-update-validation.html): When creating or updating policies directly (not through generation), validation and analysis takes into account the new policy as well as its interactions with all preexisting policies in the policy engine.

### [Use policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-use-policies.html)

Associate policy engines with gateways and test policy enforcement in your agent applications.

- [Add policies to the Policy Engine](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/add-policies-to-engine.html): You can create one or more policies in your policy engine to control how agents interact with your enterprise tools and data through Amazon Bedrock AgentCore Gateway.
- [Create gateway with Policy Engine](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-gateway-with-policy.html): This section provides examples of creating a gateway with a policy engine associated for policy enforcement.
- [Update existing gateway with Policy Engine](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/update-gateway-with-policy.html): Associate a policy engine with an existing gateway:
- [Policy enforcement modes](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-enforcement-modes.html): Enforcement mode defines how the gateway applies policy decisions.
- [Use a AgentCore Gateway with Policy in AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/use-gateway-with-policy.html): Follow the gateway authorization and authentication guide to obtain the credentials needed for gateway access.
- [Manage Policies and Policy Engines](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/manage-policies-engines.html): Use these operations to manage your Policy Engines and policies.
- [Errors](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-use-errors.html): Policy in AgentCore operations can return the following types of errors:
- [Example policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/example-policies.html): This example demonstrates authorization policies for an insurance management system using Amazon Bedrock AgentCore Gateway and Cedar.

### [Advanced topics](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-advanced.html)

This chapter covers advanced features and best practices for Policy in AgentCore, including encryption customization and other topics.

- [Customize your policy engine's encryption](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-encryption.html): Learn how to encrypt your policy engine with a customer managed KMS key so that you can customize the encryption properties.


## [AgentCore Evaluations: Evaluate agent performance](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)

### [How it works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/how-it-works-evaluations.html)

Amazon Bedrock AgentCore Evaluations provides capabilities to assess the performance of AI agents.

- [Evaluation terminology](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-terminology.html): Understanding key concepts and terminology is essential for effectively using AgentCore Evaluations.
- [Evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluators.html): Evaluators are the core components that assess your agent's performance across different dimensions.
- [Evaluation types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-types.html): AgentCore Evaluations provides two evaluation types, which differ in when and how the evaluation is performed:

### [Built-in evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-evaluators-overview.html)

Built-in evaluators in AgentCore AgentCore Evaluations provide pre-configured evaluator for assessing your agents.

- [Cross region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-cross-region-inference.html): AgentCore AgentCore Evaluations will automatically select the optimal region within your geography to process your inference requests.
- [Prompt templates](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/prompt-templates-builtin.html): Each prompt template contains at least one placeholder, which is replaced with actual trace information before it is sent to the judge model.

### [Custom evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/custom-evaluators.html)

Custom evaluators in AgentCore Evaluations allow you to define your own evaluator model, evaluation instruction and scoring schemas.

- [Create evaluator](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-evaluator.html): The CreateEvaluator API creates a new custom evaluator that defines how to assess specific aspects of your agent's behavior.
- [List evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/list-evaluators.html): The ListEvaluators API returns a paginated list of all custom evaluators in your account and Region, including both your custom evaluators and built-in evaluators.
- [Update evaluator](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/update-evaluator.html): The UpdateEvaluator API modifies an existing custom evaluator's configuration, description, or evaluation level.
- [Get evaluator](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/get-evaluator.html): The GetEvaluator API retrieves complete details of a specific custom or built-in evaluator including its configuration, status, and lock state.
- [Delete evaluator](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/delete-evaluator.html): The DeleteEvaluator API permanently removes a custom evaluator and all its configuration data.

### [Online evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/online-evaluations.html)

An online evaluation configuration is a resource that defines how your agent is evaluated, including which evaluators to apply, which data sources to monitor, and evaluation parameters.

- [Prerequisites](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-prerequisites.html): Before you begin using Amazon Bedrock AgentCore Evaluations, ensure you have the necessary AWS permissions and service roles configured.
- [Create and deploy your agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-deploy-agent.html): If you have an agent already up and running in AgentCore Runtime, you can skip the following steps
- [Create online evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/create-online-evaluations.html): The CreateOnlineEvaluationConfig API creates a new online evaluation configuration that continuously monitors your agent's performance using live traffic.
- [Get online evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/get-online-evaluations.html): The GetOnlineEvaluationConfig API retrieves the complete details and current status of an existing online evaluation configuration.
- [List online evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/list-online-evaluations.html): The ListOnlineEvaluationConfigs API retrieves a paginated list of all online evaluation configurations in your account and Region.
- [Update online evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/update-online-evaluations.html): The UpdateOnlineEvaluationConfig API modifies an existing online evaluation configuration, allowing you to change evaluators, data sources, execution settings, and other parameters.
- [Delete online evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/delete-online-evaluations.html): The DeleteOnlineEvaluationConfig API permanently removes an online evaluation configuration and stops all associated evaluation processing.
- [Results and output](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/results-and-output.html): Online evaluation results are automatically saved to Amazon CloudWatch.

### [On-demand evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/on-demand-evaluations.html)

On-demand evaluation provides a flexible way to evaluate specific agent interactions by directly analyzing a chosen set of spans.

- [IAM permissions for on-demand evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/iam-permissions-on-demand.html): Your IAM user or role needs the following permissions to run on-demand evaluations:
- [Getting started with on-demand evaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-on-demand.html): Follow these steps to set up and run your first on-demand evaluation.
- [Understanding input spans](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/understanding-input-spans.html): The evaluate API accepts a list of sessionSpans, which consists of two types of entities: spans and events


## [Security](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security.html)

### [Data protection](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AgentCore.

- [Data encryption](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/data-encryption.html)

### [VPC and AWS PrivateLink](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc.html)

Use Amazon VPC and AWS PrivateLink to create private connections and configure Amazon Bedrock AgentCore Runtime for VPC access.

- [Use AWS PrivateLink to create a private connection](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and your AgentCore resources.
- [Configure Gateway VPC Egress](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-vpc-egress.html): The AgentCore Gateway service provides secure and controlled egress traffic management for your applications, enabling seamless communication with resources within your Virtual Private Cloud (VPC).
- [Configure AgentCore Runtime and built-in tools VPC configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html): You can configure Amazon Bedrock AgentCore Runtime and built-in tools (Code Interpreter and Browser Tool) to connect to resources in your Amazon Virtual Private Cloud (VPC).
- [Use VPC condition keys with AgentCore Runtime and built-in tools VPC settings](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-vpc-condition.html): Use AgentCore-specific condition keys for VPC settings to provide additional permission controls for your AgentCore Runtime and built-in tools.
- [Cross-region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html): Learn how to use cross-region inference to increase throughput and resilience of your chat requests.

### [Identity and access management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-iam.html)

How to authenticate requests and manage access your AgentCore resources.

- [How Amazon Bedrock AgentCore works with IAM](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AgentCore, learn what IAM features are available to use with AgentCore.
- [Identity-based policy examples](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AgentCore resources.
- [AWS managed policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AgentCore and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/service-linked-roles.html): Amazon Bedrock AgentCore uses IAM service-linked roles to manage network interfaces in your VPC.
- [Credentials Management](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-credentials-management.html): Learn about credentials management and best practices for setting up execution roles with Amazon Bedrock AgentCore.
- [Troubleshooting](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AgentCore and IAM.
- [Resource-based policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-based-policies.html): Learn how to use resource-based policies to control access to your Amazon Bedrock AgentCore Runtime and Gateway resources.
- [Compliance validation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AgentCore features for data resiliency.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
