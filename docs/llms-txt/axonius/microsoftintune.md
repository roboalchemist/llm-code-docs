# Source: https://docs.axonius.com/docs/microsoftintune.md

# Microsoft Intune

Microsoft Intune is a management tool that offers mobile device and application management capabilities.

<Callout icon="📘" theme="info">
  Note

  This adapter is in addition to the [Microsoft Entra ID (Azure AD) and Microsoft Intune](/docs/microsoft-azure-active-directory-ad) adapter. It does not remove any capabilities from Microsoft Entra ID (Azure AD) and Microsoft Intune. It is recommended to use the Microsoft Intune adapter when you need to fetch Intune data separately from Entra.
</Callout>

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications

## Before You Begin

### APIs

Axonius uses the [Microsoft Graph API](https://graph.microsoft.com).

### Permissions

The following permissions are required:

**Delegated Permissions**

* DeviceManagementManagedDevices.Read.All - This is a Delegated permission on the **Application** level. To set this permission, refer to the [instructions for setting permissions on Entra ID, Microsoft 365, and Intune](/docs/microsoft-azure-active-directory-ad#set-permissions).

**Application Permissions**

* DeviceManagementApps.ReadWrite.All, DeviceManagementManagedDevices.ReadWrite.All - these permissions are required to successfully use the **Enrich Intune Devices with Intune Devices Reports**[advanced setting](/docs/microsoftintune#advanced-settings).
* DeviceManagementServiceConfiguration.Read.All

### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Azure Client ID** - The Application ID of the Axonius application.
2. **Azure Client Secret** - Specify a non-expired key generated from the new client secret.
3. **Azure Tenant ID** - The ID for Microsoft Entra ID.
4. **Cloud Environment** - Select your Microsoft Azure or Microsoft Entra ID cloud environment type.

![IntuneParameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-I9WA8OUO.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoint Config

This section lists different data types to enrich Devices with. Enable **Fetch Devices from Intune Devices** to be able to select the enrichment data you're interested in.

**Notes on specific configurations:**

* When enabling **Enrich Intune Devices with Intune Devices Reports**, expand the **Reports** section to select specific Intune reports to enrich devices with.
* When enabling **Enrich Intune Devices with Specific Fields**, select the fields you want to enrich devices with from the **Fields to fetch** dropdown.

  <Callout icon="📘" theme="info">
    **Notes**

    1. **For existing connections:** This setting was previously named **Hardware Information**. If you had a connection where this setting was enabled before the name change, the `hardwareInformation` and `physicalMemoryInBytes` fields will be selected to maintain the same data collection behavior. You can change that from the **Fields to fetch** dropdown.
    2. This setting increases fetch time substantially. Only enable it if necessary.
  </Callout>

### Additional Advanced Settings

* **Fetch Software from Intune All Apps** - Select to fetch all applications registered in Intune. These applications are then saved in Axonius as Software assets and their **Approval Status** is set to Approved. See [Software Registry](/docs/software-approval-list) for more information on approved / unapproved software.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| Graph API v1.0 | Yes       | --    |

### Related Enforcement Actions

* [Microsoft Intune - Update Device](/docs/intune-update-device)
* [Microsoft Intune - Delete Managed Device](https://docs.axonius.com/axonius-help-docs/docs/intune-delete-managed-device)
* [Microsoft Intune - Delete Autopilot Device](https://docs.axonius.com/axonius-help-docs/docs/intune-delete-autopilot-device)

<br />