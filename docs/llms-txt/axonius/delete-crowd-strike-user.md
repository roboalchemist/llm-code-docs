# Source: https://docs.axonius.com/docs/delete-crowd-strike-user.md

# CrowdStrike Falcon - Delete User

**CrowdStrike Falcon - Delete User** deletes users from CrowdStrike Falcon for:

* Users that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from CrowdStrike Falcon adapter** - Select this option to use [CrowdStrike Falcon](/docs/crowdstrike-falcon) connected adapter credentials.  (add a link to adapter, only write the first when the select adapter is not there)
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [CrowdStrike Falcon](/docs/crowdstrike-falcon) adapter connection.  Full link to adapter when relevant
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [CrowdStrike API](https://assets.falcon.crowdstrike.com/support/api/swagger.html).

## Required Ports

Axonius must be able to communicate via the following ports:

* TCP Port 443

## Required Permissions

The account used to access CrowdStrike must have user management write permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).