# Source: https://docs.axonius.com/docs/asset-profile-page-complex-fields.md

# Asset Profile Page - Complex Fields

The **Tables** section shows fields that can be presented in a table view. These are also known as complex fields.
You can see all of the complex fields in the **Tables** section.
The complex fields which are displayed depend on the data fetched by your system. A set of predefined fields are displayed.

<Image alt="ComplexTable" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-DZQ1FAMF.png" />

Click on a complex field to display its table. If a complex field is brought only from a specific adapter connection, it is not displayed by default. You can add new complex fields to this left pane, even if they are fetched by one specific adapter.

### Displaying Complex Fields

Fields which are made up of a number of different parameters are displayed in blue in the **All Fields** table. Click any of those fields to display them as a table under **Tables**.

<Image alt="ComplexinAllFields" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WT2JW462.png" />

Each Complex Field is displayed as a table. The column on the left-hand side displays the Adapter Connections which lets you identify the source for each row. Each table consist of the following elements, in addition to the data displayed:

<Image alt="TableExample" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-L5CSVPMM.png" />

* **Search bar** - Free text search on the table results.
* **Adapter Connections** - Filter the display by specific adapter connections.
* **Filter** - Add a filter for any of the table's fields to display data that includes specific values for those fields.
* **Total** - The total number of displayed results is displayed on the top left side of the table.
* **Reset** - Clear all search and filters of the display.
* **Export CSV** - Export the table to a CSV file.
* **Navigation and pagination** - By default, 20 results are displayed in each of the tables page. You can change the number of results per page and choose between 20, 50, or 100, by clicking the appropriate icon on the bottom left side of the table.
  Use the pagination bar on the bottom right side of the table to move between the pages of the table.

**To create a filter**

1. Above the table, click **+ Filter**.
2. Select the field you want to filter by.
3. Enter or select the field value you want to display.

Some nested fields (displayed as columns in the table) might contain multiple values, aggregated from multiple adapter connections. For example, the **IP Addresses** column in the **Network Interfaces** table might contain multiple IP addresses. To see which adapter contributed each value, expand the table by the Adapter Connection column (the Expand button is circled in red).

<Image alt="ExpandButton" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-NIDWCMMI.png" />

<Image alt="ExpandByAdapterCon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExpandByAdapterCon.png" />

Alternatively, hover over the \[+number] icon in the relevant cell and click **View All Results**. The value list with the associated adapter connections will be displayed on a new page.

### Nested Complex Fields

When a complex field is nested in another complex field, a column is created in the complex field's table with a link to open the inner field in a separate page. This makes it easier to view the data and navigate between complex fields.

<Image alt="Nested1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-Z4SQ5BDS.png" />

You can use the Query Wizard to search for certain values inside the nested complex field objects. In this example, the query searches inside the 'Network Interface' complex field object for certain values inside the Vlan complex field.

**To search values inside nested complex fields**

1. In the Query Wizard, from the Source drop-down, select **Complex Field**.
   ![QueryWizardSourceDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QW_NestedComplex1.png)
2. Select the top-level complex field you want to query.
3. In the subsequent row, from the Adapter drop-down, select **Complex Field**.
   ![QueryWizardAdapterDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QW_NestedComplex2.png)
4. Select the nested complex field you want to query.
5. Create the query for the nested complex field.
6. Click **Search**.

<Image alt="QW_NestedComplex" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QW_NestedComplex.png" />

## Managing the Complex Fields

You can manage the list of complex fields that are displayed in order to only see fields that interest you.
Any complex field can be shown as a table (including fields that were fetched from a specific adapter connection). Click on a field shown in blue in the main table to display this as a table, and display its link in **Tables** in the side panel. Any asset that belongs to that complex field is then displayed on the table.  You can choose **Pin to list** to save the complex field table to your display.

<Image alt="PintoList" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PintoList.png" />

Once you pin a complex field, this display is saved for you. Next time you open the system, these fields are displayed. Note pinned fields are only displayed if they contain data for the asset that you selected. If you do not want to see that complex field any more, click unpin to remove the field from the display. Default **Complex Field** tables are also part of the display. You can also unpin these tables if you are not interested in seeing them.

<Callout icon="📘" theme="info">
  Note

  Pinning and unpinning Complex Field tables only affects assets for your user account, and not for other people using the system.
  Pinned and unpinned Complex Fields affect all of the assets on your system, not only this specific asset.
</Callout>

<Image alt="Unpinfrom" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Unpinfrom.png" />

### Exporting Complex Field Tables

You can export **Complex Field Tables** to a CSV file.
To export the results displayed, select  **Export CSV**. A CSV file is created and downloaded to your system.
The CSV file is named according to the table, with the current date in UTC.

## Complex Fields Available

This page details some of the complex fields that are displayed on the **Asset Profile** page. The complex fields which are displayed depend on the data fetched by your system. In addition, you can select a complex field in the **Asset Profile** table and click on it to display it in the list of complex fields. Refer to **Managing the Complex Fields** for information.

The following tables may be displayed, depending on the collected data.

### Associated Azure Configuration

The **Associated Azure Configuration** table lists the following information from Azure devices:

* Policy Name
* Compliance State (for compliant devices)
* Non Compliance State (for non-compliant devices)
* Account Name

### Associated Devices

The **Associated Devices** table lists the devices associated with that user.
Each row shows information about the device including: Device Name, Device Serial, Device Status, Device Unique ID,  and Device Labels.
Click on a device to open it on the **Devices** page.
![AssociatedDevicesTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssociatedDevices\(1\).png)

### Agent Versions

The **Agent Versions** table lists the agents installed on the device.
Information displayed for each agent includes its Name, Version, and Status.
![AgentVersionsTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-6PVZBOV2.png)

### Connected Hardware

The **Connected Hardware** table lists registry logged connected hardware.

<Image alt="ConnectedHardware" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConnectedHardware.png" />

### Firewall Rules

The **Firewall Rules** table lists firewall rules that define allowed or denied traffic to and from virtual machines.
![FirewallRulesTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Firewall_Rules.png)

Each rule consists of the following information:

* **Name** and **Source** - For example, AWS security group or GCP firewall rule.
* **Allow / Deny** - Action is either allow or deny access.
* **Direction** - Incoming (INGRESS) or outgoing (EGRESS) traffic, not both.
* **Target** – Target subnet. Firewall rule that applies to any IP address is displayed as “0.0.0.0/0” for IPv4 and as “::/0” for IPv6.
* **Target Subnet Count**
* **Protocol** – Internet protocol for which the rule applies. If protocol value is ‘Any’, the firewall rule applies for all protocols.
* **From Port**, **To Port** – Range of ports for which the rule applies. If port values are not specified, the firewall rule applies for all ports.

For example:

* ‘Rule 1’ allows outgoing traffic to any IP address using any protocol.
* ‘Rule 2’ denies incoming traffic from a specific subnet (108.162.192.0/18) using TCP port 443.

| Name   | Source                      | Allow/Deny | Direction | Target           | Protocol | From Port | To Port |
| ------ | --------------------------- | ---------- | --------- | ---------------- | -------- | --------- | ------- |
| Rule 1 | AWS Instance Security Group | Allow      | EGRESS    | 0.0.0.0/0        | Any      |           |         |
| Rule 2 | AWS Instance Security Group | Deny       | INGRESS   | 108.162.192.0/18 | TCP      | 443       | 443     |

### Hard Drives

The **Hard Drives** table lists hard drives installed on the device, including their file system, total, and free sizes.
![HardDrivesTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-R2FUI394.png)

### Installed Software

The **Installed Software** table lists installed software on the device, including its version and vendor.
![InstalledSoftwareTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-L5CSVPMM.png)

### Linked Tickets

The **Linked Tickets** table lists tickets, which were created in third-party ticketing systems (for instance, ServiceNow) on the asset, using Enforcement Actions see  [Create Incident or Ticket](https://docs.axonius.com/axonius-help-docs/docs/create-incident), and enables you to track their progress. Each linked ticket includes, by default, the following fields: Ticket Vendor, Ticket ID, Key (Display ID), Status, Summary, Created, Updated (the date and time that the ticket was created and updated), and Adapter Connections.
![LinkedTicketsTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LinkedTickets.png)

As tickets are created by Axonius Enforcement Actions, the **Adapter Connections** column displays the Axonius icon ![AxoniusIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AxoniusLogo.png)

<Callout icon="📘" theme="info">
  Note

  Although Enforcement Actions that create tickets use the credentials of the asset's relevant ticketing vendor adapters (for example, ServiceNow) to open tickets, the tickets themselves are not written as assets that belong to this adapter connection (effective for tickets created Version 6.0.16 and later), but as belonging to the Axonius pseudo adapter (and therefore the Axonius icon appears in the **Adapter Connections** column).
</Callout>

Learn more on [how to monitor third-party tickets from within the Axonius application](/docs/monitoring-third-party-tickets).

<Callout icon="📘" theme="info">
  Note

  You can also view ticket information in the [Tickets Tab](/docs/asset-profile-page#tickets-tab) on the Asset Profile page.
</Callout>

### Associated Ticket Devices

The **Associated Ticket Devices** table lists the devices associated with the ticket. Each row shows information about one associated device including: **Host Name**, **Source Application**, **Device IPs**, **Internal Device ID**, and **Adapter Connections**.

Clicking the **Internal Device ID** opens the Asset Profile page of the device associated with the ticket.
![AssociatedTicketDevicesTable](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssociatedTicketDevices.png)

### Affected Assets

The **Affected Assets** table lists the assets impacted by the ticket.

Each row shows information about one affected asset including:

* **Asset Name** - The name of the asset.
* **Asset Type** - The category of the asset (e.g., device, server, network device, application).
* **Entity ID** - A unique identifier for the asset within the system.

Clicking the **Entity ID** opens the Asset Profile page of the asset impacted by the ticket.

### Local Admins

The **Local Admins** table lists admin users identities logged on to this device.

### Network Interfaces

The **Network Interfaces** table lists network interfaces collected by the different adapters, including MAC addresses, IP addresses, and subnet addresses.

<Image alt="NetworkInterfaces(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetworkInterfaces(1).png" />

### Notes

Notes entered on the [asset profile](/docs/asset-profile-page#notes-tab). The Notes table includes the note, user name, and last update date.

### Open Ports

The **Open Ports** table lists ports open to the world, including the access protocol and service name.

<Callout icon="📘" theme="info">
  Note

  The table is displayed only if collected from '[Enrich Device Data with Shodan](/docs/enrich-device-data-with-shodan)' or from the following adapters: Amazon Web Services (AWS) with Shodan, Censys, Forescout CounterACT, CyCognito CyCAST Platform, Nmap Security Scanner, Qualys Cloud Platform.
</Callout>

<Image alt="OpenPorts" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-N0HKFFQM.png" />

### OS Installed Security Patches

The **OS Installed Security Patches** table lists security patches installed on Windows devices.

<Image alt="OSInstalledSEcPAtches" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OSInstalledSEcPAtches.png" />

### OS Available Security Patches

The **OS Available Security Patches** table lists security patches available for Windows devices.

### Qualys Vulnerabilities

The **Qualys Vulnerabilities** table lists vulnerabilities fetched from <Anchor label="**Qualys Cloud Platform** adapter connections" target="_blank" href="/docs/qualys-cloud-platform">**Qualys Cloud Platform** adapter connections</Anchor>.

### Rapid7 Vulnerabilities

The **Rapid7 Vulnerabilities** table lists vulnerabilities fetched from <Anchor label="**Rapid7 Nexpose and InsightVM** adapter connections" target="_blank" href="/docs/rapid7-nexpose">**Rapid7 Nexpose and InsightVM** adapter connections</Anchor>.

### Related Assets

The **Related Assets** table lists the assets that triggered a Finding alert.
Information displayed for each asset includes:

* **Asset Name** - Name of the related asset.
* **Entity ID** - ID of the Axonius entity in the identity provider.
* **Asset Type** - The type of asset. For example, Devices, Users, Groups.

### Running Processes

The **Running Processes** table lists running processes collected from the device.

### Services

The **Services** table lists running and stopped services collected from the device.

### Shares

The **Shares** table lists shared folders on the device, including the name, description, and path.

### Normalization Reasons

The **Normalization Reasons** table displays indicators that use the holistic data available in Axonius to hint why a record didn't correlate with others. For the full list of the normalization reasons that can be displayed for different asset types,[see Normalization Reasons Complex Field](/docs/normalization-reasons-complex-field).

### Users

The **Users** table lists user identities logged on to this device, including SID, Username, Last Use Time, and indications whether the user is a local and/or active user.

<Image alt="Users" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Users.png" />

### Security Findings

<Callout icon="❗️">
  **Note**

  This table was previously called **Vulnerable Software**.
</Callout>

The **Security Findings** table lists vulnerable software and vulnerability details, including:

* **Vuln ID** - Link to the CVE details in the NIST National Vulnerability Database (NVD).
* **Software Name** and **Software Vendor** - If the CVE is applicable for multiple software, these fields are populated as "Multiple Software" and "Multiple Vendors".
* [Common Vulnerability Scoring System (CVSS)](https://nvd.nist.gov/vuln-metrics/cvss), a numeric score used to supply a qualitative measure of severity. The CVSS rating is fetched from the source (v2,0, v3.0, v4.0, etc.).
* **CVE severity** -[LOW/MEDIUM/HIGH/CRITICAL](https://nvd.nist.gov/vuln-metrics/cvss) value which is based on the CVSS rating.
* CVE description, synopsis, and reference
* [**CVE Vector information**](/docs/vulnerabilities#cve-vector-information)
* **Axonius Risk Score** - This column is displayed in the table only when a Risk Score has been calculated for this asset. For more information, see [Risk Score Settings](/docs/risk-score-settings).

<Image alt="VulnSfotware" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-YYM2JG1A.png" />

### CISA Known Exploited Vulnerabilities

The **CISA Known Exploited Vulnerabilities** table displays additional details from the CISA catalog of existing CVEs of vulnerabilities detected in your software.

The details include:

* **CVE ID** - Link to the CVE details in the NIST National Vulnerability Database (NVD).

* **Vendor** and **Product** - The vendor name and product name. If the CVE is applicable for multiple software, these fields are populated as "Multiple Software" and "Multiple Vendors".

* **Action** - Describes the recommended action to mitigate the vulnerability.

<Image alt="CISAKnowUpdated" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CISAKnowUpdated.png" />