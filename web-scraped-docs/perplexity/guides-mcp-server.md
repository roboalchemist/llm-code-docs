# Source: https://docs.perplexity.ai/guides/mcp-server

## 
[​](https://docs.perplexity.ai/guides/mcp-server#what-is-mcp%3F)
What is MCP?
The **Model Context Protocol (MCP)** is an open standard designed to connect AI assistants with the systems where data lives. By providing a universal interface for AI applications to access structured and unstructured data, MCP eliminates the need for custom integrations, enabling AI models to retrieve real-time, relevant information more efficiently. Learn more about MCP [here](https://modelcontextprotocol.io/introduction).
## 
[​](https://docs.perplexity.ai/guides/mcp-server#mcp-server-for-perplexity%E2%80%99s-sonar-api)
MCP Server for Perplexity’s Sonar API
Our **MCP server implementation** for Sonar allows any AI-powered tool to perform real-time, web-wide research using Perplexity’s powerful search engine. This server acts as a bridge between AI applications and the Sonar, enabling seamless integration for retrieving and synthesizing relevant, up-to-date information from the web.
### 
[​](https://docs.perplexity.ai/guides/mcp-server#how-it-works)
How It Works
  * The **Perplexity Ask MCP Server** follows MCP’s **open standard** , allowing any AI assistant or automation tool to connect to the **Sonar API** for live web searches.
  * AI models can query the server for information retrieval, leveraging Perplexity’s search capabilities to return the most relevant insights.


### 
[​](https://docs.perplexity.ai/guides/mcp-server#example%3A-using-mcp-with-claude)
Example: Using MCP with Claude
Claude is one example of how this MCP server can be used effectively. When connected to Claude, the **Perplexity Ask MCP Server** enables it to **perform live web searches** and return **highly relevant, up-to-date responses** , enhancing its ability to provide real-time knowledge.
### 
[​](https://docs.perplexity.ai/guides/mcp-server#where-to-find-the-documentation)
Where to Find the Documentation
Developers looking to integrate and deploy the **Perplexity Ask MCP Server** can find our implementation, detailed documentation, and setup instructions in our official MCP repository: 📖 [**Perplexity Ask MCP Server**](https://github.com/ppl-ai/modelcontextprotocol/tree/main) This includes:
  * Implementation code
  * Setup instructions
  * Configuration steps
  * API usage guidelines
  * Deployment and troubleshooting tips


