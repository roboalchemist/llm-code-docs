# Source: https://docs.axonius.com/docs/gigamon-threatinsight.md

# Fortinet FortiNDR Cloud

Fortinet FortiNDR Cloud is a cloud-native network detection and response (NDR) platform that provides threat activity detection and the data and context needed for cybersecurity response and investigation.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Token

### Permissions

The value supplied in [API Token](#required-parameters) must be associated with credentials that have permissions to fetch assets.

A token is required to access Fortinet FortiNDR Cloud APIs. To generate a token:

1. From the **Profile Settings**, select **API Tokens**.
2. Under the **Token** section, click **Create New Token**. Be sure to immediately save the token in a secure location, such as a password manager, as the token will not be viewable after you close the display.

All tokens you have created will be listed in the **Token** section. You can delete tokens by clicking **Revoke** for the target token.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://sensor.icebrg.io`)* - The hostname or IP address of the Fortinet FortiNDR Cloud server.
2. **API Token** - An API token associated with a user account that has the Required Permissions to fetch assets.

![Fortinet FortiNDR Cloud new.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Fortinet%20FortiNDR%20Cloud%20new.png)

### Optional Parameters

1. **Account UUID** - Enter an account UUID in order to fetch the users from a different API endpoint that includes more data and user groups. Find the account UUID on the Account `>` Account management API page, during creation of an OAuth client.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Limit fetched data to last x days** *(required, default: 7)* - Specify for how many days   this adapter will fetch data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>