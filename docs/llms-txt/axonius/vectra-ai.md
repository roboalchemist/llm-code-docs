# Source: https://docs.axonius.com/docs/vectra-ai.md

# Vectra AI

Vectra AI is a cybersecurity platform that uses AI to detect and respond to cyberattacks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users

## Parameters

1. **Vectra Domain** *(required)* - The hostname of the Vectra server.
2. **Deployment** *(required)* - Select either **On-Prem** or **Cloud**.
3. **API Token** *(optional)* - An API token generated in Vectra.

<Callout icon="📘" theme="info">
  Note

  When **On-Prem** deployment is selected, **API Token** is required.
</Callout>

4. **Client ID** and **Client Secret** *(optional)*  - The credentials for a user account that has permission to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **Cloud** deployment is selected, **Client ID** and **Client Secret** are required.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Vectra AI](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vectra%20AI.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Devices per page** *(default: 500)* - Specify the number of devices fetched per page.
2. **Enrich Host Data** - Select this option to fetch extra data about each host/device, including an asset with a low risk status.
3. **Enrich detections data** - Select this option to fetch extra data about detections.
4. **Fetch Users** - Select this option to fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## API

Axonius uses the Vectra API v2.1.

## Required Permissions

The value supplied in [Client ID](#parameters) must have read-only permissions in order to fetch assets.