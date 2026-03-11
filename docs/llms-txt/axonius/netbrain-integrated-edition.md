# Source: https://docs.axonius.com/docs/netbrain-integrated-edition.md

# NetBrain

NetBrain Integrated Edition is an adaptive automation integrated with existing NMS tools and IT workflows to automate documentation, troubleshooting, network change, and defense.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### Permissions

The value supplied in [**User Name and Password**](#required-parameters) must have read-only permissions in order to fetch assets.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **NetBrain Web API Server Host** - The hostname of the NetBrain server.
2. **NetBrain Domain Name** and **NetBrain Tenant Name** - The domain and tenant name associated with your NetBrain server.

<Callout icon="📘" theme="info">
  Note

  When **NetBrain Domain ID** and **NetBrain Tenant ID** are not supplied, **NetBrain Domain Name** and **NetBrain Tenant Name** are required.
</Callout>

3. **NetBrain Domain ID** and **NetBrain Tenant ID** - The domain and tenant identifier associated with your NetBrain server.

<Callout icon="📘" theme="info">
  Note

  When **NetBrain Domain Name** and **NetBrain Tenant Name** are not supplied, **NetBrain Domain ID** and **NetBrain Tenant ID** are required.
</Callout>

4. **User Name** and **Password**  - The user name and password for an account that has read access to the API.
5. **Use Backwards-Compatible (pre-8.01) API** *(default: true)* - Select this option when connecting to NetBrain versions earlier than v8.01 (this includes v8.0 and all v7.x).

<Image alt="NetBrain connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/NetBrain_AddConnection.png" />

<br />

### Optional Parameters

1. **External Authentication ID** - This parameter is only required for an external user through LDAP/AD or TACACS and the value must match with the name of external authentication which the user created with an admin role in system management under "User Account" section.
2. **Verify SSL** - Verify the SSL certificate offered by the host supplied in **NetBrain Web API Server Host**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - A proxy to use when connecting to **NetBrain Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch extended interface data** - Select this option to fetch physical interfaces, IPSec VPN interfaces, GRE VPN interfaces, and extended data for devices.
2. **Fetch One-IP table data** - Select this option to fetch One-IP table data for devices and all interfaces and extended data for devices (even if the **Fetch extended interface data** checkbox is disabled).
3. **Create One-IP entries as device** - Select this option to create One-IP entries as devices.
4. **Fetch latest found One-IP devices** - Select this option to fetch only the latest seen One-IP devices.
5. **Async One-IP requests in parallel** *(default: 5)* - Select this option to configure how many requests to send each time to OneIP.
   * If you configure this option, you must enable **Create One-IP entries as device**.
6. **Number of parallel processes**  *(default: 1)* - Select this option to configure the number of parallel processes to fetch devices from NetBrain.
7. **Comma separated list of DNS resolvers** - Add a comma-separated list of DNS resolvers. The system will then use them to get the DNS name of the device from the IP address.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>