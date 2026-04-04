# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-overview.md

# Run Apache Spark™ workloads on Snowflake with Snowpark Connect for Spark

With Snowpark Connect for Apache Spark™, you can connect your existing Spark workloads directly to Snowflake and run them on the Snowflake compute engine.
Snowpark Connect for Spark supports using the [Spark DataFrame API](https://spark.apache.org/docs/latest/sql-programming-guide.html) on Snowflake.
All workloads run on Snowflake warehouse. As a result, you can run your PySpark dataframe code with all the benefits of the
Snowflake engine.

In Apache Spark™ version 3.4, the Apache Spark community introduced Spark Connect. Its decoupled client-server architecture separates
the user’s code from the Spark cluster where the work is done. This new architecture makes it possible for Snowflake to power Spark jobs.

You can develop using familiar client tools.

Snowpark Connect for Spark offers the following benefits:

* Decouples client and server, so that Spark code can run remotely against the Snowflake compute engine without your needing to manage a
  Spark cluster.
* Lets team use their existing ecosystem to author and orchestrate their Spark workloads—for example, Jupyter notebooks, VS code,
  and Airflow.
* Allows you to reuse open source Spark dataframes and Spark SQL code with minimal migrations or changes.
* Offers a streamlined way to integrate Snowflake governance, security, and scalability into Spark-based workflows, supporting a familiar
  PySpark experience with pushdown optimizations into Snowflake.
* Allows you to use any of several languages, including PySpark and Spark SQL.

## Get started with Snowpark Connect for Spark

To get started with Snowpark Connect for Spark, follow these steps:

1. [Set up the client tool](snowpark-connect-clients.md) that you’ll use to develop Spark
   workloads to run on Snowflake.

   For example, you can use [Snowflake Notebooks](snowpark-connect-workloads-snowflake-notebook.md)
   or [another tool](snowpark-connect-workloads-jupyter.md).
2. Run Spark workloads asynchronously using Snowpark Submit.

   For more information, see [Submitting Spark applications](snowpark-submit.md).
3. Get to know Snowpark Connect for Spark support for Spark particulars.

   For more information, see [Snowpark Connect for Spark compatibility guide](snowpark-connect-compatibility.md).

## Develop and run Spark workloads on Snowflake

You can use familiar development tools to develop Spark workloads that run on Snowflake, and then run those workloads in batches by
using the Snowpark Submit command-line tool. For more information on which development clients are supported and how to use them, see [Development clients for Snowpark Connect for Spark](snowpark-connect-clients.md).

* For interactive development, use tools such as Snowflake Notebooks or VS Code to develop Spark workloads. You can authenticate with Snowflake,
  start a Spark session, and run PySpark code to load, transform, and analyze data. For more information, see [Development clients for Snowpark Connect for Spark](snowpark-connect-clients.md).
* For non-interactive batch workloads, you can run asynchronous Spark workloads directly on Snowflake’s infrastructure while using familiar Spark semantics. Use Snowpark Submit to submit production-ready Spark applications using a
  simple CLI interface and using your tools, including Airflow. For more information, see [Submitting Spark applications](snowpark-submit.md).
