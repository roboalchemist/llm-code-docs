# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-workloads-snowflake-notebook.md

# Run Spark workloads from Snowflake Notebooks

You can run Spark workloads interactively from Snowflake Notebooks without needing to manage a Spark cluster. The workloads run on the
Snowflake infrastructure.

To use Snowflake Notebooks as a client for developing Spark workloads to run on Snowflake:

1. Launch Snowflake Notebooks.
2. Within the notebook, start a Spark session.
3. Write PySpark code to load, transform, and analyze data—such as to filter high-value customer orders or
   aggregate revenue.

## Use a Snowflake Notebook that runs on a warehouse

For more information about Snowflake Notebooks, see [Create a notebook](../../user-guide/ui-snowsight/notebooks-create.md).

1. Create a Snowflake Notebook by completing the following steps:

   1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
   2. At the top of the navigation menu, select  (Create) » Notebook » New Notebook.
   3. In the Create notebook dialog, enter a name, database, and schema for the new notebook.

      For more information, see [Create a notebook](../../user-guide/ui-snowsight/notebooks-create.md).
   4. For Runtime, select Run on warehouse.
   5. For Runtime version, select Snowflake Warehouse Runtime 2.0.

      When you select version 2.0, you ensure that you have the dependency support you need, including Python 3.10. For more information,
      see [Notebook runtimes](../../user-guide/ui-snowsight/notebooks.md).
   6. For Query warehouse and Notebook warehouse, select warehouses for running query code and kernel and Python code,
      as described in [Create a notebook](../../user-guide/ui-snowsight/notebooks-create.md).
   7. Select Create.
   8. In the notebook you created, under Packages, ensure that you have the following packages listed to support code in your
      notebook:

      * Python, version 3.10 or later
      * snowpark-connect, latest version

        If you need to add these packages, use the following steps:

        1. Under Anaconda Packages, type the packages name in the search box.
        2. Select the package name.
        3. Select Save.
2. To connect to the Snowpark Connect for Spark server and test the connection, copy the following code and paste it in the Python cell of the
   notebook you created:

   ```python
   from snowflake import snowpark_connect

   spark = snowpark_connect.init_spark_session()
   df = spark.sql("show schemas").limit(10)
   df.show()
   ```

## Use a Snowflake Notebook that runs in a workspace

[Preview Feature](../../release-notes/preview-features.md) — Open

Available to all AWS and Azure accounts. PrivateLink is not supported.

For more information about Snowflake Notebooks in Workspaces, see [Snowflake Notebooks in Workspaces](../../user-guide/ui-snowsight/notebooks-in-workspaces/notebooks-in-workspaces-overview.md).

1. Create a PyPI external access integration.

   You must use the ACCOUNTADMIN role and have a database you can access.

   Run the following commands from a SQL file in a workspace.

   ```sqlexample
   USE DATABASE mydb;
   USE ROLE accountadmin;

   CREATE OR REPLACE NETWORK RULE pypi_network_rule
   MODE = EGRESS
   TYPE = HOST_PORT
   VALUE_LIST = ('pypi.org', 'pypi.python.org', 'pythonhosted.org', 'files.pythonhosted.org');

   CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION pypi_access_integration
   ALLOWED_NETWORK_RULES = (pypi_network_rule)
   ENABLED = true;
   ```

2. Enable PyPI integration in a notebook.

   1. In the notebook, for Service name, select a service.
   2. For External access integrations, select the PyPI integration you created.
   3. For Python version, select Python 3.11.
   4. Select Create.
3. Install the `snowpark_connect` package from PyPI in the notebook, using code such as the following:

   ```bash
   pip install snowpark-connect[jdk]
   ```

4. Restart the kernel.

   * From the Connect button, select Restart kernel.
5. Start the `snowpark_connect` server using code such as the following:

   ```python
   import snowflake.snowpark_connect

   spark = snowflake.snowpark_connect.init_spark_session()
   ```

6. Run your Spark code, as shown in the following example:

   ```python
   from pyspark.sql.connect.functions import *
   from pyspark.sql.connect.types import *
   from pyspark.sql import Row

   # Sample nested data
   data = [(1, ("Alice", 30))]
   schema = "id INT, info STRUCT<name:STRING, age:INT>"

   df = spark.createDataFrame(data, schema=schema)
   df.show()

   spark.sql("show databases").show()
   ```
