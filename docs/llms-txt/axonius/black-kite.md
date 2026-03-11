# Source: https://docs.axonius.com/docs/black-kite.md

# Black Kite

Black Kite provides cyber risk assessments that analyze the organization’s supply chain cybersecurity posture from three dimensions: technical, financial and compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Domains & URLs

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Black Kite server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="BlackKite" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BlackKite.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Items to fetch** *(required)* - Select one or more options to include in the fetch. By default, all items are selected. Clear options that you want to exclude from the fetch.

<Callout icon="📘" theme="info">
  Note

  At least one of the options in the **Items to fetch** dropdown must be selected.
</Callout>

2. **Fetch Subdomains as Domains & URLs** - Select this option to fetch subdomains as URLs instead of devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the <Anchor label="Black Kite Cyber Risk Scorecard API" target="_blank" href="https://app.blackkitetech.com/ApiDocs/v2/swagger/">Black Kite Cyber Risk Scorecard API</Anchor>.

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5