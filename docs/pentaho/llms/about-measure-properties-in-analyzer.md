# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-measures/about-measure-properties-in-analyzer.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-measures/about-measure-properties-in-analyzer.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-measures/about-measure-properties-in-analyzer.md

# About measure properties in Analyzer

You can update the properties on base measures and calculated measures within Analyzer. For example, you may want to rename 'QTY' to 'Quantity,' change the aggregation method from a sum to an average, or adjust the MDX formula on a calculated measure. When you make and save such a change to a measure, you are making a change to the data source which will affect all users who are creating reports based on that data source. In addition, when you save your report after making inline modeling changes, the **Undo** and **Redo** buttons are unavailable. Therefore, it is recommended that you complete all your inline modeling changes, including 'undoing' or 'redoing' those changes, prior to saving the report.

While most users can view the properties of a measure in Analyzer, select users can edit some of these properties. To edit, you must be assigned the **Manage Data Sources** operation permission in Users and Roles. For more information on setting and maintaining permissions and roles for users, see [Use Pentaho Security](https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/administration/manage-users-and-roles-in-puc).

You can only update the properties for base measures and for calculated measures which were added to the data source in Analyzer. However, you can only edit the **Display Name** for calculated measures created in PDI and published to Analyzer. To change additional properties, you will need to edit the calculated measure in PDI. See **Pentaho Data Integration** for more information.

You can use hidden fields to update calculated measure formulas. When you select the **Show Hidden Fields** option in the **View** menu for the **Available Fields** list, measures set as 'hidden' are available for selection in the Calculated Measure Properties dialog box. To view hidden measures, you need the **Manage Data Source** permission. See [Hide and Unhide Fields](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/hide-and-unhide-fields) for additional details.
