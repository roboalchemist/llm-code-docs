# Source: https://docs.axonius.com/docs/add-ips-to-qualys-user-subscription.md

# Qualys - Add IP Addresses to User Subscription

**Qualys - Add IP Addresses to User Subscription** adds IP addresses to an existing subscription or to a new one.

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

* **Use stored credentials from the [Qualys Cloud Platform adapter](/docs/qualys-cloud-platform)** - This uses the first connected Qualys Cloud Platform adapter credentials. This action can only be used when the Qualys Cloud Platform action is configured.

  <Callout icon="📘" theme="info">
    Note

    * To use this option, you must successfully configure a [Qualys Cloud Platform adapter](/docs/qualys-cloud-platform)] adapter connection.
    * The user name and the password used for the adapter connection must have the [Required Permissions](#required-permissions) listed below.
  </Callout>

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Qualys Cloud Platform Domain** - The hostname of the Qualys API (for example, qualysapi.apps.qualys.com). For more details on how to determine your Qualys API URL, see [Identify your Qualys platform](https://www.qualys.com/platform-identification/).

  * **User name** and **Password** -  The credentials for a user account that has the [Required Permissions](#required-permissions) to add a specified list of tags to each host asset in Qualys.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Use private IP addresses** - Choose whether to add private IP addresses to Qualys.
* **Use public IP addresses** - Choose whether to add public IP addresses to Qualys.
* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded. Axonius will not add to Qualys devices IP addresses in the IP range of the specified CIDRs.
* **Enable hosts for the VM app** - Enable the host for the VM app.
* **Enable hosts for the PC app** - Enable the hosts for the PC app.
* **Only send preferred IPs** - When selected, the action will use only the preferred IPs in the IP network.
* **IP Network** - The IP address of the network that all the IPs in the related query should belong.

## Required Permissions

The credentials used to connect to Qualys must be associated with one of the following user roles and have the following permissions:

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