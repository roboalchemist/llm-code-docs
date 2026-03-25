# Source: https://docs.axonius.com/docs/infosec-iq-phishing-simulator.md

# Infosec IQ Phishing Simulator Platform

Infosec IQ is a security awareness platform that offers training and phishing simulations.

### Asset Types Fetched

* Users, Tickets

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the [Infosec IQ Public API](https://developers.infosecinstitute.com/apidocs/v2/).

### Permissions

The following permissions are required:

* The account manager must enable “API functionality” before accessing the API.

* The user must be “Administrator”.

#### Supported From Version

Supported from Axonius version 7.0.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Infosec IQ server.
2. **API Version** *(default: v2)* - Select the API Version you want to use to connect.
3. **API Token** - An API Token associated with a user account that has the Required Permissions to fetch assets.

![Infosec IQ Phishing Simulator Platform.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Infosec%20IQ%20Phishing%20Simulator%20Platform.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).