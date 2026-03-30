# Source: https://docs.axonius.com/docs/openvas.md

# Greenbone Vulnerability Management (OpenVAS)

Greenbone Vulnerability Management (OpenVAS) is a software framework including several services and tools for vulnerability scanning and vulnerability management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **OpenVAS host** *(required)* - The hostname or IP address of the Greenbone Vulnerability Management (OpenVAS) server, for example: `https://openvas.my.corp`.
2. **OpenVAS user name** and **OpenVAS password** *(required)* - The user name and password for an account to connect to Greenbone Vulnerability Management (OpenVAS).
3. **Port** - *(optional, default: 443)* - The port used in the connection.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="openVas.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/openVas.png" />

## Required Permissions

The adapter connects to the GSA (Greenbone Security Assistant) web UI to perform operations.  Modify the GSAD configuration on the OpenVAS / Greenbone host to connect to the GSA web UI from the Axonius host.

The value supplied in [OpenVAS user name](#parameters) must have the following permissions to fetch assets:

* authenticate
* get\_assets
* get\_results, commands