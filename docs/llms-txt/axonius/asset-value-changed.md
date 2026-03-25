# Source: https://docs.axonius.com/docs/asset-value-changed.md

# Asset Value Changed

## Overview

The **Asset value changed** event triggers a Workflow when **Asset Investigation** discovers a change in a value for an asset field you have selected to track.

* **Asset Investigation** runs every 6 hours, checking for changes in tracked asset field values since its previous run.

<Callout icon="📘" theme="info">
  Note

  Adapters supporting differential fetches run more frequently (every 15 minutes) to detect changes in asset field values. These frequent changes are aggregated and factored into the main Asset Investigation calculation, which runs every 6 hours.

  Read more about [**Asset Investigation**](/docs/asset-investigation) for full details.
</Callout>

* A Workflow configured with this event runs only on the assets whose tracked field values have changed.

* The asset's current value is compared to its value at the time the Workflow was last saved.

<Callout icon="📘" theme="info">
  Note

  * Only asset fields covered in Asset Investigation are available for selection and tracking.

  * The **Asset value changed** event ignores initial values. A change in an asset field from NULL to a value is not considered a value change and therefore will not trigger the event.
</Callout>

## Selecting and Configuring the Event

**To select and configure the Asset value changed event**

1. In the **Trigger Type** (for a triggering Event) or **Event** pane (for a non-triggering Event), select ![AssetValueChangedButton](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetValueChangedButton.png).
2. In the **Asset value changed** section that opens:
   1. Select the asset type for comparison of the adapter field.
   2. From the adapter dropdown, select an adapter.
   3. From the **Select Axonius field** dropdown, select a field. This dropdown includes all fields supported by **Asset Investigation**.

**Triggering Event Screen**

![EventTriggerAssetValueChanged.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerAssetValueChanged.png)

* You select the asset type in which to compare adapter fields. Subsequent nodes run on this asset type (the default).
* The **Add Timeout** option is not available.

**Non-Triggering Event Screen**

![EventAssetValueChanged.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventAssetValueChanged.png)

* The event retrieves the asset from the previous node.
* The **Add Timeout** option can be enabled.