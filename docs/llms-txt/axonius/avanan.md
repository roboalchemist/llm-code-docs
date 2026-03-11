# Source: https://docs.axonius.com/docs/avanan.md

# Check Point Harmony Email & Collaboration (Avanan)

Check Point Harmony Email & Collaboration (formerly Avanan) is a solution that provides inline API‑based protection for email and collaboration platforms to block phishing, malware, zero‑day threats, account takeovers, and data leaks before delivery.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users |    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Application ID/Secret Key

### APIs

Axonius uses the Avanan SmartAPI and the Avanan MSP SmartAPI.

### Permissions

* Authentication requires credentials: You must obtain the following from Avanan Support:
  * Application ID (App ID)
  * Secret Key
  * These are tied to your MSP or tenant account and are not publicly self-generated.

* **Access Token Generation**:
  A valid JWT token must be retrieved by calling the `/auth` endpoint using:
  * Your App ID
  * A time-based request signature (`x-av-sig`)
  * A unique request ID (`x-av-req-id`)​
  * **Token Usage**: The JWT token returned must be included in all subsequent API requests via the `x-av-token` header. Without it, requests will be unauthorized.

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Check Point Harmony Email & Collaboration, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Avanan server. Use the correct base URL based on your tenant's region (All endpoints follow the pattern: `{region_url}/v1.0/{endpoint}`).

| Region                     | URI Base                               |
| -------------------------- | -------------------------------------- |
| USA                        | smart-api-production-1-us.avanan.net   |
| Europe                     | smart-api-production-1-eu.avanan.net   |
| Canada                     | smart-api-production-1-ca.avanan.net   |
| Australia                  | smart-api-production-5-ap.avanan.net   |
| United Kingdom             | smart-api-production-1-euw2.avanan.net |
| United Arab Emirates (UAE) | smart-api-production-1-mec1.avanan.net |
| India                      | smart-api-production-1-aps1.avanan.net |

2. **Application ID**  - Enter the application ID to be used to get the token.
3. **Secret Key** - Enter the secret key that should be shared and stored securely.

<Image alt="Avanan.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Avanan.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Incidents from the last X days** *(optional, default: 30)* - Specify the number of days back to fetch the incidents.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>