# Source: https://docs.jit.io/docs/upwind-integration.md

# Upwind Security Integration

The Jit-Upwind integration empowers you to enhance your security posture by seamlessly importing Upwind’s runtime vulnerability findings into your security workflows.\
By combining Upwind’s real-time risk context with Jit’s security automation, you can prioritize vulnerabilities based on actual exploitability and ensure your most critical assets remain protected.

# Integration Capabilities

* **Runtime Risk Context**: Ingest Upwind’s findings, enriched with runtime context such as exploitability, internet exposure, and production impact.
* **Contextual Prioritization**: Leverage Upwind’s insights to prioritize vulnerabilities that pose real-world risks.
* **Unified Security Workflow**: Address vulnerabilities alongside other security findings in Jit’s unified platform.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ed0e3063317ab0e515d54bb6ad6a7bbd19bfd5bd7df6cbacc3cba4c1b38fb38a-upwind-issue-cve.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

## Integration Setup

### Prerequisites

* An active Upwind account with administrative privileges.
* The necessary permissions to create API credentials in Upwind.
* A Jit account with administrative privileges

### Step 1: Generate API Credentials in Upwind

1. Navigate to the [Upwind Credentials Page](https://console.upwind.io/settings?mainPageTab=Credentials) to generate your API credentials.
2. Click on **Generate Credentials**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/079897e78e257813449cd5fbbdc1faf88d1ed7d2a3a906c090b8bf95a8befd7b-Screenshot_2025-04-24_at_12.37.51.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

3. In the **Client credentials**, select the **API** option.
4. Provide a descriptive name for the credentials (e.g., “Jit-Integration”).
5. Click **Generate** to create the credentials.
6. Securely store the generated **Client ID** and **Client Secret**; these will be used in the Jit integration setup.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/016d8eb8d7ca2fa074a0c38794d9fbb8840cb7155e701eaa5dd08943a04d0c47-Screenshot_2025-04-24_at_12.40.05.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

For more detailed instructions, refer to the official Upwind documentation: [Credentials](https://docs.upwind.io/settings/credentials).

### Step 2: Retrieve Your Upwind Organization ID

1. In the [Upwind Settings Page](https://console.upwind.io/settings).
2. Your Organization ID will be displayed at the top of the page.
3. Copy this ID for use in the Jit integration configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0b26b3b427a3287cdd4c50c54f50017e8d8dd5f222ea2445c66a1ba86a918106-Screenshot_2025-04-24_at_12.46.50.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Step 3: Configure the Integration in Jit

1. Log in to your Jit account.
2. Navigate to [Integrations page](https://platform.jit.io/integrations) and select Upwind.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f0bbf22cb36b845342f8c4d09a0a12fbbe747081cf925bfb334eb7e4e210e8f7-Screenshot_2025-04-24_at_12.51.31.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

3. Click on **Connect** to open the configuration modal.
4. In the Configuration modal, click **Connect** and enter the following details:

* **Client ID**: Paste the Client ID obtained from Upwind.
* **Client Secret**: Paste the Client Secret obtained from Upwind.
* **Organization ID**: Paste your Upwind Organization ID.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/44f30660cbe49ba1a628a03e952c2fdbcda7e3424c08f200a54792cce65effcc-Screenshot_2025-04-24_at_12.55.06.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

5. Click **Continue** to establish the connection.

## Data Synchronization

Once configured, Jit will periodically pull vulnerability data from Upwind and ingest it into the Knowledge Graph. This process ensures that your security insights are up-to-date and integrated with other data sources for comprehensive analysis.

<br />

For further assistance, please contact Jit Support.