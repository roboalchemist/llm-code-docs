# Source: https://docs.axonius.com/docs/github-update-issue.md

# GitHub - Update Issue

**GitHub - Update Issue** updates an existing issue in GitHub for:

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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the GitHub adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [GitHub](/docs/github) adapter connection.
</Callout>

* **Organization** - The GitHub organization name.
* **Repository** - The GitHub repository name.
* **Issue Number** - The issue number.
* **Issue State** - The state of the issue.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  For a detailed explanation on GitHub connection parameters, refer to [GitHub Parameters](/docs/en/github#parameters).
</Callout>

* **Issue Title** - An updated title for the issue.
* **Issue Body** - Optional body text for the issue, for example, a justification for why it was opened.
* **Issue State Reason** - A reason to change the issue's state.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [GitHub API](https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#update-an-issue).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* 'Issues' repository permissions (write)
* 'Pull requests' repository permissions (write)

The permissions should be set on the token used in the connection.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).