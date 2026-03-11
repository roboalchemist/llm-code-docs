# Source: https://docs.axonius.com/docs/alcide.md

# Alcide

Alcide provides cloud and Kubernetes discovery, K8s audit and compliance scanner, microservices anomaly detection and security policies management and enforcement.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Alcide Domain** *(required)* - The hostname or IP address of the Alcide server. The recommended value is 'devel.cloud.alcide.io'.

2. **Organization UID** *(required)* - Specify an internal Alcide Organization UID, will be supplied by Alcide.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![alcide.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/alcide.png)