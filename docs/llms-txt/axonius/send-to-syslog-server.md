# Source: https://docs.axonius.com/docs/send-to-syslog-server.md

# Syslog Server - Send Log Message

**Syslog Server - Send Log Message** sends a message with the action results summary to syslog and optional messages with the device data for each of the devices in the query results as a JSON file. It sends a JSON file with data about the system entity queried, for queries created  on Activity logs and Fetch History using filters.

To use this action, you must enable the **Use Syslog** setting and configure a Syslog host and port. For more details, see [Configuring Syslog Settings](/docs/configuring-syslog-settings).

The message includes:

* The Enforcement Set name
* The triggered query
* The condition for executing the Enforcement action (if it exists)
* The number of current and previous results

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Message Example

The following text is a sample message.

***

*Alert - "test" for the following query has been triggered: Missing Sophos*

*Alert Details*
*The alert was triggered because: The number of entities is above 0
The number of devices returned by the query:4
The previous number of devices was:4*

\_You can view the query and its results here: `https://demo-latest.axonius.com/devices?view=MissingSophos`

***

## Required Fields

These fields are required to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Message severity** *(default: info)* - Select the message severity: info, warning or error.

## Additional Fields

These fields are optional.

* **Send result details** - When selected, sends additional messages to Syslog with the details of the results.
* **Use RFC5424 Compliant Timestamp** - When selected, sends all Syslog messages using the RFC 5424 protocol.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).