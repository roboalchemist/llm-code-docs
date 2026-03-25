# Source: https://docs.axonius.com/docs/create-atlassian-opsgenie-alert.md

# Opsgenie - Create Alert

**Opsgenie - Create  Alert**  creates an alert in  Opsgenie for:

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

* **Alert message (up to 130 characters)** - Specify the message of the alert, limited to 130 characters.
* **Priority** *(required, default: P3)* - Priority level of the alert. Possible values are P1, P2, P3, P4 and P5. Default value is P3.
* **Integrations API key** - Insert a key associated with the integration in order to create alerts.

## Additional Fields

These fields are optional.

* **Add default incident description** - Select whether to send the incident description to ServiceNow.

  * If enabled, Axonius will include the default incident description (mentioned below) in the ServiceNow incident.
  * If disabled, Axonius will not include the default incident description (mentioned below) in the ServiceNow incident.

  **Message + description example:**
  *Alert - "test" for the following query has been triggered: Missing Sophos*

  *Alert Details*
  *The alert was triggered because: the number of entities is above 0
  The number of devices returned by the query:4
  The previous number of devices was:4*

  *You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos*

* **Tags** - Tags of the alert.

* **Alias** - Client-defined identifier of the alert, that is also the key element of [Alert De-Duplication](https://docs.opsgenie.com/docs/alert-deduplication).

* **User** - Display name of the request owner.

* **Description**  - Description field of the alert that is generally used to provide a detailed information about the alert.

<Callout icon="📘" theme="info">
  **Note:**

  You can replace text with params that can assist you in better informing in the Jira Issues. The following params can be used:

  ```json
    {{HOSTNAME}}, {{USERNAME}}, {{FIRST_NAME}}
  ```
</Callout>

* **Note**  - Additional note that will be added while creating the alert.

* **Source** - Source field of the alert. Default value is IP address of the incoming request.

## APIs

Axonius uses the [Atlassian Opsgenie Alert API](https://docs.opsgenie.com/docs/alert-api#section-create-alert).
Also see [API Key Management](https://support.atlassian.com/opsgenie/docs/api-key-management/).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).