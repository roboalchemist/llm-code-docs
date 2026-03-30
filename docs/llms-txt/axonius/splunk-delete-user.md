# Source: https://docs.axonius.com/docs/splunk-delete-user.md

# Splunk - Delete User

**Splunk - Delete User** deletes Splunk users for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Splunk adapter** - Select this option to choose which [Splunk](/docs/en/splunk) connected adapter credentials to use.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Splunk](/docs/en/splunk) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name** - The hostname of the Splunk search head.

  * **Port** - Specify the port of the Splunk system. It is recommended to use TCP port 8089. For more details, see [Splunk Docs - Securing Splunk Enterprise](https://docs.splunk.com/Documentation/Splunk/8.0.3/Security/SecureSplunkonyournetwork).

  * **Protocol** *(rdefault: HTTPS)* - Select between HTTP and HTTPS protocols when using that specific adapter connection.

  * **User Name** and **Password** - The user name and password for an account that has read access to the API.

  <Callout icon="📘" theme="info">
    Note

    If **API Token** is not supplied, **User Name** and **Password** are required.
  </Callout>

  * **API Token** - API token can be used instead of user name and password.

  <Callout icon="📘" theme="info">
    Note

    If **User Name** and **Password** are not supplied, **API Token** is required.
  </Callout>
</Callout>

* **Exclude connections** - Assets from the selected connections will not be included in the query results. You can select more than one.

## APIs

Axonius uses the [Splunk API](https://docs.splunk.com/Documentation/Splunk/9.4.2/RESTREF/RESTkvstore#storage.2Fcollections.2Fdata.2F.7Bcollection.7D).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Permission to delete assets.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).