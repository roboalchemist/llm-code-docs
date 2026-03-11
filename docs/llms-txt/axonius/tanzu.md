# Source: https://docs.axonius.com/docs/tanzu.md

# VMWare Tanzu

The VMware Tanzu for Kubernetes Operations bundle allows platform operators to build, manage, and monitor Kubernetes environments across multiple platforms.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the VMWare Tanzu server.

2. **API Token** *(required)* - An API Key associated with a user account that has the  Permissions to fetch assets.

3. **Cluster ID** *(required)* - The Cluster ID

4. **Namespace** *(required)* - The namespace

5. **Podname** *(required)* - The podname

**Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![VMWareTAnzu](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/VMWareTAnzu.png)

## Supported From Version

Supported from Axonius version 4.7