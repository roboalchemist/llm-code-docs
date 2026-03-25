# Source: https://docs.axonius.com/docs/isolate-unisolate-in-carbon-black-cb-response.md

# VMware Carbon Black Cloud EDR - Isolate/Unisolate Assets

**VMware CB EDR - Isolate Assets** quarantines each of the assets returned by the selected query or assets selected on the relevant asset page.

The VMware Carbon Black EDR (Carbon Black CB Response) network isolation functionality allows administrators to isolate endpoints that may be actively involved in an incident, while preserving access to perform Live Response on that endpoint and collect further endpoint telemetry.

**VMware CB EDR - Unisolate Assets**  restores full network connectivity to each of the assets (endpoints) that are the result of the query.

<Callout icon="📘" theme="info">
  NOTE

  To use the actions below, you must successfully configure a [VMware Carbon Black EDR (Carbon Black CB Response)](/docs/carbon-black-cb-response) adapter connection.
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

## Required Fields

These fields must be configured to run the Enforcement Set and apply to both Enforcement Actions described in this document.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from VMware Carbon Black EDR (Carbon Black CB Response) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [VMware Carbon Black EDR (Carbon Black CB Response)](/docs/carbon-black-cb-response) adapter connection.
  </Callout>

### Isolate in VMware Carbon Black EDR

To configure the **VMware CB EDR - Isolate Assets** action, do as follows:

1. Define a unique action name.
2. If you are using multi-nodes, choose the Axonius node to use to interact with the adapter when executing the enforcement action.
3. Save the action.

### Unisolate in VMware Carbon Black EDR

To configure the **VMware CB EDR - Uninsolate Assets** action, do as follows:

1. Define a unique action name.
2. If you are using multi-nodes, choose the Axonius node to use to interact with the adapter when executing the enforcement action.
3. Save the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).