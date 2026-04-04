# Source: https://docs.api7.ai/enterprise/api7-mcp-server-guide/deploy-api7-mcp.md

# Source: https://docs.api7.ai/enterprise/3.8.x/api7-mcp-server-guide/deploy-api7-mcp.md

# Deploy API7 MCP

[API7-MCP](https://github.com/api7/api7-mcp) is a Model Context Protocol (MCP) server for connecting to the API7ee API, allowing AI LLMs to analyze gateway resource configurations, monitoring data analysis, permission management, risk item detection, and more.

This tutorial walks you through deploying API7-MCP, using it to manage resources and send requests. The tutorial uses VS Code and Cline for demonstration, but you can choose other AI clients such as Cursor and Claude Desktop that best suit your workflow.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. [Install API7 Enterprise](https://docs.api7.ai/enterprise/3.8.x/getting-started/install-api7-ee.md).
2. Install Cline from the Extension Marketplace in Visual Studio Code (VS Code).

### Install and Configure API7-MCP[â](#install-and-configure-api7-mcp "Direct link to Install and Configure API7-MCP")

The following are different ways of installation.

#### npm[â](#npm "Direct link to npm")

If you are installing from npm, configure the MCP server with the following details. Then update the API7 dashboard address, gateway address, and API7 Enterprise token per your environment in the AI client:

```
{
  "mcpServers": {
    "api7-mcp": {
      "command": "npx",
      "args": ["-y", "api7-mcp"],
      "env": {
        "DASHBOARD_URL": "your-api7ee-dashboard-url",
        "GATEWAY_URL": "your-api7ee-gateway-server-url",
        "TOKEN": "your-api7ee-token"
      }
    }
  }
}
```

#### Source Code[â](#source-code "Direct link to Source Code")

To install from source code, first clone the api7-mcp repository:

```
git clone https://github.com/api7/api7-mcp.git
cd api7-mcp
```

Install the dependencies and build the project:

```
pnpm install
pnpm build
```

Finally, configure the MCP server with the following details and update the API7 dashboard address, gateway address, and API7 Enterprise token per your environment in the AI client:

```
{
  "mcpServers": {
    "api7-mcp": {
        "disabled": false,
        "command": "node",

        "args": ["your-project-path/dist/index.js"],
        "env": {
          "DASHBOARD_URL": "your-api7ee-dashboard-url",
          "GATEWAY_URL": "your-api7ee-gateway-server-url",
          "TOKEN": "your-api7ee-token"
      }
    }
  }
}
```

â¶ `args`: After running the command above, a **dist** folder will appear in the Explorer panel of VS Code. Keep the path of the **dist** folder, e.g., `/Users/alice/workspace/new/api7-mcp/dist/index.js`.

â· `DASHBOARD_URL`: The domain name of the API7 Enterprise dashboard, e.g., `http://192.168.31.29:7443`.

â¸ `GATEWAY_URL`: The gateway server URL of your API7 Enterprise, e.g., `http://192.168.64.1:9080`.

â¹ `TOKEN`: Configure the token generated on the API7 Enterprise Dashboard.

Once the configurations are saved, you should see that the MCP server is successfully installed in your AI client.

## Launch MCP Servers[â](#launch-mcp-servers "Direct link to Launch MCP Servers")

This tutorial uses VS Code and Cline for demonstration.

Open VS Code and click Cline on the left side navigation bar to open it.

![Open Cline](https://static.api7.ai/uploads/2025/04/30/kuUVEHH4_1-open-cline.webp)

On top of Cline, click on **MCP Servers**.

![Configure MCP Servers](https://static.api7.ai/uploads/2025/04/30/n8NWVfKm_2-configure-mcp-servers.webp)

Select **Installed** and click **Configure MCP Servers** to open the `cline_mcp_settings.json` file.

![Configure MCP Servers](https://static.api7.ai/uploads/2025/04/30/KQRDceIW_installed-configure-mcp.webp)

Update the `cline_mcp_settings.json` file according to the guide of the [Source Code](#source-code) part to configure the MCP Server.

After configuring the `cline_mcp_settings.json` file, the status on the right side of **api7-mcp** will turn green, indicating successful configuration and that API7-MCP is running.

![Successful MCP Configuration](https://static.api7.ai/uploads/2025/05/07/NLgJwriH_successful-configuration.webp)

Click the **Done** button in the upper right corner to complete.

![Finish MCP Configuration](https://static.api7.ai/uploads/2025/05/07/JBKKkLfx_finish-the-configuration.webp)

## Configure Cline in VS Code[â](#configure-cline-in-vs-code "Direct link to Configure Cline in VS Code")

Click the settings icon in the top right corner to access the settings.

![Open Settings](https://static.api7.ai/uploads/2025/05/07/pFDQc3co_open-settings.webp)

In the **API Provider** field, select your preferred API provider, e.g., **OpenRouter**.

![Select OpenRouter as API Provider](https://static.api7.ai/uploads/2025/05/07/KhYaqIVU_api-provider.webp)

Enter the **OpenRouter API Key** generated on the OpenRouter platform.

![Enter OpenRouter API Key](https://static.api7.ai/uploads/2025/05/07/WjROowF0_enter-openrouter-key.webp)

Select the desired AI model, e.g., **deepseek/deepseek-chat-v3-0324**, as the **Model**.

![Select Model](https://static.api7.ai/uploads/2025/05/07/gDRRuq2I_select-model.webp)

Click **Save** in the top right corner to complete the configuration.

![Save Settings](https://static.api7.ai/uploads/2025/05/07/Xwvpoaeo_save-settings.webp)

## Verify[â](#verify "Direct link to Verify")

In VS Code, ask Cline to send 5 API requests to API7 Enterprise.

![Send 5 API Requests](https://static.api7.ai/uploads/2025/05/16/Qyoub0nF_deploy-api7-mcp-1.webp)

Cline wants to use the `send_request_to_gateway` operation to run the command. Click **Approve** to authorize it.

![Authorize Cline to send requests](https://static.api7.ai/uploads/2025/05/16/hez0wDaW_deploy-api7-mcp-2.webp)

Cline returns that 5 API requests are successfully sent.

![Send API requests successfully](https://static.api7.ai/uploads/2025/05/16/2Wmn0r5H_deploy-api7-mcp-3.webp)

### Check API Request Count[â](#check-api-request-count "Direct link to Check API Request Count")

Ask Cline to check all API requests of API7 Enterprise over the past 10 minutes.

![Check API Request](https://static.api7.ai/uploads/2025/04/30/QArf9HI1_1-check-api-requests.webp)

Cline requests data on API requests over the past 10 minutes. Click **Approve** to authorize it.

![Approve to Fetch API Request Data](https://static.api7.ai/uploads/2025/04/30/Jdwd2cPz_2-approve-to-fetch-data.webp)

Cline returns the API request data for the past 10 minutes of API7 Enterprise. The result shows that the request count in the past 10 minutes is "5.13", and the 5 requests are sent successfully.

![API Request Summary](https://static.api7.ai/uploads/2025/04/30/ppMhTdyP_3-api-request-response.webp)

Select **Monitoring** from the side navigation bar on the API7 Enterprise dashboard. The request volume is `5`, and all 5 requests received `200` responses, consistent with the result from API7-MCP.

![Verified API Request Count](https://static.api7.ai/uploads/2025/05/06/0YyAypyY_verified-api-requests.webp)

note

The 13% deviation in the API request count could be attributed to factors such as network latency, data transmission issues, caching mechanisms, or data update delays, which are normal phenomena.

### Check QPS and Latency[â](#check-qps-and-latency "Direct link to Check QPS and Latency")

Ask Cline to check the QPS and Latency data of API7 Enterprise over the past 10 minutes.

![Check QPS and Latency](https://static.api7.ai/uploads/2025/04/30/jeZvaQKD_5-check-qps-and-latency.webp)

Cline requests to fetch QPS and latency data using the `get_prometheus_metrics` operation. Click **Approve** to authorize it.

![Fetch QPS and Latency](https://static.api7.ai/uploads/2025/04/30/FQRysF3C_6-fetch-qps-and-latency.webp)

Cline returns the monitoring data of QPS and latency for the past 10 minutes of API7 Enterprise. The result shows that the latency peaked at 181.9ms.

![QPS and Latency Summary](https://static.api7.ai/uploads/2025/04/30/pXLk2HJU_7-qps-and-latency-summary.webp)

Select **Monitoring** from the side navigation bar on the API7 Enterprise dashboard. The latency peaking at 181.9ms occurred at 11:15:55, which aligns with the conclusion from API7-MCP.

![Verified QPS Data](https://static.api7.ai/uploads/2025/04/30/VEGzLuh8_8-verified-qps.webp)

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* References
  <!-- -->
  * [Supported Operations in API7-MCP](https://docs.api7.ai/apisix/reference/apisix-mcp.md#supported-operations)
