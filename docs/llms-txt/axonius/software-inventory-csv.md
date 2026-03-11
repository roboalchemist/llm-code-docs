# Source: https://docs.axonius.com/docs/software-inventory-csv.md

# CSV - Software Inventory

CSV - Software Inventory imports software inventory information from a CSV file.

## Asset Types Fetched

* Software, SaaS Applications

The adapter parameters are the same as the [CSV Adapter](/docs/csv). Since the CSV - Software Inventory adapter provides data about Software and SaaS Applications only, unlike the generic CSV adapter, there is no option to configure the adapter to contain information about Users, Devices, or any other type of asset.

The functionality of this adapter is the same as the [CSV adapter](/docs/csv).

## Which fields are imported with a Software Inventory file?

The following data is imported as part of the Software Inventory file.

<Callout icon="💡" theme="warn">
  **Attention**

  The field names must be **exactly** as listed under "Field".
</Callout>

| Field                      | Notes                        | Required? |
| :------------------------- | :--------------------------- | :-------- |
| `Axonius_Software_Name`    | The software name            | Yes       |
| `Axonius_Publisher_Name`   | The software vendor          | Yes       |
| `Axonius_Software_Version` | The software version         | Yes       |
| `Axonius_Approval_Status`  | The software approval status | No        |

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Custom Parsing** - See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.