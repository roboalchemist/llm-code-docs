# Source: https://docs.axonius.com/docs/cisco-sntc.md

# Cisco Smart Net Total Care (SNTC)

Cisco Smart Net Total Care (SNTC) portal provides current information about your installed base, contracts, and alert status to enhance the efficiency of your support workflows.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://apix.cisco.com`)* - The hostname or IP address of the Cisco Smart Net Total Care server.

2. **Client ID** *(required)* - An API Key associated with a user account that has the API Developer role  to fetch assets.

3. **Client Secret** *(required)* - An API Secret Key associated with a user account that has permissions to fetch assets.
   To obtain the **Client ID** and **Client Secret**:

   1. Login to the Cisco API Developer portal.
   2. Search for the Services APIs that you are interested in using, such as "inventory".
   3. Select the API link, then click **Request API access** from the top right corner.
   4. Click **New Application** (unless you have a pre-existing application registration that you want to use). The **Add Application** dialog is displayed.
   5. In the **Name** field, enter: axonius (recommended)
   6. From the **OAuth 2.0 Grant Type** section, select **Client Credentials Grant**.
   7. Click **Add**.
   8. Accept the terms and conditions and click **Request API Access**. The Client ID and Client Secret are displayed.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CiscoSNTC](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoSNTC.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch devices hardware info** - Select this option to fetch devices hardware information.
2. **Fetch devices software info** - Select this option to fetch devices software information.
3. **Fetch hardware coverage information (warranty included)** - Select this option to fetch hardware coverage information.
4. **Fetch device coverage** - Select this option to fetch device coverage.
5. **Fetch hardware EOL** - Select this option to fetch hardware EOL.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Cisco Services API](https://developer.cisco.com/docs/service-apis/#!application-registration).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**: REST API

## Required Permissions

The value supplied in [User Name](#parameters) must have the following permissions:\
a - /inventory

b - /customer-info

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5