# Source: https://docs.axonius.com/docs/vmware-vrops.md

# VMware vRealize Operations (vROps)

VMware vRealize Operations (vROps) delivers an IT operations management platform for private, hybrid, and multi-cloud environments that covers physical, virtual, and cloud infrastructure, including VMs and containers.

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices

## Before You Begin

### APIs

Axonius uses the [VMware vRealize Ops API](https://vdc-download.vmware.com/vmwb-repository/dcr-public/1e2150d8-8682-4213-a6f0-03fb3b1dc410/b10f698a-21c4-4194-84a5-d3aca9002a07/index.html).

### Permissions

Global reader permissions on the vcenters is required in order to fetch assets.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Hosting Environment** - Select the hosting environment, either **On-Premise** or **Cloud Hosted**. The authentication configuration depends on the option you choose.

<Tabs>
  <Tab title="On-Premise">
    **User Name** and **Password**   - The credentials for a user account that has the required permissions to fetch assets. The user name should be in a 'user\@domain' format.
  </Tab>

  <Tab title="Cloud Hosted">
    **API Token**  - An API refresh token. Refer to [How do I generate API tokens ](https://docs.vmware.com/en/VMware-Cloud-services/services/Using-VMware-Cloud-Services/GUID-E2A3B1C1-E9AD-4B00-A6B6-88D31FCDDF7C.html) for details.
  </Tab>
</Tabs>

1. **Host Name or IP Address**   - The hostname or IP address of the VMware vRealize Operations (vROps) server.

<Image align="center" alt="vRops" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/vRops.png" className="border" />

<br />

### Optional Parameters

1. **Auth Source** *(optional, default: empty)* - Specify the name of the authentication parameter that is sent to the API.

Auth Source examples values:

* LDAP
* ACTIVE\_DIRECTORY
* LOCAL\_USER
* VC
* VIDM

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Ignore "NOT\_EXISTING" devices** *(required, default: true)*  - Enable this setting to not fetch devices in "NOT\_EXISTING" state, otherwise the adapter fetches devices in any state.
2. **Fetch Alerts** - Select to fetch Alerts.
3. **Enrich Alerts With Symptoms** - Select to enrich Alerts with Symptoms information.
4. **Use UUID as manufacturer serial number** - Select this option to use the UUID instead of the manufacturer serial number.
5. **Override hostname** - Select this option to override the device name with the contents of the `summary|guest|hostName` or `config|name` fields, if they exist. If `summary|guest|hostName` exists it is used, otherwise `config|name` is used. If neither has a value, then the hostname is not overridden and the value in this field, is the same as that of the device.
6. **Force device serial to specific field** *(optional, default: off)* - Allows you to specify the type of serial number to fetch. When enabled, select the type of serial number from the **Field for device serial** dropdown.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>