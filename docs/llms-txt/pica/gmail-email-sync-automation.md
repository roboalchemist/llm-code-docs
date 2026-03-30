# Source: https://docs.picaos.com/use-cases/gmail-email-sync-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.picaos.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build a Gmail Email Sync Automation

> 🚀 Create an automated Gmail email sync system that runs every hour using AuthKit for secure multi-tenant authentication and BuildKit MCP for email processing, storing emails in Supabase for scalable data management.

export const AddConnections = ({platforms}) => {
  if (!platforms) return null;
  return <>
      {platforms.map(platform => <Columns cols={1}>
          <Card title={`Add ${platform.name} Connection`} href={`https://app.picaos.com/connections#open=${platform.code}`} arrow="true" key={platform.code}>
          </Card>
        </Columns>)}
    </>;
};

export const platformNames_1 = "Gmail accounts through AuthKit"

export const Header = ({size, text}) => {
  const Tag = `h${size}`;
  return <Tag>{text}</Tag>;
};

export const platformNames_0 = "Gmail and Supabase accounts with AuthKit integration"

export const projectType_0 = "Next.js with BuildKit MCP"

### What we'll do

1. Install the Pica MCP Server.
2. Connect your {platformNames_0}.
3. Set up a starter {projectType_0} project.
4. Add some rules for the LLMs to understand BuildKit.
5. Prompt the LLM to build your tool.

## Architecture Overview

This tutorial demonstrates a production-ready Gmail email sync system that:

* **Authenticates users** via AuthKit's secure multi-tenant OAuth flow
* **Syncs emails hourly** using cron jobs or scheduled functions
* **Stores data** in Supabase for scalable, real-time access
* **Processes emails** through BuildKit MCP server for AI-powered analysis

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

## Required Environment Variables

You'll need these keys in your environment:

```bash Environment Setup theme={null}
# Pica Configuration
PICA_SECRET_KEY=your_pica_secret_key

# Supabase Configuration  
SUPABASE_URL=your_supabase_project_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key

# Application Configuration
NEXTAUTH_SECRET=your_nextauth_secret
NEXTAUTH_URL=http://localhost:3000
```

## AuthKit Integration Setup

### 1. Install Dependencies

```bash Package Installation theme={null}
npm install @picahq/authkit-token @picahq/authkit
npm install @supabase/supabase-js
npm install node-cron
npm install @modelcontextprotocol/sdk
```

### 2. Supabase Database Schema

```sql Database Schema theme={null}
-- Create emails table
CREATE TABLE emails (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id TEXT NOT NULL,
  connection_key TEXT NOT NULL,
  message_id TEXT UNIQUE NOT NULL,
  thread_id TEXT,
  subject TEXT,
  sender TEXT,
  recipient TEXT,
  body TEXT,
  snippet TEXT,
  labels TEXT[],
  is_unread BOOLEAN DEFAULT false,
  received_date TIMESTAMPTZ,
  processed_at TIMESTAMPTZ DEFAULT NOW(),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create sync_status table for tracking
CREATE TABLE sync_status (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id TEXT NOT NULL,
  connection_key TEXT NOT NULL,
  last_sync_at TIMESTAMPTZ,
  next_sync_at TIMESTAMPTZ,
  emails_synced INTEGER DEFAULT 0,
  status TEXT DEFAULT 'active',
  error_message TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create indexes for performance
CREATE INDEX idx_emails_user_id ON emails(user_id);
CREATE INDEX idx_emails_message_id ON emails(message_id);
CREATE INDEX idx_emails_received_date ON emails(received_date DESC);
CREATE INDEX idx_sync_status_user_id ON sync_status(user_id);
CREATE INDEX idx_sync_status_next_sync ON sync_status(next_sync_at);

-- Enable Row Level Security
ALTER TABLE emails ENABLE ROW LEVEL SECURITY;
ALTER TABLE sync_status ENABLE ROW LEVEL SECURITY;

-- Create RLS policies
CREATE POLICY "Users can only access their own emails" ON emails
  FOR ALL USING (auth.jwt() ->> 'sub' = user_id);

CREATE POLICY "Users can only access their own sync status" ON sync_status
  FOR ALL USING (auth.jwt() ->> 'sub' = user_id);
```

### 3. AuthKit Button Component

```tsx Component: components/AuthKitButton.tsx theme={null}
'use client';

import { useAuthKit } from "@picahq/authkit";
import { useState } from "react";

interface AuthKitButtonProps {
  userId: string;
  onConnectionSuccess?: (connection: any) => void;
}

export function AuthKitButton({ userId, onConnectionSuccess }: AuthKitButtonProps) {
  const [isConnecting, setIsConnecting] = useState(false);

  const { open } = useAuthKit({
    token: {
      url: "/api/authkit",
      headers: {},
      body: { userId },
    },
    onSuccess: (connection) => {
      console.log("Successfully created connection:", connection);
      setIsConnecting(false);
      onConnectionSuccess?.(connection);
    },
    onError: (error) => {
      console.error("Error creating connection:", error);
      setIsConnecting(false);
    },
    onClose: () => {
      console.log("AuthKit modal closed");
      setIsConnecting(false);
    },
  });

  const handleConnect = () => {
    setIsConnecting(true);
    open();
  };

  return (
    <button
      onClick={handleConnect}
      disabled={isConnecting}
      className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
    >
      {isConnecting ? "Connecting..." : "Connect Gmail"}
    </button>
  );
}
```

## System Implementation

The system consists of several key components working together for automated Gmail email synchronization.

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

### First, discover the Gmail and Supabase actions available in Pica

Before building the Gmail email sync system, discover the available actions using Pica MCP:

<Card>
  ```markdown Action Discovery via Pica MCP theme={null}
  # Discovery Phase: Gmail & Supabase Actions via Pica MCP

  I need to discover the available Gmail and Supabase actions through Pica MCP before building the email sync system. Help me:

  1. **List Gmail Platform Actions**: Use Pica MCP to discover all available Gmail actions
  2. **List Supabase Platform Actions**: Use Pica MCP to discover all available Supabase actions  
  3. **Get Action Knowledge**: Fetch detailed documentation for the actions I need
  4. **Build Implementation**: Create the email sync system using the discovered action IDs

  DISCOVERED GMAIL ACTIONS:
  - **List User Messages**: `conn_mod_def::F_JeIVCQAiA::oD2p47ZVSHu1tF_maldXVQ`
  - **Get Gmail Message**: `conn_mod_def::F_JeIErCKGA::Q2ivQ5-QSyGYiEIZT867Dw`

  DISCOVERED SUPABASE ACTIONS:
  - **Run SQL Query**: `conn_mod_def::GC40SckOddE::NFFu2-49QLyGsPBdfweitg`
  - **List All Projects**: `conn_mod_def::GC40U5B8xKY::_N0C5lBNSoWseIxyeQs1KQ`

  These action IDs will be used in the implementation below for Gmail and Supabase integration via Pica passthrough.
  ```
</Card>

### Prompt the LLM to build your tool

#### Vercel AI SDK

Copy this prompt to build the Vercel AI SDK email sync system:

```markdown Vercel AI SDK Agent Prompt expandable theme={null}
# Vercel AI SDK Agent Prompt (Gmail Email Sync Automation)

Create a comprehensive Vercel AI SDK agent for automated Gmail email synchronization using Pica integrations. The agent should sync emails to Supabase database every hour with full multi-tenant support.

TOOLS NEEDED:
1. fetchGmailEmails - Fetch Gmail emails using Pica Gmail integration (List Messages + Get Message details)
2. storeEmailsSupabase - Store emails in Supabase database using Pica SQL query execution
3. setupEmailSync - Initialize email sync configuration for a user with connection details
4. syncUserEmails - Complete email sync workflow combining fetch and store operations
5. getEmailInsights - Analyze email patterns and generate insights using stored email data
6. updateSyncStatus - Track sync performance and schedule next sync using Supabase
7. handleSyncErrors - Manage failed syncs with retry logic and error logging

SUPABASE DATABASE STRUCTURE (Single Database Approach):
Use Pica Supabase integration to create and manage these tables via SQL queries:

Main Table: "emails" 
- id (uuid, primary key)
- user_id (text) - for multi-tenant RLS
- connection_key (text) - Gmail connection identifier
- message_id (text, unique) - Gmail message ID
- thread_id (text) - Gmail thread ID
- subject (text)
- sender (text)
- recipient (text) 
- body (text) - email content
- snippet (text) - Gmail snippet
- labels (jsonb) - Gmail labels array
- is_unread (boolean)
- received_date (timestamptz)
- created_at (timestamptz, default now())

Sync Status Table: "sync_status"
- user_id (text, primary key)
- connection_key (text)
- last_sync_at (timestamptz)
- next_sync_at (timestamptz)
- emails_synced (integer)
- status (text: active, paused, error)
- error_message (text, nullable)
- updated_at (timestamptz)

WORKFLOW:
1. Setup user email sync with Gmail connection key from AuthKit
2. Fetch recent Gmail messages using Pica Gmail List Messages action
3. Get full email details for each message using Pica Gmail Get Message action  
4. Store emails in Supabase using Pica SQL query execution with UPSERT for deduplication
5. Update sync status and schedule next sync (1 hour interval)
6. Handle errors gracefully with retry logic and status updates
7. Generate email insights and analytics from synchronized data

ENVIRONMENT VARIABLES NEEDED:
- GMAIL_CONNECTION_KEY (from AuthKit Gmail connection)
- SUPABASE_CONNECTION_KEY (from Pica Supabase integration)
- PICA_API_KEY

TOOL IMPLEMENTATION APPROACH:
Use Pica integrations for ALL external API calls:
- Gmail operations via Pica Gmail actions (no direct Gmail API calls)
- Supabase operations via Pica SQL query action (no Supabase client library)
- Let Pica handle OAuth tokens, rate limiting, and error handling
- Focus on business logic and workflow orchestration

ERROR HANDLING STRATEGY:
- Use Pica's built-in retry mechanisms and error handling
- Store sync errors in Supabase for monitoring and recovery
- Implement exponential backoff for failed sync attempts
- Provide detailed error messages for troubleshooting

SYNC SCHEDULING:
- Set next_sync_at to 1 hour from successful sync completion
- Support manual sync triggers for immediate synchronization
- Handle overlapping syncs by checking sync status before starting
- Provide sync statistics and performance monitoring

Make the system intelligent enough to:
- Detect and skip duplicate emails using Gmail message IDs
- Handle Gmail API rate limits through Pica's rate limiting
- Process large inboxes efficiently with pagination
- Provide real-time sync progress updates
- Generate email analytics and insights from synchronized data
```

<Note>The system uses Pica for all Gmail and Supabase operations, eliminating the need for complex OAuth and API management code.</Note>

#### LangChain

Copy this prompt to build the LangChain email sync tools:

```markdown LangChain Email Sync Tools expandable theme={null}
# LangChain Gmail Email Sync Tools

Create a comprehensive LangChain tool suite for automated Gmail email synchronization using Pica integrations for both Gmail and Supabase operations.

CORE TOOLS:
1. GmailEmailFetcher - LangChain tool that fetches Gmail emails via Pica Gmail actions
2. SupabaseEmailStore - Tool that stores emails in Supabase via Pica SQL query action
3. EmailSyncOrchestrator - Tool that coordinates complete email sync workflow
4. SyncStatusManager - Tool that tracks and updates sync status using Pica Supabase integration
5. EmailAnalyzer - Tool that analyzes email patterns and generates insights
6. ErrorRecoveryHandler - Tool that manages sync failures and retry logic
7. PerformanceMonitor - Tool that tracks sync performance and generates reports

LANGCHAIN IMPLEMENTATION REQUIREMENTS:
- Use LangChain's tool decorator and structured input/output schemas
- Implement proper error handling with LangChain's error types
- Use LangChain's memory system to track sync state across operations
- Integrate with LangChain agents for workflow orchestration
- Support streaming responses for real-time sync progress updates

PICA INTEGRATION PATTERN:
All external API calls should go through Pica:

Gmail Operations:
- List Messages: Use action ID `conn_mod_def::F_JeIVCQAiA::oD2p47ZVSHu1tF_maldXVQ`
- Get Message: Use action ID `conn_mod_def::F_JeIErCKGA::Q2ivQ5-QSyGYiEIZT867Dw`

Supabase Operations:  
- Run SQL Query: Use action ID `conn_mod_def::GC40SckOddE::NFFu2-49QLyGsPBdfweitg`

EMAIL SYNC WORKFLOW:
1. **Initialize Sync**: Check sync status and prepare for new sync cycle
2. **Fetch Gmail Data**: Get email list and detailed content via Pica Gmail actions
3. **Process Emails**: Parse and structure email data for storage
4. **Store in Supabase**: Execute SQL queries via Pica to insert/update emails
5. **Update Status**: Record sync results and schedule next sync
6. **Generate Insights**: Analyze email patterns and create reports
7. **Error Handling**: Manage failures and implement recovery strategies

SIMPLIFIED DATABASE DESIGN:
Single database approach with embedded metadata:
- Main emails table with all email data and metadata
- Sync status tracking table for managing sync schedules
- No complex relationships - everything in primary tables
- Use JSON columns for flexible metadata storage

EMAIL CATEGORIZATION AND INSIGHTS:
- Detect email types: promotional, personal, work, newsletters
- Identify important senders and frequent contacts  
- Track email volume patterns and peak times
- Generate email health reports (inbox zero metrics, response times)
- Provide search and filtering capabilities across synchronized emails

AUTOMATED SCHEDULING:
- Set up hourly sync cycles using sync_status table
- Support different sync frequencies for different users
- Handle sync conflicts and overlapping operations
- Provide manual sync triggers for immediate updates

PERFORMANCE OPTIMIZATION:
- Use UPSERT operations to avoid duplicate emails
- Implement incremental sync based on last sync timestamp
- Batch email processing for large inboxes
- Use Pica's built-in rate limiting and retry mechanisms

Use Pica integrations for all Gmail and Supabase operations. This eliminates the need for managing OAuth tokens, API clients, and rate limiting - Pica handles all of that complexity.
```

<Note>The LangChain tools leverage Pica's Gmail and Supabase integrations for simplified, reliable email synchronization without complex API management.</Note>

#### MCP Server

Copy this prompt to build the MCP server:

````markdown MCP Email Sync Server expandable theme={null}
# Complete MCP Gmail Email Sync Server

Create a complete MCP (Model Context Protocol) server for automated Gmail email synchronization using Pica integrations for Gmail and Supabase operations. The server should provide a comprehensive email sync solution with minimal custom code.

MCP SERVER STRUCTURE:
- Server name: "gmail-email-sync-server"
- Version: "1.0.0"
- Description: "MCP server for automated Gmail email synchronization via Pica integrations"

TOOLS TO IMPLEMENT:
1. discover_pica_actions - Discover available Gmail and Supabase actions via Pica MCP
2. setup_email_sync - Initialize email sync for a user with connection configuration
3. fetch_gmail_emails - Retrieve Gmail emails via Pica Gmail integration
4. store_emails_supabase - Save emails to Supabase via Pica SQL query execution
5. sync_user_emails - Complete email sync workflow (fetch + store + status update)
6. get_sync_status - Check current sync status and schedule information
7. update_sync_schedule - Modify sync frequency and scheduling parameters
8. analyze_email_data - Generate insights from synchronized email data
9. handle_sync_recovery - Recover from failed syncs with retry mechanisms

PICA INTEGRATION APPROACH:
The server should use Pica for ALL external operations:

Gmail Integration:
- No direct Gmail API calls or OAuth management
- Use Pica Gmail actions for all email operations
- Leverage Pica's rate limiting and error handling

Supabase Integration:
- No Supabase client library or direct database connections
- All database operations via Pica SQL query action
- Use Pica for connection management and error handling

Benefits:
- Eliminates OAuth token management complexity
- Built-in rate limiting and retry mechanisms  
- Unified error handling across all integrations
- Simplified deployment without multiple API configurations

DATABASE SCHEMA (via Pica SQL Queries):
Create these tables using Pica Supabase SQL query action:

```sql
-- Emails table for storing synchronized Gmail data
CREATE TABLE emails (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id TEXT NOT NULL,
  connection_key TEXT NOT NULL,
  message_id TEXT UNIQUE NOT NULL,
  thread_id TEXT,
  subject TEXT,
  sender TEXT,
  recipient TEXT,
  body TEXT,
  snippet TEXT,
  labels JSONB DEFAULT '[]',
  is_unread BOOLEAN DEFAULT false,
  received_date TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Sync status table for managing sync schedules and performance
CREATE TABLE sync_status (
  user_id TEXT PRIMARY KEY,
  connection_key TEXT NOT NULL,
  last_sync_at TIMESTAMPTZ,
  next_sync_at TIMESTAMPTZ,
  emails_synced INTEGER DEFAULT 0,
  total_emails INTEGER DEFAULT 0,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'paused', 'error')),
  error_message TEXT,
  sync_frequency_hours INTEGER DEFAULT 1,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable RLS for multi-tenant security
ALTER TABLE emails ENABLE ROW LEVEL SECURITY;
ALTER TABLE sync_status ENABLE ROW LEVEL SECURITY;
````

SYNC WORKFLOW IMPLEMENTATION:

1. **Discovery Phase**: Use Pica MCP to discover Gmail and Supabase actions
2. **Connection Setup**: Initialize Gmail connection via AuthKit and Supabase connection
3. **Email Fetching**: Retrieve Gmail messages using discovered Pica Gmail actions
4. **Data Processing**: Parse email content and prepare for database storage
5. **Database Storage**: Execute SQL queries via Pica to store emails with deduplication
6. **Status Management**: Update sync status and schedule next sync cycle
7. **Error Handling**: Manage failures with automatic retry and recovery

AUTOMATED SCHEDULING STRATEGY:

* Default 1-hour sync intervals with configurable frequency
* Use sync\_status table to track next sync time
* Support priority syncs for active users or error recovery
* Implement sync conflict detection to avoid overlapping operations
* Provide manual sync triggers for immediate synchronization

EMAIL ANALYTICS AND INSIGHTS:
Generate insights from synchronized email data:

* Email volume trends and patterns
* Top senders and frequent contacts
* Unread email management and inbox health
* Response time analysis and email habits
* Custom filters and search capabilities

ERROR HANDLING AND RECOVERY:

* Leverage Pica's built-in error handling and retry mechanisms
* Log sync errors with detailed context for troubleshooting
* Implement exponential backoff for failed sync attempts
* Provide error recovery tools for manual intervention
* Monitor sync performance and alert on consistent failures

DEPLOYMENT CONSIDERATIONS:

* Minimal environment variables (PICA\_API\_KEY and connection keys)
* No complex OAuth setup or API client configurations
* Simplified Docker deployment with Pica handling external integrations
* Health checks and monitoring endpoints for production use
* Scaling support through Pica's infrastructure capabilities

The MCP server should be production-ready with comprehensive error handling, automated scheduling, and detailed logging. The Pica integration approach eliminates most of the complexity typically associated with multi-API integrations.

```

<Note>The MCP server uses Pica integrations exclusively, eliminating the need for complex OAuth, API client management, and rate limiting code.</Note>
```

## Benefits

<CardGroup cols={2}>
  <Card title="Multi-Tenant Security" icon="shield-check">
    **Enterprise-grade authentication**

    AuthKit handles OAuth flows, token management, and secure multi-tenant access
  </Card>

  <Card title="Automated Sync" icon="clock">
    **Hourly email synchronization**

    Background processes ensure your application always has the latest email data
  </Card>

  <Card title="Scalable Storage" icon="database">
    **Supabase real-time database**

    PostgreSQL-powered storage with RLS security and real-time subscriptions
  </Card>

  <Card title="AI-Ready Processing" icon="cpu-chip">
    **BuildKit MCP integration**

    Process emails through AI agents for classification, sentiment analysis, and automation
  </Card>
</CardGroup>

## Advanced Features

<CardGroup cols={3}>
  <Card title="Real-time Updates" icon="bolt">
    * WebSocket connections for live email updates
    * Instant notification system
    * Progressive sync with conflict resolution
  </Card>

  <Card title="Smart Processing" icon="brain">
    * AI-powered email classification
    * Sentiment analysis and priority scoring
    * Automated response generation
  </Card>

  <Card title="Enterprise Scale" icon="building-office">
    * Multi-tenant architecture
    * Rate limiting and error handling
    * Comprehensive audit logging
  </Card>
</CardGroup>

## Expand Your Email Automation

Ready to build more email integrations? Explore these additional capabilities:

<CardGroup cols={2}>
  <Card title="Outlook Integration" icon="envelope">
    Add Microsoft 365 and Outlook.com email sync with the same AuthKit flow
  </Card>

  <Card title="Slack Notifications" icon="chat-bubble-left">
    Send real-time notifications to Slack channels for important emails
  </Card>

  <Card title="AI Email Assistant" icon="sparkles">
    Build intelligent email responses and automated workflows with LLM integration
  </Card>

  <Card title="Analytics Dashboard" icon="chart-bar">
    Create comprehensive email analytics and insights for business intelligence
  </Card>
</CardGroup>

🚀 **Ready for more?** Browse our catalog of 25,000+ actions across 200+ integrations to expand your email automation pipeline!

[Explore All Integrations →](https://app.picaos.com/tools)


Built with [Mintlify](https://mintlify.com).