# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-fields/troubleshooting-your-report-does-not-display-data.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/troubleshooting-your-report-does-not-display-data.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/troubleshooting-your-report-does-not-display-data.md

# Troubleshooting: Your report does not display data

In some situations, your report might not display any data. The table below outlines the most likely scenarios and their solutions.

| What you did                                                         | What happened              | Likely Reason                                                                                                                  | Example                                                                               | Solution                                                                                                 |
| -------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| You added or modified a filter                                       | The report returned blank. | The filter(s) you added are too restrictive.                                                                                   | Your filter only includes the year '1997' but you have sales revenue only for '2005'. | Change your filters or change the report options to show rows or columns where the number cell is blank. |
| You added a new number field.                                        | The report returned blank. | There are no values for the number field(s) that in the report.                                                                | You added the "Quota" field but you have not yet loaded any Quota data into Pentaho.  | Contact your administrator to: 1) get data loaded into this field OR 2) hide this field.                 |
| You added a new text field. You have no number fields on the report. | The report returned blank. | You have two or more text fields on the report but in some cases Pentaho Analyzer needs a number field to tie it all together. | You have Account Name and Order Status on the report                                  | Add a number field.                                                                                      |
