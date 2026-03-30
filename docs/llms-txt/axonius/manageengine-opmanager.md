# Source: https://docs.axonius.com/docs/manageengine-opmanager.md

# ManageEngine OpManager

ManageEngine OpManager enables monitoring of  routers, switches, firewalls, servers and VMs for fault and performance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ManageEngine OpManager server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   **To generate an API key**
   1. From the OPManager web client, go to **Settings** `>` **Basic Settings** `>` **REST API**.
   2. Click **Regenerate Key**.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ManageEngine_OpManager" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine_OpManager.png" />

## APIs

Axonius uses the [OpManager REST API](https://www.manageengine.com/network-monitoring/help/rest-api-opmanager.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Version Matrix

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6