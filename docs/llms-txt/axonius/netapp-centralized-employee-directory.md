# Source: https://docs.axonius.com/docs/netapp-centralized-employee-directory.md

# NetApp Centralized Employee Directory

NetApp Centralized Employee Directory (CED) enables retrieval of job and contact information on NetApp employees and contractors.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NetApp server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Client ID** and **Client Secret** *(required)* - The Client ID and Client Secret for a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NetApp Centralized Employee Directory](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetApp%20Centralized%20Employee%20Directory.png)

## APIs

Axonius uses the NetApp CED Employee Search API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.28.0