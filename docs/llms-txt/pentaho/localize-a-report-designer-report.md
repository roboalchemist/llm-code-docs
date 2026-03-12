# Source: https://docs.pentaho.com/pba-report-designer/localize-a-report-designer-report.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/localize-a-report-designer-report.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/localize-a-report-designer-report.md

# Localize a report

Report Designer can dynamically pull text content from message bundles that contain localized strings. This enables you to localize the static and dynamic text content in a report. The relevant report elements you must work with to dynamically localize a report are: Resource Message, Resource Label, and Resource Field. You'll use these in place of standard report text elements.

For instructions on localizing a report, review the following sections:

* [Prepare a report for localization](#prepare-a-report-for-localization)
* [Use externalized message bundles](#use-externalized-message-bundles)

## Prepare a report for localization

Follow the below procedure to prepare a report for localization.

1. Open the report you want to localize.
2. Go to the **File** menu and select **Resources**.

   The Resource Editor window will appear.
3. Click **Create** to create a new default resource bundle.

   A resource details window will appear.
4. Type in a file name for your resource file (using a `.properties` extension), and select its content type from the drop-down list.

   You should name this properties file without any country or language codes. Pentaho Reporting will default to a non-localized message bundle name if no locale is specified, so the first message bundle you create should be the one you want to use by default. Typically you would use the report name for the resource bundle name. So for an `InventoryList.prpt` report, you would name your resource bundle `InventoryList.properties`.
5. In the Resource Editor, select the message bundle you just created, then click **Edit**.

   A text window will appear.
6. Enter name/value pairs for all of the **Resource Labels** you intend to create, with the name of the label on the left and the value on the right, as shown in the example below.

   ```
   title=Sales Report 2011
   companyLabel=Steel Wheels, Inc.
   ```
7. Repeat the previous four steps for every locale and language you want to account for, using the appropriate language and country codes in the file names.

   Following the example above, the traditional French version of the properties file would be`InventoryList_fr_FR.properties`.

   Refer to the **Customizing Pentaho Business Analytics** document for more details on message bundle naming conventions.
8. Add a **Resource Label**, **Message**, or **Field** to the report canvas.
9. With the new element selected, go to the **Attributes** pane.
10. Set the name of this replaceable resource in the value field.

    This must match the name that you specified in your message bundle earlier.

    To follow the example above, your resource labels should be named `title` and `companyLabel`.
11. Set the name of the resource bundle that will contain this replaceable resource in the resource-id field.

    This should not have a .properties extension.

    Following the example above, this would be `InventoryList`.

Your report will be localized according to your specifications. You can test this by changing the language code for Report Designer through the `.environment.designtime.Locale` variable in the Configuration dialog box in the **File** menu.

## Use externalized message bundles

You can localize a Pentaho Report and keep the property files external. This enables you to share property files among multiple PRPT reports, which minimizes the files you need to maintain. To use external message bundles (`.properties` files), define the key/value pairs, but place the bundles on the classpath for the report engine to find.

If you are in Pentaho Report Designer, add the files to the `*\[PRD Install\]*/resources` directory. For them to be recognized in the Pentaho Webapp, put the files in the `pentaho/WEB-INF/classes` directory.
