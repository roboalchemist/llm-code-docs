# Source: https://docs.api7.ai/apisix/reference/apisix-mcp.md

# APISIX Model Context Protocol (APISIX-MCP)

APISIX-MCP is a Model Context Protocol (MCP) server designed to bridge large language models (LLMs) with the APISIX Admin API. This integration enables natural language interactions for managing and viewing resources within APISIX through MCP-compatible AI clients, regardless of how APISIX is deployed.

By leveraging APISIX-MCP, users can perform operations such as creating, retrieving, updating, deleting resources, as well as sending requests. This approach simplifies API management by allowing conversational commands to handle tasks that traditionally required manual configurations.

APISIX-MCP is open-sourced and available on [npm](https://www.npmjs.com/package/apisix-mcp) and [GitHub](https://github.com/api7/apisix-mcp). It can be configured via any MCP-compatible AI client, such as Claude Desktop, Cursor, or the Cline extension in VS Code.

## Install and Configure APISIX-MCP[â](#install-and-configure-apisix-mcp "Direct link to Install and Configure APISIX-MCP")

The following are different ways of installation.

### npm[â](#npm "Direct link to npm")

If you are installing from npm, configure the MCP server with the following details and update the APISIX server address, port, Admin API port, prefix, and authentication key per your environment in the AI client:

```
{
  "mcpServers": {
    "apisix-mcp": {
      "command": "npx",
      "args": ["-y","apisix-mcp"],
      "env": {
        "APISIX_SERVER_HOST": "http://127.0.0.1",
        "APISIX_SERVER_PORT": "9080",
        "APISIX_ADMIN_API_PORT": "9180",
        "APISIX_ADMIN_API_PREFIX": "/apisix/admin",
        "APISIX_ADMIN_KEY": "edd1c9f034335f136f87ad84b625c8f1"
      }
    }
  }
}
```

### Smithery[â](#smithery "Direct link to Smithery")

To install APISIX-MCP for Claude Desktop, run:

```
npx -y @smithery/cli install @api7/apisix-mcp --client claude
```

### Source Code[â](#source-code "Direct link to Source Code")

To install from source code, first clone the `apisix-mcp` repository:

```
git clone https://github.com/api7/apisix-mcp.git
cd apisix-mcp
```

Install the dependencies and build the project:

```
pnpm install
pnpm build
```

Finally, configure the MCP server with the following details and update the APISIX server address, port, Admin API port, prefix, and authentication key per your environment in the AI client:

```
{
  "mcpServers": {
    "apisix-mcp": {
      "command": "npx",
      "args": [
        "your-apisix-mcp-path/dist/index.js"
      ],
      "env": {
        "APISIX_SERVER_HOST": "http://127.0.0.1",
        "APISIX_SERVER_PORT": "9080",
        "APISIX_ADMIN_API_PORT": "9180",
        "APISIX_ADMIN_API_PREFIX": "/apisix/admin",
        "APISIX_ADMIN_KEY": "edd1c9f034335f136f87ad84b625c8f1"
      }
    }
  }
}
```

tip

The `APISIX_SERVER_HOST`, `APISIX_SERVER_PORT`, `APISIX_ADMIN_API_PORT`, `APISIX_ADMIN_API_PREFIX`, and `APISIX_ADMIN_KEY` above are configured to their default values. If your APISIX installation uses these default values, you can optionally omit the `env` configurations.

Once the configurations are saved, you should see the MCP server is successfully installed in your AI client.

## Supported Operations[â](#supported-operations "Direct link to Supported Operations")

APISIX-MCP supports the following operations. When you use the AI client with APISIX-MCP, your natural language inputs will be translated into these operations.

### Common Operations[â](#common-operations "Direct link to Common Operations")

* `get_resource`: Retrieve resources by type, such as routes, services, and upstreams.
* `delete_resource`: Delete resources by ID.
* `send_request_to_gateway`: Send requests to the gateway.

### API Resources Operations[â](#api-resources-operations "Direct link to API Resources Operations")

* `create_route` / `update_route` / `delete_route`: Manage routes.
* `create_service` / `update_service` / `delete_service`: Manage services.
* `create_upstream` / `update_upstream` / `delete_upstream`: Manage upstreams.
* `create_or_update_proto`: Manage protobuf definitions.
* `create_or_update_stream_route`: Manage stream routes.

### Plugin Operations[â](#plugin-operations "Direct link to Plugin Operations")

* `get_all_plugin_names`: Get all available plugin names.
* `get_plugin_info` / `get_plugins_by_type` / `get_plugin_schema`: Retrieve plugin configurations.
* `create_plugin_config` / `update_plugin_config`: Manage plugin configurations.
* `create_global_rule` / `update_global_rule`: Manage global plugins.
* `get_plugin_metadata` / `create_or_update_plugin_metadata` / `delete_plugin_metadata`: Manage plugin metadata.

### Security Configuration[â](#security-configuration "Direct link to Security Configuration")

* `get_secret_by_id` / `create_secret` / `update_secret`: Manage secrets.
* `create_or_update_consumer` / `delete_consumer`: Manage consumers.
* `get_credential` / `create_or_update_credential` / `delete_credential`: Manage consumer credentials.
* `create_consumer_group` / `delete_consumer_group`: Manage consumer groups.
* `create_ssl` / `update_ssl` / `delete_ssl`: Manage SSL certificates.

## Example[â](#example "Direct link to Example")

To create a route, you can enter this prompt in your AI client:

```
Create a route named httpbin-get-route with route URI /get for accessing https://httpbin.org upstream, rate limiting the requests to 2 requests every 30 seconds. Print the route details after configuration.
```

You should see the route is successfully created by your AI client:

```
Successfully created route "httpbin-get-route" with the following configuration:

URI: /get
Upstream: https://httpbin.org (roundrobin load balancing)
Rate limiting: 2 requests per 30 seconds per IP address
Route ID: httpbin-get-route
Status: Active (1)
The route is now ready to accept requests at the /get path, which will be forwarded to httpbin.org with rate limiting applied.
```

You can also send a request to the route from your AI client for verification:

```
Send a request to this route.
```

You should see a response similar to the following in your AI client:

```
Successfully tested the route "httpbin-get-route":

Received HTTP 200 response from httpbin.org
Rate limiting headers show:
Limit: 2 requests per 30 seconds (x-ratelimit-limit: 2)
Remaining: 1 request available (x-ratelimit-remaining: 1)
Reset in: 30 seconds (x-ratelimit-reset: 30)
The route is properly configured and forwarding requests to httpbin.org
The rate limiting plugin is working as expected
```

For more examples, please follow the [getting started tutorials](https://docs.api7.ai/apisix/getting-started/configure-routes.md).
