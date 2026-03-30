# Source: https://docs.axonius.com/docs/endgame.md

# Endgame

Endgame is an endpoint protection platform that combines on-line and off-line protection against exploits, phishing, malware, ransomware, and fileless attacks.

## Adapter Parameters

1. **Endgame Domain** *(required)* - The hostname or IP Address of the Endgame management server.
2. **User Name** and **Password** *(required)* - The user name and password for an account that has site viewer access to the management server.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the host supplied in **Endgame Domain**. For more details, see [SSL Trust & CA Settings](../global-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the host will be verified against the CA database inside of Axonius. If it fails validation, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the host will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to **Endgame Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the host defined for this connection.
   * If not supplied, Axonius will connect directly to the host defined for this connection.

![endgame.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/endgame.png)

## Configuring Endgame Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

To configure the Endgame adapter advanced settings, open the **Endgame adapter** page, click **Advanced Settings**, and then click the **Endgame Configuration** tab:

* **Endgame status exclude list** *(Optional, default: empty)* - Specify a comma-separated list of Endgame statuses.
  * If supplied, all connections for this adapter will not fetch devices whose Endgame status is any of the comma-separated list of Endgame statuses that have been defined in this field.
  * If not supplied, all connections for this adapter will fetch devices with any Endgame status.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(316\).png)