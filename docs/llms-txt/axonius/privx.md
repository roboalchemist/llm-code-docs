# Source: https://docs.axonius.com/docs/privx.md

# PrivX

PrivX provides privileged access to on-prem and cloud environments, including control access to servers, network devices, and other critical infrastructure according to user roles and privileges.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PrivX server.

2. **OAuth Client ID**, **OAuth Client Secret**, **API Client ID**, and **API Client Secret** *(required)* - The credentials for an API client that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="privx" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-G67X5252.png" />

## APIs

Axonius uses the <Anchor label="SSH PrivX  API Guide " target="_blank" href="https://privx.docs.ssh.com/v41/api">SSH PrivX  API Guide </Anchor>.

* The [endpoint](https://privx.docs.ssh.com/api/connection-manager/connections#list-connections) provides all the connection details per device.

## Required Ports

* HTTPS port 443

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Using instance-id as hostname** - Select to use the instance ID as the asset's hostname.
2. **Try resolving FQDN addresses to IP Addresses** - Select this to have the adapter do the following: parse each address to network interfaces, check if the address is an FQDN, and if it is, try to resolve it to its proper IP address.
3. **Enable connections enrichment** - Toggle this setting on for the system to collect details about device connections.
   * **Number of days ago to fetch connections details** - When **Enable connections enrichment** is enabled, specify how many days back from the current date the system should collect connection information.
     The connection details fetched include:
     * **Who accessed the device** - This information is categorized into two parts:
       * *user\_data* - The user's display name.
       * *user\_roles* -  The user's role name.
     * **From what IP** - The *remote\_address* from which the connection originated.
     * **Length of connection** - The *duration* of the connection.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The values supplied in [**OAuth Client ID**, **OAuth Client Secret**, **API Client ID** and **API Client Secret**](#parameters) must have read access to devices and users.

**To create an API client**

1. Log as a system admin to the PrivX server
2. Go to **Settings** → **Deployment** → **Integrate with PrivX using API Clients**
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1168\).png)
3. Click **ADD API CLIENT**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1169\).png)
4. Select the following permissions:
   * users-view
   * hosts-view
5. Click **SAVE**.
   The client API credential will be displayed. Use those in the adapter connection parameters.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                               | Supported | Notes |
| ------------------------------------- | --------- | ----- |
| SSH PrivX Authentication API:   1.0.1 | Yes       |       |
| SSH PrivX Local User Store API: 1.0.3 | Yes       |       |
| SSH PrivX Host Store API:       1.0.3 | Yes       |       |