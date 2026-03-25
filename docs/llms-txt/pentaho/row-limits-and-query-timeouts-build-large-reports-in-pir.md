# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/build-large-reports/row-limits-and-query-timeouts-build-large-reports-in-pir.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-interactive-reports-cp/build-large-reports/row-limits-and-query-timeouts-build-large-reports-in-pir.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/build-large-reports/row-limits-and-query-timeouts-build-large-reports-in-pir.md

# Row limits and query timeouts

You can limit the number of rows that are displayed in your report during your design process in Interactive Reports by setting the **Row Limit** options in the **Interactive Toolbar**. You can also limit the number of seconds a query runs before a timeout occurs by selecting**Query Timeout** and specifying the number of seconds in the Query Settings dialog box. Imposing row limits and time-outs on queries is important to avoid out-of-memory errors, or processes that consume too many resources on the database server.

If you have exceeded the system maximum of rows, a help message appears to guide you.

![Interactive Report Row Limit Reached message](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-140bf2a64862c960dace1683530b77574ffaa024%2FPUC_PIR_Row_Limit_Reached.png?alt=media)

To define the system maximum row limit for your Interactive Reports, ask your system administrator to review the **Administer Pentaho Data Integration and Analytics** document for further information.
