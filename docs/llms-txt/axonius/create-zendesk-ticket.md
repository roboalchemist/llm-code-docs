# Source: https://docs.axonius.com/docs/create-zendesk-ticket.md

# Zendesk - Create Ticket

**Zendesk - Create Ticket** creates a ticket in Zendesk for:

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
* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **Use stored credentials from Zendesk adapter**  - Select this option to use the Zendesk connected adapter credentials. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Zendesk](/docs/zendesk) adapter connection.
</Callout>

* **Requester Full Name** - The full name of the user creating the ticket.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

<Callout icon="📘" theme="info">
  Note - ZenDesk MFA

  The ZenDesk API does not support MFA or SAML; an API token is required when using either of these:

  * User Name Email - Add the /token to the end of the account.

  * Password
</Callout>

## Ticket Main Settings

These fields are optional.

* **Ticket Subject** - Type a short description of the ticket issue.
* **Ticket Body (Description)** - Type a full description of the issue.
* **Ticket Status** - From the dropdown, select the ticket status: new, open, pending, hold, solved, closed.
* **Ticket Priority** *(default: normal)* - From the dropdown, select the ticket priority. Available options: low, normal, high, urgent.
* **Assignee Full Name** - Type the full name of the user assigned to this ticket.
* **Group Name** - Enter the name of the group to which the user creating the ticket belongs.
* **Ticket Form** - Select the value you want to populate in the Form field in this ticket. (Ticket fetch must be enabled to populate this drop-down)
* **Tags to Add** - Select tags from the dropdown or add a list of comma separated new tags to add to the ticket.
* **Create Zendesk Ticket even if no new assets are found in the Query** *(default: enabled)* - When selected, a ticket is generated even if no new assets resulted from the query.

## Ticket Additional Settings

These fields are optional.

* **Add default incident description** - Enable this option to include the default incident description at the end of the ticket body. The incident description message includes the Enforcement Set name, the triggering query, the condition for executing the Enforcement, if such exists, the number of current and previous results, and a list of all affected assets.

<Callout icon="📘" theme="info">
  Message example

  Alert - "test" for the following query has been triggered: Missing Sophos

  Alert Details <br />
  The alert was triggered because: The number of entities is above 0 <br />
  The number of devices returned by the query: 4 <br />
  The previous number of devices was: 4 <br />

  You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos
</Callout>

## CSV Configuration

* **Attach a CSV file with the affected entities** - Enable this option to attach a CSV file containing the results of the query.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Sub Domain** - The sub-domain of the Zendesk server. For example, Axonius is the subdomain for *[https://axonius.zendesk.com](https://axonius.zendesk.com)*.

  * **User Name** - User name associated with an Axonius dedicated user account that has permissions to update assets.

  * **API Key/Token** - An API Key/Token associated with a user account that has permissions to update assets.

  * **Password** - The password of the Axonius dedicated user account.

  * **2FA Secret Key** - The secret generated in Zendesk for setting up two-factor authentication for the Zendesk user created to collect SaaS Management data. See Zendesk documentation for instructions on [how to set up two-factor authentication (2FA) and generate the 2FA secret](https://support.zendesk.com/hc/en-us/articles/4408829277466-Using-2-factor-authentication).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).