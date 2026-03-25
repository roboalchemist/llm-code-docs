# Source: https://docs.axonius.com/docs/iomt-devices.md

# IoMT Devices

IoMT devices include clinical equipment like infusion pumps, patient monitors, and imaging systems. For more information, see [Overview of IoT and IoMT Assets](https://docs.axonius.com/axonius-help-docs/docs/overview-of-iot-and-iomt-assets).

Use the **IoMT** asset page to view the details of the IoMT devices on your network. Click the **Assets** icon on the left pane, and then select **Compute > IoMT**.﻿

<Image align="center" alt="IoMT Assets" border={true} width="100% " src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_cloud/IoMT_Assets_Table.png" className="border" />

## Adapter Connections

The displayed information is collected through the Axonius Network Inspector device and the [Axonius Network Inspector adapter](https://docs.axonius.com/axonius-help-docs/docs/axonius-network-inspector).

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_cloud/IoMT_Adapter.png" className="border" />

## IoMT Devices Table

The **IoMT** asset page displays a table listing the IoMT devices in a default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns.

Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Display](https://docs.axonius.com/axonius-help-docs/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## IoMT Device Fields

There are numerous fields that you can view and query on the IoMT asset page. This includes the following most-important fields:

* **Asset Entity Info** - Information about the actual asset entity fetched. This lists what the actual device is.
* **Category** - The category of the IoMT device (for example: infrastructure, bedside, labs, radiology).
* **Asset Name** - The unique, human-readable name assigned to the device, typically the hostname or a custom identifier.
* **Device Model** - The specific hardware type or variant of a particular device, designated by its manufacturer. For IoMT devices, this includes a wide range of medical device models.
* **Device Manufacturer** - The company or entity that designs, produces, and sells various types of devices. For IoMT devices, this includes a wide range of medical device manufacturers (for example: Phillips, Baxter, Nova, Siemens).
* **Network Interfaces: IPv4s** - The current list of IPv4 addresses associated with the device network interfaces.
* **Network Interfaces: MAC** - The unique hardware media access control (MAC) address of the device network interfaces.
* **Last Seen** - The most recent timestamp indicating when the device was observed or communicated with by any connected adapter.
* **ePHI** - Indicates whether the device contains ePHI (electronic Protected Health Information). The presence of ePHI on a device makes its security a high-priority concern.
* **VLAN** - The VLAN to which the device is connected.
* **VLAN Name** - The name of the VLAN to which the device is connected.
* **Severity Score** - The maximum score of the vulnerabilities that this device has.

## Adding Custom Fields to IoMT Devices

You can add custom fields to one or more IoMT devices at the same time. You can use this to add additional details like a description or manually add acc

Refer to [Working with Custom Data](https://docs.axonius.com/axonius-help-docs/docs/working-with-custom-data) to learn about adding custom fields.

## Creating Queries on IoMT Devices

You can create queries on this page using the Query Wizard or the Basic Query and query fields. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

<Image align="center" alt="IoMT Query" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_cloud/Query_IoMT.png" className="border" />

After running the query, the overview and table show the relevant Expenses, filtered by the criteria you defined in your query.

## Add Tags to IoMT Devices

Use tags to assign context to your IoMT devices for granular filters and queries. Apply new or existing tags to the selected devices. The list of selected tags is applied to all selected applications.

Refer to [Working with Tags](https://docs.axonius.com/axonius-help-docs/docs/working-with-tags) to learn about adding tags to IoMT devices.

## View an IoMT Devices Profile

You can click on an individual asset in IoMT devices to see all its relevant data. For more information, see [Asset Profile Page](https://docs.axonius.com/axonius-help-docs/docs/asset-profile-page).