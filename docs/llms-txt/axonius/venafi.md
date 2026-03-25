# Source: https://docs.axonius.com/docs/venafi.md

# Venafi

Venafi secures and protects cryptographic keys and digital certificates.

### Asset Types Fetched

* Devices, Certificates, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password
* Application ID

### Permissions

The value supplied in [User Name](#required-parameters) must have the following permissions and scopes to fetch assets:

* Permissions - Read permission and Private Key Read/View permission to the Certificate Object and Client Entry.
* Token scope - Certificate, Agent, Certificate Manage.
* configuration:manage scope - required to use the Fetch Identities as Users advanced setting.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Server Host Name or IP Address** - The hostname or IP address of the Venafi server.
2. **Authentication Host Name or IP Address** - The hostname or IP address of the Venafi authentication server.
   * If supplied, the hostname supplied in **Authentication Host Name or IP Address** will be used.
   * If not supplied, the hostname supplied in **Server Host Name or IP Address** will be used.
3. **User Name** and **Password** - The credentials for a user account that has access to the **Authentication Host Name or IP Address**. This server will be used to authenticate and receive a token, which will be used for API calls to **Server Host Name or IP Address**.
4. **Application ID** - The Application ID is generated from the application key when creating the integration. It identifies an integration, application, or client that uses the web SDK.

<Image alt="Venafi" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Venafi.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **Enable Client Side Certificate** - Select to enable Axonius to send requests using the certificates uploaded to allow Mutual TLS configuration for this adapter.
   * Click **Upload File** next to **Client Private Key File (.pem)** to upload a client private key file in PEM format.
   * Click **Upload File** next to **Client Certificate File (.pem)** to upload a public key file in PEM format.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async chunks in parallel** *(default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Venafi server in parallel at any given point.
2. **Skip disabled certificates** - Select this option to skip disabled certificates.
3. **Skip revoked certificates** - Select this option to skip revoked certificates.
4. **Fetch Agents** - Select this option to fetch agents.
5. **Parse Manufacturer Serial** *(default: true)* - By default this adapter enables parsing of the manufacturer serial. Clear this option to not parse the manufacturer serial.
6. **Filter Certificates by Self-signed Status** - Select this option to filter self-signed certificates.
7. **Show Certificates also as "Devices" (in addition to "Certificates")** *(default: true)* - By default this adapter parses devices that have CertificateDetails as Devices, in addition to Certificates. Clear this option to parse those devices only under Certificates.
8. **Fetch Identities as Users** - Select this option to fetch identities as users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 19.2    | Yes       |       |