# Source: https://docs.axonius.com/docs/veritas-netbackup.md

# Veritas NetBackup

Veritas NetBackup is an enterprise backup solution offering data management, automation, artificial intelligence, and elastic architecture.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Veritas NetBackup server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Domain Type** *(optional, default: vx)* - The domain of the service used for authentication.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Veritas%20NetBackup](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Veritas%20NetBackup.png)

## APIs

Axonius uses the NetBackup API.

1. For authentication Axonius uses [NetBackup API - 8.1.2 Authentication](https://sort.veritas.com/public/documents/nbu/8.1.2/windowsandunix/productguides/html/index/#getting-started:~:text=Overview-,Authentication,-NetBackup%20authenticates%20the).
2. To fetch users Axonius uses the [NetBackup API - 8.1.2 GET /config/hosts](https://sort.veritas.com/public/documents/nbu/8.1.2/windowsandunix/productguides/html/index/#_config-config_hosts_get).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [User Name](#parameters) must have a Security administrator role, which should include the permissions to “View Assets“.

## Supported From Version

Supported from Axonius version 6.1