# Source: https://docs.axonius.com/docs/software-profile.md

# Software Profile

The **Software Profile** page provides detailed information about the Software selected. Click on a software item, the **Software Profile** page opens.

<Image alt="SoftwareProfilePageN" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SoftwareProfilePageN.png" />

The **Software Profile** page is similar to the [Asset Profile page](/docs/asset-profile-page), with all of its relevant capabilities.  In addition it displays the following two tabs:

* **Software Versions**
* **Associated Devices**

### Software Information

The side pane shows profile information about the Software selected. This information presents the name of the  Software found to help you understand what the Software asset is that you are looking at.

For each Software the following information is displayed (when available).

* The Vendor name
* The Software name.

If there are no values in these fields, they are not displayed.

## Software Versions

<Image alt="SoftwareVErsionNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SoftwareVErsionNew.png" />

The **Software Versions** page shows the following information, sorted by Software Version number:

* **Adapter Connections** -   Shows the adapter connections from which the software version was fetched.  Hover over a field  to see  the adapter or all the adapters that this software version comes from. Click the arrow to see all adapters that fetched the field, and its value on each of them.
* **Software Version** - The software version. The table is displayed by order of version from highest to lowest by default. You can click on the arrow to change the sort order, or to sort by version if the table has been sorted by another parameter.
* **Software Name** -  The software name.
* **Software Vendor** - The software vendor.
* **End-of-life** - The date this software reaches end-of-life.
* **Is End-of-life** - Whether the software has reached end-of-life (either Yes or no)
* **End-of-support** - The date this software reaches end-of-support.
* **Is  End-of-support** -  Whether the software has reached end-of-support (either Yes or no)
* **Device Count** - The number of devices on which this software version was found. Click on the device count to view all of the devices with this software version on the **Devices** page.
* **Last Used On** - An aggregated  date field that shows the latest date this software version was  used.

### Filter Detailed Software Display

You can filter the detailed software versions as follows:

* **Adapter Connections** - Select one or more adapter connections.

* **Software Version** - Select one or more Software versions to display.

* **Software Name** - Select one or more Software names.

* **Software Vendor** - Select  one or more vendors.

* **End-of-life** -  Use the Time Range to filter versions that reached end of life in the last X days, or within  a certain time range.

* **Is End-of-life** -  Select yes or no to filter either by versions that have reached end-of-life, or that that have not.

* **End-of-support** -  Use the Time Range to filter versions that reached end of support in the last X days, or within a certain time range.

* **Is End-of-support** - Select  yes or no to filter either by versions that have reached end-of-support, or that that have not.

* **Last Used On** - Use the Time Range filter to filter versions by the date they were last used.

Click **Reset** to  clear the   filters.

## Associated Devices

<Image alt="SWProfileDEvicesN2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SWProfileDEvicesN2.png" />

**Adapter Connections** - Shows the adapter connections from which the device was fetched.  Hover over a field  to see  the adapter or all the adapters that this software comes from.

Click the arrow to see all adapters that fetched the field, and its value on each of them.

* **Preferred Host Name** - the value of the Preferred Host Name.

* **Installed Software: Software Version** - the software version. If there is more than one version the number of additional values.  If more than one version is available, the first few versions are displayed with the number of additional values available shown in blue.  Click to copy the version.

* **Installed Software: Software Name** - The name of the Installed Software.

* **Installed Software: Software Vendor** - The name of the Installed Software Vendor.

### Setting Columns Display

You can use **Edit Columns** to set the columns displayed on the Associated Devices page, so that you can see columns related to the devices you are investigating. When you add a column, the data displayed in some of the columns is already refined for the Software displayed.  Refer to [Setting Page Columns Display](/docs/setting-page-columns-display).

### Filtering and Searching

You can filter the **Associated Devices** page as follows:

**Search** - enter any value by which to search for an adapter connection or software version  (this is free text search).

* **Adapter Connections** - Select one or more adapter connections.

* **Software Versions** - Select one or more software versions to display.

Click **Clear All** to  clear the   filters.
Click **View in Devices** to open the page on the **Devices** page  filtered by the specific software entity you chose and any other filters you selected.

## Exporting Software Profile Data to CSV

You can export the Software Versions and the Associated Devices data to a CSV file. Learn about [exporting  asset data to a CSV file](/docs/exporting-devices-data-to-csv).

* For **Associated Devices** you can choose to split the CSV file by Installed Software. Installed software and Security Finding Instances cannot be added to the exported CSV file.

* For **Software Versions** you can select **Export associated devices** to include information about the devices in the CSV file created. Select the device fields to include in the file, refer to [exporting  asset data to a CSV file](/docs/exporting-devices-data-to-csv).