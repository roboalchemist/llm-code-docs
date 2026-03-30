# Source: https://docs.jit.io/docs/invicti-integration.md

# Invicti Integration

# Invicti Security Integration

## Overview

The Jit-Invicti Security integration empowers you to strengthen your application security by seamlessly importing Invicti's DAST findings into your security workflows.

By combining Invicti Security's comprehensive dynamic application security testing with Jit's security automation, you can prioritize vulnerabilities based on real-time risk context and ensure your most critical web applications remain protected.

## Integration Capabilities

Once integrated, you get:

* **Comprehensive DAST Visibility**: Import Invicti Security's findings from your web applications directly into Jit
* **Risk-Based Prioritization**: Leverage Invicti's risk scoring to prioritize security issues based on their actual impact
* **Streamlined Security Workflows**: Address web application security issues alongside your other security findings in one unified platform
* **Context Enrichment**: Enrich Jit's context graph with Invicti Security's findings for better issue prioritization

## Integration Setup

### Prerequisites

* An active Invicti Security account
* The necessary permissions to create API keys in Invicti
* A Jit account with administrative privileges

### Quickstart

1. In Jit's web app, navigate to the **Integrations page**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3fc61a863be486ec4628cf7e0b9ac5e95066cc0281b1aa522bab593fbf979567-Screenshot_2025-04-02_at_16.13.03.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

2. Find the "Invicti" card and click "Connect"

3. You will be prompted to provide:

   * Your Invicti Security **User ID**

   * Your Invicti Security **API Token**

[block:image]{"images":[{"image":["https://files.readme.io/839dcf6d68f99295ef451105b643354a2a3f6c8b9410b07e36a9bf74f59f9b4c-Screenshot_2025-04-02_at_16.48.38.png","",""],"align":"center"}]}[/block]

To generate the required credentials in Invicti Security:

* Navigate to the [API Settings](https://www.netsparkercloud.com/account/apisettings/) page
* Create a new API Token

4. After submitting your credentials, the integration will be complete. Jit will start pulling findings from Invicti periodically and enriching its context graph with this data.

## Troubleshooting

If you encounter issues with the integration:

1. Verify your API key has the correct permissions in Invicti Security
2. Check your network configuration to ensure Jit can reach the Invicti Security API endpoints
3. Verify that DAST scans are configured and running in your Invicti account
4. Contact Jit support if issues persist