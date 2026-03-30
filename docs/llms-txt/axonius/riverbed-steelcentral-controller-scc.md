# Source: https://docs.axonius.com/docs/riverbed-steelcentral-controller-scc.md

# Riverbed SteelCentral Controller (SCC)

Riverbed SteelCentral Controller (SCC) facilitates administration tasks for groups of SteelHeads, Interceptors, Mobile Controller, Cores, and Edges.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Riverbed Domain** *(required)* - The hostname or IP address of the Riverbed SteelCentral Controller (SCC) server.
2. **User Name** and **Password** *(optional* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If **API Key** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If **User Name** and **Password** are not supplied, **API Key** is required.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Riverbed SteelCentral Controller.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Riverbed%20SteelCentral%20Controller.png)