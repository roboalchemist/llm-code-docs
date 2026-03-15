# Source: https://docs.jit.io/docs/orca-integration.md

# Orca Integration

# Orca Security Integration

The Jit-Orca Security integration empowers you to strengthen cloud security by seamlessly importing Orca's cloud security findings into your security workflows.

By combining Orca Security's comprehensive visibility across cloud environments with Jit's security automation, you can prioritize vulnerabilities based on real-time risk context and ensure your most critical cloud assets remain protected.

# Integration Capabilities

* **Comprehensive Cloud Security Visibility**: Ingest Orca Security's findings across your cloud environments directly into Jit
* **Context Enrichment**: Enrich Jit's context with Orca Security's findings, for better prioritization

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dad94eeeb7c1826c934dcaa4336bcd48c7ac3f58778dc17efbabed402221d979-Orca_Graph.png",
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

* An active Orca Security account
* The necessary permissions to create API keys in Orca
* A Jit account with administrative privileges

### Quickstart

1. In Jit's web app, navigate to the **Integrations page**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c08b4d53dcf1281c8fdfd2038eb81d7da833fd3529c61cd028c8b2c86ff64940-Screenshot_2025-04-02_at_12.23.43.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

2. Find the "Orca Security" card and click "Connect"
3. You will be prompted to provide:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7470663962ab44082aab2a6ea62e3464be17c48ea6ef6db804f4120b0ab6d241-Screenshot_2025-04-02_at_12.25.25.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

* Your Orca Security **API Key** with **Read** access to the `/query/` API
* Your Orca **API Region** based on your location:
  * **US**: Enter `api` for users in the US
  * **Europe**: Enter `app.eu` for users in Europe
  * **Australia**: Enter `app.au` for users in Australia
  * **India**: Enter `app.in` for users in India
  * **Israel**: Enter `api.il` for users in Israel
  * **Brazil**: Enter `api.sa` for users in Brazil
  * **US Gov**: Enter `app.us.gov` for US Government users

> ℹ️ For detailed instructions, refer to the [Orca documentation](https://docs.orcasecurity.io/docs/managing-api-tokens)

4. After submitting your credentials, the integration will be complete. Jit will start pulling findings from Orca periodically and enriching its context graph with this data.

## Troubleshooting

If you encounter issues with the integration:

1. Verify your API key has the correct permissions in Orca Security
2. Confirm you've selected the correct API region for your Orca account
3. Check your network configuration to ensure Jit can reach the Orca Security API endpoints
4. Contact Jit support if issues persist