# Source: https://docs.tabnine.com/main/getting-started/tabnine-agent/mcp-intro-and-setup.md

# Model Context Protocol servers (MCP)

## What is MCP?

The **Model Context Protocol (MCP)** is an open standard for connecting large language models (LLMs) to external tools, data sources, and APIs. *MCP servers* implement the MCP. They act as standardized interfaces that allow language models to communicate with external applications or systems—similar in concept to APIs, but specifically designed for LLM-driven interactions.

With Tabnine Agent, these are managed in a similar manner to creating guidelines, through a specific file.

***

### MCP Server Configuration <picture><source srcset="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fc216297f60d93c5012dad81821871165aec58d6%2Fmcp-white.png?alt=media" media="(prefers-color-scheme: dark)"><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b12bfdf91f6dbf1b2297b3bf2126bc97d2d849be%2Fmcp-black.png?alt=media" alt="" data-size="line"></picture>

MCP servers are configured through a JSON file under the `.tabnine` folder in your project root:

First, enter the same `/.tabnine/` directory inside your project directory.

{% hint style="success" %}
`.tabnine/mcp_servers.json` can **also** be placed in the home directory:\
\
`~/.tabnine/mcp_servers.json`
{% endhint %}

To direct to specific MCP servers, create the `mcp_servers.json` file, which will follow this structure here:

```json
{
    "mcpServers": {
        "server-name": {
            "command": "server-executable",
            "args": [
                "arg1",
                "arg2"
            ],
            "env": {
                "API_KEY": "your-api-key",
                "BASE_URL": "https://api.example.com"
            }
        }
    }
}
```

In that `mcp_servers.json` file, list each server you want to include. For each server mentioned in the file, Tabnine Agent requires the following configuration components:

1. `mcp_server` — this is the top-level container
2. `<server-name>` – the name of the server itself
3. `command` – the script command that launches the server

Optional fields include:

4. `args` – command line arguments (with no spaces, otherwise they’ll be treated as separate paths)
5. `env` – environment key-value pairs

Here is an example of that structure filled in with variables for Jira:

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp-atlassian:latest"
      ],
      "env": {
        "JIRA_URL": "https://mcp.atlassian.com/v1/mcp",
        "JIRA_API_TOKEN": "7H15-15_Ju57-4_54Mp13-4P1_C0D3-f0R_47145514n-Bu7_U-c4N-g3N3R473-Y0Ur-0Wn_Fr0M-y0Ur-J1R4_4Cc0Un7-47-1D-47145514N-C0M"
      }
    }
  }
}
```

***

### Supported Transport Layers <a href="#transport-types" id="transport-types"></a>

The service automatically detects the transport type based on your configuration:

| ***Detected Transport*** | ***Configuration Field*** | ***Use Case***               |
| ------------------------ | ------------------------- | ---------------------------- |
| **STDIO**                | `command` present         | Local MCP servers, CLI tools |
| **Streamable HTTP**      | `url` present             | Modern remote APIs           |
| **SSE**                  | `transport: "sse"`        | Legacy remote servers        |

***

### Commonly Used MCP Servers

There are dozens of available MCP integrations on the market, official MCP servers for individual third parties. Here are a few of commonly used ones:

<table><thead><tr><th width="178.9739990234375">Category</th><th>MCP Servers</th></tr></thead><tbody><tr><td>Development Tools</td><td><ul><li><a href="https://github.com/github/github-mcp-server"><strong>GitHub</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-cd28a4f62c11fcbb8dae30bad751b9da1cf6303c%2Ficon%3Dgithub%402x.png?alt=media" alt="" data-size="line"></li><li><a href="https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server/"><strong>GitLab</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f0c8c729dd97f4a29416936c633e087936377eca%2Fgitlab2%402x-1.png?alt=media" alt="" data-size="line"></li></ul></td></tr><tr><td>Project Management</td><td><ul><li><a href="https://github.com/makenotion/notion-mcp-server#readme"><strong>Notion</strong></a> <picture><source srcset="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e090d2ce2e261dcd819ce1865f3dcbb948279cd6%2Fwhite%20notion.png?alt=media" media="(prefers-color-scheme: dark)"><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5920cff5bce23affa0cf45c5ceb51eabf7a168e0%2FNotion_App_Logo-672x700.png?alt=media" alt="" data-size="line"></picture> - For Notion API</li></ul></td></tr><tr><td>CloudOps</td><td><ul><li><a href="https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server"><strong>Azure</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7c750318da4477aa49b555b3a3f3f7e5c6060a2d%2Fazure.png?alt=media" alt="" data-size="line">- Access to Azure Storage, Cosmos DB, the Azure CLI, etc.</li><li><a href="https://github.com/microsoft/azure-devops-mcp"><strong>Azure DevOps</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-dcfbf853d685cd5aef312a6013235441d0e56ef9%2FAzure%20Devops.svg?alt=media" alt="" data-size="line"> - Specific to services like repos, builds, releases, tests, code, etc.</li><li><p><a href="https://github.com/awslabs/mcp"><strong>AWS</strong></a> </p><p><picture><source srcset="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0068abbeb8aa55b8973c2289b40c7ed880fc40da%2Faws%20white.png?alt=media" media="(prefers-color-scheme: dark)"><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fbcde29d2b74c2be4406f5fd299744bc50b46286%2FAmazon_Web_Services_Logo.svg%20(1).png?alt=media" alt="" data-size="line"></picture></p></li><li><a href="https://github.com/awslabs/mcp/tree/main/src/cloudtrail-mcp-server"><strong>AWS CloudTrail</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c9ac878154d2cff18f223f6a9a9604795d8d8a76%2FAWS-CloudTrail_light-bg%404x.png?alt=media" alt="" data-size="line"></li><li><a href="https://mcpservers.org/servers/awslabs/cdk-mcp-server"><strong>AWS CDK</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-05c4815a8b448011c95a2d81bb96700e944f5132%2Faws%20cdk.png?alt=media" alt="" data-size="line"></li><li><a href="https://github.com/awslabs/mcp/tree/main/src/core-mcp-server"><strong>AWS Core</strong></a></li><li><a href="https://github.com/googleapis/gcloud-mcp"><strong>Google Cloud Protocol</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e9d755e8fcaf177463ef47441095e2210ae16681%2FGoogle%20Cloud.svg?alt=media" alt="" data-size="line"></li></ul></td></tr><tr><td>Database Tools</td><td><ul><li><a href="https://github.com/googleapis/genai-toolbox"><strong>MCP Toolbox for Databases</strong></a> <strong>(open source)</strong></li><li><a href="https://github.com/idoru/influxdb-mcp-server"><strong>InfluxDB</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-665636a62175fd24231ee72d0fb2f3ecd31cf4f8%2Finfluxdb-logo.png?alt=media" alt="" data-size="line"></li><li><a href="https://github.com/qdrant/mcp-server-qdrant"><strong>Qdrant</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f2878fbbdc38f38faea1b38814958aeee67e1354%2Fqdrant%20logo.png?alt=media" alt="" data-size="line"></li><li><a href="https://github.com/ClickHouse/mcp-clickhouse"><strong>ClickHouse</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f2144b5d7ee85fe5e1f0134dc88a2404b3f7ced4%2Fclickhouse.svg?alt=media" alt="" data-size="line"></li><li><a href="https://github.com/neondatabase/mcp-server-neon"><strong>Neon</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d3299b576e5dd1eace7b8a555ed05743e716ae62%2FNeon.png?alt=media" alt="" data-size="line"></li></ul></td></tr><tr><td>Languages &#x26; Frameworks</td><td><ul><li><a href="https://github.com/sveltejs/mcp"><strong>Svelte</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a8849cf9f84fcaae213227a5baeb7dcc310e26f6%2FSvelte_Logo.svg.png?alt=media" alt="" data-size="line"></li><li><a href="https://www.npmjs.com/package/next-devtools-mcp"><strong>Next.js</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5adfd9c664b728eab3648fb436ffc83fcb3a70b6%2Fimage.png?alt=media" alt="" data-size="line"></li></ul></td></tr><tr><td>Monitoring</td><td><ul><li><a href="https://github.com/grafana/mcp-grafana"><strong>Grafana</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5a46c8ebd54915094f8b8ed1e95576e520b50321%2FGrafana_icon.svg.png?alt=media" alt="" data-size="line"></li><li><a href="https://www.elastic.co/docs/solutions/search/agent-builder/mcp-server"><strong>Elastic</strong></a> <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b95507cd54b288035ff7e01a013a38e522fff42e%2Felastics.svg?alt=media" alt="" data-size="line"> (Elasticsearch &#x26; Kibana)</li></ul></td></tr></tbody></table>

## Configuration Examples <a href="#configuration-examples" id="configuration-examples"></a>

#### Local MCP Server (Stdio Transport) <a href="#local-mcp-server-stdio-transport" id="local-mcp-server-stdio-transport"></a>

**Detected by**: Presence of `command` field

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Documents"
      ],
      "env": {
        "NODE_ENV": "production",
        "DEBUG": "mcp:*"
      },
      "cwd": "/Users/username/workspace"
    }
  }
}
```

**Properties**:

* `command` (required): The executable to run
* `args` (optional): Array of command-line arguments
* `env` (optional): Environment variables for the process
* `cwd` (optional): Working directory for the process

#### Remote MCP Server with JWT Authentication <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-30d2a983434526f2885839f00612f317b04ec7e5%2Fjwt-3.svg?alt=media" alt="" data-size="line"> <a href="#remote-mcp-server-with-jwt-authentication" id="remote-mcp-server-with-jwt-authentication"></a>

**Detected by**: Presence of `url` field (defaults to Streamable HTTP)

```json
{
  "mcpServers": {
    "my-api": {
      "url": "https://api.example.com/mcp",
      "requestInit": {
        "headers": {
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
          "Content-Type": "application/json"
        }
      }
    }
  }
}
```

**Properties**:

* `url` (required): The MCP endpoint URL
* `requestInit` (optional): Standard Fetch API RequestInit object
  * `headers`: HTTP headers to include in all requests
* `sessionId` (optional): Session identifier for the connection

#### Remote MCP Server with API Key (multiple headers) <a href="#remote-mcp-server-with-api-key" id="remote-mcp-server-with-api-key"></a>

This example shows how various authorizations might appear in the `mcp_servers.json` file.

```json
{
  "mcpServers": {
    "weather-service": {
      "url": "https://weather-mcp.example.com/mcp",
      "requestInit": {
        "headers": {
          "Authorization": "Bearer token",
          "X-API-Key": "api-key",
          "X-Client-ID": "client-id",
          "X-Environment": "production",
          "X-Session-Token": "session-token-value"
        }
      }
    }
  }
}
```

#### Legacy SSE Server <a href="#legacy-sse-server" id="legacy-sse-server"></a>

**Detected by**: Explicit `transport: "sse"` field

```json
{
  "mcpServers": {
    "legacy-api": {
      "transport": "sse",
      "url": "https://old-api.example.com/sse",
      "requestInit": {
        "headers": {
          "Authorization": "Bearer legacy-token-123"
        }
      },
      "eventSourceInit": {
        "withCredentials": true
      }
    }
  }
}
```

**Properties**:

* `transport` (required): Must be `"sse"`
* `url` (required): The SSE endpoint URL
* `requestInit` (optional): Request configuration
* `eventSourceInit` (optional): EventSource-specific options
* `authProvider` (optional): OAuth client provider (advanced)

{% hint style="info" %}
Some MCP servers can silently fail OAuth authentication after a token is revoked on the provider side. When this happens, the local cached OAuth credentials remain in place, and the OAuth flow is *not* automatically re-triggered.

These cached OAuth credentials are stored in the .`mcp_auth` folder in your home folder. The fix is to remove the .mcp-auth folder. This removes all cached credentials and will force all new OAuth flows to retrigger.

Delete the `.mcp_auth` folder from the user’s home directory. This clears all cached OAuth credentials. The next MCP action requiring authentication will correctly trigger a fresh OAuth flow.
{% endhint %}
