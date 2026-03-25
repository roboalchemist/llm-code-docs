# Source: https://docs.axonius.com/docs/tailscale.md

# Tailscale

Tailscale is a "zero config" mesh VPN and Zero Trust Network Access (ZTNA) solution for creating a secure, private network (a "tailnet") connecting all your systems, no matter where they are. Tailscale leverages the WireGuard protocol for fast, encrypted, peer-to-peer connections, bypassing firewall/NAT hassles.

## Integrations

Axonius integrates with Tailscale to: :

Discover assets:

* **Devices**: Servers or Client devices part connected to your Tailnet.
* **Users**: Users in your tailnet network or with access to your Tailscale admin interfaces.

Drive action (via Workflows and Enforcements):

* [Authorize Asset - Tailscale](/docs/authorize-asset-tailscale): Grant permission for a device asset to join and be part of your Tailscale network (tailnet).

***

## Setup

<Accordion title="Requirements" icon="fa-info-circle">
  To integrate Axonius with Tailscale, you will need

  * **Tailnet id**: A unique ID provided by Tailscale that identifies your tailnet in API calls.
  * **API Credentials**: For authorizing access within Tailscale. Tailscale offers two types of API credentials:
    * A reusable **auth key** and **secret**.
    * An **API access token**
  * **A service account (optional)**: To simplify management and avoid accidental interruption due to account deactivation, the credentials should be associated with a dedicated admin or service account.
</Accordion>

To integrate Axonius and TailScale, you need to obtain the key in TailScale, and then configure the adapter in Axonius:

### Obtain a key in Tailscale

1. Access the <Anchor label="Tailscale settings" target="_blank" href="https://login.tailscale.com/admin/settings/general">Tailscale settings</Anchor> as administrator.
2. Click **General** and then record your **Tailnet ID**.
3. Click **Keys**
4. Click **Generate auth key** or **Generate access token** to create your token.\
   **Tip:** If you opted for generating an **auth key**, make sure to select **Reusable**.
5. Follow the instructions in the screen to create your token.
6. Record the newly generated key.\
   **Tip**: If you created an auth key, also record the respective ID in the auth keys table.

### Configure Axonius

1. Access your Axonius Dashboard as an Administrator
2. Click **Adapters**.
3. Search for and then open the **Tailscale** Adapter.
4. Click **Add Connection**.
5. Enter the following information:
   1. **Tenant name**: The **Tailnet ID** copied from Tailscale.
   2. **API Key**: The **API Key** copied from Tailscale. (*if you opted for using the API access token*)
   3. **Client ID** and **Client Secret**: copied from Tailscale account (*if you opted for using the auth key*)
   4. **Connection Label**: An identifier for the connector. Example "**tailscale-prd**"
6. (Optional) Enter additional parameters for the adapter connectivity:
   1. **HTTPS Proxy (proxy url, username, and password)**: In case you use a proxy for connection
   2. **Verify SSL**: If you want to verify the SSL certificate of Tailscale against a CA database in of Axonius.
   3. **Gateway**: If you want the adapter traffic to be routed by an Axonius Gateway.

***

## Additional Specifications

This section provides additional specifications on parameters, advanced configurations, APIs, and the supported versions within the Tailscale adapter.

### Parameters

1. **Tenant Name** *(required)* - The domain or name associated with your Tailscale server.
2. **API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **Client ID** and **Client Secret** are not supplied, **API Key** is required.
</Callout>

5. **Client ID** and **Client Secret** *(optional)* - The credentials for a user account that has permission to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Key** is not supplied, **Client ID** and **Client Secret** are required.
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Tailscale" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tailscale.png" />

### Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Users** *(required, default: true)*   - Select this option to fetch users

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### APIs

Axonius uses the [Tailscale API](https://tailscale.com/api#tag/devices/GET/device/`\{deviceId}`).

### Supported From Version

Supported from Axonius version 4.6

<br />