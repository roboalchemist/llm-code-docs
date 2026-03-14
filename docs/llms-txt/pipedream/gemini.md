# Source: https://pipedream.com/docs/connect/mcp/ai-frameworks/gemini.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pipedream MCP with Gemini

> Use Pipedream MCP with Google Gemini

<Note>
  Make sure to complete the [setup steps](/connect/mcp/developers#prerequisites) before continuing.
</Note>

<Card title="Try Gemini Agent" horizontal href="https://github.com/philschmid/gemini-samples/blob/main/scripts/gemini-mcp-pipedream.py">
  Check out the Gemini Agent built by the Gemini team, featured [here](https://x.com/_philschmid/status/1948025573403492621)
</Card>

## Installation

<CodeGroup>
  ```bash JavaScript theme={null}
  npm install @google/generativeai @modelcontextprotocol/sdk @pipedream/sdk
  ```

  ```bash Python   theme={null}
  pip install google-genai fastmcp pipedream
  ```

</CodeGroup>

Set your Google API key:

```env  theme={null}
GOOGLE_API_KEY=your_google_api_key
```

## Basic Usage

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { GoogleGenerativeAI } from '@google/generativeai';
  import { Client } from '@modelcontextprotocol/sdk/client/index.js';
  import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
  import { PipedreamClient } from '@pipedream/sdk';

  // Environment variables
  const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY!;
  const PIPEDREAM_CLIENT_ID = process.env.PIPEDREAM_CLIENT_ID!;
  const PIPEDREAM_CLIENT_SECRET = process.env.PIPEDREAM_CLIENT_SECRET!;
  const PIPEDREAM_PROJECT_ID = process.env.PIPEDREAM_PROJECT_ID!;
  const PIPEDREAM_ENVIRONMENT = process.env.PIPEDREAM_ENVIRONMENT as 'development' | 'production';

  async function runGeminiWithMCP() {
    // Initialize Pipedream SDK client
    const pdClient = new PipedreamClient({
      projectEnvironment: PIPEDREAM_ENVIRONMENT,
      clientId: PIPEDREAM_CLIENT_ID,
      clientSecret: PIPEDREAM_CLIENT_SECRET,
      projectId: PIPEDREAM_PROJECT_ID
    });

    // Get access token for MCP authentication
    const accessToken = await pdClient.rawAccessToken;
    const externalUserId = 'user-123'; // Your user's unique ID
    const appSlug = 'gmail,google_calendar'; // Apps to use

    // Create MCP transport
    const transport = new StreamableHTTPClientTransport(
      new URL('https://remote.mcp.pipedream.net'),
      {
        requestInit: {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
            'x-pd-project-id': PIPEDREAM_PROJECT_ID,
            'x-pd-environment': PIPEDREAM_ENVIRONMENT,
            'x-pd-external-user-id': externalUserId,
            'x-pd-app-slug': appSlug,
          }
        }
      }
    );

    // Initialize MCP client
    const mcpClient = new Client({
      name: 'gemini-pipedream-client',
      version: '1.0.0',
    });

    await mcpClient.connect(transport);

    // Initialize Gemini client
    const genAI = new GoogleGenerativeAI(GOOGLE_API_KEY);
    
    try {
      // Get available tools from MCP
      const toolsResponse = await mcpClient.listTools();
      const mcpTools = toolsResponse.tools || [];

      // Convert MCP tools to Gemini function calling format
      const geminiTools = mcpTools.map((tool: any) => ({
        function_declarations: [{
          name: tool.name,
          description: tool.description,
          parameters: tool.inputSchema,
        }]
      }));

      // Create model with tools
      const model = genAI.getGenerativeModel({
        model: 'gemini-pro',
        tools: geminiTools,
        systemInstruction: `You are a helpful AI assistant with access to powerful tools.
        
  The current date is ${new Date().toISOString().split['T'](0)}.

  Use the available tools to help users accomplish their tasks effectively.
  If you encounter any errors, explain what happened and suggest alternatives.`
      });

      // Start chat
      const chat = model.startChat({
        history: [],
      });

      const userMessage = "Check my recent emails and summarize the important ones";
      console.log(`User: ${userMessage}`);

      // Send message and handle tool calls
      const result = await chat.sendMessage(userMessage);
      const response = await result.response;

      // Handle function calls if present
      if (response.functionCalls?.length > 0) {
        console.log('Executing tools...');
        
        const functionResults = [];
        
        for (const functionCall of response.functionCalls) {
          try {
            const result = await mcpClient.callTool({
              name: functionCall.name,
              arguments: functionCall.args,
            });
            
            functionResults.push({
              name: functionCall.name,
              response: result,
            });
            
            console.log(`✅ ${functionCall.name}: Success`);
          } catch (error) {
            console.error(`❌ ${functionCall.name}: ${error}`);
            functionResults.push({
              name: functionCall.name,
              response: { error: String(error) },
            });
          }
        }

        // Send function results back to Gemini
        const finalResult = await chat.sendMessage([{
          functionResponse: {
            name: functionResults[0].name,
            response: functionResults[0].response,
          }
        }]);

        console.log(`Gemini: ${finalResult.response.text()}`);
      } else {
        console.log(`Gemini: ${response.text()}`);
      }

    } finally {
      // Clean up MCP client
      await mcpClient.close();
    }
  }

  // Run the example
  runGeminiWithMCP().catch(console.error);

  ```

  ```python Python theme={null}
  import os
  import asyncio
  from datetime import datetime
  from google import genai
  from fastmcp import Client
  from pipedream import Pipedream

  async def run_gemini_with_mcp():
      # Initialize Pipedream client and get access token
      pd = Pipedream(
          project_id=os.environ.get('PIPEDREAM_PROJECT_ID'),
          project_environment=os.environ.get('PIPEDREAM_ENVIRONMENT'),
          client_id=os.environ.get('PIPEDREAM_CLIENT_ID'),
          client_secret=os.environ.get('PIPEDREAM_CLIENT_SECRET'),
      )
      
      access_token = await pd.raw_access_token
      
      # Initialize Gemini client
      client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

      # Initialize MCP client with Pipedream
      mcp_client = Client({
          "mcpServers": {
              "pipedream": {
                  "transport": "http",
                  "url": "https://remote.mcp.pipedream.net",
                  "headers": {
                      "Authorization": f"Bearer {access_token}",
                      "x-pd-project-id": os.environ.get('PIPEDREAM_PROJECT_ID'),
                      "x-pd-environment": os.environ.get('PIPEDREAM_ENVIRONMENT'),
                      "x-pd-external-user-id": "user-123",  # Your user's unique ID
                      "x-pd-app-slug": "gmail, google_calendar",  # Apps to use
                  },
              }
          }
      })

      async with mcp_client:
          # Configure Gemini with MCP tools and system instructions
          config = genai.types.GenerateContentConfig(
              temperature=0,
              tools=[mcp_client.session],
              system_instruction=f"""You are a helpful AI assistant with access to powerful tools.
              
  Very important: The user's timezone is {datetime.now().strftime("%Z")}. 
  The current date is {datetime.now().strftime("%Y-%m-%d")}.

  Use the available tools to help users accomplish their tasks effectively.
  If you encounter any errors, explain what happened and suggest alternatives.""",
          )

          # Create chat session
          chat = client.aio.chats.create(model="gemini-2.0-flash-exp", config=config)

          # Send user message
          user_message = "Check my recent emails and summarize the important ones"
          
          print(f"User: {user_message}")
          
          # Generate response with automatic tool calling
          response = await chat.send_message(user_message)
          
          print(f"Gemini: {response.text}")
          
          # Continue conversation if needed
          follow_up = "Can you schedule a meeting based on the most important email?"
          print(f"User: {follow_up}")
          
          response = await chat.send_message(follow_up)
          print(f"Gemini: {response.text}")

  if __name__ == "__main__":
      asyncio.run(run_gemini_with_mcp())
  ```

</CodeGroup>

Built with [Mintlify](https://mintlify.com).
