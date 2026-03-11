# Source: https://docs.axonius.com/docs/hpe-greenlake-for-compute-ops-management.md

# HPE GreenLake for Compute Ops Management

HPE GreenLake for Compute Ops Management is a cloud-based management platform for automating and optimizing compute operations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the HPE GreenLake for Compute Ops Management server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. For information about how to obtain these credentials, see [Generating a token](https://developer.greenlake.hpe.com/docs/greenlake/services/audit-logs/public/guide/#generating-a-token).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HPE GreenLake for Compute Ops Management](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPE%20GreenLake%20for%20Compute%20Ops%20Management.png)

## APIs

Axonius uses the [HPE GreenLake for Compute Ops Management API](https://developer.greenlake.hpe.com/docs/greenlake/services/compute-ops-mgmt/public/openapi/compute-ops-mgmt-latest/overview/).

## Supported From Version

Supported from Axonius version 6.1