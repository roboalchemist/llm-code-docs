# Source: https://docs.axonius.com/docs/delinea-platform.md

# Delinea Platform 

Delinea Platform is a privileged access management solution that offers centralized identity security controls to define, authorize, and audit access to sensitive data and critical infrastructure resources.

### Use Cases the Adapter Solves

* Detect devices managed by the Delinea Platform, improving hardware inventory and compliance.
* Analyze privileged access activities for audit and security assurance.
* Verify that remote access engine assets have the required configuration and version properties.

## Types of Assets Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Activities.svg) Activities

## Before You Begin

**Ports**

* TCP port 443 (HTTPS, default and recommended)
* TCP port 80 (HTTP, if enabled and required)

**Authentication Method**

* OAuth 2.0 – Client Credentials flow. Authenticate by sending a POST request to `/identity/api/oauth2/token/xpmplatform` using your service user’s client ID and client secret, to retrieve a Bearer token.

### APIs

* [Delinea Platform API](https://docs.delinea.com/online-help/platform-api/start.htm)

### Permissions

The following permissions are required:

* delinea.platform/administration/remoteaccess/engine/read
* delinea.platform/audit/event/read

#### Supported From Version

Supported from Axonius version 8.0.13

### Setting Up Delinea Platform to Work with Axonius

Refer to [Delinea Documentation](https://docs.delinea.com/online-help/platform-api/start.htm) for detailed information about creating a service account and required roles.

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **Delinea Platform**, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Delinea Platform server.
2. **Client ID** - The Client ID for an OAuth 2.0 service user with the required permissions.
3. **Client Secret** - The Client Secret for the OAuth 2.0 service user.
4. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters) .

<br />

<Image align="center" alt="adapter schema screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/DelineaPlatform.png" />

### Optional Parameters

* **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** - Connect the adapter via an HTTPS proxy.
* **HTTPS Proxy User Name** - The user name for the HTTPS proxy.
* **HTTPS Proxy Password** - The password for the HTTPS proxy.

**Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />