# Source: https://docs.axonius.com/docs/axonius-network-inspector.md

# Axonius Network Inspector

Axonius Network Inspector is built for IoT, OT, and cyber-physical environments to establish a trusted, continuously updated system of record for every connected device, discover communication patterns and secure the network. It's functionality spans from identifying exposed ePHI to implementing full network segmentation.

This **adapter** is used together with the Axonius Network Inspector server appliance, which is a **physical device** that connects to the organizational network. For more information about the server appliance device, see [Axonius Network Inspector Deployment](https://docs.axonius.com/axonius-help-docs/docs/network-inspector-deployment).

The connection settings for this adapter are configured automatically.

## Types of Assets Fetched

* Devices

## Advanced Settings

Use the advanced settings to purge assets with a short lifecycle from the platform, based on the conditions below. Use the plus sign to enter as many conditions as required.

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Asset Retention based on IP Range & Type**

Click the plus sign to enter:

* **IP Range (CIDR)** - Set a range of IP addresses from which assets will be removed.
* **Asset Types** - Enter asset types. The asset types must match the values fetched from the Type field from the adapter.
* **Retention Hours** (default 24) - The time to keep the assets for. The default value is 24. You can enter a value between 1 hours and 336 hours.
* **Note** - Add a note if needed.

**Fetch only assets with last seen in the last X days** - Enter a number of days. The adapter will only fetch assets that were last seen within that number of days.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 8.0.