# Source: https://docs.axonius.com/docs/success-factors.md

# SAP SuccessFactors

SAP SuccessFactors manages various aspects of HR operations, including recruitment, employee performance, HR analytics, payroll, and learning.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* **Basic Authentication** (for Cloud): User Name/Password
* **OAuth2 Authentication** (for on-prem): Client ID, Company ID, Username and Private Key

### Generating a Private Key

To connect the adapter using OAuth2 Authentication you need to first generate a private key:

1. Generate a local X.509 certificate.
2. Upload the public certificate to SuccessFactors.
3. Use the the private, **unencrypted** certificate as the **Private Key** parameter.

[Learn how to create a X.509 certificate using your own tools](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/creating-x-509-certificate-using-your-own-tools).
[Learn how to create an X.509 certificate in SAP SuccessFactors](https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/creating-x-509-certificate-in-sap-successfactors).

### APIs

Axonius uses the [SAP SuccessFactors API (OData V2)](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/03e1fc3791684367a6a76a614a2916de.html).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 5.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the SAP SuccessFactors server.
2. **Authentication Method** - Select Authentication method, either **Basic Authentication** (default) or **OAuth2 Authentication**.
   * **Basic Authentication**:
     * **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets. Note that **User Name** should have a @ and the company ID at the end. <br />Example: "\{username}@\{company ID}"
   * **OAuth2 Authentication**:
     * **Client ID** - When you choose OAuth2 as the authentication method, specify the Client ID to be used to authenticate the request. Note that you must add the IP address of your Axonius system as 'allow listed origins' during API Key credential setup. For more information, see [Restricting Access to APIs by IP Address](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/265b5fa29d0a426d943cba2ae57e079b.html).
     * **Company ID** - This value is prefilled based on the instance of the company currently logged in.
     * **Username** - Enter the username required for authentication.
     * **Private Key** - Upload the private key you generated according to the instructions in [Generating a Private Key](/docs/success-factors#generating-a-private-key).

<Image alt="SAP%20Success%20Factors" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAP%20Success%20Factors.png" />

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

* **Enable Custom Parsing** Enable this option to define how to parse specific fields from the raw data fetched. You can choose to parse the data into an already existing field, or create a new one. This adapter supports **User Custom Parsing**. See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.