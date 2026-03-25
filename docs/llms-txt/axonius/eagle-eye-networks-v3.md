# Source: https://docs.axonius.com/docs/eagle-eye-networks-v3.md

# Eagle Eye Networks (V3)

Eagle Eye Networks provides cloud-based video surveillance products for physical security and business operations applications.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Secret
* Refresh Token

### APIs

Axonius uses the [Eagle Eye Video API Platform](https://developer.eagleeyenetworks.com/).

#### Supported From Version

Supported from Axonius version 6.1.38.2

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Setting Up the Integration

1. Create an App in the Eagle Eye developer portal - Add a redirect URL ([http://127.0.0.1:3333](http://127.0.0.1:3333)).
   * Keep the Client ID and Client Secret for later use.

2. Replace the Client ID and Redirect URL in this URL with values from Step 1. Paste into a browser:
   * **Example**: `https://auth.eagleeyenetworks.com/oauth2/authorize?scope=vms.all&client_id=CLIENTID&response_type=code&redirect_uri=http://127.0.0.1:3333`

   * You will be prompted to log in to Eagle Eye Networks with your user credentials.

   * Upon authentication, the browser will be forwarded to the redirect URL with an appended code. Keep this code for the remaining steps.
     * **Example**: `https://127.0.0.1:3333/?code=AbCdEasdfasdfafasdfasdfasfd`

3. Get the Refresh Token and Base URL.
   * Populate the Client ID, Redirect URL, and Code from the previous step in the following curl command. You will be prompted for the Client Secret (password).

```
curl -vLkX POST --location 'https://auth.eagleeyenetworks.com/oauth2/token'  -H "accept: application/json" -H "content-type: application/x-www-form-urlencoded" -u CLIENTID
--data-urlencode 'grant_type=authorization_code'
--data-urlencode 'scope=vms.all'
--data-urlencode 'code=CODEFROMPREVIOUSSTEP'
--data-urlencode 'redirect_uri=http://127.0.0.1:3333'
```

4. Use the following data output from the previous steps to populate the Adapter Connection properties:
   * Client ID and Client Secret (Step 1)
   * Base URL and Refresh Token (Step 3)

### Required Parameters

1. **Host Name or IP Address** *(default: `https://my.tenant.eagleeyenetworks.com`)* - The hostname or IP address of the Eagle Eye Networks server that Axonius can communicate with via the required ports.
2. **Client ID** and **Client Secret** - The credentials for a user account that has permission to fetch assets.
3. **Refresh Token** - A special key that enables a client for an API or service to retrieve new access tokens without requiring the user to perform a complete login. For information on authenticating and obtaining a refresh token, see [Machine-to-machine (M2M) authentication](https://developer.eagleeyenetworks.com/docs/login-confidential-client#phase-2-machine-to-machine-m2m-authentication).

![EagleEyeNetworksV3.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EagleEyeNetworksV3.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices of sub type device0 from Bridges Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'device0' from the Bridges endpoint. Disable this option to not fetch devices of the subtype 'device0' from the Bridges endpoint.
2. **Fetch Devices of sub type device1 from Cameras Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'device1' from the Cameras endpoint. Disable this option to not fetch devices of the subtype 'device1' from the Cameras endpoint.
3. **Fetch Devices of sub type device2 from Displays Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'device2' from the Displays endpoint. Disable this option to not fetch devices of the subtype 'device2' from the Displays endpoint.
4. **Fetch Devices of sub type device3 from Speakers Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'device3' from the Speakers endpoint. Disable this option to not fetch devices of the subtype 'device3' from the Speakers endpoint.
5. **Fetch Users from Users Endpoint** - Enable this option to fetch users from the Users endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>