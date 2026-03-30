# Source: https://docs.axonius.com/docs/universal-cmdb.md

# Micro Focus Universal CMDB

Micro Focus Universal Discovery and Universal CMDB discovers, maps, and manages IT configurations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Micro Focus Universal CMDB server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **TQL Query Names** - Enter a list of Query Names to be fetched. You have to enter at least one query name.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![MicroFocusCMDBNEw](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MicroFocusCMDBNEw.png)

## APIs

Axonius uses the [Universal CMDB REST API](https://docs.microfocus.com/UCMDB/11.0/ucmdb-docs/docs/eng/doc_lib/Content/REST_API/REST_API_Chapter.htm)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8