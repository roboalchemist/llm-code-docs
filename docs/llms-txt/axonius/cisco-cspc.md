# Source: https://docs.axonius.com/docs/cisco-cspc.md

# Cisco Common Service Platform Collector (CSPC)

The Cisco Common Service Platform Collector (CSPC) is an SNMP-based tool that discovers and collects information from the Cisco devices installed on companies' networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cisco Common Service Platform Collector (CSPC) server that Axonius can communicate with via the [Required Ports](#required-ports). When entering the host name or IP address, please include the port number. Example: `http://somedomain.com:8001/` or `http://192.198.1.1:8001/`

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets. For information on configuration, see the [User Guide for CSPC Collection Platform Software](https://www.cisco.com/c/dam/en/us/support/docs/cloud-systems-management/common-services-platform-collector-cspc/CSPC-User-Guide.pdf).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Cisco CSPC" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco%20CSPC.png" />

## Required Ports

The default port is 8001. Your system may be configured to use a different port. If so, use the port that your system uses.

## Supported From Version

Supported from Axonius version 6.1