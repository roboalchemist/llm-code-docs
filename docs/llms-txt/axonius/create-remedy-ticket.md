# Source: https://docs.axonius.com/docs/create-remedy-ticket.md

# BMC Helix Remedy - Create Ticket

**BMC Helix Remedy - Create Ticket** creates an incident in Remedy for all relevant entities.

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

These fields are must be configured to successfully run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **BMC Helix Remedy domain** - The domain name of BMC Helix Remedy server.
* **User name** - The user name for the BMC Helix Remedy account.
* **Password** - The password for the BMC Helix Remedy account.
* **Form name** - Specify the form name.
* **Ticket description** - Enter a ticket description.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **First Name** - User's first name.
* **Last Name** - User's last name.
* **Service Type** - The type of service the ticket is opened for. For example, *User Service Restoration*
* **Status** - The status of the ticket. For example, *Assigned*
* **Impact** - The impact of the ticket. For example, *1-Extensive/Widespread*
* **Urgency** - The urgency of the ticket. For example, *1-Critical*
* **Reported Source** - The source that reported the issue. For example, *Direct Input*
* **Add default ticket description** - Enable this option to add a default description to the ticket. The message includes the Enforcement Set name and the selected query, the condition for executing the Enforcement, if such exists, and the number of current and previous results.

  **Message example:**

  ```
  The alert "testAlert" for the following query has been triggered: Missing Sophos_

  _Alert Details_
  _The alert was triggered because: The number of entities is above 0
  The number of devices returned by the query:4
  The previous number of devices was:4_

  _You can view the query and its results here: https://demo-latest.axonius.com/devices?view=Missing Sophos_
  ```

<Callout icon="📘" theme="info">
  Note

  As valid values of these parameters are customer specific, Axonius does not validate them. You must make sure the provided values are correct for the request to complete successfully.
</Callout>

* Enter the proper values for these fields:
  * **Assignee Groups**
  * **Detailed Description**
  * **RLY\_Categorization Tier1**
  * **RLY Categorization Tier2**
  * **TicketID\_RPY**
  * **ID Cliente**

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).