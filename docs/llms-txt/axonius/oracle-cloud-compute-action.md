# Source: https://docs.axonius.com/docs/oracle-cloud-compute-action.md

# Oracle Cloud - Start or Stop Compute Instances

**Oracle Cloud - Start or Stop Compute Instances** starts an Oracle Cloud instance for:

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

* **Use stored credentials from Oracle Cloud adapter** - Enable this to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  1. You must enable  **Use stored credentials from Oracle Cloud Adapter** and select an adapter connection to be able to save this Enforcement Set.
  2. To use this option, you must successfully configure a [Oracle Cloud](/docs/oracle-cloud) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Choose action for compute instance**
  * START -  Starts the Oracle Cloud instance.
  * STOP - Stops the Oracle Cloud instance.

## APIs

Axonius uses the following APIs:

* [Public Cloud Machine REST API Reference for Oracle Compute Cloud Service](https://docs.oracle.com/cloud-machine/latest/stcomputecs/ELUAP/GUID-A06DABC3-C214-455A-9264-9946B712FD8E.htm#ELUAP-GUID-62EA9656-0C52-4B7A-9D5F-E57D2245C964)
* [ComputeClient — oci 2.125.0 documentation](https://docs.oracle.com/en-us/iaas/tools/python/2.119.1/api/core/client/oci.core.ComputeClient.html#oci.core.ComputeClient.instance_action)
* [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance.htm)

## Required Permissions

The stored credentials in the selected adapter connection must have permission to start or to stop the following Oracle Cloud instances:

* compute.instances.read
* compute.instances.update
* compute.instanceConsoleConnections.use
* compute.instanceAction

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).