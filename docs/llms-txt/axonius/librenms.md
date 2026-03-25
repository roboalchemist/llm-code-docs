# Source: https://docs.axonius.com/docs/librenms.md

# LibreNMS

LibreNMS is a network monitoring solution that provides auto-discovery for network hardware and operating systems including Cisco, Linux, Juniper, Foundry, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **LibreNMS Domain** *(required)* - Keep as *'[https://librenms.org](https://librenms.org)'*.
2. **API Key** *(required)* - Use the authentication token you have generated for a user that has site viewer access to LibreNMS. For more details, see [Using the API - LibreNMS Docs](https://docs.librenms.org/API/).
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![librenms.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/librenms.png)