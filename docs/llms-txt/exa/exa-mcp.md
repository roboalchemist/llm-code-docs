# Source: https://docs.exa.ai/reference/exa-mcp.md

# Exa MCP

[![Install in Cursor](https://img.shields.io/badge/Install_in-Cursor-000000?style=flat-square\&logoColor=white)](https://cursor.com/en/install-mcp?name=exa\&config=eyJuYW1lIjoiZXhhIiwidHlwZSI6Imh0dHAiLCJ1cmwiOiJodHRwczovL21jcC5leGEuYWkvbWNwIn0=)
[![Install in VS Code](https://img.shields.io/badge/Install_in-VS_Code-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=exa\&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.exa.ai%2Fmcp%22%7D)

### exa-code: fast and efficient web context for coding agents

Vibe coding should never have a bad vibe. `exa-code` is a huge step towards coding agents that never hallucinate.

When your coding agent makes a search query, `exa-code` searches over billions of GitHub repos, docs pages, StackOverflow posts, and more to find the perfect, token-efficient context that the agent needs to code correctly. It's powered by the Exa search engine.

Examples of queries you can make with `exa-code`:

* use Exa search in python and make sure content is always livecrawled
* use correct syntax for vercel ai sdk to call gpt-5 nano asking it how are you

**Works with Cursor and Claude Code!** Use the HTTP-based configuration format:

```json  theme={null}
{
  "mcpServers": {
    "exa": {
      "type": "http",
      "url": "https://mcp.exa.ai/mcp",
      "headers": {}
    }
  }
}
```

Installing Exa MCP like below will install Exa web search as well as `exa-code`. To maximize performance, be sure to leave *only* `exa-code` turned on in your MCP client.

***

Exa MCP Server enables AI assistants like Claude to perform real-time web searches through the Exa Search API, allowing them to access up-to-date information from the internet. It is open-source, check out [GitHub](https://github.com/exa-labs/exa-mcp-server/).

## Remote Exa MCP

Connect directly to Exa's hosted MCP server using this URL:

```
https://mcp.exa.ai/mcp
```

You can enable specific tool(s) using the `tools` parameter (if multiple, then with a comma-separated list):

```
https://mcp.exa.ai/mcp?tools=web_search_exa,get_code_context_exa
```

Or enable all tools:

```
https://mcp.exa.ai/mcp?tools=web_search_exa,get_code_context_exa,crawling_exa,company_research_exa,linkedin_search_exa,deep_researcher_start,deep_researcher_check
```

You may include your exa api key in the url like this:

```
https://mcp.exa.ai/mcp?exaApiKey=YOUREXAKEY
```

**Note:** By default, only `web_search_exa` and `get_code_context_exa` are enabled. Add other tools as needed using the `tools` parameter.

### Claude Desktop Configuration for Remote MCP

Add this to your Claude Desktop configuration file:

```json  theme={null}
{
  "mcpServers": {
    "exa": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.exa.ai/mcp"
      ]
    }
  }
}
```

### Cursor and Claude Code Configuration for Remote MCP

For Cursor and Claude Code, use this HTTP-based configuration format:

```json  theme={null}
{
  "mcpServers": {
    "exa": {
      "type": "http",
      "url": "https://mcp.exa.ai/mcp",
      "headers": {}
    }
  }
}
```

Replace the above link to this to enable all tools:

```
https://mcp.exa.ai/mcp?tools=web_search_exa,get_code_context_exa,crawling_exa,company_research_exa,linkedin_search_exa,deep_researcher_start,deep_researcher_check
```

## Available Tools

**Note:** By default, only `web_search_exa` and `get_code_context_exa` are enabled. You can enable additional tools using the `tools` parameter (see examples below).

Exa MCP includes several specialized search tools:

| Tool                       | Description                                                                                                                                                                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`get_code_context_exa`** | **NEW!** Search and get relevant code snippets, examples, and documentation from open source libraries, GitHub repositories, and programming frameworks. Perfect for finding up-to-date code documentation, implementation examples, API usage patterns, and best practices from real codebases |
| `web_search_exa`           | Performs real-time web searches with optimized results and content extraction                                                                                                                                                                                                                   |
| `deep_researcher_start`    | Start a smart AI researcher for complex questions. The AI will search the web, read many sources, and think deeply about your question to create a detailed research report                                                                                                                     |
| `deep_researcher_check`    | Check if your research is ready and get the results. Use this after starting a research task to see if it's done and get your comprehensive report                                                                                                                                              |
| `company_research`         | Comprehensive company research tool that crawls company websites to gather detailed information about businesses                                                                                                                                                                                |
| `crawling`                 | Extracts content from specific URLs, useful for reading articles, PDFs, or any web page when you have the exact URL                                                                                                                                                                             |
| `linkedin_search`          | Search LinkedIn for companies and people using Exa AI. Simply include company names, person names, or specific LinkedIn URLs in your query                                                                                                                                                      |

## Usage Examples

Once configured, you can ask Claude to perform searches:

### Code Search Examples

* "Show me how to use React hooks with TypeScript"
* "Find examples of how to implement authentication with NextJS"
* "Get documentation and examples for the pandas library"

### Other Search Examples

* "Research the company exa.ai and find information about their pricing"
* "Start a deep research project on the impact of artificial intelligence on healthcare, then check when it's complete to get a comprehensive report"

## Local Installation

### Using Claude Code

The quickest way to set up Exa MCP is using Claude Code:

```bash  theme={null}
claude mcp add exa -e EXA_API_KEY=YOUR_API_KEY -- npx -y exa-mcp-server
```

Replace `YOUR_API_KEY` with your Exa API key from above.

## Configuring Claude Desktop

To configure Claude Desktop to use Exa MCP:

1. **Enable Developer Mode in Claude Desktop**
   * Open Claude Desktop
   * Click on the top-left menu
   * Enable Developer Mode

2. **Open the Configuration File**

   * After enabling Developer Mode, go to Settings
   * Navigate to the Developer Option
   * Click "Edit Config" to open the configuration file

   Alternatively, you can open it directly:

   **macOS:**

   ```bash  theme={null}
   code ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

   **Windows:**

   ```powershell  theme={null}
   code %APPDATA%\Claude\claude_desktop_config.json
   ```

3. **Add Exa MCP Configuration**

   Add the following to your configuration:

   ```json  theme={null}
   {
     "mcpServers": {
       "exa": {
         "command": "npx",
         "args": [
           "-y",
          "exa-mcp-server"
          ],
         "env": {
           "EXA_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

   Replace `your-api-key-here` with your actual Exa API key.

4. **Enabling Specific Tools**

   To enable only code search (recommended for developers):

   ```json  theme={null}
   {
     "mcpServers": {
       "exa": {
         "command": "npx",
         "args": [
           "-y",
           "exa-mcp-server",
           "tools=get_code_context_exa"
         ],
         "env": {
           "EXA_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

   To enable code search and web search together:

   ```json  theme={null}
   {
     "mcpServers": {
       "exa": {
         "command": "npx",
         "args": [
           "-y",
           "exa-mcp-server",
           "tools=get_code_context_exa,web_search_exa"
         ],
         "env": {
           "EXA_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

   To enable all tools:

   ```json  theme={null}
   {
     "mcpServers": {
       "exa": {
         "command": "npx",
         "args": [
           "-y",
           "exa-mcp-server",
           "tools=web_search_exa,get_code_context_exa,crawling_exa,company_research_exa,linkedin_search_exa,deep_researcher_start,deep_researcher_check"
         ],
         "env": {
           "EXA_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

### Using NPX

The simplest way to install and run Exa MCP is via NPX:

```bash  theme={null}
# Install globally
npm install -g exa-mcp-server

# Or run directly with npx
npx exa-mcp-server
```

To specify which tools to enable:

```bash  theme={null}
# Run with default tools only (web_search_exa and get_code_context_exa)
npx exa-mcp-server

# Enable specific tools only
npx exa-mcp-server tools=web_search_exa

# All tools
npx exa-mcp-server tools=web_search_exa,get_code_context_exa,crawling_exa,company_research_exa,linkedin_search_exa,deep_researcher_start,deep_researcher_check
```

## Additional Resources

For more information, visit the [Exa MCP Server GitHub repository](https://github.com/exa-labs/exa-mcp-server/).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt