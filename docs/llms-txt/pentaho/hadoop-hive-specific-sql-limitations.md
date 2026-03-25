# Source: https://docs.pentaho.com/pba-report-designer/create-queries-report-designer-cp/hadoop-hive-specific-sql-limitations.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-queries-report-designer-cp/hadoop-hive-specific-sql-limitations.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/hadoop-hive-specific-sql-limitations.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/hadoop-hive-specific-sql-limitations.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/hadoop-hive-specific-sql-limitations.md

# Hadoop Hive-specific SQL limitations

There are a few key limitations in Hive that prevent some regular Metadata Editor features from working as intended, and limit the structure of your SQL queries in Report Designer:

* Outer joins are not supported.
* Each column can only be used once in a `SELECT` clause. Duplicate columns in `SELECT` statements cause errors.
* Conditional joins can only use the = conditional unless you use a `WHERE` clause. Any non-equal conditional in a `FROM` statement forces the Metadata Editor to use a cartesian join and a `WHERE` clause conditional to limit it. This is not much of a limitation, but it may seem unusual to experienced Metadata Editor users who are accustomed to working with SQL databases.
* `INSERT` statements have a specific syntax and some limitations. Hive 0.14 supports insert statements with a specific syntax: `INSERT INTO TABLE tablename [PARTITION (partcol1[=val1], partcol2[=val2] ...)] VALUES values_row [, values_row ...]`. There are also some limitations surrounding use of the `INSERT` statement with the `SORTED` BY clause, non-support of literals for complex types, and the insertion of values into columns. For more details see:
  * <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DML>
  * <https://cwiki.apache.org/confluence/display/Hive/Hive+Transactions>
