# Source: https://docs.axonius.com/docs/managing-saas-applications-discovery.md

# Managing SaaS Applications Discovery

<Callout icon="📘" theme="info">
  Note

  This feature is only available for Axonius SaaS Applications administrators.
</Callout>

Axonius shows you an inventory of all of the [SaaS Applications](/docs/saas-applications) discovered on your system. SaaS Applications are discovered in various ways, whether through applications directly installed, or applications that are part of applications, or by using various indicators on your system that imply that a specific application is present, for example, if your system has YouTube Music Desktop application installed, then it is quite likely  that the YouTube application is in use on your system. These indications have been found to have a high level of correlation to indicate that a specific application is present.
However, you may decide that you prefer not to use the predefined indicators presented by Axonius, and select different matched applications, or declare that these indicators should not present a match for any application at all.

Use the **SaaS Application Discovery Management** page to manage how Axonius discovers SaaS Applications on your system.

To manage SaaS Applications Discovery, you need the following permissions:
*Manage SaaS Application Discovery*

To access the **SaaS Applications Discovery Management** page:

1. Click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png) in the top right corner of the platform to open **System Settings**.

2. In the Categories/Subcategories pane of the **System Settings** page, expand **Data**, and select **SaaS Applications Discovery Management**. The **SaaS Applications Discovery Management** page opens.

![SaaSAppDiscManagement.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SaaSAppDiscManagement.png)

The following information is displayed on the **SaaS Applications Discovery Management** page:

* **Discovery Indicator** - The actual indicator. All Discovery Indicators of a specific SaaS Application can be viewed in the 'Discovery Indicators' field on the SaaS Application asset page.

* **Suggested Matched Application** - The name of the application that Axonius suggests to match based on the Discovery indicator.

* **Edited Matched Application** - The application you suggest to use for your systems.

* **Adapter** - The adapter that fetched this information.

* **Time received** - The time the application was discovered.

### Editing the Matched Application

You can change the Application that Axonius suggests to display.

1. To edit the Matched Application, hover over the row and select the edit icon. The **Edit Matched Application** window opens.

![EditMatchedApplication](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditMatchedApplication.png)

2. In the dialog that opens, from the **Changed matched application to** drop-down,  select an available application that you want to match. The drop-down shows all the SaaS applications in the Axonius inventory. If you don't want to match any application, choose *No Match*.

3. (*Optional*) If you want to add a new application to match with the discovered application (and appear in the SaaS Application Repository), start typing the name of the new application and click **Add New SaaS App**.
   ![AddNewApplication.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddNewApplication.png)

4. Click **Save Changes**.

5. Once you change the Matched Application, the SaaS Applications displayed in Axonius on relevant pages are updated after the next discovery cycle.

### Bulk Editing Matched Applications

You can change the matched application for a number of Discovery Indicators in one go.

1. Select all the *Discovery Indicators* you want to change, the **Edit Matched Application** dialog opens.
2. From the **Changed matched application to** drop-down, select an available application that you want to match. The drop-down shows all the SaaS applications in the Axonius inventory. If you don't want to match any application, choose **No Match**.
3. Click **Save Changes**.
4. Once you change the Matched application, the SaaS Applications displayed in Axonius on relevant pages are updated after the next discovery cycle.

## Filtering and Searching for Discovery Indicators

Use the filter bar at the top of the page to select criteria to filter the **SaaS Application Discovery** table. The table can be filtered by:

* **Suggested Match Application**
* **Edited Match Application**
* **Adapter**
* **Time Range**

You can also search the table according to **Discovery Indicator** by entering a search string in the **Search** field.

Click the column headers to sort the table.

### Exporting the List of Discovered SaaS Applications to CSV

The list of discovered SaaS Applications can be exported to a CSV file. Only the currently listed items are exported.

**To export the list of discovered SaaS Applications**

1. On the top right above the **SaaS Application Discovery Management** table, click **Export CSV**. The file is generated and downloaded to the local computer.

### Ignoring Specific Domain Name Strings

In order to avoid conflicts from applications using similar domain names, you can [enter a list of specific strings from domain names to ignore](/docs/configuring-data-aggregation-settings) during the SaaS Applications Discovery process.
Any strings added to this list will not be processed during the discovery but will be displayed in their application's domain name on the **Edit Matched Applications** window.

***

See [Working with Tables](/docs/working-with-tables) to learn more about tables in Axonius.