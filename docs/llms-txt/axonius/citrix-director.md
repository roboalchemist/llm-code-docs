# Source: https://docs.axonius.com/docs/citrix-director.md

# Citrix Director

Citrix Director is a web-based monitoring console for Citrix XenApp and XenDesktop virtualization platforms that allows administrators to control and monitor virtual applications and desktops.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Citrix Director server.

<Callout icon="📘" theme="info">
  Note

  * If the Citrix Director server returns a 404 error, make sure that you enter the hostname or IP of the **Citrix Delivery Controller server**.

  * By default, the Citrix Delivery Controller listens on port 80.  You can test the connection by navigating to http\://**delivery-controller**/Citrix/Monitor/OData/v4/Data/Machines (where **delivery-controller** is your delivery-controller URL).

  * If the URL responds on port 80, you'll need to specify **http\://** in the **Host Name or IP Address** parameter.
</Callout>

2. **API Version** *(required, default: v4)* - Select the API version to fetch data.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Citrix Director.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Citrix%20Director.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Connections** - Select this option to fetch data from all of the device’s connections.
2. **Fetch Catalogs** - Select this option to fetch the catalog name.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Citrix Monitor Service API](https://developer-docs.citrix.com/projects/monitor-service-odata-api/en/latest/).

## Version Matrix

| Version               | Supported | Notes |
| --------------------- | --------- | ----- |
| Citrix Monitor API V4 | Yes       |       |

This adapter has only been tested with the versions marked as supported, but may work with lower versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, and it is not functioning as expected.