# Source: https://docs.picaos.com/use-cases/smart-home-data-hub.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build a Smart Home Data Hub

> 👋 Follow this tutorial to build a comprehensive Smart Home Data Hub using Pica MCP integrations that monitors weather conditions, logs environmental data to Google Sheets, and sends intelligent email reports — all in under 10 minutes.

export const AddConnections = ({platforms}) => {
  if (!platforms) return null;
  return <>
      {platforms.map(platform => <Columns cols={1}>
          <Card title={`Add ${platform.name} Connection`} href={`https://app.picaos.com/connections#open=${platform.code}`} arrow="true" key={platform.code}>
          </Card>
        </Columns>)}
    </>;
};

export const platformNames_1 = "wttr.in Weather API, Google Sheets, and Gmail accounts"

export const Header = ({size, text}) => {
  const Tag = `h${size}`;
  return <Tag>{text}</Tag>;
};

export const platformNames_0 = "wttr.in Weather API, Google Sheets, and Gmail accounts"

export const projectType_0 = "Vercel AI SDK"

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

<AddConnections platforms={[{'name': 'wttr.in Weather API', 'code': 'wttr-in'}, {'name': 'Google Sheets', 'code': 'google-sheets'}, {'name': 'Gmail', 'code': 'gmail'}]} />

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

      ```markdown Smart Home Data Hub Prompt expandable theme={null}
      # Smart Home Data Hub - Complete Vercel AI SDK Implementation

      Create a comprehensive Smart Home Data Hub using Vercel AI SDK, Pica MCP integrations, and TypeScript. This system monitors weather conditions, logs environmental data to Google Sheets, and sends intelligent email reports.

      ## CRITICAL PATH REQUIREMENTS

      **MOST IMPORTANT**: All Pica API paths must NOT include `/v4/` prefix. Use only:
      - ✅ `spreadsheets/${spreadsheetId}/values/${range}:append` 
      - ✅ `spreadsheets/${spreadsheetId}/values/${range}`
      - ❌ Never use: `/v4/spreadsheets/...` (causes path duplication errors)

      ## REQUIRED TOOLS TO BUILD

      ### 1. fetchWeatherData.ts
      **Purpose**: Fetch comprehensive weather data from wttr.in
      **Key Features**:
      - Location input with flexible formats (City,State or City,Country)
      - JSON format response with structured environmental data
      - Extract: temperature, humidity, pressure, wind, UV index, visibility, cloud cover, precipitation
      - Include current conditions, forecast, and astronomical data
      - Proper error handling and location validation

      **Pica Integration**:
      - Platform: `wttr-in`
      - Action ID: Use "Get Weather Data" action
      - Path: `/${encodeURIComponent(location)}`
      - Query: `format=j1`
      - Method: GET

      ### 2. logEnvironmentalData.ts  
      **Purpose**: Log structured environmental data to Google Sheets
      **Key Features**:
      - Automatic spreadsheet ID extraction from URLs
      - Auto-generate headers on first use: Timestamp, Location, Temperature (°C), Humidity (%), Pressure (hPa), Wind Speed (km/h), UV Index, Visibility (km), Cloud Cover (%), Precipitation (mm), Weather Description, Energy Usage (kWh), Indoor Temp (°C), Notes
      - Formatted timestamp for readability
      - Support for optional energy and indoor temperature data
      - Robust error handling with fallback for header creation

      **Pica Integration**:
      - Platform: `google-sheets`
      - Action ID: Use "Append Values to a Spreadsheet" action
      - Path: `spreadsheets/${spreadsheetId}/values/${encodeURIComponent(sheetName)}:append`
      - Method: POST
      - Query Parameters: `valueInputOption=USER_ENTERED&insertDataOption=INSERT_ROWS&includeValuesInResponse=true`
      - Body: `{ values: [[...dataRow]], majorDimension: "ROWS" }`

      ### 3. sendDailyWeatherReport.ts
      **Purpose**: Send beautiful HTML email reports with weather insights
      **Key Features**:
      - Mobile-responsive HTML email design
      - Weather emoji indicators based on conditions
      - Smart optimization recommendations based on temperature, humidity, UV index
      - Energy usage analysis (if provided)
      - Trend indicators with visual arrows
      - Professional styling with inline CSS
      - Base64url encoding for Gmail API

      **Pica Integration**:
      - Platform: `gmail`
      - Action ID: Use "Send Mail" action  
      - Path: `users/me/messages/send`
      - Method: POST
      - Body: `{ raw: base64UrlEncodedMessage }`
      - MIME format: Include To, Subject, Content-Type headers

      ## ENVIRONMENT VARIABLES NEEDED
      PICA_API_KEY=your_pica_api_key
      WTTR_IN_CONNECTION_KEY=your_wttr_connection_key
      GOOGLE_SHEETS_CONNECTION_KEY=your_google_sheets_connection_key
      GMAIL_CONNECTION_KEY=your_gmail_connection_key

      ## PICA TOOL EXECUTOR UTILITY

      Create `src/utils/picaToolExecutor.ts` with a function that handles Pica API passthrough calls:
      - Base URL: 'https://api.picaos.com/v1/passthrough'
      - Headers: content-type, x-pica-secret, x-pica-connection-key, x-pica-action-id
      - Support for GET/POST methods with query params and body
      - Proper error handling and JSON response parsing

      ## SMART RECOMMENDATIONS ENGINE

      Implement intelligent recommendations based on:
      - **Temperature > 25°C**: "High temperature - consider increasing AC efficiency"
      - **Temperature < 5°C**: "Low temperature - check heating system efficiency" 
      - **Humidity > 60%**: "High humidity - consider dehumidifier"
      - **Humidity < 30%**: "Low humidity - consider humidifier"
      - **UV Index > 7**: "High UV - close blinds to reduce cooling load"
      - **Energy Usage > 30 kWh**: "High energy usage - review appliance efficiency"

      ## VERCEL AI SDK INTEGRATION

      Update `src/app/api/chat/route.ts`:
      - Import all three tools
      - Add to tools object in streamText configuration
      - Update system prompt to include Smart Home capabilities
      - Include workflow commands: "Monitor weather", "Log environmental data", "Send daily report"

      ## DATA STRUCTURES

      **Weather Data Interface**:
      - location: { name, country, latitude, longitude }
      - current: { temperature: {celsius, fahrenheit}, humidity, pressure, windSpeed: {kmh, mph}, uvIndex, visibility: {km, miles}, cloudCover, precipitation: {mm, inches}, weatherDescription }
      - forecast: { maxTemp: {celsius, fahrenheit}, minTemp: {celsius, fahrenheit}, sunHours }

      ## ERROR HANDLING PATTERNS

      - Validate all environment variables at tool execution start
      - Extract spreadsheet IDs from URLs with regex: `/\/d\/([a-zA-Z0-9-_]+)/`
      - Handle missing optional data with fallback empty strings
      - Provide detailed error messages for debugging
      - Include retry logic for transient API failures

      ## TESTING WORKFLOW

      1. **Weather Test**: `"Get weather data for Toronto,ON"`
      2. **Logging Test**: `"Log environmental data to spreadsheet [ID] with temperature 22, humidity 45"`
      3. **Email Test**: `"Send daily weather report for New York,NY to user@example.com"`
      4. **Full Workflow**: `"Monitor weather for London,UK, log to spreadsheet [ID], and email report to user@example.com"`

      ## BUILD REQUIREMENTS

      - TypeScript with strict mode
      - Zod for input validation
      - Next.js 15+ with Turbopack
      - Vercel AI SDK latest version
      - Proper export statements for all tools
      - No circular dependencies

      ## SUCCESS CRITERIA

      ✅ Weather fetching returns structured data with all environmental metrics
      ✅ Google Sheets logging creates proper headers and appends data correctly  
      ✅ Email reports are mobile-responsive with smart recommendations
      ✅ All tools handle errors gracefully with detailed logging
      ✅ System builds without TypeScript errors
      ✅ Environment variables are properly validated

      ## IMPLEMENTATION NOTES

      Each tool should:
      1. Use Zod schemas for input validation
      2. Validate required environment variables
      3. Use the picaToolExecutor utility for all Pica API calls
      4. Return structured success/error responses
      5. Include comprehensive error handling
      6. Follow TypeScript best practices

      The fetchWeatherData tool parses wttr.in JSON response into structured weather data.
      The logEnvironmentalData tool automatically creates headers and handles spreadsheet URL parsing.
      The sendDailyWeatherReport tool generates mobile-responsive HTML emails with weather emojis and smart recommendations.

      All tools integrate seamlessly with Vercel AI SDK using the tool() function and can be chained together for complete environmental monitoring workflows.

      This creates a production-ready Smart Home Data Hub that monitors environmental conditions, provides intelligent insights, and maintains historical data for optimization opportunities.
      ```
    </Card>
  </Tab>

  <Tab title="LangChain" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/langchain-icon.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d1f458c2169abf78446261c5a3650fba" width="66" height="66" data-path="images/langchain-icon.svg">
    <Card>
      Copy this prompt to build the LangChain tool:

      ```markdown LangChain Tool Suite expandable theme={null}
      ## LangChain Tool Suite: Smart Home Data Hub (BuildKit + Pica)

      This LangChain Tool Suite creates a comprehensive Smart Home Data Hub that monitors weather conditions, logs environmental data to Google Sheets, and sends intelligent email reports using Pica MCP integrations.

      ## Critical Integration Rules
      - Do not hard-code API paths, HTTP methods, content types, or action IDs.
      - Always discover action contracts at runtime using Pica MCP utilities:
      1) list available actions for a platform
      2) fetch action knowledge for the chosen action (method, path template, params, content-type, pagination, rate limits, examples)
      - Build requests using the discovered contract with a shared `picaToolExecutor` (passthrough), not static values.
      - Validate required environment variables at runtime and fail fast if missing.

      ### Discovery Flow (per tool call)
      1. Use Pica to list platform actions (e.g., wttr-in, google-sheets, gmail).
      2. Select the specific action by title/key (e.g., "Get Weather Data", "Append Values to a Spreadsheet", "Send Mail").
      3. Use action knowledge to derive method, path, query/body schema, and content type.
      4. Execute via `picaToolExecutor` using the derived values.

      ### Tools
      1) fetchWeatherData
      - Purpose: Fetch comprehensive weather data from wttr.in API
      - Discovery: Use "Get Weather Data" action; path `/${encodeURIComponent(location)}` with query `format=j1`
      - Parse response into structured weather data with temperature, humidity, pressure, wind, UV index, etc.

      2) logEnvironmentalData
      - Purpose: Log structured environmental data to Google Sheets with automatic header creation
      - Discovery: Use "Append Values to a Spreadsheet" action; path `spreadsheets/${spreadsheetId}/values/${sheetName}:append`
      - Auto-generate headers: Timestamp, Location, Temperature, Humidity, Pressure, Wind Speed, UV Index, etc.
      - Extract spreadsheet ID from URLs using regex pattern

      3) sendDailyWeatherReport
      - Purpose: Send mobile-responsive HTML email reports with weather insights and smart recommendations
      - Discovery: Use "Send Mail" action; path `users/me/messages/send`
      - Generate HTML email with weather emojis, optimization recommendations, and professional styling
      - Base64url encode RFC822 message format

      ## Smart Recommendations Engine
      Implement intelligent recommendations based on environmental data:
      - Temperature thresholds for HVAC efficiency
      - Humidity control suggestions
      - UV index warnings for energy optimization
      - Energy usage analysis and appliance efficiency tips

      ## Environment Variables
      - `PICA_API_KEY`
      - `OPENAI_API_KEY`
      - `WTTR_IN_CONNECTION_KEY`
      - `GOOGLE_SHEETS_CONNECTION_KEY`
      - `GMAIL_CONNECTION_KEY`

      ## Workflow
      1. Fetch weather data for specified location
      2. Log environmental data to Google Sheets with timestamps
      3. Generate and send HTML email report with smart recommendations
      4. Provide actionable insights for home optimization

      ## Implementation Notes
      - Use shared `picaToolExecutor` with dynamically discovered action contracts
      - Handle missing optional data with fallback empty strings
      - Extract spreadsheet IDs from URLs with regex: `/\/d\/([a-zA-Z0-9-_]+)/`
      - Generate weather emojis based on conditions for email reports
      - Include retry logic for transient API failures
      ```
    </Card>
  </Tab>

  <Tab title="MCP Server" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/model-context-protocol.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=1b2f1412de374da9c59b275480e85f52" width="66" height="66" data-path="images/model-context-protocol.svg">
    <Card>
      Copy this prompt to build the MCP server tool:

      ```markdown MCP Server expandable theme={null}
      ## MCP Server: Smart Home Data Hub Tools (BuildKit + Pica)

      This MCP server exposes tools for a comprehensive Smart Home Data Hub that monitors weather conditions, logs environmental data to Google Sheets, and sends intelligent email reports via Pica.

      ## Critical Integration Rules
      - Do not hard-code API paths, HTTP methods, content types, or action IDs.
      - Always discover action contracts at runtime using Pica MCP utilities:
      1) list available actions for a platform
      2) fetch action knowledge for the chosen action (method, path template, params, content-type, pagination, rate limits, examples)
      - Build requests using the discovered contract with a shared `picaToolExecutor` (passthrough), not static values.
      - Validate required environment variables at runtime and fail fast if missing.

      ### Discovery Flow (per tool call)
      1. Use Pica to list platform actions (e.g., wttr-in, google-sheets, gmail).
      2. Select the specific action by title/key (e.g., "Get Weather Data", "Append Values to a Spreadsheet", "Send Mail").
      3. Use action knowledge to derive method, path, query/body schema, and content type.
      4. Execute via `picaToolExecutor` using the derived values.

      ### Tools (MCP)
      - fetch_weather_data
      - log_environmental_data
      - send_daily_weather_report

      Tool behaviors:
      - `fetch_weather_data`: Fetch weather from wttr.in with `format=j1` query, parse into structured data (temperature, humidity, pressure, wind, UV index, visibility, cloud cover, precipitation)
      - `log_environmental_data`: Auto-extract spreadsheet ID from URLs, create headers if needed, append environmental data with timestamps
      - `send_daily_weather_report`: Generate mobile-responsive HTML email with weather emojis, smart recommendations, and Base64url encoding

      ## Smart Recommendations Logic
      - Temperature > 25°C: "High temperature - consider increasing AC efficiency"
      - Temperature < 5°C: "Low temperature - check heating system efficiency"
      - Humidity > 60%: "High humidity - consider dehumidifier"
      - Humidity < 30%: "Low humidity - consider humidifier"
      - UV Index > 7: "High UV - close blinds to reduce cooling load"
      - Energy Usage > 30 kWh: "High energy usage - review appliance efficiency"

      ## Environment Variables
      - `PICA_API_KEY`
      - `WTTR_IN_CONNECTION_KEY`
      - `GOOGLE_SHEETS_CONNECTION_KEY`
      - `GMAIL_CONNECTION_KEY`

      ## Data Structures
      Weather data includes location info, current conditions (temperature in C/F, humidity %, pressure hPa, wind speed km/h and mph, UV index, visibility km/miles, cloud cover %, precipitation mm/inches, weather description), and forecast data.

      ## Error Handling
      - Validate environment variables at startup
      - Extract spreadsheet IDs with regex: `/\/d\/([a-zA-Z0-9-_]+)/`
      - Handle missing optional data gracefully
      - Provide detailed error messages for debugging
      - Include retry logic for API failures

      ## Usage Examples
      - "Get weather data for Toronto,ON"
      - "Log environmental data to spreadsheet [ID] with temperature 22, humidity 45"
      - "Send daily weather report for New York,NY to user@example.com"
      - "Monitor weather for London,UK, log to spreadsheet [ID], and email report"
      ```
    </Card>
  </Tab>
</Tabs>

You can verify setup by asking "What connections do I have in Pica?" - it should show your connections added above.


Built with [Mintlify](https://mintlify.com).