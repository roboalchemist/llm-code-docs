# Source: https://exa.ai/docs/reference/websets-mcp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Websets MCP

Websets MCP connects AI assistants to Exa's Websets API for building and enriching collections of web entities like companies, people, and research papers.

**What you can do:**

* Find AI startups in San Francisco with funding over \$10M
* Build a database of companies and enrich with CEO names, revenue, employee counts
* Create a list of research papers and extract key findings
* Monitor industries for new companies matching your criteria

## Installation

<Card title="Get your Exa API key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys" />

Connect to Websets MCP:

```
https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY
```

<Tabs>
  <Tab title="Cursor">
    [![Install with one click](https://img.shields.io/badge/Install_with_one_click-Cursor-000000?style=flat-square\&logoColor=white)](https://cursor.com/en/install-mcp?name=websets\&config=eyJuYW1lIjoid2Vic2V0cyIsInR5cGUiOiJodHRwIiwidXJsIjoiaHR0cHM6Ly93ZWJzZXRzbWNwLmV4YS5haS9tY3AifQ==)

    Or add to `~/.cursor/mcp.json`:

    ```json  theme={null}
    {
      "mcpServers": {
        "websets": {
          "url": "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
        }
      }
    }
    ```
  </Tab>

  <Tab title="VS Code">
    [![Install with one click](https://img.shields.io/badge/Install_with_one_click-VS_Code-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=websets\&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fwebsetsmcp.exa.ai%2Fmcp%22%7D)

    Or add to `.vscode/mcp.json`:

    ```json  theme={null}
    {
      "servers": {
        "websets": {
          "type": "http",
          "url": "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Claude Code">
    Run in terminal:

    ```bash  theme={null}
    claude mcp add --transport http websets "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
    ```
  </Tab>

  <Tab title="Claude Desktop">
    Add to your Claude Desktop config file:

    **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

    **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

    ```json  theme={null}
    {
      "mcpServers": {
        "websets": {
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"]
        }
      }
    }
    ```
  </Tab>

  <Tab title="Windsurf">
    Add to `~/.codeium/windsurf/mcp_config.json`:

    ```json  theme={null}
    {
      "mcpServers": {
        "websets": {
          "serverUrl": "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Other">
    For other MCP clients that support remote MCP:

    ```json  theme={null}
    {
      "mcpServers": {
        "websets": {
          "url": "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
        }
      }
    }
    ```

    If your client doesn't support remote MCP servers directly:

    ```json  theme={null}
    {
      "mcpServers": {
        "websets": {
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"]
        }
      }
    }
    ```
  </Tab>
</Tabs>

<br />

<br />

## Available Tools

| Tool                | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `create_webset`     | Create a collection with search query, criteria, and enrichments         |
| `list_websets`      | List all websets in your account                                         |
| `get_webset`        | Get details about a webset                                               |
| `update_webset`     | Update a webset's metadata                                               |
| `list_webset_items` | List items in a webset with their data                                   |
| `get_item`          | Get details about a specific item                                        |
| `create_search`     | Add more entities to a webset                                            |
| `get_search`        | Check search status                                                      |
| `cancel_search`     | Cancel a running search                                                  |
| `create_enrichment` | Extract data from items (text, number, date, email, phone, url, options) |
| `get_enrichment`    | Check enrichment status                                                  |
| `delete_enrichment` | Delete an enrichment                                                     |
| `cancel_enrichment` | Cancel a running enrichment                                              |
| `create_monitor`    | Auto-update a webset on a schedule                                       |

<br />

<Note>
  Free searches are included. A [Websets plan](https://exa.ai/pricing) is required for continued use.
</Note>

<br />

## Key Concepts

**Entity Types:** Search for different kinds of entities:

* `company` - companies and startups
* `person` - individuals (e.g., for recruiting)
* `research_paper` - academic papers
* `article` - blog posts and news articles
* `custom` - define your own entity type

**Enrichment Formats:** Extract data in different formats:

* `text` - free-form text (CEO name, description)
* `number` - numeric values (employee count, revenue)
* `date` - dates (founding date, funding date)
* `email`, `phone`, `url` - contact info
* `options` - multiple choice (e.g., funding stage: Seed, Series A, Series B)

**Criteria:** Natural language filters to verify entities:

* "Founded after 2020"
* "Has raised more than \$10M in funding"
* "Located in the United States"
* "Has more than 50 employees"

<br />

<br />

<CardGroup cols={2}>
  <Card title="Websets API Docs" icon="book" href="/websets/api/overview">
    Full API reference
  </Card>

  <Card title="Try Websets" icon="grid-2" href="https://websets.exa.ai/">
    Visual interface for websets
  </Card>
</CardGroup>

<Accordion title="Usage Examples" icon="magnifying-glass">
  **Create a Webset**

  ```
  Create a webset of AI startups in San Francisco founded after 2020. Find 10 companies and enrich with CEO name and funding amount.
  ```

  **Add More Entities**

  ```
  Search for 5 more AI companies that have raised Series A funding.
  ```

  **Extract Data**

  ```
  Add an enrichment to extract employee count for each company.
  ```

  **Set Up Monitoring**

  ```
  Create a monitor to check for new AI startups every Monday at 9am.
  ```
</Accordion>
