# Source: https://docs.axonius.com/docs/vmware-sd-wan.md

# VMware SD-WAN

VMware SD-WAN (formerly by VeloCloud) is a software-based network technology that virtualizes WAN connections.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the VMWare SD-WAN server.

2. **Enterprise Logical ID** *(required)* - Enter your Enterprise ID. To find your Enterprise ID:
   * **For partners:**
     1. Log in to Orchestrator and navigate to **Monitor Customers**.
     2. Select a customer or an edge device. The ID should be visible in the URL or in the device's details page.
   * **For enterprise users:** Log in to Orchestrator. The Enterprise Logical ID should be visible in the URL when viewing your environment details page, or listed in a specific **Account Information** or **Company Details** section after logging in.

3. **API Key/Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate an API Token, see [Configure Operator Users](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/dita/sde/velocloud-sase/velocloud-legacy-pdfs/user-guides-legacy/vmware-sd-wan-operator-guide_4.4.pdf) (page 66).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="VMware%20SD-WAN" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VMware%20SD-WAN.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch client devices** - Select this option to fetch devices of the type "Client device" in addition to the other devices fetched by the adapter.
2. **Fetch edge device profile settings** - Select this option to enrich edge devices with profile settings data. The data is available in the Devices page under the 'Is Zscaler Enabled' column.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the VMware SD-WAN Orchestration API v2

## Required Permissions

The value supplied in [API Key/Token](#parameters) must be associated with credentials that have Read permissions for enterprises, client devices and edges to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version       | Supported | Notes |
| ------------- | --------- | ----- |
| API Version 2 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7