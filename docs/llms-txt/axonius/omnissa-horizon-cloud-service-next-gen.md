# Source: https://docs.axonius.com/docs/omnissa-horizon-cloud-service-next-gen.md

# Omnissa Horizon Cloud Service Next Gen

Omnissa Horizon Cloud Service Next Gen is a cloud management solution that provides advanced infrastructure optimization and security features.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Refresh Token

### APIs

Axonius uses the [Omnissa Horizon Cloud Service Next Gen API](https://developer.omnissa.com/horizon-apis/horizon-cloud-nextgen/).

### Permissions

The user must have read permissions for the requested organization (`org_id`).

#### Supported From Version

Supported from Axonius version 7.0.12

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: [https://cloud-sg.horizon.omnissa.com](https://cloud-sg.horizon.omnissa.com))* -The hostname or IP address of the Omnissa Horizon Cloud Service Next Gen server.
2. **Refresh Token** - The token used for the connection.
3. **CSP URL (domain for tokens)** *(default: [https://connect.omnissa.com](https://connect.omnissa.com) )* - Enter the Cloud Services Portal (CSP) URL.

<Image alt="Omnissa Horizon Cloud Server Next Gen Add Connection Screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/OmnissaHorizonCloudServiceNextGen.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).