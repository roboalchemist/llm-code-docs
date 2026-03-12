# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/properties-file.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/properties-file.md

# Properties file

Giving Analyzer reports a configuration that fits your needs involves editing the `analyzer.properties` file. The following actions are examples some of the settings you can change:

* Enabling your logo to appear in PDF output.
* Specifying the placement of totals for columns and rows.
* Specifying the maximum number of rows when drilling-down in a report.
* Defining a specific value for blank cells.
* Changing the default chart options.

The complete list of properties that you can change are in the file comments, and you can find the file here: `server/pentaho-server/pentaho-solutions/system/analyzer/analyzer.properties`.

You can test your customizations to `analyzer.properties` in real time by refreshing the cache for the Analyzer report you are modifying using the **More actions and options** > **Administration** > **Clear Cache** menu action.

## Setting the default placement of column and row totals

Typically in Analyzer reports, the column totals are at the bottom and row totals are on the right. This is the default setting, but users can change it in Analyzer with the **Report Options** dialogue box by selecting **Totals on top/left**. If you prefer the default to be column totals at the top and row totals on the left, set the **report.options.totalsOnTopLeft** parameter to `true` in the `analyzer.properties` file.

## Collapse business group folders in the Available Fields list

By default, all the business group folders in the **Available Fields** list are expanded. You can change this setting to a collapsed view by editing the `analyzer.properties` file.

1. Stop the Pentaho Server.
2. Navigate to the `analyzer.properties` file, located at: `server/pentaho-server/pentaho-solutions/system/analyzer/analyzer.properties`.
3. Open the file with any text editor and locate the following lines in the file:

   ```
   # On opening the field list, collapse the business groups/folder
   # by default. Default: false
   Report.field.list.collapse=false
   ```
4. Change the **Report.field.list.collapse** value to `true` as follows:

   ```
   # On opening the field list, collapse the business groups/folder
   # by default. Default: false
   Report.field.list.collapse=true
   ```
5. Save and close the `analyzer.properties` file.
6. Restart the Pentaho Server.
7. Restart Analyzer.

   ![Collapsed business group folders in the Available Fields list](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-83398806f261b376f6df9a331dce46bb0256f264%2FAnalyzer_Business-Groups_Collapsed.png?alt=media)

   The list of available business group folders is collapsed, as shown in the example above.

See the **Install Pentaho Data Integration and Analytics** document for instructions on starting and stopping the Pentaho Server.

## Sort options in the Available Fields list

The **Available fields** list in Analyzer can be sorted using the **View** toggle with the following sorting options:

| UI Label                   | Description                                                           | Sort Option       |
| -------------------------- | --------------------------------------------------------------------- | ----------------- |
| **By Category**            | Sorts by folder names.                                                | `cmdViewCategory` |
| **Measure - Level - Time** | Sorts by the type of field.                                           | `cmdViewType`     |
| **A > Z**                  | Sorts by field names without any folders.                             | `cmdViewName`     |
| **Schema**                 | Sorts in the same order thant is defined in the Mondrian schema file. | `cmdViewSchema`   |

### Default sort option priorities

The default sort used in an Analyzer report is based on the following priority:

1. A sort specified in an URL takes the highest priority.
2. The last sort option is automatically remembered when a report is reopened.
3. Next comes the annotation value specified on the report's cube in the Mondrian schema file.
4. A system wide setting in `analyzer.properties` file.
5. Last, the default value of **cmdViewCategory**.

### Specify with an URL

The sort option can be set in the URL by adding a **fieldListView** query parameter at the end of the URL. For example, you can do something like this in a codeblock in HTML or XML.

```
http://localhost:8080/pentaho/api/repos/xanalyzer/editor?&amp;showFieldList=true&amp;showFieldLayout=true&amp;catalog=SampleData&amp;cube=Quadrant%20Analysis&amp;autoRefresh=true&amp;debug=true&amp;
```

### Specify with annotation

To specify the sort option using an annotation, add a Cube-level annotation called **AnalyzerFieldListView** in your Mondrian schema file. This annotation must be the first child element under a cube as shown here.

```
<Cube name="Quadrant Analysis">
    <Annotations>
              <Annotation name="AnalyzerFieldListView">cmdViewName</Annotation>
    </Annotations>
    <Table name="Quadrant_Acuals" />
    <DimensionUsage name="Region" source="Region" />
    <DimensionUsage name="Department" source="Department" />
    <DimensionUsage name="Positions" source="Positions" />
```

### Specify through the properties file

This sort option is specified by setting the `cmdViewType` for the **report.field.list.view** property.

```
# Default field list view mode used to sort the available field
# list in the editor.  Possible values include: cmdViewCategory,
# cmdViewType, cmdViewSchema and cmdViewName
# This can also be overriden on a cube level with the annotation
# AnalyzerFieldListView
report.field.list.view=cmdViewType
```

## Specify CSV separator for Analyzer reports

Specify the CSV separator used in Analyzer reports that are exported as CSV output.

Complete the following steps to specify the CSV separator.

1. Stop the Pentaho Server.

   For instructions on stopping and starting the Pentaho Server, see the **Install Pentaho Data Integration and Analytics** document.
2. Navigate to the `analyzer.properties` file, located at: `server/pentaho-server/pentaho-solutions/system/analyzer/analyzer.properties`.
3. Open the `analyzer.properties` file with a text editor and locate the following line:

   `report.output.csv.separator`
4. Change the **report.output.csv.separator** property value to the value that you want to use as a CSV separator.

   For example, to use a colon (:) as the CSV separator, update the property value to match the following example:

   `report.output.csv.separator = :`

   The default CSV separator value is a comma (,).
5. Save and close the `analyzer.properties` file.
6. Restart the Pentaho Server.
7. Restart Analyzer.
