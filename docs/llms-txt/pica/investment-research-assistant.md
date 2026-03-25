# Source: https://docs.picaos.com/use-cases/investment-research-assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build an Investment Research Assistant

> 🚀 Create an intelligent system that automatically fetches real-time stock data, analyzes market trends, gathers relevant financial news, and creates comprehensive investment research notes in Notion.

export const AddConnections = ({platforms}) => {
  if (!platforms) return null;
  return <>
      {platforms.map(platform => <Columns cols={1}>
          <Card title={`Add ${platform.name} Connection`} href={`https://app.picaos.com/connections#open=${platform.code}`} arrow="true" key={platform.code}>
          </Card>
        </Columns>)}
    </>;
};

export const platformNames_1 = "Twelve Data, News Data IO, and Notion accounts"

export const Header = ({size, text}) => {
  const Tag = `h${size}`;
  return <Tag>{text}</Tag>;
};

export const platformNames_0 = "Twelve Data, News Data IO, and Notion accounts"

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

<AddConnections platforms={[{'name': 'Twelve Data', 'code': 'twelve-data'}, {'name': 'News Data IO', 'code': 'news-data-io'}, {'name': 'Notion', 'code': 'notion'}]} />

### Required Environment Variables

You'll need these connection keys in your environment:

```bash Environment Setup theme={null}
TWELVE_DATA_CONNECTION_KEY=your_twelve_data_connection_key
NEWS_DATA_IO_CONNECTION_KEY=your_news_data_io_connection_key
NOTION_CONNECTION_KEY=your_notion_connection_key
OPENAI_API_KEY=your_openai_api_key
PICA_API_KEY=your_pica_api_key
```

### Using the System

Once your system is set up, you can use prompts to conduct investment research. Here's an example prompt format:

```
Research AAPL stock - fetch current price, technical indicators, recent financial news, analyst recommendations, and create a comprehensive investment research note in Notion database: {your_notion_database_id}
```

Replace `{your_notion_database_id}` with your actual Notion database ID. This command will:

* Fetch real-time stock price and market data
* Calculate key technical indicators (RSI, MACD, Moving Averages)
* Gather recent financial news and market sentiment
* Retrieve analyst recommendations and price targets
* Create a comprehensive research page in your Notion Investment Research database

### Notion Database Setup

The system will create a comprehensive Investment Research database in your Notion workspace:

<Tabs>
  <Tab title="Investment Research Database">
    **Database Name:** "Investment Research"

    **Properties:**

    * Stock Symbol (Title)
    * Company Name (Text)
    * Research Date (Date)
    * Current Price (Number)
    * Price Change % (Number)
    * Market Cap (Text)
    * Volume (Number)
    * 52 Week High (Number)
    * 52 Week Low (Number)
    * P/E Ratio (Number)
    * RSI (Number)
    * MACD Signal (Select: Bullish, Bearish, Neutral)
    * Moving Average Trend (Select: Uptrend, Downtrend, Sideways)
    * Analyst Rating (Select: Strong Buy, Buy, Hold, Sell, Strong Sell)
    * Average Price Target (Number)
    * News Sentiment (Select: Very Positive, Positive, Neutral, Negative, Very Negative)
    * Key News Headlines (Rich Text)
    * Technical Analysis (Rich Text)
    * Fundamental Analysis (Rich Text)
    * Investment Recommendation (Rich Text)
    * Risk Assessment (Select: Low, Medium, High, Very High)
    * Research Status (Select: New, In Progress, Completed, Archived)
  </Tab>
</Tabs>

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
      # Investment Research Assistant - Vercel AI SDK Agent

      Create a comprehensive Vercel AI SDK agent with multiple tools for automated investment research using Twelve Data, News Data IO, and Notion integrations through Pica. The agent should provide complete market analysis and research documentation.

      TOOLS NEEDED:
      1. fetchStockQuote - Get real-time stock price and basic market data
      2. fetchTechnicalIndicators - Calculate RSI, MACD, and moving averages
      3. fetchCompanyProfile - Get company fundamentals, financials, and key metrics
      4. fetchAnalystRecommendations - Get analyst ratings and price targets
      5. fetchFinancialNews - Get relevant news articles for the stock
      6. createNotionResearchPage - Create comprehensive research page in Notion
      7. updateResearchAnalysis - Update existing research with new data

      TWELVE DATA INTEGRATION (Key Action IDs):
      - Real-time Quote: conn_mod_def::GF2-Z7VKGyk::lFnyTBCvT-uzAjFzH4rMbg
      - Latest Price: conn_mod_def::GF2-aBZZCFo::jQlXPsJfR0q6O3bD32YBxA
      - RSI Indicator: conn_mod_def::GF2-jSqIafo::o95SRd1SStK7bctlf6tIlA
      - MACD Indicator: conn_mod_def::GF2-hWZx3Xc::EmZTkd_BTraHKCZM2L0Uag
      - Simple Moving Average: conn_mod_def::GF2-nXThAks::ORlFzdRmRi-Wh8oQ_zs-8w
      - Company Profile: conn_mod_def::GF2-cwyZSoA::D4fYT0fbTk2A2IOukaZa0w
      - Analyst Recommendations: conn_mod_def::GF2-YSGIQYQ::fgLtfLBKTHuYoG9nrbwYtg
      - Price Target: conn_mod_def::GF2-YY28HvY::C6fyIG9FRjKBBqSjbxEOxg
      - Historical Data: conn_mod_def::GF2-Zvby_Cc::i_vNEX_HRUi2c0pTS0_7Ng

      NEWS DATA IO INTEGRATION (Key Action IDs):
      - Latest News: conn_mod_def::GCMkJZ1uN7I::UKpo5iDlRoSnfi5C8ih4FA
      - News Archive: conn_mod_def::GCMkI5HRRGE::oq0ikaXKRdibN7hxItyRaA

      NOTION INTEGRATION (Key Action IDs):
      - Create Page: conn_mod_def::GCWcIDJuR4A::izAAbGNdQdKddzdP_JS4kw
      - Create Database: conn_mod_def::GCWcHtC65WM::b4RMZv4aTjG_ni4ayKc0GA
      - Update Page Properties: conn_mod_def::GCWcIBCFd3I::0UgTnKvXR5avVymmegseFA
      - Query Database: conn_mod_def::GCWcHfwwY6Y::XqFfl-WYTguWn860w-Hnqw

      NOTION DATABASE STRUCTURE:
      - Database Name: "Investment Research"
      - Properties:
        * Stock Symbol (title)
        * Company Name (text)
        * Research Date (date)
        * Current Price (number)
        * Price Change % (number)
        * Market Cap (text)
        * Volume (number)
        * 52 Week High (number)
        * 52 Week Low (number)
        * P/E Ratio (number)
        * RSI (number)
        * MACD Signal (select: Bullish, Bearish, Neutral)
        * Moving Average Trend (select: Uptrend, Downtrend, Sideways)
        * Analyst Rating (select: Strong Buy, Buy, Hold, Sell, Strong Sell)
        * Average Price Target (number)
        * News Sentiment (select: Very Positive, Positive, Neutral, Negative, Very Negative)
        * Key News Headlines (rich text)
        * Technical Analysis (rich text)
        * Fundamental Analysis (rich text)
        * Investment Recommendation (rich text)
        * Risk Assessment (select: Low, Medium, High, Very High)
        * Research Status (select: New, In Progress, Completed, Archived)

      RESEARCH WORKFLOW:
      1. Fetch real-time stock quote and basic market data
      2. Calculate key technical indicators (RSI, MACD, SMA)
      3. Get company profile and fundamental data
      4. Retrieve analyst recommendations and price targets
      5. Gather recent financial news and analyze sentiment
      6. Create comprehensive analysis combining all data
      7. Generate investment recommendation and risk assessment
      8. Create or update Notion research page with structured data

      TECHNICAL ANALYSIS RULES:
      - RSI > 70: Overbought, potential sell signal
      - RSI < 30: Oversold, potential buy signal  
      - MACD above signal line: Bullish momentum
      - MACD below signal line: Bearish momentum
      - Price above SMA: Uptrend
      - Price below SMA: Downtrend

      SENTIMENT ANALYSIS:
      - Analyze news headlines for positive/negative keywords
      - Count analyst upgrades vs downgrades
      - Factor in price target vs current price
      - Combine technical and fundamental signals

      ENVIRONMENT VARIABLES NEEDED:
      - TWELVE_DATA_CONNECTION_KEY
      - NEWS_DATA_IO_CONNECTION_KEY  
      - NOTION_CONNECTION_KEY
      - OPENAI_API_KEY
      - PICA_API_KEY

      Make the system intelligent enough to:
      - Handle various stock symbols and validate ticker symbols
      - Provide comprehensive technical and fundamental analysis
      - Generate clear, actionable investment recommendations
      - Create well-structured, searchable Notion research pages
      - Handle API rate limits and error conditions gracefully
      - Combine multiple data sources for holistic investment insights
      ```

      <Note>The system provides comprehensive investment research by combining real-time market data, technical analysis, and news sentiment.</Note>
    </Card>
  </Tab>

  <Tab title="LangChain" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/langchain-icon.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=d1f458c2169abf78446261c5a3650fba" width="66" height="66" data-path="images/langchain-icon.svg">
    <Card>
      Copy this prompt to build the LangChain tool:

      ```markdown LangChain Investment Research Tools expandable theme={null}
      # LangChain Investment Research Assistant

      Create a comprehensive LangChain tool suite for automated investment research using Twelve Data, News Data IO, and Notion integrations through Pica. Build tools that provide professional-grade market analysis.

      CORE TOOLS:
      1. StockDataFetcher - LangChain tool for real-time stock quotes and market data
      2. TechnicalAnalyzer - Tool for calculating and interpreting technical indicators
      3. FundamentalAnalyzer - Tool for company financials and valuation metrics
      4. NewsAnalyzer - Tool for gathering and analyzing financial news sentiment
      5. AnalystDataCollector - Tool for collecting analyst recommendations and targets
      6. NotionResearchCreator - Tool for creating structured research pages
      7. ResearchSynthesizer - Tool for combining all analysis into recommendations

      LANGCHAIN IMPLEMENTATION REQUIREMENTS:
      - Use LangChain's tool decorator and structured input/output schemas
      - Implement proper error handling with LangChain's error types
      - Use LangChain's memory system to track research state across tools
      - Integrate with LangChain agents for orchestrating research workflow
      - Support streaming responses for real-time research updates

      TECHNICAL INDICATORS TO IMPLEMENT:
      - RSI (Relative Strength Index) with overbought/oversold signals
      - MACD (Moving Average Convergence Divergence) with signal line crossovers
      - SMA (Simple Moving Average) for trend identification
      - Volume analysis for confirmation signals
      - Support and resistance level identification

      FUNDAMENTAL ANALYSIS COMPONENTS:
      - P/E ratio and valuation metrics
      - Revenue and earnings growth analysis
      - Debt-to-equity and financial health ratios
      - Market capitalization and sector comparison
      - Dividend yield and payout ratio analysis

      NEWS SENTIMENT ANALYSIS:
      - Keyword extraction from financial news headlines
      - Sentiment scoring using NLP techniques
      - Event impact assessment (earnings, mergers, regulatory changes)
      - Social media sentiment integration
      - News volume and recency weighting

      NOTION RESEARCH STRUCTURE:
      Create comprehensive research pages with:
      - Executive summary with key findings
      - Technical analysis section with charts and indicators
      - Fundamental analysis with financial metrics
      - News sentiment analysis with key headlines
      - Analyst consensus and price target summary
      - Investment recommendation with risk assessment
      - Historical performance and trend analysis

      RESEARCH WORKFLOW ORCHESTRATION:
      1. Validate stock symbol and fetch basic company information
      2. Gather real-time price data and calculate technical indicators
      3. Analyze company fundamentals and financial health
      4. Collect recent news articles and perform sentiment analysis
      5. Retrieve analyst recommendations and price targets
      6. Synthesize all data into comprehensive investment thesis
      7. Create structured Notion research page with all findings
      8. Generate executive summary and actionable recommendations

      ERROR HANDLING AND RESILIENCE:
      - Graceful degradation when APIs are unavailable
      - Retry mechanisms for transient failures
      - Data validation and sanitization
      - Fallback to cached data when appropriate
      - Clear error messaging for users

      Use Pica integrations for seamless API access to Twelve Data, News Data IO, and Notion. The research assistant should provide institutional-quality analysis accessible through natural language queries.
      ```

      <Note>The LangChain tools provide professional-grade investment research with comprehensive data analysis and structured documentation.</Note>
    </Card>
  </Tab>

  <Tab title="MCP Server" icon="https://mintcdn.com/pica-236d4a1e/kLG8rLJY_ZkadQp9/images/model-context-protocol.svg?fit=max&auto=format&n=kLG8rLJY_ZkadQp9&q=85&s=1b2f1412de374da9c59b275480e85f52" width="66" height="66" data-path="images/model-context-protocol.svg">
    <Card>
      Copy this prompt to build the MCP server tool:

      ```markdown MCP Investment Research Server expandable theme={null}
      # Complete MCP Investment Research Server

      Create a complete MCP (Model Context Protocol) server for automated investment research with Twelve Data, News Data IO, and Notion integrations through Pica. The server should provide comprehensive market analysis tools for financial research.

      MCP SERVER STRUCTURE:
      - Server name: "investment-research-server"
      - Version: "1.0.0"  
      - Description: "MCP server for automated investment research with real-time data, technical analysis, and comprehensive reporting"

      TOOLS TO IMPLEMENT:
      1. fetch_stock_data - Get real-time quotes, historical data, and basic market information
      2. calculate_technical_indicators - Compute RSI, MACD, moving averages, and trend signals
      3. analyze_company_fundamentals - Retrieve company profile, financials, and valuation metrics
      4. get_analyst_consensus - Fetch analyst ratings, recommendations, and price targets
      5. gather_financial_news - Collect recent news articles and perform sentiment analysis
      6. create_research_database - Set up Notion database for investment research tracking
      7. create_research_report - Generate comprehensive research page with all analysis
      8. update_research_status - Update research status and add new findings

      TWELVE DATA API INTEGRATION:
      Real-time Data Tools:
      - Stock quotes with bid/ask spreads and volume
      - Historical price data with adjustments for splits/dividends
      - Intraday data with multiple time intervals
      - Market hours and trading status information

      Technical Indicators:
      - RSI with customizable periods and overbought/oversold levels
      - MACD with signal line, histogram, and divergence detection
      - Moving averages (SMA, EMA, WMA) for trend analysis
      - Bollinger Bands for volatility and support/resistance
      - Volume indicators for confirmation signals

      Fundamental Data:
      - Company profiles with business descriptions and key metrics
      - Financial statements (income, balance sheet, cash flow)
      - Earnings data and estimates with surprise analysis
      - Dividend history and yield calculations
      - Analyst recommendations and price target consensus

      NEWS DATA IO INTEGRATION:
      News Analysis Tools:
      - Latest financial news filtered by company/symbol
      - Historical news archive for trend analysis
      - News sentiment scoring using NLP techniques
      - Event categorization (earnings, M&A, regulatory, etc.)
      - Source credibility weighting and duplicate removal

      Sentiment Analysis Features:
      - Keyword extraction from headlines and content
      - Positive/negative sentiment classification
      - Impact scoring based on news source and recency
      - Trend analysis of sentiment over time
      - Correlation with stock price movements

      NOTION DATABASE DESIGN:
      Investment Research Database:
      Primary Properties:
      - Stock Symbol (title) - Ticker symbol for the security
      - Company Name (text) - Full company name
      - Research Date (date) - When research was conducted
      - Current Price (number) - Latest stock price
      - Price Change % (number) - Daily price change percentage
      - Market Cap (text) - Market capitalization
      - Volume (number) - Trading volume

      Technical Analysis Properties:
      - RSI (number) - Relative Strength Index value
      - MACD Signal (select: Bullish, Bearish, Neutral)
      - Moving Average Trend (select: Uptrend, Downtrend, Sideways)
      - Support Level (number) - Key support price level
      - Resistance Level (number) - Key resistance price level
      - Technical Rating (select: Strong Buy, Buy, Neutral, Sell, Strong Sell)

      Fundamental Analysis Properties:
      - P/E Ratio (number) - Price-to-earnings ratio
      - P/B Ratio (number) - Price-to-book ratio
      - Debt/Equity (number) - Debt-to-equity ratio
      - ROE (number) - Return on equity percentage
      - Revenue Growth % (number) - Year-over-year revenue growth
      - EPS Growth % (number) - Earnings per share growth

      Analyst and News Properties:
      - Analyst Rating (select: Strong Buy, Buy, Hold, Sell, Strong Sell)
      - Average Price Target (number) - Consensus price target
      - Price Target High (number) - Highest analyst target
      - Price Target Low (number) - Lowest analyst target
      - News Sentiment (select: Very Positive, Positive, Neutral, Negative, Very Negative)
      - Key News Headlines (rich text) - Important recent headlines

      Research Analysis Properties:
      - Technical Analysis (rich text) - Detailed technical analysis summary
      - Fundamental Analysis (rich text) - Company and financial analysis
      - Investment Thesis (rich text) - Overall investment rationale
      - Risk Factors (rich text) - Key risks and concerns
      - Investment Recommendation (rich text) - Buy/Hold/Sell recommendation
      - Risk Assessment (select: Low, Medium, High, Very High)
      - Research Status (select: New, In Progress, Completed, Archived)

      RESEARCH WORKFLOW AUTOMATION:
      1. Stock Symbol Validation and Company Lookup
         - Validate ticker symbol format and existence
         - Fetch basic company information and sector classification
         - Check market hours and trading status

      2. Real-Time Data Collection
         - Get current stock price, volume, and market data
         - Fetch historical price data for technical analysis
         - Calculate price performance over multiple timeframes

      3. Technical Analysis Computation
         - Calculate RSI with overbought/oversold signals
         - Compute MACD with signal line crossovers and histogram
         - Generate moving average trends and crossover signals
         - Identify support and resistance levels
         - Analyze volume patterns and confirmation signals

      4. Fundamental Data Analysis
         - Retrieve company financial statements and key ratios
         - Analyze profitability, liquidity, and leverage metrics
         - Compare valuation multiples to sector averages
         - Assess earnings quality and growth sustainability
         - Evaluate dividend policy and shareholder returns

      5. News and Sentiment Analysis
         - Collect recent news articles related to the company
         - Perform sentiment analysis on headlines and content
         - Categorize news by type (earnings, guidance, M&A, etc.)
         - Weight sentiment by source credibility and recency
         - Identify potential catalysts and risk factors

      6. Analyst Consensus Integration
         - Fetch analyst ratings and recommendation changes
         - Calculate consensus price targets and revision trends
         - Analyze estimate revisions and earnings surprises
         - Compare analyst sentiment to technical/fundamental signals

      7. Comprehensive Report Generation
         - Create structured Notion page with all analysis
         - Generate executive summary with key findings
         - Provide detailed technical and fundamental analysis
         - Include risk assessment and investment recommendation
         - Add supporting charts, data tables, and news summaries

      ADVANCED FEATURES:
      Portfolio Integration:
      - Track multiple stocks in a portfolio context
      - Calculate portfolio-level risk and correlation metrics
      - Monitor sector allocation and diversification
      - Generate portfolio-level research summaries

      Alert System:
      - Price target alerts and technical indicator signals
      - News-based alerts for significant events
      - Earnings date and analyst revision notifications
      - Technical pattern recognition alerts

      Historical Analysis:
      - Track research accuracy and recommendation performance
      - Analyze prediction success rates over time
      - Identify patterns in successful vs. unsuccessful calls
      - Provide backtesting capabilities for research strategies

      ERROR HANDLING AND RELIABILITY:
      - Comprehensive error handling with meaningful messages
      - Retry mechanisms for API failures with exponential backoff
      - Data validation and sanitization for all inputs
      - Graceful degradation when data sources are unavailable
      - Caching strategies to reduce API calls and improve performance
      - Rate limiting compliance for all integrated APIs

      ENVIRONMENT REQUIREMENTS:
      - PICA_API_KEY for Pica integration
      - TWELVE_DATA_CONNECTION_KEY for market data access
      - NEWS_DATA_IO_CONNECTION_KEY for news and sentiment data
      - NOTION_CONNECTION_KEY for database operations
      - OPENAI_API_KEY for advanced NLP and analysis (optional)

      The MCP server should be production-ready with proper TypeScript types, comprehensive error handling, detailed logging, and optimized for both individual stock research and batch processing of multiple securities.
      ```

      <Note>The MCP server provides institutional-grade investment research capabilities with comprehensive data integration and analysis.</Note>
    </Card>
  </Tab>
</Tabs>

## Benefits

<CardGroup cols={2}>
  <Card title="Data-Driven Decisions" icon="chart-line">
    **Comprehensive market analysis**

    Real-time stock data, technical indicators, and sentiment analysis for informed investment decisions
  </Card>

  <Card title="Time Efficiency" icon="clock">
    **90% faster research process**

    Automate data collection, news gathering, and analysis that typically takes hours
  </Card>

  <Card title="Organized Research" icon="folder">
    **Centralized research hub**

    All investment research stored in structured Notion pages with searchable data
  </Card>

  <Card title="Real-Time Intelligence" icon="bolt">
    **Live market insights**

    Access to real-time quotes, breaking news, and up-to-date analyst recommendations
  </Card>
</CardGroup>

## Advanced Research Capabilities

<CardGroup cols={3}>
  <Card title="Technical Analysis" icon="chart-candlestick">
    * RSI and MACD indicators
    * Moving averages and trend analysis
    * Support and resistance levels
    * Momentum oscillators
  </Card>

  <Card title="Fundamental Data" icon="building">
    * Company financials and ratios
    * Earnings data and estimates
    * Dividend history and yield
    * Market capitalization metrics
  </Card>

  <Card title="Market Sentiment" icon="newspaper">
    * Real-time financial news
    * Analyst recommendations
    * Price target consensus
    * Social sentiment analysis
  </Card>
</CardGroup>

## Expand Your Investment Tools

Ready to build more financial automation? Explore these additional integrations:

<CardGroup cols={2}>
  <Card title="Portfolio Tracking" icon="briefcase">
    Connect with brokerage APIs for real-time portfolio monitoring and performance analysis
  </Card>

  <Card title="Alert System" icon="bell">
    Set up Slack or email notifications for price alerts, earnings announcements, and news events
  </Card>

  <Card title="Risk Management" icon="shield">
    Integrate with risk assessment tools for position sizing and portfolio diversification analysis
  </Card>

  <Card title="Backtesting" icon="history">
    Historical data analysis for strategy backtesting and performance evaluation
  </Card>
</CardGroup>

🚀 **Ready for more?** Browse our catalog of 25,000+ actions across 200+ integrations to expand your investment research pipeline!

[Explore All Integrations →](https://app.picaos.com/tools)


Built with [Mintlify](https://mintlify.com).