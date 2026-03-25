# Source: https://docs.axonius.com/docs/apple-business-manager-ade.md

# Apple Business Manager 

 

Apples Business Manager is a web-based portal that provides device management, app distribution, and user access control for organizations integrating with Mobile Device Management (MDM) solutions.

### Use Cases the Adapter Solves

The adapter identifies all Apple devices owned by the organization, including those that are purchased but not yet enrolled in a Mobile Device Management (MDM) solution to help security teams find devices that have been purchased but haven't checked in or been assigned to a security policy yet. It helps to confirm that devices are correctly linked to the organization’s ABM account and assigned to the intended MDM server.

The adapter fetches information that includes the device's serial number, model, and the Mobile Device Management (MDM) server it is assigned to.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

OAuth 2.0 (Client Credentials Grant) using a Client Assertion (JWT).

### APIs

Axonius uses the [Apple Business Manager API v1](https://developer.apple.com/documentation/applebusinessmanagerapi)

[Get Organization Devices](https://developer.apple.com/documentation/applebusinessmanagerapi/get-org-devices)

### Permissions

The following permissions are required:

* OAuth scope: `business.api` - This scope grants access to the ABM API endpoints.

#### Supported From Version

Supported from Axonius version 8.0.9

## Configuring the Apple Business Manager to Work With Axonius

You need to generate a private key. Follow the instructions under **Generate a Private Key** in [Create an API account in Apple Business Manager](https://support.apple.com/en-ca/guide/apple-business-manager/axm33189f66a/web).

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **Apple Business Manager**, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **API Domain** *(default `https://api-business.apple.com`)* - The base URL for calling the Apple Business Manager API endpoints.

2. **Authentication Domain** *(default `https://account.apple.com/`)* -  The URL of the Apple OAuth 2.0 authorization server.

3. **Private Key File**  Upload the private key file in PEM format used to sign the JWT for OAuth 2.0 authentication. This key is used to sign JWTs as part of the OAuth Client Assertion process. The private key must correspond to the Key ID and Team ID issued in Apple Business Manager when registering the API integration.

4. **Client ID** - The Client ID from your Apple Business Manager API account. This is the identifier for your OAuth 2.0 client, issued when registering your Apple Business Manager API account.

5. **Key ID** - The identifier for the private key registered in your Apple Developer account. You receive this value when you create and download a private key for API authentication.

6. **Connection Label** - A name for the connection that will help you identify it.

<br />

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ApplesBusinessManagerNew.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.
   <br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

<br />

<br />