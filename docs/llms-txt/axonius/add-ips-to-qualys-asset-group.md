# Source: https://docs.axonius.com/docs/add-ips-to-qualys-asset-group.md

# Qualys - Add IP Addresses to Asset Group

**Qualys - Add IP Addresses to Asset Group** (Add IPs to Qualys Cloud Platform) action adds IP addresses to an existing asset group or to a new one.

Asset groups are logical groups of host assets, domain assets, and scanner appliances (if applicable). Asset groups can be based on importance, priority, location, or ownership.

<Callout icon="📘" theme="info">
  Note

  This action supports IPv4 addresses only.
</Callout>

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Qualys Cloud Platform adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Qualys Cloud Platform](/docs/qualys-cloud-platform) adapter connection.
  </Callout>

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Qualys Cloud Platform domain** - The hostname of the Qualys API (for example, qualysapi.apps.qualys.com). For more details on how to determine your Qualys API URL, see [Identify your Qualys platform](https://www.qualys.com/platform-identification/).

  * **User name** and **Password** -  The credentials for a user account that has the [Required Permissions](#required-permissions) to add IP addresses as host assets to an existing asset group or to a new one.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Create asset group** - When selected, Axonius will create a new host asset (if it does not exist), a new asset group, and will associate the host asset to the created group. When not selected, Axonius associate the new host asset (if is does not exist) to an existing asset group, if specified in **Group name**.

* **Group name** - Specify the asset group name to which Axonius will add the IP address as a host asset. When no value is given, Axonius will not associate the host asset to any asset group. When **Create asset group** is enabled, this field must be supplied.
  * When **Create asset group** is enabled and the specified group with that name already exists in Qualys, Qualys will add the new IPs to the group.

* **Use private IP addresses** - Choose whether to add private IP addresses to Qualys.

* **Use public IP addresses** - Choose whether to add public IP addresses to Qualys.

* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded. Axonius will not add to Qualys devices IP addresses in the IP range of the specified CIDRs.

* **Send all preferred IPs** - Enable to send all the IPs provided in the query without any filtering.

* **Only send preferred IPs** - Enable to send only the preferred IPs in the IP network. These are IPs that can be selected by the filters detailed above: only private IPs, only public IPs, or only IPs that don't appear in the CIDR exclude list.

  <Callout icon="📘" theme="info">
    Note

    To enable **Only send preferred IPs**, you must also enable **Send all preferred IPs**. However, **Send all preferred IPs** can be enabled independently.
  </Callout>

* **IP Network** - The IP address of the network that all the IPs in the related query should belong.

* **Use Host Name** - Select this to add the preferred hostname to the specified group.

* **Fail when no IP added** - Select this to enable the following behavior: when the Enforcement Action does not find any IP address to add, instead of a success status, the Action status will be "Failed", and it will display the message "No IPs were added to asset group".

* **IPs to add (overrides other IP selection options)** - Provide IP addresses to add to this action. They will be added regardless of other IP selection settings.

## Required Permissions

The value supplied in [User Name](#connection-settings) must be associated with one of the following user roles and with the following permissions:

1. Manager role with full scope.
2. Unit Manager role with the following permissions:
   * "Add Assets" permissions.
   * Manage (create, edit, delete, view) all assets in their own business unit.

<Callout icon="📘" theme="info">
  Note

  Users with other roles do not have permissions to add IP addresses.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).