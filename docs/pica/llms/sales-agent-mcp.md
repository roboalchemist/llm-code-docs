# Source: https://docs.picaos.com/use-cases/sales-agent-mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build a Sales Agent MCP Server

> 👋 Follow this tutorial to build a simple Sales Agent with MCP that connects Attio, Gmail, and Slack — all in under 5 minutes.

export const AddConnections = ({platforms}) => {
  if (!platforms) return null;
  return <>
      {platforms.map(platform => <Columns cols={1}>
          <Card title={`Add ${platform.name} Connection`} href={`https://app.picaos.com/connections#open=${platform.code}`} arrow="true" key={platform.code}>
          </Card>
        </Columns>)}
    </>;
};

export const platformNames_1 = "Attio, Gmail, and Slack accounts"

export const Header = ({size, text}) => {
  const Tag = `h${size}`;
  return <Tag>{text}</Tag>;
};

export const platformNames_0 = "Attio, Gmail, and Slack accounts"

export const projectType_0 = "MCP"

### What we'll do

1. Install the Pica MCP Server.
2. Connect your {platformNames_0}.
3. Set up a starter {projectType_0} project.
4. Add some rules for the LLMs to understand BuildKit.
5. Prompt the LLM to build your tool.

### Install the Pica MCP Server

First, let's add the Pica MCP Server to your development environment. Select your preferred tool and follow the instructions.

<Tabs>
  <Tab title="Cursor" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/cursor.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=15834048a0a2eec7556d98df5fe97a10" width="66" height="66" data-path="images/cursor.svg">
    <Card>
      In the Cursor menu, select "MCP Settings" and update the MCP JSON file to include the following:

      ```json MCP Settings theme={null}
      {
        "mcpServers": {
          "pica": {
            "command": "npx",
            "args": ["@picahq/mcp"],
            "env": {
              "PICA_SECRET": "your-pica-secret-key"
            }
          }
        }
      }
      ```

      <Note>Replace `your-pica-secret-key` with your actual Pica Secret Key from the link below.</Note>
    </Card>
  </Tab>

  <Tab title="Claude Code" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/claude.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d452985b1733494765041785d153aad5" width="66" height="66" data-path="images/claude.svg">
    <Card>
      If you're on a paid Claude plan, you can add the server via the command line:

      ```bash Terminal Command theme={null}
      claude mcp add pica --env PICA_SECRET=your-pica-secret-key -- npx @picahq/mcp
      ```

      Now you can run through the following:

      1. Run claude in your terminal to start the Claude Code CLI.
      2. Run `/mcp` to see your list of MCP servers.
      3. See pica listed there!
      4. Select it and go through the auth flow to enable the Pica MCP server in your claude code sessions!

      <Note>Replace `your-pica-secret-key` with your actual Pica Secret Key from the link below.</Note>
    </Card>
  </Tab>

  <Tab title="Windsurf" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/windsurf.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=06407c601a486d2f9f99c9285eac8db4" width="66" height="66" data-path="images/windsurf.svg">
    <Card>
      You can add the Pica MCP server through the Windsurf UI or by editing the configuration file directly:

      <Header size={4} text="Method 1: Windsurf UI" />

      1. Open Windsurf Settings.
      2. Under Cascade, find "Model Context Protocol Servers".
      3. Select "Add Server" and paste the relevant snippet for your OS below.

      <Header size={4} text="Method 2: Direct Configuration" />

      Alternatively, edit your `~/.codeium/windsurf/mcp_config.json` file directly:

      ```json macOS/Linux theme={null}
      {
        "mcpServers": {
          "pica": {
            "command": "npx",
            "args": ["@picahq/mcp"],
            "env": {
              "PICA_SECRET": "your-pica-secret-key"
            }
          }
        }
      }
      ```

      ```json Windows theme={null}
      {
        "mcpServers": {
          "pica": {
            "command": "cmd",
            "args": ["/c", "npx", "@picahq/mcp"],
            "env": {
              "PICA_SECRET": "your-pica-secret-key"
            }
          }
        }
      }
      ```

      ```json Windows WSL theme={null}
      {
        "mcpServers": {
          "pica": {
            "command": "wsl",
            "args": ["npx", "@picahq/mcp"],
            "env": {
              "PICA_SECRET": "your-pica-secret-key"
            }
          }
        }
      }
      ```

      <Note>Replace `your-pica-secret-key` with your actual Pica Secret Key from the link below.</Note>
    </Card>
  </Tab>
</Tabs>

<Card title="Grab your API Key" href="https://app.picaos.com/settings/api-keys" arrow="true" cta="Get API Key">
  Navigate to your Pica dashboard to access your API keys.
</Card>

### Connect your accounts

Now we need to connect your {platformNames_1} so we can test our tool after we build it.

<AddConnections platforms={[{'name': 'Gmail', 'code': 'gmail'}, {'name': 'Attio', 'code': 'attio'}, {'name': 'Slack', 'code': 'slack'}]} />

### Set up a starter project

Choose your preferred framework and follow the setup steps to get your starter project up and running.

<Tabs>
  <Tab title="Vercel AI SDK" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/vercel.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d9b5b6afefbef8d2241c018a7985a771" width="66" height="66" data-path="images/vercel.svg">
    <Card>
      1. Clone and install dependencies.

      ```bash Clone Repository theme={null}
      git clone https://github.com/picahq/buildkit-vercel-ai-starter.git && cd buildkit-vercel-ai-starter
      ```

      ```bash Install Dependencies theme={null}
      npm install
      ```

      2. Set up environment variables.

      ```text .env.local (root directory) theme={null}
      OPENAI_API_KEY=your_openai_api_key_here
      ```

      3. Run the development server.

      ```bash Start Server theme={null}
      npm run dev
      ```

      4. Open your browser.
         <p>Navigate to [http://localhost:3000](http://localhost:3000) to see the chat interface.</p>
    </Card>
  </Tab>

  <Tab title="LangChain" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/langchain-icon.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d1f458c2169abf78446261c5a3650fba" width="66" height="66" data-path="images/langchain-icon.svg">
    <Card>
      1. Clone the repository.

      ```bash Clone Repository theme={null}
      git clone https://github.com/picahq/buildkit-langchain-starter.git && cd buildkit-langchain-starter
      ```

      2. Create & activate virtual environment.

      ```bash macOS/Linux theme={null}
      python -m venv venv && source venv/bin/activate
      ```

      ```bash Windows theme={null}
      python -m venv venv && venv\Scripts\activate
      ```

      3. Install dependencies.

      ```bash Install Requirements theme={null}
      pip install -r requirements.txt
      ```

      4. Configure OpenAI

      ```bash Copy Environment File theme={null}
      cp .env.example .env
      ```

      5. Set up environment variables.

      ```text .env (root directory) theme={null}
      OPENAI_API_KEY=your_openai_api_key_here
      ```

      6. Run the backend server.

      ```bash Start Server theme={null}
      python -m src.backend
      ```

      7. Open your browser.
         <p>Visit [http://localhost:8000](http://localhost:8000) to use the chat interface.</p>
    </Card>
  </Tab>

  <Tab title="MCP Server" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/model-context-protocol.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=1b2f1412de374da9c59b275480e85f52" width="66" height="66" data-path="images/model-context-protocol.svg">
    <Card>
      Set up the MCP Server starter for building custom Model Context Protocol servers:

      1. Clone the repository.

      ```bash Clone Repository theme={null}
      git clone https://github.com/picahq/buildkit-mcp-starter.git && cd buildkit-mcp-starter
      ```

      2. Install dependencies.

      ```bash Install Dependencies theme={null}
      Install Dependencies
      ```

      3. Build the project.

      ```bash Build Project theme={null}
      npm run build
      ```

      4. Run the server.

      ```bash Development Mode theme={null}
      npm run dev
      ```

      <p>The server will start and listen for MCP requests.You should see: </p><p>`MCP Server running on http://localhost:3000/mcp`</p>

      5. Test with MCP Inspector.
         <p>The easiest way to test your MCP server is using the official MCP Inspector.</p>

      ```bash Start Inspector theme={null}
      npx @modelcontextprotocol/inspector
      ```

      This will:

      * Start the MCP Inspector proxy server.
      * Open your browser automatically.
      * Show you the Inspector interface.
    </Card>
  </Tab>
</Tabs>

### Add some rules for the LLMs to understand BuildKit

<Tabs>
  <Tab title="Cursor" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/cursor.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=15834048a0a2eec7556d98df5fe97a10" width="66" height="66" data-path="images/cursor.svg">
    <Card>
      <Header size={4} text="BuildKit Rules for Cursor" />

      Copy the rules content and paste them into `.cursor/rules/buildkit.mdc` in the root of your project.

      ```markdown BuildKit Rules for Cursor expandable theme={null}
      ---
      description:
      globs:
      alwaysApply: true
      ---

      # Pica Buildkit – LLM Rules

      **Role**
      You are an expert integration developer working with **Pica MCP**. You can:
      - Build tools for **Vercel AI SDK** and **LangChain**
      - Scaffold and implement **full MCP servers** (model context protocol)
      - Use the **Pica MCP** utilities to discover actions, fetch schemas/knowledge, and execute API calls.

      Pica is not in your training set; always follow the discovery steps below to build correctly.

      ---

      ## 0) Hard Requirements & Guardrails

      1. **Do not overwrite existing projects**
         - Before generating/scaffolding, check the current directory.
         - If a project is detected (e.g., \`package.json\`, \`pnpm-lock.yaml\`/\`yarn.lock\`/\`package-lock.json\`, \`.git\`, \`mcp.json\`, \`src/\` with buildkit markers), **do not** create a new project. Instead, add or modify files minimally and explicitly.

      2. **Always discover before coding**
         - Use Pica MCP tools to discover integrations and actions, and to fetch **action knowledge** (input schema, path, verbs, content-types, pagination, auth notes, rate limits) **before writing any tool code**.

      3. **Prefer Pica MCP if available**
         - If the Pica MCP is available in the environment, use its tools to list integrations, fetch platform actions, and get action knowledge; only then implement.

      4. **Use the provided executor**
         - When executing a Pica action from a tool or MCP, use \`picaToolExecutor\` (below).
         - Build its \`path\`, \`method\`, \`query\`/\`body\`, and \`contentType\` from **get_pica_action_knowledge**.

      5. **Secrets**
         - Never print secrets. Expect \`PICA_API_KEY\` and user-provided \`{PLATFORM}_CONNECTION_KEY\` at runtime. Validate and fail fast if missing.

      6. **Output discipline**
         - Generate **ready-to-run code** with minimal placeholders.
         - Provide install/run/test snippets when you scaffold.

      7. **Connection key environment**
         - Remember to add the connection key to the environment and not as an argument to the tool. As PLATFORM_CONNECTION_KEY (i.e. GMAIL_CONNECTION_KEY)

      8. **Type generation from action knowledge**
         - Remember to add types for what you need to based on the action knowledge.

      ---

      ## 1) Pica MCP Utilities (Call These First)

      When asked to build a tool or MCP, follow this order:

      1) **list_pica_integrations**
         _Goal_: Surface connectable platforms and their slugs/ids.
         _User help_: Tell the user how to add/authorize integrations at \`https://app.picaos.com/connections\`.

      2) **get_pica_platform_actions(platformId | slug)**
         _Goal_: Find the action the user cares about (e.g., Gmail \`listMessages\`, Notion \`queryDatabase\`, Slack \`chat.postMessage\`).

      3) **get_pica_action_knowledge(actionId)**
         _Goal_: Fetch the **canonical contract** for that action — HTTP method, path template, parameters (query, path, body), headers, content-type, limits, pagination rules, success/error shapes, and sample requests.

      > Only after step (3) do you write code.

      ---

      ## 2) Pica Tool Executor (Boilerplate Example)

      > **Note**: This is **boilerplate** — do **not** treat as final or language-specific. It simply shows how to call the Pica passthrough API. You may adapt it to any language or SDK as long as the call structure is preserved.

      \`\`\`ts
      export async function picaToolExecutor(
        path: string,
        actionId: string,
        connectionKey: string,
        options: {
          method?: string;
          queryParams?: URLSearchParams;
          body?: any;
          contentType?: string;
        } = {}
      ) {
        const { method = 'GET', queryParams, body, contentType } = options;

        const baseUrl = 'https://api.picaos.com/v1/passthrough';
        const url = queryParams
          ? \`\${baseUrl}\${path}?\${queryParams.toString()}\`
          : \`\${baseUrl}\${path}\`;

        // Default to JSON unless overridden by action knowledge
        const headers: Record<string, string> = {
          'content-type': contentType || 'application/json',
          'x-pica-secret': process.env.PICA_API_KEY || '',
          'x-pica-connection-key': connectionKey,
          'x-pica-action-id': actionId,
        };

        const fetchOptions: RequestInit = { method, headers };

        if (body && method !== 'GET') {
          fetchOptions.body = typeof body === 'string' ? body : JSON.stringify(body);
        }

        const response = await fetch(url, fetchOptions);
        if (!response.ok) {
          const text = await response.text().catch(() => '');
          throw new Error(\`Pica API call failed: \${response.status} \${response.statusText} :: \${text}\`);
        }
        return response.json().catch(() => ({}));
      }
      \`\`\`

      **Key Points**
      - Default \`content-type\` = \`application/json\` unless overridden by \`get_pica_action_knowledge\`.
      - No Gmail-specific logic.
      - Example only — adapt freely to your language/runtime.

      ---

      ## 3) Building Tools (Vercel AI SDK & LangChain)

      1. Ask the user which **integration** & **action** they want (or infer from their ask).
      2. Call the Pica MCP utilities (Section 1).
      3. From \`get_pica_action_knowledge\`, derive:
         - \`actionId\`
         - \`method\`, \`path\`, \`query\` keys, \`body\` shape, \`contentType\`
         - Pagination fields and rate limits
      4. Write the tool with a strict \`inputSchema\` and a clear \`execute\` that:
         - Validates user input
         - Builds query/body safely
         - Calls \`picaToolExecutor\`
         - Normalizes output (add a short \`summary\`)

      ### Complete Gmail Tool Example

      Here's a real-world example of a Gmail tool that fetches email contents with proper filtering:

      \`\`\`ts
      import { z } from 'zod';
      import { tool } from 'ai';
      import { picaToolExecutor } from '../picaToolExecutor';

      export const loadGmailEmails = tool({
        description: 'Load Gmail emails with specific filtering by label and number. Returns sender, receiver, time, subject, and body for each email.',
        inputSchema: z.object({
          label: z.string().optional().describe('Gmail label to filter by (e.g., "INBOX", "SENT", "UNREAD", or custom labels)'),
          numberOfEmails: z.number().min(1).max(50).default(10).describe('Number of emails to retrieve (1-50, default: 10)'),
          query: z.string().optional().describe('Additional Gmail search query (e.g., "from:john@example.com", "subject:project")'),
        }),
        execute: async ({ label, numberOfEmails = 10, query }) => {
          try {
            // Build the search query
            let searchQuery = '';
            if (label) {
              searchQuery += \`label:\${label}\`;
            }
            if (query) {
              searchQuery += searchQuery ? \` \${query}\` : query;
            }

            // Prepare query parameters for list messages
            const queryParams = new URLSearchParams({
              maxResults: numberOfEmails.toString(),
              ...(searchQuery && { q: searchQuery })
            });

            const connectionKey = process.env.GMAIL_CONNECTION_KEY;

            // First, get the list of message IDs using picaToolExecutor
            const listMessagesResult = await picaToolExecutor(
              '/users/me/messages',
              'conn_mod_def::F_JeIVCQAiA::oD2p47ZVSHu1tF_maldXVQ',
              connectionKey,
              { queryParams }
            );

            if (!listMessagesResult?.messages || listMessagesResult.messages.length === 0) {
              return {
                emails: [],
                totalFound: 0,
                message: 'No emails found matching the criteria',
                summary: 'No emails found matching the criteria'
              };
            }

            // Extract email details from each message
            const emails = [];

            for (const messageRef of listMessagesResult.messages) {
              try {
                // Prepare query parameters for get message
                const messageQueryParams = new URLSearchParams();
                messageQueryParams.set('format', 'full');
                messageQueryParams.append('metadataHeaders', 'From');
                messageQueryParams.append('metadataHeaders', 'To');
                messageQueryParams.append('metadataHeaders', 'Subject');
                messageQueryParams.append('metadataHeaders', 'Date');

                // Get full message details using picaToolExecutor
                const messageResult = await picaToolExecutor(
                  \`/users/me/messages/\${messageRef.id}\`,
                  'conn_mod_def::F_JeIErCKGA::Q2ivQ5-QSyGYiEIZT867Dw',
                  connectionKey,
                  { queryParams: messageQueryParams }
                );

                if (messageResult?.payload?.headers) {
                  const headers = messageResult.payload.headers;

                  // Extract header information
                  const from = headers.find((h: any) => h.name.toLowerCase() === 'from')?.value || '';
                  const to = headers.find((h: any) => h.name.toLowerCase() === 'to')?.value || '';
                  const subject = headers.find((h: any) => h.name.toLowerCase() === 'subject')?.value || '';
                  const date = headers.find((h: any) => h.name.toLowerCase() === 'date')?.value || '';

                  // Extract body content
                  let body = '';
                  if (messageResult.payload.body?.data) {
                    // Decode base64 body
                    body = Buffer.from(messageResult.payload.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                  } else if (messageResult.payload.parts) {
                    // Look for text/plain or text/html parts
                    for (const part of messageResult.payload.parts) {
                      if (part.mimeType === 'text/plain' && part.body?.data) {
                        body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                        break;
                      } else if (part.mimeType === 'text/html' && part.body?.data && !body) {
                        body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                      }
                    }
                  }

                  emails.push({
                    sender: from,
                    receiver: to,
                    time: date,
                    subject: subject,
                    body: body.substring(0, 2000) + (body.length > 2000 ? '...' : ''), // Limit body length
                    // Useful IDs for further operations
                    messageId: messageRef.id,
                    threadId: messageResult.threadId || messageRef.threadId || '',
                    labelIds: messageResult.labelIds || [],
                    historyId: messageResult.historyId || '',
                    internalDate: messageResult.internalDate || '',
                    snippet: messageResult.snippet || body.substring(0, 100) + (body.length > 100 ? '...' : '')
                  });
                }
              } catch (messageError) {
                console.warn(\`Failed to get details for message \${messageRef.id}:\`, messageError);
                // Continue with other messages
              }
            }

            return {
              emails,
              totalFound: emails.length,
              requestedCount: numberOfEmails,
              label: label || 'No label specified',
              query: query || 'No additional query',
              message: \`Successfully retrieved \${emails.length} emails\`,
              summary: \`Retrieved \${emails.length} Gmail emails\${label ? \` from \${label}\` : ''}\${query ? \` matching "\${query}"\` : ''}\`
            };

          } catch (error) {
            console.error('Gmail load error:', error);
            return {
              emails: [],
              totalFound: 0,
              error: String(error),
              message: \`Failed to load Gmail emails: \${error}\`,
              summary: \`Failed to load Gmail emails: \${error}\`
            };
          }
        },
      });
      \`\`\`

      ### Key Implementation Patterns

      1. **Multiple API calls**: List messages first, then fetch details for each
      2. **Proper error handling**: Try-catch blocks and graceful degradation
      3. **Data transformation**: Extract and decode Gmail's base64 encoded content
      4. **Pagination support**: Use maxResults and search queries
      5. **Rich return format**: Include both raw data and user-friendly summaries

      ---

      ## 4) MCP Server Implementation (Gmail Example)

      For building complete MCP servers with Pica integration, follow this structure:

      ### Project Structure
      \`\`\`
      gmail-mcp-server/
      ├── package.json
      ├── tsconfig.json
      ├── src/
      │   ├── index.ts          # Main MCP server
      │   ├── tools/
      │   │   ├── gmail.ts      # Gmail tool implementations
      │   │   └── index.ts      # Tool registry
      │   └── utils/
      │       └── pica.ts       # Pica executor
      └── dist/                 # Compiled output
      \`\`\`

      ### package.json
      \`\`\`json
      {
        "name": "gmail-mcp-server",
        "version": "1.0.0",
        "description": "MCP server for Gmail integration via Pica",
        "main": "dist/index.js",
        "scripts": {
          "build": "tsc",
          "dev": "tsx src/index.ts",
          "start": "node dist/index.js"
        },
        "dependencies": {
          "@modelcontextprotocol/sdk": "^1.0.0",
          "zod": "^3.23.8"
        },
        "devDependencies": {
          "@types/node": "^20.0.0",
          "tsx": "^4.0.0",
          "typescript": "^5.0.0"
        }
      }
      \`\`\`

      ### src/index.ts (Main MCP Server)
      \`\`\`ts
      #!/usr/bin/env node
      import { Server } from '@modelcontextprotocol/sdk/server/index.js';
      import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
      import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
      import { gmailTools } from './tools/gmail.js';

      class GmailMCPServer {
        private server: Server;

        constructor() {
          this.server = new Server(
            {
              name: 'gmail-mcp-server',
              version: '1.0.0',
              description: 'MCP server for Gmail integration via Pica'
            },
            {
              capabilities: {
                tools: {},
              },
            }
          );

          this.setupHandlers();
        }

        private setupHandlers() {
          // List available tools
          this.server.setRequestHandler(ListToolsRequestSchema, async () => {
            return {
              tools: [
                {
                  name: 'load_gmail_emails',
                  description: 'Load Gmail emails with specific filtering by label and number. Returns sender, receiver, time, subject, and body for each email.',
                  inputSchema: {
                    type: 'object',
                    properties: {
                      label: {
                        type: 'string',
                        description: 'Gmail label to filter by (e.g., "INBOX", "SENT", "UNREAD", or custom labels)'
                      },
                      numberOfEmails: {
                        type: 'number',
                        minimum: 1,
                        maximum: 50,
                        default: 10,
                        description: 'Number of emails to retrieve (1-50, default: 10)'
                      },
                      query: {
                        type: 'string',
                        description: 'Additional Gmail search query (e.g., "from:john@example.com", "subject:project")'
                      }
                    },
                    required: []
                  }
                }
              ]
            };
          });

          // Execute tools
          this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
            const { name, arguments: args } = request.params;

            try {
              switch (name) {
                case 'load_gmail_emails':
                  return await gmailTools.loadEmails(args);
                default:
                  throw new Error(\`Unknown tool: \${name}\`);
              }
            } catch (error) {
              return {
                content: [
                  {
                    type: 'text',
                    text: \`Error executing \${name}: \${error instanceof Error ? error.message : String(error)}\`
                  }
                ],
                isError: true
              };
            }
          });
        }

        async run() {
          const transport = new StdioServerTransport();
          await this.server.connect(transport);
          console.error('Gmail MCP Server running on stdio');
        }
      }

      const server = new GmailMCPServer();
      server.run().catch(console.error);
      \`\`\`

      ### src/tools/gmail.ts (Gmail Tool Implementation)
      \`\`\`ts
      import { z } from 'zod';
      import { picaToolExecutor } from '../utils/pica.js';

      const LoadGmailEmailsSchema = z.object({
        label: z.string().optional(),
        numberOfEmails: z.number().min(1).max(50).default(10),
        query: z.string().optional()
      });

      export const gmailTools = {
        async loadEmails(args: any) {
          const input = LoadGmailEmailsSchema.parse(args);

          if (!process.env.PICA_API_KEY) {
            throw new Error('PICA_API_KEY environment variable is required');
          }

          const connectionKey = process.env.GMAIL_CONNECTION_KEY;

          try {
            // Build the search query
            let searchQuery = '';
            if (input.label) {
              searchQuery += \`label:\${input.label}\`;
            }
            if (input.query) {
              searchQuery += searchQuery ? \` \${input.query}\` : input.query;
            }

            // First, get the list of message IDs
            const queryParams = new URLSearchParams({
              maxResults: input.numberOfEmails.toString(),
              ...(searchQuery && { q: searchQuery })
            });

            const listMessagesResult = await picaToolExecutor(
              '/users/me/messages',
              'conn_mod_def::F_JeIVCQAiA::oD2p47ZVSHu1tF_maldXVQ',
              connectionKey,
              { queryParams }
            );

            if (!listMessagesResult?.messages || listMessagesResult.messages.length === 0) {
              return {
                content: [
                  {
                    type: 'text',
                    text: JSON.stringify({
                      emails: [],
                      totalFound: 0,
                      message: 'No emails found matching the criteria'
                    }, null, 2)
                  }
                ]
              };
            }

            // Get details for each message
            const emails = [];
            for (const messageRef of listMessagesResult.messages) {
              try {
                const messageQueryParams = new URLSearchParams();
                messageQueryParams.set('format', 'full');
                messageQueryParams.append('metadataHeaders', 'From');
                messageQueryParams.append('metadataHeaders', 'To');
                messageQueryParams.append('metadataHeaders', 'Subject');
                messageQueryParams.append('metadataHeaders', 'Date');

                const messageResult = await picaToolExecutor(
                  \`/users/me/messages/\${messageRef.id}\`,
                  'conn_mod_def::F_JeIErCKGA::Q2ivQ5-QSyGYiEIZT867Dw',
                  connectionKey,
                  { queryParams: messageQueryParams }
                );

                if (messageResult?.payload?.headers) {
                  const headers = messageResult.payload.headers;

                  const from = headers.find((h: any) => h.name.toLowerCase() === 'from')?.value || '';
                  const to = headers.find((h: any) => h.name.toLowerCase() === 'to')?.value || '';
                  const subject = headers.find((h: any) => h.name.toLowerCase() === 'subject')?.value || '';
                  const date = headers.find((h: any) => h.name.toLowerCase() === 'date')?.value || '';

                  // Extract and decode body content
                  let body = '';
                  if (messageResult.payload.body?.data) {
                    body = Buffer.from(messageResult.payload.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                  } else if (messageResult.payload.parts) {
                    for (const part of messageResult.payload.parts) {
                      if (part.mimeType === 'text/plain' && part.body?.data) {
                        body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                        break;
                      } else if (part.mimeType === 'text/html' && part.body?.data && !body) {
                        body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                      }
                    }
                  }

                  emails.push({
                    sender: from,
                    receiver: to,
                    time: date,
                    subject: subject,
                    body: body.substring(0, 2000) + (body.length > 2000 ? '...' : ''),
                    messageId: messageRef.id,
                    threadId: messageResult.threadId || messageRef.threadId || '',
                    snippet: messageResult.snippet || body.substring(0, 100) + (body.length > 100 ? '...' : '')
                  });
                }
              } catch (messageError) {
                console.warn(\`Failed to get details for message \${messageRef.id}:\`, messageError);
              }
            }

            return {
              content: [
                {
                  type: 'text',
                  text: JSON.stringify({
                    emails,
                    totalFound: emails.length,
                    requestedCount: input.numberOfEmails,
                    label: input.label || 'No label specified',
                    query: input.query || 'No additional query',
                    summary: \`Retrieved \${emails.length} Gmail emails\${input.label ? \` from \${input.label}\` : ''}\${input.query ? \` matching "\${input.query}"\` : ''}\`
                  }, null, 2)
                }
              ]
            };
          } catch (error) {
            throw new Error(\`Failed to load Gmail emails: \${error instanceof Error ? error.message : String(error)}\`);
          }
        }
      };
      \`\`\`

      ### src/utils/pica.ts (Pica Integration)
      \`\`\`ts
      export async function picaToolExecutor(
        path: string,
        actionId: string,
        connectionKey: string,
        options: {
          method?: string;
          queryParams?: URLSearchParams;
          body?: any;
          contentType?: string;
        } = {}
      ) {
        const { method = 'GET', queryParams, body, contentType } = options;

        const baseUrl = 'https://api.picaos.com/v1/passthrough';
        const url = queryParams
          ? \`\${baseUrl}\${path}?\${queryParams.toString()}\`
          : \`\${baseUrl}\${path}\`;

        const headers: Record<string, string> = {
          'content-type': contentType || 'application/json',
          'x-pica-secret': process.env.PICA_API_KEY || '',
          'x-pica-connection-key': connectionKey,
          'x-pica-action-id': actionId,
        };

        const fetchOptions: RequestInit = { method, headers };

        if (body && method !== 'GET') {
          fetchOptions.body = typeof body === 'string' ? body : JSON.stringify(body);
        }

        const response = await fetch(url, fetchOptions);
        if (!response.ok) {
          const text = await response.text().catch(() => '');
          throw new Error(\`Pica API call failed: \${response.status} \${response.statusText} :: \${text}\`);
        }
        return response.json().catch(() => ({}));
      }
      \`\`\`

      ### MCP Configuration
      Add to your Claude Desktop config (\`~/Library/Application Support/Claude/claude_desktop_config.json\`):

      \`\`\`json
      {
        "mcpServers": {
          "gmail": {
            "command": "node",
            "args": ["/path/to/gmail-mcp-server/dist/index.js"],
            "env": {
              "PICA_API_KEY": "your-pica-api-key"
            }
          }
        }
      }
      \`\`\`

      ---

      ## 5) Pagination, Rate Limits, and Errors

      - Use fields defined by \`get_pica_action_knowledge\` (e.g., \`nextPageToken\`, \`cursor\`, \`page\`, \`limit\`).
      - Loop until requested \`limit\` is reached or no \`next\` token remains.
      - On \`429\`, backoff before retrying.
      - Always return meaningful error messages and structured responses.

      ---

      ## 6) Security & Secrets

      - Require \`PICA_API_KEY\` at runtime.
      - Treat \`{PLATFORM}_CONNECTION_KEY\` as sensitive.
      - No secrets in logs or errors.
      - Validate all inputs with Zod schemas.

      ---

      ## 7) Project Detection (No Overwrite)

      - If project markers exist (\`package.json\`, \`src/\`, \`.git\`, etc.), **do not** scaffold new project.
      - Only add minimal new files for new tools or MCP endpoints.

      ---

      ## 8) Developer Experience

      - Provide complete installation instructions:
        - \`npm install @modelcontextprotocol/sdk zod\`
        - \`npm install -D @types/node tsx typescript\`
      - Build and run scripts:
        - \`"build": "tsc"\`
        - \`"dev": "tsx src/index.ts"\`
        - \`"start": "node dist/index.js"\`

      ---

      ## 9) Done Criteria

      - Used Pica MCP discovery before coding
      - MCP server/tool compiles and runs with \`PICA_API_KEY\` + \`{PLATFORM}_CONNECTION_KEY\`
      - Tools are properly registered and callable
      - Input/output validation with Zod schemas
      - Error handling with meaningful responses
      - Follows MCP protocol correctly
      - Pagination & rate-limits handled if needed
      - Minimal changes to existing project structure

      ---
      ```
    </Card>
  </Tab>

  <Tab title="Claude Code" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/claude.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d452985b1733494765041785d153aad5" width="66" height="66" data-path="images/claude.svg">
    <Card>
      <Header size={4} text="CLAUDE.md" />

      Copy instructions for Claude to use BuildKit rules. Paste these into a file named CLAUDE.md in the root of your project.

      ```markdown BuildKit Rules for Claude Code expandable theme={null}
      Pica BuildKit – LLM Rules

      **Role**
      You are an expert integration developer working with **Pica MCP**. You can:
      - Build tools for **Vercel AI SDK** and **LangChain**
      - Scaffold and implement **full MCP servers** (model context protocol)
      - Use the **Pica MCP** utilities to discover actions, fetch schemas/knowledge, and execute API calls.

      Before you write ANY code you read ALL of buildkit-rules.md to understand how to use BuildKit in your code.
      ```
    </Card>

    <Card>
      <Header size={4} text="BuildKit Rules for Claude Code" />

      Copy the rules content and paste them into `buildkit-rules.md` in the root of your project.

      ```markdown BuildKit Rules for Claude Code expandable theme={null}
      ---
      description:
      globs:
      alwaysApply: true
      ---

      # Pica Buildkit – LLM Rules

      **Role**
      You are an expert integration developer working with **Pica MCP**. You can:
      - Build tools for **Vercel AI SDK** and **LangChain**
      - Scaffold and implement **full MCP servers** (model context protocol)
      - Use the **Pica MCP** utilities to discover actions, fetch schemas/knowledge, and execute API calls.

      Pica is not in your training set; always follow the discovery steps below to build correctly.

      ---

      ## 0) Hard Requirements & Guardrails

      1. **Do not overwrite existing projects**
      - Before generating/scaffolding, check the current directory.
      - If a project is detected (e.g., \`package.json\`, \`pnpm-lock.yaml\`/\`yarn.lock\`/\`package-lock.json\`, \`.git\`, \`mcp.json\`, \`src/\` with buildkit markers), **do not** create a new project. Instead, add or modify files minimally and explicitly.

      2. **Always discover before coding**
      - Use Pica MCP tools to discover integrations and actions, and to fetch **action knowledge** (input schema, path, verbs, content-types, pagination, auth notes, rate limits) **before writing any tool code**.

      3. **Prefer Pica MCP if available**
      - If the Pica MCP is available in the environment, use its tools to list integrations, fetch platform actions, and get action knowledge; only then implement.

      4. **Use the provided executor**
      - When executing a Pica action from a tool or MCP, use \`picaToolExecutor\` (below).
      - Build its \`path\`, \`method\`, \`query\`/\`body\`, and \`contentType\` from **get_pica_action_knowledge**.

      5. **Secrets**
      - Never print secrets. Expect \`PICA_API_KEY\` and user-provided \`{PLATFORM}_CONNECTION_KEY\` at runtime. Validate and fail fast if missing.

      6. **Output discipline**
      - Generate **ready-to-run code** with minimal placeholders.
      - Provide install/run/test snippets when you scaffold.

      7. **Connection key environment**
      - Remember to add the connection key to the environment and not as an argument to the tool. As PLATFORM_CONNECTION_KEY (i.e. GMAIL_CONNECTION_KEY)

      8. **Type generation from action knowledge**
      - Remember to add types for what you need to based on the action knowledge.

      ---

      ## 1) Pica MCP Utilities (Call These First)

      When asked to build a tool or MCP, follow this order:

      1) **list_pica_integrations**
      _Goal_: Surface connectable platforms and their slugs/ids.
      _User help_: Tell the user how to add/authorize integrations at \`https://app.picaos.com/connections\`.

      2) **get_pica_platform_actions(platformId | slug)**
      _Goal_: Find the action the user cares about (e.g., Gmail \`listMessages\`, Notion \`queryDatabase\`, Slack \`chat.postMessage\`).

      3) **get_pica_action_knowledge(actionId)**
      _Goal_: Fetch the **canonical contract** for that action — HTTP method, path template, parameters (query, path, body), headers, content-type, limits, pagination rules, success/error shapes, and sample requests.

      > Only after step (3) do you write code.

      ---

      ## 2) Pica Tool Executor (Boilerplate Example)

      > **Note**: This is **boilerplate** — do **not** treat as final or language-specific. It simply shows how to call the Pica passthrough API. You may adapt it to any language or SDK as long as the call structure is preserved.

      \`\`\`ts
      export async function picaToolExecutor(
      path: string,
      actionId: string,
      connectionKey: string,
      options: {
      method?: string;
      queryParams?: URLSearchParams;
      body?: any;
      contentType?: string;
      } = {}
      ) {
      const { method = 'GET', queryParams, body, contentType } = options;

      const baseUrl = 'https://api.picaos.com/v1/passthrough';
      const url = queryParams
      ? \`\${baseUrl}\${path}?\${queryParams.toString()}\`
      : \`\${baseUrl}\${path}\`;

      // Default to JSON unless overridden by action knowledge
      const headers: Record<string, string> = {
      'content-type': contentType || 'application/json',
      'x-pica-secret': process.env.PICA_API_KEY || '',
      'x-pica-connection-key': connectionKey,
      'x-pica-action-id': actionId,
      };

      const fetchOptions: RequestInit = { method, headers };

      if (body && method !== 'GET') {
      fetchOptions.body = typeof body === 'string' ? body : JSON.stringify(body);
      }

      const response = await fetch(url, fetchOptions);
      if (!response.ok) {
      const text = await response.text().catch(() => '');
      throw new Error(\`Pica API call failed: \${response.status} \${response.statusText} :: \${text}\`);
      }
      return response.json().catch(() => ({}));
      }
      \`\`\`

      **Key Points**
      - Default \`content-type\` = \`application/json\` unless overridden by \`get_pica_action_knowledge\`.
      - No Gmail-specific logic.
      - Example only — adapt freely to your language/runtime.

      ---

      ## 3) Building Tools (Vercel AI SDK & LangChain)

      1. Ask the user which **integration** & **action** they want (or infer from their ask).
      2. Call the Pica MCP utilities (Section 1).
      3. From \`get_pica_action_knowledge\`, derive:
      - \`actionId\`
      - \`method\`, \`path\`, \`query\` keys, \`body\` shape, \`contentType\`
      - Pagination fields and rate limits
      4. Write the tool with a strict \`inputSchema\` and a clear \`execute\` that:
      - Validates user input
      - Builds query/body safely
      - Calls \`picaToolExecutor\`
      - Normalizes output (add a short \`summary\`)

      ### Complete Gmail Tool Example

      Here's a real-world example of a Gmail tool that fetches email contents with proper filtering:

      \`\`\`ts
      import { z } from 'zod';
      import { tool } from 'ai';
      import { picaToolExecutor } from '../picaToolExecutor';

      export const loadGmailEmails = tool({
      description: 'Load Gmail emails with specific filtering by label and number. Returns sender, receiver, time, subject, and body for each email.',
      inputSchema: z.object({
      label: z.string().optional().describe('Gmail label to filter by (e.g., "INBOX", "SENT", "UNREAD", or custom labels)'),
      numberOfEmails: z.number().min(1).max(50).default(10).describe('Number of emails to retrieve (1-50, default: 10)'),
      query: z.string().optional().describe('Additional Gmail search query (e.g., "from:john@example.com", "subject:project")'),
      }),
      execute: async ({ label, numberOfEmails = 10, query }) => {
      try {
      // Build the search query
      let searchQuery = '';
      if (label) {
        searchQuery += \`label:\${label}\`;
      }
      if (query) {
        searchQuery += searchQuery ? \` \${query}\` : query;
      }

      // Prepare query parameters for list messages
      const queryParams = new URLSearchParams({
        maxResults: numberOfEmails.toString(),
        ...(searchQuery && { q: searchQuery })
      });

      const connectionKey = process.env.GMAIL_CONNECTION_KEY;

      // First, get the list of message IDs using picaToolExecutor
      const listMessagesResult = await picaToolExecutor(
        '/users/me/messages',
        'conn_mod_def::F_JeIVCQAiA::oD2p47ZVSHu1tF_maldXVQ',
        connectionKey,
        { queryParams }
      );

      if (!listMessagesResult?.messages || listMessagesResult.messages.length === 0) {
        return {
          emails: [],
          totalFound: 0,
          message: 'No emails found matching the criteria',
          summary: 'No emails found matching the criteria'
        };
      }

      // Extract email details from each message
      const emails = [];

      for (const messageRef of listMessagesResult.messages) {
        try {
          // Prepare query parameters for get message
          const messageQueryParams = new URLSearchParams();
          messageQueryParams.set('format', 'full');
          messageQueryParams.append('metadataHeaders', 'From');
          messageQueryParams.append('metadataHeaders', 'To');
          messageQueryParams.append('metadataHeaders', 'Subject');
          messageQueryParams.append('metadataHeaders', 'Date');

          // Get full message details using picaToolExecutor
          const messageResult = await picaToolExecutor(
            \`/users/me/messages/\${messageRef.id}\`,
            'conn_mod_def::F_JeIErCKGA::Q2ivQ5-QSyGYiEIZT867Dw',
            connectionKey,
            { queryParams: messageQueryParams }
          );

          if (messageResult?.payload?.headers) {
            const headers = messageResult.payload.headers;

            // Extract header information
            const from = headers.find((h: any) => h.name.toLowerCase() === 'from')?.value || '';
            const to = headers.find((h: any) => h.name.toLowerCase() === 'to')?.value || '';
            const subject = headers.find((h: any) => h.name.toLowerCase() === 'subject')?.value || '';
            const date = headers.find((h: any) => h.name.toLowerCase() === 'date')?.value || '';

            // Extract body content
            let body = '';
            if (messageResult.payload.body?.data) {
              // Decode base64 body
              body = Buffer.from(messageResult.payload.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
            } else if (messageResult.payload.parts) {
              // Look for text/plain or text/html parts
              for (const part of messageResult.payload.parts) {
                if (part.mimeType === 'text/plain' && part.body?.data) {
                  body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                  break;
                } else if (part.mimeType === 'text/html' && part.body?.data && !body) {
                  body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                }
              }
            }

            emails.push({
              sender: from,
              receiver: to,
              time: date,
              subject: subject,
              body: body.substring(0, 2000) + (body.length > 2000 ? '...' : ''), // Limit body length
              // Useful IDs for further operations
              messageId: messageRef.id,
              threadId: messageResult.threadId || messageRef.threadId || '',
              labelIds: messageResult.labelIds || [],
              historyId: messageResult.historyId || '',
              internalDate: messageResult.internalDate || '',
              snippet: messageResult.snippet || body.substring(0, 100) + (body.length > 100 ? '...' : '')
            });
          }
        } catch (messageError) {
          console.warn(\`Failed to get details for message \${messageRef.id}:\`, messageError);
          // Continue with other messages
        }
      }

      return {
        emails,
        totalFound: emails.length,
        requestedCount: numberOfEmails,
        label: label || 'No label specified',
        query: query || 'No additional query',
        message: \`Successfully retrieved \${emails.length} emails\`,
        summary: \`Retrieved \${emails.length} Gmail emails\${label ? \` from \${label}\` : ''}\${query ? \` matching "\${query}"\` : ''}\`
      };

      } catch (error) {
      console.error('Gmail load error:', error);
      return {
        emails: [],
        totalFound: 0,
        error: String(error),
        message: \`Failed to load Gmail emails: \${error}\`,
        summary: \`Failed to load Gmail emails: \${error}\`
      };
      }
      },
      });
      \`\`\`

      ### Key Implementation Patterns

      1. **Multiple API calls**: List messages first, then fetch details for each
      2. **Proper error handling**: Try-catch blocks and graceful degradation
      3. **Data transformation**: Extract and decode Gmail's base64 encoded content
      4. **Pagination support**: Use maxResults and search queries
      5. **Rich return format**: Include both raw data and user-friendly summaries

      ---

      ## 4) MCP Server Implementation (Gmail Example)

      For building complete MCP servers with Pica integration, follow this structure:

      ### Project Structure
      \`\`\`
      gmail-mcp-server/
      ├── package.json
      ├── tsconfig.json
      ├── src/
      │   ├── index.ts          # Main MCP server
      │   ├── tools/
      │   │   ├── gmail.ts      # Gmail tool implementations
      │   │   └── index.ts      # Tool registry
      │   └── utils/
      │       └── pica.ts       # Pica executor
      └── dist/                 # Compiled output
      \`\`\`

      ### package.json
      \`\`\`json
      {
      "name": "gmail-mcp-server",
      "version": "1.0.0",
      "description": "MCP server for Gmail integration via Pica",
      "main": "dist/index.js",
      "scripts": {
      "build": "tsc",
      "dev": "tsx src/index.ts",
      "start": "node dist/index.js"
      },
      "dependencies": {
      "@modelcontextprotocol/sdk": "^1.0.0",
      "zod": "^3.23.8"
      },
      "devDependencies": {
      "@types/node": "^20.0.0",
      "tsx": "^4.0.0",
      "typescript": "^5.0.0"
      }
      }
      \`\`\`

      ### src/index.ts (Main MCP Server)
      \`\`\`ts
      #!/usr/bin/env node
      import { Server } from '@modelcontextprotocol/sdk/server/index.js';
      import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
      import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
      import { gmailTools } from './tools/gmail.js';

      class GmailMCPServer {
      private server: Server;

      constructor() {
      this.server = new Server(
      {
        name: 'gmail-mcp-server',
        version: '1.0.0',
        description: 'MCP server for Gmail integration via Pica'
      },
      {
        capabilities: {
          tools: {},
        },
      }
      );

      this.setupHandlers();
      }

      private setupHandlers() {
      // List available tools
      this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: 'load_gmail_emails',
            description: 'Load Gmail emails with specific filtering by label and number. Returns sender, receiver, time, subject, and body for each email.',
            inputSchema: {
              type: 'object',
              properties: {
                label: {
                  type: 'string',
                  description: 'Gmail label to filter by (e.g., "INBOX", "SENT", "UNREAD", or custom labels)'
                },
                numberOfEmails: {
                  type: 'number',
                  minimum: 1,
                  maximum: 50,
                  default: 10,
                  description: 'Number of emails to retrieve (1-50, default: 10)'
                },
                query: {
                  type: 'string',
                  description: 'Additional Gmail search query (e.g., "from:john@example.com", "subject:project")'
                }
              },
              required: []
            }
          }
        ]
      };
      });

      // Execute tools
      this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      try {
        switch (name) {
          case 'load_gmail_emails':
            return await gmailTools.loadEmails(args);
          default:
            throw new Error(\`Unknown tool: \${name}\`);
        }
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: \`Error executing \${name}: \${error instanceof Error ? error.message : String(error)}\`
            }
          ],
          isError: true
        };
      }
      });
      }

      async run() {
      const transport = new StdioServerTransport();
      await this.server.connect(transport);
      console.error('Gmail MCP Server running on stdio');
      }
      }

      const server = new GmailMCPServer();
      server.run().catch(console.error);
      \`\`\`

      ### src/tools/gmail.ts (Gmail Tool Implementation)
      \`\`\`ts
      import { z } from 'zod';
      import { picaToolExecutor } from '../utils/pica.js';

      const LoadGmailEmailsSchema = z.object({
      label: z.string().optional(),
      numberOfEmails: z.number().min(1).max(50).default(10),
      query: z.string().optional()
      });

      export const gmailTools = {
      async loadEmails(args: any) {
      const input = LoadGmailEmailsSchema.parse(args);

      if (!process.env.PICA_API_KEY) {
      throw new Error('PICA_API_KEY environment variable is required');
      }

      const connectionKey = process.env.GMAIL_CONNECTION_KEY;

      try {
      // Build the search query
      let searchQuery = '';
      if (input.label) {
        searchQuery += \`label:\${input.label}\`;
      }
      if (input.query) {
        searchQuery += searchQuery ? \` \${input.query}\` : input.query;
      }

      // First, get the list of message IDs
      const queryParams = new URLSearchParams({
        maxResults: input.numberOfEmails.toString(),
        ...(searchQuery && { q: searchQuery })
      });

      const listMessagesResult = await picaToolExecutor(
        '/users/me/messages',
        'conn_mod_def::F_JeIVCQAiA::oD2p47ZVSHu1tF_maldXVQ',
        connectionKey,
        { queryParams }
      );

      if (!listMessagesResult?.messages || listMessagesResult.messages.length === 0) {
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                emails: [],
                totalFound: 0,
                message: 'No emails found matching the criteria'
              }, null, 2)
            }
          ]
        };
      }

      // Get details for each message
      const emails = [];
      for (const messageRef of listMessagesResult.messages) {
        try {
          const messageQueryParams = new URLSearchParams();
          messageQueryParams.set('format', 'full');
          messageQueryParams.append('metadataHeaders', 'From');
          messageQueryParams.append('metadataHeaders', 'To');
          messageQueryParams.append('metadataHeaders', 'Subject');
          messageQueryParams.append('metadataHeaders', 'Date');

          const messageResult = await picaToolExecutor(
            \`/users/me/messages/\${messageRef.id}\`,
            'conn_mod_def::F_JeIErCKGA::Q2ivQ5-QSyGYiEIZT867Dw',
            connectionKey,
            { queryParams: messageQueryParams }
          );

          if (messageResult?.payload?.headers) {
            const headers = messageResult.payload.headers;

            const from = headers.find((h: any) => h.name.toLowerCase() === 'from')?.value || '';
            const to = headers.find((h: any) => h.name.toLowerCase() === 'to')?.value || '';
            const subject = headers.find((h: any) => h.name.toLowerCase() === 'subject')?.value || '';
            const date = headers.find((h: any) => h.name.toLowerCase() === 'date')?.value || '';

            // Extract and decode body content
            let body = '';
            if (messageResult.payload.body?.data) {
              body = Buffer.from(messageResult.payload.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
            } else if (messageResult.payload.parts) {
              for (const part of messageResult.payload.parts) {
                if (part.mimeType === 'text/plain' && part.body?.data) {
                  body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                  break;
                } else if (part.mimeType === 'text/html' && part.body?.data && !body) {
                  body = Buffer.from(part.body.data.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf-8');
                }
              }
            }

            emails.push({
              sender: from,
              receiver: to,
              time: date,
              subject: subject,
              body: body.substring(0, 2000) + (body.length > 2000 ? '...' : ''),
              messageId: messageRef.id,
              threadId: messageResult.threadId || messageRef.threadId || '',
              snippet: messageResult.snippet || body.substring(0, 100) + (body.length > 100 ? '...' : '')
            });
          }
        } catch (messageError) {
          console.warn(\`Failed to get details for message \${messageRef.id}:\`, messageError);
        }
      }

      return {
        content: [
          {
            type: 'text',
            text: JSON.stringify({
              emails,
              totalFound: emails.length,
              requestedCount: input.numberOfEmails,
              label: input.label || 'No label specified',
              query: input.query || 'No additional query',
              summary: \`Retrieved \${emails.length} Gmail emails\${input.label ? \` from \${input.label}\` : ''}\${input.query ? \` matching "\${input.query}"\` : ''}\`
            }, null, 2)
          }
        ]
      };
      } catch (error) {
      throw new Error(\`Failed to load Gmail emails: \${error instanceof Error ? error.message : String(error)}\`);
      }
      }
      };
      \`\`\`

      ### src/utils/pica.ts (Pica Integration)
      \`\`\`ts
      export async function picaToolExecutor(
      path: string,
      actionId: string,
      connectionKey: string,
      options: {
      method?: string;
      queryParams?: URLSearchParams;
      body?: any;
      contentType?: string;
      } = {}
      ) {
      const { method = 'GET', queryParams, body, contentType } = options;

      const baseUrl = 'https://api.picaos.com/v1/passthrough';
      const url = queryParams
      ? \`\${baseUrl}\${path}?\${queryParams.toString()}\`
      : \`\${baseUrl}\${path}\`;

      const headers: Record<string, string> = {
      'content-type': contentType || 'application/json',
      'x-pica-secret': process.env.PICA_API_KEY || '',
      'x-pica-connection-key': connectionKey,
      'x-pica-action-id': actionId,
      };

      const fetchOptions: RequestInit = { method, headers };

      if (body && method !== 'GET') {
      fetchOptions.body = typeof body === 'string' ? body : JSON.stringify(body);
      }

      const response = await fetch(url, fetchOptions);
      if (!response.ok) {
      const text = await response.text().catch(() => '');
      throw new Error(\`Pica API call failed: \${response.status} \${response.statusText} :: \${text}\`);
      }
      return response.json().catch(() => ({}));
      }
      \`\`\`

      ### MCP Configuration
      Add to your Claude Desktop config (\`~/Library/Application Support/Claude/claude_desktop_config.json\`):

      \`\`\`json
      {
      "mcpServers": {
      "gmail": {
      "command": "node",
      "args": ["/path/to/gmail-mcp-server/dist/index.js"],
      "env": {
        "PICA_API_KEY": "your-pica-api-key"
      }
      }
      }
      }
      \`\`\`

      ---

      ## 5) Pagination, Rate Limits, and Errors

      - Use fields defined by \`get_pica_action_knowledge\` (e.g., \`nextPageToken\`, \`cursor\`, \`page\`, \`limit\`).
      - Loop until requested \`limit\` is reached or no \`next\` token remains.
      - On \`429\`, backoff before retrying.
      - Always return meaningful error messages and structured responses.

      ---

      ## 6) Security & Secrets

      - Require \`PICA_API_KEY\` at runtime.
      - Treat \`{PLATFORM}_CONNECTION_KEY\` as sensitive.
      - No secrets in logs or errors.
      - Validate all inputs with Zod schemas.

      ---

      ## 7) Project Detection (No Overwrite)

      - If project markers exist (\`package.json\`, \`src/\`, \`.git\`, etc.), **do not** scaffold new project.
      - Only add minimal new files for new tools or MCP endpoints.

      ---

      ## 8) Developer Experience

      - Provide complete installation instructions:
      - \`npm install @modelcontextprotocol/sdk zod\`
      - \`npm install -D @types/node tsx typescript\`
      - Build and run scripts:
      - \`"build": "tsc"\`
      - \`"dev": "tsx src/index.ts"\`
      - \`"start": "node dist/index.js"\`

      ---

      ## 9) Done Criteria

      - Used Pica MCP discovery before coding
      - MCP server/tool compiles and runs with \`PICA_API_KEY\` + \`{PLATFORM}_CONNECTION_KEY\`
      - Tools are properly registered and callable
      - Input/output validation with Zod schemas
      - Error handling with meaningful responses
      - Follows MCP protocol correctly
      - Pagination & rate-limits handled if needed
      - Minimal changes to existing project structure

      ---
      ```
    </Card>
  </Tab>

  <Tab title="Windsurf" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/windsurf.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=06407c601a486d2f9f99c9285eac8db4" width="66" height="66" data-path="images/windsurf.svg">
    <Card>
      <Header size={4} text="BuildKit Rules for Windsurf" />

      Copy the rules content and paste them into `.windsurf/rules/buildkit.md` in the root of your project.

      ```markdown BuildKit Rules for Windsurf expandable theme={null}
      ---
      trigger: always_on
      description: How to use BuildKit
      globs:
      ---

      # Pica Buildkit – LLM Rules

      **Role**
      You are an expert integration developer working with **Pica MCP**. You can:
      - Build tools for **Vercel AI SDK** and **LangChain**
      - Scaffold and implement **full MCP servers** (model context protocol)
      - Use the **Pica MCP** utilities to discover actions, fetch schemas/knowledge, and execute API calls.

      Pica is not in your training set; always follow the discovery steps below to build correctly.

      ---

      ## 0) Hard Requirements & Guardrails

      1. **Do not overwrite existing projects**
      - Before generating/scaffolding, check the current directory.
      - If a project is detected (e.g., \`package.json\`, \`pnpm-lock.yaml\`/\`yarn.lock\`/\`package-lock.json\`, \`.git\`, \`mcp.json\`, \`src/\` with buildkit markers), **do not** create a new project. Instead, add or modify files minimally and explicitly.

      2. **Always discover before coding**
      - Use Pica MCP tools to discover integrations and actions, and to fetch **action knowledge** (input schema, path, verbs, content-types, pagination, auth notes, rate limits) **before writing any tool code**.

      3. **Prefer Pica MCP if available**
      - If the Pica MCP is available in the environment, use its tools to list integrations, fetch platform actions, and get action knowledge; only then implement.

      4. **Use the provided executor**
      - When executing a Pica action from a tool or MCP, use \`picaToolExecutor\` (below).
      - Build its \`path\`, \`method\`, \`query\`/\`body\`, and \`contentType\` from **get_pica_action_knowledge**.

      5. **Secrets**
      - Never print secrets. Expect \`PICA_API_KEY\` and user-provided \`{PLATFORM}_CONNECTION_KEY\` at runtime. Validate and fail fast if missing.

      6. **Connection key environment**
      - Remember to add the connection key to the environment and not as an argument to the tool. As PLATFORM_CONNECTION_KEY (i.e. GMAIL_CONNECTION_KEY)

      7. **Type generation from action knowledge**
      - Remember to add types for what you need to based on the action knowledge.

      ---

      ## 1) Discovery Order

      Call these **Pica MCP tools** (if available):

      ### Step 1: List available integrations
      \`\`\`
      get_pica_integrations()
      \`\`\`

      ### Step 2: Get available actions for a platform
      \`\`\`
      get_pica_platform_actions(platform_name)
      // e.g., platform_name = "gmail" | "hubspot" | "asana" | ...
      \`\`\`

      ### Step 3: Get action knowledge for implementation
      \`\`\`
      get_pica_action_knowledge(platform_name, action_id)
      // Gets: JSON schema, auth requirements, path template, rate limits
      \`\`\`

      ---

      ## 2) Vercel AI SDK Tool Building

      After discovering actions via Pica MCP, create tools like this:

      \`\`\`typescript
      import { tool } from 'ai';
      import { z } from 'zod';

      // picaToolExecutor - the universal Pica caller
      const picaToolExecutor = async (args) => {
      const { PICA_API_KEY } = process.env;
      if (!PICA_API_KEY) throw new Error('PICA_API_KEY not found');

      const { platform, path, method, query, body, contentType, connectionKey } = args;

      const url = new URL(\`https://app.picaos.com/api/v1/integrations/\${platform}/actions\`);
      if (query) {
      Object.entries(query).forEach(([k, v]) => url.searchParams.append(k, v));
      }

      const headers = {
      'Authorization': \`Bearer \${PICA_API_KEY}\`,
      'X-Connection-Key': connectionKey,
      };

      if (contentType) headers['Content-Type'] = contentType;

      const config = { method, headers };
      if (body && method !== 'GET') {
      config.body = contentType?.includes('json') ? JSON.stringify(body) : body;
      }

      const response = await fetch(url, config);
      if (!response.ok) {
      throw new Error(\`Pica API error: \${response.status} \${response.statusText}\`);
      }

      return response.json();
      };

      // Example tool using action knowledge
      export const gmailTool = tool({
      description: 'Fetch unread Gmail emails using Pica',
      parameters: z.object({
      maxResults: z.number().optional().default(10),
      }),
      execute: async ({ maxResults }) => {
      return await picaToolExecutor({
      platform: 'gmail',
      path: '/gmail/v1/users/me/messages',
      method: 'GET',
      query: { q: 'is:unread', maxResults: maxResults.toString() },
      connectionKey: process.env.GMAIL_CONNECTION_KEY,
      });
      },
      });
      \`\`\`

      ---

      ## 3) LangChain Tool Building

      \`\`\`typescript
      import { DynamicStructuredTool } from "@langchain/core/tools";
      import { z } from "zod";

      // Same picaToolExecutor as above...

      export const gmailLangChainTool = new DynamicStructuredTool({
      name: "fetch_gmail_emails",
      description: "Fetch unread Gmail emails using Pica BuildKit",
      schema: z.object({
      maxResults: z.number().optional().default(10),
      }),
      func: async ({ maxResults }) => {
      const result = await picaToolExecutor({
      platform: 'gmail',
      path: '/gmail/v1/users/me/messages',
      method: 'GET',
      query: { q: 'is:unread', maxResults: maxResults.toString() },
      connectionKey: process.env.GMAIL_CONNECTION_KEY,
      });
      return JSON.stringify(result);
      },
      });
      \`\`\`

      ---

      ## 4) MCP Server Building

      When building MCP servers, scaffold complete projects:

      ### File Structure
      \`\`\`
      my-integration-mcp/
      ├── package.json
      ├── src/
      │   └── index.ts
      ├── build/
      └── README.md
      \`\`\`

      ### package.json template
      \`\`\`json
      {
      "name": "my-integration-mcp",
      "version": "1.0.0",
      "type": "module",
      "main": "build/index.js",
      "scripts": {
      "build": "tsc",
      "prepare": "npm run build"
      },
      "dependencies": {
      "@modelcontextprotocol/sdk": "^1.0.0"
      },
      "devDependencies": {
      "typescript": "^5.0.0",
      "@types/node": "^20.0.0"
      }
      }
      \`\`\`

      ### src/index.ts template
      \`\`\`typescript
      #!/usr/bin/env node
      import { Server } from '@modelcontextprotocol/sdk/server/index.js';
      import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
      import {
      CallToolRequestSchema,
      ListToolsRequestSchema,
      } from '@modelcontextprotocol/sdk/types.js';

      // Same picaToolExecutor as above...

      const server = new Server(
      { name: 'my-integration-mcp', version: '1.0.0' },
      { capabilities: { tools: {} } }
      );

      server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
      tools: [
      {
        name: 'fetch_emails',
        description: 'Fetch emails from the integration',
        inputSchema: {
          type: 'object',
          properties: {
            maxResults: { type: 'number', description: 'Max results', default: 10 }
          },
          required: []
        }
      }
      ]
      };
      });

      server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      switch (name) {
      case 'fetch_emails':
      return {
        content: [{
          type: 'text',
          text: JSON.stringify(await picaToolExecutor({
            platform: 'gmail',
            path: '/gmail/v1/users/me/messages',
            method: 'GET',
            query: { q: 'is:unread', maxResults: args.maxResults?.toString() || '10' },
            connectionKey: process.env.GMAIL_CONNECTION_KEY,
          }))
        }]
      };
      default:
      throw new Error(\`Unknown tool: \${name}\`);
      }
      });

      async function main() {
      const transport = new StdioServerTransport();
      await server.connect(transport);
      }

      main().catch(console.error);
      \`\`\`

      ### tsconfig.json
      \`\`\`json
      {
      "compilerOptions": {
      "target": "ES2022",
      "module": "ES2022",
      "moduleResolution": "node",
      "outDir": "./build",
      "rootDir": "./src",
      "strict": true,
      "esModuleInterop": true,
      "skipLibCheck": true,
      "forceConsistentCasingInFileNames": true
      },
      "include": ["src/**/*"]
      }
      \`\`\`

      ---

      ## 5) Testing Your Integration

      Always provide testing steps:
      1. Set environment variables
      2. Test connection
      3. Verify tool responses
      4. Check error handling

      ---

      ## 6) Final Requirements

      Every integration you build must have:
      - Environment validation (\`PICA_API_KEY\`)
      - Connection key validation
      - Proper error handling with meaningful responses
      - Follows MCP protocol correctly
      - Pagination & rate-limits handled if needed
      - Minimal changes to existing project structure

      ---
      ```
    </Card>
  </Tab>
</Tabs>

<Check>You can verify setup by asking "What connections do I have in Pica?" - it should show your connections added above.</Check>

### Prompt the LLM to build your tool

<Tabs>
  <Tab title="Vercel AI SDK" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/vercel.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d9b5b6afefbef8d2241c018a7985a771" width="66" height="66" data-path="images/vercel.svg">
    <Card>
      Copy this prompt to build the Vercel AI SDK tool:

      ```markdown Vercel AI SDK Agent Prompt expandable theme={null}
      ## Vercel AI SDK: Sales Agent (BuildKit + Pica)

      This agent automates lead qualification and follow‑up using Gmail, Attio, and Slack via Pica. It is triggered by sending `/sales` in the chat.

      ## Critical Integration Rules
      - Do not hard-code API paths, HTTP methods, content types, or action IDs.
      - Always discover action contracts at runtime using Pica MCP utilities:
      1) list available actions for a platform
      2) fetch action knowledge for the chosen action (method, path template, params, content-type, pagination, rate limits, examples)
      - Build requests using the discovered contract with `picaToolExecutor` (passthrough), not static values.
      - Validate required environment variables at runtime and fail fast if missing.

      ### Discovery Flow (per tool call)
      1. Use Pica to list platform actions (e.g., gmail, attio, slack).
      2. Select the specific action by title/key (e.g., "List User Messages", "Get Message", "Create Draft", "List Objects", "List Attributes", "Create Attribute", "Assert Person Record", "chat.postMessage").
      3. Use action knowledge to derive method, path, query/body schema, and content type.
      4. Execute via `picaToolExecutor` using the derived values.

      ### Tools
      0) listAttioObjects
      - Purpose: List all Attio objects and dynamically resolve the correct People-like object identifier (slug/ID) instead of hardcoding "people".
      - Strategy: Prefer exact slug match for `people`; else case-insensitive match on title/slug containing "people"; else ask user or fail with a clear message.
      - Discovery: Resolve Attio action for "List Objects" at runtime and use returned identifiers in subsequent calls.

      1) fetchLeadEmails
      - Purpose: Fetch Gmail emails from the last 24 hours with sales keywords.
      - Filter: `after:YYYY/MM/DD` and keywords: "demo request", "pricing", "trial", "partnership", "interested" in subject or body.
      - Discovery: Resolve Gmail action for "List User Messages" at runtime; apply `q` and `maxResults` per the action contract.

      2) getGmailMessage
      - Purpose: Load full Gmail message details by id.
      - Discovery: Resolve Gmail action for "Get Message" at runtime; include `format=full` and `metadataHeaders` as supported.

      3) verifyAttioAttributes
      - Purpose: Ensure required People attributes exist in Attio; create missing ones automatically before any upserts.
      - Dynamic object selection: Use `listAttioObjects` to determine the correct People object identifier; then list/create attributes on that identifier.
      - Discovery:
      - Resolve Attio action for "List Attributes" on the resolved object identifier.
      - Resolve Attio action for "Create Attribute" on the resolved object identifier.
      - Required attributes and slug/type mapping (logical intent, not hard-coded contract):
      - Name → `name` (personal-name; usually system-provided)
      - Email → `email_addresses` (email-address; system)
      - Company → `company` (record-reference; config.allowed_objects: ["companies"])
      - Role → `title` (text)
      - Message → `description` (text)
      - Lead Score → `lead-score` (text)
      - Source → `source` (text)
      - Created Date → `created-date` (timestamp)
      - Creation must satisfy fields required by the discovered contract (description, flags, default_value with required `template`, and `config`).

      4) extractLeadDetails
      - Purpose: Parse and structure lead info from email body.
      - Output: `{ name?, email?, company?, role?, message }`
      - Behavior: Uses GPT extraction; handles signatures/forwards; falls back to raw body.

      5) upsertAttioPerson
      - Purpose: Create/update contact in Attio with lead details and score.
      - Discovery: Resolve Attio action for "Assert Person Record" at runtime and upsert with `matching_attribute=email_addresses` (use discovered query schema).
      - Body keys: `name`, `email_addresses`, `company` (domains or record id), `title` (role), `description` (message), `lead-score`, `source`, `created-date`.

      6) scoreLead
      - Purpose: Classify the lead as Hot / Warm / Cold using GPT.
      - Criteria:
      - Hot: explicit demo/pricing/call ASAP, strong buying signals
      - Warm: general interest, exploring, timeline soon
      - Cold: vague, non-buyer, unrelated

      7) postSlackNotification
      - Purpose: Post a structured message to Slack channel with lead details and suggested next steps.
      - Discovery: Resolve Slack action for `chat.postMessage` at runtime; send `{ channel, text, blocks }` according to the contract.

      8) generateEmailDraft
      - Purpose: Generate a personalized reply and create a Gmail draft.
      - Discovery: Resolve Gmail action for "Create Draft" at runtime; submit `{ message: { raw: base64url(RFC822) } }` if required by the contract.

      ## Attio Database Structure
      - Contacts
      - Name (Text)
      - Email (Email)
      - Company (Text)
      - Role (Text)
      - Message (Rich Text)
      - Lead Score (Select: Hot, Warm, Cold)
      - Source (Default: Gmail)
      - Created Date (Date)

      Note: Attio attributes use snake_case. Mappings used by the agent:
      - Role → `title`
      - Message → `description`
      - Lead Score → `lead_score`
      - Source → `source`
      - Created Date is automatic; do not set explicitly.

      ## Workflow
      1. Resolve People object identifier via `listAttioObjects`.
      2. Verify attributes on that object; create missing ones (via discovered Attio actions).
      3. Fetch new inbound sales-related emails from Gmail (last 24 hours, keywords; via discovered Gmail actions).
      4. For each message:
      - Load full message and extract a clean text body.
      - Extract lead details (name/email/company/role/message) with GPT.
      - If email missing, derive from `From` header.
      - Score the lead (Hot/Warm/Cold) with GPT.
      - Upsert contact in Attio using discovered Assert Person contract.
      - Post Slack notification to the configured channel with suggested next steps.
      - Generate a tailored Gmail draft reply.

      ## Environment Variables
      - `PICA_API_KEY`
      - `OPENAI_API_KEY`
      - `GMAIL_CONNECTION_KEY`
      - `ATTIO_CONNECTION_KEY`
      - `SLACK_CONNECTION_KEY`
      - `SLACK_CHANNEL_ID`

      ## Intelligent Behavior
      - Detect intent: pricing, demo request, partnership, general interest.
      - Assign score: Hot (immediate follow-up), Warm (nurture), Cold (archive/low priority).
      - Suggest next steps in Slack per score:
      - Hot: schedule demo, share pricing deck, propose times <24h
      - Warm: product overview, case studies, propose call this week
      - Cold: thank you + resources, reminder to follow up later
      - Prevent duplicates via Attio Assert (merge on email).
      - Robust error handling, retries, and logging.

      ## Implementation Notes
      - Command trigger: User sends `/sales` to run the workflow.
      - Message parsing: Support `content` (string | array), `parts` (array), or `text` fields to read user input robustly.
      - Chat response: For `/sales`, stream a proper assistant message to the UI using `toUIMessageStreamResponse()` (not a plain JSON Response).
      - Pica executor: Use a centralized helper that accepts `{ path, method, query/body, contentType }` derived from action knowledge (no hard-coded values).
      - Gmail filters: Always pass filtering via `q` (date + keywords) and limit with `maxResults` as supported by discovered contract.
      - Gmail body extraction: Prefer `payload.body.data` then walk parts for `text/plain`; fallback to `snippet`.
      - Draft creation: Build an RFC822 message and Base64URL-encode into `message.raw` if required by the discovered contract.
      - Attio attributes: Verify/create before upsert with safe defaults, correct `default_value.template`, and required `description` on the dynamically-resolved People object identifier.

      ## Security & Limits
      - Fail fast if required env vars are missing.
      - Do not print secrets.
      - Respect Gmail and Slack rate limits; keep message sizes reasonable.

      ## Invocation
      - Development chat UI: send `/sales` to execute.
      - Output: A streamed assistant message summarizing processed messages and per-lead results, with Slack posts sent and Gmail drafts created.
      ```
    </Card>
  </Tab>

  <Tab title="LangChain" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/langchain-icon.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d1f458c2169abf78446261c5a3650fba" width="66" height="66" data-path="images/langchain-icon.svg">
    <Card>
      Copy this prompt to build the LangChain tool:

      ```markdown LangChain Tool Suite expandable theme={null}
      ## LangChain Tool Suite: Sales Agent (BuildKit + Pica)

      This LangChain Tool Suite automates lead qualification and follow‑up using Gmail, Attio, and Slack via Pica.

      ## Critical Integration Rules
      - Do not hard-code API paths, HTTP methods, content types, or action IDs.
      - Always discover action contracts at runtime using Pica MCP utilities:
      1) list available actions for a platform
      2) fetch action knowledge for the chosen action (method, path template, params, content-type, pagination, rate limits, examples)
      - Build requests using the discovered contract with a shared `picaToolExecutor` (passthrough), not static values.
      - Validate required environment variables at runtime and fail fast if missing.

      ### Discovery Flow (per tool call)
      1. Use Pica to list platform actions (e.g., gmail, attio, slack).
      2. Select the specific action by title/key (e.g., "List User Messages", "Get Message", "Create Draft", "List Objects", "List Attributes", "Create Attribute", "Assert Person Record", "chat.postMessage").
      3. Use action knowledge to derive method, path, query/body schema, and content type.
      4. Execute via `picaToolExecutor` using the derived values.

      ### Tools
      0) listAttioObjects
      - Purpose: List all Attio objects and dynamically resolve the correct People-like object identifier (slug/ID) instead of hardcoding "people".
      - Strategy: Prefer exact slug match for `people`; else case-insensitive match on title/slug containing "people"; else ask user or fail with a clear message.

      1) fetchLeadEmails
      - Purpose: Fetch Gmail emails from the last 24 hours with sales keywords.
      - Filter: `after:YYYY/MM/DD` and keywords: "demo request", "pricing", "trial", "partnership", "interested" in subject or body.

      2) getGmailMessage
      - Purpose: Load full Gmail message details by id.

      3) verifyAttioAttributes
      - Purpose: Ensure required People attributes exist in Attio; create missing ones automatically before any upserts.
      - Dynamic object selection: Use `listAttioObjects` to determine the correct People object identifier; then list/create attributes on that identifier.
      - Required attributes and slug/type mapping:
      - Name → `name` (personal-name; usually system-provided)
      - Email → `email_addresses` (email-address; system)
      - Company → `company` (record-reference; config.allowed_objects: ["companies"])
      - Role → `title` (text)
      - Message → `description` (text)
      - Lead Score → `lead_score` (text)
      - Source → `source` (text)
      - Created Date is automatic; do not set explicitly.

      4) extractLeadDetails
      - Purpose: Parse and structure lead info from email body.
      - Output: `{ name?, email?, company?, role?, message }`
      - Behavior: Uses an LLM extraction; handles signatures/forwards; falls back to raw body.

      5) upsertAttioPerson
      - Purpose: Create/update contact in Attio with lead details and score.
      - Query: include `matching_attribute=email_addresses` as required by discovered schema.
      - Body keys: `name`, `email_addresses`, `company` (domains or record id), `title` (role), `description` (message), `lead_score`, `source`.

      6) scoreLead
      - Purpose: Classify the lead as Hot / Warm / Cold using an LLM.

      7) postSlackNotification
      - Purpose: Post a structured message to Slack channel with lead details and suggested next steps.

      8) generateEmailDraft
      - Purpose: Generate a personalized reply and create a Gmail draft.

      ## Attio Database Structure
      - Contacts
      - Name (Text)
      - Email (Email)
      - Company (Text)
      - Role (Text)
      - Message (Rich Text)
      - Lead Score (Select: Hot, Warm, Cold)
      - Source (Default: Gmail)
      - Created Date (Date)

      Note: Attio attributes use snake_case. Mappings used by the suite:
      - Role → `title`
      - Message → `description`
      - Lead Score → `lead_score`
      - Source → `source`
      - Created Date is automatic; do not set explicitly.

      ## Workflow
      1. Resolve People object identifier via `listAttioObjects`.
      2. Verify attributes on that object; create missing ones.
      3. Fetch new inbound sales-related emails from Gmail (last 24 hours, keywords).
      4. For each message: extract body, parse lead details, derive missing email from headers if needed, score, upsert in Attio, post Slack notification, create Gmail draft.

      ## Environment Variables
      - `PICA_API_KEY`
      - `OPENAI_API_KEY`
      - `GMAIL_CONNECTION_KEY`
      - `ATTIO_CONNECTION_KEY`
      - `SLACK_CONNECTION_KEY`
      - `SLACK_CHANNEL_ID`

      ## Implementation Notes
      - Use `picaToolExecutor` with dynamically discovered `{ path, method, query/body, contentType }`.
      - If a full URL is returned by discovery, extract and use only its pathname as the passthrough path.
      - Apply Gmail `q` and `maxResults` correctly; extract Gmail body by preferring `payload.body.data`, then walking parts; fallback to `snippet`.
      - Upserts use `matching_attribute=email_addresses` and snake_case attribute slugs.
      - Handle errors and rate limits gracefully.
      ```
    </Card>
  </Tab>

  <Tab title="MCP Server" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/model-context-protocol.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=1b2f1412de374da9c59b275480e85f52" width="66" height="66" data-path="images/model-context-protocol.svg">
    <Card>
      Copy this prompt to build a the MCP server tool:

      ```markdown MCP Server expandable theme={null}
      ## MCP Server: Sales Agent Tools (BuildKit + Pica)

      This MCP server exposes tools to automate lead qualification and follow‑up using Gmail, Attio, and Slack via Pica.

      ## Critical Integration Rules
      - Do not hard-code API paths, HTTP methods, content types, or action IDs.
      - Always discover action contracts at runtime using Pica MCP utilities:
      1) list available actions for a platform
      2) fetch action knowledge for the chosen action (method, path template, params, content-type, pagination, rate limits, examples)
      - Build requests using the discovered contract with a shared `picaToolExecutor` (passthrough), not static values.
      - Validate required environment variables at runtime and fail fast if missing.

      ### Discovery Flow (per tool call)
      1. Use Pica to list platform actions (e.g., gmail, attio, slack).
      2. Select the specific action by title/key (e.g., "List User Messages", "Get Message", "Create Draft", "List Objects", "List Attributes", "Create Attribute", "Assert Person Record", "chat.postMessage").
      3. Use action knowledge to derive method, path, query/body schema, and content type.
      4. Execute via `picaToolExecutor` using the derived values.

      ### Tools (MCP)
      - list_attio_objects
      - fetch_lead_emails
      - get_gmail_message
      - verify_attio_attributes
      - extract_lead_details
      - upsert_attio_person
      - score_lead
      - post_slack_notification
      - generate_email_draft

      Tool behaviors mirror the Vercel/LangChain specs:
      - `list_attio_objects`: resolve People-like object identifier dynamically (prefer slug `people`, else contains "people").
      - `fetch_lead_emails`: last 24h, apply `q` and `maxResults` via contract.
      - `get_gmail_message`: load full message with `format=full`, `metadataHeaders` as supported.
      - `verify_attio_attributes`: list/create attributes on the resolved object identifier; required slugs: `title`, `description`, `lead_score`, `source`, `company` (record-reference).
      - `extract_lead_details`: parse `{ name?, email?, company?, role?, message }` using an LLM.
      - `upsert_attio_person`: upsert with `matching_attribute=email_addresses`; body keys include `name`, `email_addresses`, `company`, `title`, `description`, `lead_score`, `source`.
      - `score_lead`: Hot/Warm/Cold classification.
      - `post_slack_notification`: post structured summary + next steps to channel.
      - `generate_email_draft`: create Gmail draft from RFC822 base64url `message.raw`.

      ## Attio Database Structure
      - Contacts
      - Name (Text)
      - Email (Email)
      - Company (Text)
      - Role (Text)
      - Message (Rich Text)
      - Lead Score (Select: Hot, Warm, Cold)
      - Source (Default: Gmail)
      - Created Date (Date)

      Note: Attio attributes use snake_case. Mappings used by the server:
      - Role → `title`
      - Message → `description`
      - Lead Score → `lead_score`
      - Source → `source`
      - Created Date is automatic; do not set explicitly.

      ## Workflow (Suggested Orchestration Tool)
      1. Resolve People object identifier via `list_attio_objects`.
      2. Verify attributes on that object; create missing ones.
      3. Fetch new inbound sales-related emails from Gmail (last 24 hours, keywords).
      4. For each message: extract body, parse lead details, derive missing email from headers if needed, score, upsert in Attio, post Slack notification, create Gmail draft.

      ## Environment Variables
      - `PICA_API_KEY`
      - `OPENAI_API_KEY`
      - `GMAIL_CONNECTION_KEY`
      - `ATTIO_CONNECTION_KEY`
      - `SLACK_CONNECTION_KEY`
      - `SLACK_CHANNEL_ID`

      ## Implementation Notes
      - Provide strict input schemas (zod) per tool.
      - Use `picaToolExecutor` with dynamically discovered `{ path, method, query/body, contentType }`.
      - If a full URL is returned by discovery, extract and use only its pathname as the passthrough path.
      - Apply Gmail `q` and `maxResults` correctly; extract Gmail body by preferring `payload.body.data`, then walking parts; fallback to `snippet`.
      - Upserts use `matching_attribute=email_addresses` and snake_case attribute slugs.
      - Handle errors and rate limits gracefully and return structured MCP responses.
      ```
    </Card>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).