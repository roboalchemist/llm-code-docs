# Source: https://docs.axonius.com/docs/ubiquiti-networks-unifi-controller.md

# Ubiquiti Networks UniFi Controller

The UniFi Controller is a wireless network management software solution for managing multiple wireless networks using a web browser.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **UniFi Controller Domain** - The hostname of the UniFi Controller server.
2. **User Name** and **Password** - Specify the user name and password for a read-only user. A user with 'Read Only' role provides permission to access the data necessary to a given API resource. For more details, see the section below.

![Ubiquiti Networks UniFi Controller.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Ubiquiti%20Networks%20UniFi%20Controller.png)

### Optional Parameters

1. **Site** *(default: default)* - Specify the site name to fetch devices from.
   * If supplied, Axonius will fetch data from the specified site name.
   * If not supplied, Axonius will fetch data from site name 'default'.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **UniFi SSID include list** *(optional)* - Specify a comma-separated list of UniFi SSID.
   * If supplied, all connections for this adapter will only fetch devices whose SSID is any of the comma-separated list of UniFi SSID that have been defined in this field.
   * If not supplied, all connections for this adapter will fetch devices that are associated with any SSID.
2. **Special characters to remove from device name** *(optional)* - Enter a comma-separated list of special characters to remove from each device name that the adapter parses.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Configuring a Read-Only User in UniFi Controller Dashboard

To configure a read-only user for Axonius:

1. Open the **Unifi Controller** dashboard.
2. Go to **Settings** -> **Admins** -> click **Add New Admin**.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(860\).png)

3. For **Invite to Controller**, select **Manually set and store the password**.
4. Define a name and a password.
5. Select **Read Only** role.
6. Provide the user with the following **Global Permissions**:
   * Allow system stats access
   * Allow read only access to all sites
7. Click **Create**.