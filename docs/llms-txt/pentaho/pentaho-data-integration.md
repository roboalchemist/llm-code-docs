# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/pentaho-data-integration.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/pentaho-data-integration.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/pentaho-data-integration.md

# Pentaho Data Integration

Pentaho Data Integration (Kettle) `.KTR` files can act as a data source, but you must copy all the JAR files from `pentaho/design-tools/data-integration/lib/` and all of its subdirectories except the JDBC subdirectory to `pentaho/design-tools/report-designer/lib/`.

Use the Pentaho Data Integration data source option if you want to create a report that contains data from any step in a Data Integration transformation. This is particularly useful if you want to create a report that includes data from transformation steps such as Splunk Input or Splunk Output. You must have a report file open in order to proceed, and your data source must be accessible before you can connect to it in Report Designer. As mentioned previously in this section, the first time you create a Kettle data source you must also copy all the JAR files from `pentaho/design-tools/data-integration/lib/` and all its subdirectories except the `JDBC` subdirectory to `pentaho/design-tools/report-designer/lib/` in order to access it through Report Designer.

**Note:** Your data source must not contain multi-select parameters. Data Integration does not accept array parameters; only strings are accepted.

Follow this procedure to add a Pentaho Data Integration (Kettle) data source in Report Designer.

1. Select the **Data** tab in the upper right pane.

   By default, Report Designer starts in the **Structure** tab, which shares a pane with **Data**.
2. Click the yellow cylinder icon in the upper left part of the **Data** pane, or right-click **Data Sets**.

   A drop-down menu with a list of supported data source types will appear.
3. Select **Pentaho Data Integration** from the drop-down menu.

   The Kettle Datasource window will appear.
4. Click the round green **+** icon to add a new query.
5. Type a concise yet sufficiently descriptive name into the **Name** field.
6. Click **Browse** and navigate to your Pentaho Data Integration `KTR` file.
7. Review the imported steps and modify their parameters accordingly, then click **OK**.
   * **OLAP**

     Report Designer only supports Pentaho Analysis (Mondrian) OLAP sources at this time.

     * **Pentaho Analysis**

       A Mondrian schema file.
     * **Pentaho Analysis Denormalized**

       A Mondrian schema file, denormalized.
     * **Pentaho Analysis Legacy**

       A Mondrian data source imported from a report created with a version of Report Designer older than 3.5.0.
   * **XML**

     An XQuery file.
   * **Table**

     Create your own data table by entering information manually, or importing it from an Excel spreadsheet file (XLS).
   * [**MongoDB**](http://www.mongodb.org/)

     Use data stored in this document-oriented NoSQL database.
   * **Advanced**

     The data sources in this category are typically for software developers and special-use cases.

     * **JDBC (Custom)**

       Allows designers to dynamically create a query from a formula or function.
     * **Scriptable**

       Allows designers to generate a data set via JavaScript, Bean Shell, Groovy, Netrexx, XSLT, JACL, or Jython.
     * **External**

       Used only if the report is going to run on the Pentaho Server, which means the data is retrieved via a component in an action sequence. The query name for the report must be mapped to the result set in the `.xaction` file.
