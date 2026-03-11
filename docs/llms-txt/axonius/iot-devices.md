# Source: https://docs.axonius.com/docs/iot-devices.md

# IoT Devices

IoT devices are used for general business operations, such as security cameras, smart building controls, and industrial sensors (Operational Technology - OT). For more information, see [Overview of IoT and IoMT Assets](https://docs.axonius.com/axonius-help-docs/docs/overview-of-iot-and-iomt-assets).

Use the **IoT** asset page to view the details of the IoT devices on your network. Click the **Assets** icon on the left pane, and then select **Compute > IoT**.

<Image align="center" alt="IoT Assets" border={true} width="100% " src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_cloud/IoT_Assets_Table.png" className="border" />

## Adapter Connections

The displayed information is collected through the Axonius Network Inspector device and the [Axonius Network Inspector adapter](https://docs.axonius.com/axonius-help-docs/docs/axonius-network-inspector).

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_cloud/IoMT_Adapter.png" className="border" />

## IoT Devices Table

The **IoT** asset page displays a table listing the IoT devices in a default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns.

Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## IoT Device Fields

There are numerous fields that you can view and query on the IoT asset page. This includes the following most-important fields:

* **Asset Entity Info** - Information about the actual asset entity fetched. This lists what the actual device is.

* **Category** - The category of the IoT device (for example: building automation, surveillance, network, utility).

* **Asset Name** - The unique, human-readable name assigned to the device, typically the hostname or a custom identifier.

* **Device Model** - The specific hardware type or variant of a particular device, designated by its manufacturer.

* **Device Manufacturer** - The company or vendor that designs, produces, and sells various types of devices.

* **Network Interfaces: IPv4s** - The current list of IPv4 addresses associated with the device network interfaces.

* **Network Interfaces: MAC** - The unique hardware media access control (MAC) address of the device network interfaces.

* **Last Seen** - The most recent timestamp indicating when the device was observed or communicated with by any connected adapter.

* **VLAN** - The VLAN to which the device is connected.

* **VLAN Name** - The name of the VLAN to which the device is connected.

* **Severity Score** - The maximum score of the vulnerabilities that this device has.

## Adding Custom Fields to the IoT Devices

You can add custom fields to one or more IoT device at the same time. You can use this to add additional details like a description or or any important information that you want to display.

Refer to [Working with Custom Data](/docs/working-with-custom-data) to learn about adding custom fields.

## Creating Queries on IoT Devices

You can create queries on this page using the Query Wizard or the Basic Query and query fields. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

<Image align="center" alt="IoT Query" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_cloud/Query_IoT.png" className="border" />

After running the query, the overview and table show the relevant Expenses, filtered by the criteria you defined in your query.

## Add Tags to an IoT Device

You can use tags to assign context to your IoT devices for granular filters and queries. You can apply new or existing tags to the selected devices. The list of selected tags is applied to all selected applications.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags.

## View an IoT Device Profile

You can click on an individual IoT device asset to view all its relevant data. For more information, see [Asset Profile Page](/docs/asset-profile-page).