# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/set-analyzer-report-options/turn-on-drill-through-links.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/set-analyzer-report-options/turn-on-drill-through-links.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/set-analyzer-report-options/turn-on-drill-through-links.md

# Turn on drill-through links

You can use drill-through links in Analyzer to view all individual records that make up an aggregate value in your report. Turning on drill-through links turns all non-calculated number fields into links which, when clicked, bring up a configurable data grid that enables you to quickly view more details for that data point, without having to reconfigure your report. The drill-through grid shows all levels and non-calculated measures that are defined in the report cube by default.

If needed, you can select the columns you want to show in the grid so that report designers only see the selected columns. This is useful if your report cube contains many levels and measures and you want to show only specific data for analysis.

Drill-through links are not available under the following conditions:

* Any calculated measures, including schema-defined calculated measures and user-defined measures, such as percentages, running sum, and trend measures.
* Measures and levels set as hidden in the **Available Fields** list will not be visible in the **Drill-Through** view. For more information, see [Hide or Unhide Fields](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/hide-and-unhide-fields).
* Subtotaled cells.

Follow the directions below to turn on drill-through linking in the Report Options dialog box.

1. In the **Cell drill-through** section, select the **Drill-through links on measures** check box.

   The number fields in your report will turn into links.
2. Click the **Select drill-through columns** to select the columns you want to appear.
3. Click **OK**.

   The measure fields in your report will turn into links.

You now have drill-through links for numeric, non-calculated members.

If you choose, you can later disable the drill-through links by clearing the **Drill-through links** check box.
