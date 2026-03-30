# Source: https://docs.axonius.com/docs/network-scanner-enrichment.md

# Axonius Network Discovery - Enrich Asset Data

**Axonius Network Discovery - Enrich Asset Data** enriches devices with network discovered data, such as hostname (using the IP address for devices without a hostname) for:

* Assets returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  This Enforcement Action only works with Device assets.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the [Axonius Network Discovery](https://docs.axonius.com/axonius-help-docs/docs/network-scanner) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      To use this option, you must successfully configure a [Axonius Network Discovery](https://docs.axonius.com/axonius-help-docs/docs/network-scanner) adapter connection.
    </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Comma separated list of new DNS resolvers** - Comma separated list of new DNS resolvers. When provided, the listed DNS servers are used in the reverse DNS action to get the hostname from the IP addresses. When no list is provided, the default DNS server is used.
* **Use public IP address** and **Use non public IP address** - Select any of these options (or both) to determine the source(s) of the IP addresses used in this action.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The DNS servers should have the option to perform the reverse DNS request type PTR.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).