# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/join-tuning-options-spark.md

# Join tuning options

Use the broadcast join tuning option instead of the hash join to optimize join queries when the size of one side of the data is below a specific threshold. Customizing your broadcast join can efficiently join a large table with small tables, such as a fact table with a dimensions table, which can reduce the amount of data sent over the network.

| Option                      | Description                                                                                                                                                                                                                                     | Value type | Example value |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------- |
| **join.broadcast.stepName** | Marks a DataFrame as small enough for use in broadcast joins. See the [Spark API documentation](https://spark.apache.org/docs/2.3.0/api/java/org/apache/spark/sql/functions.html#broadcast-org.apache.spark.sql.Dataset-) for more information. | String     | stepName      |
