# Source: https://docs.jit.io/docs/stackhawk-integration.md

# StackHawk Integration

# StackHawk Integration

Integrating **StackHawk** with Jit enhances your API security testing capabilities by importing findings directly into Jit's context graph.

This integration allows you to consolidate API security vulnerabilities alongside other security findings for comprehensive risk management.

## Integration Capabilities

Once integrated, Jit will:

* **Import API security findings**: **StackHawk** vulnerability data will be automatically ingested into Jit's context graph
* **View and filter findings in Jit**: Once imported, head to the Findings page in Jit, apply the Security Tool filter, and select **StackHawk** to view the results from this integration.
* **Map to applications**: Findings will be associated with corresponding applications in Jit
* **Enable unified management**: View and manage API security issues alongside other security findings

## Integration Setup

### Prerequisites

* An active **StackHawk** account
* The necessary permissions to create API keys in **StackHawk**
* A Jit account with administrative privileges

## Quickstart

1. In Jit's web app, navigate to the **Integrations page**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/788935b0a4ff5f9901455ae16d9410b43903c109fc46f73ef8b6a395b5c965c0-Screenshot_2025-04-09_at_11.06.05.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "600px"
    }
  ]
}
[/block]

2. Find the "StackHawk" card and click "Connect"
3. You will be prompted to provide the following credentials:

   * **API Key** - Generate this in your [StackHawk account settings](https://apidocs.stackhawk.com/reference/login)

[block:image]{"images":[{"image":["https://files.readme.io/983be25cca48151935cb1c55ed6274a399753267d3262b86cba64dbde848b112-image_17.png","",""],"align":"center","sizing":"600px"}]}[/block]

4. After submitting your credentials, the integration will be complete, and Jit will begin importing StackHawk findings into the context graph.

## Troubleshooting

If you encounter issues with the integration:

1. Verify your API key has the correct permissions in **StackHawk**
2. Check your network configuration to ensure Jit can reach the **StackHawk** API endpoints
3. Confirm that scans are configured and running in your **StackHawk** account
4. Contact Jit support if issues persist