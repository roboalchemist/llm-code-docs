# Source: https://docs.jit.io/docs/bright-integration.md

# Bright Integration

# Bright Security Integration

## Overview

The Jit-Bright Security integration empowers you to strengthen your application security by seamlessly importing Bright's DAST findings into your security workflows.

By combining Bright Security's comprehensive dynamic application security testing with Jit's security automation, you can prioritize vulnerabilities based on real-time risk context and ensure your most critical web applications remain protected.

## Integration Capabilities

* **Comprehensive DAST Visibility**: Import Bright Security's findings from your web applications directly into Jit
* **Risk-Based Prioritization**: Leverage Bright's risk scoring to prioritize security issues based on their actual impact
* **Streamlined Security Workflows**: Address web application security issues alongside your other security findings in one unified platform
* **Context Enrichment**: Enrich Jit's context graph with Bright Security's findings for better issue prioritization

## Integration Setup

### Prerequisites

* An active Bright Security account
* The necessary permissions to create API keys in Bright
* A Jit account with administrative privileges

### Quickstart

1. In Jit's web app, navigate to the **Integrations page**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4f964688cd8f66d3d0d7afafc79ad1755d61072f641c31fb2a49f37277e9be34-Screenshot_2025-04-02_at_16.12.01.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

2. Find the "Bright" card and click "Connect"
3. You will be prompted to provide your Bright Security **API Key**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c214eeb29d93b03075607b41a9dec26caeb5fa4d19d8469de2b2ee1b22e564c4-Screenshot_2025-04-02_at_16.22.10.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

To generate an API key in Bright Security:

* Navigate to the **User Settings** page
* Create a new API key with the following scopes:

  * `issues.read`

  * `org.read`

  * `projects.read`

  * `scans.read`

  * `user.read`

[block:image]{"images":[{"image":["https://files.readme.io/d3bd59524abfbd5225078460048d6cdc9fa48fc74b7b411cdcad746c95790f19-Screenshot_2025-04-02_at_16.53.49.png","",""],"align":"center","sizing":"400px"}]}[/block]

> ℹ️ For detailed instructions, refer to the [Bright documentation](https://docs.brightsec.com/docs/manage-your-personal-account#managing-your-personal-api-keys-authentication-tokens)

4. After submitting your credentials, the integration will be complete. Jit will start pulling findings from Bright periodically and enriching its context graph with this data.

## Troubleshooting

If you encounter issues with the integration:

1. Verify your API key has the correct permissions in Bright Security
2. Check your network configuration to ensure Jit can reach the Bright Security API endpoints
3. Confirm that DAST scans are configured and running in your Bright account
4. Contact Jit support if issues persist