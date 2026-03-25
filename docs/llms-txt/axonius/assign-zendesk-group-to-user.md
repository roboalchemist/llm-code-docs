# Source: https://docs.axonius.com/docs/assign-zendesk-group-to-user.md

# Zendesk - Assign Group to Users

**Zendesk - Assign Group to Users** assigns a group to a Zendesk user for each user returned by the saved query supplied as a trigger (or devices selected in the asset table).

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

* **Use stored credentials from Zendesk adapter** - Select this option to use [Zendesk](/docs/zendesk-adapter) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Zendesk](/docs/zendesk-adapter) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Group IDs (comma separated)** - Enter a comma-separated (,) list of group IDs. Users will be added to or removed from these groups.
* **Add assignment** - 'Add' is selected.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Sub Domain** *(required)* - The subdomain used to access Zendesk. For example, Axonius is the subdomain for `https://axonius.zendesk.com/`.

  * **User Name** *(required)* - The username of an Axonius dedicated user account.

  * **API Key/Token** *(required)* - An API Key/Token associated with a user account that has permissions to perform this action.

  * **Password** -  The password of the Axonius dedicated user account.

  * **2FA Secret Key** - The secret generated in Zendesk for setting up two-factor authentication for the Zendesk user created to collect SaaS Management data. See Zendesk documentation for instructions on [how to set up two-factor authentication (2FA) and generate the 2FA secret](https://support.zendesk.com/hc/en-us/articles/4408829277466-Using-2-factor-authentication).

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Justification reason** *(optional)* - The reason for assigning the group to the user.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Zendesk Update User](https://developer.zendesk.com/api-reference/ticketing/users/users/#update-user) API.

## Required Permissions

This action can be performed by Zendesk Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents#topic_cxn_hig_bd) to manage end users or team members.
Agents can only update end users. Administrators can update end users, agents, and administrators.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).