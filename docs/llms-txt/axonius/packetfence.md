# Source: https://docs.axonius.com/docs/packetfence.md

# PacketFence

PacketFence is a free open source network access control (NAC) solution which provides the following features: registration, detection of abnormal network activities, proactive vulnerability scans, isolation of problematic devices, remediation through a captive portal, 802.1X, wireless integration and User-Agent / DHCP fingerprinting.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **PacketFence Domain** – The hostname of the PacketFence server.
2. **User Name** and **Password** – The username and password for the user used in the connection.
3. **Verify SSL** – Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* – Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![packetfence.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/packetfence.png)