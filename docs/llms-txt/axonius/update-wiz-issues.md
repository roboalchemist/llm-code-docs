# Source: https://docs.axonius.com/docs/update-wiz-issues.md

# Wiz - Update Issues

**Wiz - Update Issues** updates the status, notes, and resolution details of Wiz Issues for assets selected from a query. or from the relevant Assets page. The action performs a GraphQL `UpdateIssue` mutation using the Wiz API connection.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Permissions

The Wiz API client must have the following scopes. If any required scope is missing, Wiz returns a GraphQL Unauthorized Error and the action fails.

* write:issue\_status
* write:issue\_due\_at,
* write:service\_ticket,
* write:issue\_comments
* write:threat\_issue\_status (For updating threat issues)

## APIs

Axonius uses the [wiz.io API](https://app.wiz.io/login?redirect=%2Fwiz-docs).

## Required Ports

* **TCP port 443**

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Wiz adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the Select Adapter Connection drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      **Note**

      To use this option, you must successfully configure a [Wiz](/docs/wiz) adapter connection.
    </Callout>

* **Issue ID** - The unique identifier of the Wiz Issue to update.

* **Issue status** - Select the status to assign to the issue. The options are:

  * **Open**
  * **In Progress**
  * **Resolved** - When selected, the following fields are also required:

    * **Resolution reason** - Only Threat Detection Issues can be resolved, and the Resolution reasons can be either: `MALICIOUS_THREAT / NOT_MALICIOUS_THREAT / SECURITY_TEST_THREAT / PLANNED_ACTION_THREAT / INCONCLUSIVE_THREAT`
    * **Resolution note** - Add a free text note explaining the status change.
  * **Rejected** - When selected, the following fields are also required:

    * **Resolution reason** - Graph Control Issues and Cloud Configuration Issues can be rejected manually, and the Resolution reasons can be either: `MALICIOUS_THREAT / NOT_MALICIOUS_THREAT / SECURITY_TEST_THREAT / PLANNED_ACTION_THREAT / INCONCLUSIVE_THREAT`
    * **Issue note** - Add a free text note explaining the status change.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  * If you are using the Wiz Axonius Integration service account for your adapter connection, enable **Use stored credentials from the Wiz adapter**, as the all the necessary permissions for adapter connection and actions are already set.

  * If you are using a custom Wiz service account for your adapter connection, migrate to using the [Wiz Axonius Integration service account](/docs/wiz#configuring-the-wiz-axonius-integration).
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).