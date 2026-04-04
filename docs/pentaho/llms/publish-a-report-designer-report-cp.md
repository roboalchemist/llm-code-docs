# Source: https://docs.pentaho.com/pba-report-designer/publish-a-report-designer-report-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/publish-a-report-designer-report-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/publish-a-report-designer-report-cp.md

# Publish a report

For instructions on publishing a report, see the following sections:

* Publish to the Pentaho Server
* Edit Interactive Reports
* Hide reports
* Link reports
* Link in tabs

**Note:** The Pentaho Server must be accessible from the machine where you are using Report Designer.

## Publish to the Pentaho Server

You can publish a report to a variety of different outputs using the Report Designer **Preview As** and **Export** functions in the **File** menu.

**Note:** Starting with Report Designer v10.2, Microsoft Excel XLSX is the only supported worksheet format.

If you have a Pentaho Server in production, you can publish directly to it instead. Additionally, you can link two reports together so that they share selected resources.

If your administrator has enabled row-level security and the report you are publishing includes data from restricted data sources, make sure you have permission to run the selected report.

1. Open the report you want to publish.
2. Click **File** > **Publish**.

   The Login window appears.
3. Enter your Pentaho Server connection information, then click **OK**.

   Contact your system administrator or IT manager if you have questions.

Report Designer connects to the Pentaho Server and publishes the report. If you have the necessary permissions, and the configuration and connection information is correct, the operation is successful. Otherwise, an error message containing information about the issue appears.

## Edit Interactive Reports

You can use Report Designer to edit a report created with Pentaho Interactive Reports.

This procedure assumes that you have a `.prpti` report created with Pentaho Interactive Reports

**Note:** Note: Once a `.prpti` file has been edited with Report Designer, it can no longer be used with Interactive Reports.

Perform the following steps to edit an Interactive Report:

1. Copy the `.prpti` file from the solution in the Pentaho Server's `pentaho-solutions/` directory to the workstation that has Report Designer.

   If you have the Pentaho Server and Report Designer on the same machine, this step may not be necessary. However, you may need to create a copy of the `.prpti` file if you want to continue using the original in Interactive Reports.
2. Copy the `.xmi` data source file from the solution in the Pentaho Server's `pentaho-solutions/` directory to the workstation that has Report Designer.
3. Start Report Designer and open the `.prpti` file.
4. Edit the report's data source definition and replace the URL to the XMI file with the one you copied from the Pentaho Server.

   Report Designer is unable to connect to XMI files on remote Pentaho Server machines. If you have the Pentaho Server on the same system with Report Designer, you can continue using that XMI file, but you still have to provide the local file system location in place of the server's URL.
5. Establish a data source connection to the database referenced in the XMI file.

   The XMI file defines a metadata model, which can be used as a data source so long as the database it provides metadata for is available to Report Designer.
6. Copy the appropriate JDBC driver for the XMI database connection to the `report-designer/lib/jdbc/` directory.

   You may already have an appropriate database driver; if so, skip this step.

You have successfully migrated an Interactive Report to Report Designer. From here, you can render and distribute or publish it. If you publish this file to the Pentaho Server, it will be treated as a Report Designer `.prpt` report, not as an Interactive Reports `.prpti` report.

## Hide reports

Use this feature in instances in which you want to prevent users from viewing an unfinished report in the Pentaho User Console, but want to ensure that the report publishes successfully. You can also use this feature to make the report exclusively accessible from another report through linking.

You must have a report file open in order to proceed.

Perform the following steps to hide a report:

1. Go to the **Structure** pane and select **Master Report**.
2. Under **Attributes**, scroll down to the visible attribute.
3. Right-click the **visible** attribute and choose **False**.
4. Save and publish your report.

The report, even though published successfully, does not display in the Pentaho User Console. You can edit the report, as needed, in Report Designer.

## Link reports

Just as you can create a hyperlink to a Web address, you can also create a hyperlink from one report to another, as long as the report you're linking to is published on the Pentaho Server.

Perform the following steps to link to a published report.

1. Log into the Pentaho User Console.
2. Run the report you want to link to.
3. When the report is generated, copy its URL from your browser's address bar.
4. Start Report Designer and open the report you want to link from.
5. Follow the process of adding a hyperlink as explained in [Create a Link to a Report on a Chart](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/broken-reference), using the URL you copied from the **User Console as the Hyperlink-Target** value.
6. Save and publish the report as you normally would.

The published report will now link to the report URL you copied at the beginning of this procedure when viewed through the Pentaho User Console.

## Link in tabs

You must define the parameters described in the table below to open a link to a report, Analyzer report, or action sequence in a **Pentaho User Console** tab.

* **::TabActive**

  Defaults to FALSE.

  When set to `TRUE`, this parameter opens the target report in the Pentaho User Console report tab.
* **::TabName**

  Allows you to assign a name to the report tab either using static text, data field, parameter or a function.

For `.prpt` reports, the **TabActive** and **TabName** parameters can be found under **System Parameters**. You must define other file types under **Custom**.
