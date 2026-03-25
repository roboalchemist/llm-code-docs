# Source: https://docs.axonius.com/docs/fortinet-fortigate.md

# Fortinet FortiGate

Fortinet FortiGate is a next-generation firewall providing security and visibility for end-to-end protection across the entire enterprise network.

<Callout icon="📘" theme="info">
  Note:

  For FortiManager use the  [FortiManager ](https://docs.axonius.com/docs/forti-manager)adapter.
</Callout>

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Users, Groups, Network/Firewall Rules, Alerts/Incidents

## Before You Begin

### Required Permissions

The value supplied for User Name, if used when connecting the adapter, must have read access to devices.

In addition, you need to create an Administrator profile and a FortiManager API locally defined API admin user, and assign the required permissions in the process.

### Creating an Administrator Profile

1. On the FortiManager GUI, select **System Settings** `>` **Admin Profiles** `>` **Create New**.

2. Populate the fields as shown in the image below.

3. Select the permissions of your choice.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Fortinet%20FortiGate%20Create%20New%20Admin%20Profiles.png)

4. Click **OK**.

### Creating the JSON API Admin

After you create your administrator profile, use the steps below to create a FortiManager API locally defined API admin user.

<Callout icon="📘" theme="info">
  **Notes**

  The JSON API admin should have the minimum permissions required to complete the request.

  The API admin can be locally defined or defined on some external LDAP, RADIUS, TACACS servers.
</Callout>

1. On the FortiManager GUI, select **System Settings** `>` **Administrators** `>` **Create New**.

2. Populate the fields as shown in the image below. Make sure you assign **select:read** (rpc-permit), **ALL ADOMs**, and **ALL Packages** (Policy Package Access).
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Fortinet%20FortiGate%20Creat%20New%20JSON%20API%20Admin.png)

3. Click **OK**.

### Generating the FortiOS API Key (Optional)

If you authenticate with a FortiOS API Key, you need to create a profile that only has read access to the firewall address permission group.

1. In the FortiGate GUI, select **System** `>` **Admin Profiles** `>` **Create New**.
2. Select at least read permissions for:
   1. User/Device
   2. Firewall
   3. Policy
   4. Address
   5. Schedule
   6. Network
   7. System
   8. VPN
   9. WiFi and Switch
3. Click **OK**.
4. Back in the FortiGate GUI, select **System** `>` **Administrators** `>` **Create New** `>` **REST API Admin**.
5. Populate the fields as shown below:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Fortinet%20FortiGate%20Create%20REST%20API%20Admin.png)

   In 6.4.2 and earlier, the **Trusted Host** must be specified to ensure that your local host can reach the FortiGate. For example, to restrict requests as coming from only 10.20.100.99, enter 10.20.100.99/32.
6. Click **OK** and an API token will be generated. **The API token as it is only shown once and cannot be retrieved. It will be needed for the rest of the process.**
7. Click **Close**.

## Deploying the Adapter in Axonius

1. **Host Name** - The hostname or IP address of the Fortinet FortiGate server.
2. **Port** - If not supplied, Axonius will use TCP port 443.
3. **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
4. **FortiOS API Key** *(optional)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  For FortiOS connections only:

  * **User Name** and **Password** are required when **FortiOS API Key** is not supplied.
  * When **FortiOS API Key** is supplied, **User Name** and **Password** are not required, and authentication should be attempted using the Bearer Token.
</Callout>

![FortiNet FortiGate adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/FortiNetFortiGate.png)

<br />

### Optional Parameters

1. **Virtual Domain** - Specify a comma-separated list of Virtual Domains (VDOMs) so that .Axonius will fetch data from specified virtual domains.
2. **Is Hosted on Cloud** - Select this option when Fortinet FortiGate is hosted on Cloud.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **DHCP lease time (seconds)** *(required, default: 604800)* - Specify the DHCP lease time, that refers to the life of an IP address remains assigned to a device.
2. **Interfaces exclude list** *(optional)* - Specify a comma-separated list of [Fortinet FortiGate interfaces](https://help.fortinet.com/fos50hlp/52data/Content/FortiOS/fortigate-system-administration-52/Interfaces/interfaces.htm) so that the adapter will only fetch devices that are not associated with the specified interfaces.
3. **VMware Interfaces exclude list** *(optional)* - Specify a comma-separated list of [Fortinet FortiGate interfaces](https://help.fortinet.com/fos50hlp/52data/Content/FortiOS/fortigate-system-administration-52/Interfaces/interfaces.htm) so that the adapter will only fetch virtual devices that are not associated with the specified interfaces.
4. **Do not fetch OS Type field** *(optional)* - Select to exclude fetching data from the OS Type field.
5. **Allow IPSEC VPN devices** - Select to allow fetching IPSEC VPN devices.
6. **Use Fortigate new OS version parser** - Select this option to fetch the OS minor version from another field on a FortiOS device instance.
7. **Fetch firewall rules** - Select this option to fetch all the firewall rules, as well as their policies and addresses.
8. **Maximum number of chunks** *(default:50)* - Enter a number to set the maximum number of parallel chunks to fetch information from the ADOMs. This can be a value between 50 and 100. Select  the number of parallel calls that works best with your system.
9. **Fetch VPN SSL Sessions as Devices** - Select this option to fetch VPN SSL sessions as Devices.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 4.5