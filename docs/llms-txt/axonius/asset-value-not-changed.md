# Source: https://docs.axonius.com/docs/asset-value-not-changed.md

# Asset Value Not Changed

## Overview

The **Asset value not changed** event triggers a Workflow when **Asset Investigation** confirms that there has been no change in the value of an asset field you have selected to track, over a specified period (days, weeks, or months).

* **Asset Investigation** runs every 6 hours, checking for changes in tracked asset field values since its previous run.

<Callout icon="📘" theme="info">
  Note

  Adapters supporting differential fetches run more frequently (every 15 minutes) to detect changes in asset field values. These frequent changes are aggregated and factored into the main Asset Investigation calculation, which runs every 6 hours.

  Read more about [**Asset Investigation**](/docs/asset-investigation) for full details.
</Callout>

* A Workflow configured with this event runs only on assets whose tracked field values have not changed within the timeframe you specify.

* The system compares the asset's current value to its historical values based on the history available in Asset Investigation. The maximum timeframe you can select is limited by this available history.

<Callout icon="📘" theme="info">
  Note

  * Only asset fields covered in Asset Investigation are available for selection and tracking.

  * Only assets that have recorded values (including 'earliest value') recorded in Asset Investigation at the time the event is created are included as assets for the Worfklow trigger.
</Callout>

## Selecting and Configuring the Event

**To select and configure the Asset value not changed event**

1. In the **Trigger Type** (for a triggering Event) or **Event** pane (for a non-triggering Event), select  ![AssetValueNotChangedButton](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetValueNotChangedButton.png).
2. In the **Asset value not changed** section that opens:
   1. Select the asset type for comparison of the adapter field.
   2. From the adapter dropdown, select an adapter.
   3. From the **Select Axonius field** dropdown, select a field. This dropdown includes all fields supported by **Asset Investigation**.
   4. Select the number of **Days**, **Weeks**, or **Months** during which to check for a lack of change in the asset value.

**Triggering Event Screen**

![EventAssetValueNotChanged.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventAssetValueNotChanged.png)

* You select the asset type in which to compare adapter fields. Subsequent nodes run on this asset type (the default).
* The **Add Timeout** option is not available.

**Non-Triggering Event Screen**

![EventAssetValueNotChanged.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventAssetValueNotChanged.png)

* The event retrieves the asset from the previous node.
* The **Add Timeout** option can be enabled.

## Use Case Example

Use this event to flag items that have stalled in a process, ensuring management attention.

**Scenario:** Trigger a Workflow if a critical helpdesk ticket's status has not changed in one month.

**Configuration:** Configure the Event to track the *ticket status* field for 4 Weeks.

**Workflow Action:**

* If the status has been 'product block' for the last month, send an email to the VP Product.

* If the status has been 'CR' (Change Request) for the last month, send a different email to the VP Engineering.