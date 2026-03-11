# Source: https://docs.axonius.com/docs/sitescope.md

# Micro Focus SiteScope

Micro Focus SiteScope (previously HPE SiteScope) provides monitoring capabilities for IT infrastructure, including servers, databases, network, media, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Micro Focus SiteScope server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![MicroFocusSiteScope.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MicroFocusSiteScope.png)

## APIs

Axonius uses the [HPE SiteScope API](https://softwaresupport.softwaregrp.com/doc/KM02681284?fileName=hpe_man_11.33_SiteScope_API_Reference.pdf).

## Required Permissions

To enable the API set "Preferences `>` Infrastructure Preferences `>` Custom Settings `>` Access controlled” to true. Refer to [SiteSCope ITOM Practitioner Portal](https://docs.microfocus.com/itom/SiteScope:2019.11/NotesLimitationsAPIs) for full details.
The value supplied in [User Name](#parameters) must have the following  permissions

* Data API - View permissions for the monitors they need to get.
* Monitor status API - Administration access