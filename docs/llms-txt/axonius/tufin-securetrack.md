# Source: https://docs.axonius.com/docs/tufin-securetrack.md

# Tufin SecureTrack

Tufin SecureTrack is a firewall management solution that delivers security, compliance, and connectivity across physical networks and hybrid cloud.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Networks
* Network/Firewall Rules

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Tufin SecureTrack server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Tufin SecureTrack.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Tufin%20SecureTrack.png" />

## APIs

Axonius uses the [Tufin SecureTrack REST API](https://forum.tufin.com/support/kc/rest-api/R20-2/securetrack/apidoc/).
It uses the [Devices API](https://forum.tufin.com/support/kc/rest-api/R20-2/securetrack/apidoc/#!/Monitored_Devices/getDevices).

## Supported From Version

Supported from Axonius version 4.5