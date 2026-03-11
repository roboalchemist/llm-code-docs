# Source: https://docs.axonius.com/docs/carbon-black-cb-defense-create-user.md

# VMware CB Cloud - Create User

**VMware CB Cloud - Create User** creates a user in VMware CB Cloud for:

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the VMware Carbon Black Cloud (Carbon Black CB Defense) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [VMware Carbon Black Cloud (Carbon Black CB Defense)](/docs/carbon-black-cb-defense) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Draft** - When selected, the user is created only in Axonius.
* **First Name**, **Last Name** and **Email** - Optional user details.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **VMware Carbon Black Cloud Domain** - The full URL of the VMware Carbon Black Cloud server.

  * **API ID** and **API Secret Key** - Use the API ID and the API Secret Key you generated from the Connectors page of the VMware Carbon Black Cloud console. For details on how to generate these, see the [CB Defense API authentication reference](https://developer.carbonblack.com/reference/cb-defense/authentication/).

  * **Access API key** and **Secret API key** - If necessary, include how these are generated or obtained.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Organization Key** - You can find your Organization Key in the VMware Carbon Black Cloud Console under **Settings** `>` **API Keys**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

* **Justification reason** - The reason for creating this user.

## APIs

Axonius uses the [ Carbon Black Developer Network](https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/user-management/#create-user).

## Required Ports

Axonius must be able to communicate via the following ports:

* Carbon Black Defense API server port

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Manage Users

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).