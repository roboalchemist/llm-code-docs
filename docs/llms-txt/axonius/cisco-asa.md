# Source: https://docs.axonius.com/docs/cisco-asa.md

# Cisco Adaptive Security Appliance (ASA)

Cisco Adaptive Security Appliance (ASA) Software is the core operating system for the Cisco ASA Family, delivering firewall capabilities for ASA devices in an array of form factors.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Network/Firewall Rules

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cisco Adaptive Security Appliance (ASA) server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

<Callout icon="📘" theme="info">
  Note

  The configuration of SSL parameters for Management connections might impact some of the VPNs configured on Firewall devices, as some elements of the SSL firewall configuration are shared between VPN and Management interfaces.
</Callout>

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Cisco ASA" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco%20ASA.png" />

## APIs

Axonius uses the [Cisco ASA REST API](https://www.cisco.com/c/en/us/td/docs/security/asa/api/asa_rest_api.html#_Toc439951882).

## Required Permissions

Privilege 5 or greater is required in order to invoke GET APIs.

## Troubleshooting

Some old ASA devices and software may not be supported, as the Axonius adapter client’s TLS/SSL is not compatible with them. A possible error message that might return in this case is as follows:

```
Connection test failed for all Entity types: Test Connection failed for entity EntityType.Devices Error details: Failed to run on main endpoint tree Failed to run endpoints because Unable to do request: HTTPSConnectionPool ….. Caused by SSLError(SSLError(1, '[SSL: UNSAFELEGACYRENEGOTIATIONDISABLED] unsafe legacy renegotiation disabled (ssl.c:997)
```

## Supported From Version

Supported from Axonius version 6.1