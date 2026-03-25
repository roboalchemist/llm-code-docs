# Source: https://docs.pentaho.com/pdia-try-pdia/getting-started-with-analyzer-interactive-reports-and-dashboard-designer.md

# Getting Started with Analyzer, Interactive Reports, and Dashboard Designer

This guide covers core Pentaho Business Analytics workflows in one place.

Jump to:

* [About Pentaho business analytics tools](#about-pentaho-business-analytics-tools)
* [Quick tour of the Pentaho User Console](#quick-tour-of-the-pentaho-user-console)
* [Get started with Analyzer Reports](#get-started-with-analyzer-reports)
* [Get started with Interactive Reports](#get-started-with-interactive-reports)
* [Get started with Pentaho Reporting tools](#get-started-with-pentaho-reporting-tools)
* [Get started with Dashboard Designer](#get-started-with-dashboard-designer)
* [Next steps](#next-steps)

### About Pentaho business analytics tools

The topics found in this section give you an overview of the reports and dashboards you create with the User Console, to help you become familiar with the look and feel of the console.

The Pentaho User Console is a web-based design environment where you can analyze data, create interactive reports, dashboard reports, and build integrated dashboards to share business intelligence solutions with others in your organization and on the internet. In addition to its design features, the User Console offers a wide variety of system administration features for configuring the Pentaho Server, maintaining the Pentaho licenses, setting up security, managing report scheduling, and tailoring system performance to meet your requirements.

#### Prerequisites

Before you work with the User Console, install the Pentaho software and configure the Pentaho Server.

See [Install the 30-day trial of Pentaho Data Integration and Analytics](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages/pentaho-evaluation).

#### Expertise

You do not need special skills to use the design environment.

To use system administration features, you should understand your data sources, system configuration, and security providers.

#### Tools

In the User Console, you can access the Pentaho Repository on the server and these tools:

* Analyzer
* Interactive Reports
* Dashboard Designer
* Data Source Wizard
* Data Source Model Editor

#### Sign-in credentials

Some tasks require that you [sign in to the User Console](#log-in-to-the-pentaho-user-console) with an evaluator username and password.

### Quick tour of the Pentaho User Console

If you use file management tools or any web browser, you should feel right at home with the Pentaho User Console (PUC). To familiarize yourself with the different features and options of the User Console, take a quick tour.

{% hint style="info" %}
The features and options you see depend on your role and permissions.

See the **Pentaho Business Analytics** documentation for full details.
{% endhint %}

Jump to a section:

* [Log in](#log-in-to-the-pentaho-user-console)
* [Home](#home)
* [Opened](#opened)
  * [Use Pentaho tools](#use-pentaho-tools)
* [Browse Files](#browse-files)
* [Schedules](#schedules)
* [Administration](#administration)

#### Log in to the Pentaho User Console

Follow these steps to log in to the User Console.

1. Launch a web browser.
2. Enter the URL for the Pentaho Server.

   Your IT administrator can provide the URL.
3. On the Welcome page, enter your username and password.
4. Select **Log in**.

   You can also use **Log in as an evaluator** if enabled.

![Welcome page](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-683e2620184cc5f3f8ad2ac76d6e3ca676346f71%2FPUC_Welcome_page.png?alt=media)

#### Home

After you log in, you land on the Home perspective. Use it to start most tasks.

![Home perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-7c10750739d5f2f08a52dd26165a4c8af4a077c3%2FPUC_Home_page.png?alt=media)

| Item | Name                    | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | User menu               | Shows the name of the user currently logged in to the User Console. To log out or change your password, click the arrow next to your username.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 2    | **Home**                | <p>Indicates the Home perspective, which you can use to explore learning resources, create reports, dashboards and data sources, open recent files, view Help documentation, and access other User Console perspectives. Click <strong>Home</strong> and use the drop-down menu to navigate to the different perspectives:</p><ul><li>Home - Shows the Home perspective. See the <strong>Pentaho Business Analytics</strong> documentation for more information.</li><li><a href="#opened">Opened</a> - Shows your open files.</li><li><a href="#browse-files">Browse Files</a> - Helps you access, view, and manage the files and folders you need.</li><li><a href="#schedules">Schedules</a> - Shows your active scheduled reports, any block out times, and allows you to create, edit, and maintain report schedules.</li><li><a href="#administration">Administration</a> - Allows you to perform user setup, mail server configuration, revise Pentaho Server authentication settings, and view the available Pentaho licenses.</li></ul> |
| 3    | **Getting Started**     | <p>Shows resources to help you get familiar with Pentaho. Click the tabs in this section for videos, and report and dashboard examples.- The <strong>Welcome</strong> tab contains an introductory video about Pentaho products. Click the play icon to view the video.</p><ul><li>The <strong>Samples</strong> tab contains sample reports and dashboards that you can use to get familiar with the features and functionality of the User Console. Click <strong>Explore</strong> to view the samples.</li><li>The <strong>Tutorials</strong> tab contains tutorial videos that provide a visual tour of the User Console, reports, and dashboards. Click <strong>Watch the Video</strong> to view the tutorial.</li></ul>                                                                                                                                                                                                                                                                                                                     |
| 4    | **Browse Files**        | Opens the Browse Files perspective, where you can locate your files and folders, manage files, and schedule reports. Any file that you open appears in a new tab on the Opened perspective.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 5    | **Create New**          | Allows you to create new reports, dashboards, and data sources, if your user role has permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 6    | **Manage Data Sources** | Allows you to manage existing, and add new, data sources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 7    | **Documentation**       | Opens the [Pentaho documentation](https://docs.hitachivantara.com/) in a new window or tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 8    | **Recents**             | Shows a list of your most recently opened files. Click the star next to the file name to add it to Favorites.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 9    | **Favorites**           | Shows a list of your favorite files for quick access. To add a file for future access, use **Recents**, or select **Add to Favorites** in Browse Files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

#### Opened

The Opened perspective contains your open files. It appears after you open a file from **Recents**, **Favorites**, or the **Browse Files** perspective.

Select **Home** > **Opened**.

The icons and options you see depend on the file type you select. See the **Pentaho Business Analytics** documentation for more information.

![Opened perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-b67c339b9762cd17f2816c9af55e2d4117cdb1ff%2FPUC_Opened.png?alt=media)

**Use Pentaho tools**

Your download includes sample reports and dashboards. It also includes the Steel Wheels sample database.

* [Interactive Reports](#get-started-with-interactive-reports) helps you create operational, tabular reports.
* [Analyzer Reports](#get-started-with-analyzer-reports) helps you explore data visually with filtering and drill-down.
* [Dashboard Designer](#get-started-with-dashboard-designer) helps you combine multiple visuals into one dashboard.

#### Browse Files

The Browse Files perspective helps you organize, find, and manage files. Your files can be local, stored in the repository, or accessed through a virtual file system (VFS) connection.

Select **Home** > **Browse Files**.

You can use this view for file management and actions like sharing and scheduling. See the **Pentaho Business Analytics** documentation for more information.

![Browse Files perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-8e5cbac2ea2583eba5f11d82eb081ffde910e64a%2FPUC_Browse_Files.png?alt=media)

#### Schedules

The Schedules perspective shows your active scheduled reports.

Select **Home** > **Schedules**.

You can view recurrence patterns, last run time, next run time, and status. You can also edit schedules and create blockout times. See the **Pentaho Business Analytics** documentation for more information.

![Schedules perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d5523307297d5680b61f61567a17302dd25f03eb%2FPUC_Schedules.png?alt=media)

#### Administration

The Administration perspective is for users with the **Administer Security** permission.

Select **Home** > **Administration**.

If you do not have admin privileges, you do not see **Administration**.

Options include:

* **Users & Roles**
* **Authentication**
* **Mail Server**
* **Licenses**
* **VFS Connections**
* **Settings**
* **Email Groups**

See the **Pentaho Business Analytics** documentation for more information.

![Administration perspective](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-b75ca2af8f796898af27294875a32732ef3a5331%2FPUC_Admininstration.png?alt=media)

### Get started with Analyzer Reports

Analyzer Reports is an analytical visualization tool. It helps you filter and drill into data from Pentaho analysis data sources.

Use Analyzer when you need quick, interactive analysis. You can sort, filter, pivot, and add chart visualizations.

#### View an Analyzer report sample

This section highlights popular Analyzer capabilities. It uses the sample report **European Sales** in the **Getting Started** widget.

1. In the **Getting Started** widget on the Home page, click the **Samples** tab.
2. In the scrolling panel, scroll down and click **European Sales**, then click **Explore**.

   ![European Sales (Geo Map)](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-07ef77577a0251a4fae19fafeb532b4d5a17d576%2FssGetStartedWidgetEuroSalesGeoSample.png?alt=media)

   A new browser window opens. Click the **Samples** tab to see the report.

#### Tour the Analyzer panels

You can open an editable version of **European Sales** in Analyzer from the **Browse Files** page.

1. From the User Console Home page, click **Browse Files**.
2. In the **Browsing** pane, expand `Public`, then expand **Steel Wheels**.
3. In the center pane, double-click **European Sales**.

   ![Opened page, Analysis report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ef22b7e630bbbba31fdfe12527acfda3dcf1ee70%2FssgetstartedwidgetAnalyzerPanel.png?alt=media)

   The **Opened** page appears with the Analyzer report.
4. On the toolbar, click **Add More Fields** and **Rearrange Fields**.

   The **Available Fields** and **Layout** panels expand.

**Panel and toolbar basics**

* **Opened page**
  * Quick-access buttons for **Analysis Report**, **Interactive Report**, and **Dashboard**.
  * Tabs across the page for opened reports and files.
* **Available Fields** and **Layout**
  * Drag levels and measures into a report.
  * The canvas updates as you build the layout.
  * Remove a field by dragging it off the **Layout** panel.
* **Report canvas**
  * Dynamic view of your report as you build it.
  * Shown fields depend on the selected chart type.
* **Analyzer toolbar and filters**
  * Undo/redo, show or hide panels, and change settings.
  * Use the **Filters** panel to view, edit, and delete filters.

#### Create your first Analyzer report

These steps use the **Steel Wheels** sample data.

1. From the User Console Home page, click **Create New**, then select **Analysis Report**.
2. In **Select Data Source**, select **SteelWheels:SteelWheelsSales**, then click **OK**.

   A blank Analyzer report appears.
3. Build a basic pivot table:

   * Drag **Territory** to **Rows**.
   * Drag **Years** to **Columns**.
   * Drag **Sales** to **Measures**.

   ![Pivot table, Analysis Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5ce42c84ad63c34082d8ebe3e19dbcf68d84203d%2FssGettingStartedAnalyzerScreen1.png?alt=media)
4. Add subtotals:

   1. Drag **Line** above **Territory** in the **Layout** column.
   2. Right-click the **Line** header, then select **Show Subtotals**.

   ![Show Subtotals, Analysis Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-5bf868d737da1765ec7c73892706940806e3f513%2FssGettingStartedAnalyzerScreen2.png?alt=media)
5. Add conditional formatting:
   * Right-click the first **Sales** column.
   * Select **Conditional Formatting** > **Data Bar - Green**.
6. Add a user-defined measure:

   1. Right-click the same **Sales** column.
   2. Select **User Defined Measure** > **% of Rank, Running Sum**.
   3. Select **% of Sales**, then click **Next**.

   ![Measure field creation](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-486f8c13837fbb4521a53ac0af5f848c60fe74c2%2FssGettingStartedAnalyzerDialog1.png?alt=media)
7. Refine the measure:

   * Select **Each Line Column/Row Subtotal (Subtotal is 100%)**, then click **Done**.

   ![Measure field refinement](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e8bc66767aa22d403a919310a847a83468d0f147%2FssGettingStartedAnalyzerDialog2.png?alt=media)
8. Add a filter:

   1. Click **Show Filters** to expand the filters canvas.
   2. Drag **Territory** from **Available Fields** to the filter canvas.

   The **Filter on Territory** dialog box appears.
9. In **Filter on Territory**, select **APAC**, then click the right arrow to move it to the selected list.
10. Enable **Parameter Name**.
11. In **Parameter Name**, type `region`, then click **OK**.

![Filter on Territory dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-04c72be63f6496d0e6f2c3763e05caacefbea0f3%2FssGettingStartedAnalyzerDialog3.png?alt=media)

The report updates and shows APAC sales data. 12. Resize columns as needed for readability.

![Sales data, Analysis report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-51768e5e0849ded0c7db6276f0c0e39013dac3af%2FssGettingStartedAnalyzerScreen3.png?alt=media) 13. Save the report:

1. Click **Save As**.
2. Save the report as `Territory - Sales` in your user folder.

You have created a simple Analyzer report from scratch. For deeper Analyzer workflows, see [About Pentaho business analytics tools](#about-pentaho-business-analytics-tools).

### Get started with Interactive Reports

Interactive Reports is a web-based design interface which is used to create both simple and on-demand operational reports without depending on IT or report developers. Use Interactive Reports if you want to create a quick report that answers an immediate business question, looks professional, and provides significant control over formatting elements such as fonts, column width or sorting, background colors, and more.

Jump to:

* [View an Interactive report sample](#view-an-interactive-report-sample)
* [Tour the Interactive panels](#tour-the-interactive-panels)
* [Create your first Interactive report](#create-your-first-interactive-report)

#### View an Interactive report sample

This section highlights some popular Interactive Reports capabilities that are available, using the sample report called Vendor Sales Report, located in the **Getting Started** widget.

1. In the **Getting Started** widget on the Home page, click the **Samples** tab.

   ![Home page](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ab458750968240ded31b3ccf7b6248bc2b88f1ef%2FPIR_Tutorial_01_Tab_Samples_Select_Vendor_Sales_w596.png?alt=media)
2. Click **Vendor Sales** from the scrolling panel on the right.
3. Click **Explore** in the **Samples** pane.

   A new window opens showing the Vendor Sales sample report.

   ![Vendor Sales Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-615fa8bc29056259d23a1896904542c1233f7a0e%2FPIR_Tutorial_02_Tab_Samples_Select_Vendor_Sales_Report_Open_w555.png?alt=media)

#### Tour the Interactive panels

By going to the Browse Files page in the User Console, you can also view an editable version of the Vendor Sales report.

1. Switch to the Browse Files page in the User Console.
2. In the **Folders** pane, click to expand the **Public** folder, then click to highlight the `Steel Wheels` folder.
3. In the **Files** pane, click **Vendor Sales**, then click **Edit** in **File Actions**.

   The Opened page appears with the interactive report and toolbars active.

   ![Opened page](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-98ca399a4612e36559ce7bbfe92943020bd50689%2FPIR_Tutorial_03_Vendor_Sales_Edit_Report_Hitachi_Red_Numbers_w555.png?alt=media)

Key areas on the page:

1. **Opened page**\
   Provides quick access buttons across the top to create and save a new **Analysis Report**, **Interactive Report**, and **Dashboard**. Opened reports and files show as a series of tabs across the page.
2. **Data**, **Formatting**, and **General** panels\
   Use the **Data** panel to drag information into a column or a row on the report. Your report updates as you drag items onto the report canvas. Use **Find** to search for a specific field. Delete a field by dragging it from the layout area to the trash can that appears in the lower right corner of the report canvas.

   Use the **Formatting** panel to change font size and type.

   Use the **General** panel to set preferences, select a paper size for printing, and select templates for your report.
3. **Report canvas**\
   Shows a dynamic view of your report as you build it. The look of your report changes as you use the **Data**, **Formatting**, and **General** panels.
4. **Interactive toolbar and filters**\
   Use the toolbar to undo and redo actions, hide lists of fields, add or hide filters, disable auto-refresh, adjust settings, change the report view, and limit the number of rows queried. Use the **Filters** panel to view, edit, and delete filters for the active report.

#### Create your first Interactive report

The instructions below guide you through the creation of your first Interactive report using the Steel Wheels sample data.

1. From the Home page, click **Create New**, then choose **Interactive Report**.

   ![Home page, Interactive Report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0b7c1024cca2129b33ab85e42d2f96d3ed406115%2FPIR_Tutorial_04_Home_Create_Interactive_Report_w565.png?alt=media)
2. Choose the **Inventory** data source from the **Select Data Source** dialog box. Click **OK**.

   ![Select Data Source dialog box](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-652cb3b7a25e5c2ced683f20ec52958af35d2007%2FPIR_Tutorial_05_Select_Data_Source_w365.png?alt=media)
3. Click **Get Started** on the dialog box that appears.

   A blank Interactive report canvas appears.
4. Click and drag the **Product Code** element onto the report canvas until a highlighted vertical line appears. Drop it onto the report canvas.

   ![Click and drag item to canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-6a89473abc32594fd7f05cd584102c7abe5884eb%2FPIR_Tutorial_06_Drag_Product_Code_w555.png?alt=media)
5. Continue dragging and dropping these fields onto the canvas: **Product Name**, **Product Vendor**, **Quantity in Stock**, **MSRP**, and **Buy Price**.

   ![Report fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1091d498d0201ca83747dd6634050eff2eefd36f%2FPIR_Tutorial_07_Drag_Fields_Canvas_w562.png?alt=media)

   The data from the chosen fields appears on the report canvas and populates with the information from the server.

   **Note:** You can change the order of the columns by clicking the column headings and dragging them left or right. If you want to delete a column, drag the column title to the trash can.
6. Rename your report by double-clicking **Untitled** in the report canvas and typing a name in the field that appears. `In Stock Report` is used in this example.

   ![Renaming the report](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-4889d0928f75fd5ee1613cd40d80370864c521f6%2FPIR_Tutorial_08_Rename_report_w311.png?alt=media)
7. After you have arranged your columns, apply a filter to the data. Click the **Filter** icon in the toolbar. After the **Filter** pane expands, drag the **Product Code** field onto the filter workspace.

   ![Applying a filter](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-0938602e32f96ffae23eb2eea1c01885f9348341%2FPIR_Tutorial_09_Drag_Product_Code_into_Filters_w580.png?alt=media)
8. In the **Filter on** dialog box, click **Select from a list**.

   ![Selecting filter values](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-3c7b00925b4b63eb8e10db061d706973524ea915%2FPIR_Tutorial_10_Filter_on_Product_Code_Dialog_w530.png?alt=media)
9. Choose items from the filter list using one of these methods. Click the arrows to move your selected filters on or off the filter list.
   * To choose more than one item, hold down Ctrl and click the items. Then click the top arrow to move them to the right panel.
   * To choose a range, hold down Shift. Then click the first and last item.
   * To choose a single item, click it. Then click the top arrow to move it to the right panel.
10. Click **OK**, then click **Save As** on the toolbar.
    1. In the **Save As** dialog box, save your report using the title you used in Step 6. `In Stock Report` is used in this example.
    2. Choose your user folder as the location. Remember the folder and report title. You use the report in a later tutorial. Click **Save**.
11. If you want to export the report, click the **Export** icon on the toolbar and choose a format from the dropdown list.

    ![Report export selection](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-8fcfbded60db6626a176bfc66add5afcd0c983da%2FPIR_Tutorial_11_Export_w580.png?alt=media)

    The report exports in the selected format. You can print a paper copy from the export.

    ![Exported report example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2d8796e0967273cd4e028405a3b884341bd623d2%2FPIR_Tutorial_12_HTML_Report_w550.png?alt=media)

You have successfully created a simple Interactive report from scratch. See **Pentaho Business Analytics** for details on how to work with more complex interactive reports.

### Get started with Pentaho Reporting tools

After you define the data sources for your Pentaho Server, you are ready to begin working with the Pentaho User Console to create your first reports. Each section below uses sample data sources that are included with the installation.

Use these sections in order:

* [Quick tour of the Pentaho User Console](#quick-tour-of-the-pentaho-user-console)
* [Get started with Interactive Reports](#get-started-with-interactive-reports)
* [Get started with Analyzer Reports](#get-started-with-analyzer-reports)
* [Get started with Dashboard Designer](#get-started-with-dashboard-designer)
* [Next steps](#next-steps)

### Get started with Dashboard Designer

Dashboard Designer lets you build dashboards with minimal training. A dashboard combines several reports in one view. Use it to monitor multiple reports at once, keep quick links to pages you use often, and view charts while you work.

In this topic:

* [View a dashboard sample](#view-a-dashboard-sample)
* [Tour the Dashboard panels](#tour-the-dashboard-panels)
* [Create your first dashboard](#create-your-first-dashboard)

#### View a dashboard sample

This section highlights popular Dashboard Designer capabilities, using the sample dashboard **Sales Performance (Dashboard)** in the **Getting Started** widget.

1. In the **Getting Started** widget on the Home page, click the **Samples** tab.
2. Scroll down to **Sales Performance (Dashboard)**.
3. Click **Explore** to open a new browser window, then click the **Samples** tab.
4. Scroll right in the horizontal list at the bottom.
5. Click **Sales Performance (Dashboard)**.

![Dashboard sample](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-ba47b1cc29009b8b0cb345d53cda2eaa2b699065%2FssDashboardSampleNew.png?alt=media)

#### Tour the Dashboard panels

You can open the editable version of **Sales Performance (Dashboard)** in Dashboard Designer from **Browse Files**.

1. In the **Folders** pane, expand `Public`, then select `Steel Wheels`.
2. In the center pane, double-click **Sales Performance (Dashboard)**.
3. After the dashboard opens, in **File Actions**, click **Edit**.

![Dashboard example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-f0a3aee1fe810d298093853260cbc3d7e9f7d8d5%2FssDashboardSampleEditPanels.png?alt=media)

| Item | Name                           | Function                                                                                                                                                                                                           |
| ---- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | **Opened** page                | Provides quick access buttons across the top to create and save a new **Analysis Report**, **Interactive Report**, and **Dashboard**. Opened reports and files show as a series of tabs across the page.           |
| 2    | Prompts panel                  | The prompts panel gives you a way to add filters to the individual parts of your dashboard.                                                                                                                        |
| 3    | **Browse** and **Files** panel | Locate your files using the **Browse** and **Files** panels, and add them to dashboards.                                                                                                                           |
| 4    | Dashboard canvas               | Shows a dynamic view of your dashboard as you work to build it. The look of your dashboard refreshes as you add content from the **Browse** and **Files** panels, and work with the prompts or **Objects** panels. |
| 5    | **Objects** panel              | Refine the look of your dashboard with the **Objects** panel by choosing a dashboard template or changing the titles for each object in the dashboard.                                                             |

#### Create your first dashboard

1. From the User Console Home page, click **Create New**, then select **Dashboard**.
2. In the **Edit** pane, click the **Templates** tab, then select **2 over 1**.
3. In the **Edit** pane, click the **Properties** tab, then enter `My Dashboard` in **Page Title**.

   This is the title for your dashboard page.

   ![Properties tab, Dashboard](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-37cfc658332b92fa18006128f8aeb523e5c211bc%2FssGettingStartedDashboardScreen1.png?alt=media)
4. Click the **Themes** tab, then select a theme.

   The new theme applies immediately.
5. In the **Browse** pane, open the folder you used earlier.
6. From the **Files** pane, drag `Territory - Sales` onto the top-left dashboard panel.

   ![Drag and drop into dashboard](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c12e21c7d9d29c94cf7046af44efcb76a4e0741f%2FssGettingStartedDashboardScreen2.png?alt=media)
7. In the **Edit** pane, enter `Territory - Sales` in **Title**, then click **Apply**.

   The panel populates with the **Territory - Sales** report.
8. Locate your Interactive report in the **Browse** pane.
9. Drag `In Stock Report` onto the top-right dashboard panel.
10. In the **Edit** pane, enter `In Stock Report` in **Title**, then click **Apply**.

    The panel populates with the **In Stock Report**.
11. Drag any report from `Public/Steel Wheels` into the bottom dashboard panel.
12. Enter a title for the bottom panel, then click **Apply**.
13. In the toolbar, click **Save As**.
14. Save the dashboard as `My Dashboard`, then click **Save**.
15. Close the dashboard (click **X** on its tab).
16. Go to **Browse Files**, then double-click `My Dashboard` in the **Files** pane.

![Created dashboard](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-810f8c294ed3edc061304288a2919e1c57977a1d%2FssGettingStartedDashboardScreen3.png?alt=media)

You created a simple dashboard. See **Pentaho Business Analytics** for details on complex dashboards.

### Next steps

After you have finished working through the walk-through tutorials, you are ready to learn more about Pentaho reporting with the following documents:

* **Pentaho Business Analytics**
* **Pentaho Report Designer**
