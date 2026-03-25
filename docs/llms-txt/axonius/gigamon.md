# Source: https://docs.axonius.com/docs/gigamon.md

# Gigamon GigaVUE-FM (Fabric Manager)

Gigamon GigaVUE-FM (Fabric Manager) delivers management and monitoring of all physical and virtual nodes across your on-premises, virtual and public-cloud deployments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the GigaVUE-FM server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a Read-Only user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Gigamon GigaVUE-FM.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Gigamon%20GigaVUE-FM.png)

## APIs

Axonius uses the [GigaVUE-FM REST API](https://www.gigamon.com/content/dam/resource-library/english/guide---cookbook/gu-gigavue-fm-rest-api-user-guide.pdf).

## Required Ports

* **HTTPS port 443**