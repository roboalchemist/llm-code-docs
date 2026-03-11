# Source: https://docs.axonius.com/docs/attack-forge.md

# AttackForge

AttackForge is a collaborative platform for managing penetration testing projects, centralizing vulnerability data and reporting.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Business Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the AttackForge server.

2. **API Key** *(required)* - See [the AttackForge documentation](https://support.attackforge.com/attackforge-enterprise/modules/self-service-restful-api/getting-started) for instructions on how to generate an API key.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![AttackForge connection parameters.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AttackForge%20connection%20parameters.png)

## APIs

Axonius uses the [ AttackForge API](https://support.attackforge.com/attackforge-enterprise/modules/self-service-restful-api/getting-started).

## Supported From Version

Supported from Axonius version 6.1.30