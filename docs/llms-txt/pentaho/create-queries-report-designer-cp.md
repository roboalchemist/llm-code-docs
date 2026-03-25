# Source: https://docs.pentaho.com/pba-report-designer/create-queries-report-designer-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-queries-report-designer-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp.md

# Create queries

After [connecting to most data sources](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp), a query needs to be created and assigned a name to retrieve your data. This named query can be assigned to retrieve data for the master report, sub report, or parameter selections. A JDBC data source is used to access data from relational databases using the SQL query language. Pentaho also provides two data modeling layers, Pentaho Metadata Editor and Pentaho Analyzer. The Pentaho metadata layer focuses on reporting. The other layer focuses on analysis (OLAP). Pentaho metadata relies on Pentaho’s MQL query language where Pentaho Analyzer uses Microsoft Multidimensional Expression (MDX) query language.

**Note:** The default setting for the query is to pull from session-based cache. If you do not want your query to use session-based cache, go to the **Master Report** tab then the **Attributes** tab to change the **data-cache** field to **False** so that every time the query is run or the report opens, the query will refresh.

For instructions on creating queries, see the following topics:

* [Create queries with SQL Query Designer](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/create-queries-with-sql-query-designer-create-queries-in-prd)
* [Create queries with Metadata Query Editor](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/create-queries-with-metadata-query-editor-create-queries-in-prd)
* [Create MDX queries](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/create-mdx-queries-create-report-designer-queries)
* [Dynamic query scripting](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/dynamic-query-scripting)
* [Hadoop Hive-specific SQL limitations](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/hadoop-hive-specific-sql-limitations)
