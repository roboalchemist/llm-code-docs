# Source: https://docs.axonius.com/docs/update-tickets-zendesk.md

# Update Zendesk Tickets

**Update Zendesk Tickets** updates tickets relevant for:

* Assets matching the Enforcement Set query or assets selected on the relevant asset page. For example, if the action is triggered on asset type=Users, the action updates tickets linked to each user.
  * When triggered on any asset type except Tickets (for example, Users, Devices), this action updates related ServiceNow tickets based on your selection in the **Select Which Related Tickets To Update** dropdown (see below).
  * When triggered on asset type=Tickets, this action runs on all tickets resulting from the selected query. The **Select Which Related Tickets To Update** dropdown is not applicable in this scenario.

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

* **Use stored credentials from Zendesk adapter**  - Select this option to use the [Zendesk](/docs/zendesk) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** dropdown becomes available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Zendesk](/docs/zendesk) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Ticket Main Settings

These fields are optional.

* **Set ticket tags (replaces current)** - This field allows you to overwrite all existing ticket tags with a comma-separated list of tags. Type a tag (string) and press Enter, comma (,), or semicolon (;). Alternatively, paste a comma-separated list into the field.

* **Ticket Status** - From the dropdown, select the ticket status: new, open, pending, hold, solved, closed.

* **Ticket Assignee** - Type the name of the user assigned to the ticket.

* **Ticket Comments** - Type comments for this ticket.

* **Select Which Related Tickets To Update** - Relevant when this enforcement action runs on an asset category other than Tickets. Select which tickets to update.

## Ticket Additional Settings

These fields are optional.

* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Mapping Fields From Axonius** - Use the **Field Mapping Wizard** to map **Axonius fields** to fields in Zendesk (**Vendor fields**). In this way, you can transfer data found in Axonius into Zendesk. The wizard shows you which fields exist in the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note

  For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping)(where in step 3, the external fields to fill in are the **Vendor fields**).
</Callout>

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Sub Domain** - The sub-domain of the Zendesk server.

  * **User Name** - User name associated with a user account that has permissions to update assets.

  * **API Key/Token** - An API Key/Token associated with a user account that has permissions to update assets.

  * **Password** - The password of the Axonius dedicated user account.

  * **2FA Secret Key** - The secret generated in Zendesk for setting up two-factor authentication for the Zendesk user created to collect SaaS Management data. See Zendesk documentation for instructions on [how to set up two-factor authentication (2FA) and generate the 2FA secret](https://support.zendesk.com/hc/en-us/articles/4408829277466-Using-2-factor-authentication).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).