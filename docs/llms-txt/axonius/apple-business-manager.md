# Source: https://docs.axonius.com/docs/apple-business-manager.md

# Apple Device Management (formerly Apple Business Manager)

Apple Device Management (formerly Apple Business Manager) supports deployment and remote MDM enrollment of corporate-owned Apple devices.

## Assets Types Fetched

This adapter fetches the following types of assets:

* Devices

<Callout icon="📘" theme="info">
  Note

  * To Fetch MDM devices in Axonius - use the respective Axonius Adapter for your MDM solution (JAMF, Azure, SimpleMDM, etc) and connect directly.

  * This adapter only fetches devices which are unassigned to an MDM (and does not fetch devices assigned to an MDM).

  * This adapter is useful if you want to fetch  ‘unprovisioned or unattached’ MDM devices.
</Callout>

## Before You Begin

### APIs

Axonius uses the [Get Device Details API](https://developer.apple.com/documentation/devicemanagement/get_device_details).

### Authentication Methods

* Client Key and Client Secret
* OAuth2 Authentication - required to fetch data from organization devices

### Generate Client Key and Secret

**To obtain a client key and client secret**

1. Generate the Key pair:

   ```
   openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
   ```

2. Save the **key.pem** file, which is used to decrypt the token.

3. In Apple Business Manager, go to **Settings** → **MDM Servers**, select an existing MDM server or click **Add MDM Server**, and upload the **cert.pem** file.

4. Download the **Token** file (.p7) and decrypt it with key.pem

   ```
   openssl smime -decrypt -inform smime -in fileFromApple.p7 -inkey key.pem
   ```

5. Utilize the values from the decrypted token file for the corresponding fields in the adapter configuration: consumer key, consumer secret, access token, access secret
   For more information, see [Authenticating with a Device Enrollment Program (DEP) Server](https://developer.apple.com/documentation/devicemanagement/device_assignment/authenticating_with_a_device_enrollment_program_dep_server).

## Connecting the Adapter in Axonius

### Required Parameters - General

1. **Host Name or IP Address** *(default: `https://mdmenrollment.apple.com/`)* - The hostname or IP address of the Apple Business Manager server.

### Required Parameters - Client Key and Client Secret Authentication

1. **Client Key** and **Client Secret** - The credentials for a user account that has permissions to fetch assets.
   See [generate a client key and secret](/docs/apple-business-manager#generate-client-key-and-secret) for more information.

2. **Access Token** and **Access Secret** - The credentials associated with a user account that has permissions to fetch assets.

### Required Parameters - OAuth2 Authentication

1. **Use OAuth2 for enrichments** - Enable this to use OAuth2 Authentication and provide the parameters listed below.
2. **Private Key File** - A non-encrypted (passphrase free) private key file.
3. **Client ID**  and **Key ID** - For information on how to generate these parameters, see [Create a client assertion](https://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-and-business-manager-api#Create-a-client-assertion) in the Apple API documentation.

<Image alt="apple business manager parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/AdapterBusinessManagerParameters.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch profiles** - Select this option to fetch profiles.
* **Fetch organization devices info** - Select this option to fetch organization devices information. To fetch this data successfully, you must enable **Use OAuth2 for enrichments** in the **Add Connection** drawer and provide the required parameters.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

## Supported From Version

Supported from Axonius version 4.6