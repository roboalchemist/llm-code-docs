# Source: https://docs.axonius.com/docs/qualys-remove-ips-from-asset-group.md

# Qualys - Remove IPs from Asset Group

**Qualys - Remove IPs from Asset Group** removes all Axonius IP addresses from a Qualys asset group for:

* Assets returned by the selected query or assets selected on the relevant asset page.

Qualys asset groups contain a list of IP addresses that exist both in Axonius and in Qualys. This action removes these IP addresses from a specific asset group after selecting in the query assets that belong to that group.

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

* **Use stored credentials from the Qualys Cloud Platform adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Qualys Cloud Platform](https://docs.axonius.com/axonius-help-docs/docs/qualys-cloud-platform) adapter connection.
  </Callout>

* **Group name** - Name of the asset group in Qualys you want to remove the Axonius IP addresses from.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Qualys Cloud Platform Domain** - The hostname of the Qualys API (for example, qualysapi.apps.qualys.com). For more details on how to determine your Qualys API URL, see [Identify your Qualys platform](https://www.qualys.com/platform-identification/).

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * <br />
</Callout>

<br />

* **Use private IP addresses** - Choose whether to add remove IP addresses from Qualys.

* **Use public IP addresses** - Choose whether to remove public IP addresses from Qualys.

* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded. Axonius will not remove from Qualys devices IP addresses in the IP range of the specified CIDRs.

* **Send all preferred IPs** - Enable to send all the IPs provided in the query without any filtering.

* **Only send preferred IPs** - Enable to send only the preferred IPs in the IP network. These are IPs that can be selected by the filters detailed above: only private IPs, only public IPs, or only IPs that don't appear in the CIDR exclude list.

  <Callout icon="📘" theme="info">
    Note

    To enable **Only send preferred IPs**, you must also enable **Send all preferred IPs**. However, **Send all preferred IPs** can be enabled independently.
  </Callout>

* **IP Network** - The IP address of the network that all the IPs in the related query should belong.

* **Use Host Name** - Select this to remove the preferred hostname from the specified group.

## APIs

Axonius uses the [Qualys API](https://drive.google.com/file/d/136MG7pLBJ0a1c5Ae7aqlyqnbme1o7I9f/view).

## Required Ports

Axonius must be able to communicate via the following ports:

* 80
* 443

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).