# Source: https://docs.axonius.com/docs/software-versions-view.md

# Software Versions View

The **Software Versions View** is available for Axonius users who have **Axonius Software Assets** enabled. This view is available from the **Devices** page and allows you to:

* View a list of all software entities installed on each device, their versions, vendors, and other data.
* Discover which software have reached or are about to reach their end-of-life (EOL) or end-of-support (EOS).

In this view, each row in the **Devices** table is expanded by all software entities installed on the device, with the following fields displayed for each software.

* Installed Software: Software Name
* Installed Software: Software Vendor
* Installed Software: Software Version
* Installed Software: End of Life
* Installed Software: End of Support Date

To access this view, from the **Devices** page, click **Edit Table** and under **Saved Views**, select **Software Versions View**.

<Image alt="select software versions view" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Select%20view.png" />

<Callout icon="📘" theme="info">
  Note

  All data in the Software Versions View, including EOL and EOS data, is enriched based on information from the [Axonius Software Catalog.](/docs/axonius-software-catalog)
</Callout>

Each row in this view is automatically expanded by the **Installed Software** complex field, which means it displays a list of all software entities installed on the device. To learn more about this capability, refer to [Expanding Assets by a Complex Field](/docs/expanding-assets-by-a-complex-field).

![Expanding software list.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Expanding%20software%20list.png)

## Exploring Software Entities

You can use the different filtering tools of the **Devices** table to show only devices containing software that meet specific criteria - for example, a specific version.

### Step 1 - Running a Query

1. In the **Query Wizard**, from the **Source** drop-down, select Complex Field **(OBJ)**.
2. Enter the Installed Software complex field.
3. Add the parameters you want to display. For example, you can search for devices that have a certain software installed from version X and up.

![Software Versions View Query Wizard.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Software%20Versions%20View%20Query%20Wizard.png)

### Step 2 - Refining the Data

The results of the query defined in the previous step show all devices that meet the defined criteria, but they still include other software installed on each device.
To hide any other software from view and show only software that meet the criteria, you can use the **Refine Data** capability. To learn more about data refinement, see [Refining the Data Displayed in Table Columns and Rows](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows).

1. Click the **Refine Data** main button.
2. In the **Refine Data Display** dialog, the **Installed Software** complex field tab is already selected.
3. Open the **Refine display by field value** pane.
4. Enter the required parameters for filtering the data.
5. Click **Apply**.

<Image alt="Refine data" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine%20software%20data.png" />

According to this example, only devices that have the McAfee ePO software installed, from version 5 and up, are displayed. Any other software installed on these devices is removed from the table.

![refined software versions results.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/refined%20software%20versions%20results.png)

## Exploring End of Life / End of Support Data

A common use case for employing the Software Versions View is to detect EOL / EOS dates. For accurate results, do this first in the Query Wizard and then in the Refine Data Display dialog, according to the steps explained in the previous section.
In the following example, we want to display only devices that have installed software that will reach their EOL during the next 0 days. The query parameters are as follows:

* **Field:** Installed Software: End of Life (a nested field of the Installed Software complex field)
* **Function:** next days
* **Value:** 0

<Image alt="EOL query" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EOL%20query.png" />

After refining the data by the same parameters, only devices that have some installed software whose EOL date is in the next 0 days are displayed.

## Accessing Device's Software Data from the Software Page

Each row in the **Software** table represents a software entity and contains by default the **Device Count** field, showing how many devices with this software exist.

![Software view with Device Count](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Device%20count%20column.png)

Click the number displayed under **Device Count** to view a list of devices containing this software. This redirects you to the **Devices** page, displaying the Software Versions View and refined automatically by the software's unique ID. In the example below, we clicked the **Device Count** from the Microsoft row in the **Software** page.

![Devices with specific software](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Device%20page_specific%20software.png)

The **Refine Data Display** dialog is automatically populated with this condition:

![Refine by software](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Refine_specific%20software.png)

If there is EOL / EOS data available for this software, it will also be displayed after you click **Device Count** and reach the **Devices** page - assuming the appropriate fields are added to the view.

![eol/eos data](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EOL_EOS.png)