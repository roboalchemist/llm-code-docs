# Source: https://docs.axonius.com/docs/cisco-unified-communications-manager-ucm.md

# Cisco Unified Communications Manager (UCM)

Cisco Unified Communications Manager provides secure and manageable call control and session management.

The Cisco Unified Communications Manager adapter enables Axonius to fetch and catalog communication devices, providing visibility into their inventory details and registration status.

## Asset Types Fetched

* Devices

## Before You Begin

### Required Permissions

Create a dedicated user for AXL Access. It is recommended that a User and Group for your application be created, rather than using the admin user.

1. Create a special application user for AXL access.
2. Create a User Group for AXL access.
3. Put an AXL user in this user group.
4. To enable Read-Only access, add the **Standard AXL API Users** and **Standard AXL Read Only API Access** roles to the user group.

## Connection Parameters

1. **Cisco UCM Domain** *(required)* - The hostname or IP address of the Cisco UCM server.
2. **API Version** - Select the version of the Cisco UCM API.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CiscoUCM.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoUCM.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch inactive devices** - Select this option to fetch inactive devices from the Cisco UCM server.
2. **Use description as the asset name** - Select this option to use the description as the asset name if the name field is not available.
3. **Enrich Devices with IPs** - Select this option to fetch IP addresses of phones and enrich the devices with this information.
4. **Exclude devices with no IP addresses** - Select this option to exclude devices with no IP address from the fetch.

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                                                      | Supported | Notes |
| ------------------------------------------------------------ | --------- | ----- |
| Cisco Unified Communications Manager version 10.5 and higher | Yes       |       |