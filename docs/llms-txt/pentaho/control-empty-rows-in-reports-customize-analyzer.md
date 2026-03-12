# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/control-empty-rows-in-reports-customize-analyzer.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/control-empty-rows-in-reports-customize-analyzer.md

# Control empty rows in reports

As an administrator, you can enable or disable the **Show empty rows** property at the Pentaho Server level. You can use this property to prevent a cross-join that is resource-intensive on the server. The values for the **Show empty rows** property are:

* **enable**

  All users have access (default).
* **Disable**

  No users have access.
* **adminOnly**

  Only admin users have access.

To control the report option, perform the following steps:

1. Navigate to the `pentaho-server/pentaho-solutions/system/analyzer/` directory and open the `analyzer.properties` file with any text editor.
2. Set the report options **showEmpty** property to **enable**.

   The **Show rows or columns with** drop-down menu displays in the **Report Options**dialog box, as shown in the following example:

   ![Analyzer Report Options dialog box](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-2004d2e0ef46e2f48d6d5d44d4b4bf8e5df29f2a%2FPDI%20Analyzer%20Report%20Options%20dialog%20box.png?alt=media)
3. Choose one of the following options:
   * **Measure Data.**
   * **Measure and Calculated Measure data**
   * **Show all even blank measures**
4. Restart the Pentaho Server.
