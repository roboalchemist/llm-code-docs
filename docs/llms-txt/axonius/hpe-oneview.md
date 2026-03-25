# Source: https://docs.axonius.com/docs/hpe-oneview.md

# HPE OneView

HPE OneView is an integrated IT management solution that transforms compute, storage, and networking into software-defined infrastructure for task automation.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for HPE OneView, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the HPE OneView server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/HPEONeVIew.png)

<br />

### Optional Parameters

1. **Authentication Login Domain**  - Specify an optional directory used for authentication.
2. **API Version** *(default 1200)* - Enter an API Version.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
5. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## APIs

Axonius uses the [HPE OneView API](https://techlibrary.hpe.com/docs/enterprise/servers/oneview5.0/cicf-api/en/index.html#search?query=default%20directory).