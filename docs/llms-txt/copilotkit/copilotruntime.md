# CopilotRuntime

Copilot Runtime is the back-end component of CopilotKit, enabling interaction with LLMs.

This is the reference for the `CopilotRuntime` class. For more information and example code snippets, please see [Concept: Copilot Runtime](https://docs.copilotkit.ai/concepts/copilot-runtime).

## [Usage](https://docs.copilotkit.ai/reference/classes/CopilotRuntime\#usage)

```
import { CopilotRuntime } from "@copilotkit/runtime";

const copilotKit = new CopilotRuntime();
```

## [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/CopilotRuntime\#constructor-parameters)

middlewareMiddleware

Middleware to be used by the runtime.

```
onBeforeRequest: (options: {
  threadId?: string;
  runId?: string;
  inputMessages: Message[];
  properties: any;
}) => void | Promise<void>;
```

```
onAfterRequest: (options: {
  threadId?: string;
  runId?: string;
  inputMessages: Message[];
  outputMessages: Message[];
  properties: any;
}) => void | Promise<void>;
```

actionsActionsConfiguration<T>

A list of server side actions that can be executed. Will be ignored when remoteActions are set

remoteActionsCopilotKitEndpoint\[\]

Deprecated: Use `remoteEndpoints`.

remoteEndpointsEndpointDefinition\[\]

A list of remote actions that can be executed.

langserveRemoteChainParameters\[\]

An array of LangServer URLs.

delegateAgentProcessingToServiceAdapterboolean

Delegates agent state processing to the service adapter.

When enabled, individual agent state requests will not be processed by the agent itself.
Instead, all processing will be handled by the service adapter.

observability\_cCopilotObservabilityConfig

Configuration for LLM request/response logging.
Requires publicApiKey from CopilotKit component to be set:

```
<CopilotKit publicApiKey="ck_pub_..." />
```

Example logging config:

```
logging: {
  enabled: true, // Enable or disable logging
  progressive: true, // Set to false for buffered logging
  logger: {
    logRequest: (data) => langfuse.trace({ name: "LLM Request", input: data }),
    logResponse: (data) => langfuse.trace({ name: "LLM Response", output: data }),
    logError: (errorData) => langfuse.trace({ name: "LLM Error", metadata: errorData }),
  },
}
```

mcpEndpointsMCPEndpointConfig\[\]

Configuration for connecting to Model Context Protocol (MCP) servers.
Allows fetching and using tools defined on external MCP-compliant servers.
Requires providing the `createMCPClient` function during instantiation.
@experimental

createMCPClientCreateMCPClientFunction

A function that creates an MCP client instance for a given endpoint configuration.
This function is responsible for using the appropriate MCP client library
(e.g., `@copilotkit/runtime`, `ai`) to establish a connection.
Required if `mcpEndpoints` is provided.

```
import { experimental_createMCPClient } from "ai"; // Import from vercel ai library
// ...
const runtime = new CopilotRuntime({
  mcpEndpoints: [{ endpoint: "..." }],
  async createMCPClient(config) {
    return await experimental_createMCPClient({
      transport: {
        type: "sse",
        url: config.endpoint,
        headers: config.apiKey
          ? { Authorization: `Bearer ${config.apiKey}` }
          : undefined,
      },
    });
  }
});
```

processRuntimeRequestrequest: CopilotRuntimeRequest

// \-\-\- MCP Instruction Injection Method ---

requestCopilotRuntimeRequestrequired

discoverAgentsFromEndpointsgraphqlContext: GraphQLContext

graphqlContextGraphQLContextrequired

loadAgentStategraphqlContext: GraphQLContext, threadId: string, agentName: string

graphqlContextGraphQLContextrequired

threadIdstringrequired

agentNamestringrequired

[Previous\\
\\
useLangGraphInterrupt](https://docs.copilotkit.ai/reference/hooks/useLangGraphInterrupt) [Next\\
\\
OpenAIAdapter](https://docs.copilotkit.ai/reference/classes/llm-adapters/OpenAIAdapter)

### On this page

[Usage](https://docs.copilotkit.ai/reference/classes/CopilotRuntime#usage) [Constructor Parameters](https://docs.copilotkit.ai/reference/classes/CopilotRuntime#constructor-parameters)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/classes/CopilotRuntime.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## LangGraph Interrupt Hook
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageUsage