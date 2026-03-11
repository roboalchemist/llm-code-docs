# Source: https://docs.axonius.com/docs/kolide-k2.md

# Kolide K2

Kolide K2 is a paid cloud-hosted SaaS platform for gathering detailed device information and securing endpoints.

## Asset Types Fetched

* Devices, Users

## APIs

Axonius uses the [Kolide K2 API](https://api.kolide.com/).

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Kolide K2 server. The default hostname is `https://api.kolide.com`.

2. **Token** - The Kolide K2 API uses token-based authentication to fetch assets. Refer to the [Kolide K2 API](https://api.kolide.com/) to obtain one.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/KolideConnection.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Devices using query** - Toggle on to enrich Kolide devices using a custom report that will be fetched from the `reporting/queries/{query_id}` endpoint.
  * **Enrich devices using query ID** - Specify the value of the Kolide query ID.
  * **Enrich devices query identifier fields** - Enter the common field for both the Kolide devices and Kolide query results. For example, the devices and query results both have the `serial` field, so the adapter will connect them based on the `serial` field. If the identifier fields have different names (i.e., `serial` for the devices and `serial_number` for the query results), the client can enter `serial,serial_number` and the adapter will make the connection.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>