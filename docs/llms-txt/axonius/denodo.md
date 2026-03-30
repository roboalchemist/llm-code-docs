# Source: https://docs.axonius.com/docs/denodo.md

# Denodo

Denodo is a data virtualization platform that offers real-time data integration and management.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* OAuth Token for on-prem

### APIs

Axonius uses the [Denodo Platform RESTful Web Service](https://community.denodo.com/docs/html/browse/9.2/en/vdp/administration/restful_architecture/restful_web_service/restful_web_service).

### Permissions

* The user (associated with Basic Auth or OAuth token) must have `EXECUTE` privileges on the view.

  * If the view joins other views, the user may also need `ACCESS` or `METADATA` privileges on those underlying views.

* The view must be published to the REST interface.

  * Views must be explicitly made available through the web container (e.g., `denodo-restfulws`).
  * If the view is not published, no REST access is possible, even if the user has permissions in VDP.

* Minimum recommended permissions for API access:

  * `EXECUTE` on the target view
  * `CONNECT` on the database
  * `ACCESS` and `METADATA` on dependent views (if applicable)

#### Supported From Version

Supported from Axonius version 7.0.10

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Device Inventory View URL** - The full URL of the view from which you should pull devices.
2. **User Inventory View URL** - The full URL of the view from which you should pull users.

<Callout icon="📘" theme="info">
  Notes

  * You must configure at least on of the inventory view URLs in order for the adapter to work.

  * The general format is as follows: `https://<denodo_host>:/<web_container>/<vdp_database>/views/<device_user_inventory_view>`
</Callout>

3. **Auth Method** - Select an Authentication method, either **User Name and Password** (default) or **OAuth Token**. For more information on authentication, see the [Denodo Platform Data Catalog Guide REST API](https://community.denodo.com/docs/html/browse/9.2/en/vdp/data_catalog/appendix/rest_api/rest_api).

   * **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
   * **OAuth Token** - An OAuth Token associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Denodo.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Denodo.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](https://docs.axonius.com/docs/adding-a-new-adapter-connection).