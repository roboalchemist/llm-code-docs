# Source: https://docs.axonius.com/docs/hp-network-node-manager-i-nnmi.md

# HP Network Node Manager i (NNMi)

HP Network Node Manager i (NNMi) is a network health and performance monitoring software with scalability and device support.

The HP Network Node Manager i adapter connection requires the following parameters:

1. **HP NNMi Domain** – The hostname of the HP NNMi server.

2. **User Name** and **Password** – The user name and password for an account used in the connection.

3. **API Rate Limit (Requests per Minute)** - Enter a value to set the number of requests the adapter will send to the API per minute.

4. **Verify SSL** – Select whether to verify the SSL certificate of the server.

5. **HTTPS Proxy** (optional) – Connect the adapter to a proxy instead of directly connecting it to the domain.

![HPNNMI](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPNNMI.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich devices with IP Addresses** - Select this option to enrich devices with IP Addresses. To enable this option IPAddress permissions for the WSDL services are required
2. **Enrich devices with interfaces** -  Select this option to enrich devices with interfaces. To enable this option Interface permissions for the WSDL services are required
3. **Enrich devices with node groups** - Select this option to enrich devices with node groups. To enable this option NodeGroup permissions for the WSDL services are required
4. **Enrich devices with security groups** - Select this option to enrich devices with security groups. To enable this option Security permissions for the WSDL services are required

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>