# Source: https://docs.jit.io/docs/traceable-integration.md

# Traceable Integration

# Traceable Integration with Jit

Integrating **Traceable** with Jit to centralize your API security findings, enabling a unified view of vulnerabilities across your applications. This integration allows you to import API security issues detected by **Traceable** into Jit’s context graph, facilitating streamlined vulnerability management.

## Integration Capabilities

Once integrated, Jit will:

* **Import API security findings**: **StackHawk** vulnerability data will be automatically ingested into Jit's context graph
* **Map to applications**: Findings will be associated with corresponding applications in Jit

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d573b148280232aa9884a305814972eb8e4488fbef1b921298104beeb25eaf07-Screenshot_2025-06-18_at_9.56.49.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

* **Enable unified management**: View and manage API security issues alongside other security findings

## Prerequisites

* An active Traceable account with appropriate permissions to generate API tokens.
* Access to your Traceable platform URL (e.g., <https://app.us1.traceable.ai/>).

## Integration Setup

1. **Navigate to Jit’s [Integrations Page](https://platform.jit.io/integrations):**

   * Log in to your Jit account.

   * Go to the Integrations section.

   * Locate the Traceable integration card and click on **Connect**.

[block:image]{"images":[{"image":["https://files.readme.io/c796ae1ef1d812f1b05ffcd63e4eb84a2b03e94e5178bf550faa0f8b6b42de9c-Screenshot_2025-06-05_at_10.09.10.png","",""],"align":"center"}]}[/block]

2. **Enter Integration Details:**
   * **API Token:**
     * In your Traceable platform, navigate to **Your Profile > My Preferences > API Tokens.**
     * Generate a new API token and copy it.
     * Paste the token into the **API Token** field in Jit.
   * **Region:**
     * Determine your Traceable region based on your platform URL.
     * For example, if your platform URL is <https://app.us1.traceable.ai/>, your region is **api.us1**.
     * Enter the region identifier (e.g., **api.us1**) into the Region field in Jit.
       > ❗️ The region should be prefixed with api
3. **Complete the Integration:**

   * After entering the required information, click on **Continue**.

   * Upon successful connection, the integration status will update, and you will have the option to **Disconnect** if needed.

[block:image]{"images":[{"image":["https://files.readme.io/04ad56cfa37af765cc988a3eb5ecf2ecf4c59babe1cddd806c143ea47054d89b-Screenshot_2025-06-05_at_10.33.10.png","",""],"align":"center","sizing":"604px"}]}[/block]

## Post-Integration Behavior

* Traceable’s API security findings will be automatically ingested into Jit’s context graph.
* These findings will be associated with the relevant applications managed within Jit.