# Source: https://docs.axonius.com/docs/nessus-delete-account.md

# Nessus - Delete Account

**Nessus - Delete Account** deletes a user account from an existing Tenable Nessus group for users that match the parameters of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

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

* **Use stored credentials from the Tenable Nessus adapter** - Select this option to use the the first connected Nessus adapter credentials.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Tenable Nessus](/docs/tenable-nessus) adapter connection.
  </Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Address** - The address of the Nessus host.

  * **Port** - The port to use to connect to the Nessus host.

  * **User Name** and **Password** - The credentials for a user account that has the required permissions to add IP addresses.

  * **Access API key** and **Secret API key** - These values must be created in the Tenable.io console. To generate an API key in the Tenable.io console, see [Generate an API Key (Tenable Nessus 10.7)](https://docs.tenable.com/nessus/Content/GenerateAnAPIKey.htm).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
</Callout>

## APIs

Axonius uses the [pyTenable 1.4.22 documentation](https://pytenable.readthedocs.io/en/stable/) API.

## Required Ports

Axonius must be able to communicate with the values supplied in **Connection Parameters** via the following ports:

* 80
* 443

## Required Permissions

The values supplied in [Connection Parameters](#connection-parameters) above must have permission to write.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).