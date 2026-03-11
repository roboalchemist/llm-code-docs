# Source: https://docs.axonius.com/docs/randori.md

# Randori

Randori is an attack platform that combines continuous reconnaissance, real-time target analysis, and the ability to safely execute attacks on-demand to provide an attacker’s perspective.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Randori Domain** *(required, default: `https://app.randori.io`)* – The hostname of the Randori server.
2. **API Key** *(required)* – Specify the API key provided from Randori support.
3. **Verify SSL** *(optional)* – Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* – Connect the adapter to a proxy instead of connecting it directly to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Randori\_adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Randori_adapter.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch Target Information** *(optional)* - Select whether to fetch information about the device as a target, such as the Perspective Name.
2. **Fetch Implant Information** *(optional)* - Select whether to fetch Implant information from the device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Randori API SDK document](https://github.com/RandoriDev/randori-api-sdk).