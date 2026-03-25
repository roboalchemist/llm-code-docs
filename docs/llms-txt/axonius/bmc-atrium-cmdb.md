# Source: https://docs.axonius.com/docs/bmc-atrium-cmdb.md

# BMC Atrium CMDB

BMC Atrium CMDB stores information about the configuration items (CIs) in your IT environment and the relationships between them.

Related Enforcement Actions:

* [BMC Atrium - Create or Update Asset](/docs/create-or-update-bmc-atrium-asset)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the BMC Atrium CMDB server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **API Source** *(required, default: arsys)* - Select the type of API source from the dropdown:
   * If an AR System server, select **arsys**
   * If a BMC Atrium Configuration Management Database, select **cmdb**
4. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![BMC Atrium CMDB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BMC%20Atrium%20CMDB.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

<br />

**Skip devices marked as Deleted**  - Select to exclude deleted devices from the fetch.

### Arsys Settings

1. **Specific Field list** - When the API Source is 'ARSYS', specify which fields to fetch. All unspecified default fields will be ignored.

<Callout icon="📘" theme="info">
  Note

  The fields must match the names appearing in the API response.
</Callout>

2. **Device Forms** *(default: AST:ComputerSystem)* - Specify the Arsys forms from which devices will be fetched. By default, devices are fetched from the `AST:ComputerSystem` form. You can add additional forms such as `AST:BaseElement` to fetch devices from multiple sources.

<Callout icon="📘" theme="info">
  Note

  Enter form names exactly as they appear in the Arsys API (e.g., `AST:ComputerSystem`, `AST:BaseElement`). All forms must follow the same schema structure as `AST:ComputerSystem`.
</Callout>

### CMDB Settings

3. **CMDB API Page Size** *(default: 500)* - Specify the page limit for CMDB API requests.
4. **CMDB API Qualification** - Enter a filter for the CMDB API requests, if needed.
5. **CMDB API fetch AST:AssetPeople** *(default: true)* - Select this option to fetch users.
6. **Fetch custom instance(s)** - Toggle on this option to fetch devices from outside of the standard BMC\_ComputerSystem class.
   * **Custom instance(s)** *(optional)* - Enter a list of dataset ID, namespace, class names to fetch devices from in this format: "Dataset ID/Namespace/Class Name".
7. **Fetch specific attributes (CMDB API)** *(optional)* - Enter a list of specific customer-provided attributes to fetch. When filling in attributes, the fields `ReconciliationIdentity`, `Name`, and `SerialNumber` must be present for devices to be parsed. If no additional attributes are entered, the adapter will fetch all available attributes for each device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [BMC Atrium Core 9.0 API](https://docs.bmc.com/docs/ac9000/rest-api-502997627.html).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [BMC Atrium Core 9.0 API](https://docs.bmc.com/docs/ac9000/rest-api-502997627.html).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| BMC Atrium CMDB 9.0 | Yes       |       |