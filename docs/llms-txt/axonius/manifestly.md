# Source: https://docs.axonius.com/docs/manifestly.md

# Manifestly

Manifestly is a checklist, workflow, and SOP platform for managing recurring team tasks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Manifestly server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Department ID** *(optional)* - Specify a list of department IDs to fetch users from.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Manifestly](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Manifestly.png)

## APIs

Axonius uses the following API endpoints:

* [Manifestly API - Users Collection](https://manifestlyapi.docs.apiary.io/#reference/0/run-step/list-all-users)
* [Manifestly API V1 - Users](https://api.manifest.ly/api/v1/users/)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.30.0