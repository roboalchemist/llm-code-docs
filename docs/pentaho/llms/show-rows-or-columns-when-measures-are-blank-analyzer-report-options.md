# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/show-rows-or-columns-when-measures-are-blank-analyzer-report-options.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/show-rows-or-columns-when-measures-are-blank-analyzer-report-options.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/set-analyzer-report-options/working-with-rows-where-the-number-cell-is-blank-analyzer-report-options/show-rows-or-columns-when-measures-are-blank-analyzer-report-options.md

# Show rows or columns when measures are blank

Analyzer hides rows and columns when all measures in the row or column are blank. This default behavior results in the best performance because only combinations of text fields with measure data show on the report.

If you have rows or columns where there is no measure data, but there is calculated measure data (for example, 'YTD Sales for a Month' when no sales are recorded for the month), you can choose to show rows or columns with measure and calculated measure data. You can also select to show all columns and rows for blank measures. Because the latter option allows you to show all combinations of text fields regardless if those field have data or not, you may want to limit the number of fields on the report when using this option.

* To modify when to show rows or columns when all measures in the row or column are blank, select an option in the **Show rows or columns with** field. The options are described below.

| Option                                  | Description                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Measure data**                        | Returns attribute combinations of fields with measure data that is defined by having a relationship in the database. This option is most frequently used.                                                                                                                                                                                              |
| **Measure and calculated measure data** | Returns **Measure data** attribute combinations and additional combinations that are the result of MDX calculations. This option should only be used with the **Measure data** option.                                                                                                                                                                 |
| **Show all even blank measures**        | Returns attribute combinations as a Cartesian join so that you can see combinations even if they have no data at all. Use this option when you want to verify that your dimensions have new data, but there is no corresponding fact data yet. For example, showing **Product Line** and **Sales Territory** combinations even if there were no sales. |

\*\*Note:\*\* If the option is set to \*\*Measure and Calculated Measure data\*\* or \*\*Show all even blank measures\*\*, cross-joins are computed in-memory and the amount of processing goes up significantly. Additionally, changing the report options prompts a warning message about performance.

![](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-ae755f96edb7373a78620347bae2d843edb3f5b9%2FOption%20changes.png?alt=media)

This property can be enabled or disabled by your administrator. For more information on this customization, see the **Administer Pentaho Data Integration and Analytics** document for details.
