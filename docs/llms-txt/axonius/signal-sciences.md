# Source: https://docs.axonius.com/docs/signal-sciences.md

# Signal Sciences

Signal Sciences is a web protection platform that protects on-premise, multi-cloud and hybrid-cloud apps, within containers and serverless functions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Signal Sciences Domain** *(required)* - The hostname or IP address of the Signal Sciences server.
2. **Email** *(required)* - The email of a user account that has the permissions to fetch assets. For more details on creating an API user, see [Signal Sciences Developer Guide - Using Our API](https://docs.signalsciences.net/developer/using-our-api/).
3. **Password** or **API Token** *(optional)* - The password or the API access token associated with a user account that has the permissions to fetch assets. For more details on creating an API access token, see [Signal Sciences Developer Guide - Managing API Access Tokens](https://docs.signalsciences.net/developer/using-our-api/).

<Callout icon="📘" theme="info">
  Note

  It is recommended to use API token.
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Signal Sciences.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Signal%20Sciences.png)