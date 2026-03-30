# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/spark-sql-catalyst-errors-using-merge-or-group-by-steps-ael-troubleshooting.md

# Spark SQL catalyst errors using the Merge or Group By steps

If you are using the Spark engine with the Merge Rows (diff), Merge Join, or Group By step, you might receive an error similar to the following message:

```
org.apache.spark.sql.catalyst.analysis.package$AnalysisErrorAt.failAnalysis(package.scala:42)
org.apache.spark.sql.catalyst.analysis.Analyzer.checkAnalysis(Analyzer.scala:91)

```

Field names for join keys (values to compare or group) cannot contain special characters, such as whitespaces or dashes.

To resolve the issue, remove the special characters from the field names within your transformation.
