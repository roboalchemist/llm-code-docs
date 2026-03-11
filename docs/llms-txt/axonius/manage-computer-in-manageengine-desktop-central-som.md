# Source: https://docs.axonius.com/docs/manage-computer-in-manageengine-desktop-central-som.md

# ManageEngine  Endpoint (Desktop) Central and Patch Manager Plus - Perform Action

**ManageEngine  Endpoint (Desktop)  Central and Patch Manager Plus - Perform Action**  (Manage Computer in ManageEngine  Endpoint (Desktop)  Central SoM) action   lets you Install/Uninstall desktop central agent and remove details of a computer managed by ManageEngine  Endpoint (Desktop)  Central on the devices that are the result  of the saved query supplied as a trigger (or devices that were selected in the asset table).

<Callout icon="📘" theme="info">
  Note

  To use the action below, you must successfully configure a [ManageEngine  Endpoint (Desktop) Central](/docs/manageengine-desktop-central) adapter connection.
</Callout>

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

## Action Settings

1. **Action type** *(required, default: Install Agent)* - Select the action to be executed on the device:
   * Install desktop central agent.
   * Uninstall desktop central agent.
   * Remove details of a computer managed by ManageEngine Desktop Central.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).