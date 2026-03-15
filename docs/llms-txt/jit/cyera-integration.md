# Source: https://docs.jit.io/docs/cyera-integration.md

# Cyera Integration

# Integrating Cyera with Jit

Integrating **Cyera** with Jit enhances security workflows by synchronizing data security findings and risks between the two platforms. This integration enables the enrichment of Jit's context graph with Cyera's data security insights, allowing teams to stay informed about sensitive data exposure and security risks in their AWS environment.

Jit integrates with Cyera to:

1. Automatically ingest Cyera's data security findings into Jit's context graph
2. Enrich Jit's context with AWS resource information and data classification details
3. Provide daily updates of security issues.

# Integration Setup

## Quickstart

1. In Jit's web app, navigate to the **Integrations page**:

[block:image]{"images":[{"image":["https://files.readme.io/3382c872815b70bce0cee0bfaa632d814514bcca0b213b70a9d924c7d6e6655a-Screenshot_2025-02-09_at_15.34.58.png","",""],"align":"center"}]}[/block]

2. Find the "Cyera" card and click "Connect".

3. You will be prompted to provide:

[block:image]{"images":[{"image":["https://files.readme.io/f02d4794513b4a7cde43a77c137e6e52f43e51c8db1d9171f38853e1e6300166-Screenshot_2025-02-09_at_15.36.24.png","",""],"align":"center"}]}[/block]

* Your Cyera **Client ID** and **Client Secret** (generated from the Cyera dashboard)
  * Choose a role that has the following permissions:
    * `cyera.read.issue`
    * `cyera.manage.global-scope`
* Your Cyera **API Region**:
  * `api` for US
  * `api-eu` for EU
  * `api-ca` for Canada
  * `api-ap` for Asia Pacific

For more information about API regions, see the [Cyera API documentation](https://api.cyera.io).

4. After submitting your credentials, the integration will be complete. Jit will automatically begin enriching its context graph with Cyera data security findings.

## Integration Capabilities

Once integrated, you get:

* **Automated Data Security Insights**: Cyera automatically scans and identifies AWS issues daily, providing fresh security insights every day.

* **Context Enrichment**: Cyera findings enrich Jit's context graph by providing:
  * Data sensitivity classifications
  * Risk severity levels
  * Remediation recommendations
  * Detailed issue descriptions and impact analysis

This integration helps streamline security workflows by providing comprehensive visibility into data security risks across your AWS environment, all visualized within the Jit platform.