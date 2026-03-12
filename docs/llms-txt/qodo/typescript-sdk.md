# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/features/typescript-sdk.md

# Typescript SDK

Run Qodo Command agents entirely in-process (no child process) from your Node/TypeScript app using QodoClient. It shares the same orchestration core as the CLI SDK mode and is designed for concurrency, quiet logs, and typed streaming.

Highlights:

* Zero child processes – fully in-process
* Per-client environment isolation (config + session + tools) for safe parallel use
* Auto-approval of tools by default (configurable)
* Stream rich events or run to completion
* Programmatic agent configs (define in code) or load from file/string

### Install / Import <a href="#install--import" id="install--import"></a>

Prerequisites: set QODO\_API\_KEY in your environment (and optional QODO\_BASE\_URL) so the client can reach the Qodo backend.

```bash
export QODO_API_KEY=your_api_key_here
# export QODO_BASE_URL=https://api.qodo.ai  # optional override
```

```ts
// From the main package
import { QodoClient, agent, command, mode, jsonSchema } from '@qodo/command';
// Types only (optional):
// import type { AgentFileObject, CommandConfig, ModeConfig, MCPConfig, OutputSchema } from '@qodo/command';
```

### Quick Start (blocking) <a href="#quick-start-blocking" id="quick-start-blocking"></a>

```ts
const client = new QodoClient({
  agentFile: 'agents/example.toml',
  model: 'gpt-5.2-high',          // optional model override
  autoApproveTools: true,       // default true
  // New: Working directory UX
  cwd: '/path/to/project',      // default shell/git cwd if tool args omit cwd (auto-derives from agentFile if not provided)
  projectRoots: ['/path/to/project', '/path/to/shared-lib'], // allowed roots for filesystem/ripgrep
});

const final = await client.run('build', {
  args: { target: 'prod' },
});

// Prefer structured_output, fall back to final_output
console.log(final?.result?.structured_output ?? final?.result?.final_output);
await client.dispose();
```

### Streaming (typed event feed) <a href="#streaming-typed-event-feed" id="streaming-typed-event-feed"></a>

```ts
const client = new QodoClient({ agentFile: 'agents/example.toml' });

for await (const ev of client.stream('build', { args: { target: 'prod' } })) {
  switch (ev.type) {
    case 'init':
      // { protocol, model, pid }
      break;
    case 'hello':
      // { message: 'Hello from SDK mode! 👋', mode: 'sdk', ready: true }
      break;
    case 'messages':
      // ev.data.messages.langchain (LangChain-style) and .openai (OpenAI chat array)
      break;
    case 'progress':
      // Structured progress JSON emitted by the agent
      break;
    case 'isLoading':
      // boolean – true while running
      break;
    case 'error':
      console.error('Agent error:', ev.data.message);
      break;
    case 'final':
      console.log('Done:', ev.data.result.structured_output ?? ev.data.result.final_output);
      break;
  }
}

await client.dispose();
```

### Defining agents in code (recommended for libraries) <a href="#defining-agents-in-code-recommended-for-libraries" id="defining-agents-in-code-recommended-for-libraries"></a>

You can define the agent configuration programmatically with strict types and sensible SDK defaults (execution\_strategy defaults to 'act').

```ts
const myAgent = agent({
  version: '1.0',
  system_prompt: 'You are a helpful engineering assistant.',
  model: 'gpt-5.2-high',
  available_tools: ['filesystem.list', 'ripgrep.search'],
  commands: {
    build: command({
      description: 'Build the project',
      instructions: 'Analyze the repository and produce a production build.',
      available_tools: ['shell.exec'],
      arguments: [
        { name: 'target', type: 'string', required: false, description: 'Build target' },
      ],
      output_schema: jsonSchema('build_result', {
        type: 'object',
        required: ['success'],
        properties: {
          success: { type: 'boolean', description: 'Whether build succeeded' },
          logs: { type: 'string', description: 'Build logs' },
        },
      }),
      permissions: 'rwx',
    }),
  },
  modes: {
    chat: mode({
      description: 'Conversational mode',
      instructions: 'Answer questions succinctly.',
      available_tools: ['ripgrep.search'],
    }),
  },
  mcpServers: {
    shell: { command: 'bash' },
    ripgrep: { command: 'rg' },
  },
});

// Create a client from the in-memory agent object
const client = QodoClient.fromAgent(myAgent, { autoApproveTools: true });
const result = await client.run('build', { args: { target: 'prod' } });
console.log(result?.result?.structured_output ?? result?.result?.final_output);
await client.dispose();
```

See also: docs/sdk/agent-object.md for more type-centric examples.

### Using agent content strings <a href="#using-agent-content-strings" id="using-agent-content-strings"></a>

```ts
const toml = `
version = '1.0'
model = 'gpt-5.2-high'

[commands.build]
description = 'Build the project'
instructions = 'Analyze the repo and produce a build.'
available_tools = ['shell.exec']
`;

const client = new QodoClient({ agentContent: toml });
await client.run('build');
await client.dispose();
```

### Per-call output schema override <a href="#per-call-output-schema-override" id="per-call-output-schema-override"></a>

You can supply an output\_schema per call. Pass either a JSON string (validated) or a structured object (use jsonSchema helper).

```ts
const perCallSchema = jsonSchema('answer', {
  type: 'object',
  required: ['answer'],
  properties: { answer: { type: 'string' } },
});

const res = await client.run('build', {
  args: { target: 'debug' },
  outputSchema: perCallSchema,
});
console.log(res.result.structured_output); // { answer: '...' }
```

### Session context and resumability <a href="#session-context-and-resumability" id="session-context-and-resumability"></a>

* withSessionIds: Prefetch and inject summaries from previous session IDs (useful for continuity):

```ts
const client = new QodoClient({
  agentFile: 'agents/example.toml',
  withSessionIds: ['prev-session-id-1', 'prev-session-id-2'],
});
const res = await client.run('build');
```

* Resuming a specific session: provide flags.sid. If the session is resumable, QodoClient will call resume under the hood.

```ts
const client = new QodoClient({
  agentFile: 'agents/example.toml',
  flags: { sid: 'existing-session-id' },
});
await client.run('build');
```

### Working directory and allowed roots <a href="#working-directory-and-allowed-roots" id="working-directory-and-allowed-roots"></a>

* cwd (optional): Sets a preferred execution working directory for shell/git tools when their args omit cwd.
  * If not provided but agentFile is set, QodoClient defaults cwd = dirname(agentFile).
  * If neither is provided, falls back to process.cwd().
* projectRoots (optional): Additional allowed directories for filesystem/ripgrep tools. QodoClient uses \[cwd, ...projectRoots] for allowed roots.
* You can still override per-tool: pass cwd in shell\_execute arguments.

### Command and mode selection <a href="#command-and-mode-selection" id="command-and-mode-selection"></a>

QodoClient resolves the run target as follows (priority):

* flags.mode → selected as a command equivalent from the agent file
* explicit command name passed to run()/stream()
* flags.command → if provided
* single command in the agent file → if only one exists

Tips:

* For conversational chat, define a mode (e.g., chat) and call with flags.mode = 'chat'.
* For free-form prompts, ensure your agent has a single default command or call with a dedicated mode.

### Tool approvals <a href="#tool-approvals" id="tool-approvals"></a>

* autoApproveTools (default true) will auto-approve all tool calls (non-interactive, CI-friendly).
* Set autoApproveTools: false to disable auto-approval. Note: the client remains non-interactive; you are responsible for handling any user engagement prompts emitted via messages.

### Event reference <a href="#event-reference" id="event-reference"></a>

QodoClient streams events with this shape:

* init
  * data: { protocol: 'qodo.sdk.v1', model: string, pid: number }
* hello
  * data: { message: string, mode: 'sdk', ready: true }
* messages
  * data: { messages: { langchain: Array<{ type: string; data: any }>, openai: any\[] } }
* progress
  * data: any (JSON parsed from assistant progress messages)
* isLoading
  * data: boolean
* error
  * data: { message: string }
* final
  * data: { success: boolean, error?: string, session\_id: string, model: string, result: { structured\_output?: any; final\_output?: string }, messages: { langchain: any\[]; openai: any\[] }, meta: { tools\_auto\_approved: boolean; subagents\_used: boolean } }

### Flags and advanced options <a href="#flags-and-advanced-options" id="flags-and-advanced-options"></a>

* model: Override the model at construction.
* flags: Arbitrary CLI-style flags supported by the core (e.g., { mode: 'chat', tools: 'shell.exec,ripgrep.search', noTools: 'filesystem.\*', sid: '...' }).
* mcpFile: Path to an MCP servers file; also supports defining servers in the agent object under mcpServers.
* debug: true to keep internal logs enabled (by default, QodoClient mutes internal logging while streaming).
* debugChatMessages: true to pretty-print AI/chat messages and tool calls to stdout while streaming (useful for debugging agent behavior).

### Cancellation and cleanup <a href="#cancellation-and-cleanup" id="cancellation-and-cleanup"></a>

```ts
const client = new QodoClient({ agentFile: 'agents/example.toml' });
const promise = client.run('build');
setTimeout(() => client.cancel(), 1000); // request cancellation
const final = await promise;
await client.dispose();
```

### Concurrency & isolation <a href="#concurrency--isolation" id="concurrency--isolation"></a>

You can safely create multiple QodoClient instances in parallel. Each instance owns its own logical "environment":

* Independent config/session (agent config + SessionContext)
* Its own MessageManager stream
* Its own MCP server registry and MCPManager (tool list, approvals, connection state)

Some resources remain process-wide (shared across clients), such as:

* Backend metadata/cache from ServerData
* stdout/stderr and global console (unless muted via `debug` or `debugChatMessages`)

Example:

```ts
const a = new QodoClient({ agentFile: 'agents/a.toml' });
const b = new QodoClient({ agentFile: 'agents/b.toml' });
const [ra, rb] = await Promise.all([
  a.run('build', { args: { target: 'debug' } }),
  b.run('build', { args: { target: 'prod' } }),
]);
await Promise.all([a.dispose(), b.dispose()]);
```

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

* If you don’t see progress or messages, ensure your agent emits them and that tools are available. Use debug: true to surface internal logs.
* If you pass a command name and your agent doesn’t contain it, QodoClient falls back to the default/selected command. Double‑check the command list in your agent config.
* For structured outputs, validate your per-call outputSchema. QodoClient validates and will throw if invalid.
