# Source: https://docs.axonius.com/docs/netbox.md

# NetBox

NetBox is an open source web application to help manage and document computer networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Networks

## Parameters

1. **NetBox Domain** *(required)* - The hostname or IP Address of the NetBox server.
2. **Custom NetBox Domain Path Prefix** *(optional)* -  If you have configured a custom path prefix for the NetBox API, enter it here. The path should not include `/api` at the end, as this is automatically added by the adapter. For example, if your NetBox API is located at `mydomain.com/netbox_services/api`, enter the value `netbox_services` in this field.
3. **Authentication Token** *(optional)* - Use the API key you have generated, if required.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Netbox.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Netbox.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **NetBox role include list** *(optional)* - Enter a comma-separated list of NetBox roles. Note that values are case-sensitive.
2. **NetBox role exclude list** *(optional)* - Enter a comma-separated list of NetBox roles to exclude. Note that values are case-sensitive.

<Callout icon="📘" theme="info">
  Note

  The excluded list may only be used when the include list is empty. When the include list is empty and the exclude list has roles to be excluded, the adapter will fetch all the available roles and discard the ones present in the excluded list. When both lists are empty the roles will not be used to fetch devices.
</Callout>

3. **NetBox tenant include list** *(optional)* - Enter a comma-separated list of NetBox tenants. Note that values are case-sensitive.
4. **Fetch virtual machines** - Select to include virtual machines in the fetch.
5. **Fetch IPAM IPs** - Select to fetch all known IPs with their hostnames.
6. **Include custom fields for devices** - Select this option to also fetch custom fields for devices.
7. **Do not include Domain in Hostname** *(optional)* - Select to not include the domain within the hostname.
8. **Fetch active devices only** - Select to only fetch active devices.
9. **Include contacts info for devices** - Select this option to fetch contacts associated with each device (<Anchor label="NetBox Documentation - Contacts" target="_blank" href="https://netboxlabs.com/docs/netbox/features/contacts/">NetBox Documentation - Contacts</Anchor>).
10. **Fetch IPAM Prefixes** - Select this option to fetch IPAM Prefixes as Network assets.

## Required Permissions

Users must have View permissions in order to fetch assets, as per [NetBox Documentation - Permissions](https://docs.netbox.dev/en/stable/administration/permissions/).

* "NetBox will check for the `dcim.view_device` permission to fetch devices. If the user has not been assigned this permission (either directly or via a group assignment), NetBox will return a 403 (forbidden) HTTP response."

* "Internally, in NetBox, all actions granted by a permission (both built-in and custom) are stored as strings in an array field named `actions`."