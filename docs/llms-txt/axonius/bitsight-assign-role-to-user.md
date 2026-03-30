# Source: https://docs.axonius.com/docs/bitsight-assign-role-to-user.md

# BitSight - Assign Role to User

**BitSight - Assign Role to User** assigns a role to BitSight user for each user returned by the saved query supplied as a trigger (or devices selected in the asset table).

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

* **Use stored credentials from  BitSight Security Ratings adapter** - Select this option to use [BitSight Security Ratings](/docs/bitsight-security-ratings) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [BitSight Security Ratings](/docs/bitsight-security-ratings) adapter connection.
</Callout>

* **Role** - Select the role to assign the user.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* * **User guid** -  The guid of the user to which to assign the role.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **BitSight Domain** - The hostname or IP address of the Datadog server.

  * **API Key** - API key associated with a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Company Name** - The name of the company from which to fetch data. Leave empty to fetch data from parent company.

  * **CIDR Data CSV File** - Upload the .csv file with your CIDR data. This is a CSV file that allows adding data for a specific IP CIDR range. The CSV file should contain the following columns, "CIDR Block", "Country", "Attributed To", "Source", "AS Number". If an IP address is contained in the CIDR block in the CSV file, the values from the other columns in this file are applied to the device.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Justification reason** - Enter the reason the user is being created.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).