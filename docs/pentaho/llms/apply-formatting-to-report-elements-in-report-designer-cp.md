# Source: https://docs.pentaho.com/pba-report-designer/apply-formatting-to-report-elements-in-report-designer-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/apply-formatting-to-report-elements-in-report-designer-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/apply-formatting-to-report-elements-in-report-designer-cp.md

# Apply formatting to report elements

Once you have your elements in place, all elements can be modified through the **Style** panel. All text-based elements such as text, message, number, date fields, and labels can be modified through the toolbar just above the report canvas. These text controls also work for non-textual elements, but the settings will only affect how the element's label appears in the layout bands. You can also perform more advanced formatting, such as hyperlinking, pasting, morphing, and row banding.

For instructions on applying formatting to report elements, see the following sections:

* [Create hyperlinks](#create-hyperlinks)
* [Paste formatting](#paste-formatting)
* [Morph an element](#morph-an-element)
* [Implement row banding](#implement-row-banding)

## Create hyperlinks

Hyperlinks can be created to go to a report on a chart or link directly from a visualization.

* [Create hyperlinks to go to a report on a chart](#create-hyperlinks-to-go-to-a-report-on-a-chart)
* [Create hyperlinks to link from a visualization](#create-hyperlinks-to-link-from-a-visualization)

### Create hyperlinks to go to a report on a chart

You can create a chart within Report Designer that links to other reports or URLs. This action is known as creating a hyperlink or a drill-down on a link.

Perform the following steps to create a hyperlink to a report:

1. Within the report, double-click on the chart to place a hyperlink.

   The Edit Chart window appears.
2. Within the Edit Chart dialog box, scroll down to the **Values** section on the left panel. Select url-formula and a **...** appears. Click on the **...** to show the Formula Editor.
3. Within the Formula Editor dialog box, select the last button on the right. This is the **Drill-down Function** button, which looks like a chain link.

   `DRILLDOWN` appears in the **Formula** box.
4. In the top of the **Formula Editor** display, click on the drop-down box to select the **Location** type.
5. Choose **Pentaho Repository** if the link opens a report from the repository. Enter the URL to the Pentaho Server in the **Server URL** field.

   For example,

   ```
   http://<myPentahoServer>:<PortNumber>/<FileName>
   ```

   Use the **Path** field to browse to the desired linking report
6. Choose **URL** if the link goes to a defined URL. Enter the URL for the link in the **Path** field.

   For example,

   ```
   http://www.*&lt;ApplicationName&gt;*/search?
   ```

   If the URL requires parameters, you can define them in the **Parameters** section. Click the **Add parameter** button to add an entry for the parameter name and value. They must be defined as formulas.

   For example, `myRegion = East` or `myLine = Trains`. You can also use any data columns or functions in the formula. For this example, the URL generated is `http://www.myApplication.com/search?...&myLine=Trains`.
7. Choose **Self** if the link goes to a custom web application and refers back to itself as a link.

   Set the list of parameters that your web application passes back into the report. The parameter values need to be defined as a formula. You can also add any additional parameters and values that your custom web application requires. You may find it necessary to use the internal chart fields here.
8. Within the Formula Editor display, view the **Parameters** applied to the report to ensure they are correct.

   This display contains the following tabs:

   * The **Report Parameters** tab displays the parameters used in the targeted report. This tab shows all the parameters defined in the target report that can be mapped to the current report.
   * The **System Parameters** tab allows report designer to optionally control the behavior of the Report Viewer. The initial list provided is a pre-defined list of the most popular parameters. For example, **TabActive** (when set to **true**, allows the target report to open in a new tab) and **TabName** (when **TabActive** is to **true**, allows the tab name to be dynamically named using a formula) are frequently used as **TabActive** true and `TabName = "[::chart-series-key]"`. The defined list of parameters can be found in the Report Viewer Plugin wiki.
   * The **Custom Parameters** tab adds additional parameters to the report unique to a specific use case. In rare cases, this would be a situation where the Report Viewer has been extended to accept additional parameters.
9. Depending on location type, a **DRILLDOWN** function is generated in the Formula section.

   For example, for a local report called **oStatus** that you want to link to `Order Status.prpt`, you would enter:

   ```
   =DRILLDOWN("local-prpt"; NA();
   {"oStatus"; ["chart::category-key"] | "showParameters"; [STATUS] |
      "solution"; "steel-wheels" | "path"; "reports" | "name"; 
      "OrderStatus.prpt"})
   ```
10. Run the report in your desired format. Click the green arrow and select the desired output type from the drop-down menu.

    The final product appears.
11. Double-click on the appropriate area within the chart to launch the link.

    The new report appears in the browser.

The report is linked to another report using a hyperlink. This is also known as a drill-down link on a report.

### Create hyperlinks to link from a visualization

You can also add hyperlinks to charts with Pentaho Report Designer.

A chart can link to the three following location types;

| Location Type      | Description                                                                                                       | Generated Link Example                                                                                                                                                |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pentaho Repository | Creates a context link on the Pentaho server                                                                      | `http://localhost:8080/pentaho//conte...ditor?command= open&solution=steel-wheels&path=analysis &action=Product%20Line%20Sales% 20Trend.xanayzer&line=Classic%20Cars` |
| URL                | Creates a link that goes to a defined URL                                                                         | `http://www.myApplication.com/search?...&myLine=Trains`                                                                                                               |
| Self               | Creates a link to a custom-built web application and refers back to itself as a link. This option is rarely used. | N/A                                                                                                                                                                   |

The following link locations depend on their chart type:

| Chart Type       | Location of Link |
| ---------------- | ---------------- |
| Bar              | Bars             |
| Area and line    | Markers          |
| Pie and doughnut | Slices           |
| Bubble           | Bubbles          |

In the chart editor, you have several **Chart Field** options. Depending on the chart type, there are various internal chart fields that can be used by the link and are only available when used within the **Edit Chart** dialogue box. Go to **Formula Editor** > **Toolbar** to see the following options:

| Chart Field          | Descriptions                                    | Chart Type         |
| -------------------- | ----------------------------------------------- | ------------------ |
| chart:series-key     | Returns the series name                         | Bar, line and area |
| chart:series-keys    | Returns all the series name                     | Bar, line and area |
| chart:series-index   | Returns the series index number starting at 0   | Bar, line and area |
| chart:category-key   | Returns the category name                       | Bar, line and area |
| chart:category-keys  | Returns all category names                      | Bar, line and area |
| chart:category-index | Returns the category index number starting at 0 | Bar, line and area |
| chart:value          | Returns the numeric value                       | Bar, line and area |
| chart:key            | Returns the slice name                          | Pie and doughnut   |
| chart:keys           | Returns all the slice names                     | Pie and doughnut   |
| chart:item           | Returns the category name                       | Pie and doughnut   |
| chart:items          | Returns all category names                      | Pie and Doughnut   |
| chart:pie-index      | Returns the category index number starting at 0 | Pie and Doughnut   |
| chart:x-value        | Returns the value of x                          | Scatter and XY     |
| chart:y-value        | Returns the value of y                          | Scatter and XY     |
| chart:z-value        | Returns the value of z                          | Scatter and XY     |

## Paste formatting

Report Designer has the ability to copy the formatting properties of a certain element and apply them to other elements.

Follow this procedure to paste formatting:

1. Click on the element you want to copy formatting properties from.
2. Copy the element to the clipboard by either pressing CtrlC, or by right-clicking the element and selecting **Copy** from the context menu.
3. Right-click the element you want to paste the formatting to, then press Ctrl Shift V, or right-click the target element and select **Paste Formatting** from the context menu.

## Morph an element

Any data-driven element can be transformed into another type of data-driven element.

For instance, if you created and configured a date field and you later realize that it actually needs to be a number field, you can easily change the element type with the morph feature by following this process:

1. Select the element you want to morph.
2. Go to the **Format** menu, then select the **Morph** sub-menu.
3. In the **Morph** sub-menu, select the element type you would like to change to.

The element type should now be changed to the one you selected.

## Implement row banding

Sometimes report data can be difficult to read from left to right, especially if there is not much space between rows. Report Designer has a row banding property that allows you to add alternately colored backgrounds to each row.

Follow the process below to implement row banding:

1. In the **Data** pane, click on **Add Function**.

   The Add Function window will appear.
2. Double-click the **Report function** category, then select **Row Banding**, then click **OK**.

   A **Row Banding** function will appear in your **Data** tab.
3. Select the new **Row Banding** function in the **Functions** section.
4. In the **Properties** pane, select colors for the **Active Banding Color** and **Inactive Banding Color** properties, and set any other options according to your preference.

Row banding is now implemented for each distinct rendered line in your **Details** band. Row banding makes it easier to read reports, but if you need to go one step further, you can override it with conditional formatting.
