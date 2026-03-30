# Source: https://docs.pentaho.com/pba-report-designer/get-started-with-the-report-designer.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/get-started-with-the-report-designer.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/get-started-with-the-report-designer.md

# Get started with the Report Designer

How you start Report Designer depends on which platform you are using Windows, Linux, or OS X.

* **On Windows**

  If you used the Pentaho Business Analytics installer available to you through your subscription, you will have a Start menu category for all of your Pentaho applications. To run Report Designer, click the **Report Designer** item in the `Pentaho` Business Analytics subdirectory in the `Pentaho` application folder. Alternatively, you can run the `pentaho\design-tools\report-designer\report-designer.exe` from Windows Explorer or the command prompt.
* **On Linux**

  The Business Analytics installer does not create program entries in the **K** menu or **Applications** menu in Linux desktop environments, so you will have to start Report Designer by navigating to the `pentaho/design-tools/report-designer/` directory and running the `report-designer.sh` script. You can do this from your file manager, or from a terminal window.
* **On OS X**

  The Mac installation procedure does not create program entries in the dock, so you will have to start Report Designer by opening your `Applications` folder, then the `report-designer` sub-folder, then running `report-designer.app`.

### Configuration files

Upon first launch, Report Designer creates a `.pentaho` directory in the current user's home directory, and populates it with the configuration subdirectories and files. For more information about configuration files, see the topic, [Report Designer configuration files](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/report-designer-configuration-files).

### Tour the interface​

To learn how to navigate the user interface before moving on to more complex tasks, see the topic, [Tour the Report Designer interface](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/tour-the-report-designer-interface-cp).&#x20;

## Create a report

To create a report in Report Designer, follow this process.

1. [Connect to a data source](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp) (usually a database, yet you can also pull data from a flat file).&#x20;
2. [Create queries](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp) to get your data.
3. [Add report elements](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-report-elements-in-report-designer-cp) and arrange data elements in the Report Designer workspace.&#x20;
4. [Apply formatting to report elements](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/apply-formatting-to-report-elements-in-report-designer-cp).&#x20;
5. [Add a chart](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-a-chart).
6. [Perform calculations ](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/perform-calculations-in-report-designer-cp)by creating formulas or calculating fields using data retrieved from your query.
7. [Publish a report](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/publish-a-report-designer-report-cp), either to the Pentaho Server, or locally as a PDF or other supported file format.

Your report will consist mostly of data retrieved from a database query that you will create through Report Design Wizard, SQL Query Designer, MQL Query Builder, or by hand. Once you have a dataset, you are able to further constrain it to show specific details, and then move on to report layout and design.

## Advanced topics

The following topics help to extend your knowledge of Report Designer beyond basic setup and use:

* [Output parameterization](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp)

  Maintain one report with output parameters so the person viewing the report can change its data structure or values.
* [Localize a report](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/localize-a-report-designer-report)

  Pull text content from message bundles that contain localized strings.
* [Create Report Design Wizard templates](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-report-design-wizard-templates-cp)

  Creating templates for the Report Design Wizard and Interactive Reports.

## Troubleshooting

See our list of common problems and resolutions in the topic, [Report Designer and Reporting engine issues](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/report-designer-and-reporting-engine-issues-cp).
