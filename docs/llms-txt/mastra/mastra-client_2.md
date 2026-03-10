# Source: https://mastra.ai/reference/client-js/mastra-client

# Mastra Client SDK

The Mastra Client SDK provides a type-safe interface for interacting with your [Mastra Server](https://mastra.ai/docs/deployment/mastra-server) from your client environment.

## Usage example

```typescript
import { MastraClient } from '@mastra/client-js'

export const mastraClient = new MastraClient({
  baseUrl: 'http://localhost:4111/',
})
```

## Parameters

**baseUrl** (`string`): The base URL for the Mastra API. All requests will be sent relative to this URL.

**retries** (`number`): The number of times a request will be retried on failure before throwing an error. (Default: `3`)

**backoffMs** (`number`): The initial delay in milliseconds before retrying a failed request. This value is doubled with each retry (exponential backoff). (Default: `300`)

**maxBackoffMs** (`number`): The maximum backoff time in milliseconds. Prevents retries from waiting too long between attempts. (Default: `5000`)

**headers** (`Record<string, string>`): An object containing custom HTTP headers to include with every request.

**credentials** (`"omit" | "same-origin" | "include"`): Credentials mode for requests. See https\://developer.mozilla.org/en-US/docs/Web/API/Request/credentials for more info.

## Methods

**listAgents()** (`Promise<Record<string, GetAgentResponse>>`): Returns all available agent instances.

**getAgent(agentId)** (`Agent`): Retrieves a specific agent instance by ID.

**getMemoryThreads(params)** (`Promise<StorageThreadType[]>`): Retrieves memory threads for the specified resource and agent. Requires a \`resourceId\` and an \`agentId\`.

**createMemoryThread(params)** (`Promise<MemoryThread>`): Creates a new memory thread with the given parameters.

**getMemoryThread({ threadId, agentId })** (`MemoryThread`): Fetches a specific memory thread by ID.

**saveMessageToMemory(params)** (`Promise<{ messages: (MastraMessageV1 | MastraDBMessage)[] }>`): Saves one or more messages to the memory system. Returns the saved messages.

**getMemoryStatus()** (`Promise<MemoryStatus>`): Returns the current status of the memory system.

**listTools()** (`Record<string, Tool>`): Returns all available tools.

**getTool(toolId)** (`Tool`): Retrieves a specific tool instance by ID.

**listWorkflows()** (`Record<string, Workflow>`): Returns all available workflow instances.

**getWorkflow(workflowId)** (`Workflow`): Retrieves a specific workflow instance by ID.

**getVector(vectorName)** (`MastraVector`): Returns a vector store instance by name.

**listLogs(params)** (`Promise<LogEntry[]>`): Fetches system logs matching the provided filters.

**getLog(params)** (`Promise<LogEntry>`): Retrieves a specific log entry by ID or filter.

**listLogTransports()** (`string[]`): Returns the list of configured log transport types.

**getTrace(traceId)** (`Promise<TraceRecord>`): Retrieves a specific trace by ID, including all its spans and details.

**getTraces(params)** (`Promise<GetTracesResponse>`): Retrieves paginated list of trace root spans with optional filtering. Use getTrace() to get complete traces with all spans.