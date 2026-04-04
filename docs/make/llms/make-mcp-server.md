# Source: https://developers.make.com/mcp-server/make-mcp-server.md

# Make MCP Server

Make MCP server allows AI systems, such as large language models (LLMs), to run scenarios and manage the contents of your Make account. Model Context Protocol (MCP) is a communication standard between AI and external systems. It enables safe interactions by defining endpoints and providing authentication.&#x20;

**Benefits**&#x20;

* Creates bidirectional communication between AI and Make&#x20;
* Allows AI to access and manage elements of your Make account&#x20;
* Turns your **active** and **on-demand** scenarios into callable tools for AI

### How Make MCP server works

AI systems like Claude and ChatGPT act as MCP clients of Make MCP server. The server provides them access to **scenario run** and **management** tools that enable the following actions:

* Run active and on-demand scenarios
* View and modify scenarios and their related entities (e.g., connections, webhooks, and data stores)
* View and modify teams and organizations

When you connect Make MCP server to an MCP client, your selected scopes determine the callable tools available on the server.

{% hint style="warning" %}
Scenario run (**Run your scenarios**) tools are available to all plans, and management (**View and modify**...) tools are available to paid plans.
{% endhint %}

**Scenario inputs and outputs**

When using scenarios as MCP tools, define scenario [inputs and outputs](https://help.make.com/scenario-inputs-and-outputs) to help AI understand what data to receive and send:

* **Inputs:** parameters that AI fills with data when the scenario runs
* **Outputs:** data returned from the scenario to your AI

{% hint style="info" %}
Detailed scenario descriptions are strongly recommended. They help your AI understand the purpose of the scenario and improve the reliability of your prompts.
{% endhint %}

### Available transport methods

Make MCP server is a cloud-based server hosted by Make, running via Streamable HTTP and Server-Sent Events (SSE).

#### Clients with Stateless Streamable HTTP support

Stateless Streamable HTTP is Make's default transport method due to its connection reliability. It is recommended when connecting to MCP clients that support Streamable HTTP.&#x20;

Use the following connection URLs, depending on your connection type:&#x20;

<details>

<summary>OAuth</summary>

```
https://mcp.make.com
```

</details>

<details>

<summary>MCP token</summary>

```
https://<MAKE_ZONE>/mcp/u/<MCP_TOKEN>/stateless
```

In the above configuration, replace `<MAKE_ZONE>` and `<MCP_TOKEN>` with your actual values.

* `MAKE_ZONE` - The zone your organization is hosted in (e.g., `eu2.make.com`).
* `MCP_TOKEN` - You can generate your MCP token in your Make profile.

{% hint style="warning" %}
To control which scenarios are available as tools through your MCP token, see [Scenarios as tools access control](https://developers.make.com/mcp-server/connect-using-mcp-token/scenarios-as-tools-access-control).
{% endhint %}

Optionally, you can append the following advanced query parameters to the URL for a more customized experience:

* `?maxToolNameLength=<length>` - By default, generated tool names are cropped to a maximum of 56 characters to ensure compatibility with most AI systems. You can customize this behavior by specifying the maximum generated tool name length using this parameter. The allowed range is 32 to 160 characters.

**Authorization in headers support**

If your client supports sending authorization in HTTP headers, you can use the following URL:

```
https://<MAKE_ZONE>/mcp/stateless
```

Specify the MCP token in the Authorization header as follows:

```
Authorization: Bearer <MCP_TOKEN>
```

</details>

#### Clients with Streamable HTTP support

If your MCP client supports Streamable HTTP,  you can use `/stream`  at the end of the connection URL specified for your chosen connection type ([OAuth](https://developers.make.com/mcp-server/connect-using-oauth) or [MCP token](https://developers.make.com/mcp-server/connect-using-mcp-token)).&#x20;

#### Clients with Server-Sent Events (SSE) support

If your MCP client supports SSE, use the following connection URLs, depending on your connection type:

<details>

<summary>OAuth</summary>

```
https://mcp.make.com/sse
```

</details>

<details>

<summary>MCP token</summary>

```
https://<MAKE_ZONE>/mcp/u/<MCP_TOKEN>/sse
```

In the above configuration, replace `<MAKE_ZONE>` and `<MCP_TOKEN>` with your actual values.

* `MAKE_ZONE` - The zone your organization is hosted in (e.g., `eu2.make.com`).
* `MCP_TOKEN` - You can generate your MCP token in your Make profile.

{% hint style="warning" %}
To control which scenarios are available as tools through your MCP token, see [Scenarios as tools access control](https://developers.make.com/mcp-server/connect-using-mcp-token/scenarios-as-tools-access-control).
{% endhint %}

Optionally, you can append the following advanced query parameters to the URL for a more customized experience:

* `?maxToolNameLength=<length>` - By default, generated tool names are cropped to a maximum of 56 characters to ensure compatibility with most AI systems. You can customize this behavior by specifying the maximum generated tool name length using this parameter. The allowed range is 32 to 160 characters.

**Authorization in headers support**

If your client supports sending authorization in HTTP headers, you can use the following URL:

```
https://<MAKE_ZONE>/mcp/sse
```

Specify the MCP token in the Authorization header as follows:

```
Authorization: Bearer <MCP_TOKEN>
```

</details>

#### Clients without SSE support

If your MCP client does not support SSE, use the Cloudflare `mcp-remote` proxy for compatibility. Refer to [Cloudflare's MCP Remote Proxy Guide](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/#connect-to-remote-mcp-servers-from-mcp-clients-that-today-only-support-local-mcp) for more details.

<details>

<summary>OAuth</summary>

Configuration example:

```json
{
  "mcpServers": {
    "make": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.make.com/sse"
      ]
    }
  }
}
```

</details>

<details>

<summary>MCP token</summary>

Configuration example:&#x20;

```json
{
  "mcpServers": {
    "make": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://<MAKE_ZONE>/mcp/u/<MCP_TOKEN>/sse"
      ]
    }
  }
}
```

</details>

### **Timeouts for tool calls**

Calls from MCP clients to tools on Make MCP server have timeout limits for returning output. Timeouts vary depending on the tool type called and the authorization and transport method used.

#### Scenario run tool timeout limits

* `https://mcp.make.com` (OAuth): 25 seconds
* `https://<MAKE_ZONE>/mcp/<TRANSPORT>` (MCP token): 40 seconds&#x20;

**Retrieve outputs after timeout**

Even after a scenario run tool call times out, the called scenario continues running in Make for up to 40 minutes, and you can retrieve the output after the scenario finishes its run.&#x20;

The call returns a timeout response that includes the `executionId` , which the MCP client can use to retrieve the output, once ready, with the corresponding tool.&#x20;

Example response:

```json
{
	instruction: 'The Tool execution has started, but did not complete yet. Use a corresponding Tool for getting Execution Results to check for the result asynchronously.',
	executionId: '4eb841b3fe3d48a5b2b59e2eed3f55be',
	scenarioId: 1,
},
```

{% hint style="warning" %}
Select the `scenarios:read` scope to enable MCP clients to retrieve outputs after timeout once a scenario run finishes.
{% endhint %}

#### Management tool timeout limits

* `https://mcp.make.com` (OAuth): 30 seconds
* `https://<MAKE_ZONE>/mcp/<TRANSPORT>` (MCP token, direct OAuth):
  * Stateless Streamable HTTP (`/stateless`) transport: 60 seconds&#x20;
  * SSE (`/sse`) and Streamable HTTP (`/stream`) transports: 5 minutes, 20 seconds

{% hint style="info" %}
Management tool calls are typically fast and rarely time out. If you still experience timeouts when using `https://mcp.make.com`, switch to a `https://<MAKE_ZONE>/mcp/<TRANSPORT>`  URL for longer timeouts.&#x20;
{% endhint %}
