# Source: https://docs.axonius.com/docs/verkada.md

# Verkada

Verkada is a cloud-based security platform offering video surveillance, access control, and environmental sensors.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

API Key

### APIs

Axonius uses the [Verkada API](https://apidocs.verkada.com/reference/introduction).

API Endpoints Used to Fetch Data:

* `GET /cameras/v1/devices` - for cameras
* `GET /cameras/v1/alerts` - Camera Alerts
* `GET /access/v1/doors` - Doors (Access Control)
* `GET /sensors/v1/devices` - Sensors (Environmental Sensors)
* `GET /sensors/v1/alerts` - Sensor Alerts
* `GET /access/v1/access_users` - Access Users

### Permissions

The following permissions are required:

The API Key must have the following permissions configured in Verkada Command:

**Camera Permissions**

* Read access to Camera devices  - Required for `/cameras/v1/devices` endpoint
* Read access to Camera alerts  - Required for `/cameras/v1/alerts` endpoint

**Access Control Permissions**

* Read access to Doors  - Required for `/access/v1/doors` endpoint
* Read access to Access Users  - Required for `/access/v1/access_users` endpoint

**Sensor Permissions**

* Read access to Sensor devices  - Required for `/sensors/v1/devices` endpoint
* Read access to Sensor alerts  - Required for `/sensors/v1/alerts` endpoint

**Note:** The exact permission names and role requirements should be confirmed with your Verkada administrator or in the Verkada Command platform.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Verkada, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Verkada server.
2. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.
3. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="Verkada connection screen" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BackBox.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />