# Source: https://docs.exa.ai/reference/websets-mcp.md

# Websets MCP

[![Install in Cursor](https://img.shields.io/badge/Install_in-Cursor-000000?style=flat-square\&logoColor=white)](https://cursor.com/en/install-mcp?name=websets\&config=eyJuYW1lIjoid2Vic2V0cyIsInR5cGUiOiJodHRwIiwidXJsIjoiaHR0cHM6Ly93ZWJzZXRzbWNwLmV4YS5haS9tY3AifQ==)
[![Install in VS Code](https://img.shields.io/badge/Install_in-VS_Code-0098FF?style=flat-square\&logo=visualstudiocode\&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=websets\&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fwebsetsmcp.exa.ai%2Fmcp%22%7D)

### Websets MCP: Build and enrich collections of web entities with AI

Websets MCP Server enables AI assistants like Claude to create, search, and enrich collections of web entities (companies, people, research papers, articles) through the Exa Websets API. Automatically discover entities, verify them against criteria, and extract custom data with AI-powered enrichments.

Examples of what you can do with Websets MCP:

* Find and verify AI startups in San Francisco with funding over \$10M
* Create a list of research papers on quantum computing and extract key findings
* Build a database of companies in specific industries and enrich with CEO names, revenue, and employee counts
* Monitor industries for new companies matching your criteria

**Works with Cursor and Claude Code!** Use the HTTP-based configuration format below.

***

Websets MCP provides powerful tools for entity search, verification, and data enrichment, making it easy to build custom datasets for research, sales, recruiting, and more.

## Remote Websets MCP

Connect directly to Exa's hosted Websets MCP server using this URL:

```
https://websetsmcp.exa.ai/mcp
```

You **must** include your Exa API key in the URL:

```
https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY
```

**Note:** Unlike the standard Exa MCP, the Websets MCP does not require a separate Websets/Smithery key when using the custom domain. Only your Exa API key is required.

### Claude Desktop Configuration for Remote MCP

Add this to your Claude Desktop configuration file:

```json  theme={null}
{
  "mcpServers": {
    "websets": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY"
      ]
    }
  }
}
```

Replace `YOUR_EXA_API_KEY` with your actual Exa API key.

### Cursor and Claude Code Configuration for Remote MCP

For Cursor and Claude Code, use this HTTP-based configuration format:

```json  theme={null}
{
  "mcpServers": {
    "websets": {
      "type": "http",
      "url": "https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY",
      "headers": {}
    }
  }
}
```

Replace `YOUR_EXA_API_KEY` with your actual Exa API key.

## Available Tools

Websets MCP includes 14 specialized tools for managing websets, searches, enrichments, and monitors:

### Webset Management

| Tool                | Description                                                                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`create_webset`** | Create a new webset collection with automatic search and optional enrichments. Specify your search query, criteria for filtering results, and data fields to extract |
| `list_websets`      | List all websets in your account with pagination support                                                                                                             |
| `get_webset`        | Get detailed information about a specific webset including its status, searches, enrichments, and items                                                              |
| `update_webset`     | Update a webset's metadata with custom key-value pairs                                                                                                               |

### Item Management

| Tool                | Description                                                                     |
| ------------------- | ------------------------------------------------------------------------------- |
| `list_webset_items` | List all items (entities) in a webset with their properties and enrichment data |
| `get_item`          | Get detailed information about a specific item in a webset                      |

### Search Operations

| Tool                | Description                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`create_search`** | Create a new search to find and add entities to a webset. Specify entity type (company, person, paper, article), search query, and filtering criteria |
| `get_search`        | Check the status and results of a search operation                                                                                                    |
| `cancel_search`     | Cancel a running search operation                                                                                                                     |

### Enrichment Operations

| Tool                    | Description                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **`create_enrichment`** | Create a new enrichment to extract custom data from webset items. Supports text, number, date, email, phone, URL, and options formats |
| `get_enrichment`        | Get details about a specific enrichment including its progress and status                                                             |
| `delete_enrichment`     | Delete an enrichment and all its extracted data                                                                                       |
| `cancel_enrichment`     | Cancel a running enrichment operation                                                                                                 |

### Monitor Operations

| Tool                 | Description                                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **`create_monitor`** | Create a monitor to automatically update a webset on a schedule using cron expressions. Monitors run searches periodically to find new entities |

## Getting Started

<Card title="Get your Exa API key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys" />

## Usage Examples

Once configured, you can ask your AI assistant to perform webset operations:

### Creating a Webset

```
Create a webset of AI startups in San Francisco founded after 2020. 
Find 10 companies and enrich with CEO name and funding amount.
```

This will use `create_webset` to:

* Search for AI startups in San Francisco
* Filter for companies founded after 2020
* Automatically enrich each company with CEO name and funding amount

### Searching for Entities

```
Search for 5 more AI companies in the existing webset that have 
raised Series A or later funding.
```

This will use `create_search` to add more companies matching specific criteria.

### Creating Enrichments

```
Add an enrichment to extract the number of employees for each company 
in the webset.
```

This will use `create_enrichment` to extract employee counts.

### Setting Up Monitors

```
Create a monitor to check for new AI startups in San Francisco 
every Monday at 9am.
```

This will use `create_monitor` to automatically update your webset weekly.

### Listing and Viewing Results

```
Show me all the companies in my AI startups webset.
```

This will use `list_webset_items` to display the collected entities with their enrichment data.

## Key Features

### Entity Types

Websets support multiple entity types:

* **Companies** - Search and enrich company data
* **People** - Find and verify individuals with specific criteria
* **Research Papers** - Discover academic papers and extract key information
* **Articles** - Find articles and blog posts on specific topics
* **Custom** - Define your own entity type

### Enrichment Formats

Extract data in multiple formats:

* **text** - Free-form text (e.g., company description, CEO name)
* **number** - Numeric values (e.g., employee count, revenue)
* **date** - Dates (e.g., founding date, last funding round)
* **email** - Email addresses
* **phone** - Phone numbers
* **url** - Website URLs
* **options** - Multiple choice selection from predefined options (e.g., company stage: Seed, Series A, Series B)

### Search Criteria

Use natural language criteria to filter search results:

* "Founded after 2020"
* "Has raised more than \$10M in funding"
* "Located in the United States"
* "Has more than 50 employees"

The AI will evaluate each potential entity against your criteria and only include matches.

### Automated Monitoring

Set up monitors with cron expressions to keep your websets up-to-date:

* `0 9 * * 1` - Every Monday at 9:00 AM
* `0 0 * * *` - Every day at midnight
* `0 */6 * * *` - Every 6 hours

Monitors automatically run searches and add new matching entities to your webset.

## Advanced Examples

### Building a Company Database

```
Create a webset of B2B SaaS companies with:
- Query: "B2B SaaS companies in New York"
- Criteria: "Has raised Series A or later funding"
- Enrichments: 
  - CEO name (text)
  - Employee count (number)
  - Funding stage (options: Seed, Series A, Series B, Series C+)
  - Latest funding date (date)
  - Company website (url)
```

### Research Paper Collection

```
Create a webset of machine learning research papers with:
- Query: "Recent papers on transformer models in NLP"
- Criteria: "Published in 2024 or 2025"
- Enrichments:
  - Lead author (text)
  - Publication date (date)
  - Key findings (text)
  - Citation count (number)
```

### People Search for Recruiting

```
Create a webset of potential candidates:
- Query: "Senior ML engineers in San Francisco Bay Area"
- Criteria: "Has 5+ years of experience in machine learning"
- Enrichments:
  - Current company (text)
  - LinkedIn profile (url)
  - Email address (email)
  - Years of experience (number)
```

## API Integration

Websets MCP provides a seamless interface to the Websets API. For more detailed information about the underlying API, visit:

* [Websets API Documentation](/websets/api/overview)
* [Websets Dashboard Guide](/websets/dashboard/get-started)
* [Websets Overview](/websets/overview)

## Configuration Details

### Claude Desktop (macOS)

Configuration file location:

```bash  theme={null}
~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Claude Desktop (Windows)

Configuration file location:

```powershell  theme={null}
%APPDATA%\Claude\claude_desktop_config.json
```

### Required Parameters

When using the hosted MCP server at `https://websetsmcp.exa.ai/mcp`, you **must** include your Exa API key:

```
https://websetsmcp.exa.ai/mcp?exaApiKey=YOUR_EXA_API_KEY
```

### Parameter Formats

When creating websets, searches, enrichments, and monitors through natural language with your AI assistant, the following formats are automatically used:

**Search Criteria Format:**

```json  theme={null}
[
  {"description": "Founded after 2020"},
  {"description": "Has raised more than $10M"}
]
```

**Enrichment Format:**

```json  theme={null}
[
  {"description": "CEO name", "format": "text"},
  {"description": "Company stage", "format": "options", "options": [
    {"label": "Seed"},
    {"label": "Series A"},
    {"label": "Series B"}
  ]}
]
```

**Entity Type Format:**

```json  theme={null}
{"type": "company"}
```

**Cron Expression Format (for Monitors):**

```
"0 9 * * 1"  (Every Monday at 9:00 AM)
```

## Tips for Best Results

1. **Be specific with search queries** - The more specific your query, the better the results
2. **Use clear criteria** - Write criteria in simple, declarative sentences
3. **Choose appropriate enrichment formats** - Use "options" format when you want to categorize data
4. **Start small** - Begin with a small search count (5-10 items) to test your query and criteria
5. **Monitor long-running operations** - Use `get_search` and `get_enrichment` to check progress
6. **Use external IDs** - Provide your own IDs to websets for easier reference in your application

## Troubleshooting

### Common Issues

**Issue: Enrichment not extracting the right data**

* Solution: Make your enrichment description more specific and include example formats

**Issue: Search returning no results**

* Solution: Try broadening your search criteria or making your query less specific

**Issue: Monitor not running**

* Solution: Verify your cron expression format (5 fields: minute hour day month weekday)

### Getting Help

* Check the [Websets FAQ](/websets/faq)
* Visit the [Websets API Documentation](/websets/api/overview)
* Join our [Discord community](https://discord.com/invite/HCShtBqbfV)

## Additional Resources

* [Websets Dashboard](https://websets.exa.ai/) - Visual interface for managing websets
* [Websets API Reference](/websets/api/overview) - Complete API documentation
* [Websets Examples](/websets/dashboard/websets-example-queries) - Example queries and use cases
* [Exa Search API](/reference/search) - The underlying search technology


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt