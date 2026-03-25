# Source: https://docs.axonius.com/docs/ca-service-management.md

# CA Service Management

CA Service Management is an IT service management (ITSM) solution that offers incident management and IT asset management.

## Parameters

1. **CA CMDB Domain** *(required)* - The hostname or IP address of the CA Service Management server.
2. **Username** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="CAServiceMaangemetn.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CAServiceMaangemetn.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **CA CMDB device type include list** *(optional, default: empty)* - Specify a comma-separated list of device types.
   * If supplied, all connections for this adapter will fetch only devices whose type is any of the comma-separated list of CA device types  you have specified.
   * If not supplied, all connections for this adapter will fetch any device from CA CMDB.
2. **CA CMDB asset lifecycle status include list** *(optional, default: empty)* - Specify a comma-separated list of asset lifecycle statuses.
   * If supplied, all connections for this adapter will fetch only devices whose status is any of the comma-separated list of CA asset lifecycle statuses  that have been defined in this field.
   * If not supplied, all connections for this adapter will fetch devices with any status on CA CMDB.
3. **Fetch only active devices** \*(required, default: False)
   * If enabled, all connections for this adapter will fetch only active devices from CA CMDB.
   * If disabled, all connections for this adapter will fetch also inactive devices from CA CMDB.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>