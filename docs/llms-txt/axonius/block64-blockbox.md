# Source: https://docs.axonius.com/docs/block64-blockbox.md

# Block64 BlockBox

Block64 is an agentless, appliance-based asset management solution collecting data about assets across the network and using that to provide actionable insights.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Block64 BlockBox  server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  Both **User Name** and **Password**, and  **API Key** are required fields.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Block64 BlockBox](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Block64%20BlockBox.png)

## APIs

Axonius uses the BlockBox API.

## Supported From Version

Supported from Axonius version 4.5