# Source: https://docs.axonius.com/docs/sysdig.md

# Sysdig - Monitor

Sysdig is a monitoring, troubleshooting, cost-optimization, and alerting suite for containers, cloud, and Kubernetes environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://app.sysdigcloud.com`)* - The hostname or IP address of the Sysdig server.

2. **Token** *(required)* - An API token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Client Type** - Select the type of client (Monitor or Secure).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Sysdig](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sysdig.png)

## APIs

Axonius uses [Sysdig Monitor](https://docs.sysdig.com/en/docs/sysdig-monitor/using-monitor/).

## Supported From Version

Supported from Axonius version 6.0