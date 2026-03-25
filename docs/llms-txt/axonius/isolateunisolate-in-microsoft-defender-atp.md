# Source: https://docs.axonius.com/docs/isolateunisolate-in-microsoft-defender-atp.md

# Microsoft Defender ATP - Isolate/Unisolate Assets

**Microsoft Defender ATP - Isolate Assets** quarantines assets returned by the selected query or assets selected on the relevant asset page.

**Microsoft Defender ATP - Unisolate Assets** restores full network connectivity to assets returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from the Defender ATP adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Microsoft Defender for Endpoint](/docs/microsoft-defender-atp) adapter connection.
  </Callout>

* **Comment** - Enter a comment that will be displayed.

* **Isolation Type** - Select an isolation type, either 'Full' or 'Selective'.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Required Permissions

The Microsoft Entra ID (Azure AD) application configured in the [Defender ATP adapter](/docs/microsoft-defender-atp) must have the following Application permission:

* Machine.Isolate

See [Microsoft Defender ATP](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/isolate-machine?view=o365-worldwide#permissions) documentation for more information.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).