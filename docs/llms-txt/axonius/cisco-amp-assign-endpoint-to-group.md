# Source: https://docs.axonius.com/docs/cisco-amp-assign-endpoint-to-group.md

# Cisco AMP - Assign Assets to Group

**Cisco Advanced Malware Protection (AMP) - Assign Assets to Group** assigns assets to a group in Cisco Advanced Malware Protection (AMP) for:

* Assets that match the selected saved query, and
* Assets that match the Enforcement Action dynamic values, if defined.
* Assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  To use this Enforcement Action, you must successfully configure a [Cisco Advanced Malware Protection (AMP)](/docs/cisco-advanced-malware-protection-amp) adapter connection.
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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Cisco Advanced Malware Protection (AMP) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Cisco Advanced Malware Protection (AMP)](/docs/cisco-advanced-malware-protection-amp) adapter connection.
  </Callout>

* **Group Name** - The name of the group to which to add the assets.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Required Permissions

The user account used to connect must have full access to Cisco AMP.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).