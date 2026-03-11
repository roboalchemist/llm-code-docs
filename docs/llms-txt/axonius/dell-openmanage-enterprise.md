# Source: https://docs.axonius.com/docs/dell-openmanage-enterprise.md

# Dell OpenManage Enterprise

Dell OpenManage Enterprise is a one-to-many systems management console. It facilitates lifecycle management for Dell EMC PowerEdge servers in one console.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* API Key for on-prem

### APIs

Axonius uses the following APIs:

* <Anchor label="OpenManage Enterprise RESTful API Guide" target="_blank" href="https://www.dell.com/support/manuals/en-us/dell-openmanage-enterprise/ome_p_3.10_api_guide/Revision-history?guid=guid-7bfc2ef1-e606-447d-8ed2-e28aed414fa4&lang=en-us">OpenManage Enterprise RESTful API Guide</Anchor>.

* <Anchor label="OpenManage Enterprise - Documentation Website" target="_blank" href="https://www.dell.com/support/product-details/en-us/product/dell-openmanage-enterprise/resources/manuals">OpenManage Enterprise - Documentation Website</Anchor>.

### Permissions

The value supplied in [User Name](#required-parameters) must have the relevant permissions as defined in
[OpenManage Enterprise RESTful API Guide](https://www.dell.com/support/manuals/il/en/ilbsdt1/dell-openmanage-enterprise/ome-3.3.1_omem-1.10.00_apiguide/authorization?guid=guid-31777fc4-84d2-45f9-ab44-2fd6ea63258e\&lang=en-us).

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Dell OpenManage Enterprise server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
3. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Dell OpenManage Enterprise" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dell%20OpenManage%20Enterprise.png" />

### Optional Parameters

1. **Verify SSL**  - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **Server time Offset from UTC** - Use the dropdown to match the server's time offset in order to display the timestamp correctly.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async chunks** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Dell OpenManage Enterprise server in parallel at any given point.
2. **Fetch inventories from devices** *(required, default: true)* - Select to fetch inventories related to devices.
3. **Fetch warranties of devices** - Select this option to fetch warranties of each device.
4. **Use DNS name as device hostname** - Select this option to use the DNS name as the device hostname. If enabled, this will affect correlation and the device ID.
5. **Fetch compliance status of devices** - Select this option to fetch the compliance statuses of each device and the components of the device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                                        | Supported | Notes |
| ---------------------------------------------- | --------- | ----- |
| OpenManage Enterprise Version 3.3.1 and higher | Yes       |       |