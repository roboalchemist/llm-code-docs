# Source: https://docs.jit.io/docs/sweet-security-integration.md

# Sweet Security Integration

## Overview

The Jit–Sweet Security integration enriches your vulnerability findings with runtime context by importing package runtime data from Sweet Security into Jit.

Jit can identify which vulnerable packages are actually loaded, executed, or communicating at runtime, helping you prioritize the vulnerabilities that matter most.

By combining Sweet Security's cloud-native runtime visibility with Jit's security automation, you can focus on issues that have real runtime impact and keep your most critical applications protected.

## Integration Capabilities

Once integrated, you get:

* **Runtime visibility**: Jit imports which packages are in use at runtime from Sweet and links that data to packages and SCA findings in the knowledge graph.
* **Context graph enrichment**: The knowledge graph is enriched with Sweet’s runtime package data so relationships and attributes reflect actual usage.
* **Unified Security Workflow**: Findings whose vulnerable package is confirmed in use at runtime get the "Runtime Validated" factor so you can prioritize and filter them in the Findings page.

## Integration Setup

### Prerequisites

* An active [Sweet Security](https://app.sweet.security) account.
* Permissions to create API tokens in Sweet Security.
* A Jit account with administrative privileges.

### Quickstart

1. In Jit's web app, go to the **Integrations** page.

[block:image]{"images":[{"image":["https://files.readme.io/2bb5cf56a4806c5eb4a2281c1e6ab4c412abe8839711580a3662bf6d7f3f7659-integration_page.png","",""],"align":"center"}]}[/block]

2. Find the **Sweet Security** card and click **Connect**.

[block:image]{"images":[{"image":["https://files.readme.io/ff5b83e006f6cdd8599f050a74b22e1e25b9844672c0b4da8da42dab7e1ee4a0-sweet_integration_card.png","",""],"align":"center"}]}[/block]

3. When prompted, provide:

   * **Client ID**: Your Sweet Security **API Key**

   * **Client Secret**: Your Sweet Security **Secret**

[block:image]{"images":[{"image":["https://files.readme.io/bad5bae754114c4967d0a6621d7782f7fc3a05f5202d8809213bbf7b44b28d90-sweet_card_creds.png","",""],"align":"center"}]}[/block]

```
  To get these in Sweet Security:
```

* Open the [Sweet Security App](https://app.sweet.security).

* Click your name → **Settings**.

* Go to **API Tokens** and create an API token.

* Use the **API Key** as Client ID and the **Secret** as Client Secret in Jit.

[block:image]{"images":[{"image":["https://files.readme.io/bf18bbbe63c95d032f8650fe4e53eb9e871bc611434c7dc2f4360de333d7647d-sweet_portal_token.png","",""],"align":"center"}]}[/block]

4. After submitting your credentials, the connection is complete. Jit will start syncing package runtime data from Sweet Security and use it to enrich findings.

## Data Synchronization

After the integration is connected, Jit periodically pulls package runtime data from Sweet Security and links it to existing packages in the knowledge graph. The package enrichment pipeline then uses this to set runtime validation flags and improve prioritization. You do not need to configure anything else for ongoing sync.

## Troubleshooting

If you run into issues:

1. **Check credentials**: Ensure the API token in Sweet Security is valid and has the right scopes. Use the API Key as Client ID and the Secret as Client Secret in Jit.
2. **Network and endpoints**: Confirm Jit can reach Sweet's API (`https://eapi.sweet.security`). If you use a proxy or firewall, allow these calls.
3. **Integration status**: In Jit, open Integrations and confirm Sweet Security shows as connected. If it shows an error, try disconnecting and reconnecting with the same credentials.

For further help, contact [Jit Support](https://www.jit.io/contact).